from __future__ import annotations

from enum import StrEnum
from typing import Iterable

from .events import ApplicationEvent, EventType


class ApplicationStatus(StrEnum):
    DETECTED = "detected"
    ACKNOWLEDGED = "acknowledged"
    ASSESSMENT = "assessment"
    RECRUITER_SCREEN = "recruiter_screen"
    INTERVIEW = "interview"
    OFFER = "offer"
    ACCEPTED = "accepted"
    REJECTED = "rejected"
    WITHDRAWN = "withdrawn"
    OFFER_DECLINED = "offer_declined"


_STATUS_BY_EVENT: dict[EventType, ApplicationStatus] = {
    EventType.APPLICATION_DETECTED: ApplicationStatus.DETECTED,
    EventType.APPLICATION_ACKNOWLEDGED: ApplicationStatus.ACKNOWLEDGED,
    EventType.ASSESSMENT_RECEIVED: ApplicationStatus.ASSESSMENT,
    EventType.ASSESSMENT_COMPLETED: ApplicationStatus.ASSESSMENT,
    EventType.RECRUITER_CONTACTED: ApplicationStatus.RECRUITER_SCREEN,
    EventType.RECRUITER_SCREEN_SCHEDULED: ApplicationStatus.RECRUITER_SCREEN,
    EventType.RECRUITER_SCREEN_COMPLETED: ApplicationStatus.RECRUITER_SCREEN,
    EventType.INTERVIEW_INVITED: ApplicationStatus.INTERVIEW,
    EventType.INTERVIEW_SCHEDULED: ApplicationStatus.INTERVIEW,
    EventType.INTERVIEW_COMPLETED: ApplicationStatus.INTERVIEW,
    EventType.OFFER_RECEIVED: ApplicationStatus.OFFER,
    EventType.OFFER_ACCEPTED: ApplicationStatus.ACCEPTED,
    EventType.REJECTED: ApplicationStatus.REJECTED,
    EventType.WITHDRAWN: ApplicationStatus.WITHDRAWN,
    EventType.OFFER_DECLINED: ApplicationStatus.OFFER_DECLINED,
}

_TERMINAL = {
    ApplicationStatus.ACCEPTED,
    ApplicationStatus.REJECTED,
    ApplicationStatus.WITHDRAWN,
    ApplicationStatus.OFFER_DECLINED,
}


def project_status(events: Iterable[ApplicationEvent]) -> ApplicationStatus:
    ordered = sorted(events, key=lambda event: (event.occurred_at, str(event.id)))
    if not ordered:
        return ApplicationStatus.DETECTED

    status = ApplicationStatus.DETECTED
    for event in ordered:
        if event.event_type == EventType.MANUAL_CORRECTION:
            corrected = event.metadata.get("corrected_event_type")
            if corrected:
                status = _STATUS_BY_EVENT[EventType(corrected)]
            continue

        candidate = _STATUS_BY_EVENT.get(event.event_type)
        if candidate is None:
            continue

        if status in _TERMINAL and candidate not in _TERMINAL:
            continue

        status = candidate

    return status
