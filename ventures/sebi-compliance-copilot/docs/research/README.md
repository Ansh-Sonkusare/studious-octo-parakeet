# Research Index

Source material for the SEBI compliance copilot. These files are inputs and are not edited here; [HANDOFF.md](../HANDOFF.md) synthesises them for this project. All were gathered up to 7 Oct 2026 and rely mostly on secondary coverage (law-firm notes, trade press). Verify any rule against sebi.gov.in before building to it.

## Files

| File | What it contains | Sections most relevant to this project |
|---|---|---|
| [00-full-research-report.md](00-full-research-report.md) | The full report: market structure of Indian retail investing, regulation, 14 opportunity profiles scored and ranked, implementation and commercialisation guidance | Section 6 (regulatory landscape); section 8.5, Profile 4 (compliance copilot); section 10 and Table 15 (suggested component stack, pricing, unit economics); section 11 (limitations) |
| [b2b_fintech_gaps.md](b2b_fintech_gaps.md) | B2B opportunities in Indian finance: buyer pools, regtech, AMC/broker AI, data APIs, willingness to pay | Section 2 (advertisement code, AI disclosure, CSCRF, record-keeping); section 1 (RIA/RA/PMS/MFD buyer counts and current tools); section 6 (willingness to pay and sales cycles) |
| [regulation_and_rails.md](regulation_and_rails.md) | Indian regulatory framework and market rails: IA/RA rules, AI/ML and finfluencer rules, DPDP, MF rules | Q1 (IA/RA regulations, AI disclosure and liability, Reg 15(14), 18(9), 22A); Q4 (SEBI on AI/ML, finfluencers, "advice versus education"); Q8 (DPDP Act and Rules timeline, offshore processing caveat) |
| [global_regulation.md](global_regulation.md) | Regulation of AI-delivered financial guidance in the US, UK, EU, Singapore and other jurisdictions | Section 1 (US: AI-washing enforcement, FINRA Regulatory Notice 24-09 on generative AI), for the US-expansion hypothesis only |
| [global_b2b_ai_fintech.md](global_b2b_ai_fintech.md) | Global B2B AI fintech category map, pricing and traction | Section 1 (advisor compliance tools such as Smarsh and Red Oak; notetaker adoption and pricing); section 6 (sales cycles and small-team winners) |
| [ai_native_entrants.md](ai_native_entrants.md) | AI-native personal finance entrants in India and abroad; agentic finance; chatbot-versus-outcome evidence | Q1 (Indian entrants that could bundle compliance checks); Q3 (how regulated firms bound agent actions, relevant to human-in-the-loop design) |

## Key facts and where to find them

| Topic | Location |
|---|---|
| Common Advertisement Code consultation (23 Jun 2026), board approval (24 Sept 2026), celebrity definition, six-month transition in the draft | [b2b_fintech_gaps.md, section 2](b2b_fintech_gaps.md); [report, Profile 4](00-full-research-report.md) |
| Notified code text and effective date | Not found in any file (**[Unconfirmed]**) |
| AI-use disclosure (8 Jan 2025) and AI-output liability (10 Feb 2025) | [regulation_and_rails.md, Q1 and Q4](regulation_and_rails.md) |
| Finfluencer circulars (Aug 2024, Oct 2024, 29 Jan 2025) | [regulation_and_rails.md, Q4](regulation_and_rails.md) |
| CSCRF deadlines, exemptions and clarification of 30 Apr 2025 | [b2b_fintech_gaps.md, section 2](b2b_fintech_gaps.md) |
| Buyer counts (RIAs, RAs, PMS, top MFDs) | [b2b_fintech_gaps.md, section 1](b2b_fintech_gaps.md); [report, Profile 4](00-full-research-report.md) |
| DPDP timeline and penalties | [regulation_and_rails.md, Q8](regulation_and_rails.md) |
| Suggested stack and the "no fine-tuning" rule | [report, Table 15](00-full-research-report.md) |

## Known gaps carried from the research

- Notified advertisement-code text, effective date, report recipient and format, and record-retention period.
- Buyer counts for brokers and for each CSCRF category.
- Whether CSCRF restricts sending client data to offshore model APIs.
- Call-recording and audit-tool vendors and pricing; IRDAI advertising rules.
- Sales-cycle lengths for Indian buyer types are inference, not sourced.
