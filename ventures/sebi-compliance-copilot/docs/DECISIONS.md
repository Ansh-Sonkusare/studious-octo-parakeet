# Architecture and Product Decisions

Lightweight decision records for the SEBI compliance copilot. Each record states context, decision, consequences and status. **Accepted** means the team has adopted it as a working rule; **Proposed** means it answers an open question in [HANDOFF section 13](HANDOFF.md) and needs confirmation after the M0 interviews. Records are added, not rewritten: a changed decision gets a new record that supersedes the old one. Tags **[Assumption]**, **[Inference]** and **[Unconfirmed]** follow HANDOFF.

Last updated 8 Oct 2026.

## ADR-001: The tool advises; the firm decides

- **Status:** Accepted
- **Context.** Under the February 2025 amendments, any SEBI-regulated entity using AI, built in-house or procured, is solely responsible for its outputs ([regulation_and_rails.md, Q4](research/regulation_and_rails.md)). SEBI said on 19 Aug 2026 that tiered AI rules will require human oversight and kill-switch controls; the final circular was not found. The product needs no SEBI licence only while it does not advise investors, execute trades or hold client money ([HANDOFF section 7](HANDOFF.md)).
- **Decision.** The product is decision support. It never posts, never files and never selects securities. Every filing or regulator-facing document needs approval by a named human. Verdicts are phrased as "findings under rule pack X", never "compliant". Suitability output is a draft for the RIA's own decision. Each customer firm can pause the tool's processing (kill switch).
- **Consequences.** Review-console and approval steps are P0. Terms of service cap liability and disclaim legal advice. The legal opinion on the "no licence" position is a gate before the suitability feature ships. Some customers may want more automation; that is deliberately deferred.

## ADR-002: Recall over precision for high-severity findings

- **Status:** Accepted
- **Context.** A false negative (the tool clears a breaching post) is the highest-impact failure in HANDOFF section 12. A false positive costs reviewer time and risks alert fatigue; HANDOFF sets a kill trigger when override rate exceeds 40%.
- **Decision.** Tune thresholds so high-severity recall meets the gate (at least 95% at M3; 90% at the Week 6 checkpoint) before improving precision (at least 85% at M3). Low-confidence or high-severity items always route to a human. Targets are **[Assumption]**.
- **Consequences.** Expect noisier early output. Findings carry confidence and severity so reviewers can triage. Evaluation reports recall per rule class and shows misses, not only averages. If recall stays below 90% after two iterations, the HANDOFF fallback is an AI-assisted service model.

## ADR-003: Versioned rule sets with explicit status

- **Status:** Proposed (answers "launch before the notified text?")
- **Context.** The Common Advertisement Code was approved on 24 Sept 2026, but the notified text and effective date are **[Unconfirmed]**. Other rules also change: the AI/ML guidelines are pending, and CSCRF deadlines have been extended before. Findings must be defensible later, which means knowing exactly which rule text was applied.
- **Decision.** Rules live in git as versioned packs with a status (`draft`, `advisory_pending_notification`, `in_force`, `superseded`), effective date and source citation. Draft-derived rules ship labelled "advisory, pending notification". Findings store the pack version. Activating a pack is a reviewed pull request that runs the regression suite. Re-checking old items creates new findings and never overwrites.
- **Consequences.** More engineering overhead early, but the product stays useful if the notified text differs from the draft, and historical audits remain reproducible. Marketing must not describe advisory rules as mandatory.

## ADR-004: Immutable evidence and a hash-chained audit log

- **Status:** Accepted
- **Context.** Under the code, a firm must show that every ad was correctly classified, compliant when issued, reported on time and supportable later ([Mondaq](https://www.mondaq.com/india/fund-management-reits/1826178/sebis-proposal-for-a-common-advertisement-code-financial-advertisements-under-the-regulatory-lens), as cited in HANDOFF). Evidence that the vendor could alter is weak evidence.
- **Decision.** Store the original content, the as-published capture and the report pack in object storage with write-once (Object Lock) retention, recording SHA-256 and UTC time. Keep an append-only, hash-chained audit log; publish the chain head daily to the lock bucket. Run a nightly integrity job.
- **Consequences.** Deletion requests and DPDP erasure must be handled through retention rules and crypto-shredding rather than direct deletes (design needed before DPDP duties bind around May 2027). The retention period is **[Unconfirmed]** and is configurable per firm. Storage cost is small relative to the value of the evidence.

## ADR-005: No fine-tuning; retrieval, deterministic rules and pinned prompts

- **Status:** Accepted
- **Context.** HANDOFF section 6 and the research report (Table 15) specify retrieval, a deterministic rule engine, a mid-tier model for judged checks and a small model for classification, with no fine-tuning. Rules change and must be citable; a fine-tuned model hides which text it applied.
- **Decision.** Use general-purpose models through an API. Deterministic code handles disclaimers, registration numbers, banned phrases, follower thresholds, price-data lag and the 24-hour clock. The model judges only what rules cannot (implied guarantees, performance claims, advice versus education) and must return a clause identifier and a verbatim quote that a validator checks against the corpus. Prompts, schemas and model IDs are versioned and pinned.
- **Consequences.** Behaviour changes by editing rules and examples, not by retraining. Model upgrades go through the same regression suite as rule changes. Labelled data is used for evaluation and few-shot examples, not training. Reconsider only if evaluation shows a ceiling that rules and retrieval cannot fix.

## ADR-006: Start with RIAs and RAs; add PMS and brokers through design partners

- **Status:** Proposed (answers "first customer segment")
- **Context.** RIAs (about 1,000) and RAs (about 1,500) are reachable and their sales cycles are short, but the pool is small and RAs are cash-strapped. PMS (515 to 530+) and brokers pay more but take 1 to 3 months and their counts are partly unknown ([HANDOFF sections 2, 3 and 8](HANDOFF.md); [b2b_fintech_gaps.md, section 6](research/b2b_fintech_gaps.md)). The sales-cycle figures are **[Inference]**.
- **Decision.** Build the MVP around the solo RIA/RA workflow and the compliance-officer review console. Recruit the first three design partners mostly from RIAs and RAs, and at least one PMS or broker compliance officer so enterprise needs shape the roadmap. Revisit after M0 interviews and the Week 6 checkpoint.
- **Consequences.** Branch/AP hierarchy, SSO and API stay P2. Pricing starts at the Solo and Firm tiers; Enterprise is tested with the PMS and broker partners. If PMS interviews show stronger demand, the segment order changes through a new record.

## ADR-007: Data minimisation, zero-retention vendors and region choices

- **Status:** Proposed (answers "hosting region and LLM vendors")
- **Context.** The firm is the data fiduciary and the team its processor. Sending client-related content to a foreign model API is cross-border processing; whether CSCRF imposes localisation on small RIAs was not researched (**[Unconfirmed]**). DPDP fiduciary duties bind around May 2027 ([regulation_and_rails.md, Q8](research/regulation_and_rails.md)).
- **Decision.** Process public post text and firm-authored drafts only; do not store client PAN, holdings or call recordings in the MVP. Use model vendors with zero-retention terms, document sub-processors, and host the database and evidence store in an India region where available **[Assumption]**. Obtain written counsel advice on offshore model use before any design-partner data is sent. Strip or redact personal identifiers before model calls where feasible.
- **Consequences.** The advice audit trail from imported transcripts stays P2 because it carries the most personal data. If counsel rejects offshore processing, the fallback is redaction plus an India-hosted model option, with a cost and quality check. Vendor choice is recorded in a follow-up record.

## ADR-008: CSCRF-lite is an add-on module, not part of the core release gate

- **Status:** Proposed (answers "include the CSCRF kit in the MVP?")
- **Context.** CSCRF cycles for self-certification, small, mid-size and qualified entities have an action-taken/revalidation report due 30 Nov 2026 (circular number not fully verified). No Indian self-serve kit was found, but category counts, and therefore buyer count, are unknown ([b2b_fintech_gaps.md, section 2](research/b2b_fintech_gaps.md)). Willingness to pay is anchored to VAPT fees of ₹30k to ₹2 lakh (generic, from the TCSA source cited there).
- **Decision.** Ship a lightweight CSCRF kit (deadline calendar, policy and asset-inventory templates, reminders) as a P1 add-on in M2, published before 30 Nov 2026 for lead generation and learning. It does not block the MVP release gate. Do not offer VAPT; the product points to CERT-In-empanelled auditors.
- **Consequences.** The kit costs about a week of work and tests demand from firms that may later buy the ad-check. If interviews show weak demand, drop it without affecting the core. Any claim about applicability by entity category waits for verification against the circulars.
