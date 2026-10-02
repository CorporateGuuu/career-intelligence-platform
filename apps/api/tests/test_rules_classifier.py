from app.domain.events import EventType
from app.services.rules_classifier import classify


def test_classification_is_deterministic():
    first = classify("Application received", "Thank you for applying to Example Co.")
    second = classify("Application received", "Thank you for applying to Example Co.")

    assert first == second
    assert first.event_type == EventType.APPLICATION_ACKNOWLEDGED
    assert first.input_hash == second.input_hash


def test_unknown_message_stays_unclassified():
    result = classify("Hello", "Checking in about next week.")

    assert result.event_type is None
    assert result.confidence == 0.0
