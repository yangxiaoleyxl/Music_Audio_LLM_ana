import unittest

import urllib.error

from audio_radar.briefing import compact_items
from audio_radar.lark_digest import build_message, explain_errors
from audio_radar.net import retry_delay_seconds


def sample():
    return {
        "generated_at": "2026-10-30",
        "errors": ["arXiv: HTTP Error 500"],
        "papers": [
            {
                "score": 20,
                "title": "A Music Language Model",
                "url": "https://arxiv.org/abs/1",
                "matched_topics": ["Music Foundation Models & Representations"],
                "abstract": "We study symbolic music.",
            },
            {
                "score": 8,
                "title": "Speech Dialogue Model",
                "url": "https://arxiv.org/abs/2",
                "matched_topics": ["Speech Generation, Recognition & Dialogue"],
                "abstract": "A long abstract " + ("word " * 80),
            },
        ],
        "models": [
            {
                "score": 12,
                "repo_id": "org/musicgen",
                "pipeline_tag": "text-to-audio",
                "url": "https://huggingface.co/org/musicgen",
            }
        ],
    }


class LarkDigestTests(unittest.TestCase):
    def test_brief_message_keeps_keyword_and_limits(self):
        text = build_message(
            sample(),
            repo="owner/repo",
            report_name="2026-10-30.md",
            paper_limit=1,
            model_limit=1,
        )
        self.assertIn("音频研究雷达 2026-10-30", text)
        self.assertIn("https://github.com/owner/repo/blob/main/reports/2026-10-30.md", text)
        self.assertIn("A Music Language Model", text)
        self.assertNotIn("Speech Dialogue Model", text)
        self.assertIn("其余 1 篇见全文", text)
        self.assertNotIn("We study symbolic music.", text)

    def test_default_limits_keep_every_item_and_translate_source_failures(self):
        text = build_message(sample(), repo="owner/repo", report_name="2026-10-30.md")
        self.assertIn("Speech Dialogue Model", text)
        self.assertIn("org/musicgen", text)
        self.assertNotIn("其余", text)
        self.assertIn("arXiv 没有返回", text)
        self.assertNotIn("HTTP Error 500", text)

    def test_brief_replaces_the_raw_list(self):
        text = build_message(
            sample(),
            repo="owner/repo",
            report_name="2026-10-30.md",
            brief="这篇论文比较了口音评测。",
        )
        self.assertIn("这篇论文比较了口音评测。", text)
        self.assertIn("reports/2026-10-30-brief.md", text)
        self.assertNotIn("org/musicgen", text)

    def test_semantic_scholar_rate_limit_is_named(self):
        text = explain_errors([
            "Semantic Scholar / Audio Understanding & Reasoning: HTTP Error 429: Too Many Requests",
        ])
        self.assertEqual(text, "Semantic Scholar「Audio Understanding & Reasoning」被限流")

    def test_compact_items_clip_long_card_text(self):
        payload = compact_items({
            "generated_at": "2026-10-30",
            "papers": [],
            "models": [{
                "repo_id": "org/musicgen",
                "card_text": "word " * 200,
                "reasons": ["music generation"],
            }],
        })
        self.assertLess(len(payload["models"][0]["card"]), 300)

    def test_retry_waits_on_rate_limit_and_stops_on_not_found(self):
        limited = urllib.error.HTTPError("https://example.test", 429, "Too Many Requests", {}, None)
        missing = urllib.error.HTTPError("https://example.test", 404, "Not Found", {}, None)
        try:
            self.assertEqual(retry_delay_seconds(limited, 0), 8)
            self.assertIsNone(retry_delay_seconds(missing, 0))
            self.assertIsNone(retry_delay_seconds(limited, 4))
        finally:
            limited.close()
            missing.close()

    def test_detailed_message_includes_short_abstract(self):
        text = build_message(
            sample(),
            repo="owner/repo",
            report_name="2026-10-30.md",
            paper_limit=2,
            include_abstract=True,
        )
        self.assertIn("We study symbolic music.", text)
        self.assertLess(len(text.encode("utf-8")), 18000)
