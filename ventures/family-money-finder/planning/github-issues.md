# GitHub issue index

The backlog in [issues.json](issues.json) has been seeded as GitHub issues in [Ansh-Sonkusare/family-money-finder](https://github.com/Ansh-Sonkusare/family-money-finder/issues): one epic per milestone (label `epic`) and one issue for each of the 39 backlog entries, attached to its epic as a sub-issue. Goals, scope and exit criteria for each milestone are in [milestones.md](milestones.md). Each issue keeps the labels from `issues.json` (`type:*` and `priority:*`) and ends with a footer naming its milestone and due date.

This file is a snapshot of the issue numbers at seeding time. Titles in `issues.json` stay the source of truth: `scripts/seed_github.py` matches existing issues by title, so do not rename seeded issues without updating `issues.json`.

## M0 Discovery & legal

Due Fri 23 Oct 2026 (weeks 1-2).

| Issue | Title | Type | Priority |
|---|---|---|---|
| [#1](https://github.com/Ansh-Sonkusare/family-money-finder/issues/1) | Epic — M0 Discovery & legal | epic | n/a |
| [#5](https://github.com/Ansh-Sonkusare/family-money-finder/issues/5) | Commission legal opinion on the six open questions | legal | P0 |
| [#6](https://github.com/Ansh-Sonkusare/family-money-finder/issues/6) | Compile bank transmission thresholds and claim procedures (top banks) | research | P0 |
| [#7](https://github.com/Ansh-Sonkusare/family-money-finder/issues/7) | Compile mutual fund transmission procedures (CAMS, KFintech, MITRA) | research | P0 |
| [#8](https://github.com/Ansh-Sonkusare/family-money-finder/issues/8) | Compile insurer and EPF death-claim procedures | research | P0 |
| [#9](https://github.com/Ansh-Sonkusare/family-money-finder/issues/9) | Document the IEPF claim procedure and timelines | research | P0 |
| [#10](https://github.com/Ansh-Sonkusare/family-money-finder/issues/10) | Run 20 family interviews and write the synthesis | research | P0 |
| [#11](https://github.com/Ansh-Sonkusare/family-money-finder/issues/11) | Close the competitor sweep and verify headline figures | research | P1 |
| [#12](https://github.com/Ansh-Sonkusare/family-money-finder/issues/12) | Draft the authority-verification policy and consent notice | legal | P0 |
| [#13](https://github.com/Ansh-Sonkusare/family-money-finder/issues/13) | Set up repository, CI, landing page and intake form | ops | P0 |

## M1 Prototype

Due Fri 30 Oct 2026 (week 3).

| Issue | Title | Type | Priority |
|---|---|---|---|
| [#2](https://github.com/Ansh-Sonkusare/family-money-finder/issues/2) | Epic — M1 Prototype | epic | n/a |
| [#14](https://github.com/Ansh-Sonkusare/family-money-finder/issues/14) | Recruit and onboard 10 to 15 consented families | gtm | P0 |
| [#15](https://github.com/Ansh-Sonkusare/family-money-finder/issues/15) | Run the concierge sweep with user-assisted portal guides | ops | P0 |
| [#16](https://github.com/Ansh-Sonkusare/family-money-finder/issues/16) | Build the procedures knowledge base and matrix loader | build | P0 |
| [#17](https://github.com/Ansh-Sonkusare/family-money-finder/issues/17) | Prototype the rules engine: route and document list | build | P0 |
| [#18](https://github.com/Ansh-Sonkusare/family-money-finder/issues/18) | Pack generator v0: bank deceased-depositor claim pack | build | P0 |
| [#19](https://github.com/Ansh-Sonkusare/family-money-finder/issues/19) | Pack generator v0: mutual fund RTA transmission pack | build | P0 |
| [#20](https://github.com/Ansh-Sonkusare/family-money-finder/issues/20) | Pack generator v0: IEPF Form IEPF-5 pack | build | P0 |
| [#21](https://github.com/Ansh-Sonkusare/family-money-finder/issues/21) | Build the eval harness and the first 30 golden items | eval | P0 |
| [#22](https://github.com/Ansh-Sonkusare/family-money-finder/issues/22) | Create the reviewer checklist and reason-code taxonomy | ops | P0 |
| [#23](https://github.com/Ansh-Sonkusare/family-money-finder/issues/23) | Rehearse and record the prototype demo on a synthetic family | design | P1 |

## M2 MVP

Due Fri 11 Dec 2026 (weeks 4-9).

| Issue | Title | Type | Priority |
|---|---|---|---|
| [#3](https://github.com/Ansh-Sonkusare/family-money-finder/issues/3) | Epic — M2 MVP | epic | n/a |
| [#24](https://github.com/Ansh-Sonkusare/family-money-finder/issues/24) | Intake, consent and authority-check flow | build | P0 |
| [#25](https://github.com/Ansh-Sonkusare/family-money-finder/issues/25) | Vault: encrypted storage, PAN field encryption and Aadhaar redaction | build | P0 |
| [#26](https://github.com/Ansh-Sonkusare/family-money-finder/issues/26) | Document extraction with validators | build | P0 |
| [#27](https://github.com/Ansh-Sonkusare/family-money-finder/issues/27) | Entity matching with a reviewer queue | build | P0 |
| [#28](https://github.com/Ansh-Sonkusare/family-money-finder/issues/28) | Rules engine v1: versioned matrix with effective dates | build | P0 |
| [#29](https://github.com/Ansh-Sonkusare/family-money-finder/issues/29) | Ranking and the ranked claim list | build | P0 |
| [#30](https://github.com/Ansh-Sonkusare/family-money-finder/issues/30) | Pack generator v1: insurance packs and EPF death-claim pack | build | P0 |
| [#31](https://github.com/Ansh-Sonkusare/family-money-finder/issues/31) | Reviewer console | build | P0 |
| [#32](https://github.com/Ansh-Sonkusare/family-money-finder/issues/32) | Claim tracker, reminders, escalation drafts and heir status page | build | P0 |
| [#33](https://github.com/Ansh-Sonkusare/family-money-finder/issues/33) | Audit log, retention and deletion | build | P0 |
| [#34](https://github.com/Ansh-Sonkusare/family-money-finder/issues/34) | Extend the golden set to 60 items and add the CI regression gate | eval | P0 |
| [#35](https://github.com/Ansh-Sonkusare/family-money-finder/issues/35) | NRI remote-consent flow, local-representative marker and repatriation checklist | build | P0 |
| [#36](https://github.com/Ansh-Sonkusare/family-money-finder/issues/36) | Flat-fee payments in test mode | build | P1 |
| [#37](https://github.com/Ansh-Sonkusare/family-money-finder/issues/37) | Decide model hosting and complete the compliance pre-pilot review | legal | P0 |

## M3 Pilot & decision

Due Fri 29 Jan 2027, day-90 checkpoint Fri 8 Jan 2027 (weeks 10-16).

| Issue | Title | Type | Priority |
|---|---|---|---|
| [#4](https://github.com/Ansh-Sonkusare/family-money-finder/issues/4) | Epic — M3 Pilot & decision | epic | n/a |
| [#38](https://github.com/Ansh-Sonkusare/family-money-finder/issues/38) | Pilot onboarding: terms, fee flow and operations runbook | ops | P0 |
| [#39](https://github.com/Ansh-Sonkusare/family-money-finder/issues/39) | Acquire 40 to 50 pilot families across channels | gtm | P0 |
| [#40](https://github.com/Ansh-Sonkusare/family-money-finder/issues/40) | Recruit local representatives for NRI cases in two cities | ops | P1 |
| [#41](https://github.com/Ansh-Sonkusare/family-money-finder/issues/41) | Weekly eval runs and the leading-indicator dashboard | eval | P0 |
| [#42](https://github.com/Ansh-Sonkusare/family-money-finder/issues/42) | Partner outreach and Project 1 cross-sell test | gtm | P1 |
| [#43](https://github.com/Ansh-Sonkusare/family-money-finder/issues/43) | Day-90 checkpoint and week-16 decision review | ops | P0 |

## GitHub milestones and labels

The four GitHub milestones exist with their due dates (M0 Fri 23 Oct 2026, M1 Fri 30 Oct 2026, M2 Fri 11 Dec 2026, M3 Fri 29 Jan 2027), and every epic and work item is attached to its milestone. Labels carry the standard colours and descriptions, and each work item is a sub-issue of its milestone's `Epic — <milestone>` issue.

When `planning/issues.json` gains new entries, re-run the seed script; it matches issues by title, creates only what is missing and never removes anything:

```bash
export GITHUB_TOKEN=...   # fine-grained token with Issues: read and write on this repository
python3 scripts/seed_github.py --owner Ansh-Sonkusare --repo-path . --dry-run   # preview
python3 scripts/seed_github.py --owner Ansh-Sonkusare --repo-path . --sync
```

New issues created this way are attached to their milestone but not to an epic; link them as sub-issues of the matching epic in the GitHub UI.
