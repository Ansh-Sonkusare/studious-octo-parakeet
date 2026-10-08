# Architecture and Product Decisions

Initial decision records, 8 October 2026. Each record states the context, the decision, the consequences and what would make the team revisit it. Evidence labels follow [HANDOFF.md](HANDOFF.md): **assumption** and **unverified** items are to be confirmed in discovery (M0) or the pilot (M3). Detail on the plan is in [PROTOTYPE_AND_MVP_PLAN.md](PROTOTYPE_AND_MVP_PLAN.md).

| ADR | Decision | Status |
|---|---|---|
| 001 | Sell to CA firms, not SMEs | Proposed; confirm at M0 exit |
| 002 | The CA reviews, signs and files; the product never submits to an authority | Accepted |
| 003 | File imports before GSP/ASP integration | Accepted |
| 004 | Deterministic matching; no model decides a number | Accepted |
| 005 | Retrieval and tool use; no fine-tuning | Accepted |
| 006 | Price per GSTIN per month plus a per-notice fee | Proposed; test at M3 |
| 007 | Python engine and API, Next.js UI, Postgres with pgvector on Supabase | Accepted |
| 008 | Anonymise at source; no real client data in the repository | Accepted |

---

## ADR-001: Sell to CA firms, not SMEs

**Status.** Proposed. Confirm at M0 exit (HANDOFF gate: at least 8 of 20 CAs confirm a paid pain).

**Context.** The buyer could be the small business that bears lost input tax credit, or the CA firm that handles its reconciliation and notices. India has 98,967 CA firms and 159,557 members with practice certificates (Feb 2025; [TaxConcept](https://taxconcept.net/icai/statistics-of-icai-members-students-firms-till-28th-february-2025/), secondary source). SME bookkeeping apps lose money: Vyapar lost INR 63 cr in FY25 ([Entrackr](https://entrackr.com/fintrackr/vyapar-posts-rs-63-cr-loss-in-fy25-cash-reserve-fades-93-10819211)). Global winners in AI for accounting sell to firms, not owners ([global_b2b_ai_fintech.md](research/global_b2b_ai_fintech.md), section 2). The CA channel is also reachable through ICAI's member-benefits portal, where Suvit and Accu Reco are listed ([b2b_fintech_gaps.md](research/b2b_fintech_gaps.md), section 4).

**Decision.** The CA firm is the customer and the daily user. The SME client is a passive beneficiary who receives summaries and, later, approves actions.

**Consequences.** Multi-client dashboards, role-based review and per-firm tenancy are core. Pricing and onboarding fit a firm's workflow. Seasonality follows return and notice cycles. The firm's own tool habits (Tally, Suvit) set the integration burden.

**Revisit if.** Fewer than 8 of 20 interviewed CAs confirm a paid pain, or pilot firms use the product for fewer than 3 of 4 weeks.

## ADR-002: The CA reviews, signs and files

**Status.** Accepted.

**Context.** Only authorised professionals can represent a taxpayer before tax authorities; this is background knowledge per the research and **unverified** until counsel confirms ([unsolved_smb_payments.md](research/unsolved_smb_payments.md), Problem 3, inference on regulatory path). A wrong citation or figure in a reply harms a client. Human sign-off is also a selling point: Integral (Germany) has licensed professionals review and sign off ([Vestbee](https://vestbee.com/insights/articles/integral-lands-18-m)).

**Decision.**
- Drafts are only drafts. A user with the CA reviewer role must approve every reply and every supplier message before it leaves the system.
- The product has no integration with any government system and exports unsigned documents; the CA files.
- Contracts state the product is a drafting tool and the CA keeps professional responsibility.
- Every approval, edit and outbound message is logged in an append-only, hash-chained audit log.

**Consequences.** Lower regulatory exposure and a defensible audit trail. Throughput is bounded by CA review time, so time-to-reviewable-draft is a key metric. Auto-filing is out of scope even if technically possible.

**Revisit if.** Counsel advises a different structure, or the profession's rules change. Do not relax the gate for speed.

## ADR-003: File imports before GSP/ASP integration

**Status.** Accepted for M0-M3; revisit at the M3 decision.

**Context.** Data can come from portal downloads uploaded by the CA or client, from a licensed GST data provider (GSP/ASP) with taxpayer authorisation, or from Tally exports. Becoming a GSP/ASP adds licensing and audit overhead; integrating through one adds cost, a dependency and a contract. These mechanics are **unverified** background knowledge. Account Aggregator is not the route for 2B ([HANDOFF section 6](HANDOFF.md)).

**Decision.** Start with Excel and JSON files downloaded from the portal, plus Tally and Excel purchase registers. Define a data-source interface so a licensed provider can be added behind it. Do not become a GSP/ASP.

**Consequences.** No licence on the critical path and fast partner onboarding. The user experience is slower (manual download), so the importer must be forgiving and column mappings reusable. Real files set the schema, which de-risks later API work. IMS ingestion by file assumes IMS data is downloadable (unverified).

**Revisit if.** Pilot firms drop out because of the upload burden, or a provider offers acceptable per-fetch pricing. Route A in HANDOFF section 7 is then recommended.

## ADR-004: Deterministic matching; no model decides a number

**Status.** Accepted.

**Context.** Reconciliation is exact arithmetic over structured data, and the rupee at risk must be defensible to a CA and, later, an officer. HANDOFF requires that every rupee figure originates in deterministic code. Model outputs vary between runs and versions.

**Decision.**
- Matching uses normalisation, exact and tolerance tiers, and fuzzy string similarity (`rapidfuzz`). Only tiers 1 and 2 auto-accept; fuzzy and identity matches are suggestions a person confirms.
- Cause classification is rule-based. A small model may propose hints from free-text narrations; hints never change amounts.
- Drafts may state only figures traceable to tool output and law cited from retrieved text; a verifier enforces both.

**Consequences.** Reproducible runs and testable invariants (every line in exactly one group; totals to the paisa). Edge cases need explicit rules, which the CA advisor helps write. A labelled golden set measures precision and recall per tier.

**Revisit if.** The labelled set shows rules cannot reach 99% line-level agreement by M3. Consider a model-ranked suggestion layer for ambiguous groups, still behind human confirmation.

## ADR-005: Retrieval and tool use; no fine-tuning

**Status.** Accepted.

**Context.** The 2024-26 evidence favours retrieval and tool calls over fine-tuning because rules change and numbers must be exact ([tech_feasibility.md](research/tech_feasibility.md), section 4). Skipping fine-tuning saves roughly 3-6 weeks and GPU spend (estimate, section 6 of the same note). The team is one to three people.

**Decision.** Use a mid-tier model for drafting and a small model for extraction and classification, with hybrid retrieval over a versioned law corpus (effective dates) and read-only tools. Pin model versions. No fine-tuning of generative models; revisit only an embedder or a narrow classifier later.

**Consequences.** Law updates are corpus updates, not retraining. Model upgrades are gated by the eval harness in CI. Vendor dependency and data-handling terms need review before real data is sent.

**Revisit if.** Citation precision stays below 90% after retrieval and prompt work (HANDOFF kill trigger), or unit costs make a smaller fine-tuned model clearly cheaper at scale.

## ADR-006: Price per GSTIN per month plus a per-notice fee

**Status.** Proposed. All numbers are **assumptions** until the M3 price test.

**Context.** A CA firm manages many GSTINs, and notice work is episodic. HANDOFF hypothesises INR 250 per GSTIN per month (20-GSTIN minimum) and INR 2,500 per notice for the evidence pack plus first draft, giving about INR 11,667 revenue and about INR 9,500 contribution per typical 40-GSTIN firm per month (81%). Suvit's 50% ICAI discount is a price anchor; no price data exists for this segment.

**Decision.** Test INR 150, 250 and 400 per GSTIN per month in the pilot, keep the notice fee separate, and start firms in free shadow mode before charging. Per-GSTIN pricing aligns revenue with the firm's own billing to clients.

**Consequences.** Usage metering per GSTIN and per notice is required from the MVP. A minimum commitment protects against idle sign-ups. Notice-only pricing stays as the fallback.

**Revisit if.** Firms accept only below INR 75 per GSTIN (HANDOFF trigger: move to a notice-only fee model), or per-GSTIN value is unclear to buyers.

## ADR-007: Python engine and API, Next.js UI, Postgres with pgvector on Supabase

**Status.** Accepted.

**Context.** The team needs one language for reconciliation, evaluation and model calls, a fast table-and-diff UI, and a single store for relational data, embeddings and tenancy. HANDOFF suggests Postgres with pgvector, for example Supabase, and deterministic Python/SQL.

**Decision.** Python 3.12 with FastAPI and pandas for the engine and API; TypeScript with Next.js for the review console; Postgres with pgvector on Supabase with row-level security; Postgres-backed job queue; Claude API for models. Hosting region is to be confirmed (Mumbai preferred, assumption).

**Consequences.** One database to secure and back up; embeddings next to the data they describe. Supabase lock-in is limited by plain Postgres and SQL migrations. A monorepo keeps engine, API and UI in step.

**Revisit if.** Pilot scale or data-residency advice requires self-hosting, or row-level security proves insufficient for firm and client isolation.

## ADR-008: Anonymise at source; no real client data in the repository

**Status.** Accepted.

**Context.** Design-partner exports contain GSTINs, supplier names and amounts, and notices contain taxpayer details. A leak would end partner trust. DPDP duties phase in through about May 2027 ([Deccan Herald](https://www.deccanherald.com/india/centre-notifies-dpdp-rules-implementation-planned-in-phases-spread-over-12-18-months-3798465)). The firm is likely the data fiduciary and the company a processor (assumption; confirm).

**Decision.**
- Partners run a local anonymisation script before sharing: GSTINs become checksum-valid synthetic ones that keep state code and PAN structure, names are replaced, narrations dropped. The partner keeps the mapping.
- Raw partner files and labelled sets live in an access-controlled store outside the repository; the repository holds synthetic fixtures only.
- Real, non-anonymised data enters the system only after a signed processing agreement and confirmed model-vendor terms.

**Consequences.** Slightly less realistic test data (for example, free-text patterns), mitigated by keeping invoice-number structure intact. Extra work for partners, so the script must be a single command. Secret and data scanning are part of CI and the PR checklist in [CONTRIBUTING.md](../CONTRIBUTING.md).

**Revisit if.** Anonymisation degrades matching accuracy measurably, in which case move to a signed processing agreement and a locked-down environment for that partner.
