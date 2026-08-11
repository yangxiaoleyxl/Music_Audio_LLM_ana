from __future__ import annotations

import datetime as dt
import json
import shutil
from collections import Counter
from pathlib import Path
from typing import Dict, Iterable, List

from .models import HubModel, Paper


def _escape(value: str) -> str:
    return (value or "").replace("|", "\\|")


def _summary(abstract: str, limit: int = 420) -> str:
    value = " ".join((abstract or "No abstract").split())
    if len(value) <= limit:
        return value
    cut = value[:limit].rsplit(" ", 1)[0]
    return cut + "…"


def markdown_report(
    config: dict,
    papers: List[Paper],
    run_date: dt.date,
    start_date: dt.date,
    source_counts: Dict[str, int],
    errors: List[str],
    total_relevant: int,
    models: List[HubModel],
    total_relevant_models: int,
    raw_model_count: int,
) -> str:
    topic_counts = Counter(topic for paper in papers for topic in paper.matched_topics)
    lines = [
        "# {} — {}".format(config["radar_name"], run_date.isoformat()),
        "",
        "> Lookback window: {} to {} · New papers: {} · New models: {} · relevant papers/models in window: {}/{} · raw papers/models: {}/{}".format(
            start_date.isoformat(), run_date.isoformat(), len(papers), len(models), total_relevant,
            total_relevant_models,
            sum(source_counts.values()),
            raw_model_count,
        ),
        "",
        "Sources: " + " · ".join("{}={}".format(name, count) for name, count in source_counts.items())
        + " · huggingface_models={}".format(raw_model_count),
        "",
    ]
    if errors:
        lines.extend(["## Source notes", ""] + ["- " + error for error in errors] + [""])

    if not papers and not models:
        lines.extend([
            "## No new highly relevant papers today",
            "",
            "This usually means every hit in the lookback window already appeared in an earlier digest; use `--include-seen` to list all relevant items in the window.",
            "",
        ])
        return "\n".join(lines)

    if models:
        lines.extend([
            "## Hugging Face model signals",
            "",
            "> Activity is not research quality; downloads/likes are adoption signals only — model cards, licenses, benchmarks, and linked papers still need manual review.",
            "",
            "| # | Model family | Updated | Task | Score | Variants | Downloads | Likes | License |",
            "|---:|---|---|---|---:|---:|---:|---:|---|",
        ])
        for index, model in enumerate(models, 1):
            lines.append(
                "| {} | [{}]({}) | {} | {} | {} | {} | {} | {} | {} |".format(
                    index, _escape(model.repo_id), model.url, model.last_modified,
                    _escape(model.pipeline_tag or "—"), model.score, 1 + len(model.variants), model.downloads,
                    model.likes, _escape(model.license),
                )
            )
        lines.extend(["", "### Model cards", ""])
        for index, model in enumerate(models, 1):
            paper_links = " · ".join(
                "[arXiv:{}](https://arxiv.org/abs/{})".format(arxiv_id, arxiv_id)
                for arxiv_id in model.arxiv_ids
            ) or "—"
            lines.extend([
                "#### M{}. {}".format(index, model.repo_id),
                "",
                "- **Created / updated**: {} / {}".format(model.created_at or "unknown", model.last_modified),
                "- **Task / library**: {} / {}".format(model.pipeline_tag or "unknown", model.library_name or "unknown"),
                "- **Relevance**: {} pts · {}".format(model.score, "; ".join(model.reasons)),
                "- **Adoption signals**: downloads={} · likes={} · trending={}".format(
                    model.downloads, model.likes, model.trending_score
                ),
                "- **License / access**: {} / {}".format(model.license, "gated" if model.gated else "public"),
                "- **Related papers**: {}".format(paper_links),
                "- **Datasets / base models**: {} / {}".format(
                    ", ".join(model.datasets[:5]) or "unknown", ", ".join(model.base_models[:5]) or "unknown"
                ),
                "- **Variants in family**: {}".format(", ".join(model.variants[:10]) or "—"),
                "",
            ])

    if not papers:
        lines.extend(["## No new highly relevant papers today", "", "Model signals are above; no new relevant papers in the window.", ""])
        return "\n".join(lines)

    lines.extend(["## Research signals", ""])
    for name, count in topic_counts.most_common():
        lines.append("- {}: {} papers".format(name, count))
    lines.extend(["", "## Quick scan", "", "| # | Paper | Date | Score | Topics | Code |", "|---:|---|---|---:|---|---|"])
    for index, paper in enumerate(papers, 1):
        code = "[repo]({})".format(paper.code_urls[0]) if paper.code_urls else "—"
        lines.append(
            "| {} | [{}]({}) | {} | {} | {} | {} |".format(
                index, _escape(paper.title), paper.url, paper.published, paper.score,
                _escape(", ".join(paper.matched_topics)), code,
            )
        )

    lines.extend(["", "## Paper cards", ""])
    for index, paper in enumerate(papers, 1):
        authors = ", ".join(paper.authors[:8])
        if len(paper.authors) > 8:
            authors += " et al."
        links = ["[Paper]({})".format(paper.url)]
        if paper.pdf_url:
            links.append("[PDF]({})".format(paper.pdf_url))
        links.extend("[Code {}]({})".format(i + 1, url) for i, url in enumerate(paper.code_urls))
        lines.extend([
            "### {}. {}".format(index, paper.title),
            "",
            "- **Authors**: {}".format(authors or "unknown"),
            "- **Date / sources**: {} · {}".format(paper.published, ", ".join(paper.sources)),
            "- **Relevance**: {} pts · {}".format(paper.score, "; ".join(paper.reasons)),
            "- **Links**: " + " · ".join(links),
            "",
            _summary(paper.abstract),
            "",
            "**Reading notes** (method / data / metrics / reproducibility / transferability): _TODO_",
            "",
        ])
    return "\n".join(lines)


def write_reports(
    output_dir: Path,
    config: dict,
    papers: List[Paper],
    run_date: dt.date,
    start_date: dt.date,
    source_counts: Dict[str, int],
    errors: List[str],
    total_relevant: int,
    models: List[HubModel],
    total_relevant_models: int,
    raw_model_count: int,
) -> Path:
    output_dir.mkdir(parents=True, exist_ok=True)
    dated_markdown = output_dir / (run_date.isoformat() + ".md")
    content = markdown_report(
        config, papers, run_date, start_date, source_counts, errors, total_relevant,
        models, total_relevant_models, raw_model_count,
    )
    dated_markdown.write_text(content, encoding="utf-8")
    shutil.copyfile(str(dated_markdown), str(output_dir / "latest.md"))
    payload = {
        "generated_at": run_date.isoformat(),
        "window_start": start_date.isoformat(),
        "source_counts": source_counts,
        "errors": errors,
        "papers": [paper.to_dict() for paper in papers],
        "models": [model.to_dict() for model in models],
    }
    (output_dir / (run_date.isoformat() + ".json")).write_text(
        json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    return dated_markdown
