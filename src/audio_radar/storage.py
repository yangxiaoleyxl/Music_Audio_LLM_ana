from __future__ import annotations

import datetime as dt
import sqlite3
from pathlib import Path
from typing import Iterable, Set

from .models import HubModel, Paper
from .ranking import canonical_key


SCHEMA = """
CREATE TABLE IF NOT EXISTS papers (
    canonical_key TEXT PRIMARY KEY,
    title TEXT NOT NULL,
    url TEXT NOT NULL,
    published TEXT,
    score INTEGER NOT NULL,
    first_seen TEXT NOT NULL,
    last_seen TEXT NOT NULL
);
CREATE TABLE IF NOT EXISTS hub_models (
    repo_id TEXT PRIMARY KEY,
    last_modified TEXT,
    score INTEGER NOT NULL,
    first_seen TEXT NOT NULL,
    last_seen TEXT NOT NULL
);
"""


class RadarStore:
    def __init__(self, path: Path):
        path.parent.mkdir(parents=True, exist_ok=True)
        self.connection = sqlite3.connect(str(path))
        self.connection.executescript(SCHEMA)
        self.connection.commit()

    def seen_keys(self, papers: Iterable[Paper]) -> Set[str]:
        keys = [canonical_key(paper) for paper in papers]
        if not keys:
            return set()
        found: Set[str] = set()
        for start in range(0, len(keys), 800):
            chunk = keys[start:start + 800]
            placeholders = ",".join("?" for _ in chunk)
            rows = self.connection.execute(
                "SELECT canonical_key FROM papers WHERE canonical_key IN ({})".format(placeholders),
                chunk,
            )
            found.update(row[0] for row in rows)
        return found

    def upsert(self, papers: Iterable[Paper], now: dt.date) -> None:
        stamp = now.isoformat()
        for paper in papers:
            key = canonical_key(paper)
            self.connection.execute(
                """
                INSERT INTO papers(canonical_key, title, url, published, score, first_seen, last_seen)
                VALUES (?, ?, ?, ?, ?, ?, ?)
                ON CONFLICT(canonical_key) DO UPDATE SET
                    title=excluded.title,
                    url=excluded.url,
                    published=excluded.published,
                    score=excluded.score,
                    last_seen=excluded.last_seen
                """,
                (key, paper.title, paper.url, paper.published, paper.score, stamp, stamp),
            )
        self.connection.commit()

    def unchanged_model_ids(self, models: Iterable[HubModel]) -> Set[str]:
        model_list = list(models)
        ids = [model.repo_id for model in model_list]
        if not ids:
            return set()
        found: Set[str] = set()
        for start in range(0, len(ids), 800):
            chunk = ids[start:start + 800]
            placeholders = ",".join("?" for _ in chunk)
            expected = {model.repo_id: model.last_modified for model in model_list if model.repo_id in chunk}
            rows = self.connection.execute(
                "SELECT repo_id, last_modified FROM hub_models WHERE repo_id IN ({})".format(placeholders), chunk
            )
            found.update(row[0] for row in rows if expected.get(row[0]) == row[1])
        return found

    def upsert_models(self, models: Iterable[HubModel], now: dt.date) -> None:
        stamp = now.isoformat()
        for model in models:
            self.connection.execute(
                """
                INSERT INTO hub_models(repo_id, last_modified, score, first_seen, last_seen)
                VALUES (?, ?, ?, ?, ?)
                ON CONFLICT(repo_id) DO UPDATE SET
                    last_modified=excluded.last_modified,
                    score=excluded.score,
                    last_seen=excluded.last_seen
                """,
                (model.repo_id, model.last_modified, model.score, stamp, stamp),
            )
        self.connection.commit()

    def close(self) -> None:
        self.connection.close()
