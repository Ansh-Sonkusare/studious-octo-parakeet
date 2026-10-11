# CLAUDE.md — Health Claim Recovery Agent

This repository is an AI-assisted service that recovers rejected and short-paid health-insurance claims for Indian policyholders (insurer grievance → Bima Bharosa → Insurance Ombudsman), with a human reviewer approving every letter.

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

Python 3.12 + FastAPI, Jinja2/HTMX review console, Postgres + pgvector on Supabase (Mumbai), Claude API (mid-tier model for analysis/drafting, small model for classification), WhatsApp Cloud API, Razorpay (ADR-008).

## Rules for any change

- Never take money from insurers, brokers or hospitals, never sell policies and never hold client money (ADR-005).
- The user files with their own login and OTP; the product drafts and guides (ADR-006).
- Health data is sensitive: no real policyholder documents, bills or discharge summaries in the repo, fixtures or prompts in issues.
- Every rupee amount, date, deadline and threshold comes from deterministic, tested code or a cited source — never from free model text.
- Retrieval plus tools; no fine-tuning. Pin prompts and model versions; changes go through the eval harness.
- Keep the evidence labels used in the docs: Fact (sourced), Assumption/estimate (replace with pilot data), Inference, Unverified/Unconfirmed (counsel or primary source must confirm), Conflict (sources disagree).
- No personal framing in docs; write in third person or "the team".

## Working conventions

- Branch from `main` as `feat/<issue-number>-<slug>`, `fix/...`, `docs/...`; reference the issue in the PR.
- PRs follow `.github/pull_request_template.md`, including the eval-regression check once the harness exists.
- No secrets in the repo; use `.env` (ignored) and document variables in `.env.example`.
- If a plan document and the code disagree, update the plan or record an ADR in the same PR.
