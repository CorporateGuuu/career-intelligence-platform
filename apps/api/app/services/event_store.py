from __future__ import annotations

from collections import defaultdict
from uuid import UUID

from app.domain.events import ApplicationEvent


class DuplicateSourceEventError(ValueError):
    pass


class InMemoryEventStore:
    """Development event store with append-only semantics.

    Production persistence will implement the same interface using SQLite/PostgreSQL.
    """

    def __init__(self) -> None:
        self._events: dict[UUID, list[ApplicationEvent]] = defaultdict(list)
        self._source_keys: set[tuple[str, str]] = set()

    def append(self, event: ApplicationEvent) -> ApplicationEvent:
        if event.source_id:
            key = (event.source.value, event.source_id)
            if key in self._source_keys:
                raise DuplicateSourceEventError(
                    f"source event already ingested: {event.source}:{event.source_id}"
                )
            self._source_keys.add(key)

        self._events[event.application_id].append(event)
        return event

    def list_for_application(self, application_id: UUID) -> tuple[ApplicationEvent, ...]:
        return tuple(self._events.get(application_id, ()))
