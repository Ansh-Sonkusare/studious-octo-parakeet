# CLAUDE.md — GST Notice Desk

This repository is an AI reconciliation and notice desk for Indian CA firms: GSTR-2B/IMS vs books reconciliation, per-supplier action lists, supplier chasing, and cited draft replies to GST notices for CA sign-off.

**Status:** pre-prototype. Plan start Mon 12 Oct 2026; milestones M0 Discovery & legal (Fri 23 Oct 2026), M1 Prototype (Fri 30 Oct 2026), M2 MVP (Fri 11 Dec 2026), M3 Pilot & decision (Fri 29 Jan 2027).

## Where things are

| Path | What it is |
|---|---|
| `README.md` | Front page: pitch, problem in numbers, timeline, risks |
| `docs/HANDOFF.md` | Source of truth for problem, users, scope, legal, pricing, GTM |
| `docs/PROTOTYPE_AND_MVP_PLAN.md` | Build plan: timeline, specs, architecture, data model, eval plan, legal gates |
| `docs/DECISIONS.md` | Architecture and product decision records (ADRs) — add a new ADR for any change of direction |
| `docs/research/` | Research notes and the full research report (read-only reference) |
| `planning/milestones.md`, `planning/issues.json` | Milestones and the seed backlog (mirrored as GitHub issues) |
| `scripts/seed_github.py` | Creates labels, milestones and issues from `planning/`; `--sync` completes existing ones |

## Stack

Python engine and API, Next.js UI, Postgres + pgvector on Supabase, Claude API (ADR-007).

## Rules for any change

- The CA reviews, signs and files; the product never submits anything to an authority (ADR-002).
- File imports come before any GSP/ASP integration (ADR-003).
- Anonymise at source; no real client GSTINs, invoices or notices in the repo (ADR-008).
- Every rupee amount, date, deadline and threshold comes from deterministic, tested code or a cited source — never from free model text.
- Retrieval plus tools; no fine-tuning. Pin prompts and model versions; changes go through the eval harness.
- Keep the evidence labels used in the docs: Fact (sourced), Assumption/estimate (replace with pilot data), Inference, Unverified/Unconfirmed (counsel or primary source must confirm), Conflict (sources disagree).
- No personal framing in docs; write in third person or "the team".

## Working conventions

- Branch from `main` as `feat/<issue-number>-<slug>`, `fix/...`, `docs/...`; reference the issue in the PR.
- PRs follow `.github/pull_request_template.md`, including the eval-regression check once the harness exists.
- No secrets in the repo; use `.env` (ignored) and document variables in `.env.example`.
- If a plan document and the code disagree, update the plan or record an ADR in the same PR.
