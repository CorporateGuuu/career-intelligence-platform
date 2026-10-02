# ADR-001: Canonical history uses an append-only event ledger

## Status
Accepted

## Context
Career workflows arrive from unreliable and heterogeneous sources: email, manual input, calendar events, recruiter messages, and AI-assisted extraction. A mutable status field would make it difficult to explain why a state changed or to distinguish inferred data from confirmed history.

## Decision
Store canonical application history as append-only events. Derive current application state through deterministic projection rules.

AI-generated classifications and recommendations remain separate advisory artifacts until a deterministic rule or explicit human action produces a canonical event.

## Consequences

### Benefits
- auditable history
- deterministic replay
- correction without deleting prior evidence
- classifier-version traceability
- easier debugging of ingestion mistakes
- analytics derived from the same source of truth

### Costs
- projection logic must be versioned and tested
- event schemas require compatibility discipline
- duplicate detection and idempotency become first-class concerns
- corrections add events rather than mutating history in place

## Rejected alternative
A single mutable application status was rejected because it loses provenance and makes AI-assisted changes too difficult to audit.
