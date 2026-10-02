from __future__ import annotations

import re
from datetime import datetime, timezone
from uuid import UUID, uuid4

from pydantic import BaseModel, Field


class ResumeVersion(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    parent_id: UUID | None = None
    label: str
    text: str
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))


class JobDescription(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    company: str
    role: str
    text: str
    captured_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))


class ResumeMatch(BaseModel):
    score: float
    matched_terms: list[str]
    missing_terms: list[str]


_STOPWORDS = {
    "and", "the", "with", "for", "you", "our", "are", "this", "that", "from",
    "will", "have", "has", "job", "role", "team", "work", "years", "using",
}


def _terms(text: str) -> set[str]:
    tokens = set(re.findall(r"[a-zA-Z][a-zA-Z0-9+#.-]{2,}", text.lower()))
    return {token for token in tokens if token not in _STOPWORDS}


def match_resume(resume_text: str, job_text: str) -> ResumeMatch:
    resume_terms = _terms(resume_text)
    job_terms = _terms(job_text)

    if not job_terms:
        return ResumeMatch(score=0.0, matched_terms=[], missing_terms=[])

    matched = sorted(resume_terms & job_terms)
    missing = sorted(job_terms - resume_terms)
    score = round(len(matched) / len(job_terms), 4)

    return ResumeMatch(score=score, matched_terms=matched, missing_terms=missing)
