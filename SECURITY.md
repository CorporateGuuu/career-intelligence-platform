# Security and privacy boundaries

Career Intelligence Platform handles sensitive personal workflow data by design. The public repository therefore uses a strict separation between **portfolio-safe architecture** and any real user data.

## Current executable boundary

The current FastAPI append/list endpoints have no authenticated-principal or per-user authorization check. A process-global in-memory store is shared by requests; it is a development fixture, not a durable isolated user ledger. Do not put real resumes, mail, recruiter details or application histories into this prototype. The privacy controls below define the intended integration boundary; they do not imply that OAuth, durable storage or production access controls are already installed.

The current Next.js dashboard contains static synthetic examples and disconnected review buttons. A displayed human-verified label does not prove a real review or an authorized backend mutation.

## Data classifications

### Public-safe
- synthetic applications
- synthetic resumes
- synthetic recruiter messages
- sample job descriptions
- fake company names
- anonymized architecture diagrams
- deterministic test fixtures

### Private / excluded from Git
- real resumes
- real email bodies
- OAuth tokens
- refresh tokens
- access tokens
- recruiter contact details
- interview notes tied to real people
- personal calendar contents
- API credentials
- browser/session cookies

## Trust boundaries

### Gmail
The intended integration uses read-only scopes. Ingestion may create candidate events, but email content is not the canonical system of record.

### Calendar
Calendar data may propose interview associations. Ambiguous matches require review before canonical linkage.

### AI / LLM providers
AI output is advisory. It may classify, summarize, extract, rewrite, rank, or draft, but it cannot silently mutate canonical application history.

### Canonical event ledger
Only validated deterministic events and explicit human corrections become canonical history.

## Logging

Logs must not contain:
- resume bodies
- email bodies
- OAuth credentials
- session cookies
- raw access/refresh tokens
- full personal message content

Operational logs should favor identifiers, event types, classifier versions, request IDs, timings, and redacted error context.

## Public portfolio rule

This repository must remain reviewable without exposing private career data. Any demo deployment should use synthetic fixtures by default and make external integration readiness explicit as READY, DEGRADED, or NOT_CONFIGURED.
