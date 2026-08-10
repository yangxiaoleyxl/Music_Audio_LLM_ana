from __future__ import annotations

import datetime as dt
import os
import re
import urllib.parse
import xml.etree.ElementTree as ET
from typing import Dict, Iterable, List, Sequence, Tuple

from .models import Paper
from .net import get_bytes, get_json


GITHUB_URL_RE = re.compile(r"https?://github\.com/[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+", re.I)


def _clean(text: str) -> str:
    return " ".join((text or "").split())


def _github_urls(*texts: str) -> List[str]:
    urls = []
    for text in texts:
        for match in GITHUB_URL_RE.findall(text or ""):
            url = match.rstrip(".,;:)]}")
            if url not in urls:
                urls.append(url)
    return urls


def _topic_phrases(config: dict) -> List[str]:
    phrases: List[str] = []
    for topic in config["topics"]:
        for phrase in topic["keywords"]:
            if phrase not in phrases:
                phrases.append(phrase)
    return phrases


def fetch_arxiv(config: dict, start: dt.date, end: dt.date) -> List[Paper]:
    source_config = config["sources"]["arxiv"]
    phrases = _topic_phrases(config)
    term_query = " OR ".join('all:\"{}\"'.format(p.replace('"', "")) for p in phrases)
    date_range = "submittedDate:[{}0000 TO {}2359]".format(
        start.strftime("%Y%m%d"), end.strftime("%Y%m%d")
    )
    params = urllib.parse.urlencode(
        {
            "search_query": "({}) AND {}".format(term_query, date_range),
            "start": 0,
            "max_results": int(source_config.get("max_results", 300)),
            "sortBy": "submittedDate",
            "sortOrder": "descending",
        }
    )
    payload = get_bytes("https://export.arxiv.org/api/query?" + params)
    root = ET.fromstring(payload)
    atom = "{http://www.w3.org/2005/Atom}"
    arxiv = "{http://arxiv.org/schemas/atom}"
    papers: List[Paper] = []
    for entry in root.findall(atom + "entry"):
        identifier = _clean(entry.findtext(atom + "id")).rsplit("/", 1)[-1]
        base_id = re.sub(r"v\d+$", "", identifier)
        title = _clean(entry.findtext(atom + "title"))
        abstract = _clean(entry.findtext(atom + "summary"))
        comment = _clean(entry.findtext(arxiv + "comment"))
        links = {link.attrib.get("title", link.attrib.get("rel", "")): link.attrib.get("href", "")
                 for link in entry.findall(atom + "link")}
        papers.append(
            Paper(
                source="arxiv",
                source_id=base_id,
                title=title,
                abstract=abstract,
                authors=[_clean(a.findtext(atom + "name")) for a in entry.findall(atom + "author")],
                published=_clean(entry.findtext(atom + "published"))[:10],
                updated=_clean(entry.findtext(atom + "updated"))[:10],
                url="https://arxiv.org/abs/" + base_id,
                pdf_url=links.get("pdf", "https://arxiv.org/pdf/" + base_id),
                doi=_clean(entry.findtext(arxiv + "doi")),
                venue=comment,
                categories=[c.attrib.get("term", "") for c in entry.findall(atom + "category")],
                code_urls=_github_urls(abstract, comment),
                sources=["arxiv"],
            )
        )
    return papers


def _s2_query(topic: dict) -> str:
    phrases = list(topic["keywords"].keys())
    return " | ".join('"{}"'.format(p.replace('"', "")) for p in phrases)


def fetch_semantic_scholar(config: dict, start: dt.date, end: dt.date) -> Tuple[List[Paper], List[str]]:
    source_config = config["sources"]["semantic_scholar"]
    headers: Dict[str, str] = {}
    api_key = os.environ.get("SEMANTIC_SCHOLAR_API_KEY", "").strip()
    if api_key:
        headers["x-api-key"] = api_key
    fields = "paperId,title,abstract,authors,year,publicationDate,url,openAccessPdf,externalIds,venue"
    papers: List[Paper] = []
    errors: List[str] = []
    for topic in config["topics"]:
        params = urllib.parse.urlencode(
            {
                "query": _s2_query(topic),
                "fields": fields,
                "year": "{}-{}".format(start.year, end.year),
                "sort": "publicationDate:desc",
            }
        )
        url = "https://api.semanticscholar.org/graph/v1/paper/search/bulk?" + params
        try:
            response = get_json(url, headers=headers)
        except Exception as exc:  # one topic must not stop the daily run
            errors.append("Semantic Scholar / {}: {}".format(topic["name"], exc))
            continue
        limit = int(source_config.get("max_results_per_topic", 30))
        for item in response.get("data", [])[:limit]:
            published = item.get("publicationDate") or "{}-01-01".format(item.get("year") or end.year)
            try:
                if not (start <= dt.date.fromisoformat(published[:10]) <= end):
                    continue
            except ValueError:
                continue
            external = item.get("externalIds") or {}
            arxiv_id = external.get("ArXiv", "")
            source_id = arxiv_id or item.get("paperId", "")
            abstract = _clean(item.get("abstract") or "")
            pdf = (item.get("openAccessPdf") or {}).get("url", "")
            papers.append(
                Paper(
                    source="semantic_scholar",
                    source_id=source_id,
                    title=_clean(item.get("title") or ""),
                    abstract=abstract,
                    authors=[_clean(a.get("name", "")) for a in item.get("authors", [])],
                    published=published[:10],
                    updated=published[:10],
                    url=("https://arxiv.org/abs/" + arxiv_id) if arxiv_id else item.get("url", ""),
                    pdf_url=pdf,
                    doi=external.get("DOI", ""),
                    venue=_clean(item.get("venue") or ""),
                    code_urls=_github_urls(abstract),
                    sources=["semantic_scholar"],
                )
            )
    return papers, errors


def _rebuild_openalex_abstract(index: dict) -> str:
    if not index:
        return ""
    positions = [(position, word) for word, values in index.items() for position in values]
    return " ".join(word for _, word in sorted(positions))


def fetch_openalex(config: dict, start: dt.date, end: dt.date) -> Tuple[List[Paper], List[str]]:
    api_key = os.environ.get("OPENALEX_API_KEY", "").strip()
    if not api_key:
        return [], ["OpenAlex 已启用，但缺少 OPENALEX_API_KEY，已跳过。"]
    source_config = config["sources"]["openalex"]
    papers: List[Paper] = []
    errors: List[str] = []
    for topic in config["topics"]:
        # One representative search per topic controls API use and duplicate volume.
        query = " OR ".join(list(topic["keywords"].keys())[:5])
        params = {
            "search": query,
            "filter": "from_publication_date:{},to_publication_date:{}".format(start, end),
            "sort": "publication_date:desc",
            "per_page": int(source_config.get("max_results_per_topic", 30)),
            "api_key": api_key,
        }
        email = os.environ.get("OPENALEX_EMAIL", "").strip()
        if email:
            params["mailto"] = email
        try:
            response = get_json("https://api.openalex.org/works?" + urllib.parse.urlencode(params))
        except Exception as exc:
            errors.append("OpenAlex / {}: {}".format(topic["name"], exc))
            continue
        for item in response.get("results", []):
            ids = item.get("ids") or {}
            doi = (ids.get("doi") or "").replace("https://doi.org/", "")
            arxiv_id = ""
            for location in [item.get("primary_location") or {}] + (item.get("locations") or []):
                landing = location.get("landing_page_url") or ""
                match = re.search(r"arxiv\.org/abs/([^/?#]+)", landing)
                if match:
                    arxiv_id = re.sub(r"v\d+$", "", match.group(1))
                    break
            best = item.get("best_oa_location") or item.get("primary_location") or {}
            abstract = _rebuild_openalex_abstract(item.get("abstract_inverted_index") or {})
            papers.append(
                Paper(
                    source="openalex",
                    source_id=arxiv_id or item.get("id", "").rsplit("/", 1)[-1],
                    title=_clean(item.get("display_name") or ""),
                    abstract=abstract,
                    authors=[_clean(a.get("author", {}).get("display_name", ""))
                             for a in item.get("authorships", [])],
                    published=(item.get("publication_date") or "")[:10],
                    updated=(item.get("publication_date") or "")[:10],
                    url=("https://arxiv.org/abs/" + arxiv_id) if arxiv_id else (best.get("landing_page_url") or item.get("id", "")),
                    pdf_url=best.get("pdf_url") or "",
                    doi=doi,
                    venue=_clean((item.get("primary_location") or {}).get("source", {}).get("display_name", "")),
                    code_urls=_github_urls(abstract),
                    sources=["openalex"],
                )
            )
    return papers, errors


def fetch_all(config: dict, start: dt.date, end: dt.date) -> Tuple[List[Paper], List[str], Dict[str, int]]:
    papers: List[Paper] = []
    errors: List[str] = []
    counts: Dict[str, int] = {}

    if config["sources"].get("arxiv", {}).get("enabled"):
        try:
            result = fetch_arxiv(config, start, end)
            papers.extend(result)
            counts["arxiv"] = len(result)
        except Exception as exc:
            errors.append("arXiv: {}".format(exc))
            counts["arxiv"] = 0

    if config["sources"].get("semantic_scholar", {}).get("enabled"):
        result, source_errors = fetch_semantic_scholar(config, start, end)
        papers.extend(result)
        errors.extend(source_errors)
        counts["semantic_scholar"] = len(result)

    if config["sources"].get("openalex", {}).get("enabled"):
        result, source_errors = fetch_openalex(config, start, end)
        papers.extend(result)
        errors.extend(source_errors)
        counts["openalex"] = len(result)

    return papers, errors, counts

