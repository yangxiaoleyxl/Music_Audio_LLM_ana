import tempfile
import unittest
from pathlib import Path

from audio_radar.huggingface import collapse_model_variants, rank_hub_models
from audio_radar.models import HubModel, Paper
from audio_radar.ranking import canonical_key, deduplicate, rank
from audio_radar.storage import RadarStore


def paper(**overrides):
    values = dict(
        source="arxiv",
        source_id="2608.12345",
        title="A New Audio Large Language Model for Musical Reasoning",
        abstract="We introduce an audio language model for music understanding.",
        authors=["A. Researcher"],
        published="2026-08-08",
        updated="2026-08-08",
        url="https://arxiv.org/abs/2608.12345",
        sources=["arxiv"],
    )
    values.update(overrides)
    return Paper(**values)


CONFIG = {
    "minimum_score": 6,
    "negative_keywords": ["radar signal"],
    "topics": [
        {"id": "alm", "name": "Audio Language Models", "keywords": {"audio large language model": 8}},
        {"id": "music", "name": "Musical Reasoning", "keywords": {"musical reasoning": 6}},
    ],
}


class RankingTests(unittest.TestCase):
    def test_ranking_matches_multiple_topics(self):
        ranked = rank([paper()], CONFIG)
        self.assertEqual(len(ranked), 1)
        self.assertGreaterEqual(ranked[0].score, 20)
        self.assertEqual(len(ranked[0].matched_topics), 2)

    def test_negative_keyword_filters_noise(self):
        noisy = paper(title="Radar Signal Audio Large Language Model")
        self.assertEqual(rank([noisy], CONFIG), [])

    def test_deduplication_merges_sources_and_code(self):
        first = paper()
        second = paper(
            source="semantic_scholar",
            source_id="abc",
            abstract="A much longer abstract for this audio language model and its evaluations.",
            code_urls=["https://github.com/example/model"],
            sources=["semantic_scholar"],
        )
        merged = deduplicate([first, second])
        self.assertEqual(len(merged), 1)
        self.assertEqual(merged[0].sources, ["arxiv", "semantic_scholar"])
        self.assertEqual(len(merged[0].code_urls), 1)


class StorageTests(unittest.TestCase):
    def test_store_tracks_seen_papers(self):
        with tempfile.TemporaryDirectory() as directory:
            store = RadarStore(Path(directory) / "radar.db")
            item = paper()
            self.assertEqual(store.seen_keys([item]), set())
            import datetime as dt
            store.upsert([item], dt.date(2026, 8, 9))
            self.assertEqual(store.seen_keys([item]), {canonical_key(item)})
            store.close()

    def test_store_tracks_huggingface_models(self):
        with tempfile.TemporaryDirectory() as directory:
            store = RadarStore(Path(directory) / "radar.db")
            model = HubModel(
                repo_id="lab/audio-llm", author="lab", created_at="2026-08-08",
                last_modified="2026-08-09", pipeline_tag="audio-text-to-text",
                tags=["audio-language-model"], downloads=12, likes=2, trending_score=0,
                library_name="transformers", license="apache-2.0", gated=False,
                url="https://huggingface.co/lab/audio-llm",
            )
            self.assertEqual(store.unchanged_model_ids([model]), set())
            import datetime as dt
            store.upsert_models([model], dt.date(2026, 8, 9))
            self.assertEqual(store.unchanged_model_ids([model]), {"lab/audio-llm"})
            model.last_modified = "2026-08-10"
            self.assertEqual(store.unchanged_model_ids([model]), set())
            store.close()


class HuggingFaceTests(unittest.TestCase):
    def test_model_metadata_is_ranked(self):
        model = HubModel(
            repo_id="lab/audio-large-language-model", author="lab", created_at="2026-08-08",
            last_modified="2026-08-09", pipeline_tag="audio-text-to-text",
            tags=["arxiv:2608.12345"], downloads=100, likes=11, trending_score=2,
            library_name="transformers", license="apache-2.0", gated=False,
            url="https://huggingface.co/lab/audio-large-language-model",
            arxiv_ids=["2608.12345"],
        )
        ranked = rank_hub_models([model], CONFIG)
        self.assertEqual(len(ranked), 1)
        self.assertGreater(ranked[0].score, 10)

    def test_variants_with_same_author_and_base_are_collapsed(self):
        common = dict(
            author="lab", created_at="2026-08-08", last_modified="2026-08-09",
            pipeline_tag="text-to-speech", tags=[], downloads=10, likes=1,
            trending_score=0, library_name="transformers", license="apache-2.0",
            gated=False, base_models=["org/base-tts"], score=12,
        )
        first = HubModel(repo_id="lab/base-tts-int4", url="https://huggingface.co/lab/base-tts-int4", **common)
        second = HubModel(repo_id="lab/base-tts-int8", url="https://huggingface.co/lab/base-tts-int8", **common)
        collapsed = collapse_model_variants([first, second])
        self.assertEqual(len(collapsed), 1)
        self.assertEqual(collapsed[0].downloads, 20)
        self.assertEqual(collapsed[0].variants, ["lab/base-tts-int8"])


if __name__ == "__main__":
    unittest.main()
