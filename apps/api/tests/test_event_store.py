from uuid import uuid4

import pytest

from app.domain.events import ApplicationEvent, EventSource, EventType
from app.services.event_store import DuplicateSourceEventError, InMemoryEventStore


def test_duplicate_provider_source_id_is_rejected():
    store = InMemoryEventStore()
    application_id = uuid4()

    first = ApplicationEvent(
        application_id=application_id,
        event_type=EventType.APPLICATION_ACKNOWLEDGED,
        source=EventSource.GMAIL,
        source_id="gmail-message-123",
    )
    duplicate = first.model_copy(update={"id": uuid4()})

    store.append(first)

    with pytest.raises(DuplicateSourceEventError):
        store.append(duplicate)


def test_events_are_returned_as_immutable_tuple():
    store = InMemoryEventStore()
    application_id = uuid4()
    store.append(
        ApplicationEvent(
            application_id=application_id,
            event_type=EventType.APPLICATION_DETECTED,
            source=EventSource.MANUAL,
        )
    )

    assert isinstance(store.list_for_application(application_id), tuple)
