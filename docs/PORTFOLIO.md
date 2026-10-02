# Portfolio Positioning

## Project

**Career Intelligence Platform**

An AI-assisted career operating system that combines deterministic application tracking, resume intelligence, interview preparation, recruiter workflow support, and analytics.

## Engineering themes

This project is intentionally designed to show more than an LLM API call.

Key engineering themes:

- deterministic event sourcing
- idempotent ingestion
- classifier versioning
- human-in-the-loop review
- reproducible inference
- data provenance
- resume document processing
- multi-module full-stack architecture
- analytics derived from canonical history
- least-privilege external integrations
- production-oriented reliability and observability

## Interview narrative

A concise project explanation:

> I designed a career intelligence platform where Gmail and other sources can produce candidate application events, but canonical application history remains deterministic and auditable. AI is used for enrichment, resume matching, interview preparation, and drafting, while rules, provenance, event sourcing, and human review protect the system of record.

## Demo narrative

A public demonstration should use synthetic data:

1. create or ingest a synthetic application
2. classify an acknowledgement email
3. append the verified event
4. upload a sample resume
5. compare the resume against a job description
6. create a tailored resume version
7. link that version to the application
8. associate an interview record
9. show recruiter follow-up recommendations
10. show conversion and timing analytics

## Claims discipline

Do not claim:
- live Gmail authorization unless configured
- production deployment before release verification passes
- AI-generated experience or credentials
- causal conclusions from resume-version analytics

Prefer language such as:
- designed
- implemented
- evaluated
- verified
- derived
- recommended
- human-reviewed
