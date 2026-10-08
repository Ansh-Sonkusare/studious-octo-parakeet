# Contributing

## Data rules (read first)

- **No real customer data in the repository, ever.** That covers ledgers, invoices, bank statements, buyer names, phone numbers, emails, GSTIN, Udyam numbers, screenshots and logs.
- Test and eval fixtures are synthetic or irreversibly anonymised (names, GSTIN and contact details removed). A second person checks each new fixture batch.
- Originals live outside the repo, with access limited to named staff, under the supplier's signed consent.
- No secrets in the repo. Use environment variables or the managed secret store; `.env` is git-ignored. If a secret is committed, rotate it at once and tell the team.
- Legal conclusions are recorded only after counsel confirms them. Mark unconfirmed points **Unverified**, as in [HANDOFF.md](docs/HANDOFF.md).

## Branching

- `main` is protected and always releasable. Open a pull request for every change; no direct pushes.
- Branch names: `type/short-description`, for example `build/interest-engine`, `eval/golden-set-v0`, `docs/rule-spec`.
- Keep pull requests small and linked to an issue from `planning/issues.json`.
- Squash-merge with a message that says what changed and why. Release tags follow milestones (`m1-prototype`, `m2-mvp`).

## Pull-request checklist

- [ ] Linked issue and milestone
- [ ] Tests added or updated; CI is green
- [ ] **Eval regression:** if the change touches `packages/core`, `templates`, `corpus`, `rules` or `evals`, the eval report is attached and every blocking suite meets `evals/thresholds.yaml` (golden set at 100%)
- [ ] A fixed bug adds a regression case to its suite
- [ ] Rule-set or rate-table change: second reviewer approved; golden set re-run; legal-confirmation status updated
- [ ] No figure, date or legal citation hard-coded in a template or prompt outside the approved slots and citation list
- [ ] No letter cites a provision whose status is unconfirmed (for example the MSMED amendment before assent is confirmed)
- [ ] No real customer data, credentials or personal data in code, fixtures, logs or screenshots
- [ ] Contact rules unchanged, or the change is explained (8am-9pm; contact caps; opt-out and dispute pause; AI-assistance disclosure)
- [ ] Docs and decision records updated where behaviour changed; ADR added if a decision changed

## Reviews

One approval is required. Changes to calculators, rule sets, the post-check, consent flows or the audit log need review by someone other than the author, and calculator changes need the CA reviewer's sign-off on any new or changed golden case.

## Style

Python: type hints, `Decimal` for money, integer paise in storage, no floating-point money arithmetic. TypeScript: strict mode. Write documents in plain, third-person language and label assumptions.
