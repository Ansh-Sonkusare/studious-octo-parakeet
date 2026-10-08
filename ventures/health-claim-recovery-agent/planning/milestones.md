# Milestones

Four milestones for a dedicated team of one to three people starting Monday 12 October 2026. Full detail, the week-by-week plan and the definitions of done are in [../docs/PROTOTYPE_AND_MVP_PLAN.md](../docs/PROTOTYPE_AND_MVP_PLAN.md). Backlog items are seeded in [issues.json](issues.json); the `milestone` field in each issue matches the names below exactly.

| Milestone | Window | Due |
|---|---|---|
| M0 Discovery & legal | Weeks 1-2 (12-23 Oct 2026) | Fri 23 Oct 2026 |
| M1 Prototype | Weeks 1-3 (12-30 Oct 2026) | Fri 30 Oct 2026 |
| M2 MVP | Weeks 4-9 (2 Nov-11 Dec 2026) | Fri 11 Dec 2026 |
| M3 Pilot & decision | Weeks 10-16 (14 Dec 2026-29 Jan 2027) | Fri 29 Jan 2027 |

M0 and M1 overlap: prototype build starts in week 2 while discovery and legal work finish.

## M0 Discovery & legal

**Due:** Friday 23 October 2026.

**Goals**
- Learn whether rejected-claim holders will pay, and what they will pay for.
- Get counsel's preliminary view on whether the concierge service can run, and start the written opinion.
- Put the minimum consent, security and entity foundations in place to handle real documents.
- Begin collecting consented real files, which become the golden set.

**Exit criteria**
- [ ] 30 interviews with recently rejected or short-paid claimants completed and synthesised; at least 20 of 30 say they would pay to recover the money.
- [ ] Counsel's preliminary view shows no legal blocker for the concierge service; the written opinion is commissioned (due 13 Nov).
- [ ] Gate G0 closed: counsel-reviewed consent and privacy notice; secure upload live; WhatsApp Business number and one-page site live.
- [ ] Part-time claims specialist engaged.
- [ ] Incorporation filed.
- [ ] At least 25 consented, anonymised real files collected.
- [ ] Wordings for four products acquired and the 8-10 product shortlist agreed.
- [ ] Model-vendor data terms reviewed and a short data-protection impact assessment written.
- [ ] Pricing hypotheses and the willingness-to-pay read-out written.

## M1 Prototype

**Due:** Friday 30 October 2026.

**Goals**
- Show a working Claim X-ray on real documents, with every number from a tool and every clause cited.
- Run the concierge service for the first live cases.
- Have an eval harness that reports the metrics defined in the plan.

**Exit criteria**
- [ ] X-ray runs end to end on at least 20 real consented document sets without developer intervention.
- [ ] On the development split of golden set v0 (40 files, about 100 deductions): clause-citation precision at least 90%, zero invented clauses, deduction-class accuracy at least 80%, amounts within ±2% on at least 90% of deductions.
- [ ] Median time from upload to X-ray under 10 minutes.
- [ ] At least 10 concierge cases received, 5 filed with insurers, 2 paying the token fee.
- [ ] Eval run reproducible from a clean checkout; no customer data in the repository.
- [ ] 12-minute demo delivered and feedback recorded.

## M2 MVP

**Due:** Friday 11 December 2026.

**Goals**
- Automate intake, analysis, letter drafting, review, tracking and payments, with a human approving every outbound letter.
- Pass the release gates on the sealed holdout of the golden set.
- Close the legal and compliance gates that block a public pilot.

**Exit criteria**
- [ ] All P0 user stories (US-01 to US-11) accepted.
- [ ] Release gates passed on the sealed holdout: clause-citation precision at least 95%, zero invented clauses, amounts within ±2% on at least 95% of deductions, class accuracy at least 90%, 100% correct refusals on the adversarial set.
- [ ] Gates G1 to G5 and G7 closed: payments, consent for proof content, written legal opinion, consent and deletion flows with AI disclosure, vendor terms and breach runbook, caregiver authorisation.
- [ ] Backup-restore drill and data-deletion drill passed.
- [ ] Reviewer turnaround within the 4-working-hour target on at least 20 shadow-mode cases.
- [ ] Release tagged `v0.1.0`.

## M3 Pilot & decision

**Due:** Friday 29 January 2027 (data freeze Friday 22 January).

**Goals**
- Operate the MVP on 50-100 live cases across search, partner and employer channels.
- Measure the five questions in the plan: arrival, correctness, recovery, willingness to pay, economics.
- Decide whether to continue, pivot to B2B2C, or stop.

**Exit criteria**
- [ ] At least 50 cases filed by Monday 21 December 2026 so that the 30-day insurer window closes by 20 January 2027; 50-100 filed by the freeze.
- [ ] Metrics reported with sample sizes against the thresholds: at least 40% of qualified leads upload documents; clause precision at least 95% with reviewer edit rate below 30%; at least 25% reversal at the insurer stage within 30 days; at least 30% fee acceptance and at least 70% of owed success fees collected; acquisition cost below 30% of expected fee and reviewer time below 20 minutes per case.
- [ ] Unit-economics model rebuilt from actual data.
- [ ] Decision memo reviewed by the team and advisers on Wednesday 27 January, delivered Friday 29 January.
- [ ] If fewer than 50 cases have matured, the memo states a provisional verdict and a time-boxed extension proposal.
