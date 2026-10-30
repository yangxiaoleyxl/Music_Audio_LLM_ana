from __future__ import annotations

import json
import os
import urllib.request
from pathlib import Path


def latest_report(reports_dir: Path) -> Path:
    matches = sorted(reports_dir.glob("20*.json"))
    if not matches:
        raise FileNotFoundError("No dated report JSON in {}".format(reports_dir))
    return matches[-1]


def _clip(value: str, limit: int) -> str:
    text = " ".join((value or "").split())
    if len(text) <= limit:
        return text
    return text[: limit - 1].rstrip() + "…"


def build_message(
    data: dict,
    *,
    repo: str,
    report_name: str,
    paper_limit: int = 5,
    model_limit: int = 5,
    include_abstract: bool = False,
) -> str:
    papers = data.get("papers") or []
    models = data.get("models") or []
    errors = data.get("errors") or []
    day = data.get("generated_at") or Path(report_name).stem
    lines = [
        "音频研究雷达 {}".format(day),
        "新论文 {} · 新模型 {}".format(len(papers), len(models)),
        "全文 https://github.com/{}/blob/main/reports/{}".format(repo, report_name),
    ]
    if errors:
        lines.append("源异常: " + _clip(" | ".join(errors), 300))
    lines.extend(["", "论文"])
    if not papers:
        lines.append("- 无")
    for paper in papers[:paper_limit]:
        topics = ", ".join(paper.get("matched_topics") or [])
        lines.append("- {} {} {}".format(paper.get("score", 0), paper.get("title", ""), paper.get("url", "")))
        if topics:
            lines.append("  " + topics)
        if include_abstract:
            abstract = _clip(paper.get("abstract") or "", 180)
            if abstract:
                lines.append("  " + abstract)
    if len(papers) > paper_limit:
        lines.append("- 其余 {} 篇见全文".format(len(papers) - paper_limit))
    lines.extend(["", "模型"])
    if not models:
        lines.append("- 无")
    for model in models[:model_limit]:
        task = model.get("pipeline_tag") or "—"
        lines.append("- {} {} {} {}".format(model.get("score", 0), model.get("repo_id", ""), task, model.get("url", "")))
    if len(models) > model_limit:
        lines.append("- 其余 {} 个见全文".format(len(models) - model_limit))
    message = "\n".join(lines)
    encoded = message.encode("utf-8")
    if len(encoded) <= 18000:
        return message
    return encoded[:18000].decode("utf-8", errors="ignore")


def post_text(webhook: str, text: str) -> dict:
    payload = json.dumps({"msg_type": "text", "content": {"text": text}}, ensure_ascii=False).encode("utf-8")
    request = urllib.request.Request(
        webhook,
        data=payload,
        headers={"Content-Type": "application/json; charset=utf-8"},
        method="POST",
    )
    with urllib.request.urlopen(request, timeout=30) as response:
        result = json.loads(response.read().decode("utf-8"))
    code = result.get("code", result.get("StatusCode"))
    if code not in (0, None):
        raise RuntimeError("Lark rejected the message: {}".format(result))
    return result


def _env_int(name: str, default: int) -> int:
    raw = os.environ.get(name, "").strip()
    if not raw:
        return default
    return int(raw)


def notify_latest(reports_dir: Path, webhook: str, repo: str) -> str:
    path = latest_report(reports_dir)
    data = json.loads(path.read_text(encoding="utf-8"))
    message = build_message(
        data,
        repo=repo,
        report_name=path.with_suffix(".md").name,
        paper_limit=_env_int("LARK_PAPER_LIMIT", 5),
        model_limit=_env_int("LARK_MODEL_LIMIT", 5),
        include_abstract=os.environ.get("LARK_INCLUDE_ABSTRACT", "").strip().lower() == "true",
    )
    post_text(webhook, message)
    return message
