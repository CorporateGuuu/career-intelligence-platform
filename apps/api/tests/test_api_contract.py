from __future__ import annotations

from uuid import uuid4

import pytest
from fastapi.testclient import TestClient

import app.main as main_module
from app.services.event_store import InMemoryEventStore


@pytest.fixture
def client(monkeypatch):
    monkeypatch.setattr(main_module, "store", InMemoryEventStore())
    return TestClient(main_module.app)


def event_payload(application_id, event_type="APPLICATION_ACKNOWLEDGED", source_id="gmail-123"):
    return {
        "application_id": str(application_id),
        "event_type": event_type,
        "source": "gmail",
        "source_id": source_id,
        "human_verified": False,
        "metadata": {},
    }


def test_health_and_readiness_are_explicit(client):
    health = client.get("/healthz")
    assert health.status_code == 200
    assert health.json() == {"status": "ok"}

    readiness = client.get("/readyz")
    assert readiness.status_code == 200
    assert readiness.json() == {
        "status": "degraded",
        "database": "in_memory_development_store",
        "gmail": "not_configured",
        "ai_provider": "not_configured",
    }


def test_append_and_list_projects_application_status(client):
    application_id = uuid4()
    created = client.post(
        f"/applications/{application_id}/events",
        json=event_payload(application_id),
    )
    assert created.status_code == 200
    assert created.json()["event_type"] == "APPLICATION_ACKNOWLEDGED"

    result = client.get(f"/applications/{application_id}/events")
    assert result.status_code == 200
    assert result.json()["derived_status"] == "acknowledged"
    assert len(result.json()["events"]) == 1


def test_application_id_mismatch_is_rejected(client):
    path_id = uuid4()
    payload_id = uuid4()

    response = client.post(
        f"/applications/{path_id}/events",
        json=event_payload(payload_id),
    )

    assert response.status_code == 400
    assert response.json()["detail"] == "application_id mismatch"


def test_duplicate_source_event_returns_conflict(client):
    application_id = uuid4()
    payload = event_payload(application_id, source_id="gmail-duplicate")

    first = client.post(f"/applications/{application_id}/events", json=payload)
    second = client.post(f"/applications/{application_id}/events", json=payload)

    assert first.status_code == 200
    assert second.status_code == 409
    assert "source event already ingested" in second.json()["detail"]
