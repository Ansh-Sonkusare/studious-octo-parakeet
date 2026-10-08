# Milestones

Plan start: Monday 12 October 2026. Full week-by-week plan and specifications: [docs/PROTOTYPE_AND_MVP_PLAN.md](../docs/PROTOTYPE_AND_MVP_PLAN.md). Issues for each milestone: [planning/issues.json](issues.json).

Labels follow [HANDOFF.md](../docs/HANDOFF.md): **Assumption** = number to replace with pilot data; thresholds are proposals.

| Milestone | Due | Weeks |
|---|---|---|
| M0 Discovery & legal | Fri 23 Oct 2026 | 1-2 |
| M1 Prototype | Fri 30 Oct 2026 | 3 |
| M2 MVP | Fri 11 Dec 2026 | 4-9 |
| M3 Pilot & decision | Fri 29 Jan 2027 (day-90 checkpoint Fri 8 Jan 2027) | 10-16 |

## M0 Discovery & legal

**Due:** Friday 23 October 2026.

**Goal.** Know the institution-specific rules, the legal position and what real families need, before building anything beyond a template.

**Scope**
- Institution-specific succession, legal-heir and indemnity thresholds and claim procedures for the top banks, CAMS, KFintech, top insurers and IEPF, each with source and retrieval date.
- Legal opinion commissioned on the six questions in HANDOFF section 7.
- 20 family interviews (adult children and NRIs) plus a few CAs and advocates.
- Competitor sweep completed (fee-based IEPF agents, will and estate startups).
- DEA Fund and insurance figures verified against primary documents, or the conflict kept flagged.

**Exit criteria**
- [ ] Requirement matrix covers the first 10 institutions; at least 60% of fields have source, date and a verifier (below that, M1 slips one week).
- [ ] Counsel engaged and the opinion commissioned, with a draft date of 6 Nov 2026.
- [ ] 20 interviews logged and a synthesis written (top assets, top pains, fee reactions, NRI needs).
- [ ] Competitor sweep closed and documented.
- [ ] 3 consented families recruited for M1; repository, CI and landing page live.

## M1 Prototype

**Due:** Friday 30 October 2026.

**Goal.** Show that the concierge can find money and produce a correct pack for banks, mutual-fund RTAs and IEPF, with the team doing the manual work.

**Scope**
- Concierge search for 10 to 15 consented families (user-assisted portal searches).
- Procedures knowledge base loaded from the M0 matrix.
- Rules engine prototype and pack generator for the top three institution types.
- Eval harness with 30 claim-level golden items (assumption).
- Demo on a synthetic family.

**Exit criteria**
- [ ] At least 10 real families served; at least 3 NRI heirs interviewed.
- [ ] Demo script runs end to end (about 10 minutes).
- [ ] Baseline numbers committed: requirement accuracy (target at least 90%, assumption), route accuracy, name-match precision and recall, reviewer time per family.
- [ ] Share of families with a previously unknown claimable asset measured (continue signal: at least 50%).
- [ ] At least 6 packs prepared, 3 submitted, feedback from at least 3 institution desks or branches.
- [ ] Reviewer edits logged with reason codes.

## M2 MVP

**Due:** Friday 11 December 2026.

**Goal.** Run the full flow in software, safely, in under 3 reviewer hours per family.

**Scope**
- Intake, consent, authority check, vault and encryption; extraction; entity matching with reviewer queue.
- Versioned rules engine, ranking, packs for all five asset classes, reviewer console, claim tracker, audit log.
- NRI remote-consent flow; flat-fee payments in test mode.
- Golden set at 60 items; CI gates; deletion and breach drill.

**Exit criteria**
- [ ] All P0 user stories meet acceptance criteria.
- [ ] Golden set: requirement accuracy at least 95%, zero critical omissions, route accuracy at least 95% (assumption).
- [ ] No pack released without a recorded reviewer approval; deceased-person search blocked until authority check is approved.
- [ ] Five dry-run families complete end to end, each under 3 reviewer hours.
- [ ] Legal opinion received; fee terms cleared; hosting decision for model calls made.
- [ ] Deletion on request verified by test; breach drill completed.

## M3 Pilot & decision

**Due:** Friday 29 January 2027; day-90 checkpoint Friday 8 January 2027.

**Goal.** Decide whether to continue, pivot or stop, using leading indicators because IEPF claims are slow.

**Scope**
- Paid pilot with 40 to 50 families (assumption), including at least 10 NRI cases and local representatives in two cities.
- Partner outreach to CAs, advocates and advisers using anonymised results; Project 1 cross-sell test.
- Weekly eval runs and tracking of Found, Ready, Filed, Engaged and Paid stages.

**Exit criteria**
- [ ] Metrics reported against HANDOFF section 11 at day 90 and week 16, with and without IEPF: upload rate (at least 40%), discovery value (at least 50%), first-submission acceptance (at least 70%) and requirement accuracy (at least 95%), fee acceptance (at least 30%) and success fees collected (at least 70%), claims paid (at least 10; zero outside IEPF is a stop signal), reviewer time (under 3 hours) and acquisition cost (under 30% of revenue).
- [ ] Cost per family and unit economics recomputed from actuals.
- [ ] Decision memo written: continue, pivot (white-label to CAs, flat per-pack fees, nominee and KYC audit, or fold into Project 1) or stop.
