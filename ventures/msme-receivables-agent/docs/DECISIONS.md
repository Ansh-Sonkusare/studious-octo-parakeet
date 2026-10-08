# Architecture and Product Decisions

Lightweight decision records. Status is **Proposed** until ratified at kickoff on Mon 12 Oct 2026; after that **Accepted**, **Superseded** or **Rejected**. New records take the next number; a changed decision gets a new record that supersedes the old one.

Source of the underlying facts: [HANDOFF.md](HANDOFF.md). Labels follow HANDOFF: Fact, Inference, Assumption, Unverified.

| ID | Decision | Status |
|---|---|---|
| ADR-001 | CA channel first | Proposed |
| ADR-002 | No lending and no handling of funds | Proposed |
| ADR-003 | Deterministic calculators own every number | Proposed |
| ADR-004 | Human approval for campaigns, formal notices and filings | Proposed |
| ADR-005 | India first | Proposed |
| ADR-006 | Retrieval plus tools; no fine-tuning | Proposed |
| ADR-007 | Concierge before automation | Proposed |
| ADR-008 | Python core, Postgres with row-level security, thin web layer | Proposed |

---

## ADR-001: CA channel first

**Date:** 2026-10-08 · **Status:** Proposed

**Context.** Micro and small suppliers are hard and expensive to acquire directly: Vyapar lost about ₹63 crore in FY25 and Khatabook lost ₹116 crore in FY24 on ₹69-103 crore of revenue ([b2b_fintech_gaps.md](research/b2b_fintech_gaps.md), Section 4). One CA serves dozens to hundreds of MSMEs, ICAI runs a member-benefits marketplace where Suvit is listed, and filing deadlines create recurring urgency. The ranking scores distribution at 2 out of 5 (HANDOFF Section 1).

**Decision.** The CA is the buyer and the distribution channel. Suppliers are onboarded by invitation from their CA. Product, pricing and support are designed for the CA's multi-client workflow first. No direct-to-MSME self-serve.

**Consequences.**
- The CA dashboard and the free 43B(h) and interest exposure audit are P0 (HANDOFF Section 9).
- The CA takes on review duties for formal notices and packs, which creates a liability concern to resolve in the CA agreement ([HANDOFF Section 3](HANDOFF.md)).
- Revenue is a share arrangement with the CA (HANDOFF Section 8 base case: 25% CA share).

**Revisit when.** Fewer than 8 CAs bring at least 5 suppliers each by 29 Jan 2027 (HANDOFF Section 11 pivot rule).

## ADR-002: No lending and no handling of funds

**Date:** 2026-10-08 · **Status:** Proposed

**Context.** Holding buyer payments would likely require licences and create fund-flow risk. A lender referral falls under RBI Digital Lending Directions; success-fee debits fall under RBI e-mandate rules of 21 Apr 2026 (24-hour notice; extra authentication above ₹15,000) (HANDOFF Section 7; counsel to confirm).

**Decision.** Buyers pay suppliers directly. The product never receives, holds or moves customer money and takes no commission from buyers or lenders. TReDS and lender routing are referrals only, with no balance sheet. Fees are charged to the CA or supplier by invoice, or by e-mandate once compliance is confirmed.

**Consequences.**
- Attribution of recoveries relies on supplier- and CA-reported payments and bank-statement matching, not on a payment rail. Fee leakage is a known risk (HANDOFF Section 12).
- Licensing exposure stays low: reminders for the supplier on B2B invoices have no licence identified (Inference).

**Revisit when.** Counsel's opinion changes the licence view, or pilot data shows fee collection below 70% with no mitigation.

## ADR-003: Deterministic calculators own every number

**Date:** 2026-10-08 · **Status:** Proposed

**Context.** A large model scored 13.33% on direct tax law without tools ([CA-Ben review](https://www.themoonlight.io/de/review/large-language-models-acing-chartered-accountancy), cited in [tech_feasibility.md](research/tech_feasibility.md) Section 4). A wrong interest figure in a letter would damage the supplier's credibility and the CA's.

**Decision.** Due dates, interest and 43B(h) exposure are computed only by tested code (`compute_due_date`, `compute_interest`, `compute_43bh_exposure`) with rule parameters in versioned data. Messages are built from templates with named slots; the model may not introduce or alter a figure, date or citation. A post-check blocks any output that does. A CA-signed golden set must match at 100% for any release.

**Consequences.**
- Legal uncertainties (rate multiplier, compounding, deemed acceptance) are parameters, so a counsel answer changes data, not code.
- The model's role is language and tone, which limits the benefit of larger models.

**Revisit when.** Never for figures. The post-check design may be revised if false blocks exceed 5% of drafts (Assumption).

## ADR-004: Human approval for campaigns, formal notices and filings

**Date:** 2026-10-08 · **Status:** Proposed

**Context.** Buyer relationships are the supplier's main fear. Regulators elsewhere already flag AI-generated "duplicative and spurious" complaints ([Orrick](https://infobytes.orrick.com/2026-04-10/cfpb-reports-complaint-volume-doubled-in-2025-citing-surge-in-credit-reporting-disputes/)); NPCI's stated principle is that AI may recommend while execution follows auditable rules ([MediaNama](https://www.medianama.com/2026/09/223-npci-ai-agents-upi-payments/)). Whether non-lawyers may assemble Council filings is an open legal question (HANDOFF Section 7).

**Decision.**
- The supplier approves each campaign and each escalation wording; protected buyers receive no automated contact.
- A CA reviews every formal notice and filing pack.
- The supplier files with their own login and OTP; the product never files autonomously and never mass-files.
- Disputes, opt-outs and promise dates pause automation until a human resumes it.

**Consequences.**
- Review minutes per case become a core cost metric (target under 20; HANDOFF Section 11).
- Throughput is bounded by reviewer capacity until trust is earned.

**Revisit when.** Edit rates stay under 30% and counsel clears a lighter-touch path for specific steps. Any relaxation requires a new record.

## ADR-005: India first

**Date:** 2026-10-08 · **Status:** Proposed

**Context.** The legal lever is India-specific: Section 43B(h), the MSMED Act and the Facilitation Council route, with the 2026 amendment pending assent confirmation. UK and US competitors (Xero, Intuit) are closer there and B2B conduct rules are lighter (Unverified) (HANDOFF Section 14).

**Decision.** Build for India only: INR, Indian financial year, Tally and GST data, Udyam registration, English, Hindi and one regional language (to be chosen in M0). UK and US are P2.

**Consequences.**
- Rule sets are versioned by effective date so that India-specific rules can be isolated and a second jurisdiction added later.
- The Indian-language review budget is a fixed cost.

**Revisit when.** The pilot decision (29 Jan 2027) is continue and India unit economics are proven.

## ADR-006: Retrieval plus tools; no fine-tuning

**Date:** 2026-10-08 · **Status:** Proposed

**Context.** Fine-tuning a generator lowered faithfulness in financial QA (0.700 to 0.625; [arXiv 2404.11792](https://arxiv.org/html/2404.11792), see [tech_feasibility.md](research/tech_feasibility.md) Section 4). Legal text and interest rates change; the corpus is small.

**Decision.** Use a mid-tier Claude model for drafting and a small model for reply classification, with hybrid retrieval over a versioned corpus and deterministic tools. No fine-tuning of generators. Model IDs sit in configuration. Fine-tuning a classifier or embedder is allowed later only if evaluation shows a specific gap.

**Consequences.**
- Quality depends on templates, retrieval and post-checks, all testable.
- Vendor and offshore processing need counsel review and no-training terms (HANDOFF Section 6).

**Revisit when.** Classifier recall on opt-out or dispute stays under thresholds after prompt and example improvements.

## ADR-007: Concierge before automation

**Date:** 2026-10-08 · **Status:** Proposed

**Context.** The riskiest assumptions are willingness to pay and attributable recovery, not technology. The report's approach is to sell the outcome manually first and automate only steps done at least 20 times ([00-full-research-report.md](research/00-full-research-report.md), Section 10.1; HANDOFF Section 9).

**Decision.** Milestone M1 runs collections by hand for 3-5 suppliers through 2-3 CAs, with automation limited to the calculators, parsers and drafting. Other steps are automated in M2 only after the team has performed them about 20 times (Assumption: threshold applied per step).

**Consequences.**
- M1 gives learning, not scale; the MVP backlog is ordered by what the concierge work shows.
- Early cases are charged under a counsel-reviewed paid-pilot letter, or run unpaid if that review is late.

**Revisit when.** A step is performed 20 times with stable inputs and outputs.

## ADR-008: Python core, Postgres with row-level security, thin web layer

**Date:** 2026-10-08 · **Status:** Proposed

**Context.** A 1-3 person team needs exact money arithmetic, strong parsing and evaluation tooling, and tenant isolation per CA and supplier. HANDOFF Section 6 suggests Postgres with pgvector (for example Supabase).

**Decision.** A pure-Python `core` package (calculators, parsers, matching, drafting, post-check) with no web dependency. FastAPI for the API and worker. Postgres on Supabase with row-level security and object storage. Next.js for the CA dashboard, review console and buyer page; Streamlit for the M1 prototype only. Details in [PROTOTYPE_AND_MVP_PLAN.md](PROTOTYPE_AND_MVP_PLAN.md) Section 6.

**Consequences.**
- One package serves the prototype, the MVP and the eval harness.
- Two languages (Python, TypeScript) to maintain; a Python-only server-rendered alternative is open until the end of M0.
- India-region availability on the chosen host is Unverified.

**Revisit when.** M0 finds a blocker on data residency, or the team is Python-only.
