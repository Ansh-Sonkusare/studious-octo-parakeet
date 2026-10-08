# Research Index

This folder holds the desk research behind the health-claim recovery agent. It is a snapshot with an evidence cut-off of 7 October 2026, copied from a wider study of AI products in personal and small-business finance. Only part of it concerns this project; the table below says which parts.

**How to use it.** Start with [../HANDOFF.md](../HANDOFF.md), which distils the project-relevant findings and carries the inline sources. Come here when a figure, rule or source needs checking. The files are not edited to match later decisions; if a project document and a research file disagree, check the primary source and record the outcome in the project document.

**Reading the evidence.** Most figures come from secondary coverage (trade press, summaries of regulator reports), not primary PDFs. Each note separates cited findings from the author's inferences and lists gaps and conflicts; conflicts that matter here are the FY25 Ombudsman totals (37,431 versus 53,102) and the "41% in favour" figure, both discussed in HANDOFF.md section 2. Regulatory material is not legal advice.

## Files

| File | What it contains | Most relevant to this project |
|---|---|---|
| [00-full-research-report.md](00-full-research-report.md) | The complete study: abstract, methodology, Indian market structure, investor needs, tests of five strategic hypotheses, regulation, unresolved financial problems, 14-idea scoring matrix, the recommended opportunity and its commercialisation plan. | Section 7 (problem sizing, Table 8); section 8.5, Profile 1 (health-claim recovery agent profile); section 9 (design, legal prerequisites, 90-day plan, validation metrics, risks); section 10 (concierge-first build, pricing, unit economics, B2B2C, go-to-market); section 6.1 (licensing by activity, Table 6) |
| [unsolved_insurance_health.md](unsolved_insurance_health.md) | Global insurance and healthcare-finance problems that AI agents can address: US denials and appeals, medical billing, India claim rejection, out-of-pocket spending, mis-selling, policy comprehension, other regions, and a ranking for small teams. | Section 3 (India claim rejection, partial settlements, grievance ladder, IRDAI 2024 master circular, Bima Bharosa and Ombudsman data, incumbents); section 4 (co-pay, room-rent and non-payable causes of partial payment); section 1 (US denials and the US competitors Counterforce and Claimable, for the later US expansion) |
| [household_finance_gaps.md](household_finance_gaps.md) | Indian household-finance opportunities beyond investing: insurance, tax, credit, retirement schemes, unclaimed assets, NRI finance, fraud, family finance. | Section 1 (insurance: claim rejection figures, incumbents Insurance Samadhan and Ditto, web-aggregator rules, the Acko fine, fake-site warnings); section 5 (unclaimed assets) and section 8 (family finance) for the later expansion path |
| [regulation_and_rails.md](regulation_and_rails.md) | Indian regulatory framework and market rails, written for a mutual-fund startup: SEBI adviser rules, AMFI distribution, execution platforms, AI guidance, data rails, payments, DPDP. | Q8 (IT Act SPDI Rules and DPDP timeline and penalties, cross-border processing); Q7 (payments and pooling, for the no-client-money rule). The SEBI sections apply to the mutual-fund pivot, not to the MVP |
| [tech_feasibility.md](tech_feasibility.md) | Technical blueprint for an AI assistant, originally for mutual funds: data sources, ingestion, transaction rails, fine-tuning versus retrieval, evaluation and guardrails, costs and timelines, Indic language and voice. | Section 4 (retrieval plus tools, not fine-tuning); section 5 (golden set, tool design, human-in-the-loop, audit log, eval cadence); section 6 (model and speech pricing, hosting costs, build timeline) |
| [global_regulation.md](global_regulation.md) | Regulation of AI-delivered financial guidance and agent-executed transactions in the US, UK, EU, Singapore, UAE, Hong Kong, Australia, Brazil, Indonesia and Nigeria, plus cross-border service and sandboxes. | Section 5 (cross-border service, data residency, US model APIs) and section 1 (US position) when scoping the US expansion. Not needed for India-only work |
| [global_underserved_segments.md](global_underserved_segments.md) | Underserved personal-finance segments worldwide: diaspora, gig workers, retirees and caregivers, emerging markets, young earners, household chores, and willingness to pay. | Section 6 (US medical-bill and denial-appeal competitors such as Counterforce; unclaimed property); section 3 (caregivers); section 7 (willingness to pay and monetisation) |
| [financial_gaps_sizing.md](financial_gaps_sizing.md) | Fact sheet sizing consumer and small-business money problems across markets, each row with a source URL, a verification status and a conflicts list. | Rows on India health out-of-pocket spend, the health protection gap and US claim denials; the conflicts section for figures that disagree |

## Quick lookup

| Question | Where |
|---|---|
| How big is the Indian rejected-claims pool and what does the data not tell us? | HANDOFF.md section 2; unsolved_insurance_health.md section 3 |
| Which insurers draw the most Ombudsman health complaints? | unsolved_insurance_health.md section 3; household_finance_gaps.md section 1 |
| Is an IRDAI licence needed for claim assistance? | 00-full-research-report.md Table 6; household_finance_gaps.md section 1 (Regulation) |
| What are the unresolved legal questions? | HANDOFF.md section 7; unsolved_insurance_health.md section 3 (Inferences, Gaps) |
| Why retrieval and tools rather than fine-tuning? | tech_feasibility.md section 4 |
| How should evaluation work? | tech_feasibility.md section 5; the evaluation plan in [../PROTOTYPE_AND_MVP_PLAN.md](../PROTOTYPE_AND_MVP_PLAN.md) section 8 |
| What do DPDP and the IT Act require of health data? | regulation_and_rails.md Q8 |
| What are the US competitors and constraints? | unsolved_insurance_health.md section 1; global_underserved_segments.md section 6; HANDOFF.md section 14 |
| What do model, speech and hosting cost? | tech_feasibility.md section 6 (unconfirmed list prices) |

## Known gaps relevant to the project

- Insurer-level rejection reasons are not published by IRDAI.
- Health-only Bima Bharosa data and a reconciled FY25 Ombudsman total were not found.
- Ombudsman representation rules and the current award cap were not verified.
- The five-year moratorium rule under the 2024 health regulations was mentioned but not researched.
- No current LLM price pages were fetched; prices in the notes are from third-party aggregators.

Closing these is scheduled in the M0 backlog; see [../../planning/issues.json](../../planning/issues.json).
