# MSME Receivables Agent

An AI agent that helps Indian micro and small suppliers recover delayed payments. It ingests invoices, GST and Tally data, scores buyers, sends escalating multilingual reminders that cite Section 43B(h) and MSMED Act interest, computes the interest owed, assembles an MSME Samadhaan / Facilitation Council filing pack, and routes eligible invoices to TReDS. It is sold mainly through chartered accountants (CAs): the CA buys, the supplier benefits. Every date, interest figure and exposure number comes from tested code, not from the language model.

**Status: Pre-prototype, planning.** No product code exists yet. Dated 8 Oct 2026.

## The problem in three numbers

| Number | Meaning | Source and flag |
|---|---|---|
| About ₹8.1 lakh crore | Overdue MSME receivables (Sep 2026) | [Fintechbiznews](https://www.fintechbiznews.com/fintech-technology/rs81-trn-is-locked-up-in-overdue-receivables); company-sourced (Recordent sells collections data); no primary source |
| 73 days | Average time SMEs take to pay invoices; 82.6% of invoices carry 0-30 day terms | [Telangana Today](https://telanganatoday.com/indian-msmes-face-mounting-delayed-payments-recordent-report-reveals), [KNN India](https://knnindia.co.in/news/newsdetails/msme/delayed-payments-stretch-msme-cash-cycles-strain-working-capital-report) |
| ₹20,979 crore | Still pending in MSME Samadhaan cases at 14 Aug 2026; 16% unresolved beyond a year | [Crisil, Aug 2026](https://intelligence.crisil.com/en/homepage/newsroom/press-releases/2026/08/executed-well-msme-bill-can-be-an-ibc-moment-for-delayed-payments.html) |

Small suppliers lack leverage and fear losing the customer, so their own reminders are weak (Inference). Section 43B(h) gives a non-hostile lever: the buyer's tax deduction is at stake.

## How it works

1. **Onboard.** The CA invites the supplier, who consents and uploads a Tally or Excel export.
2. **Compute.** Deterministic tools work out the due date, accrued interest and 43B(h) exposure.
3. **Remind.** After the supplier approves, the agent sends reminders on WhatsApp and email in English, Hindi and one regional language, climbing a ladder from a courtesy note to a notice citing 43B(h) and interest.
4. **Listen.** Buyer replies are classified; a dispute, opt-out or promise date pauses the ladder.
5. **Escalate.** The agent builds a filing pack for CA review; the supplier files with their own login. Eligible invoices are referred to TReDS.

The product never holds or moves money, never files on its own, and never gives legal advice. The model writes language around numbers computed by tools, and a post-check blocks anything else.

## Status and timeline

Plan assumes a dedicated team of 1-3 starting Mon 12 Oct 2026.

| Milestone | Window | Due | Outcome |
|---|---|---|---|
| M0 Discovery & legal | Weeks 1-2 | Fri 23 Oct 2026 | At least 12 CAs committed; legal opinion commissioned; rule spec written |
| M1 Prototype | Weeks 1-3 | Fri 30 Oct 2026 | Concierge collections for 3-5 suppliers via 2-3 CAs; dashboard, interest calculator, eval harness |
| M2 MVP | Weeks 4-9 | Fri 11 Dec 2026 | P0 features for design-partner CAs; 300-case golden set at 100% |
| M3 Pilot & decision | Weeks 10-16 | Fri 29 Jan 2027 | Outcome data; continue, pivot or stop memo |

Success targets (proposed, to ratify at kickoff): 100 suppliers via at least 15 CAs; 20% or more of past-due value paid within 60 days of the first reminder against a holdout; 100% match on a CA-verified golden set. See [HANDOFF.md](docs/HANDOFF.md) Section 11.

## Repository map

| Path | Contents |
|---|---|
| [docs/HANDOFF.md](docs/HANDOFF.md) | Detailed handoff: evidence, product, legal view, business model, metrics |
| [docs/PROTOTYPE_AND_MVP_PLAN.md](docs/PROTOTYPE_AND_MVP_PLAN.md) | Prototype and MVP specification, architecture, evaluation, gates, costs |
| [docs/DECISIONS.md](docs/DECISIONS.md) | Decision records (ADR-001 to ADR-008) |
| [docs/research/](docs/research/README.md) | Research notes and an index of the parts that matter here |
| [planning/milestones.md](planning/milestones.md) | Milestones M0-M3 with due dates and exit criteria |
| [planning/issues.json](planning/issues.json) | 39 issues ready to import into a tracker |
| [CONTRIBUTING.md](CONTRIBUTING.md) | Branching, pull-request checklist, data rules |

Planned code layout (not yet created) is in the plan, Section 7.

## Key risks

- **Legal points unconfirmed.** Presidential assent and commencement of the MSMED (Amendment) Bill 2026; interest at three times the RBI bank rate compounded monthly (Unverified); whether non-lawyers may assemble Council filings; enforceability of success fees; lawful basis for messaging a buyer's named employee. Counsel to confirm; letters cite only confirmed provisions.
- **Distribution and willingness to pay.** Distribution scores 2 of 5 and willingness to pay 3 of 5. The CA channel, a free exposure audit and a concierge start address this.
- **Buyer relationship damage.** Relationship guard, supplier-approved cadence, neutral tone.
- **Wrong figure or invented clause.** Tools own numbers; post-check; golden-set gate on every release.
- **Bundling.** Tally (TallyIra), Xero and Intuit could add reminders; the focus is escalation and filing within the CA workflow.
- **Attribution and fee leakage.** Holdout baseline and clear contracts.

Full list: [HANDOFF.md](docs/HANDOFF.md) Section 12 and [plan](docs/PROTOTYPE_AND_MVP_PLAN.md) Section 12.

## Next actions

1. Mon 12 Oct: kickoff; ratify metrics and decision records.
2. By Fri 16 Oct: engage counsel on the open legal questions; start outreach to 25 CAs; repo and CI ready.
3. By Fri 23 Oct: at least 12 CAs committed; 40 interviews done; WhatsApp route chosen; rule spec v0 reviewed by a CA.
4. By Fri 30 Oct: prototype demo and go/no-go for M2.

## Links

- Handoff: [docs/HANDOFF.md](docs/HANDOFF.md)
- Plan: [docs/PROTOTYPE_AND_MVP_PLAN.md](docs/PROTOTYPE_AND_MVP_PLAN.md)
- Section 43B(h) explainer: [Business Standard](https://www.business-standard.com/finance/personal-finance/45-day-msme-payment-rule-impact-and-details-of-section-43b-h-explained-124032600333_1.html)
- Amendment Bill analysis: [Vinod Kothari](https://vinodkothari.com/2026/07/strengthening-msme-ecosystem-msmed-amendment-bill/)
- Pricing benchmark: [Boostly](https://invoice.boostly.com/blog/best-ai-debt-collection-software)

This repository is private. Do not commit customer data or credentials.
