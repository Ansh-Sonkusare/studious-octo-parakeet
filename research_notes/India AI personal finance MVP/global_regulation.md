# Global Regulation of AI-Delivered Financial Guidance, Advice and Agent-Executed Transactions (as of 7 Oct 2026)

Method note: research was done via web search tools that return summarised results; I could not open most primary regulator PDFs. Each finding is tagged [IN FORCE], [PROPOSAL/PENDING] or [GUIDANCE] where the status is clear. Where sources are consultancy/vendor marketing (low quality) I say so. Nothing here is legal advice. India is not researched here (covered separately).

---

## 1. United States: advice, broker-dealer, AI rules, open banking, money transmission, publisher exclusion

### Takeaway
The US has no AI-specific financial-advice rule: the SEC's proposed predictive-analytics rule was withdrawn (June 2025), so AI is policed through existing Advisers Act fiduciary duty, marketing/"AI washing" enforcement, exam priorities and FINRA's technology-neutral guidance. A startup giving personalised AI advice must register as an RIA (state-level for small firms; SEC only if it fits the narrowed internet-adviser exemption or has more than ~$100-110M AUM), while impersonal, non-tailored education can plausibly rest on the Lowe publisher's exclusion. The CFPB 1033 open-banking rule is enjoined and being rewritten, so data access still depends on private aggregator contracts.

### Cited Findings

**SEC investment adviser registration (state vs SEC)**
- [IN FORCE] An adviser must register with the SEC at $110M+ AUM; advisers with $100-110M may choose; must also register with the SEC at $25M+ if principal office is in a state that exempts advisers or does not examine them (New York is the one cited). Below that, advisers are generally state-registered. — [Kitces / secondary summary](https://www.kitces.com/blog/switching-between-state-and-sec-registration-100-million-raum-threshold-ria/) (the search summary itself flagged the $90M "buffer" detail as unconfirmed against rule text)
- [IN FORCE] Internet adviser exemption (Rule 203A-2(e)) amended 27 March 2024: de minimis exception for <15 non-internet clients eliminated; adviser must maintain an operational interactive website at all times and advise exclusively through it; human-directed, client-specific advice delivered electronically is not eligible. Effective 8 July 2024; compliance date 31 March 2025; advisers that no longer qualified had to leave SEC registration (Form ADV-W) by 29 June 2025. New robo-advisers registering after 8 July 2024 must comply from inception. — [Federal Register, 9 Apr 2024](https://www.govinfo.gov/content/pkg/FR-2024-04-09/html/2024-06865.htm); [K&L Gates](https://www.klgates.com/The-SEC-Limits-the-Internet-Adviser-Exemption-4-15-2024); [ACA Group](https://acaglobal.com/insights/changes-sec-robo-adviser-exemption/)
- [IN FORCE] State filing costs are small: state IA registration/notice-filing fees on average $50-$500 (e.g. Louisiana $150, Delaware $250, Alabama $250 + $70/rep, Kentucky $100 + $50/rep); IAR fees roughly $10-$285 per rep per year; registrations expire 31 Dec annually. — [RIA Compliance Consultants](https://ria-compliance-consultants.com/?p=1121) and state regulator pages (e.g. [Alabama](https://asc.alabama.gov/for-industry/registration/investment-advisers-notice-filing/)). Sources partly dated (2012-2015 packets).
- [IN FORCE, varies by state] Net worth/bond rules follow the principal-office state: examples Kentucky $10,000 (discretion, no custody, <$25M AUM) and $35,000 with custody (surety bond can cover part); South Carolina $35,000 discretion / $50,000 custody; Virginia >$25,000 net worth or $25,000 surety bond; some states require bonds up to $50,000. Robo-advisers often have discretion, which triggers the higher tier. — [NASAA Kentucky](https://www.nasaa.org/industry-resources/investment-advisers/state-investment-adviser-registration-information/kentucky/); [S.C. Code Regs 13-406](https://www.law.cornell.edu/regulations/south-carolina/R-13-406); [Va. 21VAC5-80-180](https://www.law.cornell.edu/regulations/virginia/21VAC5-80-180)
- Time-to-register: one practitioner describes SEC approval under 30 days for qualifying internet advisers; I found no benchmark for state review times (ACA/RIA-compliance commentary: [ACA Group](https://www.acaglobal.com/industry-insights/changes-sec-robo-adviser-exemption/)). Treat as unverified.
- [IN FORCE] Amended Regulation S-P (privacy/incident response): compliance 3 Dec 2025 for advisers with $1.5B+ AUM, 3 June 2026 for smaller advisers; 30-day customer breach notification. — [Rimon Law](https://www.rimonlaw.com/amended-regulation-s-p-is-now-fully-in-effect-and-yes-it-applies-to-private-fund-managers/); [Kroll](https://www.kroll.com/en/publications/financial-compliance-regulation/regulation-s-p-amendments)

**SEC AI-specific posture**
- [WITHDRAWN] The SEC withdrew 14 pending proposals on 12 June 2025, including the July 2023 predictive data analytics (PDA) conflicts rule for broker-dealers and advisers; any revival requires a fresh proposal. Underlying conflict-of-interest duties remain and staff may raise PDA issues in exams. — [Paul Hastings](https://www.paulhastings.com/insights/client-alerts/sec-withdraws-14-pending-rule-proposals); [Ocorian](https://www.ocorian.com/knowledge-hub/insights/sec-proposed-rule-withdrawals-what-14-withdrawn-rules-signal-regulatory)
- [ENFORCEMENT] "AI washing": March 2024 settled actions vs Delphia ($225,000) and Global Predictions ($175,000) for false AI claims (Global Predictions advertised a chatbot that gave no recommendations); Nov 2024 settled action vs an investment company/adviser/CEO/board member (CEO >$460k total plus 5-year industry bar; board member $60k). — [MoFo](https://mofo.com/resources/insights/240320-sec-targets-ai-washing-with-two-new-settled-cases); [Seward & Kissel](https://40actblog.sewkis.com/blog/sec-charges-investment-company-ceo-and-board-member-for-alleged-misleading-statements-regarding-use-of-artificial-intelligence). I did not find any 2026 SEC AI-washing adviser settlement in search results (gap).
- [GUIDANCE] SEC Division of Examinations 2026 priorities (released ~17 Nov 2025): automated investment tools, AI technologies, accuracy of AI-capability representations, and policies to supervise AI use; AI treated as a cross-cutting risk with cybersecurity/Reg S-P and S-ID. — [Foley](https://www.foley.com/insights/publications/2025/12/sec-releases-its-2026-examination-priorities/); [Debevoise](https://www.debevoise.com/insights/publications/2025/11/2026-sec-division-of-examinations-priorities)

**FINRA / broker-dealer**
- [GUIDANCE] FINRA Regulatory Notice 24-09 (27 June 2024): existing rules apply to generative AI/LLMs; no new requirements; e.g. Rule 2210 content standards apply whether a human or tool writes the communication. — [FINRA RN 24-09](https://finra.org/sites/default/files/2024-06/regulatory-notice-24-09.pdf); [Mayer Brown](https://www.mayerbrown.com/en/insights/publications/2024/07/finra-reminds-members-of-regulatory-obligations-when-using-generative-artificial-intelligence-ai-and-large-language-models)
- [GUIDANCE] FINRA 2026 Annual Regulatory Oversight Report (9 Dec 2025): expanded GenAI section and, for the first time, AI-agent risks (action tracking, access restrictions, hallucination/bias governance). Not binding, but exam findings draw on it. — [Debevoise](https://www.debevoise.com/insights/publications/2025/12/finras-2026-regulatory-oversight-report-continued); [Sidley](https://datamatters.sidley.com/2025/12/16/finra-issues-2026-regulatory-oversight-report/)
- Broker-dealer registration cost/time and net capital: not retrieved (gap). Practical alternative is partnering with an existing broker-dealer/custodian so the startup never executes or holds.

**Publisher's exclusion (Lowe v. SEC) for AI education**
- [CASE LAW] Lowe v. SEC (1985): impersonal, non-tailored, bona fide newsletters of general and regular circulation fall outside the Advisers Act "investment adviser" definition; Congress targeted personalised, person-to-person advice. — [Greenberg Traurig](https://www.gtlaw.com/en/insights/2024/8/no-need-for-seeking-alpha-to-seek-registration); [Casemine](https://www.casemine.com/commentary/us/exclusion-of-bona-fide-investment-publications-from-the-investment-advisers-act:-lowe-v.-sec/view)
- Seeking Alpha (federal court, 15 Aug 2024) applied the exclusion and declined a narrow reading; "bona fide" excludes promotional touting and false/misleading content. — [Greenberg Traurig](https://www.gtlaw.com/en/insights/2024/8/no-need-for-seeking-alpha-to-seek-registration)
- No case found applying Lowe to an AI chatbot (the tool's own search summary stated that conclusion is inference). SEC has treated robo-advisers as advisers since ~2017. — [search synthesis; GT link above]

**CFPB 1033 (open banking)**
- [ENJOINED / UNDER RECONSIDERATION] Final rule Oct 2024 with compliance dates 1 Apr 2026 to 1 Apr 2030; E.D. Ky. enjoined enforcement on 29 Oct 2025 (court found plaintiffs likely to succeed on statutory-authority claim); CFPB issued ANPR Aug 2025 (who is a "representative", data-access fees, security) and sent a reconsideration NPRM to OIRA on 6 Aug 2026; no published NPRM confirmed; commentary expects fees to be allowed and the authorised-representative standard tightened (prediction, not text). — [Cozen O'Connor](https://www.cozen.com/news-resources/publications/2026/section-1033-compliance-date-open-banking-rule-enjoined-and-under-reconsideration); [Risk Template (28 Sep 2026, lower-quality blog)](https://risktemplate.com/blog/2026-09-28-cfpb-section-1033-rewrite-data-access-fees-open-banking-fintech-2026/); [Moore & Van Allen](https://www.mvalaw.com/data-points/cfpb-enjoined-from-enforcing-personal-financial-data-rights-rule-1033)

**Money transmission**
- [IN FORCE, state-by-state] Money transmitter licensing is state-level (about 50 regimes). An "agent of the payee" exemption exists in many states but counts conflict (one source ~39 states, another ~22 explicit + 3 case-by-case); conditions include a written agreement, holding out as payee's agent, and payment deemed received by payee on receipt; Vermont exempts neither processors nor payee agents. — [Modern Treasury](https://moderntreasury.com/learn/what-is-an-agent-of-the-payee-exemption); [Private.law wiki (secondary)](https://wiki.private.law/en/money-transmitter-license-usa.md)
- Maryland treats covered payment handling (incl. bill-pay) as money transmission from 1 Oct 2026. — [PolicyRisk, MD HB0118/SB0261 (2026)](https://policyrisk.com/state-bill/MD-HB0118-2026RS) (bill tracker; verify enactment)
- A consumer-side agent paying on behalf of the payor is outside the payee-agent exemption; no source found directly addressing AI agents (the research tool labelled this its own reasoning). — [Modern Treasury link above]

**State AI laws / federal preemption**
- Colorado: original AI Act (delayed to 30 June 2026) replaced by SB 26-189 (signed mid-May 2026), a narrower automated-decision-making law effective 1 Jan 2027 (subject to an x.AI challenge and AG rulemaking); it removed the original conditional exemptions for some federally regulated entities. — [Consumer Finance Monitor](https://www.consumerfinancemonitor.com/2026/05/12/colorado-rewrites-its-landmark-ai-law-unpacking-sb-26-189-and-what-it-means-for-businesses/); [Mayer Brown](https://www.mayerbrown.com/ja/insights/publications/2026/05/colorado-enacts-new-admt-law-replacing-colorado-ai-act)
- Executive Order 11 Dec 2025 "Ensuring a National Policy Framework for AI": DOJ AI Litigation Task Force (from 10 Jan 2026) to challenge state AI laws; calls for federal preemption legislation; state laws remain in effect meanwhile. — [Gibson Dunn](https://www.gibsondunn.com/president-trump-latest-executive-order-on-ai-seeks-to-preempt-state-laws/)

### Inferences
- Lowest-friction US path: (a) AI education that is impersonal and not tailored to the user's own holdings can plausibly rely on Lowe, but anything that ingests a user's accounts and says "you should buy X" is the Advisers Act's core; the line is fact-specific and untested for LLMs. (b) Personalised advice: state RIA (small firm, low fees, modest net worth/bond) is cheap in dollars; the real costs are compliance programme, ADV/brochure, fiduciary duty/conflict controls and AI-claim substantiation. Internet-adviser exemption is available only if advice is fully automated through an interactive site (human-directed advice disqualifies). (c) For agent-executed investment/payments with no fund custody, the startup should avoid being the party that "receives" money (use a licensed broker/custodian and bank/PISP-style aggregator) and expect a state-by-state money transmission analysis if any funds pass through it.
- With no active 1033 rule, US data access relies on aggregator contracts (Plaid-type); the pending rewrite may allow bank fees, raising cost risk.
- Colorado SB 26-189 (1 Jan 2027) is the main US state-law AI exposure to watch for credit/lending-related automated decisions; less relevant to pure investing/budgeting.

### Gaps
- Primary-source SEC/FINRA texts were not opened; FINRA broker-dealer cost/time not found; no verified state processing times; no 2026 SEC AI enforcement found; status of any SEC "AI task force"/new AI guidance in 2026 not checked; Seeking Alpha appeal status unchecked; CFPB NPRM publication status unconfirmed as of Oct 2026.

---

## 2. United Kingdom: FCA advice vs guidance, targeted support, AI posture, sandboxes, open banking/payments

### Takeaway
The UK is the most active jurisdiction for lowering the cost of mass-market AI-delivered "advice-lite": the targeted support regime went live on 6 April 2026 (needs Part 4A permission, no appointed representatives at launch), the FCA runs AI Live Testing and a Supercharged Sandbox, and the July 2026 Mills Review recommends no new AI-specific rules while promising a perimeter review. Authorisation itself is slow-ish (statutory 6 months for a complete application) but fees are modest; agentic payments are an acknowledged open question being consulted on now.

### Cited Findings
- [IN FORCE from 6 April 2026] Targeted support: FCA Board made final rules 26 Feb 2026 (PS25/22 near-final 11 Dec 2025; announced as final 2 Mar 2026); a new regulated activity requiring a Part 4A permission (variation or new application); gateway opened 2 March 2026 via Connect; firms define pre-defined "situations" and consumer segments and suggestions are assessed against common characteristics of a segment; FCA/FOS complaints handled under DISP; free voluntary Pre-Application Support Service (PASS); post-implementation review within two years. — [Freshfields](https://www.freshfields.com/en/our-thinking/blogs/risk-and-compliance/fca-finalises-targeted-support-rules-applications-now-open-102mmq0); [FCA PS25/22](https://www.fca.org.uk/publications/policy-statements/ps25-22-supporting-consumers-pensions-investment-decisions-rules-targeted-support); [Burges Salmon](https://www.burges-salmon.com/articles/102mohl/targeted-support-goes-live-on-6-april-2026-what-you-need-to-know)
- Appointed representatives cannot deliver targeted support at launch (FCA working assumption / HMT decision). — [Burges Salmon](https://www.burges-salmon.com/articles/102mohl/targeted-support-goes-live-on-6-april-2026-what-you-need-to-know); [search synthesis of PS25/22 coverage](https://www.aoshearman.com/en/insights/fca-ps25-22-fcas-new-targeted-support-regime-snapshot)
- At consultation stage targeted support could be free or charged; commissions not allowed (confirm in final PS25/22). — [CMS](https://cms.law/en/gbr/legal-updates/targeted-support-consultation-heralds-new-era-for-advice-options2) (consultation-stage source)
- [PROPOSAL] CP26/10 (25 Mar 2026): simplify investment/pensions advice rules (merge COBS 9/9A into COBS 9C; replace mandatory annual review with periodic firm-determined review; keep RDR charging/qualification rules; explicitly not a bespoke "simplified advice" regime). Responses closed 22 May 2026; policy statement expected Q4 2026. — [FCA CP26/10](https://www.fca.org.uk/publications/consultation-papers/cp26-10-simplifying-pensions-investment-advice-rules); [Simmons & Simmons](https://www.simmons-simmons.com/en/publications/cmoip0ucj016yukkkiqgaltnu/cp26-10-simplifying-the-pensions-and-investment-advice-rules)
- [GUIDANCE] Mills Review on AI in retail financial services published 6 July 2026: concludes existing framework (Consumer Duty, SM&CR) remains fit for purpose, no new AI-specific rules; seven recommendations including an FCA perimeter review within 3-6 months covering general-purpose LLMs operating outside the perimeter; Consumer Duty/SMCR to be clarified for autonomous AI; "good and poor practice" AI publication due later in 2026. — [FCA Mills Review](https://www.fca.org.uk/publications/corporate-documents/mills-review); [Regulation Tomorrow](https://www.regulationtomorrow.com/2026/07/fca-publishes-mills-review-into-ai-and-the-future-of-retail-financial-services/); [A&O Shearman](https://finreg.aoshearman.com/mills-review-sets-out-recommendations-to-the-fca-on-ai-and-the-future-of-retail-financial-services) (some detail from vendor blog Aveni; verify in FCA text). Earlier FCA stance: no additional AI-specific rules planned — [Financial Planning Today](https://www.financialplanningtoday.co.uk/news/no-ai-related-rules-to-come-from-fca)
- FCA research cited by commentary: only ~40% understand there is no formal recourse when relying on a general-purpose chatbot (secondary citation). — [Aveni summary of Mills](https://aveni.ai/blog/mills-review-takeaways/) (vendor; low-confidence)
- [SANDBOX] FCA AI Live Testing: cohort 1 (from Dec 2025) incl. NatWest, Monzo, Santander, Scottish Widows, Gain Credit, Homeprotect, Snorkl, focused on retail use cases incl. financial advice and debt resolution; cohort 2 announced 21 Apr 2026 (8 firms: Barclays, Experian, Lloyds, UBS, Coadjute, GoCardless, Palindrom, Aereve) incl. AI-enabled targeted support for investments, credit-score insights, agentic payments, AML/KYC; testing ends end-2026, evaluation report Q1 2027; assurance partner Advai. — [Mortgage Solutions, 21 Apr 2026](https://www.mortgagesolutions.co.uk/mortgage-news/2026/04/21/fca-to-assess-good-and-bad-use-of-ai-as-barclays-and-lbg-join-second-test-programme/); [Fintech Global](https://fintech.global/2025/12/04/fca-begins-live-ai-testing-with-major-uk-banks/); [FCA press release](https://www.fca.org.uk/news/press-releases/fca-helps-firms-test-ai-safely/printable/print)
- [SANDBOX] Supercharged Sandbox (with NVIDIA; launched June 2025) is for discovery/experimentation (GPU cloud, datasets, expert support); 2025 round ran late Sep 2025 to early Jan 2026; no 2026 intake found. — [FCA Supercharged Sandbox](https://www.fca.org.uk/firms/innovation/supercharged-sandbox); [Mortgage Solutions](https://www.mortgagesolutions.co.uk/mortgage-news/2025/06/09/fca-launches-sandbox-to-allow-firms-to-experiment-with-ai/)
- [IN FORCE] FCA must determine a complete Part 4A application within 6 months (12 months if incomplete); application fees range from £280 (cat 1) to ~£222,940-£225,170 (cat 10) — two FCA page versions disagree; fees non-refundable; 2026/27 fee rates in PS26/14 (2 Jul 2026) not read. Commentary (consultancy) puts well-prepared straightforward applications at 3-4 months — treat as non-authoritative. — [FCA operating metrics 2025-26](https://www.fca.org.uk/data/fca-operating-service-metrics-2025-26/enabling-business-preventing-harm/printable/print); [FCA fees page](https://www.fca.org.uk/firms/authorisation/apply/fees); [PS26/14](https://www.fca.org.uk/publications/policy-statements/ps26-14-fca-regulated-fees-and-levies-2026-27)
- AISP (account information, "RAISP") fee is Category 3 and PISP small PI Category 3 (authorised PI Cat 4/5); £ amounts not retrieved. — [FCA fees page](https://www.fca.org.uk/firms/authorisation/apply/fees)
- [CONSULTATION] Agentic payments: FCA 2026 Payments Regulatory Priorities (25 Mar 2026) says it will consider whether regulation needs to change to support agentic AI payments; HM Treasury published a Financial Services AI Adoption Plan and a payments-modernisation consultation on 14 July 2026 (one source says consultation closes 6 Oct 2026; it proposes a "Know Your Agent" standard and an agentic payments trust framework); PSRs 2017 require payer consent to each transaction or defined series, an awkward fit for agent discretion; Consumer Duty may apply to firms that fail to adapt fraud controls. — [Payment Expert](https://paymentexpert.com/2026/03/25/fca-2026-payments-regulatory-priorities-report/); [Bratby Law](https://bratby.law/agentic-ai-payments-consent-regulation/); [Finexer (vendor blog)](https://blog.finexer.com/?p=35913); [Freshfields, May 2026](https://www.freshfields.com/ja/our-thinking/briefings/2026/05/agentic-ai-in-the-payments-chain-regulatory-challenges-for-financial-institutions)
- Existing UK firms: Plum (Saveable Ltd, FRN 739214), Moneybox (Digital Moneybox Ltd, FRN 712935), Nutmeg (J.P. Morgan Personal Investing Ltd, FRN 552016) are FCA-authorised investment firms; Cleo is regulated for payment services (its AI coach legal status unclear from sources); Scottish Widows is piloting an AI investment guidance tool framed as guidance not advice. — [Plum](https://withplum.com/legal/money-protections); [Moneybox](https://support.moneyboxapp.com/terms-and-conditions/); [FCA clone warning (Nutmeg)](https://www.fca.org.uk/news/warnings/nutmeg-easy-invest-nutmegeasyinvestcom-clone-fca-authorised-firm); [Money to the Masses on Cleo](https://moneytothemasses.com/banking/cleo-review-the-ai-chatbot-that-manages-your-money-for-you); [Financial Reporter on Scottish Widows](https://www.financialreporter.co.uk/fca-chooses-next-cohort-of-firms-for-live-ai-testing.html)

### Inferences
- UK "guidance" (generic information, no personal recommendation) needs no authorisation; this is the lowest-friction product, and the FCA's own stance (and Scottish Widows' pilot) supports it. Moving to personalised segment-level suggestions needs a Part 4A targeted-support permission, which is far cheaper than full advice (no individual suitability per client) and has PASS support, but ARs cannot yet use it, so a startup must be directly authorised (cost is time: statutory up to 6 months, plus Consumer Duty and SM&CR set-up).
- The Mills perimeter review (due roughly Oct 2026-Jan 2027 on the 3-6 month recommendation) is a live risk/opportunity for LLM products sitting outside the perimeter.
- For agent-executed payments without holding funds, a UK startup would likely need AISP/PISP-type registration or authorisation, and regulation of agent consent is in flux (consultation ongoing).

### Gaps
- Did not open PS25/22 text: unknown whether automated/AI delivery of targeted support is expressly allowed or restricted; no confirmed application fee/time for targeted support permission; UK Open Banking/Open Finance (Data (Use and Access) Act 2025, Smart Data, FCA open finance plans) not researched; no confirmed 2026 Supercharged Sandbox intake; FCA sandbox alumni specific to AI advice start-ups not identified.

---

## 3. European Union: MiFID II, AI Act, PSD3/PSR, FiDA, data transfers

### Takeaway
In the EU, personalised investment recommendations are MiFID II "investment advice" needing national authorisation (initial capital EUR 75,000 if no client assets; 6-month statutory decision window), with ESMA saying AI use does not dilute management-body accountability or best-interest duties. The AI Act's high-risk (Annex III, creditworthiness) obligations have been pushed to 2 Dec 2027 by the AI Omnibus, but transparency (Art. 50) and AI-literacy duties are earlier; PSD3/PSR is agreed in text but not yet applying, and FiDA is unresolved.

### Cited Findings
- [IN FORCE] MiFID II Art. 7(3): applicant informed within six months of a complete application; Art. 74 gives a right of appeal if no decision within six months; national law may be faster (Bulgaria example: 3 months from confirmed completeness). Initial capital: EUR 75,000 for advice where firm holds no client money; EUR 150,000 if it holds client assets; EUR 750,000 for dealing on own account etc. — [ESMA Interactive Single Rulebook Art. 7](https://www.esma.europa.eu/publications-and-data/interactive-single-rulebook/mifid-ii/article-7-procedures-granting-and); [Private.law MiFID wiki (secondary)](https://wiki.private.law/en/mifid-investment-firm)
- [GUIDANCE] ESMA Public Statement on AI and investment services (30 May 2024): MiFID II organisational, conduct and best-interest duties apply; management body remains responsible for AI-driven decisions; clients should be told about AI's role; risks cited include bias, opacity and over-reliance. — [ESMA statement](https://www.esma.europa.eu/sites/default/files/2024-05/ESMA35-335435667-5924__Public_Statement_on_AI_and_investment_services.pdf); [Regulation Tomorrow](https://www.regulationtomorrow.com/2024/05/esma-issues-initial-guidance-for-firms-using-ai-in-investment-services/). No standalone 2026 ESMA AI statement found.
- [IN FORCE then AMENDED] AI Act Digital Omnibus: provisional agreement 6/7 May 2026 (after 28 Apr trilogue collapse); Council formally adopted 29 June 2026 (Official Journal publication date not confirmed in my sources; one expected 18-25 July 2026). New dates: Annex III stand-alone high-risk (incl. creditworthiness assessment) moved from 2 Aug 2026 to 2 Dec 2027; Annex I product-embedded high-risk to 2 Aug 2028; Art. 50 transparency still 2 Aug 2026 (existing systems get until 2 Dec 2026 for the Art. 50(2) watermarking duty); AI literacy (Art. 4) applies since 2 Feb 2025 but softened; GPAI obligations since 2 Aug 2025; national AI sandboxes deadline moved to 2 Aug 2027. — [Gibson Dunn (pre-adoption alert)](https://www.gibsondunn.com/eu-ai-act-omnibus-agreement-postponed-high-risk-deadlines-and-other-key-changes/); [Addleshaw Goddard, 1 Jul 2026](https://www.addleshawgoddard.com/en/insights/insights-briefings/2026/technology/eu-ai-act-ai-omnibus-formally-adopted/); [Linklaters](https://techinsights.linklaters.com/post/102ms10/omnibus-agreement-how-the-eu-ai-act-changes). Source conflict: Winston & Taylor shows Annex I as 2 Aug 2026, which appears a typo vs 2028 elsewhere.
- One law firm view: the AI Act is "largely inapplicable" to MiFID-licensed advice firms because advice is not an Annex III use case; creditworthiness scoring of natural persons is Annex III. — [Mamo TCV](https://www.mamotcv.com/insights/ai-investment-services-mifid-considerations/) (single-firm view; verify)
- [PENDING] PSD3/PSR: provisional deal 27 Nov 2025; COREPER endorsed 22 Apr 2026; final texts published 23 Apr 2026; ECON approved 5 May 2026 (tracker); plenary/Council votes and OJ publication pending in my sources; application roughly 18-21 months after entry into force (sources conflict), so ~2028; extends liability to technical service providers/wallets. — [Worldline](https://worldline.com/en/home/main-navigation/resources/blogs/2026/the-scope-and-timeline-are-locked-in-for-psd3-and-psr-what-should-psps-know); [Taylor Wessing](https://www.taylorwessing.com/en/insights-and-events/insights/2025/11/eu-lawmakers-strike-a-deal-on-payments-reforms)
- [PENDING / UNCLEAR] FiDA: Commission signalled in Feb 2025 it would drop it, reversed within days; in May 2025 a streamlined non-paper excluded firms with turnover >EUR 50M; trilogues began; no primary 2026 status found. — [Vixio](https://www.vixio.com/insights/pc-fida-lives-see-another-day-european-commission-backs-away); [Fiskil tracker (commercial)](https://www.fiskil.com/open-finance-tracker/standard/fida)
- [IN FORCE] PSD2 applies to agent-initiated payments (technology-neutral); payment initiation requires PSP authorisation, AISP-only firms are registered not authorised; firms supplying only technical infrastructure and never holding funds may fall outside licensing; SCA is tied to a human, which fits poorly with delegation to agents; no EBA position yet. — [Taylor Wessing, Feb 2026](https://www.taylorwessing.com/en/insights-and-events/insights/2026/02/agentic-ai-in-payments); [Osborne Clarke](https://www.osborneclarke.com/pl/insights/agentic-payments-nowe-wyzwanie-dla-europejskiego-ekosystemu-platniczego)

### Inferences
- A US/UK/Indian startup cannot serve EU users with personalised investment recommendations from outside without MiFID authorisation (or a third-country route); EU "education only" content is much lower risk. The AI Act delay gives roughly 14 months extra for credit-scoring-type features; budgeting/spending coaching is not obviously Annex III, but any creditworthiness evaluation would be.
- EU authorisation via a smaller member state is the cheapest EU route (EUR 75k capital for advice-only), but timing is 3-6+ months and national practice varies.

### Gaps
- AI Act penalty amounts and exact Official Journal date not confirmed; exact MiFID capital/time per member state not verified in primary law (IFD text not read); FiDA 2026 status unverified; no research on EU regulatory sandboxes under AI Act (national deadline now 2 Aug 2027) or on DORA third-party ICT obligations.

---

## 4. Other major jurisdictions

### 4a. Singapore (MAS)

### Takeaway
Singapore has the clearest, longest-standing digital-adviser framework and an explicit AI risk programme, plus a 21-day Sandbox Express, but the licence capital is higher than the US/UK/EU small-firm routes (S$300-500k base capital for most advisory activity).

### Cited Findings
- [IN FORCE] MAS licensing page: base capital for financial advisory activity S$500,000 (or S$300,000 plus S$500,000 professional indemnity cover); research-only advisers S$250,000; financial-resources test higher of 1/4 relevant annual expenditure or S$150,000. — [MAS financial adviser licence](https://www.mas.gov.sg/regulation/capital-markets/apply-for-licensing-or-registration-of-capital-market-entities/financial-advisers)
- [IN FORCE since 2017-18] Digital advisory guidelines: robo-advisers need licences by operating model (FA, fund management, CMS dealing); relief from collecting the full client financial profile if unsuitability risks are mitigated; relief from SFA track-record requirement for retail fund management if conditions met (experienced board/senior management, simple CIS-only portfolios, independent audit after year one); can pass orders to brokers without another CMS licence; board/senior management must govern algorithms. — [Wealth Briefing Asia](https://www.wealthbriefingasia.com/article.php/MAS-issues-guidelines-for-providers-of-digital-advisory-services); [Conventus Law](https://conventuslaw.com/report/singapore-eases-robo-advice-eligibility/); [Pinsent Masons](https://pinsentmasons.com/out-law/news/singapore-eases-robo-advice-eligibility-regulations). Dated sources; confirm current text.
- [GUIDANCE] FEAT principles (2018); Veritas Initiative (2019); open-source Veritas Toolkit 2.0 (26 Jun 2023). — [Rajah & Tann](https://www.rajahtannasia.com/viewpoints/mas-publishes-toolkit-for-responsible-use-of-ai-in-financial-sector/); [Fintech Global](https://fintech.global/?p=121990)
- [PROPOSAL] MAS Guidelines on AI Risk Management: consultation 13 Nov 2025 to 31 Jan 2026; covers generative AI and AI agents; proportionate; higher-risk uses (e.g. credit) get stricter controls; proposed 12-month transition after issuance; no final guidelines found as of my searches. MAS launched an AI Risk Management Toolkit/Operationalisation Handbook on 20 Mar 2026 (developed with 24 firms). — [Linklaters](https://techinsights.linklaters.com/post/102lw91/singapore-mas-proposes-comprehensive-ai-risk-management-guidelines-for-financial); [Hogan Lovells](https://www.hoganlovells.com/en/publications/from-principles-to-practice-maturing-ai-supervision-in-singapores-financial-sector); [Rahmat Lim](https://www.rahmatlim.com/sg/publication/articles/32836/mas-launches-ai-risk-management-toolkit-for-financial-services-sector)
- [SANDBOX] Sandbox Express launched 7 Aug 2019: MAS targets response within 21 days of a complete application; experiments up to 9 months; launch scope was insurance brokers, recognised market operators and remittance (robo-advisory not confirmed in scope). — [Allen & Gledhill](https://www.allenandgledhill.com/sg/perspectives/articles/13314/mas-launches-sandbox-express-for-faster-market-testing-of-innovative-financial-services-and-products)
- StashAway is a known Singapore robo-adviser (mentioned in results) — [StashAway](https://www.stashaway.ae/r/stashaway-raises-sdollar-3-million-in-pre-series-a-fundraising); licence details not retrieved.

### Inferences
- Singapore is credible for personalised AI advice (clear rules, good regulator engagement) but not the cheapest; the AI Risk Management Guidelines will land as supervisory expectations (12-month transition).

### Gaps
- FAA exemptions for small/foreign advisers, licence timeline, sandbox acceptance of AI advice, and final status of the AI guidelines were not confirmed.

### 4b. UAE (DIFC/DFSA, ADGM/FSRA)

### Takeaway
The UAE offers sandbox-style routes (DFSA Innovation Testing Licence; ADGM RegLab) and a robo-adviser precedent, but cost and capital figures in public sources conflict badly and many come from consultancy marketing.

### Cited Findings
- DFSA ITL application page lists a USD 5,000 service fee for a restricted testing licence; testing subject to caps on client numbers/types and transaction limits (law-firm commentary); capital and timing figures from consultancies conflict (AED 100k-500k; 12 months vs up to 2 years). — [DFSA ITL page](https://services.dfsa.ae/services/crypto-and-innovation-innovation/request-for-Innovation-testing-license); [Neolegal](https://neolegal.ae/insights/dfsa-innovation-testing-licence-itl-difc)
- DFSA Cat 4 (advising) capital figures conflict (USD 10k older guide; USD 30k to 140k in a 2026 guide; USD 70k elsewhere); DFSA moved to an activity-based capital requirement. — [Salvus Funds, 2026](https://salvusfunds.com/2026/04/14/establishing-a-dfsa-category-3a-and-category-4-licence-in-dubai-in-2026/) (consultancy; verify in DFSA rulebook)
- ADGM FSRA issued robo-adviser/digital investment management guidance (algorithm integrity, human oversight, explainability; reduced prudential capital possible if criteria met; secondary newsletter cites USD 250k for managing assets, USD 50k for other Cat 4). — [Fintech Futures](https://www.fintechfutures.com/regulatory-actions/adgm-issues-robo-advisor-regulatory-framework); [The Riffle](https://riffle.beehiiv.com/p/regulatory-framework-for-digital-investment-management-in-adgm)
- Sarwa was the first graduate of the DFSA regulatory sandbox (robo-advisory). — [DFSA](https://www.dfsa.ae/news/robo-advisory-firm-sarwa-first-graduate-dfsas-regulatory-sandbox)
- DFSA AI survey (2025 edition): 52% of firms use AI vs 33% in 2024; 21% lack clear accountability. — [DFSA](https://www.dfsa.ae/news/new-dfsa-ai-survey-generative-ai-adoption-has-nearly-tripled-within-difc-last-12-months-governance-continues-develop)

### Inferences
- UAE is a plausible sandbox-first route for a pilot; real costs need DFSA/FSRA confirmation. VARA (virtual assets) was not researched; it matters only if crypto assets are in scope.

### Gaps
- No primary DFSA/FSRA fee schedule or capital figures; no ADGM RegLab primary source; no AI-specific DFSA/FSRA rule found; VARA not covered.

### 4c. Hong Kong (SFC)

### Takeaway
Hong Kong requires a Type 4 (advising on securities) and/or Type 9 (asset management) licence with realistic timelines of about 4-6 months; the SFC has robo-advice guidelines (2019) and a mandatory GenAI circular (2024) that classes AI-generated investment advice as high risk, and the SFC says most robo-advisers should skip the sandbox.

### Cited Findings
- [IN FORCE from 6 Apr 2019] Guidelines on Online Distribution and Advisory Platforms (Chapter 4: robo-advice; suitability applies; auto-rebalancing treated as a recommendation; algorithm supervision, testing, contingency plans). — [Hong Kong Gazette notice](https://www.gld.gov.hk/egazette/pdf/20182214/egn201822142403.pdf); [Charltons](https://www.charltonslaw.com/sfc-guidelines-on-online-platforms-and-advisory-services/)
- [IN FORCE, 2024] SFC circular on generative AI language models applies to licensed corporations; treats AI LMs for investment recommendations/advice/research as high risk; effective immediately with pragmatic enforcement. Exact issue date not confirmed. — [Linklaters](https://techinsights.linklaters.com/post/102jp7z/key-implications-of-hong-kongs-new-sfc-circular-on-genai-language-models); [A&O Shearman](https://www.aoshearman.com/en/insights/ao-shearman-on-data/hong-kong-sfc-issues-circular-on-the-use-of-generative-ai-language-models)
- Licensing timing: SFC pledge 15 weeks from formal acceptance for corporations; law-firm view 4-6 months; fee HK$4,740 per type; paid-up/liquid capital tiers conflict in sources (HK$100k liquid for Types 4/9 without client assets up to HK$5M paid-up/HK$3M liquid). — [Ocorian](https://www.ocorian.com/knowledge-hub/insights/getting-licensed-hong-kong-successfully-navigating-sfcs-process); [Kaizen CPA (consultancy)](https://www.kaizencpa.com/services/info/id/518.html)
- SFC Regulatory Sandbox (launched 29 Sep 2017) still requires licences; SFC page (updated 26 Mar 2026) expects most applicants, including robo-advisers, to use the normal licence route. — [SFC sandbox page](https://www.sfc.hk/en/Welcome-to-the-Fintech-Contact-Point/SFC-Regulatory-Sandbox)

### Inferences
- Hong Kong offers no special fast track for AI advice; its value is an accessible regulator and clear AI-risk expectations.

### Gaps
- Precise capital tiers and current processing metrics unverified; HKMA/PCPD AI guidance not reviewed.

### 4d. Australia (ASIC)

### Takeaway
Australia regulates by licence (AFSL) with scaled and digital advice covered by RG 255; the Delivering Better Financial Outcomes "new class of adviser" reform is stalled, and ASIC processing is slow (70% of licence applications within 150 days, 90% within 240 days, per a trade update).

### Cited Findings
- General advice = no consideration of client's objectives/situation/needs; personal advice requires the best-interests duty; RG 255 (2016) covers automated advice incl. algorithm testing and a responsible manager; fully digital advice still needs an AFSL. — [Bright Law](https://www.brightlaw.com.au/asic-finalises-guide-on-digital-financial-product-advice/); [Canstar](https://www.canstar.com.au/news-articles/asic-releases-robo-advice-guidance/)
- ASIC AFSL processing: service charter 70% within 150 days, 90% within 240 days (Oct 2024 report on 2023-24); application fees vary by complexity (consultancy cites AUD 3,721 for financial planners; a proposal would raise fees — adoption not confirmed). — [HSF Kramer funds update, Oct 2024](https://www.hsfkramer.com/notes/fsraustralia/2024-posts/funds-update-18-october-2024); [AFSL House (consultancy)](https://afslhouse.com.au/insights/how-much-does-an-afsl-actually-cost/)
- [PROPOSAL, stalled] DBFO Tranche 1 passed mid-2024; Tranche 2 exposure draft (Mar 2025) omitted the new class of adviser and best-interests duty modernisation; Feb 2026 minister signalled caution after the Shield/First Guardian collapses; no bill found. — [Professional Planner, Feb 2026](https://www.professionalplanner.com.au/2026/02/new-class-of-adviser-might-not-survive-shield-first-guardian-fallout/); [Investment Magazine](https://www.investmentmagazine.com.au/2026/02/dbfo-new-class-of-adviser-unlikely-to-survive-shield-first-guardian-fallout/)
- ASIC REP 798 (29 Oct 2024) found AI governance lagging licensee obligations. — [search result via JD Supra index](https://www.jdsupra.com/topics/asic/artificial-intelligence/innovative-technology) (truncated; verify on asic.gov.au)

### Inferences
- Australia is slow and licensing-heavy for AI advice; the "general advice" route can be used for non-personalised education but requires an AFSL if it amounts to a financial product recommendation.

### Gaps
- Current AFSL fees, ASIC sandbox (licensing exemption) terms, and AI-chatbot general-advice guidance not found.

### 4e. Brazil

### Takeaway
Robo-advice sits under CVM Resolution 19 (registered securities consultant) and algorithms do not reduce obligations; CVM and the Central Bank run sandboxes; payment initiation under Open Finance/Pix is regulated by the Central Bank, with an "initiator" participant category.

### Cited Findings
- Robo-advisers are covered by CVM Resolution 19 (securities consulting); algorithmic delivery does not remove the registration obligation (CVM Res. 21 concerns portfolio administration, which a source conflated). — [Mattos Filho](https://www.mattosfilho.com.br/unico/novas-regras-cvm-administradores-fundos/); [Euqueroinvestir](https://euqueroinvestir.com/robo-investidor)
- CVM sandbox: Resolution CVM 29 (in force 1 Jun 2021) requires prior authorisation from the CVM Sandbox Committee; BCB sandbox: CMN Res. 4,865 and BCB Res. 29 (Dec 2020), cycles up to 1 year extendable once; first cycle included open banking themes. — [Felsberg](https://www.felsberg.com.br/en/cvm-publishes-new-resolution-on-regulatory-sandbox/); [Infomoney](https://www.infomoney.com.br/?p=1537432)
- Pix Automático launched 16 Jun 2025; BCB rules effective 13 Oct 2025; integrated with Open Finance; a payment "initiator" participant category exists under BCB Res. 360/2023; a vendor announced an agentic Pix payments MCP (product news, not a rule). — [Mattos Filho](https://www.mattosfilho.com.br/unico/bcb-divulga-pix-automatico/); [LetsMoney](https://www.letsmoney.com.br/pagamentos/iniciador-lanca-o-primeiro-mcp-de-pagamentos-agenticos-via-pix/); [Lex](https://www.lex.com.br/resolucao-bacen-no-360-de-7-de-dezembro-de-2023/)

### Inferences
- Brazil has the strongest public payment-initiation rails (Pix + Open Finance) for agent-executed payments where the startup never holds funds, but initiator authorisation and consent journeys are prescriptive.

### Gaps
- CVM consultant registration cost/time/capital, AI-specific CVM/BCB rules, and current Open Finance consent rules not verified (sources mostly 2020-2021 and vendor/news).

### 4f. Indonesia (OJK)

### Takeaway
Indonesia has an ITSK/sandbox regime (POJK 3/2024) but it is slow in practice, an AI ethics guideline (non-binding, Nov 2023) and no found dedicated robo-adviser rule.

### Cited Findings
- POJK 3/2024 on technology innovation in the financial sector (ITSK) replaced POJK 13/2018; by 30 June 2026 OJK had received 335 sandbox consultation requests and had two participants in testing. — [Bisnis, 23 Jul 2026](https://finansial.bisnis.com/read/20260723/563/1990576/ojk-bidik-indonesia-jadi-pusat-inovasi-global); [Makarim](https://www.makarim.com/news/refining-digital-financial-innovation-new-ojk-regulation-aims-to-enhance-regulatory-sandbox)
- OJK AI ethics guideline for fintech (Nov 2023); a 2025 banking AI governance framework is reported by an aggregator only. — [Tempo](https://en.tempo.co/amp/1801086/ojk-launches-ethical-guidelines-to-artificial-intelligence-use-in-fintech-industry); [BABL AI (unverified)](https://babl.ai/indonesia-unveils-ai-governance-framework-to-guide-banking-sector-transformation/)
- POJK 4/2025 financial services aggregators; OJK may require entities near its scope to enter the sandbox. — [OJK press release](https://ojk.go.id/en/berita-dan-kegiatan/siaran-pers/Pages/OJK-Issues-Regulation-on-the-Operation-of-Financial-Services-Aggregators.aspx)

### Inferences
- Indonesia is not a low-friction first launch market for AI advice; its sandbox throughput is low.

### Gaps
- Licence type for investment advice (manajer investasi/penasihat), capital and AI-specific obligations not found.

### 4g. Nigeria (SEC)

### Takeaway
Nigeria has explicit robo-adviser rules (2021) with a minimum capital recently raised tenfold to N100 million (Jan 2026); its incubation programme targets digital-asset firms and has been slow.

### Cited Findings
- SEC Nigeria circular 26-1 (16 Jan 2026) raised minimum capital for robo-advisers from N10M to N100M; digital asset exchanges/custodians N2B (deadline reported 30 Jun 2027). — [TechCabal](https://techcabal.com/2026/01/16/sec-2-billion-minimum-capital-for-exchanges/); [Techpoint](https://techpoint.africa/news/revised-sec-capital-requirements/)
- 2021 robo-advisory rules (30 Aug 2021): comply with adviser rules, minimum capital, fidelity bond, pre-launch and ongoing algorithm audits, independent tech reviews. — [SEC Nigeria fintech rules](https://www.sec.gov.ng/our-mandate/regulation/rules-and-regulations/sec-rules-for-fintechs/); [Robo adviser registration checklist](https://sec.gov.ng/about/resources/checklists/individual-registration-requirements-for-each-cmo/robo-adviser-registration-requirements)
- ARIP sandbox (June 2024): only Busha and Quidax provisionally licensed; no new admissions since Aug 2024; digital-asset focus. — [TechCabal](https://techcabal.com/?p=178357)

### Gaps
- Investments and Securities Act 2025 effect on robo-advisers, AI-specific rules, and licensing times not confirmed.

---

## 5. Cross-border: serving foreign users, reverse solicitation, data residency, US LLM APIs

### Takeaway
Online services reaching a country's residents are typically treated as conducted in that country; reverse solicitation is narrow and, in the EU, any solicitation (including websites, advertising and influencers) defeats it. Sending EU users' financial data to US LLM APIs relies on the EU-US Data Privacy Framework (still valid but under CJEU appeal) or SCCs.

### Cited Findings
- [IN FORCE] MiFID II Art. 42: third-country firms may serve EU clients only at the client's "own exclusive initiative"; ESMA (13 Jan 2021) rejected boilerplate clauses/pop-up "I agree" boxes and said any solicitation or promotion (press, internet ads, phone) defeats it; later offering of other products is limited to similar products. ESMA's 2025 MiCA reverse solicitation guidelines (published 26 Feb 2025, from 27 Apr 2025) are broader on influencers and third parties; ESMA says both regimes share principles, but applicability of the MiCA detail to MiFID is unclear. — [Freshfields](https://www.freshfields.com/en/our-thinking/blogs/risk-and-compliance/finally-some-clarity-on-reverse-solicitation-under-micar-and-beyond-esmas-fi-102jrp8); [Simmons & Simmons](https://www.simmons-simmons.com/en/publications/clu87xbun000uv82o5yhohnm9/a-stricter-approach-to-reverse-solicitation-for-financial-services-); [Burges Salmon](https://www.burges-salmon.com/articles/102gorl/brexit-update-esma-warns-against-certain-reverse-solicitation-practices)
- CRD VI Art. 21c mirrors Art. 42 for banking services. — [Freshfields link above]
- [PENDING APPEAL] EU-US Data Privacy Framework: General Court dismissed Latombe's challenge 3 Sep 2025; appeal filed 31 Oct 2025 (C-703/25 P, OJ 22 Dec 2025); DPF stays in force meanwhile; Safe Harbor and Privacy Shield were both struck down previously. — [WilmerHale](https://www.wilmerhale.com/en/insights/blogs/wilmerhale-privacy-and-cybersecurity-law/20251201-european-court-of-justice-to-review-challenge-to-eu-us-data-privacy-framework); [Digital Policy Alert](https://digitalpolicyalert.org/event/35459-latombe-filed-appeal-against-general-court-dismissal-of-challenge-to-european-unionunited-states-data-protection-framework-adequacy-decision-in-latombe-v-commission)
- [IN FORCE] FINRA/SEC data-protection duties (Reg S-P) apply to US advisers regardless of where the LLM is hosted (see section 1).

### Inferences
- Geo-fence products (block or disclaim non-launch countries, avoid targeted marketing/influencers) rather than rely on reverse solicitation; use SCCs plus DPF as belt-and-braces for EU data to US LLM APIs; prefer zero-retention enterprise API terms and EU-region endpoints where available (not researched).

### Gaps
- GDPR Art. 22 / automated decision-making and DPIA treatment of financial profiling, data-residency mandates (Singapore, UAE, Brazil, Indonesia, Nigeria, India), and LLM-vendor DPA terms were not researched; UK and Singapore equivalents of reverse solicitation not covered.

---

## 6. Sandboxes and fast-track programmes; startup examples

### Takeaway
Active AI-relevant programmes are the UK FCA (AI Live Testing, Supercharged Sandbox), Singapore MAS (Sandbox Express, 21 days), DFSA ITL, ADGM RegLab, Brazil CVM/BCB, Nigeria ARIP and Indonesia OJK; the Hong Kong SFC explicitly says robo-advisers should use the normal licence route.

### Cited Findings
- UK AI Live Testing cohorts 1-2 (see section 2) include NatWest, Monzo, Santander, Scottish Widows, Barclays, Lloyds, Experian, GoCardless and smaller firms (Snorkl, Gain Credit, Palindrom, Aereve, Coadjute). — [Mortgage Solutions](https://www.mortgagesolutions.co.uk/mortgage-news/2026/04/21/fca-to-assess-good-and-bad-use-of-ai-as-barclays-and-lbg-join-second-test-programme/)
- Singapore Sandbox Express 21-day response target; 9-month experiments. — [Allen & Gledhill](https://www.allenandgledhill.com/sg/perspectives/articles/13314/mas-launches-sandbox-express-for-faster-market-testing-of-innovative-financial-services-and-products)
- DFSA: Sarwa (robo-advisory) first sandbox graduate. — [DFSA](https://www.dfsa.ae/news/robo-advisory-firm-sarwa-first-graduate-dfsas-regulatory-sandbox)
- Nigeria ARIP: only two provisional licences (Busha, Quidax), digital assets. — [TechCabal](https://techcabal.com/?p=178357)
- Indonesia OJK sandbox: two participants in testing by mid-2026. — [Bisnis](https://finansial.bisnis.com/read/20260723/563/1990576/ojk-bidik-indonesia-jadi-pusat-inovasi-global)
- Hong Kong: sandbox participants still need licences; great majority of applicants incl. robo-advisers expected to use the normal route. — [SFC](https://www.sfc.hk/en/Welcome-to-the-Fintech-Contact-Point/SFC-Regulatory-Sandbox)
- EU: AI Act national regulatory sandboxes now due by 2 Aug 2027. — [Gibson Dunn](https://www.gibsondunn.com/eu-ai-act-omnibus-agreement-postponed-high-risk-deadlines-and-other-key-changes/)

### Gaps
- No verified list of AI-advice start-ups that graduated from a sandbox into a licence; US has no AI-advice sandbox found (SEC has no sandbox for advisers; not separately verified).

---

## 7. Comparative map and lowest-friction launch paths (synthesis, as of 7 Oct 2026)

### Takeaway
Cheapest and fastest: (a) education/guidance is largely unlicensed in the US (publisher's exclusion), UK (generic guidance) and EU/Singapore/HK/Australia if truly non-personal; (b) personalised AI advice is cheapest via a US state RIA, then a UK Part 4A targeted-support permission or an EU advice-only MiFID licence; (c) agent-executed investments/payments without holding funds are easiest where payment initiation is a defined, light-touch role (UK/EU AISP/PISP, Brazil initiator, or US via licensed partners) and hardest where state-by-state licensing and consent law are unsettled.

### Cited Findings (condensed map; each line summarises findings cited above)

| Jurisdiction | Licence for personalised advice | Cost / capital (verified items) | Time (verified items) | AI-specific rule status | Fast-track |
|---|---|---|---|---|---|
| US | State RIA (or SEC if internet-adviser exempt / $110M+) | State fees $50-500 + IAR; net worth $10k-50k or surety bond (state-specific) | SEC <30 days (practitioner claim); state time unverified | No AI rule; PDA rule withdrawn Jun 2025; exam priorities, AI-washing enforcement; Colorado ADMT law 1 Jan 2027 | None found |
| UK | Part 4A advice, or new targeted-support permission (live 6 Apr 2026) | Fees GBP 280 to ~225k by category; capital not retrieved | 6 months statutory (complete app) | No new AI rules (Mills Review, Jul 2026); Consumer Duty/SM&CR; agentic payments consultation | AI Live Testing, Supercharged Sandbox, PASS |
| EU | MiFID II investment firm | EUR 75k (advice, no client assets) | 6 months statutory, shorter in some states | AI Act: Annex III high-risk 2 Dec 2027; Art. 50 2 Aug 2026; ESMA AI statement 2024 | National AI sandboxes by Aug 2027 |
| Singapore | FA licence (digital adviser relief) | S$300-500k base capital | Not verified (Sandbox Express 21-day response) | AI risk guidelines proposed (consulted to Jan 2026); toolkit Mar 2026 | Sandbox Express |
| UAE | DFSA Cat 4 / FSRA advising | Conflicting (USD 10k-140k); ITL fee USD 5k | Not verified | No AI-specific rule found | DFSA ITL, ADGM RegLab |
| Hong Kong | SFC Type 4/9 | Fee HK$4,740/type; capital tiers disputed | ~15 weeks pledge to 4-6 months | GenAI circular 2024 (mandatory); robo guidelines 2019 | Sandbox (not for robo-advisers) |
| Australia | AFSL | AUD ~3.7k+ lodgement (consultancy) | 150-240 days service charter | REP 798 governance report; no AI-specific rule found | None found |
| Brazil | CVM consultant (Res. 19) | Not retrieved | Not retrieved | None found | CVM/BCB sandbox |
| Indonesia | OJK (not identified) | Not retrieved | Not retrieved | Non-binding AI ethics guideline | OJK ITSK sandbox (slow) |
| Nigeria | SEC robo-adviser registration | Min. capital N100M (Jan 2026) | Not retrieved | Algorithm audit requirements | ARIP (digital assets only) |

### Inferences
- (a) AI education/guidance: lowest friction is a US-based product (First Amendment/Lowe-based publisher's exclusion) or UK guidance, with strict "no personalised recommendations" product design, disclaimers that are not relied on alone, and no AI overclaiming.
- (b) Personalised AI advice: lowest total friction in order: US state RIA (small fees and bond, but strong fiduciary and marketing-claims exposure; SEC internet exemption possible for fully automated advice); UK targeted support (new, regulator-supported, but needs direct authorisation and takes up to 6 months); EU advice-only firm in a small member state (EUR 75k) with passport; Singapore/HK/UAE for Asian expansion with sandboxes.
- (c) Agent-executed investments/payments with no custody: partner-led structures (licensed broker-dealer/custodian and licensed bank/PISP/aggregator) minimise own licences; UK/EU PISP-AISP registration and Brazil initiator are defined routes; US state money-transmitter exposure remains the largest uncertainty; the UK and EU are explicitly revising consent/authentication rules for agents, so product design should keep the user as the final authoriser with spending/asset limits.
- Priority watch-list dates: Mills perimeter review (late 2026/early 2027); UK CP26/10 policy statement (Q4 2026); UK payments/AI consultation outcome; CFPB 1033 NPRM (late 2026/early 2027); AI Act Art. 50 (2 Aug 2026 passed; 2 Dec 2026 grace) and Annex III (2 Dec 2027); Colorado SB 26-189 (1 Jan 2027); MAS AI guidelines final; PSD3/PSR OJ publication; CJEU Latombe appeal.

### Gaps
- Comparison with India deliberately excluded. Cost and time figures for Brazil, Indonesia, Nigeria, UAE, Australia are low-confidence. Time-to-licence for US state RIAs, targeted-support permissions and Singapore FA licences was not found. Several jurisdiction facts rest on law-firm or consultancy secondary sources; primary regulator texts should be checked before any decision.
