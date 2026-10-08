# Research Index

These files are the evidence base for [HANDOFF.md](../HANDOFF.md). They are research notes as of 7 October 2026 and are not edited as part of project planning. Most figures are secondary reporting of regulator or parliamentary data; verify against primary documents before external use.

**Path mapping.** HANDOFF section 15 cites `reports/India AI personal finance MVP.md`, which is [00-full-research-report.md](00-full-research-report.md) here, and `research_notes/India AI personal finance MVP/`, which is this folder.

Labels used in the notes: **Cited Findings** (sourced), **Inferences** (author judgement), **Gaps** (not found or not verified).

## Files

| File | What it contains | Most relevant sections for this project |
|---|---|---|
| [household_finance_gaps.md](household_finance_gaps.md) | Indian household finance pain points with sizing and gaps | **5 Unclaimed assets and succession** (core evidence: DEA Fund, IEPF, mutual funds, insurance, government-drive returns; conflicting figures). Also 6 NRI finance, 4 Retirement and government schemes (EPF), 8 Family finance (parents' finances) |
| [financial_gaps_sizing.md](financial_gaps_sizing.md) | Sizing fact sheet for consumer and small-business gaps, with source status (primary or secondary) | Fact sheet rows 34 to 36 (US unclaimed property; DEA Fund ₹86,917 cr at 30 Jun 2026); Gaps (no national IEPF dividend total) and Conflicts |
| [investor_pain_points.md](investor_pain_points.md) | Mutual-fund investor base, pain points and willingness to pay | 2 Pain point E (KYC, bank and nominee mismatches and unclaimed money; MITRA); 3 Willingness to pay for financial help; 4 Which pain points suit an AI agent |
| [regulation_and_rails.md](regulation_and_rails.md) | Indian regulatory framework and market rails (SEBI, AMFI, data rails, DPDP) | Q6 Data rails (Account Aggregator, CAS, MFCentral); Q8 Data protection (DPDP Act and Rules 2025, penalty ceilings, cross-border processing); Q4 SEBI on AI and advice versus education (why the product must not advise on inherited investments) |
| [tech_feasibility.md](tech_feasibility.md) | Build blueprint for an AI assistant on mutual funds; retrieval versus fine-tuning; evaluation and costs | 1 Data sources (scraping legality); 2 Portfolio import (CAS, `casparser`); 4 AI approach (retrieval and tools over fine-tuning); 5 Evaluation and guardrails (golden sets, audit log, human in the loop); 6 Indicative costs and timeline |
| [agentic_rails_trends.md](agentic_rails_trends.md) | Agentic AI in finance and India's public rails for agents | 1 India rails (UPI Autopay and mandates, Account Aggregator status, OCEN, DigiLocker); 4 WhatsApp and vernacular distribution; 5 Risks and regulation for agents; 6 Product ideas enabled by the rails |
| [global_underserved_segments.md](global_underserved_segments.md) | Underserved segments and cross-border gaps | 1 Diaspora and cross-border (NRIs); 3 Retirees, elder finance, caregivers and estate (US analogues: Atticus, Empathy, Carefull, executor burden); 6 Household financial chores (unclaimed property) |
| [00-full-research-report.md](00-full-research-report.md) | Full research paper: market structure, regulation, opportunity scoring and recommended opportunity | 8.5 Profile 5 (family money finder: scoring and workflow); 9.5 Validation metrics and kill criteria; 10 Commercialisation (build approach, pricing, unit economics, go-to-market, revenue ladder); Table 15 suggested implementation of core components; 6.1 India regulatory requirements |

## Where to look for common questions

| Question | Start here |
|---|---|
| What is the size of each unclaimed pool, and where do the sources disagree? | [household_finance_gaps.md](household_finance_gaps.md) section 5, then HANDOFF section 2 |
| Is a licence needed for discovery plus paperwork help? | [00-full-research-report.md](00-full-research-report.md) Profile 5 and section 6.1; [regulation_and_rails.md](regulation_and_rails.md) Q4 |
| DPDP timelines, penalties and offshore model use | [regulation_and_rails.md](regulation_and_rails.md) Q8 |
| Why retrieval plus rules rather than fine-tuning | [tech_feasibility.md](tech_feasibility.md) sections 4 and 5 |
| Model prices and hosting cost assumptions | [tech_feasibility.md](tech_feasibility.md) section 6 |
| Pricing, unit economics, go-to-market | [00-full-research-report.md](00-full-research-report.md) section 10 |
| US analogues for estate settlement | [global_underserved_segments.md](global_underserved_segments.md) section 3 |

## Known gaps in the research (carried from HANDOFF)

- No public data on transmission-after-death volumes, time to settle, serviceable families, willingness to pay, or NRI cross-border inheritance.
- Fee-based IEPF agents and will and estate startups were not researched.
- Institution-specific succession, legal-heir and indemnity thresholds are not in the notes; compiling them is the first task of milestone M0 (see [planning/milestones.md](../../planning/milestones.md)).
- DEA Fund and insurance totals conflict across sources; see HANDOFF section 2 and verify against Rajya Sabha answers.
