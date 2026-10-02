# Architecture

## Product boundary

Career Intelligence Platform is one flagship product with separable modules:

- Job Tracker
- AI Resume Copilot
- Interview Intelligence
- Recruiter / Follow-Up Engine
- Application Intelligence
- Career Analytics

## System of record

The canonical source of truth is an append-only application event ledger.

Derived application state is computed from events using deterministic projection rules. AI outputs are enrichment artifacts and never silently mutate canonical history.

## High-level flow

```text
Gmail / Manual Input / Calendar
            |
            v
   Integration Adapters
            |
            v
 Normalize + Deduplicate
            |
            v
 Deterministic Classifier
            |
       ambiguous?
       /       \
     yes        no
      |          |
 Review Queue   |
      \          /
       v        v
   Application Event Ledger
            |
            v
  Deterministic Projection
            |
            +----------------------+
            |                      |
            v                      v
  Resume / Job Intelligence   Career Analytics
            |
            v
 Interview + Follow-Up Intelligence
```

## Trust boundaries

### Canonical
- application identity
- event history
- human corrections
- selected resume version
- confirmed interview associations
- confirmed outcomes

### Advisory
- LLM classifications
- skill-gap analysis
- resume rewriting suggestions
- interview questions
- recruiter follow-up drafts
- portfolio-project recommendations

## Persistence

The domain layer should depend on repository interfaces rather than a concrete database.

Supported direction:
- local/demo: SQLite
- hosted: PostgreSQL

## Integration readiness

External integrations must report one of:

- READY
- DEGRADED
- NOT_CONFIGURED

The UI and API must never report an integration as healthy solely because the process is running.

## Security

- authenticated ownership is server authoritative
- no client-supplied user ID is trusted as authorization
- Gmail uses read-only scope
- public demos use synthetic data
- uploaded documents and personal messages are excluded from Git
- secrets are environment-only
- logs must not contain resume bodies, email bodies, tokens, or credentials
