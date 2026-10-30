"""Turn one radar JSON digest into a Chinese briefing.

The GitHub runner cannot use a local Codex login. When OPENAI_API_KEY is set,
this makes one completion call over the abstracts and model notes already
fetched by the radar. It does not browse, and it does not use Cursor or Codex
desktop quota.
"""

from __future__ import annotations

import json
import os
import urllib.error
import urllib.request
from pathlib import Path


SYSTEM = (
    "你是音乐与音频研究助手。只根据用户给出的材料写中文简报。"
    "不要编造材料里没有的指标、数据或结论。材料不足时写「材料不足」。"
    "论文每篇两到三句：做了什么、方法或数据、和音乐/音频研究的关系，并保留原链接。"
    "模型每个一句：它是什么、任务类型、材料里能看出的底模或许可证，并保留原链接。"
    "按论文、模型两节输出 Markdown。"
)


def _clip(value: str, limit: int) -> str:
    text = " ".join((value or "").split())
    if len(text) <= limit:
        return text
    return text[: limit - 1].rstrip() + "…"


def compact_items(data: dict, paper_limit: int = 60, model_limit: int = 40) -> dict:
    papers = []
    for paper in (data.get("papers") or [])[:paper_limit]:
        papers.append({
            "title": paper.get("title") or "",
            "url": paper.get("url") or "",
            "score": paper.get("score") or 0,
            "topics": paper.get("matched_topics") or [],
            "abstract": _clip(paper.get("abstract") or "", 900),
        })
    models = []
    for model in (data.get("models") or [])[:model_limit]:
        models.append({
            "repo_id": model.get("repo_id") or "",
            "url": model.get("url") or "",
            "score": model.get("score") or 0,
            "task": model.get("pipeline_tag") or "",
            "license": model.get("license") or "",
            "reasons": _clip("; ".join(model.get("reasons") or []), 240),
            "card": _clip(model.get("card_text") or "", 280),
        })
    return {
        "generated_at": data.get("generated_at") or "",
        "errors": data.get("errors") or [],
        "papers": papers,
        "models": models,
    }


def complete(api_key: str, model: str, payload: dict) -> str:
    body = {
        "model": model,
        "messages": [
            {"role": "system", "content": SYSTEM},
            {"role": "user", "content": json.dumps(payload, ensure_ascii=False)},
        ],
    }
    request = urllib.request.Request(
        "https://api.openai.com/v1/chat/completions",
        data=json.dumps(body).encode("utf-8"),
        headers={
            "Authorization": "Bearer {}".format(api_key),
            "Content-Type": "application/json",
        },
        method="POST",
    )
    try:
        with urllib.request.urlopen(request, timeout=120) as response:
            result = json.loads(response.read().decode("utf-8"))
    except urllib.error.HTTPError as exc:
        detail = exc.read().decode("utf-8", errors="replace")[:500]
        raise RuntimeError("OpenAI HTTP {}: {}".format(exc.code, detail)) from exc
    choices = result.get("choices") or []
    if not choices:
        raise RuntimeError("OpenAI response had no choices")
    content = ((choices[0].get("message") or {}).get("content") or "").strip()
    if not content:
        raise RuntimeError("OpenAI response was empty")
    return content


def write_brief(reports_dir: Path, api_key: str, model: str) -> Path:
    matches = sorted(reports_dir.glob("20*.json"))
    if not matches:
        raise FileNotFoundError("No dated report JSON in {}".format(reports_dir))
    source = matches[-1]
    data = json.loads(source.read_text(encoding="utf-8"))
    text = complete(api_key, model, compact_items(data))
    destination = reports_dir / (source.stem + "-brief.md")
    destination.write_text(text + "\n", encoding="utf-8")
    return destination


def model_name() -> str:
    return os.environ.get("OPENAI_BRIEF_MODEL", "").strip() or "gpt-4.1-mini"
