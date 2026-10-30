#!/usr/bin/env python3
"""Send the latest radar digest to a Lark custom-bot webhook."""

from __future__ import annotations

import os
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT / "src"))

from audio_radar.lark_digest import notify_latest


def main() -> int:
    webhook = os.environ.get("LARK_WEBHOOK", "").strip()
    if not webhook:
        print("LARK_WEBHOOK is not set; Lark notification skipped.", file=sys.stderr)
        return 1
    repo = os.environ.get("REPORT_REPO", "yangxiaoleyxl/Music_Audio_LLM_ana").strip()
    message = notify_latest(PROJECT_ROOT / "reports", webhook, repo)
    print(message.splitlines()[0])
    print("Lark notification sent.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
