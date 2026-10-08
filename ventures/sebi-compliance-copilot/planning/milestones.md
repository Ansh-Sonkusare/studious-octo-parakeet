# Milestones

Dates assume a dedicated team of 1 to 3 starting Monday 12 Oct 2026 **[Assumption]**. Details and week-by-week work are in [PROTOTYPE_AND_MVP_PLAN.md](../docs/PROTOTYPE_AND_MVP_PLAN.md); issues are in [issues.json](issues.json). Quality gates come from [HANDOFF sections 6 and 11](../docs/HANDOFF.md). Timing depends on SEBI notifying the Common Advertisement Code (text and effective date **[Unconfirmed]**); see the contingency scenarios in the plan.

| Milestone | Due | Weeks |
|---|---|---|
| M0 Discovery & legal | Fri 23 Oct 2026 | 1 to 2 |
| M1 Prototype | Fri 30 Oct 2026 | 3 |
| M2 MVP | Fri 11 Dec 2026 | 4 to 9 |
| M3 Pilot & decision | Fri 29 Jan 2027 | 10 to 16 |

Checkpoints inside milestones: Week 6 (Fri 20 Nov 2026) is HANDOFF's Phase 1 gate; Week 13 (Fri 8 Jan 2027) is HANDOFF's day-90 check.

## M0 Discovery & legal

**Due:** Fri 23 Oct 2026

**Goals**
- Find the notified ad-code text, or confirm it is not yet published, and log the effective date and reporting channel if it is.
- Interview 15 RIAs, RAs and compliance officers (5 more by 13 Nov to reach HANDOFF's 20).
- Sign design partners with written data-use consent.
- Start the labelled ad dataset; write the labelling guide.
- Build rule schema and rules corpus v0 with sources.
- Commission the legal opinion; settle the offshore-model and retention questions.

**Exit criteria**
- [ ] Ad-code status note written (notified text and date, or "not published as of date X"), with the weekly SEBI watch running
- [ ] 15 interview summaries recorded; top 5 pains and willingness-to-pay ranges written up
- [ ] At least 3 design partners signed with consent forms
- [ ] At least 60 public items collected for the labelled set; labelling guide v1 approved
- [ ] Rule schema and pack v0 loaded with source citations
- [ ] Legal opinion engagement signed; terms of reference cover "no licence" position and suitability drafting
- [ ] Repository, CI and a working environment in place

## M1 Prototype

**Due:** Fri 30 Oct 2026

**Goals**
- Classifier (ad or not, celebrity, entity type, channel) and rule checker (deterministic plus model-judged with clause quotes) running on 150 labelled real public posts and synthetic variants.
- Evidence archive prototype (hash, timestamp, snapshot).
- Sample 24-hour report (template; format **[Unconfirmed]**).
- Evaluation harness with per-rule metrics.

**Exit criteria**
- [ ] 150 items double-labelled and adjudicated; kappa reported
- [ ] Ad / not-ad F1 at least 0.80 and high-severity recall at least 85%, with every miss analysed
- [ ] Citation validator in place; relevance precision at least 90% on a 50-finding review
- [ ] Recomputed hashes match for 100% of evidence records
- [ ] Demo delivered to at least 3 compliance professionals; at least 3 of 5 reviewers call the output worth a first pass
- [ ] Baseline results note and top-10 misses published

## M2 MVP

**Due:** Fri 11 Dec 2026 (checkpoint Fri 20 Nov 2026)

**Goals**
- Hosted multi-tenant MVP: intake (web paste, URL, email forward, WhatsApp export), review console, evidence store with object lock, hash-chained audit log, 24-hour report pack and deadline tracker.
- Versioned rule packs with status flags and regression tests in CI.
- Disclosure and suitability generators, register export, CSCRF-lite calendar and template (published before 30 Nov 2026).
- Terms of service and DPA drafted for counsel.

**Exit criteria**
- [ ] Week 6 checkpoint met: F1 at least 0.85 on 300+ labelled items and 5 firms onboarded
- [ ] All MVP acceptance criteria in section 5.3 of the plan pass, including the tenant-isolation test
- [ ] No open P0 defects; load test with 1,000 items passes
- [ ] CSCRF calendar and template published before 30 Nov 2026
- [ ] Legal opinion received or its absence recorded with the suitability feature flagged off
- [ ] Terms, DPA and liability cap drafted

## M3 Pilot & decision

**Due:** Fri 29 Jan 2027 (checkpoint Fri 8 Jan 2027, HANDOFF day 90)

**Goals**
- Run the pilot with design-partner firms on live workflows; process 100+ real items.
- Test pricing at ₹20k, ₹35k and ₹50k a year.
- Final evaluation on 500 items against the gates; external penetration test.
- Start a consultant-partner programme; produce case studies.
- Decide: scale, pivot or stop.

**Exit criteria**
- [ ] At least 5 firms using the tool weekly; at least 10 paying (HANDOFF day-90 targets; at risk if the ad code is not notified)
- [ ] 500-item evaluation meets: high-severity recall at least 95%, precision at least 85%, citation precision at least 95%, ad/not-ad F1 at least 0.90 (targets **[Assumption]**)
- [ ] 100% of 24-hour packs prepared on time; zero tool-caused misses
- [ ] Median accepted price at least ₹20,000 a year; gross margin at least 65%
- [ ] Penetration test complete; critical findings fixed
- [ ] Decision memo scores every row of HANDOFF section 11 and recommends scale, pivot or stop
