# Health Claim Recovery Agent

An AI-assisted service that recovers rejected and short-paid health-insurance claims for Indian policyholders. It reads the policy wording and the insurer's rejection or settlement letter, maps every deduction to the clause and IRDAI rule behind it, drafts the insurer grievance and, if needed, the Bima Bharosa and Insurance Ombudsman complaints, and tracks the case until money is recovered. A human reviewer approves every letter, every number comes from deterministic code rather than the model, and the user files with their own login. The product earns an upfront filing fee plus a success fee, never takes money from insurers, brokers or hospitals, and never holds client money. India comes first; the same engine may later address US health-denial appeals.

**Status: pre-prototype, planning.** No code exists yet. The planning start date is Monday 12 October 2026.

## The problem in three numbers

| Number | What it means | Source |
|---|---|---|
| **₹26,037.65 crore** | Health claims rejected or disallowed in FY24 (about ₹15,100 crore disallowed under policy terms, about ₹10,937 crore repudiated) | [Moneylife, Lok Sabha reply](https://moneylife.in/article/health-insurance-claims-worth-rs2603765-crore-rejected-by-insurers-in-fy2324-govt/76282.html) |
| **31,490** | Health-insurance complaints to the Insurance Ombudsman in FY24, up from 25,873; about 95% concerned claim rejections | [Outlook Money](https://www.outlookmoney.com/amp/story/personal-finance/why-95-per-cent-of-health-insurance-complaints-concern-claim-rejections) |
| **+35%** | Growth in Bima Bharosa grievances from 47,658 (FY24) to 64,365 (FY25), all insurance lines | [TaxGuru](https://taxguru.in/?p=1035064) |

These figures come from secondary coverage of regulator and parliamentary data; some conflict (for example FY25 Ombudsman totals), and the reasons for rejection are not published by insurer. See [docs/HANDOFF.md](docs/HANDOFF.md) section 2 for the caveats.

## How it works

1. The user sends documents (policy, rejection or settlement letter, discharge summary, bills) by WhatsApp or web, after giving consent.
2. Within minutes the user receives a **Claim X-ray**: each deduction, the clause that supports it, the amount likely recoverable, the route and the deadline. Deductions that look valid are labelled as such and are not charged for.
3. The user accepts the fee terms.
4. The agent drafts the insurer grievance; a human reviewer approves or edits it; the user submits it using their own login and OTP.
5. If the insurer has not resolved the matter in 30 days, the agent prepares the Bima Bharosa and Ombudsman filings and keeps a dated case file.
6. On recovery the fee is collected and the outcome is logged (anonymised and only with consent).

Design rules: retrieval plus tools, no fine-tuning; numbers only from tested calculators, enforced by a validator; mandatory clause citations; an append-only audit log. Details: [docs/PROTOTYPE_AND_MVP_PLAN.md](docs/PROTOTYPE_AND_MVP_PLAN.md) and [docs/DECISIONS.md](docs/DECISIONS.md).

## Milestones

Assumes a dedicated team of one to three people starting Monday 12 October 2026. Dates are targets, not commitments.

| Milestone | Window | Due | Outcome |
|---|---|---|---|
| M0 Discovery & legal | Weeks 1-2 | 23 Oct 2026 | 30 interviews, legal opinion commissioned, consent foundations, first consented files |
| M1 Prototype | Weeks 1-3 | 30 Oct 2026 | Concierge service, working Claim X-ray on real documents, eval harness |
| M2 MVP | Weeks 4-9 | 11 Dec 2026 | Automated intake, analysis, letter drafting, review console, tracking, payments |
| M3 Pilot & decision | Weeks 10-16 | 29 Jan 2027 | 50-100 live cases, metrics read-out, continue / pivot / stop memo |

Success in the pilot (proposed thresholds): clause-citation precision at least 95% with zero invented clauses; at least 25% reversal at the insurer stage within 30 days; at least 30% fee acceptance and 70% of success fees collected; acquisition cost below 30% of the expected fee; reviewer time below 20 minutes per case. See [planning/milestones.md](planning/milestones.md).

## Repository map

| Path | What it is |
|---|---|
| [docs/HANDOFF.md](docs/HANDOFF.md) | The handoff: problem, evidence, users, competition, product spec, architecture, legal position, business model, go-to-market, metrics, risks, open questions |
| [docs/PROTOTYPE_AND_MVP_PLAN.md](docs/PROTOTYPE_AND_MVP_PLAN.md) | Prototype and MVP plan: week-by-week timeline, specs, technical design, evaluation plan, legal gates, costs |
| [docs/DECISIONS.md](docs/DECISIONS.md) | Decision log (lightweight ADRs) |
| [docs/research/](docs/research/README.md) | Desk research behind the project, with an index |
| [planning/milestones.md](planning/milestones.md) | The four milestones with dates, goals and exit criteria |
| [planning/issues.json](planning/issues.json) | Seed backlog of 40 issues (title, body, labels, milestone) ready to import into an issue tracker |
| [CONTRIBUTING.md](CONTRIBUTING.md) | Branching, pull-request checklist, data rules |
| `src/`, `eval/`, `corpus/`, `tests/`, `site/`, `infra/` | Planned implementation directories; see the proposed layout in the plan (section 7). Not yet created |

## Key risks

- **Legal.** Whether a non-lawyer service may assist before the Ombudsman, and whether success fees are enforceable, is unverified. A written legal opinion is a launch gate.
- **Correctness.** A wrong clause or amount harms the user's case. Mitigated by tools for all numbers, mandatory citations, a validator and a golden-set release gate.
- **Demand and acquisition cost.** Demand is episodic; the plan implies roughly 420 qualified leads are needed for 50 filed cases at threshold conversion rates.
- **Fee collection.** Users may not pay a success fee after recovery. Mitigated by an upfront fee and a flat-fee fallback.
- **Insurer pushback** against templated complaints. Mitigated by a case-specific, evidence-backed letter each time and no mass filing.
- **Health-data breach.** Mitigated by minimisation, encryption, access control, deletion and a breach runbook.
- **Weak source data.** Most figures are secondary; primary verification is scheduled in week 1-2.

The full list is in [docs/HANDOFF.md](docs/HANDOFF.md) section 12 and the schedule risks in the [plan](docs/PROTOTYPE_AND_MVP_PLAN.md) section 12.

## How to contribute and next actions

1. Read [docs/HANDOFF.md](docs/HANDOFF.md), then the [plan](docs/PROTOTYPE_AND_MVP_PLAN.md), then [CONTRIBUTING.md](CONTRIBUTING.md).
2. Import [planning/issues.json](planning/issues.json) into the tracker and create the four milestones from [planning/milestones.md](planning/milestones.md).
3. Start the week-1 items: engage counsel and a claims specialist, file incorporation, begin interviews, draft the consent notice, apply for WhatsApp Business verification.
4. Scaffold the code repository layout and CI (issue in M1).
5. Never commit real customer documents or personal data.

*This repository contains planning material, not legal, medical or financial advice. Regulatory conclusions need confirmation by counsel.*
