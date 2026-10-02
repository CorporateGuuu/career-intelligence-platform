from __future__ import annotations

import hashlib
import re
from dataclasses import dataclass

from app.domain.events import EventType


CLASSIFIER_NAME = "rules"
CLASSIFIER_VERSION = "1.0.0"

_RULES: list[tuple[EventType, tuple[str, ...]]] = [
    (EventType.OFFER_RECEIVED, ("offer letter", "pleased to offer", "employment offer")),
    (EventType.REJECTED, ("not moving forward", "other candidates", "unfortunately")),
    (EventType.INTERVIEW_INVITED, ("interview", "schedule a call", "meet with the team")),
    (EventType.ASSESSMENT_RECEIVED, ("assessment", "coding challenge", "take-home")),
    (EventType.APPLICATION_ACKNOWLEDGED, ("application received", "thank you for applying", "we received your application")),
    (EventType.RECRUITER_CONTACTED, ("recruiter", "talent acquisition", "opportunity")),
]


@dataclass(frozen=True)
class Classification:
    event_type: EventType | None
    confidence: float
    matched_rule: str | None
    input_hash: str
    classifier_name: str = CLASSIFIER_NAME
    classifier_version: str = CLASSIFIER_VERSION


def _normalize(text: str) -> str:
    return re.sub(r"\s+", " ", text.lower()).strip()


def classify(subject: str, body: str) -> Classification:
    normalized = _normalize(f"{subject}\n{body}")
    digest = hashlib.sha256(normalized.encode("utf-8")).hexdigest()

    for event_type, phrases in _RULES:
        for phrase in phrases:
            if phrase in normalized:
                return Classification(
                    event_type=event_type,
                    confidence=1.0,
                    matched_rule=phrase,
                    input_hash=digest,
                )

    return Classification(
        event_type=None,
        confidence=0.0,
        matched_rule=None,
        input_hash=digest,
    )
