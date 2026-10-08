# Contributing

This is a private repository for a small team. These rules keep the work reviewable and keep client data out of source control.

## Hard rule: no real client data in the repository

- Never commit GSTINs, supplier or client names, invoices, 2B or register exports, ledgers, notices, replies or screenshots from a real firm, even partially redacted.
- Design-partner data is anonymised by the partner with `tools/anonymise` and kept in the access-controlled store described in [docs/DECISIONS.md](docs/DECISIONS.md) (ADR-008). Labelled sets live there too.
- Only synthetic fixtures under `evals/fixtures/` may be committed. Generate them with `scripts/` tooling.
- Never paste real data into prompts, issues, pull requests or chat tools.
- If real data is committed by mistake: stop, tell the team the same day, and remove it from history (not just the latest commit) before anything else is pushed.
- Secrets (API keys, database URLs) go in a secret manager or an untracked `.env`; commit only `.env.example`.

## Branching

- `main` is protected and always green. No direct pushes.
- Branch from `main` as `type/short-description`, for example `feat/matching-tier-3`, `fix/gstin-checksum`, `eval/notice-set-v2`, `docs/adr-009`.
- Keep branches short-lived (a few days). Rebase on `main` before opening a pull request.
- Link each pull request to an issue from [planning/issues.json](planning/issues.json) or its GitHub copy and to its milestone.
- Squash-merge with a clear message; one logical change per pull request.

## Pull request checklist

Copy into the description and tick before requesting review.

- [ ] Linked issue and milestone
- [ ] Tests added or updated; unit and property tests pass locally
- [ ] **Eval regression:** if the change touches `packages/recon`, `packages/importers`, matching configs, prompts, model versions, retrieval or the law corpus, the eval report is attached and shows no drop against `evals/baselines.json` and no newly wrong case
- [ ] If thresholds or baselines changed: the description says why and a second reviewer approved
- [ ] Safety set passes (any failure blocks merge)
- [ ] No real client data, no secrets, no new large binary files
- [ ] Any rupee figure shown to a user traces to a run and lines; nothing computed by a model
- [ ] Any legal statement in output carries a citation; any new law source records its effective dates and licensing status
- [ ] No code path submits to a government system or sends a message without CA approval ([docs/DECISIONS.md](docs/DECISIONS.md), ADR-002)
- [ ] Audit events added for any new approval, edit, export or outbound action
- [ ] Docs updated (plan, ADRs or README) if behaviour or scope changed; assumptions labelled as such

## Code style

- Python: type hints, `Decimal` for money (never float), no I/O in `packages/recon`. Format and lint with the repository's configured tools.
- TypeScript: strict mode; the API client is generated from the OpenAPI schema, not hand-written.
- Prompts and model versions are versioned in the repository and change only through a pull request with an eval report.

## Documentation conventions

Follow the labels in [docs/HANDOFF.md](docs/HANDOFF.md): mark **assumption**, **estimate** and **unverified** items, and link sources from `docs/research/`. Record significant decisions as a new ADR in [docs/DECISIONS.md](docs/DECISIONS.md).
