# Contributing

This is a private repository for a product that handles a bereaved family's sensitive data. Take care with data first, speed second.

## No real family data in the repository

- Never commit real names, PAN, Aadhaar (full or partial), account or folio numbers, policy numbers, death certificates, relationship proofs, statements, screenshots of portals, or interview recordings and notes.
- Golden-set items and demos use **synthetic families** only. Consented real cases are stored outside the repository with identifiers removed, and referenced by a consent id.
- Do not paste real data into issues, pull requests, prompts, logs or test fixtures. Mask PAN in anything shared.
- Never commit secrets or API keys. Use `.env` files (ignored) and commit `.env.example` only.
- If real data is committed by mistake, tell the team immediately; the history must be purged, not just reverted.

## Branching

- `main` is protected: pull request, one approving review, CI green.
- Branch names: `feat/<short-name>`, `fix/<short-name>`, `matrix/<institution>` for requirement-matrix changes, `docs/<short-name>`, `eval/<short-name>`.
- Keep pull requests small and linked to an issue from [planning/issues.json](planning/issues.json) (once imported into GitHub).
- Squash merge with a clear message.
- Do not edit [docs/HANDOFF.md](docs/HANDOFF.md) or [docs/research/](docs/research/README.md) files in a feature branch. Changes there are separate, reviewed pull requests, and decisions are added to [docs/DECISIONS.md](docs/DECISIONS.md) as new records.

## Requirement-matrix changes

A matrix entry must have `source_url`, `retrieved_on`, `verified_by` and `effective_from`. Thresholds stay `null` until a source states them. Branch-reported information is marked as lower-grade evidence. A matrix change needs a second reviewer and re-verification of the golden items it affects.

## Pull request checklist

- [ ] Linked issue and a clear description of the change
- [ ] Tests added or updated; CI is green
- [ ] **Eval regression run**: the golden-set runner passes on this branch (requirement accuracy, zero critical omissions, route accuracy, zero unsupported statements). Required for any change to a prompt, model identifier, template, matrix entry or rules code; attach the summary
- [ ] No real family data, secrets or unmasked PAN in code, fixtures, logs or screenshots
- [ ] No threshold, amount, form name or date comes from model output; every such value traces to the rules engine or a cited source
- [ ] Anything outbound still passes human review; the audit log still records the decision
- [ ] Privacy impact considered: new fields, retention, deletion path, what is sent to a model
- [ ] Legal-sensitive wording (indemnities, affidavits, fee terms) flagged for counsel; unverified legal points labelled **Unverified**
- [ ] Docs updated; facts labelled **Assumption**, **Inference** or **Conflict** where they apply
- [ ] Tone check for user-facing text: plain language, respectful of bereavement, no upsell in the first message

## Style

TypeScript with strict mode; Python only for the CAS worker. Format and lint with the repository configuration once added. Prefer clear names over comments, and put business rules in the matrix, not in code branches.
