# Unsolved Problems in Insurance and Healthcare Finance That AI Agents Can Now Address (Global; as of Oct 2026)

Method note: Facts below come from web search summaries and one direct fetch of KFF. Most figures were not verified against primary PDFs, and I flag where. Product concepts, feasibility and regulatory-path views are labelled as Inferences (my reasoning, not sourced). Sources that conflict are marked.

## 1. US claim denials and appeals (ACA marketplace, Medicare Advantage, employer plans)

### Takeaway
Roughly one in five in-network ACA marketplace claims is denied, yet under 1% of denials are appealed. Where appeals do happen, a large share succeed (very high in Medicare Advantage). The gap between how often denials are wrong and how rarely people contest them is the core unsolved problem, and AI letter-drafting now targets it.

### Cited Findings
- KFF, HealthCare.gov non-group QHPs, 2023: 20% of in-network claims denied (86M of 436M) and 36% of out-of-network claims. In-network denial rates by insurer ranged from 1% to 54%; 24 of 175 insurers denied 30% or more. — [KFF fetch of brief](https://www.kff.org/private-insurance/claims-denials-and-appeals-in-aca-marketplace-plans-in-2023/) (a search summary of the same brief rounds this to "19%"; minor rounding difference)
- Denial reasons (in-network): "Other" 34%, administrative 21%, excluded service 14%, no prior auth/referral 9%, medical necessity about 6%. — [KFF](https://www.kff.org/private-insurance/claims-denials-and-appeals-in-aca-marketplace-plans-in-2023/)
- 376,508 denied in-network claims were appealed internally (under 1%). Insurers upheld 211,383 (56%), so about 44% were not upheld (a secondary summary says 44% overturned; the KFF page fetched does not state an overturn rate explicitly). At least 5,000 external appeals were filed. — [KFF](https://www.kff.org/private-insurance/claims-denials-and-appeals-in-aca-marketplace-plans-in-2023/); [HFMA via search summary](https://www.hfma.org/fast-finance/aca-marketplace-plans-payment-denial/)
- KFF updated the brief on March 24, 2026 for corrected CMS data, and a 2024-data analysis exists. I did not retrieve the 2024 numbers. — [KFF](https://www.kff.org/private-insurance/claims-denials-and-appeals-in-aca-marketplace-plans-in-2023/)
- KFF 2023 consumer survey: 58% of insured adults reported a problem using insurance; among those with trouble paying medical bills, 39% said denied claims contributed. — [KFF (via search summary)](https://www.kff.org/private-insurance/issue-brief/claims-denials-and-appeals-in-aca-marketplace-plans-in-2023/)
- Medicare Advantage prior authorization (PA), 2023: about 6.4% of PA decisions unfavorable; only 11.7% of denials appealed; 81.7% of appeals partially or fully overturned (vs 29% in traditional Medicare in 2022). A different KFF analysis of insurer transparency data reported 67% overturned in MA, 47% Medicaid managed care, 43% ACA federal marketplace (year not confirmed; different data, not directly comparable). — [KFF via LeadingAge/TechTarget summaries](https://leadingage.org/new-kff-report-more-ma-prior-authorizations-appeals-remain-successful/)
- AMA physician survey (1,000 physicians, Dec 2025, released May 13, 2026): 94% say PA hurts clinical outcomes; only 33% believe the June 2025 insurer pledge (about 60 insurers) will matter; only 24% say medical-necessity denials are consistently reviewed by qualified clinicians. — [AMA](https://www.ama-assn.org/press-center/ama-press-releases/ama-survey-prior-authorization-reform-pledge-falls-short-physicians); [Medical Economics, May 13, 2026](https://www.medicaleconomics.com/view/prior-auth-reform-physicians-bemoan-lot-of-promises-but-little-progress)
- What changed (regulation): CMS-0057-F requires affected payers (MA, Medicaid/CHIP, QHP issuers on federal exchanges) to decide urgent PAs in 72 hours and standard in 7 days and give specific denial reasons from 2026; four FHIR APIs (including Prior Authorization API) due January 1, 2027. Traditional Medicare and most commercial group plans are not covered. Source is mostly vendor summaries plus a CMS fact sheet; verify dates. — [CMS fact sheet](https://www.cms.gov/files/document/fact-sheet-cms-interoperability-and-prior-authorization-final-rule-cms-0057-f.pdf); [Innovaccer summary](https://innovaccer.com/resources/blogs/cms-0057-prior-authorization-rule-requirements-deadlines-apis-and-operational-impact)
- Existing attempts: Counterforce Health (free; letters built from the patient's policy and a record of successful appeals; funded by grants, with sources conflicting on size: $280,000 per CBS17 vs $10,000 per Caplight) — [Axios Raleigh](https://www.axios.com/local/raleigh/2025/08/20/using-ai-to-fight-back-against-insurance-denials-counteforce), [CBS17](https://www.cbs17.com/news/local-news/wake-county-news/raleigh-organization-helps-thousands-of-americans-appeal-health-insurance-denials-using-ai/amp/). Claimable ($50 per letter; claims 75% success, self-reported; seed led by Walkabout Ventures, amount undisclosed) — [PYMNTS](https://www.pymnts.com/artificial-intelligence-2/2026/insurance-denials-meet-their-match-in-ai-powered-appeals/), [CO/AI](https://getcoai.com/news/ai-startup-helps-patients-overturn-insurance-denials/). Sheer Health (claims/advocacy; CEO said $5M returned to members as of Oct 2024) — [Gerald guide](https://joingerald.com/learn/financial-wellness/sheer-health-guide). Aegis (YC X25, self-reports 78% overturn on appealed denials) — [PitchBook](https://pitchbook.com/profiles/company/820625-32).
- Legal path: patients can appoint an authorized representative (often a signed insurer form) to file internal appeals; DOL FAQ says an assignment of benefits typically does not confer appeal authority. — [Illinois DOI form](https://idoi.illinois.gov/content/dam/soi/en/web/insurance/consumers/documents/appointment-authorized-rep.pdf), [Thomson Reuters](https://tax.thomsonreuters.com/blog/court-allows-medical-provider-to-appeal-claim-denial-on-behalf-of-plan-participant/)
- Unauthorized practice of law (UPL) risk is unsettled: Nippon Life v. OpenAI (N.D. Ill., filed March 2026, No. 1:26-cv-02448) alleges ChatGPT practiced law without a licence in a disability-claim dispute; OpenAI moved to dismiss May 15, 2026 calling ChatGPT a tool; no ruling found. I found no ruling that an appeal-letter generator is UPL, and no source on whether UPL rules reach internal insurance appeals. — [Techstrong](https://techstrong.ai/features/nippon-life-sues-openai-alleging-chatgpt-engaged-in-unauthorized-practice-of-law/), [Bloomberg Law](https://news.bloomberglaw.com/ip-law/open-ai-dismissal-motion-says-chatgpt-is-mere-tool-not-attorney)

### Inferences
- Why unsolved: the insurer bears no cost when a denial is not contested and bears small cost when overturned; the consumer faces a time and knowledge cost with an uncertain payoff; providers often write off rather than appeal. Denial volume (hundreds of millions of claims) is far too large for human advocates at $50+ per case.
- Concept: an agent that ingests the denial letter/EOB plus the plan document (SBC/EOC), classifies denial type (administrative vs medical necessity vs excluded), checks for resubmittable coding errors first, drafts the appeal citing plan language and clinical guidelines, tracks deadlines, and escalates to external review. Administrative denials (about a fifth of the total, plus much of "Other") are the highest-yield and lowest-clinical-risk wedge.
- Feasibility for a small team: high for a letter generator (LLM plus plan-document retrieval). Hard parts are clinical-evidence retrieval and payer-specific appeal rules; neither needs an on-premise ML team. Pricing is likely pay-on-success or low flat fee; free incumbents (Counterforce) compress price.
- Regulatory path (US): safest is user-in-the-loop (user signs and files the letter, tool is documentation software with disclaimers). Filing as the patient's representative needs the plan's signed authorization form and likely HIPAA authorization. Avoid giving individualized legal strategy. Check each state's UPL stance and watch the Nippon ruling.

### Gaps
- KFF 2024 denial/appeal figures not retrieved. Independent evidence on AI-letter win rates is absent (all rates are company-reported). No ruling found on UPL for appeal letters.

## 2. Medical billing errors, surprise bills, medical debt, price opacity (US)

### Takeaway
The US has the rules (No Surprises Act, price transparency) but enforcement and usability lag: hospital compliance is incomplete, the NSA dispute system is flooded with volume far above projections, and the patient-side bill-checking problem is still mostly unserved. Reliable billing-error rates are old and disputed.

### Cited Findings
- NSA arbitration (IDR) volume: 1.2M disputes filed in H1 2025 vs about 590,000 in H1 2024; nearly 1.4M in H2 2025; 4.8M total cases through end-2025; officials originally expected about 17,000-18,000 per year; providers won 88% in H1 2025; top three initiators filed about 44% of disputes; fees in H1 2025 about $844M-$900M (sources differ). — [Georgetown CHIR](https://chir.georgetown.edu/the-no-surprises-act-idr-process-an-early-look-at-2025-data/), [Health Affairs Forefront](https://www.healthaffairs.org/content/forefront/no-surprises-act-idr-process-early-look-2025-data), [Healthcare Dive](https://www.healthcaredive.com/news/no-surprises-disputes-idr-2025-cms/810525/)
- Billing error rates are old and inconsistent: AMA 7.1% of paid claims (2013); NerdWallet 49% of Medicare claims (2014); advocates 75-80%; workers' comp audit 35%. No CMS-published current rate found. — [Etactics compilation](https://etactics.com/blog/medical-billing-error-statistics), [KFF Health News morning briefing](https://kffhealthnews.org/morning-breakout/studies-find-high-rates-of-errors-in-medical-billing/) (low-quality aggregators; treat as indicative only)
- Medical debt: at least $220B owed at end of 2021 (conservative method); about 14M adults (6%) owe over $1,000 and about 3M (1%) over $10,000. — [KFF](https://www.kff.org/health-costs/report/the-burden-of-medical-debt-in-the-united-states/)
- Hospital price transparency: Patient Rights Advocate reports conflicted: 21.1% fully compliant in one report vs 34.5% (Feb 2024) vs about 49% in the latest scorecard, which Healthcare Dive calls the highest since 2021; CMS had fined 28 hospitals and warned 500+; many compliant hospitals post vague algorithms rather than dollar prices. Dates for the reports were not confirmed. — [PRA](https://www.patientrightsadvocate.org/blog/new-report-just-21-of-us-hospitals-complying-with-federal-price-transparency-rule), [Healthcare Dive](https://www.healthcaredive.com/news/hospital-compliance-price-transparency-regulations-pra-report/830087/)

### Inferences
- Why unsolved: the bill-reviewing party (patient) lacks the chart, CPT/ICD literacy and negotiating leverage; hospital financial assistance and charity-care rules are fragmented; there is no revenue pool for a consumer-side auditor except contingency fees.
- Concept: an agent that reads the itemized bill, the EOB and the machine-readable price files, flags duplicates/unbundling/NSA violations (out-of-network surprise billing at in-network facilities), and drafts disputes plus financial-assistance applications. Contingency-fee model fits.
- Feasibility: medium. Data (price files) is public but messy; requires coding knowledge and bill/EOB OCR. Regulatory: collecting on contingency may implicate state billing-advocate or debt-adjustment licensing rules (not researched). Needs HIPAA business-associate arrangements if acting for providers; as a consumer app, user-authorized.

### Gaps
- No current authoritative billing-error rate. Did not retrieve exact PRA report dates. State licensing rules for medical billing advocates not researched.

## 3. India: health claim rejection, partial settlements, grievance resolution

### Takeaway
India's regulator reports about 8% of health claims repudiated in FY25 and a large rise in complaints, while survey data suggest far more policyholders experience partial payment or rejection than headline settlement ratios suggest. The 2024 cashless timelines help the cashless leg only; post-claim disputes and deductions remain a complaint-driven, slow process.

### Cited Findings
- IRDAI Annual Report FY2024-25: 3.26 crore health claims processed; 87% settled, 8% repudiated, about 5% pending; payouts Rs 94,248 crore vs Rs 83,493 crore prior year. FY2023-24: 11% rejected, 6% pending; repudiated value Rs 26,000 crore (up 19.10%). — [Insurance Business Asia](https://www.insurancebusinessmag.com/asia/news/life-insurance/irdai-cannot-explain-why-health-insurance-claims-go-unpaid-583814.aspx), [Business Standard](https://www.business-standard.com/amp/finance/personal-finance/health-insurance-claims-rejection-up-19-10-in-fy24-irdai-report-124122700754_1.html), [Algates summary](https://algatesinsurance.in/irdai-annual-report-2024-25-highlights/)
- The regulator publishes industry-level repudiation percentages but not insurer-level reasons. — [Insurance Business Asia](https://www.insurancebusinessmag.com/asia/news/life-insurance/irdai-cannot-explain-why-health-insurance-claims-go-unpaid-583814.aspx)
- Bima Bharosa grievance counts (not split by health): 47,658 (FY24), 64,365 (FY25), 73,729 up to Feb FY26; FY25 total 2,57,790 grievances, of which 1,37,361 general and health. Health insurers received 1,17,979 complaints in FY26 per a Lok Sabha reply. — [Lok Sabha answer (eparlib)](https://eparlib.sansad.in/bitstream/123456789/3015516/1/AS20_AaaDVE.pdf), [Outlook Money](https://www.outlookmoney.com/amp/story/personal-finance/insurance-claims-mis-selling-account-for-most-insurance-complaints-in-fy25-reveals-irdai-annual-report), [Cafemutual](https://cafemutual.com/news/insurance/38460-insurance-industry-disposed-off-287-lakh-complaints-in-fy26-through-bima-bharosa) (the FY26 figure sits in a search summary; the second Lok Sabha-derived complaint counts conflict across summaries)
- Insurance Ombudsman (CIO): FY24 health complaints 31,490 vs 25,873; 95% concerned claim rejections (CIO 2023-24); FY24 54% of ombudsman complaints were health. FY25 insurer-level counts: Star Health 12,186, Care 4,423, Niva Bupa 3,983, Aditya Birla 2,354. Total ombudsman complaints FY25 reported as 53,102 (Lok Sabha) vs 37,431 (other summary): conflict, scope unclear. FY25 outcomes (health): 6,126 in favour of policyholders; withdrawn complaints rose from 2,087 to 3,649. — [Outlook Money, FY24](https://www.outlookmoney.com/amp/story/personal-finance/why-95-per-cent-of-health-insurance-complaints-concern-claim-rejections), [Cafemutual FY25](https://cafemutual.com/news/industry/36635-41-of-health-insurance-complaints-were-resolved-in-favour-of-policyholders-in-fy25)
- Bima Bharosa is not integrated with the Ombudsman system; the policyholder must file separately; IRDAI proposed an Internal Insurance Ombudsman (status unconfirmed). — [Lok Sabha answer](https://eparlib.sansad.in/bitstream/123456789/3015516/1/AS20_AaaDVE.pdf) via search summary
- LocalCircles survey (reported Jan 2025): over 50% of claimants in prior three years faced rejection or partial approval; only 25% fully approved; 33% partially approved "with invalid reasons" and 36% rejected "with invalid reasons" (percentages do not reconcile with "over 50%"; survey base unclear). — [Business Today](https://www.businesstoday.in/amp/personal-finance/insurance/story/insurance-claims-over-50-health-cover-claims-faced-rejection-or-partial-approval-says-survey-459394-2025-01-02)
- Regulation (what changed): IRDAI master circular (effective August 1, 2024): decide cashless request in 1 hour, final discharge authorisation within 3 hours; delay beyond 3 hours means extra hospital charges borne from insurer shareholder funds; repudiation requires Claims Review Committee approval. — [The Week](https://www.theweek.in/news/india/2024/05/30/irdai-issues-new-master-circular-to-make-health-insurance-claims-process-more-seamless.amp.html), [Moneylife](https://moneylife.in/article/health-insurance-decide-cashless-request-in-1-hour-provide-final-authorisation-for-discharge-within-3-hours-says-irdai/74269.html). A December 2025 Lok Sabha question asked about breaches; figures not retrieved.
- Plumbing: Bima Sugam portal live September 2025 but core platform repeatedly delayed; IRDAI chair said on September 27, 2026 launch likely by November 2026. NHCX (claims exchange under ABDM) adoption is uneven and voluntary per vendor commentary. — [IPO Market, Sept 2026](https://www.ipomarket.in/news/bima-sugam-upi-moment-insurance-irdai-not-ipo), [Nirmitee](https://nirmitee.io/blog/is-nhcx-mandatory-hospitals-hmis-2026/) (weak sources)
- Existing attempts: Insurance Samadhan (grievance platform; raised Rs 8.5 crore in 2025; claims 18,000+ complaints resolved and Rs 160 crore recovered, self-reported; AI claim weakly supported) — [Entrackr](https://entrackr.com/snippets/insurance-samadhan-secures-rs-85-cr-to-boost-tech-infrastructure-9040178). Beshak and Ditto: no data found.

### Inferences
- Why unsolved: insurers are rewarded for claims ratio and partial settlement is not reported as rejection; hospitals and insurers disagree on "reasonable and customary" rates; consumers do not know about the escalation ladder (insurer grievance officer, Bima Bharosa, Ombudsman within one year, consumer court).
- Concept: a WhatsApp/voice agent that takes a rejection letter or discharge summary, maps the stated ground to the policy wording and IRDAI circular (e.g., 2024 master circular, moratorium period of five years under the 2024 health regulations, not researched here), drafts the grievance, files on Bima Bharosa, and then prepares the Ombudsman complaint with the 30-day timeline. India's vernacular and voice-first setting favours an agent.
- Feasibility: high for drafting and tracking; filing requires the user's own login/OTP on the portals, so the product should be a guided co-pilot. Regulatory path: Insurance Ombudsman rules allow complaints by the complainant or authorized representative (not verified here); non-lawyer assistance at Ombudsman is common but check rules. Insurance Samadhan's business shows a fee-on-recovery model exists.

### Gaps
- No health-only FY25 Bima Bharosa split; no insurer-level repudiation reasons; no FY25 CIO total reconciled; Lok Sabha breach figures for the 1-hr/3-hr rule not retrieved. Ditto/Beshak not found. Regulatory detail for Ombudsman representation not verified.

## 4. India: out-of-pocket spending, hospital billing opacity, cashless friction

### Takeaway
Out-of-pocket expenditure (OOPE) share has fallen to 39.4% but remains very high, hospital prices are unregulated and opaque, and the Supreme Court rate-standardisation case is still unresolved. Cashless and price opacity combine to produce partial approvals and surprise co-pays.

### Cited Findings
- OOPE was 39.4% of total health expenditure in 2021-22 (down from 64.2% in 2013-14 per most reports; PIB gives 62.6% for 2014-15). Total health expenditure Rs 9,04,461 crore (3.83% of GDP); government share 48%. — [NITI Aayog via IANS](https://ianslive.in/out-of-pocket-health-expenditure-declined-to-394pc-in-2021-22-niti-aayog--20240926101032), [PIB](https://static.pib.gov.in/WriteReadData/specificdocs/documents/2024/oct/doc2024104408201.pdf)
- Supreme Court (Feb 2024) PIL: cataract surgery costs about Rs 10,000 in government sector vs Rs 30,000-1,40,000 in private hospitals; threatened to enforce CGHS rates as interim measure. As of an August 2026 Centre affidavit, most states have still not determined rate ranges under Rule 9(ii) of the Clinical Establishments Rules; Act adopted by only 12 states and 7 UTs (2024); no final judgment found. — [LiveLaw](https://www.livelaw.in/top-stories/centre-defends-clinical-establishment-rule-in-supreme-court-says-it-curbs-excessive-pricing-of-medical-services-545337), [Business Today](https://www.businesstoday.in/amp/personal-finance/news/story/standardise-hospital-treatment-charges-or-cghs-rates-will-be-enforced-supreme-court-tells-centre-419298-2024-02-28)
- Partial approvals often arise from co-pay, room-rent caps (with proportionate deductions), sub-limits and non-payable consumables. — [Money9](https://www.money9.com/news/exclusive/understanding-cashless-health-insurance-challenges-and-solutions-139314.html), [Business Standard](https://www.business-standard.com/amp/finance/personal-finance/partial-hospital-bill-payout-boost-policy-cover-to-secure-full-claims-125111401478_1.html)
- IMA and hospital bodies cautioned against "Cashless Everywhere" in its current form. — [Business Today / search summary](https://www.businesstoday.in/amp/personal-finance/news/story/standardise-hospital-treatment-charges-or-cghs-rates-will-be-enforced-supreme-court-tells-centre-419298-2024-02-28) (low authority)

### Inferences
- Why unsolved: hospitals have no incentive to publish prices; insurers fight rate inflation by deductions, which pushes cost to patients; neither wants a transparent price list.
- Concept: a pre-admission agent. Upload policy plus hospital estimate; it computes expected net payable under room-rent cap/proportionate deduction/co-pay, suggests cheaper in-network alternatives, and generates a post-discharge bill audit comparing line items to policy terms. The same engine can generate an informed "pre-authorisation request" language.
- Feasibility: medium. Hospital price data are not public in India, so the agent depends on user-supplied estimates and crowdsourced price data. Regulatory: no licence apparent for information service; if it earns commissions from insurers it could fall under IRDAI intermediary rules (web aggregator/corporate agent licence), so avoid commissions.

### Gaps
- No Indian hospital bill error-rate data. No source found for the share of OOP spend that is inpatient vs outpatient/pharmacy.

## 5. Protection gap, under-insurance, mis-selling and lapse

### Takeaway
Protection gaps are large and growing in dollar terms, concentrated in emerging markets. In India, complaints about mis-selling in life insurance are rising and persistency (renewal) is below the regulator's targets. Estimates differ widely between studies and years, so use ranges and cite scope.

### Cited Findings
- Swiss Re Institute: global mortality protection gap record $432B (2024; $423B in 2023; $321B in 2014); emerging markets $271B (63%); US gap about $83B; Mortality Resilience Index 44.4%. — [Insurance Business](https://www.insurancebusinessmag.com/reinsurance/news/breaking-news/global-mortality-protection-gap-hits-432-billion--swiss-re-572131.aspx)
- Swiss Re sigma: health protection gap $889B globally in 2022 (premium equivalent); combined nat cat/crop/mortality/health gap $1.8T (2022). — [Insurance Business Asia / Swiss Re summary](https://www.insurancebusinessmag.com/us/news/breaking-news/global-protection-gaps-widening--swiss-re-450165.aspx), [Swiss Re](https://www.swissre.com/reinsurance/insights/asia-protection-gap-consumer-survey.html) (summaries)
- Asia health protection gap: $258B across 12 Asian markets in 2024 (+21% from 2017), likely underestimated since it excludes those unable to access/afford care; an older, undated study gave $1.8T for Asia, with India at $369B (the two are not reconcilable from the sources found). — [Swiss Re Asia survey](https://www.swissre.com/reinsurance/insights/asia-protection-gap-consumer-survey.html), [Swiss Re study](https://www.swissre.com/institute/research/topics-and-risk-dialogues/economy-and-insurance-outlook/Closing-Asia-s-USD-1.8-trillion-health-protection-gap.html)
- India (National Insurance Academy, Dec 2023): health protection gap 73% (over 40 crore without health insurance); life protection gap 87%. — [Business Standard](https://www.business-standard.com/amp/finance/personal-finance/health-protection-gap-persists-in-india-40-crore-uninsured-report-123121400799_1.html)
- Mis-selling: unfair business practice grievances (includes mis-selling) 26,667 in FY25 vs 23,335 FY24; 22.14% of life-insurer complaints (up from 19.33%). Life complaints 15.72 per lakh policies. — [Outlook Money](https://www.outlookmoney.com/insurance/insurance-claims-mis-selling-account-for-most-insurance-complaints-in-fy25-reveals-irdai-annual-report), [Insurance Business Asia](https://www.insurancebusinessmag.com/asia/news/breaking-news/irdai-sees-misselling-complaints-rise-amid-stable-grievances-561149.aspx)
- Persistency: IRDAI chair target (2020): 13th month at least 90%, 61st month at least 65%. FY25 13th-month by premium: Tata AIA 88.05%, HDFC Life 86.9%, ABSL 85.76%; by policy count LIC 64.12%, Axis Max 83%, Tata AIA 82.97%, HDFC Life 81.2%, ICICI Pru 80%, Kotak 79.08%. An unverified glossary claims 65-70% private-insurer industry figure for FY24; low confidence. Industry-wide 13th-month number from IRDAI not found. — [Cafemutual](https://cafemutual.com/news/insurance/37974-which-life-insurers-retain-customers-the-best), [Business Standard on Q1 FY26 persistency](https://www.business-standard.com/amp/finance/insurance/13th-month-persistency-rate-of-life-insurance-companies-sees-a-fall-in-q1-125080300414_1.html)

### Inferences
- Why unsolved: advice is paid by commission, so the advisor's incentive favours high-commission endowment/ULIP over term; self-directed buyers cannot assess adequacy; lapse is driven by affordability shocks and low engagement after sale.
- Concept: a fee-free "coverage audit" agent. User uploads existing policies (or consents to pull via account aggregator/Bima Sugam when live); the agent computes needs-based cover (income replacement, debts), flags endowment/ULIP with low IRR, lists lapse dates and revival options, and nudges before premium due dates. Monetization risk: referral commissions would trigger IRDAI licensing (web aggregator or corporate agent) and recreate the conflict.
- Feasibility: high for analysis; the data-access friction (no single policy view) is the barrier until Bima Sugam launches (target November 2026, history of slips). Regulatory: pure education/analysis is unlicensed; IRDAI Insurance Advertisements and Disclosures rules on "advice" not checked. In the US/UK, "personalised recommendation" can be regulated advice (FCA/SEC), not researched.

### Gaps
- No current India-specific Swiss Re gap figure (only 2014-16 and the NIA 2023 study). No IRDAI-level industry persistency number. UK/EU protection gap data not retrieved.

## 6. Policy comprehension and comparison (exclusions, room-rent caps, waiting periods)

### Takeaway
Few direct quantitative sources were found on comprehension itself; the strongest evidence is indirect (rejections and partial payments driven by policy terms, mis-selling complaints, KFF's "excluded service" category). LLMs reading long policy wordings is the clearest new capability.

### Cited Findings
- Excluded services made up 14% and "other" 34% of ACA in-network denials. — [KFF](https://www.kff.org/private-insurance/claims-denials-and-appeals-in-aca-marketplace-plans-in-2023/)
- Typical Indian partial-payment causes: co-pay, room-rent cap with proportionate deductions, sub-limits, consumables. — [Money9](https://www.money9.com/news/exclusive/understanding-cashless-health-insurance-challenges-and-solutions-139314.html)
- Insurance Samadhan is raising on a "Know Your Policy" feature to counter mis-selling and rejection. — [Entrackr](https://entrackr.com/snippets/insurance-samadhan-secures-rs-85-cr-to-boost-tech-infrastructure-9040178)
- US employee benefits: HSA Bank index of 2,000 employees found only 10% funded or invested an HSA; a Guardian study found many employees overestimate their benefits understanding; InComm says half of HSA users skip reimbursements, missing about $2,500 a year (all vendor surveys). — [HSA Bank](https://www.hsabank.com/Employers/Health-Wealth-Index/2025-HSA-Bank-Health-and-Wealth-Index.html), [PlanAdviser](https://www.planadviser.com/hsa-limits-rise-but-frustrated-users-leave-money-behind/)

### Inferences
- Concept: "policy X-ray" agent that reads a policy PDF and produces a plain-language summary with a per-treatment simulation ("if I have a knee replacement in a metro hospital, what do I pay?"), plus side-by-side comparison across insurers. A comparison layer with real quotes needs licensing, so keep it to analysis of owned policies at first.
- Feasibility: high technically (long-context LLMs on policy PDFs), but hallucination risk is material and must be validated against clause citations. This is likely a feature of the claim, appeal and audit products above rather than a standalone business (low willingness to pay before a claim).

### Gaps
- No rigorous comprehension-survey data (e.g., share of policyholders who know their room-rent cap) was found.

## 7. Parametric insurance for climate risk (crop, heat) in emerging markets

### Takeaway
Parametric cover is spreading and paying out (East Africa drought), but heat-specific crop products in India and Kenya are mostly pilots or NGO/CSR-funded, and basis risk remains the main hurdle. Claims that AI cuts basis risk are mostly vendor assertions.

### Cited Findings
- East Africa drought triggered parametric payouts worth about $9M to farmers (March 2026); more than 70,000 farmers across the Horn of Africa paid, per reinsurer Zep-Re; drought, not heat. — [The Insurer, March 2026](https://www.theinsurer.com/parametric-insurer/news/east-africa-drought-triggers-parametric-payouts-to-farmers-worth-9-million-2026-03-11/)
- Kenya Livestock Insurance Program paid KSh 1.2B in 2015-2021 while collecting KSh 1.1B in premiums, then was replaced (older data). — [Business Daily Africa](https://www.businessdailyafrica.com/bd/opinion-analysis/letters/why-africa-s-insurers-must-rethink-parametric-products-5347144)
- India: most crop insurance products revolve around rainfall deficits, floods, cyclones or total loss; heat damage is a coverage gap (Business Standard, May 2026). PMFBY uses area-level yield assessment; the weather-based scheme uses predefined triggers. Parametric insurance is largely NGO/CSR driven; IBISA has a heat-stress dairy cover; HDFC ERGO and Manchester are designing temperature/rain products for Punjab and Haryana. — [Business Standard](https://www.business-standard.com/industry/agriculture/how-extreme-heat-is-exposing-gaps-in-india-s-crop-insurance-system-126052701040_1.html), [Manchester project](https://research.manchester.ac.uk/en/projects/mitigating-basis-risk-in-weather-index-based-crop-insurance-harne/)
- Maharashtra field test of improved index design raised farmer satisfaction 50% and 72% (soybean, pearl millet) and improved payout-yield correlation. — [PreventionWeb](https://www.preventionweb.net/quick/48721)
- Claim that AI recalibration cuts basis risk 15-25% is unverified (vendor). — [Actuary.info](https://actuary.info/insights/parametric-insurance-21b-ai-basis-risk-reduction)

### Inferences
- Why unsolved: premium subsidies and distribution drive volume, but trust collapses when payouts miss real loss; individual farmers cannot judge trigger quality; designers lack field-level yield data.
- Concept for a small team: a B2B2C satellite+weather "trigger auditor" and farmer-facing voice agent (local language) that explains cover, confirms payout triggers automatically, and documents mismatches for the insurer. Not a consumer-direct product; sells to insurers, MFIs or NGOs. Feasibility: medium-low for a small team without insurer partnership; regulated underwriting needs a licensed carrier.

### Gaps
- No independent evidence of AI-derived triggers performing better. No data on heat-insurance uptake in SEA or LatAm.

## 8. US HSA optimization and employer-benefit underutilization

### Takeaway
HSAs are huge ($85B invested, 41.7M accounts) but most balances are uninvested, and many users leave reimbursements unclaimed. This is a smaller pain but a clean, low-regulation wedge.

### Cited Findings
- 41.7M HSAs at end-2025 covering about 62M people. Invested assets grew 33% in 2025 to about $85B, but only about 10% of HSAs hold investments (Devenir). — [Devenir demographic survey](https://www.devenir.com/2025-devenir-hsa-council-demographic-survey-findings/), [Devenir Sept 2026 newsletter](https://www.devenir.com/blog/devenir-hsa-newsletter-september-2026/)
- PSCA 2026 survey: 22% of participants invested part of balance in 2025 (20.3% in 2024); 83% of employees with HSA access contributed; only about a quarter of employers position HSAs as retirement tools. — [InvestmentNews](https://www.investmentnews.com/retirement-planning/hsa-participation-hits-record-high-but-retirement-strategy-lags-psca-finds/268006)
- InComm: half of HSA users skip reimbursement due to process hassles, missing about $2,500 a year in eligible expenses (vendor survey). — [PlanAdviser](https://www.planadviser.com/hsa-limits-rise-but-frustrated-users-leave-money-behind/)

### Inferences
- Concept: an agent connected to the HSA custodian and EOBs that tracks eligible receipts, auto-matches EOBs to HSA reimbursements, recommends contribution and invest-vs-spend, and drafts the appeal if a claim is denied. Revenue is hard (custodians own the relationship; employers pay for benefits tools). Not India-relevant. Lower priority than denials.

### Gaps
- No FSA forfeiture data found. No evidence on willingness to pay.

## 9. Other regions: UK/EU, SEA, Africa, LatAm (partial coverage)

### Takeaway
Claim denial and fraud problems appear in every region but with different shapes: in Brazil denials drive huge litigation, in Kenya mass claim rejection and fraud strain a new public scheme, and Asia has a large health protection gap. I found no usable UK/EU or SEA claims-friction data.

### Cited Findings
- Brazil: about 126,100 new lawsuits against health plans in Jan-May 2025 (+6.8%); about 231,000 between Aug 2024 and July 2025 (CNJ/UNDP); about 62% of suits concern procedures already on ANS's mandatory list; in two studies courts sided with consumers in 80%+ of sampled cases (São Paulo) and 92%+ (2011-2018); health plans accounted for about 30% of consumer-complaint rankings in 2024 (Idec). Many sources are industry/legal commentary. — [Revista Oeste](https://www.revistaoeste.com/saude/judicializacao-contra-planos-de-saude-cresce-quase-7-nos-5-primeiros-meses-de-2025/), [IESS](https://www.iess.org.br/sites/default/files/2025-12/Judicializac%CC%A7a%CC%83o.pdf), [USP journal](https://journals.usp.br/rdisan/article/download/176983/185553/573891), [Idec](https://idec.org.br/em-acao/em-foco/negativa-de-cobertura-em-planos-de-saude-sera-investigada)
- Kenya SHA: Ministry audit found about KSh 11B lost to fake claims (Oct 2024-Apr 2025); private hospital association RUPHA alleged KSh 10.6B of claims rejected without justification (Sept 2025) and demanded the legally mandated dispute tribunal; SHA CEO said about 80% of claims from level 5/6 hospitals under one fund were rejected in a pilot for out-of-package billing. Unresolved status unknown. — [Capital FM Africa](https://capitalfm.africa/audit-fake-claims-cost-sha-sh11bn-in-losses/), [The 254 Report](https://the254report.beehiiv.com/p/kenya-s-healthcare-emergency-sha-and-private-hospitals-at-breaking-point-437c), [K24](https://k24.digital/411/mercy-mwangangi-explains-why-sha-declined-80-of-hospitals-claims)
- Nigeria: thin sources; HMO rejections explained in a commercial blog only. — [NairaCompare](https://nairacompare.ng/blogs/why-health-insurance-claims-get-rejected-in-nigeria)

### Inferences
- Brazil and Kenya suggest a provider-side opportunity: claim-coding and documentation agents that reduce rejection (for hospitals), plus patient-side denial letters in Portuguese citing the ANS mandatory list. Brazil's "NIP" process with ANS and court preference for consumers imply high win odds for patient-side tools.

### Gaps
- No UK/EU, SEA, or Mexico/Colombia data retrieved. No ANS official 2025 complaint breakdown. Nigeria data weak.

## Cross-cutting: ranking for a small-team MVP (inference)

### Takeaway
(Inference, not sourced.) Highest leverage for an India-first small team: (1) rejected/partial health-claim co-pilot (Problem 3), (2) pre-admission cost simulator plus policy X-ray (Problems 4 and 6), (3) coverage audit with mis-selling and lapse alerts (Problem 5). For a US wedge: denial-appeal agent (Problem 1), where evidence of high overturn and low appeal is strongest.

### Cited Findings
- Timing facts that make late-2026 favourable: India's cashless timelines in force since August 1, 2024; Bima Sugam likely November 2026; US CMS-0057-F operational provisions in force 2026 with APIs January 2027; NSA IDR volume up several-fold; AI appeal tools already live in US. — see sections above.

### Inferences
- Common architecture: document ingestion (OCR for discharge summaries, EOBs, denial letters), policy/plan RAG with clause citations, rules library by jurisdiction, letter drafting, deadline tracker, human-review gate. Avoid insurer commissions to keep regulatory exposure low. Success-fee pricing aligns incentives but requires proof of recovery.

### Gaps
- Willingness to pay and unit economics were not researched. All AI-tool success rates are self-reported. Regulatory conclusions are not legal advice and need counsel in each jurisdiction.
