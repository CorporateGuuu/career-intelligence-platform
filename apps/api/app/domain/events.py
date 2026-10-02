from __future__ import annotations

from datetime import datetime, timezone
from enum import StrEnum
from typing import Any
from uuid import UUID, uuid4

from pydantic import BaseModel, Field


class EventType(StrEnum):
    APPLICATION_DETECTED = "APPLICATION_DETECTED"
    APPLICATION_ACKNOWLEDGED = "APPLICATION_ACKNOWLEDGED"
    ASSESSMENT_RECEIVED = "ASSESSMENT_RECEIVED"
    ASSESSMENT_COMPLETED = "ASSESSMENT_COMPLETED"
    RECRUITER_CONTACTED = "RECRUITER_CONTACTED"
    RECRUITER_SCREEN_SCHEDULED = "RECRUITER_SCREEN_SCHEDULED"
    RECRUITER_SCREEN_COMPLETED = "RECRUITER_SCREEN_COMPLETED"
    INTERVIEW_INVITED = "INTERVIEW_INVITED"
    INTERVIEW_SCHEDULED = "INTERVIEW_SCHEDULED"
    INTERVIEW_COMPLETED = "INTERVIEW_COMPLETED"
    FOLLOW_UP_SENT = "FOLLOW_UP_SENT"
    REJECTED = "REJECTED"
    WITHDRAWN = "WITHDRAWN"
    OFFER_RECEIVED = "OFFER_RECEIVED"
    OFFER_ACCEPTED = "OFFER_ACCEPTED"
    OFFER_DECLINED = "OFFER_DECLINED"
    MANUAL_CORRECTION = "MANUAL_CORRECTION"


class EventSource(StrEnum):
    MANUAL = "manual"
    GMAIL = "gmail"
    CALENDAR = "calendar"
    SYSTEM = "system"
    IMPORT = "import"


class ClassifierMetadata(BaseModel):
    name: str
    version: str
    confidence: float = Field(ge=0.0, le=1.0)
    input_hash: str
    evidence: list[str] = Field(default_factory=list)


class ApplicationEvent(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    application_id: UUID
    event_type: EventType
    occurred_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    source: EventSource
    source_id: str | None = None
    classifier: ClassifierMetadata | None = None
    human_verified: bool = False
    metadata: dict[str, Any] = Field(default_factory=dict)


class ManualCorrection(BaseModel):
    application_id: UUID
    original_event_id: UUID | None = None
    corrected_event_type: EventType
    reason: str
    corrected_by: str
