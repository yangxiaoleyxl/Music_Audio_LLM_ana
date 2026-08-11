# Music / Audio Foundation Model Research Radar

A daily incremental monitoring pipeline for research on music, audio, and speech foundation models. It discovers new papers from academic sources and new models / model updates from the Hugging Face Hub, scores them against research topics, records seen items in SQLite for incremental deduplication, and outputs a Markdown daily digest plus machine-readable JSON.

## Run Directly

No third-party dependencies required:

```bash
cd audio-llm-radar
./scripts/run_daily.sh
```

Outputs:

- `reports/latest.md`: the latest daily digest
- `reports/YYYY-MM-DD.md`: archived daily digests
- `reports/YYYY-MM-DD.json`: machine-readable, for dashboards, LLM summarization, or Zotero import
- `data/radar.db`: incremental deduplication state

The first run treats every relevant item in the lookback window as new. Later runs only output newly appeared items. To review the whole window again:

```bash
./scripts/run_daily.sh --include-seen
```

To verify a specific day or temporarily widen the window:

```bash
./scripts/run_daily.sh --date 2026-08-09 --days 14 --include-seen --no-write-state
```

## Current Monitoring Scope

Topics are configured in `config/topics.json`. Defaults:

1. Audio & Speech Language Models
2. Music Foundation Models & Representations
3. Generative Music & Audio
4. Audio Understanding & Reasoning
5. Speech Generation, Recognition & Dialogue
6. Evaluation, Alignment, Safety & Copyright

Each phrase carries a weight: title hits score at twice the weight, abstract hits at the base weight; a paper crossing two topics accumulates the top two topic scores, and papers with GitHub code links or found in multiple sources get small bonuses. `minimum_score` controls the threshold for entering the digest.

## Data Source Design

| Source | Default | Role | Credentials |
|---|---:|---|---|
| arXiv | on | Fastest preprint discovery, the daily entry point | none |
| Semantic Scholar | on | Complements metadata and finds cross-domain papers | API key optional but recommended |
| OpenAlex | off | Adds journal, conference, and open-access info | currently requires API key |
| Hugging Face Models | on | Finds newest/updated models, adoption signals, reproducible assets | token optional |

Copy the environment template to raise rate limits:

```bash
cp .env.example .env
```

A single failing source does not break the digest; errors appear both in the terminal and at the top of the digest so nothing fails silently. Sources only provide recall — the final filter is always the unified local topic scoring.

## Automatic Daily Runs

### GitHub Actions (recommended)

The repo ships `.github/workflows/daily-radar.yml`, which runs daily at 11:30 UTC and commits the digest plus SQLite state back to the repository. Manual triggering is also supported.

Push the whole `audio-llm-radar` directory as the repository root; if it lives as a subdirectory of a larger repo, prefix the workflow commands and `git add` paths accordingly. Add these repository Secrets:

- `SEMANTIC_SCHOLAR_API_KEY`
- `OPENALEX_API_KEY` (only needed when OpenAlex is enabled)
- `OPENALEX_EMAIL`
- `HF_TOKEN` (optional; public models work without it, but it stabilizes rate limits)

### Local cron

Run once manually to confirm the path, then add to `crontab -e`:

```cron
30 7 * * * cd /absolute/path/to/audio-llm-radar && ./scripts/run_daily.sh >> data/cron.log 2>&1
```

cron uses the machine's local timezone and will not run while a laptop is asleep; for long-term monitoring prefer GitHub Actions or a server.

## From "Paper List" to a Research Workflow

Every paper card in the digest reserves a reading-notes slot (method / data / metrics / reproducibility / transferability). A weekly three-tier triage is recommended:

- **P0: reproduce now** — directly relevant to the current problem, code and data available, metrics comparable.
- **P1: enter related work** — method or conclusion matters, but no near-term reproduction.
- **P2: trend signal** — do not read the full text yet; just record direction, team, and task shifts.

The JSON digest keeps full abstracts, topic scores, match reasons, and code links, so any LLM can be attached later for structured summaries (in any language), experiment suggestions, or comparison against your own paper drafts; the raw fetching layer is not tied to any model vendor, which keeps it reproducible and cost-controlled.

## Tests

```bash
PYTHONPATH=src python3 -m unittest discover -s tests -v
```

## Tests
