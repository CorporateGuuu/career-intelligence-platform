# Career Intelligence Platform

A portfolio-grade career operating system that unifies deterministic job-application tracking with AI-assisted resume intelligence, interview preparation, recruiter follow-up, and career analytics.

## Why this project exists

Most career tools treat applications, resumes, recruiter emails, interviews, and analytics as separate workflows. Career Intelligence Platform combines them into one auditable system while keeping AI advisory rather than authoritative over canonical application history.

## Core modules

### Job Tracker
- Gmail read-only ingestion boundary
- Application acknowledgement, rejection, interview, assessment, offer, and recruiter-message detection
- Idempotent synchronization and deduplication
- Append-only application event history
- Deterministic derived application status
- Rules-based classifier with versioning and cached inference
- Optional local Ollama enrichment
- Human review/correction queue
- CSV/XLSX export
- Funnel, response-rate, and time-to-response analytics

### AI Resume Copilot
- PDF/DOCX parsing
- Master resume and version lineage
- Job-description matching
- Keyword and skills-gap analysis
- Role-specific bullet recommendations
- Tailored resume versions
- Application-to-resume-version linkage
- Resume-version performance analytics

### Interview Intelligence
- Interview records linked to applications
- Email invitation vs calendar-event separation
- Evidence-based calendar association
- Human review for ambiguous matches
- Technical and behavioral interview preparation
- STAR-story prompts
- Post-interview notes and outcome tracking

### Recruiter / Follow-Up Engine
- Recruiter and thread timelines
- Stage-aware follow-up recommendations
- Draft generation only
- No automatic outbound communication

### Career Analytics
- Application funnel
- Response/interview/offer conversion
- Time-to-response, time-to-interview, time-to-offer
- Breakdowns by role, company, source, location, outcome, and resume version
- Classifier review/correction analytics

## Architecture principle

Canonical application state is deterministic and auditable.

AI may:
- enrich
- extract
- summarize
- rank confidence
- tailor resumes
- prepare interviews
- recommend portfolio projects
- draft follow-ups

AI may not:
- silently rewrite application history
- fabricate application events
- overwrite human corrections
- become the sole authority over canonical state

## Canonical event model

Applications are modeled as a projection over an append-only event ledger.

Example event types:
- APPLICATION_DETECTED
- APPLICATION_ACKNOWLEDGED
- ASSESSMENT_RECEIVED
- ASSESSMENT_COMPLETED
- RECRUITER_CONTACTED
- RECRUITER_SCREEN_SCHEDULED
- RECRUITER_SCREEN_COMPLETED
- INTERVIEW_INVITED
- INTERVIEW_SCHEDULED
- INTERVIEW_COMPLETED
- FOLLOW_UP_SENT
- REJECTED
- WITHDRAWN
- OFFER_RECEIVED
- OFFER_ACCEPTED
- OFFER_DECLINED
- MANUAL_CORRECTION

## Portfolio focus

This repository is intended to demonstrate:
- Python backend engineering
- FastAPI architecture
- Next.js / React / TypeScript frontend design
- Gmail/OAuth integration patterns
- event-driven data modeling
- SQLite/PostgreSQL repository abstraction
- deterministic inference
- local LLM/Ollama integration
- human-in-the-loop systems
- analytics and exports
- testing and CI/CD
- security and least-privilege design
- idempotent and auditable production workflows

## Repository direction

The canonical product is `career-intelligence-platform`.

`job-tracker` and `ai-resume-copilot` are first-class modules within the same platform, while remaining architecturally separable enough to demonstrate individual engineering capabilities.

## Architecture and security

- `docs/ARCHITECTURE.md` — system boundary and canonical/advisory separation
- `docs/ADR-001-event-ledger.md` — why canonical history is append-only and deterministic
- `SECURITY.md` — privacy, logging, integration, and public-demo boundaries

## Safety and privacy

- Gmail integration is designed for read-only scopes.
- External integrations must expose honest READY / DEGRADED / NOT_CONFIGURED states.
- Synthetic demo data should be used for public portfolio demonstrations.
- Secrets, tokens, resumes, and personal email contents must never be committed.
- AI-generated recommendations are advisory and stored separately from canonical event history.

## Current status

The canonical GitHub repository has been created under `CorporateGuuu`.

The active implementation is being migrated from a separate Replit development workspace into this repository. Until the source migration is complete, this repository should be treated as the canonical portfolio/documentation location, not yet the complete deployable codebase.

## Roadmap

1. Complete source migration from the current development workspace
2. Lock repository structure and CI
3. Verify deterministic application ledger
4. Verify Resume Copilot versioning and application linkage
5. Verify Gmail ingestion boundaries and review queue
6. Verify analytics and export integrity
7. Add architecture diagrams and screenshots
8. Publish a synthetic-data demo deployment
9. Tag the first portfolio release

## Ownership

Independent portfolio repository maintained under `CorporateGuuu`.

Future development remains separate from prior collaborator repositories and does not require access to, PRs against, or notifications to any former collaborator.
