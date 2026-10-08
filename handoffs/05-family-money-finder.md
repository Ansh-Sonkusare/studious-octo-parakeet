# Handoff: Family Money Finder and Transmission Concierge

*As of 8 October 2026 (evidence cut-off 7 October 2026). **Inference** = team judgement, not sourced. **Assumption** = number to replace with pilot data. **Conflict** = sources disagree.*

## 1 TL;DR

- **What:** an AI-assisted concierge that, with consent, searches for a family's unclaimed money in India (bank deposits, shares and dividends, mutual funds, insurance, EPF), ranks what it finds, builds a document pack for each institution, and tracks every claim to completion.
- **For whom:** adult children and NRIs settling a parent's estate; later, elderly parents doing planning.
- **Why now:** discovery is free, but claiming is not. RBI's UDGAM portal covers about 30 banks and about 90% of unclaimed deposit value, yet [claiming still means visiting the bank with documents](https://www.outlookmoney.com/banking/udgam-how-to-claim-unclaimed-bank-deposits-through-rbis-portal). Only about ₹5,777 crore has been returned through government drives against a headline pool of about ₹2.2 lakh crore (about 2.6%, inference). Discovery plus paperwork help needs no licence.
- **Core bet:** families will pay a flat "Estate Pack" plus a modest success fee to have the money found and the paperwork done correctly, and a small team can deliver it with retrieval plus deterministic rules and human review of every outbound document.
- **Rank:** #5 of 14 (3.60/5): regulatory ease 5; willingness to pay, agent fit and build feasibility 3 each. The report calls it a strong module to add to health-claim recovery (Project 1).
- **Success in 90 days:** a repeatable, paid concierge where (a) the sweep finds a previously unknown claimable asset for at least 50% of families, (b) at least 70% of packs are accepted without rework, (c) at least 30% of qualified families accept the fee terms, and (d) at least 10 claims are paid out (proposed thresholds, Section 11).

## 2 Problem and evidence

Figures are secondary reporting of government or regulator data.

| Pool | Figure (date) | Notes and conflicts |
|---|---|---|
| Bank deposits (RBI DEA Fund) | ₹72,454 cr (28 Jan 2026, Rajya Sabha) ([FPJ](https://www.freepressjournal.in/business/unclaimed-bank-deposits-in-rbis-dea-fund-reach-72454-crore-government-promotes-udgam-portal-multiple-nominations)); ₹86,917 cr (30 Jun 2026) ([Outlook Money](https://www.outlookmoney.com/banking/rs-86917-crore-in-unclaimed-bank-deposits-sbi-accounts-for-largest-share)) | **Conflict.** Also: over ₹67,000 cr (30 Jun 2025, [Angel One](https://www.angelone.in/news/market-updates/67-000-crore-in-unclaimed-deposits-sbi-leads-the-way-as-funds-transfer-to-government)); ₹78,213 cr (Mar 2024, RBI annual report via [Moneylife](https://moneylife.in/article/banks-returned-nearly-10300-crore-unclaimed-deposits-to-accountholders-in-3-years-rajya-sabha-told/79010.html)); ₹97,545 cr (Dec 2025 study); ₹98,073 cr (31 Jan 2026, one report). Figures three days apart (28 vs 31 Jan) differ by about ₹25,600 cr, suggesting different definitions. Verify against Rajya Sabha answers |
| Shares and dividends (IEPF) | 166 crore shares, 1,671 companies, ₹89,004 cr (30 Nov 2025); unpaid dividends ₹8,237 cr (Mar 2024) ([Business Today](https://www.businesstoday.in/amp/personal-finance/investment/story/reliance-industries-tops-iepf-unclaimed-shares-rs89000-crore-stuck-across-1671-companies-report-525182-2026-04-12)) | 75,417 claims approved in two years; only ₹77.82 cr of dividends refunded ([Outlook Money](https://www.outlookmoney.com/personal-finance/unclaimed-funds-in-iepf-over-75000-claims-approved-in-two-years-rs-7782-crore-dividend-refunded)). No national dividend total was found, so ₹8,237 cr is single-source |
| Mutual funds | ₹3,811 cr (31 Mar 2026); 71% unpaid dividends ([Cafemutual](https://cafemutual.com/news/industry/38475-unclaimed-mutual-fund-money-rises-153-in-three-years-to-rs-3811-crore)) | Causes: outdated bank details, address changes, incomplete KYC |
| Insurance | ₹20,062 cr (FY24, study) vs ₹8,973.89 cr (government reply citing IRDAI) ([Dataful](https://insights.dataful.in/articles/indias-growing-pool-of-unclaimed-money-across-banks-insurance-companies-and-investments)) | **Conflict**, more than 2x apart |
| EPF | About 174 lakh of 796 lakh claims rejected in FY25 (about 22%) ([Business Today](https://www.businesstoday.in/personal-finance/news/story/epfos-instant-pf-withdrawal-promise-has-a-catch-one-in-five-claims-still-gets-rejected-541466-2026-07-07)) | A rejection rate, not a balance. No death-claim data collected |

**Total:** about ₹2.2 lakh crore across banks, EPF, insurance, shares and MFs ([Business Today](https://www.businesstoday.in/amp/personal-finance/news/story/rs-22-lakh-crore-unclaimed-funds-lie-idle-across-banks-epf-insurance-stocks-mfs-524958-2026-04-10)). High-end components above sum to about ₹2.19 lakh cr before EPF and low-end to about ₹1.82 lakh cr (inference), so treat ₹2.2 lakh cr as upper-end. About ₹5,777 cr across 23 lakh claims was returned by Feb 2026 ([Sentinel Assam](https://www.sentinelassam.com/more-news/national-news/government-steps-up-efforts-to-return-rs-73000-cr-unclaimed-funds-minister-pankaj-chaudhary)), roughly ₹25,000 per claim (inference).

**Why it stays unclaimed:** search is free, but transmission after a death is paper-heavy, institution-specific and often needs branch visits; IEPF claims (Form IEPF-5 plus company verification) are notoriously slow.

**Gaps:** no public data on transmission volumes, time to settle, serviceable families, willingness to pay, or NRI cross-border inheritance. US analog: executors report about 16 months, 570 hours and about $12,400 in fees per estate ([WTOP](https://wtop.com/lifestyle/2021/02/liz-weston-why-you-dont-want-to-be-an-executor/), 2021 survey, n=1,201).

## 3 Target users, personas and jobs-to-be-done

| Persona | Situation | Jobs-to-be-done |
|---|---|---|
| **Adult child after a death** (urban, 30-55; payer and doer) | Records scattered across banks, folios, policies, EPF. Grieving, time-poor | "Tell me everything my parent left." "Tell me exactly what each institution needs, in order." "Tell me where each claim stands" |
| **NRI heir** (about 3.43 crore overseas Indians including PIOs, [secondary source](https://indiannewslink.co.nz/malayalis-lead-indias-nri-wealth-inflows); no NRI-only count) | Cannot attend branches. NRO repatriation is capped at $1M a year ([Finnovate](https://www.finnovate.in/learn/blog/nri-repatriation-rules-explained)) | "Do this remotely." "Tell me what needs a local representative and what is needed to move money abroad" |
| **Elderly parent planning** (secondary) | Consent needed | "Show my family where everything is." "Fix nominee gaps now" |

## 4 Competitive landscape

No AI-native Indian competitor was found, but the sweep was limited: fee-based IEPF agents and will startups were not researched. Finish the sweep in week 1.

| Player | What it does | Gap |
|---|---|---|
| **Government portals** (UDGAM, IEPF, MITRA, MFCentral) | Free search, one asset class each | Claiming is manual. Also the product's data sources, so a dependency |
| **Banks, RTAs, insurers, EPFO** | Publish own transmission procedures | Rules vary and are rarely in one place; no cross-institution view |
| **Human services** (CAs, advocates, fee-based IEPF agents, will and estate startups) | Succession certificates, legal-heir work, IEPF recovery | Per-case human effort; pricing unresearched; also a referral channel |
| **Insurance Samadhan** (human-run; about ₹6.2 cr FY25 revenue) ([Inc42](https://inc42.com/company/insurance-samadhan/financials/)) | Insurance grievances | Adjacent; benchmark for success-fee services |
| **NRI fintechs** (Aspora, Abound, Belong) ([FinTech Futures](https://www.fintechfutures.com/venture-capital-funding/remittance-platform-aspora-raises-53m-series-b)) | Remittance, banking, investing | None reported to handle inheritance; could add it |
| **Family trackers; US analogs** (Atticus at $175-$499 a plan, MissingMoney) ([Atticus](https://www.weareatticus.com/faqs)) | Living members' MFs; US estate help and free unclaimed-property search | No death or unclaimed flows (India trackers); US-specific |

## 5 Product specification

### MVP scope

| In | Out |
|---|---|
| Discovery sweep: banks (UDGAM), IEPF, MFs, insurance, EPF | Handling client money; payouts go to the claimant |
| Ranked claim list (value, ease, speed) | Investment advice on inherited assets |
| Per-institution pack: claim forms, indemnity and affidavit drafts, checklist, cover letter | Court filings, succession or probate petitions (refer to an advocate) |
| Nominee vs legal-heir route from a rules library | Account Aggregator integration (needs regulated FIU status) |
| Human review of every outbound document | Property, vehicles, foreign assets |
| Claim tracking, reminders, escalation drafts | Contested estates and heir disputes |
| NRI concierge via a local representative | Autonomous portal login, scraping or OTP handling |

### End-to-end flow

Intake (WhatsApp or web) → consent and authority check (for a death: death certificate and relationship proof) → document extraction → discovery sweep → ranked list → pack generation and human review → family submits (online, branch or local representative) → tracking to payout → success fee.

### Agent workflow

1. **Profile:** names and spelling variants, PAN, DOB, addresses; these become search keys.
2. **Run guided searches:** the agent prepares inputs and records results; the user performs any OTP step.
3. **Entity-match** hits by name, address and folio; low-confidence matches go to a reviewer.
4. **Classify** each hit: asset class, institution, estimated value.
5. **Choose the route** with deterministic rules: nominee present, joint holder, thresholds, succession or legal-heir certificate need, indemnity need. Thresholds are institution-specific and not in the research notes; compiling them is the first research task.
6. **Rank** by value, probability, effort and expected time.
7. **Generate the pack** from templates; the model drafts only explanations and cover letters.
8. **Review and release** against a checklist.
9. **Track** each claim: reminders, follow-up and escalation drafts.
10. **Close:** log outcome, amount and days elapsed; consented cases feed the golden set.

### Features

| Feature | Priority |
|---|---|
| Intake, consent and authority check; document vault | P0 |
| Discovery sweep and ranked claim list | P0 |
| Rules library for top institutions (route, thresholds, forms) | P0 |
| Pack generator and human review console | P0 |
| Claim tracker, audit log, flat-fee payments | P0 |
| EPF death-claim pack; success-fee e-mandate; Hindi and regional languages; NRI workflow (remote consent, local representatives, repatriation checklist) | P1 |
| Partner dashboard (white label); Project 1 cross-sell | P1 |
| Nominee and KYC audit for living parents; estate map | P2 |
| DigiLocker for the claimant's own documents; institution submission APIs | P2 |

## 6 Technical architecture

### Components and stack (suggested)

| Component | Suggested implementation |
|---|---|
| Intake | WhatsApp Cloud API or an Indian BSP (Gupshup, Interakt) plus web upload; frontier models read PDFs and photos directly (report Table 15) |
| Vault | Encrypted object storage, per-case keys; field-level encryption for PAN |
| Knowledge base | Postgres with pgvector (e.g. Supabase): versioned institution transmission policies, [RBI DEA Fund guidelines](https://website.rbi.org.in/documents/87730/39016390/GuidelinesDEAFund25062025_AN6.pdf) (revised 25 Jun 2025), IEPF procedure, SEBI MITRA circular (12 Feb 2025) |
| Rules engine | Deterministic code and a versioned requirement matrix per institution and asset class, with effective dates |
| Models | Mid-tier model for drafting; small model for classification and matching. **No fine-tuning** |
| Documents and ops | Merge-field templates (HTML or DOCX to PDF), so the model never invents a form field; reviewer console; claim state machine |
| Payments | Razorpay or similar for the upfront fee; UPI AutoPay or e-mandate for success fees (RBI rules effective 21 Apr 2026: 24-hour pre-debit notice, extra authentication above ₹15,000) |

### Data sources and portals

| Source | Gives | MVP approach and caveats |
|---|---|---|
| **UDGAM** (RBI) | Unclaimed deposits, about 30 banks, about 90% of value | Guided search; claim at the bank. Login rules to verify |
| **IEPF** (MCA) | Shares and dividends | Search plus Form IEPF-5 and company verification; slowest route |
| **MITRA** (SEBI; CAMS and KFintech) | Inactive and unclaimed folios; nominees can report a death once via a new KRA mechanism ([TaxGuru](https://taxguru.in/sebi/one-stop-solution-track-reclaim-forgotten-mutual-fund-investments.html)) | Guided search. MFCentral third-party pulls were curtailed Sep-Nov 2025, so fall back to CAS upload with [casparser](https://github.com/codereverser/casparser) |
| **Insurer search** | Bima Bharosa, insurer unclaimed pages | Guided, per insurer |
| **EPFO** | Passbook, UAN, status | User-assisted only; no credential storage |
| **DigiLocker** (API Setu) | Claimant's own documents; requester API specs and onboarding exist; wrappers include Cashfree and Decentro ([API Setu](https://apisetu.gov.in/digilocker)) | P2. No consumer agent found. Access to a deceased person's records is an open question |

### AI approach, evaluation, security

- **Retrieval over procedures; deterministic rules for anything with a right answer.** Fine-tuning a generator lowered faithfulness in FinanceBench tests ([arXiv 2404.11792](https://arxiv.org/html/2404.11792)); frontier models score 70-90% zero-shot on Indian regulatory QA ([IndiaFinBench](https://arxiv.org/pdf/2604.19298)). The model may state a threshold, form or amount only if the rules engine or a cited source supplies it.
- **Golden set:** the first 30 concierge cases, growing to about 150 items (assumption), run in CI on every prompt, model or rules change. Track requirement accuracy (target at least 95%), route accuracy, name-match precision and recall, reviewer edit rate, first-submission acceptance.
- **Data handled:** PAN, bank statements, death certificates, relationship proofs. DPDP Rules were notified Nov 2025; core duties bind from about May 2027, with penalties up to ₹250 cr for security failures ([Deccan Herald](https://www.deccanherald.com/india/centre-notifies-dpdp-rules-implementation-planned-in-phases-spread-over-12-18-months-3798465), [Uniqus](https://uniqus.com/digital-personal-data-protection-act-timelines/)). IT Act SPDI Rules apply meanwhile. Build to the DPDP standard now.
- **Controls:** encryption; role-based reviewer access; mask PAN before LLM calls where possible; no training on customer data; deletion on request and default retention after closure (assumption: 90 days); vendor DPAs. Offshore LLM APIs are cross-border processing (allowed unless the destination is blacklisted; flagged for legal review).
- **Audit log:** append-only; prompts, retrieved documents, tool calls, rule and model versions, reviewer identity, user confirmations.

## 7 Regulatory and legal

**Licences.** None needed for discovery plus paperwork help, if the product never sells insurance or accepts commission from banks, insurers, RTAs or advisers; never advises on what to do with inherited investments (SEBI RIA territory); never holds client money; and does not act as an Account Aggregator FIU. Adjacent needs: a CA for Form 15CB on NRI repatriation (about ₹3-10k, vendor estimate, [Belong](https://getbelong.com/blog/returning-nris/repatriation-guide.md)); an advocate for succession certificates and probate.

**Representation limits.** The claimant (nominee, legal heir or executor) signs and submits; the product prepares and guides. Record the scope of any power of attorney from a living claimant in writing. A power of attorney from the deceased ends at death (general principle, not in the sources; counsel to confirm).

**Open legal questions** (counsel opinion before launch):
1. Does drafting indemnities, affidavits and legal-heir declarations amount to legal practice under the Advocates Act (also raised for Project 1)? Which operating model keeps the product on the "drafting software plus service" side?
2. May the product pay or receive referral fees from advocates or CAs?
3. How does DPDP treat a deceased person's data, and on what basis may it be searched?
4. Is offshore LLM processing of PAN and death certificates acceptable?
5. Does a success fee on inherited money create consumer-protection risk?
6. State-wise stamp duty and notarisation rules for indemnities.

**Compliance checklist**
- [ ] Legal opinion on the six questions
- [ ] Private limited company; terms of service and success-fee contract reviewed
- [ ] Consent and notice flow; DPDP-grade deletion and breach response
- [ ] Authority-verification policy (death certificate and relationship proof before any deceased-person search)
- [ ] Disclosure that AI drafts and a human reviews each document
- [ ] Written no-commission, no-money-handling, no-advice policy
- [ ] Vendor DPAs; complaint-handling and refund policy

## 8 Business model

| Model | Mechanics | Pros | Cons |
|---|---|---|---|
| Per-claim fee | ₹1,499 per institution pack, upfront (assumption) | Simple; covers cost | Heavy against a roughly ₹25,000 average claim |
| Success fee only | 8% of recovered amount (assumption; Project 1 hypothesis is 10-15%) | Aligned with outcome | Slow IEPF delays cash; collection risk; failed cases unpaid |
| **Bundled Estate Pack (recommended to test)** | ₹4,999 flat for discovery, up to 5 packs and tracking, plus 5% success fee on newly discovered assets (assumption) | Predictable revenue; incentives aligned | Needs trust before payment; untested |

**Unit economics (all inputs are assumptions).** Base case: 3 newly discovered claims at about ₹25,000 (the government-drive average) = ₹75,000 filed; 80% paid = ₹60,000 recovered; 70% of success fees collected (the Project 1 gate).

| Line | Arithmetic | ₹ |
|---|---|---|
| Pack fee | flat | 4,999 |
| Success fee | 5% x 60,000 x 70% | 2,100 |
| **Revenue per family** | | **7,099** |
| Reviewer time | 3 hours x ₹500 | 1,500 |
| Model, OCR, hosting | per family | 150 |
| Payment fees | about 2% of revenue | 150 |
| Stamp paper, notary, courier | per family | 250 |
| **Variable cost** | | **2,050** |
| **Contribution** | 7,099 - 2,050 | **5,049** |

- Same case under other models: per-claim = 3 x 1,499 = ₹4,497 revenue and ₹2,447 contribution; success-only = 8% x 60,000 x 70% = ₹3,360 revenue and ₹1,310 contribution, with cash arriving months later.
- Acquisition-cost ceiling: 30% of revenue, about ₹2,130.
- Break-even on an assumed ₹3 lakh monthly fixed cost: 300,000 / 5,049 = about 60 families a month before acquisition cost; 300,000 / (5,049 - 2,130) = about 103 after it.
- NRI variant (hypothesis): ₹9,999 including a local representative.

**B2B2C.** White-label estate support for MFDs, RIAs and CA firms at ₹5,000-15,000 a month per firm (Project 1 hypothesis); never accept money from institutions.

**Cross-sell with Project 1.** Both share one engine (ingestion, rules, packs, tracking); the report estimates about 70% stack reuse (inference) and sequences the family money finder in months 4-9 of the revenue ladder, as the redeploy path if health-claim recovery fails. Project 1 users with elderly parents are the warmest Estate Pack leads, and a death often leaves pending health and life claims (assumption).

## 9 Go-to-market

| Channel | Approach |
|---|---|
| **Search intent** | Hindi and English pages on claiming a deceased parent's accounts, legal-heir procedure, IEPF. Highest intent; slow to build |
| **NRI communities** | Facebook and WhatsApp groups, Reddit. Highest value per family; trust is the barrier |
| **CAs and advocates** | Referral: they send paperwork-heavy cases and keep legal work. Check fee-sharing rules first |
| **Banks' bereavement desks** | Assumption: long sales cycle, phase 2; not researched |
| **Advisers (MFDs, RIAs)** | White-label, Project 1 pricing |
| **Project 1 base** | Warm cross-sell |

**First 100 families (by week 12).**
- Funnel (assumption): about 250 qualified leads x 40% upload = 100 families; x 35% paying = about 35 paid.
- Lead mix: about 30 search and content, 25 NRI communities, 20 CA and advocate referrals, 15 Project 1, 10 advisers.
- Offer: a free or token discovery scan, then the Estate Pack; charge from the first paying case.
- Content: anonymised, documented recoveries.
- Serve the first 20 families manually; automate only steps done at least 20 times.

## 10 90-day execution plan

Assumed start: week of 12 Oct 2026; day 90 is about 10 Jan 2027.

| Phase | Weeks | Deliverables | Gate |
|---|---|---|---|
| 0 Setup | 0-1 | Legal opinion commissioned; entity; WhatsApp number, landing page, upload form; competitor sweep | Counsel engaged; leads flowing |
| 1 Manual concierge | 1-4 | Requirement matrix (top banks, CAMS, KFintech, top insurers, IEPF); 30 interviews; 20 families served; payment taken | At least 20 cases; at least 30% accept fee terms |
| 2 Automate | 4-8 | Extraction, matching, rules engine, pack generator, review console, tracker; golden set | Requirement accuracy at least 95%; reviewer time under 3 hours |
| 3 Scale | 8-12 | 100 families; 3 CA or advocate partners; 2 adviser partners; 15 NRI families; Project 1 cross-sell test | At least 70% first-submission acceptance |
| Decision | 13 | Review against Section 11 | Continue, pivot or stop |

**Checklist**
- [ ] Commission legal opinion; incorporate; open payment account; set up WhatsApp number, landing page, upload form
- [ ] Complete competitor sweep; verify DEA Fund figures; build the requirement matrix
- [ ] Run 30 interviews (adult children, NRIs, CAs, advocates)
- [ ] Serve 20 families manually; retain consented cases as the golden set
- [ ] Build vault, extraction, matching, rules engine, pack generator, reviewer console, tracker
- [ ] Sign 3 CA or advocate partners and 2 adviser partners
- [ ] Recruit local representatives for NRI cases (2 cities)
- [ ] Publish 10 intent pages and 5 proof stories
- [ ] Run the day-90 review

**Team (2-3 FTE plus advisors).** Product and operations lead running the concierge; full-stack or AI engineer; part-time reviewer. Retainer advisors: counsel, a CA, an advocate. Part-time writer for go-to-market.

## 11 Success metrics and kill/pivot criteria

Thresholds are proposals, adapted from the Project 1 gates.

| Question | Metric | Continue if | Pivot or stop if |
|---|---|---|---|
| Do families engage? | Qualified leads who upload documents | At least 40% | Under 20% |
| Does discovery add value? | Families with a previously unknown claimable asset | At least 50% | Under 25% |
| Are packs correct? | First-submission acceptance; requirement accuracy | At least 70%; at least 95% | Under 40%, or repeated wrong requirements |
| Will they pay? | Fee acceptance; success fees collected | At least 30%; at least 70% | Under 20% |
| Does money arrive? | Claims paid by day 90 | At least 10 | Zero outside IEPF |
| Is it economic? | Reviewer time; acquisition cost vs revenue | Under 3 hours; under 30% | Cost above revenue in every channel |

**Pivot paths:** consumer acquisition fails, so sell white-label to CAs, advocates and advisers; fee collection fails, so move to flat per-pack fees; discovery fails, so refocus on the nominee and KYC audit; demand weak, so fold into Project 1 as a module.

## 12 Risks and mitigations

| Risk | Mitigation |
|---|---|
| **Slow IEPF claims** (Form IEPF-5 plus company verification) | Set expectations in writing; price IEPF packs flat, not success-only; measure day-90 payouts excluding IEPF |
| **Branch visits and institution-specific demands** | Requirement matrix; per-branch checklist; local-representative network for NRIs; escalate to nodal officers |
| **Sensitive moment** (grief) | Plain language, short flows, no upsell in the first message, human contact option |
| Wrong requirement or form; legal-practice challenge | Rules engine plus retrieval only; mandatory human review; golden-set gates; counsel opinion first; claimant signs; court work referred to advocates |
| Impersonation (searching a living person's assets) | Authority checks, death certificate for deceased searches, parent's consent for living ones, audit log |
| Data breach | Encryption, minimal retention, access control, breach drill (DPDP penalties up to ₹250 cr) |
| Heir disputes | Decline or refer contested cases |
| Episodic demand, high acquisition cost | Partner channels; Project 1 cross-sell; nominee audit as a recurring product |
| Success-fee optics for a bereaved family; portal or terms changes | Low, capped fee with flat pack as main fee; user-driven searches, no scraping behind login |

## 13 Open questions and decisions needed

1. **Pricing:** Estate Pack alone or with a success fee? Which price points do interviews support?
2. **Legal:** counsel's view on the six questions, and who owns the workstream.
3. **Scope:** EPF death claims in the MVP? NRI in the first 90 days? Include the living-parent audit?
4. **Brand:** standalone product or Project 1 module?
5. **Data:** which DEA Fund and insurance figures to use externally, and who verifies them?
6. **Institutions:** which 10 banks and insurers first, and how to obtain their current transmission rules?
7. **Hosting:** offshore LLM API or India-region deployment for PAN and death certificates?
8. **Market size:** how to size families settling an estate each year, given no public data?

## 14 Expansion path

1. **Preventive nominee and KYC clean-up for living parents:** an estate-readiness audit with a nominee map, aligned with the government's push for multiple nominations. A simple will drafter is a low-regulation adjacent feature (wills need no registration in India; inference, unverified).
2. **NRI estate and cross-border:** remote workflows, local representatives, NRO repatriation (the $1M annual cap, Forms 15CA and 15CB), later the NRI tax autopilot (Profile 6). Cross-border inheritance evidence is weak; validate first.
3. **US unclaimed property and estate:** states returned about $4.25B in FY2025 and NAUPA estimates 1 in 7 Americans has unclaimed property ([NAUPA](https://unclaimed.org/wp-content/uploads/NAUPA-FY-25-Report.pdf)); the repeated $70B holdings figure is dated and unverified. Finder-fee legality varies by state (unresearched). An executor autopilot is a separate opportunity.
4. **Later:** MF portfolio fixer under a corporate RIA licence (Profile 7).

## 15 Sources

- **Research report:** `reports/India AI personal finance MVP.md` (sections 7, 8 including Profile 5, and 10; section 9.5 gates).
- **Research notes** (`research_notes/India AI personal finance MVP/`): `household_finance_gaps.md` (sections 5 and 8), `investor_pain_points.md`, `financial_gaps_sizing.md`, `global_underserved_segments.md`, `regulation_and_rails.md`, `agentic_rails_trends.md`, `tech_feasibility.md`.
- **External sources** are linked inline; most are secondary reporting of regulator or parliamentary data.
- **Caveat:** the research relied heavily on search summaries. Verify every figure against primary documents before external use.
