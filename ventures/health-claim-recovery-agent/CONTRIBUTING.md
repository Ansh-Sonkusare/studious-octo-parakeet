# Contributing

Short rules for a small team handling health data. Read [docs/PROTOTYPE_AND_MVP_PLAN.md](docs/PROTOTYPE_AND_MVP_PLAN.md) first.

## Data rules (non-negotiable)

- **No real customer data in this repository, ever.** That includes documents, screenshots, chat exports, names, phone numbers, policy numbers, claim numbers, diagnoses linked to a person, and any excerpt that could identify someone. This applies to issues, pull-request descriptions, comments and commit messages as well as files.
- Use synthetic fixtures. Fixtures must be invented, not edited copies of real documents.
- The golden set and consented files live in access-controlled encrypted storage outside the repository. Only schemas, loaders, synthetic fixtures and aggregate results are committed.
- Never commit secrets: API keys, database URLs, service-role keys, webhook secrets. Use environment variables; commit only `.env.example` with placeholder values.
- Insurer policy wordings are public documents but are not committed. Commit a manifest (source URL, date, SHA-256 hash) and a fetch script.
- If sensitive data is committed by mistake, tell the lead immediately. Do not just delete the file: history must be purged and any exposed credential rotated.

## Branching

- `main` is always releasable and protected; no direct pushes.
- Branch from `main` using `type/short-description`, for example `feat/room-rent-calculator`, `fix/deadline-timezone`, `eval/golden-v1-loader`, `docs/dpdp-notes`.
- Keep branches short-lived (ideally under three days) and rebase on `main` before review.
- Use squash merges with a clear message. Reference the issue (`Closes #NN`).
- Releases are tagged `vX.Y.Z` from `main` after the release-candidate evaluation passes. The MVP is `v0.1.0`.

## Pull-request checklist

Copy this into the pull-request description.

- [ ] Linked issue and milestone.
- [ ] Description says what changed and why, and how it was tested.
- [ ] Tests added or updated; unit and property tests pass locally and in CI.
- [ ] **Eval regression:** if the change touches a prompt, schema, model ID, retrieval setting, corpus, calculator or validator, the full development-split eval was run and the report is linked. No metric drops by more than 1 point against baseline, and invented clauses = 0. (Release candidates also run the sealed holdout and adversarial set.)
- [ ] Numbers in any generated text come from a calculator or a source document; no new arithmetic in prompts.
- [ ] No real customer data, no secrets, no document files outside allowed paths (secret and PII scans pass).
- [ ] Logs and error messages contain no document text or personal identifiers.
- [ ] New or changed data fields: encryption, retention and deletion behaviour considered; audit-log events added where relevant.
- [ ] Model or prompt versions pinned; no floating model aliases.
- [ ] Docs updated; a new entry added to [docs/DECISIONS.md](docs/DECISIONS.md) if the change is hard to reverse.
- [ ] Anything affecting legal gates (consent text, fee terms, disclosures, letter templates) reviewed by the lead and, where required, counsel.
- [ ] Reviewed by at least one other team member (the specialist for corpus, rules and letter-template changes).

## Review standards

- Reviewers check correctness of rules and clauses against primary sources, not only code quality.
- Changes to calculators need hand-worked examples in tests, confirmed by the claims specialist.
- Prefer small pull requests. If a change exceeds about 400 lines, split it.

## Style

- Python 3.12; formatter and linter configured in the project; type hints on public functions.
- Write plain, specific commit messages in the imperative mood.
- Label assumptions in documents with **[A]** and items needing verification with **[V]**, as in the plan.

## Existing documents

[docs/HANDOFF.md](docs/HANDOFF.md) and the files in [docs/research/](docs/research/README.md) are reference snapshots. Do not edit them to reflect later decisions; record decisions in [docs/DECISIONS.md](docs/DECISIONS.md) and corrections in a new dated note.
