from __future__ import annotations

import argparse
import datetime as dt
import json
import sys
from pathlib import Path

from .huggingface import collapse_model_variants, fetch_huggingface_models, rank_hub_models
from .ranking import canonical_key, deduplicate, rank
from .report import write_reports
from .sources import fetch_all
from .storage import RadarStore


def parse_args(argv=None):
    parser = argparse.ArgumentParser(description="音乐/音频大模型每日论文雷达")
    parser.add_argument("--config", type=Path, default=Path("config/topics.json"))
    parser.add_argument("--database", type=Path, default=Path("data/radar.db"))
    parser.add_argument("--output", type=Path, default=Path("reports"))
    parser.add_argument("--days", type=int, help="覆盖配置中的回看天数")
    parser.add_argument("--date", help="以 YYYY-MM-DD 作为运行日期，便于复现测试")
    parser.add_argument("--include-seen", action="store_true", help="日报包含已出现过的论文")
    parser.add_argument("--no-write-state", action="store_true", help="不更新 SQLite 状态")
    return parser.parse_args(argv)


def main(argv=None) -> int:
    args = parse_args(argv)
    if not args.config.exists():
        print("配置文件不存在：{}".format(args.config), file=sys.stderr)
        return 2
    config = json.loads(args.config.read_text(encoding="utf-8"))
    run_date = dt.date.fromisoformat(args.date) if args.date else dt.datetime.now().astimezone().date()
    lookback = args.days if args.days is not None else int(config.get("lookback_days", 7))
    if lookback < 1:
        print("--days 必须大于 0", file=sys.stderr)
        return 2
    start_date = run_date - dt.timedelta(days=lookback)

    raw_papers, errors, source_counts = fetch_all(config, start_date, run_date)
    raw_models, model_errors, raw_model_count = fetch_huggingface_models(config, start_date, run_date)
    errors.extend(model_errors)
    unique = deduplicate(raw_papers)
    relevant = rank(unique, config)
    maximum = int(config.get("maximum_daily_papers", 60))
    relevant_models = rank_hub_models(raw_models, config)
    maximum_models = int(config.get("maximum_daily_models", 40))

    store = RadarStore(args.database)
    try:
        seen = store.seen_keys(relevant)
        seen_models = store.unchanged_model_ids(relevant_models)
        for paper in relevant:
            paper.is_new = canonical_key(paper) not in seen
        selected = relevant if args.include_seen else [paper for paper in relevant if paper.is_new]
        selected = selected[:maximum]
        for model in relevant_models:
            model.is_new = model.repo_id not in seen_models
        if not args.no_write_state:
            store.upsert(relevant, run_date)
            store.upsert_models(relevant_models, run_date)
        relevant_model_families = collapse_model_variants(relevant_models)
        selected_models = relevant_model_families if args.include_seen else [
            model for model in relevant_model_families if model.is_new
        ]
        selected_models = selected_models[:maximum_models]
    finally:
        store.close()

    report_path = write_reports(
        args.output, config, selected, run_date, start_date,
        source_counts, errors, len(relevant), selected_models, len(relevant_model_families), raw_model_count,
    )
    print("原始命中 {} 篇，去重后 {} 篇，相关 {} 篇，本期输出 {} 篇。".format(
        len(raw_papers), len(unique), len(relevant), len(selected)
    ))
    print("日报：{}".format(report_path))
    print("Hugging Face 原始模型 {} 个，相关 {} 个（{} 个家族），本期输出 {} 个家族。".format(
        raw_model_count, len(relevant_models), len(relevant_model_families), len(selected_models)
    ))
    if errors:
        print("数据源提示：", file=sys.stderr)
        for error in errors:
            print("- " + error, file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
