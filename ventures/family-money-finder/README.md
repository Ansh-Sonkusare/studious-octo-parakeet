# Family Money Finder

An AI-assisted concierge that helps a family find the unclaimed money a loved one left behind in India, work out exactly what each institution needs, prepare the paperwork, and follow every claim through to payment.

**Status: Pre-prototype, planning.** No code yet. Plan start is Monday 12 October 2026. Labels used throughout: **Assumption** = number to replace with pilot data; **Inference** = team judgement, not sourced; **Conflict** = sources disagree; **Unverified** = a legal or regulatory point that counsel or a primary document must confirm.

## The pitch

When a parent dies, the records are scattered across banks, mutual fund folios, share certificates, insurance policies and provident fund accounts. Searching is free, but claiming is paper-heavy, different at every institution, and often needs branch visits. The people doing this are adult children, often grieving and short of time, and NRIs who cannot attend a branch.

Family Money Finder, with the family's consent and proof of authority, searches for the family's unclaimed assets, ranks what it finds, builds a reviewed document pack for each institution (including succession and transmission paperwork), and tracks each claim until the money arrives. The claimant signs and submits. The product prepares and guides, never holds client money, and never advises on what to do with inherited investments.

## The problem in three numbers

| Number | What it shows | Source and caveat |
|---|---|---|
| About ₹2.2 lakh crore | Headline pool of unclaimed money across banks, EPF, insurance, shares and mutual funds | [Business Today](https://www.businesstoday.in/amp/personal-finance/news/story/rs-22-lakh-crore-unclaimed-funds-lie-idle-across-banks-epf-insurance-stocks-mfs-524958-2026-04-10). Treat as upper-end; component sums run from about ₹1.82 to ₹2.19 lakh crore (inference) |
| About 2.6% | Share returned: ₹5,777 crore across about 23 lakh claims through government drives (Feb 2026), roughly ₹25,000 a claim | [Sentinel Assam](https://www.sentinelassam.com/more-news/national-news/government-steps-up-efforts-to-return-rs-73000-cr-unclaimed-funds-minister-pankaj-chaudhary); the percentage is an inference |
| ₹89,004 crore vs ₹77.82 crore | Shares held by the IEPF (30 Nov 2025) against dividends refunded in two years, while 75,417 claims were approved | [Business Today](https://www.businesstoday.in/amp/personal-finance/investment/story/reliance-industries-tops-iepf-unclaimed-shares-rs89000-crore-stuck-across-1671-companies-report-525182-2026-04-12); [Outlook Money](https://www.outlookmoney.com/personal-finance/unclaimed-funds-in-iepf-over-75000-claims-approved-in-two-years-rs-7782-crore-dividend-refunded). The two figures measure different things |

**Conflicting figures.** Unclaimed bank deposits in the RBI DEA Fund are ₹72,454 crore (28 Jan 2026) in one parliamentary answer and ₹86,917 crore (30 Jun 2026) in another; other reports give ₹67,000 crore, ₹78,213 crore, ₹97,545 crore and ₹98,073 crore. Insurance totals differ more than twofold (₹20,062 crore versus ₹8,973.89 crore). Verify against primary documents before external use. See [docs/HANDOFF.md](docs/HANDOFF.md) section 2.

## How it works

1. **Intake and authority check.** The heir consents and provides the death certificate and relationship proof. No deceased-person search starts before this check.
2. **Discovery sweep.** The app prepares exact inputs for UDGAM (banks), the IEPF portal, MITRA or a CAS upload (mutual funds), insurer pages and EPFO. The heir runs the searches with their own logins and OTPs; the product never stores credentials or scrapes behind a login.
3. **Match and rank.** Records are matched across spelling variants and ranked by value, ease and expected time.
4. **Route and requirements.** A deterministic rules engine over a versioned, sourced requirement matrix decides nominee versus legal-heir route, and which documents each institution needs.
5. **Pack generation and human review.** Templates produce claim forms, indemnity and affidavit drafts, a checklist and a cover letter. A person reviews every outbound document.
6. **Submit and track.** The family or a local representative submits. The tracker handles reminders, follow-ups and escalation drafts.

## Status and milestones

Pre-prototype, planning. Dates assume a dedicated team of 1 to 3 people starting Monday 12 October 2026.

| Milestone | Due | What is delivered |
|---|---|---|
| M0 Discovery & legal | Fri 23 Oct 2026 | Institution-specific thresholds and procedures compiled; legal opinion commissioned; 20 family interviews |
| M1 Prototype | Fri 30 Oct 2026 | Concierge search for 10 to 15 families; procedures knowledge base; packs for banks, mutual-fund RTAs and IEPF; eval harness |
| M2 MVP | Fri 11 Dec 2026 | Full flow in software; golden-set gates green; reviewer console; tracker |
| M3 Pilot & decision | Fri 29 Jan 2027 (day-90 checkpoint Fri 8 Jan) | Paid pilot with 40 to 50 families (assumption); continue, pivot or stop decision |

IEPF claims are slow, so pilot metrics use leading indicators (found, ready, filed, engaged, paid). Details: [docs/PROTOTYPE_AND_MVP_PLAN.md](docs/PROTOTYPE_AND_MVP_PLAN.md) and [planning/milestones.md](planning/milestones.md).

## Repository map

| Path | Contents |
|---|---|
| [docs/HANDOFF.md](docs/HANDOFF.md) | Product definition: problem, users, scope, architecture, legal, business model, 90-day plan, metrics, risks |
| [docs/PROTOTYPE_AND_MVP_PLAN.md](docs/PROTOTYPE_AND_MVP_PLAN.md) | Prototype and MVP specs, week-by-week timeline, technical design, evaluation plan, gates, cost |
| [docs/DECISIONS.md](docs/DECISIONS.md) | Architecture and product decision records |
| [docs/research/](docs/research/README.md) | Research notes and full report behind the handoff (index inside) |
| [planning/milestones.md](planning/milestones.md) | M0 to M3 goals, dates and exit criteria |
| [planning/issues.json](planning/issues.json) | Backlog as JSON (title, body, labels, milestone), ready to import into GitHub |
| [CONTRIBUTING.md](CONTRIBUTING.md) | Branching, pull request checklist, data rules |

Planned code layout (not yet created) is in section 7 of the plan: `apps/web`, `packages/*`, `workers/cas-parser`, `eval/`, `supabase/`.

## Key links

- Product definition: [docs/HANDOFF.md](docs/HANDOFF.md)
- Research index: [docs/research/README.md](docs/research/README.md)
- UDGAM claim friction: [Outlook Money](https://www.outlookmoney.com/banking/udgam-how-to-claim-unclaimed-bank-deposits-through-rbis-portal)
- RBI DEA Fund guidelines (revised 25 Jun 2025): [RBI PDF](https://website.rbi.org.in/documents/87730/39016390/GuidelinesDEAFund25062025_AN6.pdf)

## Key risks

| Risk | Mitigation |
|---|---|
| IEPF claims are slow | Set expectations in writing; flat pricing for IEPF packs; measure leading indicators and payouts excluding IEPF |
| Wrong requirement or form; legal-practice challenge (**unverified**) | Rules engine plus retrieval only; human review of every document; golden-set gates; counsel's opinion before charging; claimant signs; court work referred to advocates |
| Branch visits and institution-specific demands | Sourced requirement matrix; per-branch checklists; local representatives for NRIs |
| A bereaved user | Plain language, short flows, no upsell in the first message, a human contact option |
| Sensitive data (PAN, death certificates) and DPDP duties | Encryption, minimal retention, masking before model calls, breach drill; offshore model processing awaits legal review |
| Impersonation | Authority check before any deceased-person search; consent for living parents |
| Weak willingness to pay; episodic demand | Test the flat Estate Pack plus capped success fee in the pilot; partner channels; pivot paths in HANDOFF section 11 |

## Next actions

1. Engage counsel and commission the legal opinion on the six open questions (week 1).
2. Compile institution-specific succession, legal-heir and indemnity thresholds and procedures for the first 10 institutions, each with source and date (weeks 1 to 2).
3. Run 20 family interviews and recruit three prototype families (weeks 1 to 2).
4. Close the competitor sweep and verify the DEA Fund and insurance figures (week 1).
5. Set up the repository, CI and landing page, then build toward the 30 October prototype demo.
