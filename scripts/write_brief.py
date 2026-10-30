#!/usr/bin/env python3
"""Write reports/YYYY-MM-DD-brief.md when OPENAI_API_KEY is configured."""

from __future__ import annotations

import os
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT / "src"))

from audio_radar.briefing import model_name, write_brief


def main() -> int:
    api_key = os.environ.get("OPENAI_API_KEY", "").strip()
    if not api_key:
        print("OPENAI_API_KEY is not set; briefing skipped.")
        return 0
    try:
        path = write_brief(PROJECT_ROOT / "reports", api_key, model_name())
    except Exception as exc:
        print("Briefing skipped: {}".format(exc), file=sys.stderr)
        return 0
    print("Brief written: {}".format(path.name))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
