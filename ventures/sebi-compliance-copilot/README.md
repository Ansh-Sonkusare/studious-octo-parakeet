# SEBI Compliance Copilot

**Status: Pre-prototype, planning.** Last updated 8 Oct 2026. Project 4 of the India AI personal-finance research (rank 4 of 14, weighted score 3.65/5).

## Pitch

An AI tool that checks every social post, WhatsApp broadcast, web page and email from a SEBI-regulated intermediary against SEBI's Common Advertisement Code (CAC). It prepares the 24-hour post-publication report, archives tamper-evident evidence, and generates AI-use disclosures, suitability rationales and advice audit trails. A CSCRF (cybersecurity framework) kit is the second module.

Target customers are registered investment advisers (RIAs), research analysts (RAs), portfolio managers (PMS), brokers and the roughly 3,350 top mutual-fund distributors (MFDs). The tool is decision support: it never posts, never files and never selects securities. The firm stays responsible and a named human approves every filing.

## The problem in three numbers

| Number | Meaning | Source |
|---|---|---|
| **24 hours** | Under the CAC approved by SEBI's board on 24 Sept 2026, most ads move from prior approval to reporting within 24 hours of publication. Notified text and effective date: **[Unconfirmed]** | [exchange4media](https://www.exchange4media.com/marketing-news/sebi-relaxes-advertising-norms-keeps-celebrity-endorsements-under-prior-approval-158597.html), via [HANDOFF](docs/HANDOFF.md) |
| **About 6,400 firms** | About 1,000 RIAs, 1,500 RAs, 515 to 530+ PMS managers and 3,350 top MFDs; brokers not counted because the count is unknown. Counts conflict across sources, so treat as a range | [HANDOFF section 2](docs/HANDOFF.md) |
| **About ₹22 crore a year** | Theoretical India ceiling at 100% penetration and assumed prices (₹20-50k for RIAs/RAs, ₹1.5 lakh for PMS). A small market: a wedge and side line, not a venture-scale business alone | [HANDOFF section 8](docs/HANDOFF.md) |

No Indian specialist vendor for AI ad-compliance was found. That is an absence in search results, not proof; the interviews will test it.

## How it works

1. The firm sends a draft or published item by paste, URL, email forward or WhatsApp export.
2. The tool records a SHA-256 hash and UTC time and stores an immutable capture.
3. It classifies: advertisement or not, celebrity or not, entity type, channel.
4. It runs deterministic checks, then retrieval-backed model-judged checks. Every finding quotes a clause from a versioned rule pack.
5. A reviewer approves, edits or rejects. The firm publishes; the tool captures the as-published version.
6. It prepares the 24-hour report pack and tracks the deadline. A named human files.
7. Everything is archived with an append-only, hash-chained audit log.

Rule packs carry a status. Draft-derived rules show as "advisory, pending notification" until the notified text is confirmed.

## Status and milestones

The team plan assumes 1 to 3 dedicated people starting Mon 12 Oct 2026. Timing depends on SEBI notifying the CAC; see the contingency scenarios in the [plan](docs/PROTOTYPE_AND_MVP_PLAN.md).

| Milestone | Due | Outcome |
|---|---|---|
| M0 Discovery & legal | 23 Oct 2026 | Ad-code status known; 15 interviews; 3 design partners; labelled-set collection started; rules corpus v0; legal opinion commissioned |
| M1 Prototype | 30 Oct 2026 | Classifier and rule checker on 150 labelled real public posts; evidence archive; sample 24-hour report; eval harness |
| M2 MVP | 11 Dec 2026 | Hosted MVP with review console, report pack, versioned rule packs; 300+ labelled items; checkpoint 20 Nov |
| M3 Pilot & decision | 29 Jan 2027 | 5+ weekly firms; pricing tests; 500-item evaluation; penetration test; scale, pivot or stop memo; checkpoint 8 Jan |

## Repository map

| Path | Contents |
|---|---|
| [docs/HANDOFF.md](docs/HANDOFF.md) | Market case, product spec, business model, risks, kill criteria (source of truth for scope) |
| [docs/PROTOTYPE_AND_MVP_PLAN.md](docs/PROTOTYPE_AND_MVP_PLAN.md) | Build plan: timeline, specs, technical design, evaluation, legal gates, cost |
| [docs/DECISIONS.md](docs/DECISIONS.md) | Decision records (ADRs) |
| [docs/research/](docs/research/README.md) | Research reports and notes, with an index |
| [planning/milestones.md](planning/milestones.md) | Milestones, goals and exit criteria |
| [planning/issues.json](planning/issues.json) | 39 issues ready to import into the tracker, grouped by milestone, with labels |
| [CONTRIBUTING.md](CONTRIBUTING.md) | Branching, pull-request checklist, data rules |

Code directories (`apps/`, `packages/`, `rules/`, `eval/`) are planned in section 7 of the plan and do not exist yet.

## Key risks

1. **Small market** (about 2,500 RIA/RA firms plus PMS and top MFDs). Treat as a wedge; keep burn low.
2. **Ad code not yet notified, or the final text differs from the draft.** Version rule packs, stay useful without the filing step, watch SEBI weekly.
3. **False negatives** (the tool clears a breaching post). Recall gates, human review of high-severity items, decision-support positioning, evidence logs.
4. **Bundled free competition** from MFD platforms, or tiered AI rules from SEBI. Stay platform-agnostic; build human oversight, kill switch and logging from day one.
5. **Data and vendor-risk exposure**, including offshore model use for regulated firms (localisation position **[Unconfirmed]**). Zero-retention vendors, India hosting, DPA, penetration test.

Full list: [HANDOFF section 12](docs/HANDOFF.md).

## Key links

- Regulatory timeline and sources: [HANDOFF section 2](docs/HANDOFF.md)
- Kill and pivot criteria: [HANDOFF section 11](docs/HANDOFF.md)
- Open questions: [HANDOFF section 13](docs/HANDOFF.md)
- SEBI primary source to verify against: sebi.gov.in (most facts in this repo come from secondary coverage gathered on 7 Oct 2026)

## Next actions

1. Search sebi.gov.in for the notified CAC text and start the weekly SEBI watch.
2. Book and run the first interviews; target 15 by 23 Oct.
3. Commission the legal opinion on the "no licence" position and offshore model use.
4. Sign three design partners with data-use consent.
5. Start collecting public posts for the labelled set and finalise the labelling guide.
6. Create the repository scaffold and import `planning/issues.json`.
