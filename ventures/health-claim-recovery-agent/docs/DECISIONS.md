# Decision Log

A lightweight record of decisions that shape the product, the architecture or the legal position. Add a new entry when a decision is hard to reverse, affects more than one workstream, or will be questioned later. Do not rewrite accepted entries: supersede them with a new entry and link both.

**Format.** Status, date, context, decision, consequences, and the condition that would make the team revisit it.

**Status values.** *Proposed* (written, not yet confirmed), *Accepted*, *Superseded by ADR-NNN*.

All entries below are *Proposed* on 8 October 2026 and are to be confirmed at the M0 kick-off on 12 October 2026. Evidence for each is in [HANDOFF.md](HANDOFF.md) and the [research notes](research/README.md); scheduling is in [PROTOTYPE_AND_MVP_PLAN.md](PROTOTYPE_AND_MVP_PLAN.md).

| ID | Decision | Status |
|---|---|---|
| ADR-001 | India first; US later on the same engine | Proposed |
| ADR-002 | Retrieval plus tools; no fine-tuning | Proposed |
| ADR-003 | Numbers only from deterministic tools, enforced by a validator | Proposed |
| ADR-004 | Human review of every outbound letter through the pilot | Proposed |
| ADR-005 | No money from insurers, brokers or hospitals; no policy sales; no client money | Proposed |
| ADR-006 | Guided co-pilot: the user files with their own login and OTP | Proposed |
| ADR-007 | Concierge first; automate only what has been done by hand at least 20 times | Proposed |
| ADR-008 | Python and FastAPI, Postgres on Supabase (Mumbai), Claude API | Proposed |

---

## ADR-001: India first; US later on the same engine

**Status:** Proposed, 8 October 2026.

**Context.** India has a documented, large pool of rejected or disallowed health claims (about ₹26,037 crore in FY24), a defined escalation ladder (insurer grievance officer, Bima Bharosa, Insurance Ombudsman), and one human-operated incumbent with limited scale. The US market is also large (KFF reports 20% of in-network ACA marketplace claims denied in 2023), but competitors there are free or cheap, the unauthorised-practice-of-law position is unsettled, and reviewing US health data from India adds HIPAA business-associate friction ([HANDOFF.md](HANDOFF.md) sections 2 and 14).

**Decision.** Build and validate for Indian retail health insurance only. Keep the engine (corpus, rules library, calculators, letter pipeline, eval harness) jurisdiction-agnostic in structure so a US rules pack can be added later. US work is not scheduled before the M3 decision.

**Consequences.**
- Corpus, rules, forms and language support (English, Hindi) are India-specific in M1 to M3.
- Rules carry effective dates and a jurisdiction field from the start, at small cost.
- No US data is collected in the pilot, which avoids HIPAA scope.

**Revisit when.** The M3 memo is "continue" and India unit economics are positive, or an Indian blocker emerges in the legal opinion.

---

## ADR-002: Retrieval plus tools; no fine-tuning

**Status:** Proposed, 8 October 2026.

**Context.** Policy wordings and IRDAI rules change by version and date. The research found that retrieval beats fine-tuning for knowledge that changes, that fine-tuning a generator lowered faithfulness in the main financial-QA study, and that tools, not models, fix numeric errors ([tech_feasibility.md](research/tech_feasibility.md) section 4; [arXiv 2601.07054](https://arxiv.org/html/2601.07054v1)). Fine-tuning would also cost an estimated 3 to 6 weeks of the schedule.

**Decision.** Use a hosted mid-tier model for analysis and drafting and a small model for classification, with hybrid retrieval over a versioned corpus and deterministic tools. Do not fine-tune any model in M0 to M3.

**Consequences.**
- Quality depends on corpus quality, retrieval and the golden set, which become the main engineering investments.
- Model upgrades are treated as releases and gated by the eval suite.
- Cost scales with tokens per case, tracked against the ₹100 per case assumption.

**Revisit when.** After 100 or more reviewed cases, if the retriever or a narrow classifier is the measured bottleneck. Only those components are candidates, not the generator.

---

## ADR-003: Numbers only from deterministic tools, enforced by a validator

**Status:** Proposed, 8 October 2026.

**Context.** A wrong amount or an invented clause in a letter to an insurer damages the user's case and the product's credibility. Users cannot judge clause correctness themselves, so user feedback alone cannot detect these errors.

**Decision.** Every amount, date and deadline in any output is produced by a tested calculator or copied from a source document. Clause references are selected from retrieved candidates by identifier, and quotations must match the corpus verbatim. Model-written text uses placeholders for such values. A code-based grounding validator blocks any output with an untraceable number, date or quotation. Any invented clause is a hard release failure.

**Consequences.**
- Letters are template-led with model-written reasoning sections, which limits stylistic freedom.
- Calculators and the validator are P0 work and need unit and property tests.
- Some correct but unusual arguments may be blocked and routed to a human; this is accepted.

**Revisit when.** Never for the principle. Individual rules (for example the ±2% amount tolerance) may be tuned once the golden set exists.

---

## ADR-004: Human review of every outbound letter through the pilot

**Status:** Proposed, 8 October 2026.

**Context.** The hallucination and legal-practice risks are both rated high impact ([HANDOFF.md](HANDOFF.md) section 12). A reviewer also generates the edit data that grows the golden set. The unit economics assume reviewer time of about 20 minutes per case.

**Decision.** A trained reviewer approves, edits or rejects every letter before the user sees it as final. Cases above ₹1 lakh claimed, or involving pre-existing-disease or non-disclosure grounds, also need specialist sign-off (threshold is an assumption). The reviewer cannot approve while the validator is failing.

**Consequences.**
- Throughput is limited by reviewer hours; the 4-working-hour review target is an assumption to test.
- Reviewer minutes per case is a tracked pilot metric (target under 20; edit rate under 30% by the 22 January 2027 freeze).
- User disclosure states that AI drafts and a human reviews.

**Revisit when.** Edit rate and invented-clause rate have stayed below thresholds across at least 100 live letters, at which point sampling-based review could be considered, subject to counsel's view.

---

## ADR-005: No money from insurers, brokers or hospitals; no policy sales; no client money

**Status:** Proposed, 8 October 2026.

**Context.** Commission-linked insurance activity can fall under IRDAI intermediary rules (web aggregator, broker, corporate agent). IRDAI fined Acko ₹1 crore in May 2025 for commissions routed to an unlicensed entity ([Outlook Money](https://www.outlookmoney.com/insurance/acko-gets-rs-1-crore-irdai-fine-what-it-says-about-how-your-insurance-is-sold)). Holding client money adds payments and trust exposure. Claim assistance on user-paid fees appears to need no IRDAI licence, as the existing incumbent operates on success fees (counsel to confirm).

**Decision.** Revenue comes only from users and, later, from partners that pay for the service (advisers, employers). The product accepts nothing from insurers, brokers or hospitals, never sells, compares or recommends policies, and never touches settlement money: the insurer pays the policyholder, and the product invoices its own fee separately. This is written into the terms and an internal policy before any payment is taken (gate G1).

**Consequences.**
- Referral revenue and affiliate models are off the table, even where legal.
- Partner contracts must not route insurer money; counsel reviews each template.
- Fee collection depends on the user paying after recovery, so collection rate is a key risk (flat-fee fallback exists).

**Revisit when.** Never without a licensing plan and counsel's written advice.

---

## ADR-006: Guided co-pilot: the user files with their own login and OTP

**Status:** Proposed, 8 October 2026.

**Context.** Bima Bharosa and insurer portals use the policyholder's own credentials and OTPs. Autonomous filing would require handling credentials, raise impersonation and legal-practice concerns, and may breach portal terms. Whether a non-lawyer may represent a complainant before the Ombudsman is unverified ([HANDOFF.md](HANDOFF.md) section 7).

**Decision.** The product prepares evidence-backed drafts and a step-by-step walkthrough; the user signs, submits and records the acknowledgement number. Caregivers acting for a parent upload the policyholder's authorisation. The product never stores portal credentials or intercepts OTPs.

**Consequences.**
- Some drop-off at the submission step is likely; the walkthrough and reminders must be strong.
- The legal position is easier to defend (drafting software plus a service) but still needs counsel's opinion (gate G3).
- Insurer-reply parsing and portal integration are deferred (P2).

**Revisit when.** Counsel confirms authorised-representative filing is permitted and the portals offer a sanctioned delegated-access route.

---

## ADR-007: Concierge first; automate only what has been done by hand at least 20 times

**Status:** Proposed, 8 October 2026.

**Context.** The riskiest assumption is that people will pay to recover a claim, not that the pipeline can be built. Manual service tests willingness to pay in the first weeks and produces the real cases that become the golden set ([HANDOFF.md](HANDOFF.md) section 10).

**Decision.** Run a concierge service from week 2 (19 October 2026) with the team doing the work, supported by the Claim X-ray prototype. Charge from the first case once the entity can collect (a token ₹299 is proposed); earlier design-partner cases are free and excluded from willingness-to-pay metrics. Automate a step only after it has been performed manually at least 20 times.

**Consequences.**
- Early weeks include manual work that does not scale; this is intended.
- The MVP backlog is ordered by observed manual effort rather than by assumed value.
- Every consented case is retained for the golden set.

**Revisit when.** Willingness to pay fails the M0 gate (fewer than 20 of 30 interviewees would pay) or the first 20 cases show a step that is clearly automatable sooner.

---

## ADR-008: Python and FastAPI, Postgres on Supabase (Mumbai), Claude API

**Status:** Proposed, 8 October 2026.

**Context.** A team of one to three people needs a stack with few moving parts, strong document and evaluation tooling, an India data region, and room for a review UI. The research suggests Postgres with pgvector, a mid-tier model for drafting and a small model for classification, WhatsApp Cloud API and Razorpay ([HANDOFF.md](HANDOFF.md) section 6.1).

**Decision.** Use Python 3.12 with FastAPI for the API, pipeline, calculators and eval harness; server-rendered Jinja2 and HTMX for the reviewer console and case pages; Postgres with pgvector on Supabase in the Mumbai region (to be verified); a Postgres-backed job queue; the Claude API with pinned model identifiers; WhatsApp Cloud API with a BSP fallback; Razorpay for payments; a static site for landing pages. Details in [PROTOTYPE_AND_MVP_PLAN.md](PROTOTYPE_AND_MVP_PLAN.md) section 6.

**Consequences.**
- One language across backend, pipeline and tests; no separate front-end build.
- A richer interactive console would need a later move to a JavaScript front end.
- Vendor dependencies (Supabase, Anthropic, Meta, Razorpay) are accepted; the data model and prompts are kept portable.

**Revisit when.** The console becomes the delivery bottleneck, the Mumbai region or vendor data terms are unavailable, or load exceeds what a single worker pool can handle (not expected before 100 cases).
