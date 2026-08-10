from __future__ import annotations

from dataclasses import asdict, dataclass, field
from typing import Dict, List


@dataclass
class Paper:
    source: str
    source_id: str
    title: str
    abstract: str
    authors: List[str]
    published: str
    updated: str
    url: str
    pdf_url: str = ""
    doi: str = ""
    venue: str = ""
    categories: List[str] = field(default_factory=list)
    code_urls: List[str] = field(default_factory=list)
    sources: List[str] = field(default_factory=list)
    score: int = 0
    topic_scores: Dict[str, int] = field(default_factory=dict)
    matched_topics: List[str] = field(default_factory=list)
    reasons: List[str] = field(default_factory=list)
    is_new: bool = True

    def to_dict(self) -> dict:
        return asdict(self)


@dataclass
class HubModel:
    repo_id: str
    author: str
    created_at: str
    last_modified: str
    pipeline_tag: str
    tags: List[str]
    downloads: int
    likes: int
    trending_score: float
    library_name: str
    license: str
    gated: bool
    url: str
    card_text: str = ""
    arxiv_ids: List[str] = field(default_factory=list)
    datasets: List[str] = field(default_factory=list)
    base_models: List[str] = field(default_factory=list)
    variants: List[str] = field(default_factory=list)
    score: int = 0
    topic_scores: Dict[str, int] = field(default_factory=dict)
    matched_topics: List[str] = field(default_factory=list)
    reasons: List[str] = field(default_factory=list)
    is_new: bool = True

    def to_dict(self) -> dict:
        return asdict(self)
