from __future__ import annotations

import datetime as dt
import os
import re
import urllib.parse
from concurrent.futures import ThreadPoolExecutor, as_completed
from typing import Dict, List, Tuple

from .models import HubModel
from .net import get_bytes, get_json


def _headers() -> Dict[str, str]:
    token = os.environ.get("HF_TOKEN", "").strip()
    return {"Authorization": "Bearer " + token} if token else {}


def _as_list(value) -> List[str]:
    if not value:
        return []
    return [str(item) for item in value] if isinstance(value, list) else [str(value)]


def _date(value: str) -> str:
    return (value or "")[:10]


def _model_from_item(item: dict) -> HubModel:
    repo_id = item.get("id") or item.get("modelId") or ""
    tags = _as_list(item.get("tags"))
    card = item.get("cardData") or {}
    arxiv_ids = [tag.split(":", 1)[1] for tag in tags if tag.lower().startswith("arxiv:")]
    base_models = _as_list(card.get("base_model") or card.get("base_models"))
    datasets = _as_list(card.get("datasets"))
    return HubModel(
        repo_id=repo_id,
        author=item.get("author") or (repo_id.split("/", 1)[0] if "/" in repo_id else ""),
        created_at=_date(item.get("createdAt") or ""),
        last_modified=_date(item.get("lastModified") or ""),
        pipeline_tag=item.get("pipeline_tag") or card.get("pipeline_tag") or "",
        tags=tags,
        downloads=int(item.get("downloads") or 0),
        likes=int(item.get("likes") or 0),
        trending_score=float(item.get("trendingScore") or 0),
        library_name=item.get("library_name") or card.get("library_name") or "",
        license=str(card.get("license") or "unknown"),
        gated=bool(item.get("gated")),
        url="https://huggingface.co/" + repo_id,
        arxiv_ids=arxiv_ids,
        datasets=datasets,
        base_models=base_models,
    )


def _prefilter_score(model: HubModel, config: dict) -> int:
    text = " ".join([model.repo_id, model.pipeline_tag] + model.tags).lower().replace("-", " ")
    score = 2 if model.pipeline_tag else 0
    for topic in config["topics"]:
        score += max((int(weight) for phrase, weight in topic["keywords"].items()
                      if phrase.lower() in text), default=0)
    return score


def _fetch_readme(model: HubModel) -> str:
    path = urllib.parse.quote(model.repo_id, safe="/")
    url = "https://huggingface.co/{}/raw/main/README.md".format(path)
    try:
        return get_bytes(url, headers=_headers(), timeout=10, attempts=1).decode("utf-8", errors="replace")
    except Exception:
        return ""


def fetch_huggingface_models(
    config: dict, start: dt.date, end: dt.date
) -> Tuple[List[HubModel], List[str], int]:
    source_config = config["sources"].get("huggingface_models", {})
    if not source_config.get("enabled"):
        return [], [], 0

    by_id: Dict[str, HubModel] = {}
    errors: List[str] = []

    def fetch_task(pipeline_tag: str):
        params = urllib.parse.urlencode(
            {
                "pipeline_tag": pipeline_tag,
                "sort": "lastModified",
                "direction": -1,
                "limit": int(source_config.get("max_results_per_task", 60)),
                "full": "true",
                "cardData": "true",
            }
        )
        items = get_json("https://huggingface.co/api/models?" + params, headers=_headers())
        return pipeline_tag, items if isinstance(items, list) else []

    task_tags = source_config.get("pipeline_tags", [])
    with ThreadPoolExecutor(max_workers=4) as executor:
        futures = {executor.submit(fetch_task, tag): tag for tag in task_tags}
        task_results = []
        for future in as_completed(futures):
            try:
                task_results.append(future.result())
            except Exception as exc:
                errors.append("Hugging Face / {}: {}".format(futures[future], exc))

    for _, items in task_results:
        for item in items:
            model = _model_from_item(item)
            try:
                modified = dt.date.fromisoformat(model.last_modified)
            except ValueError:
                continue
            if start <= modified <= end and model.repo_id:
                by_id[model.repo_id] = model

    candidates = sorted(
        by_id.values(),
        key=lambda model: (_prefilter_score(model, config), model.last_modified, model.likes),
        reverse=True,
    )
    readme_limit = int(source_config.get("max_readmes", 50))
    readme_candidates = candidates[:readme_limit]
    with ThreadPoolExecutor(max_workers=8) as executor:
        futures = {executor.submit(_fetch_readme, model): model for model in readme_candidates}
        for future in as_completed(futures):
            futures[future].card_text = future.result()
    return candidates, errors, len(by_id)


def score_hub_model(model: HubModel, config: dict) -> HubModel:
    normalized_pipeline = model.pipeline_tag.lower().replace("-", " ").replace("_", " ")
    strong_tags = [tag for tag in model.tags if tag.lower().replace("-", "_") != model.pipeline_tag.lower().replace("-", "_")]
    metadata = " ".join(
        [model.repo_id, model.library_name] + strong_tags + model.datasets + model.base_models
    ).lower().replace("-", " ").replace("_", " ")
    card_text = re.sub(r"\s+", " ", model.card_text.lower())
    combined = metadata + " " + card_text
    if any(term.lower() in combined for term in config.get("negative_keywords", [])):
        model.score = -100
        model.reasons = ["matched a negative keyword"]
        return model

    topic_scores: Dict[str, int] = {}
    topic_names: List[str] = []
    reasons = []
    for topic in config["topics"]:
        score = 0
        matches = []
        for phrase, weight in topic["keywords"].items():
            phrase_lower = phrase.lower().replace("-", " ").replace("_", " ")
            if phrase_lower in metadata:
                score += int(weight) * 2
                matches.append(phrase)
            elif phrase_lower in card_text:
                score += int(weight)
                matches.append(phrase)
            elif phrase_lower in normalized_pipeline:
                score += max(1, int(weight) // 2)
                matches.append(phrase + " (pipeline tag)")
        if score:
            topic_scores[topic["id"]] = score
            topic_names.append(topic["name"])
            reasons.append((score, "{}: {}".format(topic["name"], ", ".join(matches[:3]))))

    model.topic_scores = topic_scores
    model.matched_topics = topic_names
    model.score = sum(sorted(topic_scores.values(), reverse=True)[:2])
    if model.arxiv_ids:
        model.score += 2
        reasons.append((2, "model card links an arXiv paper"))
    if model.license != "unknown":
        model.score += 1
        reasons.append((1, "declares license {}".format(model.license)))
    if model.likes >= 10:
        model.score += 1
        reasons.append((1, "community likes {}".format(model.likes)))
    model.reasons = [text for _, text in sorted(reasons, reverse=True)[:4]]
    return model


def rank_hub_models(models: List[HubModel], config: dict) -> List[HubModel]:
    minimum = int(config.get("minimum_model_score", 7))
    scored = [score_hub_model(model, config) for model in models]
    scored = [model for model in scored if model.score >= minimum]
    return sorted(
        scored,
        key=lambda model: (model.score, model.last_modified, model.likes, model.downloads),
        reverse=True,
    )


def _family_key(model: HubModel) -> str:
    if model.base_models:
        return "{}|{}|{}".format(
            model.author.lower(), model.pipeline_tag.lower(), ",".join(sorted(model.base_models)).lower()
        )
    name = model.repo_id.split("/", 1)[-1].lower()
    tokens = re.split(r"[-_.]+", name)
    variant_tokens = {
        "bf16", "fp16", "fp32", "int4", "int5", "int8", "gguf", "mlx", "coreml",
        "onnx", "optimized", "quantized", "q4", "q5", "q6", "q8", "awq", "gptq",
    }
    core = [token for token in tokens if token not in variant_tokens and not re.fullmatch(r"i\d+|\d+bit", token)]
    return "{}|{}|{}".format(model.author.lower(), model.pipeline_tag.lower(), "-".join(core))


def collapse_model_variants(models: List[HubModel]) -> List[HubModel]:
    families: Dict[str, HubModel] = {}
    for model in models:
        key = _family_key(model)
        if key not in families:
            families[key] = model
            continue
        representative = families[key]
        representative.variants.append(model.repo_id)
        representative.variants.extend(model.variants)
        representative.downloads += model.downloads
        representative.likes += model.likes
        representative.last_modified = max(representative.last_modified, model.last_modified)
        if model.created_at and (not representative.created_at or model.created_at < representative.created_at):
            representative.created_at = model.created_at
        representative.arxiv_ids = sorted(set(representative.arxiv_ids + model.arxiv_ids))
        representative.datasets = sorted(set(representative.datasets + model.datasets))
        representative.is_new = representative.is_new or model.is_new
    return sorted(
        families.values(),
        key=lambda model: (model.score, model.last_modified, model.likes, model.downloads),
        reverse=True,
    )
