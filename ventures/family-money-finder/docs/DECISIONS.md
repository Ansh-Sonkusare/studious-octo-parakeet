# Decision Log

Architecture and product decision records (ADRs) for Family Money Finder. Each record states the context, the decision, the alternatives considered and the consequences. **Status** is Accepted (adopted for the prototype, MVP and pilot), or Hypothesis (to be tested in the pilot and revisited at the 29 January 2027 review). Labels follow [HANDOFF.md](HANDOFF.md): **Assumption**, **Inference**, **Unverified**.

To change a decision, add a new record that supersedes the old one; do not edit history.

| ID | Decision | Status |
|---|---|---|
| ADR-001 | Portal search is user-assisted; no scraping or credential handling | Accepted |
| ADR-002 | Deterministic rules and retrieval decide requirements; the model never supplies a threshold | Accepted |
| ADR-003 | A human reviews every outbound document | Accepted |
| ADR-004 | Flat Estate Pack plus a capped success fee | Hypothesis |
| ADR-005 | India first; NRIs served through remote workflows and local representatives | Accepted |
| ADR-006 | No fine-tuning; mid-tier model for drafting, small model for classification | Accepted |
| ADR-007 | Authority check before any deceased-person search; data minimisation | Accepted |
| ADR-008 | One repository, with engine packages designed for reuse by the health-claim-recovery project | Accepted |

---

## ADR-001 Portal search is user-assisted; no scraping or credential handling

**Status:** Accepted. **Date:** 8 October 2026.

**Context.** UDGAM, the IEPF portal, MITRA, insurer pages and EPFO are the discovery sources. Several require a login or OTP. MFCentral third-party pulls were curtailed in September to November 2025 ([tech_feasibility.md](research/tech_feasibility.md)). The product handles a bereaved family's data and cannot risk portal terms violations, impersonation or credential leaks. The UDGAM login rules are still to be verified ([HANDOFF section 6](HANDOFF.md)).

**Decision.** The app prepares the exact search inputs and opens the official portal, and the heir performs the search with their own credentials and OTPs. The heir types back or uploads the result, and the app records it. The product never stores portal credentials, automates a login, handles an OTP, or scrapes behind a login. Public, unauthenticated pages may be read for the procedures knowledge base subject to their terms.

**Alternatives considered.** Automated login with stored credentials (credential risk, terms risk, impersonation exposure); screen scraping through the user's session (same, and brittle); Account Aggregator (needs regulated FIU status; out of scope per HANDOFF).

**Consequences.** Lower automation and some user friction, so search guides must be clear and short. Portal changes are tolerated because the guides are versioned text rather than code. Search recall depends on the user's diligence and is measured in the eval plan ([PROTOTYPE_AND_MVP_PLAN.md section 8](PROTOTYPE_AND_MVP_PLAN.md)). The CAS upload path ([casparser](https://github.com/codereverser/casparser)) remains the fallback for mutual funds.

## ADR-002 Deterministic rules and retrieval decide requirements

**Status:** Accepted. **Date:** 8 October 2026.

**Context.** Which documents an institution needs, and whether a succession or legal-heir certificate or an indemnity is required, has a right answer that varies by institution and date. Thresholds are institution-specific and not in the research notes. Frontier models score 70 to 90% zero-shot on Indian regulatory questions ([IndiaFinBench](https://arxiv.org/pdf/2604.19298)), which is not acceptable for a document list sent to a bank. Fine-tuning a generator lowered faithfulness in FinanceBench tests ([arXiv 2404.11792](https://arxiv.org/html/2404.11792)).

**Decision.** Requirements, routes, thresholds and forms come from a versioned requirement matrix evaluated by plain code. Each entry carries source, retrieval date, verifier, and effective dates. Retrieval over the same sources supplies citations. The model may explain and draft only from fields the rules engine or a cited passage supplies, and an output validator rejects any threshold, amount, form number or date not present in its inputs. Where no verified entry exists, the engine answers "unknown, ask the institution".

**Alternatives considered.** Letting the model answer from retrieved text (non-deterministic, hard to regression test); fine-tuning (see ADR-006).

**Consequences.** Matrix maintenance is the main operating cost and the main moat. Entry changes are reviewed like code and trigger golden-set re-verification. Coverage grows institution by institution.

## ADR-003 A human reviews every outbound document

**Status:** Accepted. **Date:** 8 October 2026.

**Context.** Errors in a claim pack delay payment for a grieving family, and drafting indemnities, affidavits and legal-heir declarations may raise Advocates Act questions (HANDOFF open question 1, **unverified**). Counsel has not yet opined.

**Decision.** No document leaves the system until a trained reviewer approves it against a checklist, with the source and effective date visible beside each requirement. The reviewer approves, edits or rejects with a reason code; every decision is audit-logged. Families are told that AI drafts and a human reviews. The claimant signs and submits; the product prepares and guides. Court filings and succession or probate petitions are referred to an advocate.

**Alternatives considered.** Sampling-based review (misses rare critical errors); no review once accuracy is high (revisit only after sustained accuracy above the gate and counsel's view).

**Consequences.** Reviewer time is the main variable cost (3 hours per family at ₹500 an hour in the unit economics, an assumption); the 3-hour target is a pilot gate. The reviewer console is P0.

## ADR-004 Flat Estate Pack plus a capped success fee

**Status:** Hypothesis. **Date:** 8 October 2026.

**Context.** HANDOFF section 8 compares per-claim, success-only and bundled models. Per-claim fees (₹1,499 per pack) weigh heavily against a roughly ₹25,000 average claim (inference from government-drive data). Success-only pricing leaves IEPF packs unpaid for a long time and carries collection risk. Willingness to pay is untested. A success fee on inherited money may create consumer-protection and optics risk for a bereaved family (HANDOFF open question 5, **unverified**).

**Decision.** Test a bundled Estate Pack: ₹4,999 flat for discovery, up to five packs and tracking, plus a 5% success fee on newly discovered assets, capped and disclosed up front (all assumptions). The NRI variant at ₹9,999 including a local representative is a hypothesis. IEPF packs are priced flat, not success-only. No fee is charged before counsel clears the terms (target week 10). No commission is accepted from banks, insurers, RTAs or advisers; the product never holds client money.

**Alternatives considered.** Per-claim only; success-only at 8% (Project 1 hypothesis: 10 to 15%); subscription (episodic need).

**Consequences.** Interviews and pilot data determine the final price points (HANDOFF open question 1). Base-case contribution is about ₹5,049 per family against a ₹2,050 variable cost (all inputs are assumptions). The thresholds that trigger revisiting this record: fee acceptance under 20%, or success fees collected under 70%.

## ADR-005 India first; NRIs through remote workflows and local representatives

**Status:** Accepted. **Date:** 8 October 2026.

**Context.** The pools (UDGAM, IEPF, MITRA, EPFO) and the paperwork are Indian. There are about 3.43 crore overseas Indians including PIOs (secondary source), but no NRI-only count and weak evidence on cross-border inheritance demand. NRIs cannot attend branches, and NRO repatriation is capped at $1M a year. The US analogue (about 16 months, 570 hours, about $12,400 in fees per estate) is a different legal system.

**Decision.** Build for Indian institutions and Indian law only. Support NRI heirs through remote consent and identity flow, clear marking of steps that need a local representative, and a repatriation checklist (Forms 15CA and 15CB through a CA). NRI cases are in the pilot (at least 10) but the NRI workflow is P1 in the MVP. US unclaimed property and executor tooling are out of scope until the India product is validated.

**Alternatives considered.** US-first (state-specific, finder-fee rules unresearched); NRI-only (trust is the barrier and the evidence is weak).

**Consequences.** Local representatives are needed in at least two cities by pilot week 3 (week 12 of the plan). NRI value per family may be higher, which the pilot should measure.

## ADR-006 No fine-tuning; mid-tier model for drafting, small model for classification

**Status:** Accepted. **Date:** 8 October 2026.

**Context.** The research found that retrieval plus deterministic tool calls on a frontier or mid-tier model beats fine-tuning for this class of task, and that skipping fine-tuning saves about 3 to 6 weeks and GPU spend ([tech_feasibility.md](research/tech_feasibility.md)). For a 1 to 3 person team, speed and auditability matter more.

**Decision.** Use a mid-tier model (Sonnet class) for document understanding and drafting, and a small model (Haiku class) for classification and name matching. Pin model identifiers in configuration and log them on every call. Do not train or fine-tune on customer data. The golden set runs in CI on every prompt, model or rules change, so model upgrades are a tested change rather than a leap.

**Alternatives considered.** Fine-tuning a small model (cost, faithfulness risk, data-use implications); a single large model for everything (higher cost with no accuracy benefit on classification).

**Consequences.** Model spend is small (about ₹90 to ₹180 per family, an assumption) and the vendor is replaceable behind one client interface. Hosting location for PAN and death certificates is a separate open decision (HANDOFF open question 7).

## ADR-007 Authority check before any deceased-person search; data minimisation

**Status:** Accepted. **Date:** 8 October 2026.

**Context.** The product holds PAN, bank statements, death certificates and relationship proofs. Searching a living person's assets without consent is impersonation risk. DPDP duties bind from about May 2027, penalties reach ₹250 cr for security failures, and the treatment of a deceased person's data is an open legal question (HANDOFF question 3).

**Decision.** No deceased-person search starts until the death certificate and relationship proof are verified and logged; searches for a living parent require that parent's consent. Store PAN with field-level encryption and mask it in logs, lists and prompts. **Unverified, counsel to confirm:** do not store full Aadhaar numbers; accept a masked copy and redact on upload. Default retention is 90 days after closure (assumption) with deletion on request. No customer data in analytics, none used for training, and consented cases only feed the golden set, outside the repository.

**Alternatives considered.** Collecting everything up front for convenience (larger breach surface); relying on user attestation alone.

**Consequences.** Slightly slower onboarding, which the plain-language, short-flow design must offset. Deletion tests and a breach drill are part of the MVP definition of done.

## ADR-008 One repository; engine packages designed for reuse

**Status:** Accepted. **Date:** 8 October 2026.

**Context.** This product and health-claim recovery share ingestion, rules, pack generation, review and tracking; the research report estimates about 70% stack reuse (inference). This product is the redeploy path if health-claim recovery fails.

**Decision.** Keep this product in its own repository, with the `rules`, `documents`, `audit` and `tracker` packages free of estate-specific logic so they can be extracted into a shared package later. Do not build a shared platform now.

**Alternatives considered.** A monorepo with Project 1 now (coordination cost for a small team); fully separate code (duplicated work).

**Consequences.** Reuse is a design constraint, not a deliverable. Revisit when either project passes its day-90 gates.
