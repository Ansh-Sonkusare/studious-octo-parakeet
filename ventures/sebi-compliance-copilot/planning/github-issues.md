# GitHub issue index

The backlog in [issues.json](issues.json) is mirrored as GitHub issues in the private repository `Ansh-Sonkusare/sebi-compliance-copilot`: four epics, one per milestone in [milestones.md](milestones.md), and 39 issues, each attached to its epic as a sub-issue. Titles, labels and bodies match `issues.json`; the repository-relative links in the original bodies are absolute here so they work from GitHub. `issues.json` stays the source of truth: change it first, then update the issue.

Links need a signed-in account with access to the private repository.

## M0 Discovery & legal

Epic: [#1](https://github.com/Ansh-Sonkusare/sebi-compliance-copilot/issues/1) (due Fri 23 Oct 2026, weeks 1 to 2)

| Issue | Title | Type | Priority |
|---|---|---|---|
| [#5](https://github.com/Ansh-Sonkusare/sebi-compliance-copilot/issues/5) | Locate notified Common Advertisement Code text and log effective date and reporting channel | research | P0 |
| [#6](https://github.com/Ansh-Sonkusare/sebi-compliance-copilot/issues/6) | Commission legal opinion on the no-licence position and suitability drafting | legal | P0 |
| [#7](https://github.com/Ansh-Sonkusare/sebi-compliance-copilot/issues/7) | Confirm record-retention, data-localisation and offshore-model position; select hosting and model vendor terms | legal | P0 |
| [#8](https://github.com/Ansh-Sonkusare/sebi-compliance-copilot/issues/8) | Run 15 interviews with RIAs, RAs and compliance officers | research | P0 |
| [#9](https://github.com/Ansh-Sonkusare/sebi-compliance-copilot/issues/9) | Recruit and sign three design partners with data-use consent | gtm | P0 |
| [#10](https://github.com/Ansh-Sonkusare/sebi-compliance-copilot/issues/10) | Collect first 60 public posts and define the collection protocol for the labelled dataset | eval | P0 |
| [#11](https://github.com/Ansh-Sonkusare/sebi-compliance-copilot/issues/11) | Write the labelling guide and set up annotation tooling | eval | P0 |
| [#12](https://github.com/Ansh-Sonkusare/sebi-compliance-copilot/issues/12) | Define the rule schema and load rules corpus v0 with sources | build | P0 |
| [#13](https://github.com/Ansh-Sonkusare/sebi-compliance-copilot/issues/13) | Bootstrap repository, CI and environments | ops | P1 |

## M1 Prototype

Epic: [#2](https://github.com/Ansh-Sonkusare/sebi-compliance-copilot/issues/2) (due Fri 30 Oct 2026, week 3)

| Issue | Title | Type | Priority |
|---|---|---|---|
| [#14](https://github.com/Ansh-Sonkusare/sebi-compliance-copilot/issues/14) | Build ad / not-ad and celebrity classifier (small model, structured output) | build | P0 |
| [#15](https://github.com/Ansh-Sonkusare/sebi-compliance-copilot/issues/15) | Implement the deterministic rule checker v0 | build | P0 |
| [#16](https://github.com/Ansh-Sonkusare/sebi-compliance-copilot/issues/16) | Implement model-judged checks with retrieval and a citation validator | build | P0 |
| [#17](https://github.com/Ansh-Sonkusare/sebi-compliance-copilot/issues/17) | Build the evidence archive prototype (hash, timestamp, snapshot) | build | P0 |
| [#18](https://github.com/Ansh-Sonkusare/sebi-compliance-copilot/issues/18) | Generate the sample 24-hour report (template, format unconfirmed) | build | P0 |
| [#19](https://github.com/Ansh-Sonkusare/sebi-compliance-copilot/issues/19) | Build the evaluation harness v0 | eval | P0 |
| [#20](https://github.com/Ansh-Sonkusare/sebi-compliance-copilot/issues/20) | Label 150 items double-blind with adjudication | eval | P0 |
| [#21](https://github.com/Ansh-Sonkusare/sebi-compliance-copilot/issues/21) | Prepare and run the prototype demo and reviewer walkthroughs | design | P1 |
| [#22](https://github.com/Ansh-Sonkusare/sebi-compliance-copilot/issues/22) | Publish prototype baseline results and the top-10 misses | eval | P1 |

## M2 MVP

Epic: [#3](https://github.com/Ansh-Sonkusare/sebi-compliance-copilot/issues/3) (due Fri 11 Dec 2026, weeks 4 to 9)

| Issue | Title | Type | Priority |
|---|---|---|---|
| [#23](https://github.com/Ansh-Sonkusare/sebi-compliance-copilot/issues/23) | Design and migrate the core data model with row-level security | build | P0 |
| [#24](https://github.com/Ansh-Sonkusare/sebi-compliance-copilot/issues/24) | Implement authentication, firm onboarding and role-based access | build | P0 |
| [#25](https://github.com/Ansh-Sonkusare/sebi-compliance-copilot/issues/25) | Implement web paste, URL and email-forward intake | build | P0 |
| [#26](https://github.com/Ansh-Sonkusare/sebi-compliance-copilot/issues/26) | Implement WhatsApp broadcast intake via export upload and forwarded drafts | build | P0 |
| [#27](https://github.com/Ansh-Sonkusare/sebi-compliance-copilot/issues/27) | Build the review console with approvals and decision logging | build | P0 |
| [#28](https://github.com/Ansh-Sonkusare/sebi-compliance-copilot/issues/28) | Build rule-pack versioning, status flags and the release workflow | build | P0 |
| [#29](https://github.com/Ansh-Sonkusare/sebi-compliance-copilot/issues/29) | Build the 24-hour report pack and deadline tracker | build | P0 |
| [#30](https://github.com/Ansh-Sonkusare/sebi-compliance-copilot/issues/30) | Implement immutable evidence store and hash-chained audit log | build | P0 |
| [#31](https://github.com/Ansh-Sonkusare/sebi-compliance-copilot/issues/31) | Implement the AI-use disclosure generator | build | P1 |
| [#32](https://github.com/Ansh-Sonkusare/sebi-compliance-copilot/issues/32) | Implement the suitability rationale drafter (RIA approves) | build | P1 |
| [#33](https://github.com/Ansh-Sonkusare/sebi-compliance-copilot/issues/33) | Scale the labelled set to 300 and enforce evaluation gates in CI | eval | P0 |
| [#34](https://github.com/Ansh-Sonkusare/sebi-compliance-copilot/issues/34) | Publish the CSCRF-lite calendar and templates before 30 Nov 2026 | build | P1 |
| [#35](https://github.com/Ansh-Sonkusare/sebi-compliance-copilot/issues/35) | Build the monthly ad register and audit-pack export | build | P1 |
| [#36](https://github.com/Ansh-Sonkusare/sebi-compliance-copilot/issues/36) | Draft terms of service, DPA and liability cap for counsel review | legal | P0 |

## M3 Pilot & decision

Epic: [#4](https://github.com/Ansh-Sonkusare/sebi-compliance-copilot/issues/4) (due Fri 29 Jan 2027, weeks 10 to 16)

| Issue | Title | Type | Priority |
|---|---|---|---|
| [#37](https://github.com/Ansh-Sonkusare/sebi-compliance-copilot/issues/37) | Onboard and support at least five design-partner firms on live workflows | gtm | P0 |
| [#38](https://github.com/Ansh-Sonkusare/sebi-compliance-copilot/issues/38) | Run pricing tests at 20k, 35k and 50k rupees a year | gtm | P0 |
| [#39](https://github.com/Ansh-Sonkusare/sebi-compliance-copilot/issues/39) | Final evaluation on 500 labelled items against gates | eval | P0 |
| [#40](https://github.com/Ansh-Sonkusare/sebi-compliance-copilot/issues/40) | Commission and complete an external penetration test | ops | P1 |
| [#41](https://github.com/Ansh-Sonkusare/sebi-compliance-copilot/issues/41) | Launch the consultant-partner programme | gtm | P1 |
| [#42](https://github.com/Ansh-Sonkusare/sebi-compliance-copilot/issues/42) | Review DPDP consent, retention and deletion flows | legal | P1 |
| [#43](https://github.com/Ansh-Sonkusare/sebi-compliance-copilot/issues/43) | Write the scale, pivot or stop decision memo | ops | P0 |

## GitHub milestones and labels

The four GitHub milestones exist with their due dates (M0 Fri 23 Oct 2026, M1 Fri 30 Oct 2026, M2 Fri 11 Dec 2026, M3 Fri 29 Jan 2027), and every epic and work item is attached to its milestone. Labels carry the standard colours and descriptions, and each work item is a sub-issue of its milestone's `Epic — <milestone>` issue.

When `planning/issues.json` gains new entries, re-run the seed script; it matches issues by title, creates only what is missing and never removes anything:

```bash
export GITHUB_TOKEN=...   # fine-grained token with Issues: read and write on this repository
python3 scripts/seed_github.py --owner Ansh-Sonkusare --repo-path . --dry-run   # preview
python3 scripts/seed_github.py --owner Ansh-Sonkusare --repo-path . --sync
```

New issues created this way are attached to their milestone but not to an epic; link them as sub-issues of the matching epic in the GitHub UI.
