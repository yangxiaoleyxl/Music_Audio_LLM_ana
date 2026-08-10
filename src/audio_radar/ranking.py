from __future__ import annotations

import re
import unicodedata
from typing import Dict, Iterable, List, Tuple

from .models import Paper


def normalize_title(title: str) -> str:
    value = unicodedata.normalize("NFKD", title).lower()
    return re.sub(r"[^a-z0-9]+", "", value)


def canonical_key(paper: Paper) -> str:
    if paper.doi:
        return "doi:" + paper.doi.lower().replace("https://doi.org/", "")
    if paper.source_id and re.fullmatch(r"\d{4}\.\d{4,5}", paper.source_id):
        return "arxiv:" + paper.source_id
    return "title:" + normalize_title(paper.title)


def _merge_text(preferred: str, candidate: str) -> str:
    return candidate if len(candidate or "") > len(preferred or "") else preferred


def deduplicate(papers: Iterable[Paper]) -> List[Paper]:
    merged: Dict[str, Paper] = {}
    title_to_key: Dict[str, str] = {}
    for paper in papers:
        title_key = normalize_title(paper.title)
        key = canonical_key(paper)
        existing_key = title_to_key.get(title_key, key)
        if existing_key not in merged:
            merged[existing_key] = paper
            title_to_key[title_key] = existing_key
            continue
        existing = merged[existing_key]
        existing.abstract = _merge_text(existing.abstract, paper.abstract)
        existing.pdf_url = existing.pdf_url or paper.pdf_url
        existing.doi = existing.doi or paper.doi
        existing.venue = existing.venue or paper.venue
        existing.authors = existing.authors or paper.authors
        existing.categories = sorted(set(existing.categories + paper.categories))
        existing.code_urls = sorted(set(existing.code_urls + paper.code_urls))
        existing.sources = sorted(set(existing.sources + paper.sources + [paper.source]))
        if existing.source != "arxiv" and paper.source == "arxiv":
            existing.url = paper.url
            existing.source_id = paper.source_id
            existing.source = "arxiv"
    return list(merged.values())


def score_paper(paper: Paper, config: dict) -> Paper:
    title = paper.title.lower()
    abstract = paper.abstract.lower()
    combined = title + " " + abstract
    if any(term.lower() in combined for term in config.get("negative_keywords", [])):
        paper.score = -100
        paper.reasons = ["命中排除词"]
        return paper

    topic_scores: Dict[str, int] = {}
    reasons: List[Tuple[int, str]] = []
    topic_names: List[str] = []
    for topic in config["topics"]:
        topic_score = 0
        matches: List[str] = []
        for phrase, weight in topic["keywords"].items():
            phrase_lower = phrase.lower()
            if phrase_lower in title:
                topic_score += int(weight) * 2
                matches.append(phrase)
            elif phrase_lower in abstract:
                topic_score += int(weight)
                matches.append(phrase)
        if topic_score:
            topic_scores[topic["id"]] = topic_score
            topic_names.append(topic["name"])
            reasons.append((topic_score, "{}：{}".format(topic["name"], "、".join(matches[:3]))))

    paper.topic_scores = topic_scores
    paper.matched_topics = topic_names
    paper.score = sum(sorted(topic_scores.values(), reverse=True)[:2])
    if paper.code_urls:
        paper.score += 2
        reasons.append((2, "提供开源代码链接"))
    if len(paper.sources) > 1:
        paper.score += 1
        reasons.append((1, "被多个学术来源同时收录"))
    paper.reasons = [text for _, text in sorted(reasons, reverse=True)[:4]]
    return paper


def rank(papers: Iterable[Paper], config: dict) -> List[Paper]:
    minimum = int(config.get("minimum_score", 1))
    relevant = [score_paper(paper, config) for paper in papers]
    relevant = [paper for paper in relevant if paper.score >= minimum]
    return sorted(relevant, key=lambda paper: (paper.score, paper.published, paper.title), reverse=True)

