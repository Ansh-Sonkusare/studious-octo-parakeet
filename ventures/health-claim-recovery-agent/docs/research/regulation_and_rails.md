# Indian Regulatory Framework & Market Rails for an AI Personal-Finance / Mutual-Fund Startup (as of Oct 2026)

Research date: 2026-10-07. Most sources are secondary (law-firm notes, trade press: Cafemutual, Business Standard, Taxguru). Where a SEBI primary document was identified it is cited. Each rule is dated, and superseded rules are flagged. **Verify all numbers against sebi.gov.in / amfiindia.com before filing.**

---

## Q1. SEBI Investment Adviser (RIA) and Research Analyst (RA) regulations: who needs what, cost, timeline

### Takeaway
Any product that recommends specific funds or securities to a specific user for consideration ("which fund should I buy?") is "investment advice" and needs SEBI IA registration. The Dec-2024 overhaul made registration much cheaper and easier for a small team: a graduate degree, no experience requirement, a ₹1 lakh deposit instead of net worth, and SEBI fees of a few thousand rupees. The trade-offs are a fee cap (₹1.51 lakh/family/yr or 2.5% of AUA), strict separation of advice from distribution, and explicit liability and disclosure for AI use.

### Cited Findings
**Amendment timeline**
- SEBI (Investment Advisers) (Second Amendment) Regulations, 2024 and RA (Third Amendment) Regulations, 2024 were notified **16 Dec 2024**. Implementing circulars followed on **8 Jan 2025**: IA circular SEBI/HO/MIRSD/MIRSD-PoD1/P/CIR/2025/003 and RA circular .../2025/004. The consultation paper was dated 6 Aug 2024. — [Taxguru overhaul summary](https://taxguru.in/sebi/sebi-eases-rules-investment-advisers-research-analysts-2024-overhaul.html); [SEBI board paper Oct 2024](https://www.sebi.gov.in/sebi_data/meetingfiles/oct-2024/1728550911419_1.pdf)

**Qualifications**
- Minimum qualification for an individual IA/RA, or the principal officer of a non-individual firm, was reduced from a postgraduate degree to a **graduate degree** in a specified or allied field. Persons associated with advice need only a graduate degree in any discipline. The **5-year experience requirement was deleted** (Dec 2024). — [Taxguru](https://taxguru.in/sebi/sebi-eases-rules-investment-advisers-research-analysts-2024-overhaul.html)
- A non-individual IA may appoint an independent professional as compliance officer if that person holds NISM X-A, X-B, X-C and III-A. — [Taxguru 2025 guidelines](https://taxguru.in/sebi/sebi-updates-guidelines-investment-advisers-2025.html)
- Sources disagree on the RA qualification: "graduate in any discipline" vs "graduates in finance, accountancy, commerce, economics only". Existing individual RAs are exempt from the revised qualification rules. — [Moneylife](https://www.moneylife.in/article/sebi-introduces-major-reforms-for-investment-advisors-and-research-analysts/75888.html); [SCC Online](https://www.scconline.com/blog/post/2024/12/19/sebi-research-analyst-third-amendment-regulations-2024/)

**Net worth replaced by a deposit (applies to both IA and RA)**
- The deposit is based on the maximum client count on any day of the prior financial year: **up to 150 clients ₹1 lakh; 151–300 ₹2 lakh; 301–1,000 ₹5 lakh; 1,001+ ₹10 lakh**. It is held with a scheduled bank under lien to the IAASB (BSE). Existing IAs had until 30 Jun 2025; new applicants must comply immediately. — [Taxguru (IA circular 8 Jan 2025)](https://taxguru.in/sebi/sebi-updates-guidelines-investment-advisers-2025.html); same tiers for RAs per [Moneylife](https://moneylife.in/article/sebis-updated-guidelines-for-research-analysts-and-investment-advisers-impose-more-compliance-burden/76060.html)
- **SUPERSEDED:** older sources cite a net worth of ₹50 lakh (non-individual) / ₹5 lakh (individual), and a ₹25 lakh corporate figure under the 2020 rules. The Dec 2024 deposit system replaced these. — [Morningstar (old 2020 rule)](https://www.morningstar.in/posts/58861/register-as-non-individual-ria-if-clientele-exceeds-150-sebi.aspx); [Taxguru](https://taxguru.in/sebi/sebi-investment-advisers-second-amendment-regulations-2024.html)

**Individual vs non-individual**
- An individual IA with more than **300 clients or ₹3 crore in fees** in a financial year must apply for non-individual registration (Reg 13(e)). In-principle approval is valid for 3 months. — [Taxguru](https://taxguru.in/sebi/sebi-updates-guidelines-investment-advisers-2025.html)
- **SUPERSEDED:** under the 2020 rule, an individual IA had to move to non-individual at 150 clients. — [Morningstar](https://www.morningstar.in/posts/58861/register-non-individual-ria-clientele-exceeds-150-sebi.aspx)
- Partnership firms with no qualifying partner had to convert to an LLP or body corporate by 30 Sep 2025. — [Taxguru](https://taxguru.in/sebi/sebi-updates-guidelines-investment-advisers-2025.html)

**Part-time IA/RA (new, Dec 2024)**
- Individuals or partnerships whose other business is outside securities may register part-time. They need an employer NOC and a declaration that the businesses are separate. Finfluencers and those advising on gold, real estate or crypto are not eligible. — [Taxguru](https://taxguru.in/sebi/sebi-eases-rules-investment-advisers-research-analysts-2024-overhaul.html)
- One commentary says a part-time IA can serve at most 75 clients at any time. This is unverified against SEBI text. — [web summary of Taxguru Second Amendment page](https://taxguru.in/sebi/sebi-investment-advisers-second-amendment-regulations-2024.html)

**Fee caps (individual/HUF clients only)**
- Fixed-fee mode: **₹1,51,000 per family per year** (up from ₹1,25,000), revised every 3 years by CII. AUA mode: **2.5% of AUA per family per year**, where AUA counts only SEBI-regulated securities. The client may switch modes; the cap is the higher of the two. Non-individuals and accredited investors negotiate fees bilaterally. — [Taxguru (IA circular 8 Jan 2025)](https://taxguru.in/sebi/sebi-updates-guidelines-investment-advisers-2025.html)
- RA advance fees are capped at **one quarter** (Dec 2024). SEBI floated extending this to one year in Feb 2025; I could not confirm whether that was adopted. — [Business Standard Feb 2025](https://www.business-standard.com/amp/markets/news/sebi-looks-into-research-analysts-concerns-may-ease-advance-fees-norms-125021201574_1.html)

**Segregation of advice vs distribution**
- Reg 22 requires segregation of advisory and distribution at both **family and group level**. Exemptions: IAs serving only institutional clients or accredited investors, with a waiver. Stock broking is not treated as "distribution" for this rule. An annual segregation certificate from a CA/CS/CMA is required. — [Taxguru](https://taxguru.in/sebi/sebi-updates-guidelines-investment-advisers-2025.html)
- AMFI bars distributors from using "adviser" nomenclature. — [cleartax/industry summary via search](https://www.amfiindia.com/distributor-corner/ImportantInformation_Distributors)

**AI-specific obligations for IAs**
- Reg 15(14): an IA using AI tools is **solely responsible** for client data security, confidentiality and integrity, for advice generated from AI output, and for legal compliance, regardless of scale. Reg 18(9): the IA must **disclose the extent of AI use** at agreement stage and whenever required (existing clients by 30 Apr 2025). — [Taxguru](https://taxguru.in/sebi/sebi-updates-guidelines-investment-advisers-2025.html)

**Other operational requirements (IA circular, 8 Jan 2025)**
- Standardised MITC in client agreements, including a mandatory clause that the IA **cannot execute any trade without the client's specific, positive consent per trade**. IAs must also guide clients on CeFCoM (the centralised fee collection mechanism). Consent can be taken via DigiLocker/Aadhaar e-sign. — [Taxguru](https://taxguru.in/sebi/sebi-updates-guidelines-investment-advisers-2025.html)
- Reg 22A: IAs offering implementation services must record telephone consents with timestamps. — same source
- Annual compliance audit within 6 months of FY end, with adverse findings filed by 31 Oct. A functional website with prescribed disclosures is required. — same source
- An individual or partnership RA may also register as an IA, at arm's length. — same source

**Registration cost and time**
- SEBI FAQ (Aug 2025): for individuals and partnership firms, application fee ₹2,000, registration fee ₹3,000 for the first 5 years, renewal ₹1,000 per 5 years. Body-corporate fees per a third-party site: ₹10,000 application and ₹15,000 registration (unverified). — [SEBI IA FAQ Aug 2025](https://www.sebi.gov.in/sebi_data/faqfiles/aug-2025/1755174193178.pdf); [Corpseed](https://corpseed.com/knowledge-centre/registration-of-investment-adviser-sebi)
- Applications go via the IAASB (BSE Administration & Supervision Ltd, portal membershipraia.bseindia.com). IAASB recommends to SEBI, and enlistment with IAASB is a prerequisite. — [same SEBI FAQ](https://www.sebi.gov.in/sebi_data/faqfiles/aug-2025/1755174193178.pdf); [Conventus Law](https://conventuslaw.com/report/india-sebi-recognises-stock-exchanges-as-supervisory-and-administrative-body-for-investment-advisers-and-research-analysts/)
- No official IA-specific processing SLA was found. SEBI IMD lists 21 days for fresh registrations generally, and consultants quote 30–90 days. — [SEBI benchmark page](https://www.sebi.gov.in/department/investment-management-department-9/dof3-122/benchmark.html); [Clevercoins (consultant)](https://clevercoins.org/?p=4674)

**Education vs advice**
- A CA's incidental securities advice during tax planning needs no registration, but **security-specific advice to a particular client does**. — [Taxguru](https://taxguru.in/sebi/sebi-updates-guidelines-investment-advisers-2025.html)
- The Dec 2024 amendment excluded "trading calls" from the IA advice definition; these fall under RA. — [Taxguru Second Amendment](https://taxguru.in/sebi/sebi-investment-advisers-second-amendment-regulations-2024.html)

### Inferences
- **Cheapest compliant path for "recommendation/advice":** one founder (a graduate) registers as an individual IA. Out-of-pocket cost is about ₹5k SEBI fees plus ₹1 lakh lien deposit plus NISM exam fees plus IAASB membership fee (not quantified here). The individual registration lasts until 300 clients or ₹3 cr fees; then a company IA is needed. A startup planning to scale should incorporate and register as a non-individual IA from day one.
- The fee cap (₹1.51 lakh/family) is not binding for a mass-market app charging ₹1–5k/yr. The bigger constraints are the segregation rule (an IA entity and its group cannot earn MF distribution commissions from the same family) and per-trade consent for implementation.
- Because Reg 15(14) puts AI-output liability on the IA, an LLM advice bot run by an RIA needs logging, suitability (risk profiling) and human-review controls.

### Gaps
- The exact NISM requirement for individual IAs (X-A and X-B) post-Dec 2024 was not confirmed from the primary text in this session. Under the earlier regime both were required, and the circular references X-A/X-B for compliance officers.
- IAASB annual membership fee and current processing timelines are not confirmed.
- The part-time IA 75-client cap is unverified.

---

## Q2. AMFI Mutual Fund Distributor (ARN/EUIN)

### Takeaway
An ARN (NISM V-A plus AMFI registration plus empanelment with each AMC) lets you sell **regular plans** and earn trail commission. It is the classic "Groww/Paytm Money pre-2023" model, but it is legally separate from advice and, under the IA segregation rule, cannot be combined with advice to the same family.

### Cited Findings
- To become an MFD: pass **NISM Series V-A**, then register with AMFI for an ARN. A non-individual needs at least one employee with NISM V-A who holds an **EUIN**. AMFI's March 2024 circular introduced a provisional ARN for entities whose EUIN mapping is pending. — [AMFI Distributor Corner](https://www.amfiindia.com/distributor-corner/ImportantInformation_Distributors); [AMFI ARN Circular 24](https://www.amfiindia.com/Themes/Theme1/downloads/circulars/ARNCircular24-OptiontoapplyforProvisionalARN.pdf)
- After the ARN, the distributor must be empanelled with each AMC separately. — [AMFI Distributor Corner](https://www.amfiindia.com/distributor-corner/ImportantInformation_Distributors)
- EUIN validity is 3 years, tied to NISM certification renewal. — [AMFI Distributor Corner](https://www.amfiindia.com/distributor-corner/ImportantInformation_Distributors)
- Historically MFDs were exempt from IA registration for advice "incidental" to distribution. SEBI proposed removing this, and the IA segregation rule (2020, reaffirmed in Dec 2024) now separates the two at family/group level. — [Business Standard 2016](https://www.business-standard.com/article/pti-stories/mf-agents-oppose-sebi-registration-norms-for-advisory-services-116110600557_1.html); [Taxguru](https://taxguru.in/sebi/sebi-updates-guidelines-investment-advisers-2025.html)
- An EOP may not offer regular plans, so a distributor wanting to run an EOP needs a separate platform or entity. — [Kruti Gogri & Co](https://cskruti.com/execution-only-platforms-has-sebi-thrown-a-lifeline/)
- 2026 MF Regulations: from **1 Apr 2026** brokerage/commission payouts are **GST-exclusive** (GST outside the expense ratio). Commentary says distributors who are not GST-registered face lower effective commissions. — [Courtkutchehry](https://www.courtkutchehry.com/pages/blog/sebi-mutual-fund-brokerage-rules-2026-gst-outside-ter-impact/); [Value Research](https://www.valueresearchonline.com/learn/mutual-funds/sebi-mutual-fund-regulations-2026/)

### Inferences
- The ARN route suits an "execution + nudges" product monetised by trail commission (roughly 0.5–1% on equity regular plans, not verified here). It conflicts with an "unbiased AI adviser" positioning and cannot be combined with fee-based advice in the same group for the same client.
- Distributors earn on regular plans only. Facilitating direct plans requires being an RIA client-servicing platform, an EOP, or a broker in its EOP capacity.

### Gaps
- ARN/EUIN application fees (AMFI fee schedule) and the NISM V-A exam fee were not found.
- Whether SEBI formally abolished the "incidental advice" exemption for MFDs, as opposed to only the segregation rule, was not confirmed.

---

## Q3. SEBI Execution-Only Platform (EOP) framework for direct plans

### Takeaway
Since **1 Sep 2023**, a platform facilitating **direct-plan** MF transactions (without advice) for unrelated investors must be an EOP. Category 1 is an AMC agent registered with AMFI (₹1 cr net worth, ≤₹2/txn paid by AMCs). Category 2 is a SEBI stock broker in the exchange EOP segment (₹10 lakh BMC). A small startup can realistically use only Category 1, and only with ₹1 cr net worth; otherwise it must be an RIA serving its own advisory clients.

### Cited Findings
- SEBI circular **SEBI/HO/IMD/IMD-PoD-1/P/CIR/2023/86, 13 Jun 2023**, effective **1 Sep 2023**. — [Taxmann](https://www.taxmann.com/post/blog/sebi-introduces-framework-for-execution-only-platforms-for-investing-in-direct-plans-of-mf-schemes/)
- **Category 1** = agent of AMCs, registered with **AMFI**, integrating with AMCs/RTAs as a direct-plan aggregator. **Category 2** = agent of the investor, registered as a **stock broker** in the EOP segment, transacting only through exchange platforms. — [Taxmann](https://www.taxmann.com/post/blog/sebi-introduces-framework-for-execution-only-platforms-for-investing-in-direct-plans-of-mf-schemes/); [AMFI Cat-1 guidelines](https://www.amfiindia.com/eops/amfi-guidelines)
- AMFI set a **₹1 crore net worth** criterion for Category 1 (Sep 2023), plus a code of conduct and cyber-security framework. Agreements with each AMC are required. — [Business Standard Sep 2023](https://www.business-standard.com/amp/markets/news/amfi-sets-rs-1-crore-net-worth-criteria-for-eops-releases-guidelines-123090100961_1.html)
- Category 2 EOP-only brokers must keep a **₹10 lakh base minimum capital** deposit with the exchange (Oct 2023). — [Business Standard Oct 2023](https://www.business-standard.com/amp/markets/news/sebi-asks-brokers-functioning-in-eop-to-maintain-minimum-capital-deposit-123100601024_1.html)
- Category 1 EOPs can receive **up to ₹2 per transaction** from AMCs, and AMCs may also reimburse payment-gateway charges (AMFI, Nov 2023). — [Cafemutual](https://cafemutual.com/news/industry/31192-execution-only-platforms-registered-with-amfi-to-get-up-to-rs2-per-transaction); [Business Standard](https://www.business-standard.com/markets/stock-market-news/amfi-sets-rs-2-transaction-charge-limit-for-direct-mutual-fund-platforms-123110900975_1.html)
- Further conditions: the EOP must be a **body corporate**, with at least 2 qualified managers and 1 compliance officer. **No regular plans** and **no scheme advertisements** are allowed. **RIA and broker platforms serving exclusively their own advisory/broking clients are outside the EOP framework.** — [Kruti Gogri & Co](https://cskruti.com/execution-only-platforms-has-sebi-thrown-a-lifeline/)
- AMFI's Category-1 list includes MF Utilities, ETMoney (Banayantree), Right Alpha (Matdev IA), smallcase (Case Platforms), Jupiter (Amica IA), Fi (EPIFI Wealth), Value Research, KFin, CAMS and Valuefy, several with end-dates in late 2026. — [AMFI list of EOPs](https://www.amfiindia.com/eops/list-of-eops)
- Groww, Zerodha Coin and Kuvera do not appear on the AMFI Category-1 list. Larger players operating under stock-broking licences were expected not to register with AMFI. — [Cafemutual](https://cafemutual.com/news/industry/31192-execution-only-platforms-registered-with-amfi-to-get-up-to-rs2-per-transaction); [AMFI list](https://www.amfiindia.com/eops/list-of-eops)
- The EOP framework also allowed platforms to monetise by charging transaction fees (Dec 2022 board decision). — [Business Standard Dec 2022](https://www.business-standard.com/amp/article/markets/sebi-opens-doors-for-monetisation-of-groww-other-mf-investment-platforms-122122001093_1.html)

### Inferences
- Zerodha Coin and Groww most likely operate direct MF under their stock-broker registration, either via the exchange EOP segment or as a broker serving its own clients. Kuvera has historically operated via an RIA entity. **This was not confirmed in this session.**
- For a small startup, Category 1 EOP economics (₹2/txn, ₹1 cr net worth, no ads, no advice) are poor. The **RIA route** is the practical way to offer direct-plan execution, because own-client RIA platforms are exempt from the EOP framework.

### Gaps
- Category 2 EOP registrations (which brokers) and Kuvera's current registration were not confirmed.
- Whether AMFI raised or changed the ₹2/txn cap after 2023 was not checked.

---

## Q4. SEBI on AI/ML, finfluencers, and "advice vs education"

### Takeaway
SEBI has not created any carve-out for AI. An unregistered chatbot that tells a specific user which fund to buy is giving unregistered investment advice, regardless of disclaimers. Since Feb 2025, any regulated entity using AI (in-house or third-party) is solely liable for its outputs. Broader tiered AI guidelines (human oversight, kill switch) were announced as "soon" in Aug 2026 but were not yet issued as of the latest sources. The finfluencer rules (Aug 2024 / Jan 2025) bar regulated entities from associating with unregistered advisers, and confine "education" to content using price data at least 3 months old.

### Cited Findings
**AI/ML reporting and liability**
- **Jan 2019:** SEBI asked brokers and depositories using AI/ML to make disclosures and report their AI systems. Exchanges continue to run AI/ML reporting circulars. — [Business Standard Jan 2019](https://www.business-standard.com/amp/article/markets/sebi-asks-brokers-depositories-using-ai-tools-to-make-security-disclosures-119010401096_1.html); [Mondaq on NSE AI/ML reporting](https://www.mondaq.com/india/new-technology/1770328/nse-circular-on-aiml-reporting-what-trading-members-need-to-know)
- **10 Feb 2025:** amendments to the Intermediaries Regulations and SECC Regulations, effective 10 Feb 2025 (Depositories from 1 Apr 2025). Any SEBI-regulated person using AI/ML, whether built in-house or procured from a third party and "irrespective of the scale", is **solely responsible** for data privacy and security, for the AI outputs, and for legal compliance. — [Fox Mandal / Lexology](https://foxmandal.in/News/regulated-entities-responsible-for-output-of-ai-usage-sebi/); [Lexplosion](https://lexplosion.in/sebi-issues-guidelines-on-ai-usage-entities-using-ai-ml-tools-responsible-for-data-security-ai-generated-outputs-and-compliance-with-applicable-laws/)
- **20 Jun 2025 consultation paper**, "Guidelines for responsible usage of AI/ML in Indian securities markets", with comments due 11 Jul 2025. It set out 5 principles (safety and reliability; equality; inclusivity and non-discrimination; privacy and security; transparency) and covered model governance, investor disclosure, testing, fairness and bias, and cyber security. It proposed a **lighter regime for AI that does not directly affect customers**. — [Taxguru](https://taxguru.in/sebi/sebi-proposes-guidelines-responsible-usage-ai-ml-indian-securities-markets.html); [Fox Mandal](https://foxmandal.in/News/sebi-floats-paper-on-responsible-ai-use-in-indian-securities-market/)
- **19 Aug 2026:** SEBI Chairman Pandey (FICCI CAPAM) said SEBI will "shortly" issue AI/ML guidelines. They will take a **tiered approach** with **human oversight, data controls and kill-switch mechanisms**, and every regulated entity remains fully responsible for AI tools. **Status as of Oct 2026: final circular not found.** — [ANI](https://aninews.in/news/business/sebi-to-soon-issue-aiml-guidelines-for-capital-markets-mandate-human-oversight-kill-switch-controls-chairman-pandey20260819121850/); [Moneylife](https://www.moneylife.in/article/ai-in-markets-sebi-to-mandate-human-oversight-kill-switches-and-data-controls-says-pandey/81406.html); [Policy Edge](https://www.policyedge.in/p/sebi-signals-tiered-ai-rules-with-kill-switches-and-human-oversight)
- **5 May 2026:** SEBI "Advisory on Emerging Advanced AI Tools for Vulnerability Detection". This is a cybersecurity advisory, **not** the AI governance framework. — [SEBI circular May 2026](https://www.sebi.gov.in/legal/circulars/may-2026/advisory-on-emerging-advanced-artificial-intelligence-ai-tools-for-vulnerability-detection_101270.html)
- SEBI's FY26 annual report (Aug 2026) describes "Project Sudarsan", which uses AI to monitor unsolicited financial advice on social media, and "SEBI R(AI)DAR" for ad review. It also notes a Google Play "verified app" label partnership. — [Business Today](https://www.businesstoday.in/markets/stocks/story/sebi-annual-report-ai-tools-deployed-to-track-finfluencers-misleading-investors-547810-2026-08-07)
- IA-level AI liability and disclosure (Reg 15(14) and 18(9)) is covered in Q1. — [Taxguru](https://taxguru.in/sebi/sebi-updates-guidelines-investment-advisers-2025.html)

**Finfluencer / association rules**
- **Aug 2024** (effective 26 or 29 Aug 2024; sources differ): amendments bar SEBI-regulated entities and their agents from associating, directly or indirectly, with persons who give unregistered advice or make performance/return claims. Persons engaged **solely in investor education**, without advice or return claims, are exempt. — [Nishith Desai](https://nishithdesai.com/research-and-articles/hotline/technology-law-analysis/securities-market-regulators-continued-quest-against-unfiltered-financial-advice-15193); [Taxmann](https://taxmann.com/post/blog/analysis-sebis-new-regulations-on-finfluencers-protecting-investors-from-unregistered-advisors)
- **Oct 2024 circular:** regulated entities had **3 months** to terminate existing contracts with such persons. Associations through "specified digital platforms" with preventive and curative controls are excluded. — [Outlook Business](https://www.outlookbusiness.com/markets/sebi-directs-regulated-entities-to-sever-ties-with-finfluencers-in-3-months)
- **29 Jan 2025 circular:** "education" content may only use market price data **at least 3 months old**. It may not use stock names, codes or recent prices in any way that implies advice or recommendation. — [Business Standard Jan 2025](https://www.business-standard.com/markets/news/sebi-finfluencer-circular-live-stock-data-market-education-rules-125013000571_1.html)

**Enforcement against unregistered advice**
- Dec 2025: SEBI barred Avadhut Sathe and impounded **₹546.16 crore** for unregistered advisory dressed up as a trading academy. Earlier cases: "Baap of Chart" (₹18.14 cr recovery) and Ravindra Bharti. No enforcement against an AI chatbot specifically was found. — [Storyboard18](https://www.storyboard18.com/amp/how-it-works/sebi-bans-finfluencer-avadhut-sathe-impounds-rs-546-crore-for-running-unregistered-advisory-85392.htm); [Deccan Herald](https://www.deccanherald.com/business/baap-of-chart-sebi-bars-three-entities-for-unauthorised-investment-advisory-services-2741685)

### Inferences
- **An education chatbot with no licence** is defensible if it explains concepts (what an ELSS is, expense ratios, how SIPs work) and avoids naming or recommending specific schemes to a specific user. Any "which fund should I buy?" answer naming a scheme for that user's situation crosses into advice under IA Reg 3, and the "education" framing did not protect the trading-academy cases. Data used in educational examples should respect the 3-month lag if it involves stock names or prices. That lag rule binds regulated entities and their associates, but it is a useful safe harbour benchmark.
- **The finfluencer rule creates distribution risk.** If the unregistered startup is "associated" with a regulated entity (an AMC, broker or EOP paying referral fees), that regulated entity is in breach. Partnerships with brokers or AMCs therefore effectively require the startup to be registered, or to be purely educational with no performance claims.
- The forthcoming tiered AI rules will likely place customer-facing advice and order-placement AI in the highest tier. Building an audit log, human-in-loop review and a kill switch from day one is prudent.

### Gaps
- Final SEBI AI/ML guidelines circular: not found as of Oct 2026.
- No SEBI order or FAQ specifically addresses generative-AI chatbots giving advice.

---

## Q5. SEBI retail algo trading framework (Feb 2025)

### Takeaway
Retail API/algo trading is permitted only through brokers. Algos must be registered with the exchange via the broker, with algo-provider empanelment. Full applicability was phased in through **1 Apr 2026**. An AI agent that places orders on users' behalf in equities/F&O falls inside this regime. MF orders are outside it, but a MF-order agent still needs RIA or broker standing.

### Cited Findings
- SEBI circular "Safer participation of retail investors in Algorithmic trading", **4 Feb 2025**. The original effective date of 1 Aug 2025 was extended to 1 Oct 2025 (circular of 29 Jul 2025). — [Taxmann](https://www.taxmann.com/post/blog/sebi-extends-deadline-for-retail-algo-trading-framework/); [The Week](https://www.theweek.in/wire-updates/business/2025/07/29/dcm84-biz-sebi-algo.html)
- The **30 Sep 2025 circular** phased the rollout. Brokers had to register at least one retail algo product and strategy by 31 Oct 2025, complete registration by 30 Nov 2025 and hold a mock session by 3 Jan 2026. Brokers that missed these milestones were barred from onboarding new API-algo clients from 5 Jan 2026. **Full applicability: 1 Apr 2026.** — [SEBI circular PDF Sep 2025](https://www.sebi.gov.in/sebi_data/attachdocs/sep-2025/1759232056254.pdf); [Outlook Business](https://www.outlookbusiness.com/markets/sebi-extends-deadline-to-implement-retail-algo-trading-by-april-2026)
- NSE implementation overview, with community discussion. — [TradingQnA](https://tradingqna.com/t/a-comprehensive-overview-of-nse-s-new-retail-algo-trading-framework/181989?page=5)

### Inferences
- The well-known framework features (broker as principal, algo provider empanelled with the exchange, unique algo ID tagging, static-IP API access, an order-per-second threshold for registration, and "black-box" algo providers needing RA registration) come from the Feb 2025 circular. Those details were **not re-verified in this session**.
- For an MF-focused MVP, algo trading is a distraction. It needs a broker partner, exchange empanelment and, for opaque strategies, RA registration.

### Gaps
- Post-Apr 2026 amendments to the algo framework were not searched.

---

## Q6. Data rails: Account Aggregator, CAS, MF Central, depository eCAS

### Takeaway
The AA network carries MF folio data (CAMS/KFin as FIPs) and demat holdings (NSDL/CDSL), but **only regulated entities can be FIUs**. An unregulated portfolio tracker must register (an RIA is the cheapest qualifying licence) or partner with a regulated FIU. The OTP-based MF Central pull was curtailed in Sep–Nov 2025. The fallback is user-uploaded or email-forwarded **CAS PDFs** (CAMS/KFin MF CAS; NSDL/CDSL eCAS), which any company can parse.

### Cited Findings
**AA ecosystem**
- RBI NBFC-AA Master Direction issued **2 Sep 2016**. In Oct 2021 AAs were placed in the base layer of scale-based regulation. FIP additions: GSTN (Nov 2022), NPS CRAs (Oct/Nov 2023), CCIL Retail Direct (Feb 2024). — [CASParser 2026 (vendor)](https://casparser.in/blog/state-of-account-aggregator-2026/)
- SEBI's **Aug 2022** circular brought depositories (and AMCs/RTAs) into the AA framework as FIPs. CDSL operates as an FIP sharing demat data on consent. — [CDSL FIP page](https://www.cdslindia.com/Investors/FIP.html)
- Coverage per a vendor (Mar 2026): equities, MF units, ETFs, AIFs, REITs and InvITs via NSDL/CDSL; MF folios via CAMS and KFin RTAs, each live with about 13 AAs. Depository history is capped at 2 years on AA. Joint accounts are excluded. Bonds, G-Secs, EPF and PPF are still "proposed". — [CASParser](https://casparser.in/blog/state-of-account-aggregator-2026/)
- **Who can be an FIU:** entities regulated by RBI, SEBI, IRDAI, PFRDA (or the Department of Revenue). Pure fintechs without a licence must license or partner. The Oct 2023 "FIP-first" rule says a regulated entity holding financial information must also join as an FIP. — [Sahamati FAQ](https://sahamati.org.in/faq/); [Sahamati FIU page](https://sahamati.org.in/fiu/); [CASParser](https://casparser.in/blog/state-of-account-aggregator-2026/)
- FIU onboarding: sandbox, then certification by a Sahamati-empanelled auditor (code/infra audit, API conformance, encryption), then optional Sahamati registration. TSPs such as Setu, Digio and Perfios offer FIU modules and handle certification. — [Setu docs](https://docs.setu.co/data/account-aggregator/licenses-and-go-live/go-live); [Digio](https://documentation.digio.in/fiu-tsp/how_to_become_a_fiu/); [Sahamati join guide](https://sahamati.org.in/how-to-join-the-account-aggregator-network-to-share-and-access-financial-data/)
- Costs: Sahamati publishes no standard pricing and fees are bilateral. Each AA must have a board-approved pricing policy. Vendor estimate: **₹5–25 lakh+ first-year cost and 5–10 months of integration**, plus quarterly self-tests and a CISA IS audit every 2 years. **Treat as vendor claim.** — [CASParser](https://casparser.in/blog/state-of-account-aggregator-2026/)
- AAs by live FIP count (Mar 2026): Anumati 80+, CAMS Finserv 70+, OneMoney 65+, Finvu 60+, NADL 60+. CAMS operates both as an RTA-FIP and as an AA (CAMSfinserv). — [CASParser](https://casparser.in/blog/state-of-account-aggregator-2026/); [CDSL FIP page](https://www.cdslindia.com/Investors/FIP.html)
- One secondary source reports RBI recognising Sahamati as the AA SRO on 5 Jun 2026 (unconfirmed). — [ecorpit builder's guide](https://ecorpit.com/account-aggregator-integration-fintech-builders-2026/)

**MF Central and CAS**
- MF Central was launched Sep 2021 by CAMS and KFin. In Nov 2024 the two formed a standalone JV to operate it. — [Business Standard Nov 2024](https://business-standard.com/amp/markets/capital-market-news/cams-and-kfin-technologies-form-jv-for-mf-central-124111101450_1.html)
- **18 Sep 2025:** AMFI reportedly asked MF Central to **stop sharing investor data directly with third-party fintech apps** (OTP-consent pulls used by apps for guided investing and loans-against-MF), citing data security and uninformed consent. The report notes that apps with PMS/RIA licences can still use AA. — [Business Standard](https://www.business-standard.com/amp/markets/mutual-fund/amfi-asks-mf-central-to-stop-sharing-investor-data-with-third-party-apps-125091801057_1.html); [Cafemutual](https://cafemutual.com/news/press-news/35828-amfi-asks-mf-central-to-stop-sharing-investor-data-with-third-party-apps)
- **Nov 2025:** the CAMS MD said MF Central will give investors more control over third-party data sharing, implying tightened rather than fully stopped access. Final status unverified. — [Business Standard Nov 2025](https://www.business-standard.com/markets/mutual-fund/mf-central-to-tighten-third-party-data-access-says-cams-md-anuj-kumar-125111401771_1.html)
- CAS remains investor-downloadable from MF Central, CAMS and KFin. CDSL/NSDL also send a consolidated eCAS covering demat holdings and MF folios. — [Business Standard](https://www.business-standard.com/amp/markets/mutual-fund/amfi-asks-mf-central-to-stop-sharing-investor-data-with-third-party-apps-125091801057_1.html); [CASParser formats](https://casparser.in/blog/understanding-cas-formats/)
- CAS-parsing vendors (e.g. CASParser, from ₹999/month by its own claim) are open to any company and offer Gmail-OAuth CAS ingestion. These are vendor claims. — [CASParser](https://casparser.in/blog/state-of-account-aggregator-2026/)
- SEBI's Apr 2024 advisory bars intermediaries from seeking access to investors' private device data (contacts, location). — [Business Standard](https://www.business-standard.com/amp/markets/mutual-fund/amfi-asks-mf-central-to-stop-sharing-investor-data-with-third-party-apps-125091801057_1.html)

### Inferences
- **MVP portfolio tracking without a licence:** use CAS PDF upload or email-forward parsing (password = PAN-based). It is legally simplest and is consent-based by the user's own action. Becoming an RIA unlocks the FIU/AA route for automated refresh.
- The AMFI/MF Central tightening signals regulator scepticism about unregulated apps pulling MF data. Expect scrutiny of screen-scraping or OTP-relay workarounds.

### Gaps
- Per-fetch AA pricing from Finvu, OneMoney, Setu and Saafe was not published or found.
- The final MF Central third-party access policy after Nov 2025 was not found.

---

## Q7. MF transaction rails, payments, KYC, pooling ban, AI agents placing orders

### Takeaway
Order rails are BSE StAR MF, NSE NMF II, MF Utilities, or direct AMC/RTA (EOP) integrations. Access requires an ARN (regular plans), RIA registration (direct plans for own clients via BSE StAR MF), broker membership, or EOP registration. Since **1 Jul 2022** money must flow directly from the investor's verified bank account to the AMC or clearing corporation (no pool accounts, no platform-named mandates). An "AI agent that never touches money" is architecturally normal, but **the entity placing orders must still be one of those registered types**, and an RIA must take per-trade client consent.

### Cited Findings
**Rails and access**
- **BSE StAR MF for RIAs:** a SEBI 2016 circular allowed RIAs to use exchange infrastructure to transact in MF units for clients (direct plans), live from 4 Nov 2016. RIAs cannot handle pay-in/pay-out; money moves between the investor and the clearing corporation. RIA membership is **direct plans only**. BSE's RIA page lists membership, processing and annual fees as **nil** for RIAs. AMCs pay BSE a per-transaction charge. — [BSE RIA page](https://bseindia.com/Static/Markets/MutualFunds/registered_invest_advisors.aspx); [Cafemutual 2016](https://cafemutual.com/news/industry/6751-rias-can-start-using-bse-star-mf-platform-from-november-4); [Business Standard 2016](https://www.business-standard.com/amp/article/pti-stories/investment-advisors-can-use-bse-mf-platform-from-tomorrow-116110301111_1.html)
- BSE's general MF-segment membership (for distributors) lists a ₹1 lakh deposit, ₹50k admission and ₹75k annual fee plus GST. It may be outdated or not apply to RIAs. — [BSE MF membership](https://www.bseindia.com/Static/Markets/MutualFunds/MFI.aspx)
- BSE StAR MF exposes SOAP APIs (an older third-party library). BSE launched StAR MF Plus (2021) with front- and back-office tools for MFDs and RIAs. — [GitHub mf-platform-bse](https://github.com/utkarshohm/mf-platform-bse); [Cafemutual](https://cafemutual.com/news/industry/21139-bse-launches-star-mf-plus-for-mfdsrias)
- **NSE NMF II:** for AMFI-registered distributors and trading members, via limited-purpose membership. A one-time ₹2,000 fee has applied since Sep 2018 (deposit waived). It offers APIs for subscription, redemption, SIP/SWP/STP, e-KYC and FATCA. Distributor-oriented, with no direct plans per a 2018-era source. AMCs pay ₹6–30/txn. — [NSE NMF II FAQ](https://www.nseindia.com/products/content/equities/mutual_funds/NMF_II_FAQ.pdf); [Cafemutual](https://cafemutual.com/news/industry/12461-after-bse-star-mf-nse-nmf-ii-to-levy-a-transaction-fee); [Cafemutual fee waiver](https://cafemutual.com/news/industry/13267-nse-nmf-ii-waives-off-registration-fee-for-distributors)
- **MF Utilities (MFU):** an AMC-owned transaction aggregator issuing a Common Account Number (CAN). It serves investors and distributors, supports direct plans, and is now on AMFI's Category-1 EOP list. — [AMFI EOP list](https://www.amfiindia.com/eops/list-of-eops); [Advisorkhoj forum](https://www.advisorkhoj.com/post-your-queries/Can-you-compare-MFU-and-NSE-platform-or-any-other-platform-for-my-investors)

**Pooling ban / "never touch money"**
- SEBI circular of **Oct 2021** (originally effective 1 Apr 2022, extended to **1 Jul 2022**). Distributors, platforms, brokers and IAs may not pool investor money or units. Payment goes from the investor's verified bank account mapped to the folio directly to the AMC, or via an RBI-authorised payment aggregator or a SEBI-recognised clearing corporation. Units go directly to the investor's folio or demat. **Third-party payments are prohibited** (the AMC must verify). Intermediaries may **not accept one-time mandates in their own name**. Portfolio managers are exempt. SEBI suspended NFOs until compliance. — [Business Standard Oct 2021](https://www.business-standard.com/amp/article/markets/sebi-discontinues-the-use-of-pool-accounts-for-transactions-in-mfs-121100401285_1.html); [NSDL copy of circular](https://nsdl.co.in/downloadables/pdf/2021-0103-Policy-SEBI%20Circular%20on%20discontinuation%20of%20usage%20of%20pool%20accounts%20for%20transactions%20in%20units%20of%20Mutual%20Funds%20on%20the%20Stock%20Exchange%20Platforms.pdf); [5paisa summary](https://www.5paisa.com/sebi-mf-circular); [Outlook Money](https://www.outlookmoney.com/amp/story/news/no-nfos-till-july-1-sebi-bars-launches-until-mfs-discontinue-pooling-of-accounts-news-189608)
- Rollout on BSE StAR MF caused about 4 weeks of processing and redemption delays (Jul 2022). Groww discontinued its "Groww Balance" pool wallet. — [Moneylife](https://www.moneylife.in/article/fin-techs-distributors-and-investors-cry-foul-as-bse-star-mf-platform-experiences-glitches-after-implementation-of-sebis-new-regulatory-changes/67888.html); [Groww blog](https://groww.in/blog/sebi-bans-pooling-money-for-mutual-funds)

**Payments**
- RBI raised the UPI AutoPay limit without additional authentication from ₹15,000 to **₹1 lakh** per transaction for MF subscriptions, insurance premiums and credit-card bills (**Dec 2023**). Above ₹1 lakh, use net-banking, debit-card or Aadhaar eNACH. — [Business Standard Dec 2023](https://business-standard.com/finance/news/automatic-payment-limit-through-upi-raised-to-rs-1-lakh-says-rbi-123121201097_1.html); [5paisa](https://tradebetter.5paisa.com/t/introducing-upi-autopay-for-seamless-mutual-funds-sip-payments/74)
- BSE StAR MF enabled e-mandates with 40 banks as of 2018. — [Business Standard 2018](https://www.business-standard.com/article/pti-stories/40-banks-enabled-for-e-mandate-on-bse-star-mf-118030600887_1.html)

**KYC**
- KRAs: CAMS KRA, CVL KRA, KFin KRA, NDML and DotEx. From **1 Apr 2024**, KRAs independently validate name, PAN and DOB against the Income Tax database. Only "**KYC Validated**" status allows unrestricted transactions. "KYC Registered" works with existing AMCs only. "On Hold" and "Rejected" block transactions. About 13 million accounts were affected in 2024. — [HyperVerge](https://hyperverge.co/blog/sebi-kyc-guidelines/); [CAMS revised KYC](https://www.camsonline.com/assets/PDF/Revised_KYC_Process.pdf); [Business Standard May 2024](https://www.business-standard.com/amp/finance/personal-finance/mutual-fund-kyc-how-to-verify-status-online-fix-pan-mf-folio-mismatch-124050200301_1.html); [Bajaj AMC](https://www.bajajamc.com/?p=19299)
- SEBI relaxed the requirement that PAN be linked to Aadhaar for "KYC Registered" status. Sources conflict on whether Aadhaar-validated KYC is needed for new purchases. — [Outlook Money](https://www.outlookmoney.com/amp/story/invest/sebi-relaxes-norms-for-investors-to-get-kyc-registered-status-read-more)

**AI agent placing orders**
- RIA MITC mandates that the **IA cannot execute any trade without the client's specific, positive consent on each trade**. Telephone consents must be recorded (Reg 22A). — [Taxguru](https://taxguru.in/sebi/sebi-updates-guidelines-investment-advisers-2025.html)

### Inferences
- **The "AI agent that places orders without touching money" pattern** is: the agent builds an order, the user approves it (OTP or in-app consent per order), the order goes to BSE StAR MF via the RIA's credentials, and payment runs from the user's own bank to the clearing corporation via UPI or eNACH. This fits the RIA plus BSE StAR MF route. Fully autonomous execution, with standing instructions and no per-trade consent, conflicts with the RIA per-trade consent rule. A pre-registered SIP mandate is a client-instructed standing order, which is likely acceptable, but whether AI-triggered rebalancing under a standing mandate counts as consent is legally untested.
- Without any registration, a startup cannot connect to BSE, NSE or MFU at all. It could only deep-link users to AMC websites or apps, or partner with a registered entity, which raises finfluencer "association" issues if paid.

### Gaps
- Current (2026) BSE StAR MF fees and API (REST vs SOAP) were not confirmed.
- Whether RIAs can access NSE NMF II or MFU directly for direct plans was not confirmed.
- CKYC integration rules for MF onboarding (CKYC as KYC source) and video-KYC specifics for KRAs were not researched in depth.

---

## Q8. Data protection: DPDP Act 2023 and DPDP Rules 2025

### Takeaway
The DPDP Rules were notified around **13–14 Nov 2025**. Consent-manager provisions start around **Nov 2026**, and the bulk of fiduciary obligations (notice, consent, security, breach notification, rights) bind from around **13–14 May 2027**. Penalties reach up to ₹250 crore. A finance app should build DPDP-grade notice and consent, deletion, and breach response now. AA consent artefacts already align with this model.

### Cited Findings
- Rules notified **14 Nov 2025** (Gazette G.S.R. 843(E)–846(E)), with the Data Protection Board provisions commencing 13 Nov 2025 (sources differ by a day). Rules 1, 2 and 17–21 apply immediately. Consent Manager registration applies **12 months** later. Rules 3 and 5–16 (fiduciary duties: notice, security safeguards, breach intimation, retention, rights) and 22–23 apply **18 months** later, around May 2027. — [Deccan Herald](https://www.deccanherald.com/india/centre-notifies-dpdp-rules-implementation-planned-in-phases-spread-over-12-18-months-3798465); [Grant Thornton](https://www.grantthornton.in/globalassets/1.-member-firms/india/assets/pdfs/flyers/dpdp-rules-nov-2025.pdf); [Uniqus](https://uniqus.com/digital-personal-data-protection-act-timelines/)
- Consent managers must register with the DPB, with a reported minimum net worth of ₹2 crore, and must meet neutrality and audit-trail obligations. — [Anantam IAS summary](https://anantamias.com/current-affairs/dpdp-rules-data-protection-framework-2025/?pdf=1); [Mondaq](https://www.mondaq.com/india/privacy-protection/1708830/dpdp-act-compliance-mandate)
- Penalty ceilings (Schedule to the Act): up to ₹250 cr for failing to maintain security safeguards, ₹200 cr for children's data, ₹200 cr for breach-notification failure (one source says ₹150 cr; check the Act schedule), ₹150 cr for SDF obligations, ₹50 cr residual. — [Uniqus](https://uniqus.com/digital-personal-data-protection-act-timelines/)
- The IT Act SPDI Rules 2011 remain in force during the 18-month transition. — [Deccan Herald](https://www.deccanherald.com/india/centre-notifies-dpdp-rules-implementation-planned-in-phases-spread-over-12-18-months-3798465)
- SEBI layer: regulated entities using AI are solely responsible for data privacy and security (Feb 2025 amendments). The SEBI CSCRF also applies to regulated entities. — [Fox Mandal](https://foxmandal.in/News/regulated-entities-responsible-for-output-of-ai-usage-sebi/)

### Inferences
- Financial data (PAN, holdings, bank details) sent to a foreign LLM API is cross-border processing. DPDP allows it unless the destination is blacklisted, but SEBI-regulated entities have separate data-localisation expectations under the cybersecurity framework (CSCRF), which were not verified here. Use of offshore LLMs for client data needs legal review.

### Gaps
- Whether SEBI's CSCRF (Aug 2024) imposes data-localisation requirements on small RIAs that would constrain foreign LLM APIs was not researched.
- The penalty figure for breach notification is inconsistent across secondary sources.

---

## Q9. 2025–2026 developments: SEBI MF Regulations 2026, TER→BER, MF Lite, SIF

### Takeaway
New **SEBI (Mutual Funds) Regulations, 2026** replaced the 1996 regulations from **1 Apr 2026**. TER became a **Base Expense Ratio (BER)** with statutory levies shown separately, and caps were lower. Brokerage caps were cut. Solution-oriented (retirement/children's) categories were removed, and GST moved outside the expense ratio. **MF Lite** (passive AMCs, effective 16 Mar 2025) and **SIFs** (₹10 lakh minimum, live 1 Apr 2025) are in force. Any product data model and fund-comparison logic must handle BER vs TER discontinuity.

### Cited Findings
- New MF Regulations effective **1 Apr 2026**. TER is replaced by **BER** (core costs only); STT, stamp duty and GST are reported separately. Caps: index funds/ETFs **0.90% BER** (from 1.00% TER); close-ended equity **1.00%** (from 1.25%); active equity slabs up to about 2.10% for small AUM. — [Value Research](https://www.valueresearchonline.com/learn/mutual-funds/sebi-mutual-fund-regulations-2026/); [Maxiom](https://maxiomassetmanagement.com/blog/sebi-mutual-fund-regulations-2026-what-changed/); [Upstox](https://upstox.com/learning-center/personal-finance/sebi-mutual-fund-rules-2026/article-1563/)
- Brokerage caps: **6 bps cash / 2 bps derivatives** (from 12/5 bps). The extra 5 bps exit-load allowance was removed. A Dec 2025 draft had proposed 2 bps/1 bp, which was superseded by the final figures. — [Value Research](https://www.valueresearchonline.com/learn/mutual-funds/sebi-mutual-fund-regulations-2026/); [Business Standard Dec 2025](https://www.business-standard.com/markets/news/sebi-board-to-review-mutual-fund-fee-structure-stock-broker-rules-125121601021_1.html)
- The solution-oriented category (retirement, children's funds) was removed. Existing schemes stopped accepting fresh subscriptions from Apr 2026. Scheme names must align with portfolios by around Aug 2026. Optional performance fees are allowed subject to conditions. Distributor brokerage is GST-exclusive. — [Value Research](https://www.valueresearchonline.com/learn/mutual-funds/sebi-mutual-fund-regulations-2026/); [Courtkutchehry](https://www.courtkutchehry.com/pages/blog/sebi-mutual-fund-brokerage-rules-2026-gst-outside-ter-impact/)
- A March 2026 MF Master Circular reportedly incorporates MF Lite. — [Wright Research](https://www.wrightresearch.in/blog/mf-lite-framework/)
- **MF Lite:** announced 31 Dec 2024, effective **16 Mar 2025**. A lighter regime for passive-only AMCs (index funds, ETFs, FoFs), with relaxed sponsor net worth (reported ₹35 cr vs ₹50 cr). — [The Week](https://www.theweek.in/news/biz-tech/2025/01/01/all-about-sebi-s-mf-lite-framework-key-provisions-who-benefits-and-more-details.amp.html); [Groww](https://groww.in/blog/sebi-introduces-mutual-funds-lite)
- **SIF:** amendment notified 16 Dec 2024, framework circular 27 Feb 2025, live **1 Apr 2025**. Minimum **₹10 lakh per investor per AMC across SIF strategies** (accredited investors exempt). Strategies include equity long-short and sector rotation. Uptake: about ₹13,814 cr AUM and 56,000 folios across 21 strategies within months. — [Business Standard Dec 2024](https://www.business-standard.com/amp/finance/personal-finance/sebi-rolls-out-specialised-investment-fund-for-hnis-with-rs-10-lakh-minimum-124121800227_1.html); [Business Standard Feb 2025](https://www.business-standard.com/amp/markets/capital-market-news/sebi-unveils-regulatory-framework-for-specialized-investment-funds-125022800173_1.html); [Kotak Neo](https://www.kotakneo.com/news/regulations/specialised-investment-funds-13814-crore-aum-sebi-2026/)

### Inferences
- MVP fund-comparison features must label expense data as TER (pre-Apr 2026) or BER (post-Apr 2026). The removal of solution-oriented categories affects goal-based "retirement fund" recommendations.
- SIFs are distributed by MFDs (which reportedly need additional NISM certification) and are a likely HNI upsell, but they are out of scope for a mass-market MVP.

### Gaps
- No SEBI primary notification for the 2026 MF Regulations was retrieved; all figures are from secondary explainers.
- The exact BER slab table for active equity funds was not retrieved.

---

## Summary matrix (synthesised from the above; see inline citations)

| Product type | Minimum registration | Key constraints | Indicative cost / time |
|---|---|---|---|
| Education chatbot (generic concepts, no scheme picks for a user) | None | No security-specific recommendations; no return claims; 3-month-old data for stock-specific examples (Jan 2025 circular benchmark); cannot be paid by regulated entities if it drifts into advice (Aug 2024 association ban) | ₹0 regulatory |
| Personalised fund recommendation / advice | SEBI IA (individual or non-individual) | Fee cap ₹1.51 lakh/family or 2.5% AUA; no distribution commissions for the same family/group; AI disclosure and sole liability; risk profiling and suitability; annual audit | ~₹5k SEBI fees + ₹1 lakh deposit (≤150 clients); IAASB processing (no official SLA; 21–90 days indicative) |
| Execution of direct-plan MF transactions | RIA (own clients, BSE StAR MF, nil membership fee) **or** Cat-1 EOP (AMFI, ₹1 cr net worth, ≤₹2/txn) **or** Cat-2 EOP (broker, ₹10 lakh BMC) | No pooling; payment from investor's verified bank account; no ads (EOP); no advice (EOP) | RIA cheapest; EOP needs ₹1 cr+ |
| Execution of regular plans (commission model) | AMFI ARN + EUIN (NISM V-A) + AMC empanelment; BSE/NSE/MFU membership | Cannot advise for a fee to the same family; no "adviser" naming | Low; fees not found |
| Portfolio tracking | None for CAS-upload parsing; regulated licence (e.g. RIA) to be an AA FIU | MF Central third-party pulls curtailed (Sep–Nov 2025); DPDP obligations from May 2027 | AA: ₹5–25 lakh / 5–10 months (vendor estimate) |
| AI agent placing orders (never touching money) | RIA (MF via BSE StAR MF) or broker; for equities algo, broker + exchange-registered algo (Feb 2025 framework, fully live Apr 2026) | RIA per-trade explicit consent; SEBI AI liability; forthcoming tiered AI rules (human oversight, kill switch) | As RIA, plus engineering for consent logging |
