import unittest

from audio_radar.lark_digest import build_message


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
