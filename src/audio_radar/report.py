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
    value = " ".join((abstract or "暂无摘要").split())
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
        "> 检索窗口：{} 至 {} · 新论文：{} · 新模型：{} · 窗口内相关论文/模型：{}/{} · 原始论文/模型：{}/{}".format(
            start_date.isoformat(), run_date.isoformat(), len(papers), len(models), total_relevant,
            total_relevant_models,
            sum(source_counts.values()),
            raw_model_count,
        ),
        "",
        "来源：" + " · ".join("{}={}".format(name, count) for name, count in source_counts.items())
        + " · huggingface_models={}".format(raw_model_count),
        "",
    ]
    if errors:
        lines.extend(["## 数据源提示", ""] + ["- " + error for error in errors] + [""])

    if not papers and not models:
        lines.extend([
            "## 今日无新增高相关论文",
            "",
            "这通常表示检索窗口内的命中已在之前日报出现；可用 `--include-seen` 查看窗口内全部相关论文。",
            "",
        ])
        return "\n".join(lines)

    if models:
        lines.extend([
            "## Hugging Face 新模型信号",
            "",
            "> 活跃度不等于研究质量；downloads/likes 只作采用信号，模型卡、许可证、基准和关联论文仍需人工核验。",
            "",
            "| # | 模型家族 | 更新 | 任务 | 分数 | 变体 | Downloads | Likes | License |",
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
        lines.extend(["", "### 模型卡片", ""])
        for index, model in enumerate(models, 1):
            paper_links = " · ".join(
                "[arXiv:{}](https://arxiv.org/abs/{})".format(arxiv_id, arxiv_id)
                for arxiv_id in model.arxiv_ids
            ) or "—"
            lines.extend([
                "#### M{}. {}".format(index, model.repo_id),
                "",
                "- **创建/更新**：{} / {}".format(model.created_at or "未知", model.last_modified),
                "- **任务/库**：{} / {}".format(model.pipeline_tag or "未知", model.library_name or "未知"),
                "- **相关性**：{} 分 · {}".format(model.score, "；".join(model.reasons)),
                "- **采用信号**：downloads={} · likes={} · trending={}".format(
                    model.downloads, model.likes, model.trending_score
                ),
                "- **许可证/访问**：{} / {}".format(model.license, "gated" if model.gated else "公开"),
                "- **关联论文**：{}".format(paper_links),
                "- **数据集/基座**：{} / {}".format(
                    ", ".join(model.datasets[:5]) or "未知", ", ".join(model.base_models[:5]) or "未知"
                ),
                "- **同家族变体**：{}".format(", ".join(model.variants[:10]) or "—"),
                "",
            ])

    if not papers:
        lines.extend(["## 今日无新增高相关论文", "", "模型信号见上；论文窗口内没有新增高相关记录。", ""])
        return "\n".join(lines)

    lines.extend(["## 研究信号", ""])
    for name, count in topic_counts.most_common():
        lines.append("- {}：{} 篇".format(name, count))
    lines.extend(["", "## 快速浏览", "", "| # | 论文 | 日期 | 分数 | 主题 | 代码 |", "|---:|---|---|---:|---|---|"])
    for index, paper in enumerate(papers, 1):
        code = "[repo]({})".format(paper.code_urls[0]) if paper.code_urls else "—"
        lines.append(
            "| {} | [{}]({}) | {} | {} | {} | {} |".format(
                index, _escape(paper.title), paper.url, paper.published, paper.score,
                _escape("、".join(paper.matched_topics)), code,
            )
        )

    lines.extend(["", "## 论文卡片", ""])
    for index, paper in enumerate(papers, 1):
        authors = ", ".join(paper.authors[:8])
        if len(paper.authors) > 8:
            authors += " et al."
        links = ["[论文页]({})".format(paper.url)]
        if paper.pdf_url:
            links.append("[PDF]({})".format(paper.pdf_url))
        links.extend("[Code {}]({})".format(i + 1, url) for i, url in enumerate(paper.code_urls))
        lines.extend([
            "### {}. {}".format(index, paper.title),
            "",
            "- **作者**：{}".format(authors or "未知"),
            "- **日期/来源**：{} · {}".format(paper.published, ", ".join(paper.sources)),
            "- **相关性**：{} 分 · {}".format(paper.score, "；".join(paper.reasons)),
            "- **链接**：" + " · ".join(links),
            "",
            _summary(paper.abstract),
            "",
            "**阅读记录**：方法/数据/指标/可复现性/可迁移点：_待填写_",
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
