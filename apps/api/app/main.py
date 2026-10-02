from __future__ import annotations

from uuid import UUID

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from app.domain.events import ApplicationEvent
from app.domain.projector import project_status
from app.services.event_store import DuplicateSourceEventError, InMemoryEventStore

app = FastAPI(
    title="Career Intelligence Platform API",
    version="0.1.0",
    description="Deterministic career application ledger with advisory AI boundaries.",
)

store = InMemoryEventStore()


class Readiness(BaseModel):
    status: str
    database: str
    gmail: str
    ai_provider: str


@app.get("/healthz")
def health() -> dict[str, str]:
    return {"status": "ok"}


@app.get("/readyz", response_model=Readiness)
def readiness() -> Readiness:
    return Readiness(
        status="degraded",
        database="in_memory_development_store",
        gmail="not_configured",
        ai_provider="not_configured",
    )


@app.post("/applications/{application_id}/events", response_model=ApplicationEvent)
def append_event(application_id: UUID, event: ApplicationEvent) -> ApplicationEvent:
    if event.application_id != application_id:
        raise HTTPException(status_code=400, detail="application_id mismatch")

    try:
        return store.append(event)
    except DuplicateSourceEventError as exc:
        raise HTTPException(status_code=409, detail=str(exc)) from exc


@app.get("/applications/{application_id}/events")
def list_events(application_id: UUID) -> dict:
    events = store.list_for_application(application_id)
    return {
        "application_id": application_id,
        "derived_status": project_status(events),
        "events": events,
    }
