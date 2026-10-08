# Handoff: Health-Claim Recovery Agent

*As of 8 October 2026. Ranked #1 of 14 opportunities (4.10/5). Facts carry inline source links; items marked **Assumption** or **Inference** are working estimates to test in the pilot.*

## 1 TL;DR

- **What:** an AI agent that takes a rejected or short-paid health-insurance claim, maps every deduction to the policy clause and IRDAI rule behind it, drafts the insurer grievance, then the Bima Bharosa and Insurance Ombudsman complaints, and tracks the case until money is recovered.
- **For whom:** urban salaried families with individual or family-floater policies, and adult children handling parents' claims. Later: employer HR teams, mutual-fund distributors (MFDs) and RIAs offering claim support to clients.
- **Why now:** about ₹26,037 crore of health claims were rejected or disallowed in FY24, grievance volumes are rising, the August 2024 IRDAI master circular created citable rules, long-context models can read policy wordings, and no AI-native player runs the full job.
- **The core bet:** households will pay (upfront fee plus success fee) to recover money already lost, and AI plus human review can cut cost per case enough to be profitable, which the human-operated incumbent has not achieved at scale.
- **Success in 90 days (proposed):** 50-100 live cases; clause-citation precision at least 95% with zero invented clauses; at least 25% reversal at the insurer stage; at least 30% fee acceptance; at least 70% of success fees collected; acquisition cost under 30% of expected fee. Otherwise pivot to B2B2C or stop (Section 11).

## 2 Problem and evidence

Insurers bear little cost when a deduction goes uncontested, and policyholders do not know the escalation ladder: insurer grievance officer, then Bima Bharosa or the Ombudsman after 30 days, then consumer court ([Outlook Money](https://www.outlookmoney.com/insurance/mis-selling-complaints-grew-112-since-2024-value-of-disputed-claims-rose-10-report)).

| Evidence | Figure | Source |
|---|---|---|
| Value rejected or disallowed, FY24 | ₹26,037.65 cr (about ₹15,100 cr "disallowed" under policy terms, about ₹10,937 cr repudiated) | [Moneylife (Lok Sabha reply)](https://moneylife.in/article/health-insurance-claims-worth-rs2603765-crore-rejected-by-insurers-in-fy2324-govt/76282.html); [Outlook Business](https://www.outlookbusiness.com/economy-and-policy/health-insurers-disallowed-claims-worth-rs-15100-crore-during-fy24) |
| Claims, FY25 | 3.26 crore processed; 87% settled, 8% repudiated (FY24: 11%); payouts ₹94,248 cr | [Algates summary of IRDAI Annual Report](https://algatesinsurance.in/irdai-annual-report-2024-25-highlights/) |
| Consumer survey (Jan 2025) | Over 50% of claimants in the prior three years faced rejection or partial approval (survey base unclear) | [Business Today](https://www.businesstoday.in/amp/personal-finance/insurance/story/insurance-claims-over-50-health-cover-claims-faced-rejection-or-partial-approval-says-survey-459394-2025-01-02) |
| Bima Bharosa grievances (all lines) | 47,658 (FY24) to 64,365 (FY25) to 73,729 (FY26 to Feb) | [TaxGuru](https://taxguru.in/?p=1035064) |
| Ombudsman health complaints, FY24 | 31,490 (up from 25,873); about 95% concern claim rejections | [Outlook Money](https://www.outlookmoney.com/amp/story/personal-finance/why-95-per-cent-of-health-insurance-complaints-concern-claim-rejections) |
| Ombudsman, FY25 | By insurer: Star Health 12,186; Care 4,423; Niva Bupa 3,983. About 41% reported in policyholders' favour (6,126 resolved in favour, 9,417 recommended for settlement) | [Cafemutual](https://cafemutual.com/news/industry/36635-41-of-health-insurance-complaints-were-resolved-in-favour-of-policyholders-in-fy25) |
| Partial-payment causes | Co-pay, room-rent cap with proportionate deduction, sub-limits, non-payables | [Money9](https://www.money9.com/news/exclusive/understanding-cashless-health-insurance-challenges-and-solutions-139314.html) |

Caveats:

- **Data conflicts.** FY25 Ombudsman totals are 37,431 (trade press) versus 53,102 (Lok Sabha reply). IRDAI does not publish insurer-level rejection reasons ([Insurance Business Asia](https://www.insurancebusinessmag.com/asia/news/life-insurance/irdai-cannot-explain-why-health-insurance-claims-go-unpaid-583814.aspx)). Most figures are secondary coverage, not primary PDFs.
- **The "41%" needs care (Inference).** 6,126 + 9,417 = 15,543, which is about 41.5% of 37,431. The headline appears to count "recommended for settlement" alongside awards. Treat 41% as an upper-bound context figure, not a win rate; hence the pilot's 25% threshold.
- **Process gaps.** Bima Bharosa is not integrated with the Ombudsman system, so complainants file twice ([Lok Sabha answer](https://eparlib.sansad.in/bitstream/123456789/3015516/1/AS20_AaaDVE.pdf)). Since the master circular (1 Aug 2024), repudiation needs Claims Review Committee approval, a trail the agent can cite ([Moneylife](https://moneylife.in/article/health-insurance-decide-cashless-request-in-1-hour-provide-final-authorisation-for-discharge-within-3-hours-says-irdai/74269.html)).
- **Sizing (Inference).** Recovering 2% of the ~₹26,000 cr pool at a 15% fee is about ₹78 cr a year (26,000 × 0.02 × 0.15), a ceiling illustration, not a forecast.

## 3 Target users, personas and jobs-to-be-done

| Persona | Situation | Job to be done | Willingness to pay (hypothesis) |
|---|---|---|---|
| **Rejected claimant** (primary): urban salaried policyholder | Cashless denied or settlement cut by room-rent deduction, waiting period, pre-existing-disease ground or "non-payables" | "Tell me if this deduction is legitimate and get my money back." | Upfront fee plus success fee |
| **Caregiver child** (primary) | Parent hospitalised; documents scattered; parent cannot handle portals or OTPs | "Handle the paperwork and deadlines while I work." | Higher: time-poor |
| **Distributor or adviser** (B2B2C): MFD, RIA, insurance adviser | Clients ask for claim help the adviser cannot give at scale | "Offer claim support under my brand without a claims desk." | Monthly firm licence |
| **Employer HR team** (B2B2C) | Employees escalate claim problems to HR | "Cut HR time lost to disputes; add a visible benefit." | Per employee per month |

Not users: hospitals, TPAs, and anyone wanting to buy or compare policies.

## 4 Competitive landscape

| Player | Model | Strengths | Gaps |
|---|---|---|---|
| **Insurance Samadhan** (India) | Human-operated claim-resolution service on success fees; raised ₹8.5 cr in 2025; self-reports 18,000+ complaints resolved, ₹160 cr recovered; about ₹6.2 cr FY25 revenue (Inc42 estimate) ([Entrackr](https://entrackr.com/snippets/insurance-samadhan-secures-rs-85-cr-to-boost-tech-infrastructure-9040178); [Inc42](https://inc42.com/company/insurance-samadhan/financials/)) | Brand, operating experience | Labour-intensive; AI claim weakly supported; revenue suggests an early ceiling |
| **Ditto** (India) | Advisory-led broker with claim support; about ₹97.1 cr FY25 revenue (Inc42 estimate) ([Inc42](https://inc42.com/company/ditto-insurance/)) | Zerodha/Rainmatter backing; trust | Claims help supports a commission business |
| **Free self-service** | Bima Bharosa, grievance officers, Ombudsman offices | Zero cost | Not integrated; users do not know the ladder or the clause arguments |
| **PolicyBazaar and others** | Marketplaces | Scale | No claim-assistance data retrieved; commission model |
| **US analogues** | Counterforce (free, grant-funded); Claimable ($50 per letter); Sheer Health; Aegis ([PYMNTS](https://www.pymnts.com/artificial-intelligence-2/2026/insurance-denials-meet-their-match-in-ai-powered-appeals/); [Axios](https://www.axios.com/local/raleigh/2025/08/20/using-ai-to-fight-back-against-insurance-denials-counteforce)) | Early traction (self-reported rates) | Letter-only or free |

No AI-native Indian player running the full job was found; this reflects the search conducted, not proof none exists. Insurers may resist; the moat is a clause-and-outcome corpus, not the model.

## 5 Product specification

### 5.1 MVP scope

| In scope | Out of scope |
|---|---|
| Retail individual and family-floater health policies, top 8-10 products by Ombudsman complaint volume | Selling, comparing or recommending policies; any commission |
| Rejected, partially paid and short-paid claims (room-rent deduction, co-pay, sub-limits, non-payables, waiting period, pre-existing disease, documentation gaps) | Group policies with bespoke wordings |
| English and Hindi; WhatsApp and web intake; voice notes | Hospital bill audit; pre-admission cost simulation |
| Insurer, Bima Bharosa and Ombudsman drafts; deadline tracking; human review of every letter | Filing without the user's own login and OTP |
| Fee collection by the product, never from the insurer | Consumer-court litigation; legal advice; client money |
| Case database and outcome logging | US claims, life disputes, other languages |

### 5.2 End-to-end user flow

1. User sends documents (policy, rejection or settlement letter, discharge summary, bills) on WhatsApp or the web.
2. Within minutes the user receives a **Claim X-ray**: each deduction, the clause, likely recoverable amount, route and deadline.
3. User accepts fee terms and consents to data processing.
4. Agent drafts the insurer grievance; a reviewer approves; the user submits via a guided walkthrough with their own login and OTP.
5. If unresolved in 30 days, the agent prepares the Bima Bharosa and Ombudsman filings and keeps a dated case file.
6. On recovery, the fee is collected and the outcome logged (anonymised for proof content, with consent).

### 5.3 Agent workflow, step by step

1. **Ingest** documents (OCR and direct model reading); extract policy, insurer, product, dates, amounts.
2. **Match** the product and wording version in the corpus; flag unknown versions for human lookup.
3. **Classify each deduction**: room-rent proportionate deduction, waiting period or pre-existing disease, non-payable item, co-pay or sub-limit, documentation gap, other.
4. **Cite** the clause and the IRDAI rule for each; mark deductions that look valid, so the product never charges for unwinnable items.
5. **Compute** the recoverable amount with deterministic code. The model may state only tool-computed figures or cited clauses.
6. **Draft** the insurer grievance, then Bima Bharosa and Ombudsman filings (Annexure VI-A, per the research notes).
7. **Review**: a claims reviewer approves or edits each letter; edits feed the golden set.
8. **Guide** submission with the user's own login and OTP; capture acknowledgement numbers.
9. **Track** deadlines and replies; escalate along the ladder; record the outcome.

### 5.4 Feature list

| Priority | Feature | Notes |
|---|---|---|
| P0 | WhatsApp and web intake, document reading | Weeks 3-7 |
| P0 | Policy wording corpus and versioned IRDAI rules library | Hybrid retrieval |
| P0 | Deduction taxonomy, classifier and deterministic calculator | Numbers only from tools |
| P0 | Claim X-ray with clause citations | The hero deliverable |
| P0 | Letter templates (insurer, Bima Bharosa, Ombudsman) and reviewer console | Human-reviewed |
| P0 | Audit log, deadline tracker; consent, deletion, AI disclosure | Trust and legal prerequisite |
| P1 | Payments: gateway for upfront fee; e-mandate or UPI link for success fee | Collect manually at first |
| P1 | Hindi voice notes (Sarvam speech-to-text about ₹30 per audio hour, [Sarvam pricing](https://docs.sarvam.ai/api-reference-docs/getting-started/pricing)) | Cheap |
| P1 | Partner dashboard and white-label links | For the B2B2C test |
| P2 | Insurer-reply parsing; outcome analytics on winning arguments | After 100+ cases; builds the data moat |
| P2 | Bima Sugam integration | Launch targeted Nov 2026 (weak source); has slipped before |

## 6 Technical architecture

### 6.1 Components and stack (suggested)

| Component | Implementation |
|---|---|
| Intake | WhatsApp Cloud API or an Indian BSP (Gupshup, Interakt) plus web upload |
| Knowledge base | Postgres with pgvector (e.g. Supabase): versioned wordings and IRDAI rules with effective dates |
| Reasoning | Mid-tier model for drafting; small model for deduction classification; API access, **no fine-tuning** |
| Numbers | Deterministic code for deductions, sub-limits, waiting periods, deadlines |
| Controls | Review console, append-only audit log, deadline reminders |
| Payments | Gateway for upfront fee; UPI AutoPay or e-mandate for success fee |

### 6.2 Data sources and rails

User-supplied documents; insurers' published wordings; IRDAI circulars; published Ombudsman awards; later Bima Sugam. The MVP has no insurer API or Account Aggregator dependency. Filing always uses the user's own OTP, so the product is a guided co-pilot, not an autonomous filer.

### 6.3 AI approach

Retrieval plus deterministic tools on a frontier or mid-tier model. The research found retrieval beats fine-tuning for knowledge that changes, and tools, not models, fix numeric errors ([arXiv 2601.07054](https://arxiv.org/html/2601.07054v1)).

- Hybrid search (keyword, embeddings, reranker) over a versioned corpus, starting with insurers drawing the most Ombudsman complaints.
- Every figure comes from a tool or a cited clause; citations are mandatory; the agent refuses when no clause is found.
- Internal tools: `get_clause`, `search_irdai_rules(as_of)`, `compute_proportionate_deduction`, `check_waiting_period`, `compute_deadlines`, `draft_letter`.
- No fine-tuning; revisit only for the retriever or narrow classifiers.
- Cost (Inference): under $200 a month in API spend for 70 pilot users ([braindetox](https://braindetox.kr/en/posts/ai_api_pricing_comparison_2026.html)). Case analysis uses longer documents, so Section 8 assumes ₹100 per case.

### 6.4 Evaluation plan

| Item | Plan |
|---|---|
| Golden set | 200-300 annotated deductions with ground-truth clause and amount, from 100 consented anonymised files; signed off by a former TPA or claims specialist (weeks 2-5) |
| Release gates | Clause-citation precision at least 95%; zero invented clauses; amounts within ±2% |
| Extra metrics (**Assumption**) | Deduction-class accuracy at least 90%; correct refusal of "guarantee recovery" or legal-advice prompts. Users cannot judge clause correctness, so user testing alone is not evaluation |
| Cadence | Full set in CI on every prompt, model or corpus change |
| Live monitoring | Reviewer edit rate (below 30% by week 12), reviewer minutes per case (below 20), insurer outcomes |

### 6.5 Security, privacy and audit

- Treat all documents as health data (**recommendations**): minimise collection, encrypt, restrict reviewer access, redact identifiers before model calls where possible, host in India.
- Consent at onboarding, retention limits, one-click deletion. The IT Act SPDI Rules 2011 apply now; DPDP fiduciary duties (notice, consent, security, breach notification, rights) bind from about May 2027, with penalties up to ₹250 cr ([Deccan Herald](https://www.deccanherald.com/india/centre-notifies-dpdp-rules-implementation-planned-in-phases-spread-over-12-18-months-3798465); [Uniqus](https://uniqus.com/digital-personal-data-protection-act-timelines/)). Build to DPDP standard now.
- Offshore model APIs mean cross-border processing; DPDP permits it unless the destination is restricted. Counsel should confirm; obtain zero-retention terms.
- Append-only audit log: prompts, retrieved passages, tool calls and outputs, model version, reviewer edits, consents, timestamps.
- IRDAI has warned of fake sites impersonating Bima Bharosa ([Cyril Amarchand blog](https://corporate.cyrilamarchandblogs.com/2026/01/insurance-distribution-in-india-emerging-channels-compliance-and-data-governance/)); use a verified WhatsApp Business profile.

## 7 Regulatory and legal

| Activity | Licence | Position |
|---|---|---|
| Claim and grievance assistance, policy explanation | None found for the MVP; Insurance Samadhan operates on success fees | Permitted if no commission and no sale |
| Insurance comparison or sales for commission | IRDAI web aggregator (₹25 lakh minimum capital), broker or corporate agent | **Avoid** |
| Money from insurers, brokers or hospitals | Treated as distribution | **Prohibited**; IRDAI fined Acko ₹1 cr (May 2025) for commissions routed to an unlicensed entity ([Outlook Money](https://www.outlookmoney.com/insurance/acko-gets-rs-1-crore-irdai-fine-what-it-says-about-how-your-insurance-is-sold)) |
| Handling client money | Payments and trust exposure | **Never**; the insurer pays the policyholder |
| E-mandate fee collection | RBI rules effective 21 April 2026 (per the report): 24-hour pre-debit notice, extra authentication above ₹15,000 | Verify with the payment partner |

**Open legal questions (for counsel):**

1. Can a non-lawyer service assist complainants before the Insurance Ombudsman? Representation rules are **not verified**; the Advocates Act position is open.
2. Is a consumer success-fee contract enforceable and adequately disclosed?
3. Does complaint drafting amount to legal practice? Mitigation: the user signs and submits.
4. Offshore LLM processing of health data under the IT Act rules and DPDP.
5. Current Ombudsman award cap (not verified).
6. Effect of the proposed internal insurer ombudsman (complaints up to ₹50 lakh; proposal only).

**Pre-launch compliance checklist**

- [ ] Legal opinion on Ombudsman representation, Advocates Act, success-fee enforceability
- [ ] Private limited company; terms of service and success-fee contract reviewed by counsel
- [ ] Written policy: no money from insurers, brokers or hospitals; no policy sales
- [ ] Health-data consent, retention and deletion flow live
- [ ] Disclosure: AI drafts, a human reviews, no guaranteed outcome
- [ ] Payment partner confirms e-mandate and pre-debit rules
- [ ] Zero-retention terms with the model vendor; breach-response procedure
- [ ] Consent recorded before any recovery is advertised

## 8 Business model

All prices, conversion rates and costs below are **Assumptions** for the pilot to replace with data.

**Pricing hypotheses**

- Consumer: ₹499 per filing upfront plus 10-15% success fee on the amount recovered; a token ₹299 from case one during concierge weeks, because payment is the signal under test. Fallback: flat per-filing fee.
- No client money is held; the fee is collected by e-mandate at onboarding or a UPI link after settlement.

**Unit economics (per filed case)**

| Line | Arithmetic | ₹ |
|---|---|---|
| Upfront fee | Given | 499 |
| Expected success fee | 0.40 recovery × 12% × ₹40,000 | 1,920 |
| **Revenue per filed case** | 499 + 1,920 | **≈ 2,419 (≈ 2,400)** |
| Revenue after 70% fee collection | 499 + (0.70 × 1,920) | ≈ 1,843 |
| Variable costs (Assumption) | CAC 700 + reviewer 20 min at ₹400/hour (133) + model/OCR 100 + gateway ~2% (48) | ≈ 981 |
| Contribution (at 100% collection) | 2,419 − 981 | ≈ 1,438 |
| Contribution (at 70% collection) | 1,843 − 981 | ≈ 862 |

- Viability condition from the research: CAC below about ₹700 per filed case and reviewer time below about 20 minutes.
- Scale: 420 filed cases a month × ₹2,400 ≈ ₹10 lakh monthly revenue.
- Break-even (Assumption: ₹6 lakh monthly cost): 600,000 ÷ 1,438 ≈ 420 cases, or 600,000 ÷ 862 ≈ 700 cases at 70% collection. Collection rate and CAC are the decisive variables.
- Cross-check: ₹160 cr ÷ 18,000 complaints ≈ ₹89,000 per resolved case (Insurance Samadhan, self-reported), so ₹40,000 looks conservative, though case mix will differ. Its ~₹6.2 cr revenue suggests the human-only model plateaus.

**B2B2C revenue** (steadier than episodic consumer demand)

| Buyer | Offer | Pricing hypothesis |
|---|---|---|
| MFDs and RIAs | White-label "claim support" for client families | ₹5,000-15,000 per month per firm (e.g. 20 firms × ₹10,000 = ₹2 lakh/month) |
| Employer HR teams | Claim support as a benefit | Per employee per month (price in pilot) |
| Unlicensed advisers | Referral partnership | Share of the success fee; never insurer money |

## 9 Go-to-market

**Channels in priority order**

1. **Intent search:** Hindi and English pages for "claim rejected", "room rent deduction" and insurer-specific queries, starting with Star Health, Care and Niva Bupa.
2. **Proof-led content:** anonymised, consented recoveries (for example "₹38,000 recovered from a proportionate room-rent deduction").
3. **Distribution partners:** 3-5 MFD, RIA or adviser partners; 2 employer HR teams.
4. **Communities:** Reddit, Facebook groups, consumer forums, housing-society WhatsApp groups.

**First-100-customers plan**

- [ ] Weeks 0-3: 10-20 concierge cases from interviewees and consumer forums, charged from case one.
- [ ] Weeks 3-6: launch landing pages and WhatsApp number; 30 cases from search and communities.
- [ ] Weeks 6-9: 3-5 partners with co-branded intake links; 30 cases.
- [ ] Weeks 8-12: 2 HR teams; 10-20 cases.
- [ ] Track CAC per channel from case one; stop any channel whose CAC exceeds the expected fee.

**Partnerships:** advisers and HR teams (channels); a former TPA specialist (reviewer); counsel; payment gateway; WhatsApp BSP. No money-linked ties to insurers, hospitals or brokers.

## 10 90-day execution plan

| Weeks | Workstream | Deliverables | Gate |
|---|---|---|---|
| 0-2 | Discovery and legal | 30 interviews with rejected claimants; 100 consented anonymised files; legal opinion commissioned; pricing documented | At least 20 of 30 would pay; no legal blocker |
| 2-5 | Corpus and evaluation | Wordings for top 8-10 products; IRDAI rules library; deduction taxonomy; 200-300 annotated deductions | Golden set signed off by a claims specialist |
| 3-7 | Build v0 | Intake, OCR, retrieval, calculator, letter templates, deadline tracker, review console | Citation precision at least 95%, zero invented clauses, amounts ±2% |
| 6-12 | Concierge pilot | 50-100 live cases over three channels; exceptions handled manually | Section 11 metrics |
| 10-13 | Decision | Unit-economics read-out, insurer-response cohort, decision memo | Continue, pivot to B2B, or stop |

Principle: sell the outcome manually first; automate only steps done by hand at least 20 times.

**Checklist**

- [ ] Incorporate; set up WhatsApp Business and a one-page site
- [ ] Run 30 interviews; synthesise willingness to pay
- [ ] Engage counsel (questions in Section 7) and a part-time claims specialist
- [ ] Collect and anonymise 100 files with written consent
- [ ] Build corpus and rules library; build golden set; wire CI evaluation
- [ ] Ship intake, X-ray, drafting, review console, audit log, consent and deletion flows
- [ ] Integrate payments (upfront and success fee)
- [ ] Launch English and Hindi landing pages and partner links
- [ ] Run pilot with weekly metrics review; write the decision memo by day 85

**Team (1-3 people plus advisers)**

| Role | Scope | Time |
|---|---|---|
| Product and GTM lead | Interviews, pricing, channels, partners | Full-time |
| Full-stack/AI engineer | Pipeline, retrieval, tools, evaluation | Full-time |
| Claims specialist (ex-TPA/insurer) | Review, golden-set sign-off | Part-time |
| Legal counsel | Opinion, contracts, privacy | External |
| Ops/support, Hindi content | Concierge handling | Part-time, from week 6 |

## 11 Success metrics and kill/pivot criteria

Thresholds are the research team's proposals; Ombudsman outcomes may take longer than the pilot, so the 90-day test uses leading indicators.

| Question | Metric | Continue if | Pivot / stop if |
|---|---|---|---|
| Do users arrive at the moment of pain? | Share of qualified leads who upload documents | ≥40% | <20% |
| Is the engine correct? | Golden-set clause precision; reviewer edit rate on live letters | ≥95%; edits below 30% by week 12 | Persistent invented clauses |
| Does it recover money? | Full or partial reversal at insurer stage within 30 days, across ≥50 filed cases | ≥25% | <15% |
| Will users pay? | Share accepting fee terms; share of owed fees collected | ≥30% accept; ≥70% collected | <20% accept |
| Can it scale economically? | CAC per paid case vs expected fee; reviewer minutes per case | CAC below 30% of expected fee; review time below 20 minutes | CAC above expected fee in every channel |

**Pivot paths**

- Correctness and recovery pass but consumer acquisition fails: sell the engine B2B2C (RIAs, MFDs, brokers, HR teams) as white-label claim support.
- Fee collection fails: flat per-filing fee.
- Recovery fails: stop; redeploy the engine to the family money finder or tax-notice resolver (about 70% stack reuse, Inference).

## 12 Risks and mitigations

| Risk | Likelihood / impact (Assumption) | Mitigation |
|---|---|---|
| Insurer pushback against templated complaints (the US CFPB already flags AI-generated "duplicative and spurious" complaints, [Orrick](https://infobytes.orrick.com/2026-04-10/cfpb-reports-complaint-volume-doubled-in-2025-citing-surge-in-credit-reporting-disputes/)) | Medium / High | Evidence-backed letter per case; human review; no mass filing |
| Legal-practice or representation challenge | Medium / High | Legal opinion first; user signs and submits; drafting-software positioning |
| Hallucinated clause or amount | Medium / High | Numbers only from tools; mandatory citations; golden-set gating on every release |
| Episodic demand and high CAC | High / High | Intent search, B2B2C and employer channels; widen to life mis-selling and unclaimed money |
| Fee non-payment after recovery | Medium / High | E-mandate at onboarding; upfront fee; flat-fee fallback |
| Health-data breach | Low / Very high | Minimisation, encryption, access control, deletion, breach plan |
| Regulatory change (e.g. insurer internal ombudsman) | Medium / Medium | Support each new forum as a route |
| Weak or conflicting source data | High / Medium | Verify against primary IRDAI and Ombudsman reports in weeks 0-2 |

## 13 Open questions and decisions needed

1. **Legal:** may a non-lawyer assist before the Ombudsman, under what disclosure, and which counsel?
2. **Pricing:** ₹299 vs ₹499 upfront; 10% vs 15% success fee; treatment of small recoveries.
3. **Fee collection:** e-mandate at onboarding vs payment link after settlement.
4. **Data:** model vendor and region; zero-retention terms; whether redaction hurts accuracy.
5. **Corpus:** which 8-10 products first; how to obtain historical wording versions; who maintains the rules library.
6. **Verification:** reconcile FY25 Ombudsman totals; obtain health-only Bima Bharosa data; confirm award caps.
7. **Reviewer supply:** can a part-time ex-TPA specialist be hired, and at what cost?
8. **Channel bet and funding:** search, partners or HR teams first; bootstrap or raise.

## 14 Expansion path

| Horizon | Move | Notes |
|---|---|---|
| Months 4-9 | Life-insurance mis-selling audits; family money finder | 26,667 unfair-practice complaints in FY25; about ₹2.2 lakh cr unclaimed ([Business Today](https://www.businesstoday.in/amp/personal-finance/news/story/rs-22-lakh-crore-unclaimed-funds-lie-idle-across-banks-epf-insurance-stocks-mfs-524958-2026-04-10)) |
| Months 6-12 | **US health-denial appeals** on the same engine | See below |
| Adjacent (Inference) | Pre-admission cost simulator and policy X-ray; EPF claim fixer (about 174 of 796 lakh claims rejected in FY25, [Business Today](https://www.businesstoday.in/personal-finance/news/story/epfos-instant-pf-withdrawal-promise-has-a-catch-one-in-five-claims-still-gets-rejected-541466-2026-07-07)) | Policy X-ray is likely a feature, not a business |
| After product-market fit | Corporate RIA and mutual-fund portfolio fixer as upsell | Earned distribution, not a cold start |

**US context.** KFF found 20% of in-network ACA marketplace claims denied in 2023 (86M of 436M), under 1% appealed internally, and about 44% of appealed denials not upheld ([KFF](https://www.kff.org/private-insurance/claims-denials-and-appeals-in-aca-marketplace-plans-in-2023/); 2024 figures not retrieved). In Medicare Advantage prior authorisation, 81.7% of appealed denials were partly or fully overturned, yet only 11.7% were appealed ([KFF via LeadingAge](https://leadingage.org/new-kff-report-more-ma-prior-authorizations-appeals-remain-successful/)). CMS-0057-F tightens prior-authorisation timelines from 2026, with APIs due January 2027.

**US constraints:** competitors are free or cheap (Counterforce free; Claimable $50 per letter), so a paid product must deliver the full outcome, not a letter. Use user-in-the-loop filing with the plan's authorised-representative form and HIPAA authorisation. Unauthorised-practice-of-law risk is unsettled ([Nippon Life v. OpenAI](https://techstrong.ai/features/nippon-life-sues-openai-alleging-chatgpt-engaged-in-unauthorized-practice-of-law/), no ruling found). India-based review of US data adds HIPAA business-associate friction. Administrative denials (about a fifth of in-network denials) are the safest wedge. Reported AI-appeal success rates are company-reported.

## 15 Sources

- Research report *India AI personal finance MVP* (sections 7-10) and notes `unsolved_insurance_health.md`, `household_finance_gaps.md`, `tech_feasibility.md`, `regulation_and_rails.md`, `global_regulation.md`, `global_underserved_segments.md`
- India claims data: [Moneylife, ₹26,037 cr FY24](https://moneylife.in/article/health-insurance-claims-worth-rs2603765-crore-rejected-by-insurers-in-fy2324-govt/76282.html); [Algates, IRDAI Annual Report 2024-25](https://algatesinsurance.in/irdai-annual-report-2024-25-highlights/); [Insurance Business Asia](https://www.insurancebusinessmag.com/asia/news/life-insurance/irdai-cannot-explain-why-health-insurance-claims-go-unpaid-583814.aspx); [Outlook Money, 95% rejections](https://www.outlookmoney.com/amp/story/personal-finance/why-95-per-cent-of-health-insurance-complaints-concern-claim-rejections); [Cafemutual, FY25 outcomes](https://cafemutual.com/news/industry/36635-41-of-health-insurance-complaints-were-resolved-in-favour-of-policyholders-in-fy25); [TaxGuru, Bima Bharosa](https://taxguru.in/?p=1035064); [Lok Sabha answer](https://eparlib.sansad.in/bitstream/123456789/3015516/1/AS20_AaaDVE.pdf); [Moneylife, master circular](https://moneylife.in/article/health-insurance-decide-cashless-request-in-1-hour-provide-final-authorisation-for-discharge-within-3-hours-says-irdai/74269.html); [Business Today, LocalCircles](https://www.businesstoday.in/amp/personal-finance/insurance/story/insurance-claims-over-50-health-cover-claims-faced-rejection-or-partial-approval-says-survey-459394-2025-01-02); [Money9](https://www.money9.com/news/exclusive/understanding-cashless-health-insurance-challenges-and-solutions-139314.html); [Outlook Money, escalation ladder](https://www.outlookmoney.com/insurance/mis-selling-complaints-grew-112-since-2024-value-of-disputed-claims-rose-10-report)
- Competitors: [Entrackr](https://entrackr.com/snippets/insurance-samadhan-secures-rs-85-cr-to-boost-tech-infrastructure-9040178); [Inc42, Insurance Samadhan](https://inc42.com/company/insurance-samadhan/financials/); [Inc42, Ditto](https://inc42.com/company/ditto-insurance/); [PYMNTS, Claimable](https://www.pymnts.com/artificial-intelligence-2/2026/insurance-denials-meet-their-match-in-ai-powered-appeals/); [Axios, Counterforce](https://www.axios.com/local/raleigh/2025/08/20/using-ai-to-fight-back-against-insurance-denials-counteforce)
- Regulation and tech: [Outlook Money, Acko fine](https://www.outlookmoney.com/insurance/acko-gets-rs-1-crore-irdai-fine-what-it-says-about-how-your-insurance-is-sold); [Deccan Herald, DPDP phasing](https://www.deccanherald.com/india/centre-notifies-dpdp-rules-implementation-planned-in-phases-spread-over-12-18-months-3798465); [Uniqus, DPDP penalties](https://uniqus.com/digital-personal-data-protection-act-timelines/); [Cyril Amarchand blog](https://corporate.cyrilamarchandblogs.com/2026/01/insurance-distribution-in-india-emerging-channels-compliance-and-data-governance/); [arXiv 2601.07054](https://arxiv.org/html/2601.07054v1); [braindetox, API pricing](https://braindetox.kr/en/posts/ai_api_pricing_comparison_2026.html); [Sarvam pricing](https://docs.sarvam.ai/api-reference-docs/getting-started/pricing); [Orrick, CFPB](https://infobytes.orrick.com/2026-04-10/cfpb-reports-complaint-volume-doubled-in-2025-citing-surge-in-credit-reporting-disputes/)
- Expansion: [Business Today, unclaimed funds](https://www.businesstoday.in/amp/personal-finance/news/story/rs-22-lakh-crore-unclaimed-funds-lie-idle-across-banks-epf-insurance-stocks-mfs-524958-2026-04-10); [Business Today, EPF](https://www.businesstoday.in/personal-finance/news/story/epfos-instant-pf-withdrawal-promise-has-a-catch-one-in-five-claims-still-gets-rejected-541466-2026-07-07); [KFF](https://www.kff.org/private-insurance/claims-denials-and-appeals-in-aca-marketplace-plans-in-2023/); [LeadingAge on KFF](https://leadingage.org/new-kff-report-more-ma-prior-authorizations-appeals-remain-successful/); [Techstrong, Nippon Life v. OpenAI](https://techstrong.ai/features/nippon-life-sues-openai-alleging-chatgpt-engaged-in-unauthorized-practice-of-law/)

*Caveat: most figures come from secondary coverage and search summaries; company-reported numbers are unverified. Regulatory conclusions are not legal advice.*
