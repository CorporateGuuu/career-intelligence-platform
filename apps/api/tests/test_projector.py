from datetime import datetime, timedelta, timezone
from uuid import uuid4

from app.domain.events import ApplicationEvent, EventSource, EventType
from app.domain.projector import ApplicationStatus, project_status


def event(application_id, event_type, minute):
    return ApplicationEvent(
        application_id=application_id,
        event_type=event_type,
        source=EventSource.MANUAL,
        occurred_at=datetime(2026, 1, 1, tzinfo=timezone.utc) + timedelta(minutes=minute),
        human_verified=True,
    )


def test_projection_is_deterministic_when_input_order_changes():
    application_id = uuid4()
    events = [
        event(application_id, EventType.APPLICATION_DETECTED, 0),
        event(application_id, EventType.INTERVIEW_INVITED, 20),
        event(application_id, EventType.APPLICATION_ACKNOWLEDGED, 10),
    ]

    assert project_status(events) == ApplicationStatus.INTERVIEW
    assert project_status(reversed(events)) == ApplicationStatus.INTERVIEW


def test_terminal_status_is_not_silently_reopened():
    application_id = uuid4()
    events = [
        event(application_id, EventType.APPLICATION_DETECTED, 0),
        event(application_id, EventType.REJECTED, 10),
        event(application_id, EventType.INTERVIEW_INVITED, 20),
    ]

    assert project_status(events) == ApplicationStatus.REJECTED


def test_manual_correction_can_override_with_auditable_event():
    application_id = uuid4()
    events = [
        event(application_id, EventType.APPLICATION_DETECTED, 0),
        event(application_id, EventType.REJECTED, 10),
        ApplicationEvent(
            application_id=application_id,
            event_type=EventType.MANUAL_CORRECTION,
            source=EventSource.MANUAL,
            occurred_at=datetime(2026, 1, 1, 0, 20, tzinfo=timezone.utc),
            human_verified=True,
            metadata={"corrected_event_type": EventType.ASSESSMENT_RECEIVED.value},
        ),
    ]

    assert project_status(events) == ApplicationStatus.ASSESSMENT
