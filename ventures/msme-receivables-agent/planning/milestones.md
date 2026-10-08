# Milestones

Start: Mon 12 Oct 2026. Thresholds are proposals to ratify at kickoff (HANDOFF Section 11). Detail: [PROTOTYPE_AND_MVP_PLAN.md](../docs/PROTOTYPE_AND_MVP_PLAN.md). Issues: [issues.json](issues.json).

| Milestone | Window | Due |
|---|---|---|
| M0 Discovery & legal | Weeks 1-2 | Fri 23 Oct 2026 |
| M1 Prototype | Weeks 1-3 | Fri 30 Oct 2026 |
| M2 MVP | Weeks 4-9 | Fri 11 Dec 2026 |
| M3 Pilot & decision | Weeks 10-16 | Fri 29 Jan 2027 |

## M0 Discovery & legal (due Fri 23 Oct 2026)

**Goal.** Know whether CAs will commit and whether any legal point blocks the plan; write down the rules the engine must implement.

**Exit criteria.**
- [ ] At least 12 CAs committed as design partners; 2-3 chosen for the prototype (HANDOFF gate).
- [ ] 25 supplier and 15 CA interviews logged, with notes stripped of personal data.
- [ ] Legal opinion commissioned with the HANDOFF Section 7 open questions in writing as scope; no blocker identified so far.
- [ ] Rule specification v0 written; every Unverified item listed with an owner.
- [ ] Open decisions from HANDOFF Section 13 answered or assigned (regional language, CA cluster, lead pricing model, WhatsApp route, first TReDS platform, first buyer segment).
- [ ] WhatsApp Business verification started or an alternative chosen.
- [ ] At least 25 anonymised ledgers or exports in hand (100 by 20 Nov).
- [ ] ADR-001 to ADR-008 ratified or amended.

## M1 Prototype (due Fri 30 Oct 2026)

**Goal.** A concierge collections service live for a handful of suppliers via 2-3 CAs, backed by a receivables dashboard on real exports, an interest calculator and an eval harness.

**Exit criteria.**
- [ ] 3-5 suppliers live through at least 2 CAs; at least ₹1 crore of past-due invoices loaded (Assumption).
- [ ] Engine v0 matches a 60-case CA-signed golden set at 100%; the harness runs in CI.
- [ ] At least 90% of rows from real exports parse without manual fixing (Assumption).
- [ ] At least 20 supplier-approved reminders sent; zero containing a figure not in tool output.
- [ ] One filing pack v0 reviewed by a CA, with a written defect list.
- [ ] Demo delivered to at least 2 CAs; at least 2 of 3 prototype CAs state they would pay.
- [ ] Go / no-go for M2 recorded.

## M2 MVP (due Fri 11 Dec 2026)

**Goal.** The HANDOFF P0 feature set working for design-partner CAs, with approval gates, an audit log, three languages and an evaluation gate in CI.

**Exit criteria.**
- [ ] P0 stories in the plan (S-1 to S-4, C-1 to C-4, A-1 to A-3) pass acceptance criteria.
- [ ] 300-case golden set at 100% and blocking in CI; matching at least 95% precision and 90% recall on 100 anonymised ledgers.
- [ ] 200 generated letters graded: citation precision at least 95%, zero invented provisions; native-speaker review done for each language.
- [ ] Reply classification meets thresholds; adversarial reply suite yields zero tool actions.
- [ ] Tenant-isolation test green; audit-log hash chain verifies.
- [ ] Legal gates G0-G3 passed in writing.
- [ ] At least 6 CAs and 15 suppliers onboarded (Assumption); release tagged.

## M3 Pilot & decision (due Fri 29 Jan 2027)

**Goal.** Measure recovery, adoption, willingness to pay and unit economics, then decide to continue, pivot or stop.

**Exit criteria.**
- [ ] Target 100 suppliers via 15 CAs (HANDOFF 90-day success); decision floor of 40 suppliers via 8 CAs (Assumption).
- [ ] Recovery measured against a delayed-start holdout: 60-day reads for invoices first reminded by 30 Nov 2026, 30-day interim reads for later cohorts.
- [ ] All HANDOFF Section 11 metrics computed (CA adoption, golden-set match, recovery, relationship damage, payment, filing, economics).
- [ ] At least 10 filing packs generated and 3 filed, none rejected for pack defects.
- [ ] Unit-economics model rebuilt on actuals.
- [ ] Decision memo delivered Fri 29 Jan 2027 with continue / pivot / stop and the pivots named in HANDOFF Section 11.
