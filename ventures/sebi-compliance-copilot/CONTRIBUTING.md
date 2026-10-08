# Contributing

This is a private repository. Work is tracked as issues grouped by milestone (see [planning/milestones.md](planning/milestones.md)).

## Branching

- `main` is always releasable and protected. No direct pushes.
- Branch from `main` as `<type>/<issue-number>-<short-name>`, with type one of `feat`, `fix`, `rules`, `eval`, `docs`, `chore`. Example: `rules/42-finfluencer-pack-v0`.
- Keep branches short-lived. Squash-merge with a message that references the issue.
- Changes to `rules/packs/` use the `rules/` prefix and are reviewed by a person with compliance context in addition to a code reviewer.

## Pull request checklist

Copy this into the PR description.

- [ ] Linked issue and milestone
- [ ] Lint, type-check and unit tests pass
- [ ] **Eval regression:** if the change touches a rule pack, prompt, output schema, retrieval, or model id, the eval harness was run against the current labelled set and the diff report is attached; no previously correct high-severity detection was lost without an approved reason; recall and citation-precision floors in `docs/PROTOTYPE_AND_MVP_PLAN.md` section 8 still hold
- [ ] **Rule-set versioning:** any rule change bumps the pack version and sets its status (`draft`, `advisory_pending_notification`, `in_force`, `superseded`), effective date and source citation; old versions are not edited in place
- [ ] Every new or changed rule cites a primary source clause; anything not verified against sebi.gov.in is marked `[Unconfirmed]`
- [ ] Model-judged checks still return a clause id and a verbatim quote that the citation validator accepts
- [ ] Numbers and dates (thresholds, deadlines) are computed in code, not by the model
- [ ] Audit-log and evidence code paths remain append-only; no update or delete added
- [ ] No secrets, client data or non-public content added (see below)
- [ ] Docs updated (plan, decisions, milestones) if scope or assumptions changed; new decisions get an ADR in `docs/DECISIONS.md`

## Data rules

- **No client data in the repository, ever.** This includes client names, PAN, holdings, phone numbers, WhatsApp exports, call recordings, design-partner archives and screenshots of non-public content.
- Labelled items, captures and exports live in a private data store and in the gitignored `data/` directory. The repository holds only the label schema, labelling guide and synthetic examples that contain no real content.
- Public posts used for evaluation are stored with URL, capture time and hash in the private store, not in git.
- Do not commit `.env` files or keys. Use `.env.example` with placeholders. Run secret scanning before pushing.
- Do not send partner data to any model vendor until the legal position on offshore processing and zero-retention terms is recorded (ADR-007).

## Style

- TypeScript is the default language; Python is used only for analysis notebooks in `eval/`.
- Tag unverified regulatory statements in docs and comments with `[Unconfirmed]`, planning choices with `[Assumption]`, and reasoning from facts with `[Inference]`, as in `docs/HANDOFF.md`.
- Keep prompts, schemas and rule packs versioned and reviewable as text files.
