# Recover Money First, Manage Wealth Later

*Strategy memo for an India-based founder choosing an AI-in-finance problem. Evidence cut-off: 7 October 2026. Indian fiscal years run April to March (FY26 = Apr 2025 to Mar 2026). 1 crore (cr) = 10 million; 1 lakh crore = ₹1 trillion. "CR" marks company-reported figures. Scores, sizing arithmetic and product designs are the author's inferences and are labelled as such.*

## Executive summary

**The recommended first product is a health-insurance claim-recovery agent, not an investing app or an algo-trading model.** The agent reads a rejected or short-paid claim, maps every deduction to the policy wording and IRDAI rules, drafts and files the grievance and then the Ombudsman complaint, and tracks the case until money comes back. The pain is large and documented by the regulator:

- Indian health insurers rejected or disallowed about **₹26,037 crore of claims in FY24** ([Moneylife, Lok Sabha reply](https://moneylife.in/article/health-insurance-claims-worth-rs2603765-crore-rejected-by-insurers-in-fy2324-govt/76282.html)).
- About **95% of health complaints to the Insurance Ombudsman concern claim rejections** ([Outlook Money](https://www.outlookmoney.com/amp/story/personal-finance/why-95-per-cent-of-health-insurance-complaints-concern-claim-rejections)).
- About **41% of health complaints were resolved in policyholders' favour in FY25** ([Cafemutual](https://cafemutual.com/news/industry/36635-41-of-health-insurance-complaints-were-resolved-in-favour-of-policyholders-in-fy25)).

No AI-native player owns this job. It also needs no IRDAI licence as long as the product never takes insurer commissions; IRDAI fined Acko ₹1 crore for paying an unlicensed referral partner ([Outlook Money](https://www.outlookmoney.com/insurance/acko-gets-rs-1-crore-irdai-fine-what-it-says-about-how-your-insurance-is-sold)).

In a scored matrix of 14 ideas, this one scored **4.10 out of 5**. The next two were an MSME receivables agent (3.85) and a GST notice desk sold to CA firms (3.70). The same engine can be exported to the US, where **20% of in-network ACA marketplace claims were denied in 2023 and fewer than 1% of denials were appealed** ([KFF](https://www.kff.org/private-insurance/claims-denials-and-appeals-in-aca-marketplace-plans-in-2023/)).

**The friend's investing thesis targets the hardest place to start:**

- Incumbents make their money on derivatives: equity F&O was **55% of Groww's Q4 FY26 revenue** ([Medianama](https://www.medianama.com/2026/05/223-groww-q4-fy26-fo-user-share-decline-customer-shift-mutual-funds-etfs/)).
- Mutual-fund-first apps are small, loss-making, or have been sold.
- Groww, Zerodha and 1% Club all launched AI layers in 2025–26.
- Any product that names a fund for a specific user, or places an order, needs SEBI registration.

The friend is right that users want finished work rather than another chatbot, and right that 1% Club's trust-first funnel deserves study. The friend is wrong that the following are sound foundations:

- a fine-tuned small model;
- a correctness test run with 50–70 users;
- a model trained on 5–7 trading algorithms.

**The path that follows from the evidence:**

1. Earn trust by recovering money people have already lost.
2. Extend into adjacent household-finance chores.
3. Only once distribution exists, add an RIA-licensed mutual-fund "fixer".

**Verdicts on the friend's five claims (detail in the section on the friend's thesis)**

| # | Claim | Verdict | Decisive evidence |
|---|---|---|---|
| 1 | Quant/algo survives AI, but only with 5–7 proven algos used to train your own model | **Half right; wrong conclusion** | Algos earn 96–97% of prop/FPI F&O profits, but 87.7% of individual traders lost money in FY26. Retail algo vendors now need exchange empanelment, plus SEBI RA registration for black-box strategies. Seven return series are far too few to train a model on. |
| 2 | Consumer finance apps are crowded with "bare minimum" products | **True on crowding; misdiagnosed on cause** | The top three brokers hold about 58.5% of NSE active clients. The gap is not missing features: no incumbent is paid to fix a portfolio, a claim or a tax notice. |
| 3 | Post-AI, people want end results, not chatbots | **Correct, with a regulatory caveat** | Money follows outcomes (Wealthfront cash sweep, Cleo advances). Regulators require a human confirmation for money movement, so "end result" means finished work plus one-tap approval. |
| 4 | 1% Club (~₹100 cr+, non-AI) is the model | **Right to admire, wrong to copy; now partly outdated** | Revenue of ₹150 cr+ over three years is company-claimed. 1% Club became an RIA in Feb 2025 and launched an "AI CFO" in Aug 2026. Its moat is an audience the founder does not have. |
| 5 | MF pilot: scrape everything → fine-tune → chatbot tested by 50–70 users → investing agent that never touches money | **Right domain, wrong sequence** | Data is free and the rules corpus is bounded. Fine-tuning lowered faithfulness in benchmarks. Users cannot verify correctness. "Never touching money" is already mandatory. The binding constraint is the licence, not the model. |

**Top five ideas (full matrix of 14 in the scoring section)**

| Rank | Idea | Score /5 | One-line rationale |
|---|---|---|---|
| 1 | Health-claim recovery agent (India first, US later) | 4.10 | Regulator-sized pain, no licence needed, success-fee economics, no AI-native incumbent |
| 2 | MSME receivables and delayed-payment agent | 3.85 | ₹8.1 lakh cr overdue (CR), plus the new MSMED Amendment 2026 deadlines; MSMEs are hard to reach |
| 3 | GST reconciliation and notice desk sold to CA firms | 3.70 | CAs pay and are reachable; Tally and Clear are bundling AI |
| 4 | Compliance copilot for SEBI intermediaries | 3.65 | Timed to SEBI's new advertisement code (Sept 2026), but the buyer pool is small |
| 5 | Family money finder and transmission concierge | 3.60 | About ₹2.2 lakh cr unclaimed; claiming requires paperwork and branch visits |

## Incumbents earn on derivatives, so nobody is paid to fix your portfolio

### Mutual funds bring users in; trading pays the bills

Every large Indian investing app acquires users with mutual funds (MFs) and SIPs, then earns from trading, margin and lending. Groww's revenue mix shows this clearly:

- Equity derivatives were **55% of operating revenue in Q4 FY26**; cash equities were 16% and the margin trading facility (MTF) 5% ([Medianama](https://www.medianama.com/2026/05/223-groww-q4-fy26-fo-user-share-decline-customer-shift-mutual-funds-etfs/)).
- Groww had **10.03 million active MF users against 1.70 million F&O users** in the same quarter ([Medianama](https://www.medianama.com/2026/05/223-groww-q4-fy26-fo-user-share-decline-customer-shift-mutual-funds-etfs/)).
- So a user base roughly six times larger than its traders generates a minority of revenue.

Other players follow the same pattern:

- Angel One's F&O brokerage was about **47% of gross income in Q4 FY26** ([Whalesbook](https://www.whalesbook.com/corporate-news/English/bankingfinance/Angel-One-FY26-Profit-at-indian-rupee915-Cr-Income-indian-rupee5152-Cr-Adds-69M-Clients/6a32b0cbb6609c8f9dd1a423)).
- Dhan earned about **88% of FY25 operating revenue from brokerage** ([BW Disrupt](https://www.bwdisrupt.com/article/dhan-posts-rs-408-cr-profit-in-fy25-as-revenue-jumps-2-3x-to-rs-877-cr-592103)).

Direct-plan MF distribution earns almost nothing by design. A Category-1 Execution-Only Platform (EOP) may receive **at most ₹2 per transaction** from AMCs ([Cafemutual](https://cafemutual.com/news/industry/31192-execution-only-platforms-registered-with-amfi-to-get-up-to-rs2-per-transaction)).

The result (inference) is that the 10-million-strong MF base is the segment incumbents monetise least and serve most thinly. The same economics explain why the MF-first independents shrank or were absorbed:

- **Kuvera** had revenue of about ₹6.2 crore against a ₹20.7 crore loss in FY25. A second Inc42 page gives ₹5.0 crore revenue and a ₹21.3 crore loss ([Inc42](https://inc42.com/company/kuvera/financials/)). CRED bought it in 2024 ([TechCrunch](https://techcrunch.com/2024/02/06/cred-acquires-mutual-fund-startup-kuvera-in-wealth-management-push/)).
- **Fisdom** lost ₹137.5 crore on ₹166.2 crore revenue in FY25 and was absorbed into Groww ([Inc42](https://inc42.com/company/fisdom/financials/)).
- **ET Money** was sold to 360 ONE for about ₹366 crore ([Business Standard](https://www.business-standard.com/amp/markets/news/wealth-management-firm-360-one-acquires-et-money-for-rs-366-crore-124061201219_1.html)).

| Company | Revenue engine | Latest financials (dated) | Scale and customer skew | AI moves 2025–26 | Visible weakness |
|---|---|---|---|---|---|
| **Groww** (listed Nov 2025) | F&O 55% of Q4 FY26 revenue; MTF, commodities, NBFC credit, AMC, Fisdom wealth | FY26 revenue from operations ₹4,644.6 cr, PAT ₹2,083 cr ([Whalesbook](https://www.whalesbook.com/corporate-news/English/tech/Billionbrains-Garage-Ventures-Groww-FY26-Profit-indian-rupee2083-Cr-Revenue-indian-rupee4645-Cr/69e5d99abca97ee10693650b)) | 29.04% of NSE active clients (Aug 2026); 16.7M active users; about ₹3 lakh cr customer assets ([StartupTalky](https://startuptalky.com/india-stock-broking-market-june-2026-analysis/); [Goodreturns](https://www.goodreturns.in/news/groww-q4-results-billionbrains-garage-profit-jumps-122-to-rs-686-cr-revenue-surges-88-user-base-1503307.html)) | GR-1 assistant (beta, Feb 2026), portfolio health checks, family wealth; user approves every action ([Entrackr](https://entrackr.com/news/groww-showcases-ai-powered-investing-tools-at-groww-next-2026-11168623)) | Share of users trading F&O fell from 18% to 10%; the AMC lost ₹21.4 cr |
| **Zerodha** (private) | Broking (₹2,738 cr FY26), growing MTF book; Coin for direct MFs | FY26 PAT about ₹4,283 cr, or ₹4,238 cr per Inc42 (**conflict**); revenue roughly flat at about ₹8,500–8,850 cr ([Lapaas](https://lapaasvoice.com/zerodha-fy26-profit-rises-1-2-to-%e2%82%b94283-crore-brokerage-income-falls-10-7/); [Inc42](https://inc42.com/buzz/zerodhas-bland-fy26-net-profit-up-a-mere-1-at-₹4238-cr-top-line-at-fy25-level/)) | 14.79% of NSE active clients; active-trader skew | Kite MCP (May 2025), a read-only connector to Claude and other assistants ([Zerodha](https://zerodha.com/products/mcp/)) | Warned FY26 revenue could fall up to 40% from FY24 after F&O curbs ([Whalesbook](https://www.whalesbook.com/news/English/bankingfinance/Zerodha-Reports-15percent-Revenue-Drop-in-FY25-Amidst-Regulatory-Changes-Warns-of-Further-Decline/68dcf6c71a9bfbf9a4659406)) |
| **Angel One** (listed) | Broking about 61% of income; F&O about 47% of gross income | FY26 income ₹5,152 cr; PAT ₹915 cr (−21.9%) | 37.4M clients; 89% of 6.9M FY26 additions from Tier 2/3 towns ([Whalesbook](https://www.whalesbook.com/corporate-news/English/bankingfinance/Angel-One-FY26-Profit-at-indian-rupee915-Cr-Income-indian-rupee5152-Cr-Adds-69M-Clients/6a32b0cbb6609c8f9dd1a423)) | Not verified | F&O concentration; IPL sponsorship cost compressing margins |
| **Upstox** | Broking | FY25 revenue from operations ₹945 cr, PAT ₹215 cr helped by ₹103 cr non-operating income ([Entrackr](https://entrackr.com/fintrackr/upstox-posts-rs-1208-cr-income-and-rs-215-cr-profit-in-fy25-11024275)) | 4.06% of NSE active clients | Not verified | Share fell from 5.58% to 4.35% during FY26 |
| **Dhan** | About 88% brokerage | FY25 revenue ₹877 cr, PAT ₹408 cr | Active traders; launched "Millions", a Gen-Z SIP app, in 2026 ([Inc42](https://inc42.com/buzz/dhan-parent-raise-launches-millions-investment-app-targeting-gen-z/)) | "Fuzz" insights model (reported) | Same F&O exposure |
| **Paytm Money** | Broking, MFs | FY25 turnover ₹173 cr (−11%) ([Storyboard18](https://www.storyboard18.com/how-it-works/one97-communications-to-invest-%e2%82%b9300-crore-in-broking-entity-paytm-money-79615.htm)) | Losing active customers | Not verified | Parent injected about ₹300 cr |
| **INDmoney** | Multi-asset, tracking | FY25 operating revenue ₹164 cr; cash loss ₹76 cr ([Entrackr](https://entrackr.com/news/indmoneys-revenue-jumps-23x-to-rs-164-cr-in-fy25-10965136)) | Tracks external folios via periodic CAS imports, not live data ([Foliyo](https://foliyo.ai/guides/mf-platforms/indmoney-review/)) | "Algorithmic rather than fiduciary" advice (reviewer) | Widening losses |
| **ET Money** (360 ONE) | Free investing; paid "Genius" portfolio review; insurance and loans | Not found | Mass retail | Genius is behind a paywall ([Vittsphere](https://one.vittsphere.com/blog/personal-finance/best-ai-personal-finance-platforms-india-2026/)) | Searching for revenue beyond MFs |
| **Scripbox** | Advice and wealth, HNI tilt | FY25 operating revenue ₹107.2 cr; PAT ₹12.8 cr, first true profit ([Entrackr](https://entrackr.com/fintrackr/12-year-old-scripbox-turns-profitable-with-rs-107-cr-revenue-in-fy25-10809852)) | Affluent | Not verified | Took 12 years to reach profit |
| **smallcase** | Model-portfolio platform, gateway | FY25 operating revenue ₹106 cr; net loss ₹34 cr ([Entrackr](https://entrackr.com/exclusive/exclusive-smallcase-crosses-rs-100-cr-revenue-mark-in-fy25-9493192)) | Self-directed investors | Not verified | Still loss-making |
| **Jar** | Daily digital-gold savings | FY25 revenue ₹2,447.8 cr, mostly gross gold sales; loss ₹50.5 cr ([Head and Tale](https://theheadandtale.com/fintech-news/jar-fy25-revenue-up-50-fold-to-rs-2447-crore-net-loss-halves/)) | Mass-market savers | Not found | Revenue is gross, not margin |

### Customers skew to small towns and first-time MF investors

Groww leads with about **13.35 million NSE active clients, 29.04% of the market**, against Zerodha at 14.79% and Angel One at 14.62% (Aug 2026). The top three hold about 58.5% ([StartupTalky](https://startuptalky.com/india-stock-broking-market-june-2026-analysis/)). NSE active clients have fallen from a peak of about 4.96 crore in January 2025 to 4.42 crore in June 2026, a result of the F&O curbs.

Groww has said that nearly 70% of its users come from Tier 2 and Tier 3 cities. That figure is from a 2021-era company blog ([Groww](https://groww.in/blog/groww-raises-251-million-series-e-funding-to-expand-its-business)). Its CFO says the acquisition funnel "has shifted more towards mutual funds and ETFs" ([Medianama](https://www.medianama.com/2026/05/223-groww-q4-fy26-fo-user-share-decline-customer-shift-mutual-funds-etfs/)).

Across the industry the profile looks like this:

- **6.19 crore unique MF investors** across 27.86 crore folios (June 2026) ([Angel One / AMFI](https://www.angelone.in/news/mutual-funds/nippon-india-mutual-fund-crosses-4-crore-investor-folios-as-mutual-fund-industry-reaches-27-86-crore-folios)).
- Women are 26.3% of investors but hold 34.6% of assets ([Cafemutual](https://cafemutual.com/news/industry/37753-one-third-of-individual-mf-assets-come-from-women-investors-amfi)).
- Investors aged 25–44 put 60% of FY25 net inflows into equity ([Angel One](https://www.angelone.in/news/mutual-funds/equity-allocation-rises-across-age-groups-25-44-bracket-jumps-from-36-to-60)).

Penetration is shallow. Per SEBI's 2025 household survey:

- 53% of households know about MFs, but only **6.7% hold them** ([Outlook Money](https://www.outlookmoney.com/invest/mutual-funds/sebi-survey-2025-mutual-fund-awareness-soars-in-india-but-still-not-enough-heres-why)).
- 59% of investors rely on friends and family for information, and 56% on finfluencers ([Outlook Money](https://www.outlookmoney.com/invest/equity/sebi-investor-survey-2025-new-investors-listen-to-friends-feeds-and-finfluencers)).

### How incumbents operate: distribution, licences and shared rails

The winners grew on distribution, not technology:

- More than 80% of Groww's customers came organically or by referral ([Ensemble VC](https://www.ensemble.vc/research/ipo-alert-groww-goes-public)).
- Zerodha used free content (Varsity) and founder-led trust.
- Angel One buys brand reach through IPL sponsorship.

All of them run on the same public rails, so infrastructure is not a moat:

| Rail | What it does | Who can access it | Economics / notes |
|---|---|---|---|
| BSE StAR MF, NSE NMF II, MF Utilities | Place MF orders, SIPs, switches | Brokers, AMFI distributors (ARN); RIAs on BSE StAR MF for direct plans | BSE lists **nil** membership fees for RIAs ([BSE](https://bseindia.com/Static/Markets/MutualFunds/registered_invest_advisors.aspx)) |
| EOP framework (from 1 Sep 2023) | Direct-plan execution without advice | Cat-1: AMFI-registered body corporate with ₹1 cr net worth. Cat-2: broker with ₹10 lakh deposit | ≤₹2 per transaction, no advice, no scheme ads ([Taxmann](https://www.taxmann.com/post/blog/sebi-introduces-framework-for-execution-only-platforms-for-investing-in-direct-plans-of-mf-schemes/); [Business Standard](https://www.business-standard.com/amp/markets/news/amfi-sets-rs-1-crore-net-worth-criteria-for-eops-releases-guidelines-123090100961_1.html)) |
| CAS (CAMS/KFin), NSDL/CDSL eCAS | Consolidated holdings statements | Any user can download and share a PDF; parsable with the open-source casparser ([GitHub](https://github.com/codereverser/casparser)) | Free; no licence needed for read-only analysis |
| MF Central OTP pull | Programmatic holdings fetch | AMFI told it to stop sharing data with third-party apps (Sept 2025) ([Business Standard](https://www.business-standard.com/amp/markets/mutual-fund/amfi-asks-mf-central-to-stop-sharing-investor-data-with-third-party-apps-125091801057_1.html)) | Effectively closed to unlicensed apps |
| Account Aggregator (AA) | Consent-based bank, MF and demat data | Only regulated entities can be data users (FIUs) ([Sahamati](https://sahamati.org.in/faq/)) | 2.61B accounts enabled; 955 FIUs (2026) ([HyperVerge](https://hyperverge.co/blog/account-aggregator-framework-rbi/)) |
| Payments | Money flows directly from the investor's bank to the clearing corporation or AMC | Pooling banned since 1 Jul 2022 ([Business Standard](https://www.business-standard.com/amp/article/markets/sebi-discontinues-the-use-of-pool-accounts-for-transactions-in-mfs-121100401285_1.html)) | UPI AutoPay up to ₹1 lakh without extra authentication for MF SIPs ([Business Standard](https://business-standard.com/finance/news/automatic-payment-limit-through-upi-raised-to-rs-1-lakh-says-rbi-123121201097_1.html)) |

**Inference:** a newcomer cannot out-acquire Groww's organic engine or Angel One's ad budget. It also cannot differentiate on rails everyone shares. The open space is jobs incumbents are not paid to do.

## Retail investors' unsolved jobs are execution jobs, not information jobs

### The pain is measurable in rupees, and free tools only diagnose it

India's MF market is large and still growing:

- **₹87.08 lakh crore** in AUM at end-August 2026 ([DD India](https://ddindia.co.in/2026/09/equity-mutual-fund-inflows-rise-19-pc-to-rs-29328-crore-in-august-amfi-data/)).
- Record SIP inflows of **₹32,297 crore** in that month, across 10.02 crore contributing accounts ([INDmoney citing AMFI](https://www.indmoney.com/blog/mutual-funds/sip-stoppage-ratio-explained)).

The behaviour underneath is fragile. The SIP stoppage ratio exceeded 100% in March–April 2026, meaning more SIPs closed than opened, and April contributions fell 3% ([Angel One](https://www.angelone.in/news/economy/monthly-sip-contributions-decline-3-to-31-115-crore-in-april-2026-amfi)). AMFI's ratio mixes matured SIPs with cancelled ones, so this is a signal, not proof, of investors stopping during a market drawdown.

Retail investors are moving to direct plans quickly. Direct plans held **36.7% of retail AUM in March 2026, up from 21.4% in 2021** ([Outlook Money](https://www.outlookmoney.com/invest/direct-vs-regular-mutual-funds-investors-holding-period)). DIY investors account for 84% of direct assets ([Cafemutual](https://cafemutual.com/news/industry/36923-rias-bring-14-of-total-direct-assets-in-mfs)). Conflict-free help is scarce: India has only about **1,000 SEBI-registered investment advisers (RIAs)**, and the SEBI chairman voiced concern in March 2026 that finfluencers are filling the gap ([News on AIR](https://www.newsonair.gov.in/sebi-expresses-concern-over-decline-in-number-of-registered-investment-advisers/)).

| Pain | Who has it | Evidence of size | Solved today? | End-result agent fit |
|---|---|---|---|---|
| Regular→direct migration | Salaried 25–40, parents, NRIs | About 63% of retail AUM still in regular plans (**inference** from 36.7% direct). Exit loads on same-scheme switches removed in 2025 ([Cafemutual](https://cafemutual.com/news/industry/34850-no-exit-loads-on-switch-from-regular-to-direct-plans-sebi)), but the switch is still taxed: 20% STCG, 12.5% LTCG above ₹1.25 lakh ([ClearTax](https://cleartax.in/s/switch-regular-to-direct-plans)) | Diagnosis yes; tax-optimal staging across years is manual | High: deterministic and measurable |
| Annual LTCG harvesting and capital-gains schedules | Salaried, NRIs | casparser already outputs Schedule 112A data ([GitHub](https://github.com/codereverser/casparser)) | Mostly manual or done by a CA | High: seasonal (Jan–Mar) |
| Fund overlap and choice overload | First-jobbers, Tier 2/3 | About 1,865 open-ended schemes ([SEBI](https://www.sebi.gov.in/statistics/mutual-fund/objective/apr-mar-2026.html)) | Free overlap checkers | Medium: consolidating funds is advice and needs an RIA |
| Unclaimed MF money, KYC and nominee fixes | Families, the elderly, NRIs | **₹3,811 cr** unclaimed MF money (31 Mar 2026), up 153% in 3 years ([Cafemutual](https://cafemutual.com/news/industry/38475-unclaimed-mutual-fund-money-rises-153-in-three-years-to-rs-3811-crore)) | SEBI MITRA search exists; claiming is paperwork | High |
| No affordable advice | Mass affluent | About 60,000 investors per RIA (**inference**); basic plans cost ₹25k–50k a year ([Tradejini](https://www.tradejini.com/blogs/why-quality-financial-advice-remains-out-of-reach-for-most-indians)) | Finfluencers | Requires an RIA licence |
| F&O speculation | Under-30s | 88.5% of traders under 30 lost money in FY26 ([Morung Express/PTI](https://morungexpress.com/885-pc-of-traders-under-30-lost-money-in-fo-trading-in-fy26-sebi-study)) | Regulator friction | Behavioural feature, not a product |

Willingness to pay exists but clusters at higher incomes:

- Value Research Fund Advisor costs **₹4,999 a year** ([Value Research](https://www.valueresearchonline.com/fund-advisor/pricing-policy/)).
- 1% Club sold a **₹16,999 lifetime membership** ([Inc42](https://inc42.com/startups/how-finance-with-sharan-is-taking-middle-class-indians-toward-financial-freedom-with-the-1-club/)).
- RIA fees are capped at ₹1.51 lakh per family per year, or 2.5% of assets under advice ([Cafemutual](https://cafemutual.com/news/industry/33937-rias-can-now-charge-fees-up-to-rs-151-lakh-per-family-in-fixed-fees)).

No free-to-paid conversion data for Indian finance apps was found.

### Indian AI entrants have converged on "analyst plus human approval"

Incumbents shipped AI in 2025–26, but every launch found so far gives guidance only:

- **Groww GR-1** "acts as a research analyst" and cannot execute trades without explicit user approval ([Business Standard](https://www.business-standard.com/companies/news/groww-builds-ai-powered-platform-across-trading-wealth-and-fixed-income-126022800536_1.html)).
- **Zerodha's Kite MCP** is officially read-only.
- **1% Club's AI CFO** (Aug 2026) reviews portfolios on eight parameters: returns, quality, benchmark, allocation, concentration, overlap, cost and tax ([Storyboard18](https://www.storyboard18.com/brand-makers/sharan-hegdes-1-club-launches-ai-cfo-for-personalised-financial-planning-portfolio-guidance-107814.htm)).

Funded AI-first startups are small. Novelty Wealth, an RIA with the "NovaAI" assistant, raised a **$1.4M seed** in March 2026 ([Business Standard/ANI](https://www.business-standard.com/content/press-releases-ani/ai-wealthtech-startup-novelty-wealth-raises-1-4m-led-by-indiaquotient-to-scale-their-wealth-advisory-platform-for-indian-investors-126032500027_1.html)). The larger rounds go to human-led or distribution models:

- Dezerv: ₹350 cr Series C, with the new money going into relationship managers ([Dezerv](https://www.dezerv.in/blog/dezerv-raises-%E2%82%B9350-crore-in-series-c-funding/)).
- AssetPlus: ₹175 cr, free to MFDs ([Entrackr](https://entrackr.com/news/wealth-tech-startup-assetplus-raises-rs-175-cr-led-by-nexus-venture-partners-11011224)).

Indian wealthtech raised about **$317M across 26 deals** in the first eight months of 2026 ([CXO Digital Pulse](https://www.cxodigitalpulse.com/?p=62093)).

**Inference:** "AI that diagnoses my portfolio" is now a feature that incumbents give away. The open space is execution: actually completing the switch, the harvest, the claim or the filing.

### Globally, money follows outcomes and distribution, not advice chat

Global evidence points the same way. AI-labelled finance businesses that make money monetise **money movement, credit or bundles**, not advice:

- **Wealthfront** took **75% of FY2025 revenue from partner-bank cash-management fees** and reported $365.0M revenue for FY2026 (CR, [10-K](https://www.sec.gov/Archives/edgar/data/0001524566/000162828026027232/wlth-20260131.htm)).
- **Cleo**'s 2024 revenue nearly doubled to **$136M**, earned from subscriptions plus cash advances. It also paid $17M to settle FTC allegations ([Sifted](https://sifted.eu/articles/ai-fintech-cleo-return-uk)).
- **Robinhood** treats AI as a Gold upsell. Gold has **4.8M subscribers**, and Robinhood had 28.4M funded customers in Q2 2026 ([Robinhood](https://investors.robinhood.com/news-releases/news-release-details/robinhood-reports-second-quarter-2026-results)).

Standalone AI planners struggle with distribution:

- **Hiro** was acqui-hired by OpenAI and shut about five months after launch ([TechCrunch](https://techcrunch.com/2026/04/13/openai-has-bought-ai-personal-finance-startup-hiro/)).
- **OpenAI** itself launched a bank-linked ChatGPT finance preview in May 2026 ([Pulse2](https://pulse2.com/openai-new-personal-finance-experience-in-chatgpt-lets-pro-users-connect-financial-accounts-and-get-money-insights/)). That is direct platform risk for any "chat about my money" app.
- Scale comes from embedding inside a super-app. **Ant's Maxiaocai** reported about **70M MAU**, 45% from below tier-3 cities (CR, Aug 2024) ([BusinessWire](https://www.businesswire.com/news/home/20240905719583/en/Ant-Group-Unveils-AI-Financial-Manager-at-Shanghais-INCLUSION-Conference)).

| Global analog | What it proves | Transfer to India |
|---|---|---|
| Wealthfront, Cleo, Robinhood Gold | Revenue comes from cash, credit and bundles, not AI advice | India's cash-sweep and credit rails are licence-heavy, so a startup should look for success-fee "found money" instead |
| Origin ($99/yr SEC-registered AI adviser) and Range (flat-fee RIA aiming to replace its own advisers with AI) | Licensed AI advice is possible, but customer acquisition cost is unproven ([Kitces](https://www.kitces.com/blog/the-latest-in-financial-advisortech-october-2025-origin-ai-financial-advisor-low-fee-stockopter-grantd/); [InvestmentNews](https://www.investmentnews.com/ria-news/ria-startup-range-plans-to-eliminate-its-advisor-workforce-as-ai-takes-over/265586)) | The RIA route is cheap in India, but distribution is the bottleneck |
| Jump: 27,000 advisers and $105M raised for an adviser notetaker ([WealthManagement.com](https://wealthmanagement.com/artificial-intelligence/jump_secures_series_b)) | Selling to professionals scales fast through channel partners | India's MFD tools are free and commission-subsidised, so willingness to pay is weaker |
| Basis ($100M at $1.15B), Black Ore (waitlist of about 4,000 firms) | AI agents that do professional accounting and tax work attract the largest checks ([BusinessWire](https://www.businesswire.com/news/home/20260224020999/en/Basis-Raises-$100M-at-a-$1.15B-Valuation-as-Accounting-Firms-Adopt-End-to-End-Agents-Across-Accounting,-Tax,-and-Audit); [Street Insider](https://www.streetinsider.com/Press+Releases/Black+Ore+Launches+Tax+Autopilot+for+Broad+Availability/26390608.html)) | India has 159,557 CAs in practice ([TaxConcept](https://taxconcept.net/icai/statistics-of-icai-members-students-firms-till-28th-february-2025/)), a reachable B2B channel |
| Cara: seven-figure ARR within 7 months of founding, automating insurance-agency workflows (CR, [TamRadar](https://www.tamradar.com/funding-rounds/cara-seed-8m)) | Agents that replace one labour-heavy workflow reach revenue quickly | Supports a narrow, workflow-shaped first product |

Consumer surveys show the same gap between trust and accuracy. In the US, 23% are comfortable with AI chatbots but only 8% with robo-advisers ([RFI Global](https://rfi.global/bridging-the-ai-trust-gap-the-key-to-consumer-confidence-in-financial-services/)). Vendor-run tests found generic AI financial advice failing 57% to 85% of the time ([FA-Mag](https://www.fa-mag.com/news/two-studies--two-continents--one-outcome--ai-financial-advice-trends-wrong-88555.html)). Both vendors have a stake in the result. **Inference:** a narrow product grounded in the user's own documents, with citations, beats general chat on trust.

## The friend's thesis: two claims hold, three need rebuilding

### Claim 1: "Quant persists, but only with 5–7 proven algos used to train your own model." Half right, wrong conclusion.

The persistence part is correct. In FY24, **96% of proprietary traders' and 97% of FPIs' F&O profits came from algorithmic trading**, while individuals lost about ₹75,000 crore net ([Moneylife, SEBI study](https://www.moneylife.in/article/93-percentage-of-individual-traders-lost-rs18-lakh-crore-in-equity-fo-in-past-3-years-sebi/75210.html)). But the winners are well-capitalised institutions. A retail AI-algo product sells to the losing side of that trade, in a shrinking market:

- **87.7% of individual F&O traders lost money in FY26**, with aggregate losses of ₹91,685 crore ([Open Magazine](https://openthemagazine.com/business/sebi-fo-loss-study-explained-why-9-in-10-retail-traders-lost-91685-crore-in-fy26)).
- Unique individual F&O traders fell from 98.1 lakh to 78.6 lakh ([Outlook Business/PTI](https://www.outlookbusiness.com/markets/sebi-measures-reduce-equity-fo-losses-for-retail-investors-in-fy26)).
- Options contracts traded fell **51.5%** ([Angel One](https://www.angelone.in/news/market-updates/sebi-report-shows-over-50-drop-in-options-trading-volumes-in-fy26-after-f-o-reforms)).

Regulation now loads cost onto exactly the product the friend describes. SEBI's retail algo framework (circular of 4 Feb 2025) became fully applicable on **1 April 2026** ([SEBI](https://www.sebi.gov.in/legal/circulars/feb-2025/safer-participation-of-retail-investors-in-algorithmic-trading_91614.html); [Business Standard](https://www.business-standard.com/markets/news/sebi-extends-retail-algo-trading-framework-rollout-to-2026-125093000956_1.html)). Under it:

- Brokers are principals, and vendors must be empanelled with the exchange.
- Every vendor strategy must be registered ([Zerodha Z-Connect](https://zerodha.com/z-connect/general/a-comprehensive-overview-of-nses-circular-on-the-new-retail-algo-trading-framework)).
- Black-box vendors must also register as SEBI Research Analysts, per vendor summaries; the primary text was not verified ([AlgoBulls](https://algobulls.com/blog/industry-insights-and-updates/sebi-new-algotrading-regulations-for-retail-investors-2026)).
- **Inference:** a "model trained on our algos" is black-box by definition, and a frequently retrained model may trigger re-registration.

The statistics are also against the plan:

- Seven strategy return series are far too small a sample to train a model on.
- "Shown results" is itself a selection filter, which is exactly the bias the Deflated Sharpe Ratio ([SSRN](https://papers.ssrn.com/abstract=2460551)) and the Probability of Backtest Overfitting ([SSRN](https://papers.ssrn.com/abstract=2326253)) were designed to correct.
- Across 97 published predictors, returns fell **58% after publication** ([McLean & Pontiff](https://Www.Gwern.net/doc/economics/2016-mclean.pdf)).
- In two-decade backtests over more than 100 symbols, previously reported advantages of LLM timing strategies "deteriorate significantly" ([FINSABER, arXiv](https://arxiv.org/abs/2505.07078)).

The market is small. AlgoTest, the best-documented independent player, booked about **₹3.2 crore revenue in FY24** ([Inc42](https://inc42.com/company/algotest/funding/)). Zerodha's Nithin Kamath summarises it as: AI can make investors "more disciplined, but not smarter" ([FinBox](https://research.finbox.in/blog/can-ai-transform-investing-all-bets-are-off/)).

**Verdict:** keep quant as a personal capability or for a later SEBI-registered RA/PMS product. Do not build the company on it.

### Claim 2: "Consumer finance apps are crowded with bare-minimum products." True on crowding, wrong on the cause.

The market is concentrated: the top three brokers hold about 58.5% of NSE active clients. But the products are not bare. Groww now has an NBFC, an AMC, PMS/AIF distribution, family wealth features and an AI assistant. The real pattern is economic. Incumbents earn on activity and balances (F&O, MTF, lending), and MF-first apps that tried to earn on advice or direct plans stayed small or were sold (Kuvera, Fisdom, ET Money, above).

**Verdict:** the gap is not missing features. It is jobs that no incumbent is paid to finish: fixing a mis-sold portfolio, recovering a rejected claim, answering a tax notice, claiming a dead parent's deposits.

### Claim 3: "People want end results, not another chatbot." Correct, with a regulatory caveat.

Revealed preference supports the claim:

- Revenue follows automated outcomes (Wealthfront's cash sweep, Cleo's advances).
- Embedded assistants get usage: Robinhood Cortex is reported at about 1M users ([ecosistemastartup](https://ecosistemastartup.com/?p=83399)).
- Standalone chat apps like Hiro fold.

Regulators also define the limit of "end result":

- NPCI's chairman said in September 2026: "AI may recommend, but authentication and final settlement must follow deterministic auditable rules" ([MediaNama](https://www.medianama.com/2026/09/223-npci-ai-agents-upi-payments/)).
- SEBI's adviser rules forbid executing any trade without the client's specific, positive consent for each trade ([Taxguru](https://taxguru.in/sebi/sebi-updates-guidelines-investment-advisers-2025.html)).
- Even the Claude–UPI commerce pilot places orders "with a single confirmation" ([Razorpay](https://razorpay.com/newsroom/razorpay-npci-launch-agentic-payments-on-claude-powering-zomato-swiggy-zepto-at-the-india-ai-impact-summit/)).

**Verdict:** design for completed work up to a one-tap human approval. Chat remains a fine interface, but it should not be the product.

### Claim 4: "Look at 1% Club, a ₹100 cr+ non-AI brand." Right to admire, wrong to copy, and the "non-AI" part is outdated.

Company-reported facts:

- 1% Club charged ₹16,999 for lifetime membership and had about 30,000 members in 2023 ([Inc42](https://inc42.com/startups/how-finance-with-sharan-is-taking-middle-class-indians-toward-financial-freedom-with-the-1-club/)).
- It became the first finfluencer-led SEBI RIA in February 2025 ([YourStory](https://cwv.yourstory.com/2025/02/in-a-first-influencer-sharan-hegde-led-1-club-gets-ria-license)).
- By August 2026 it claimed about 1M students, **₹150 crore+ revenue over three years**, about ₹2,000 crore under advisory, and an AI CFO launch ([Storyboard18](https://www.storyboard18.com/brand-makers/sharan-hegdes-1-club-launches-ai-cfo-for-personalised-financial-planning-portfolio-guidance-107814.htm)).
- Tracxn independently estimates ₹50–100 crore in annual revenue as of March 2025 ([Tracxn](https://tracxn.com/d/companies/1-club/__fYus1qXqYTvCzog_GCtbLNnMOcXRnnzz-kflcbfFDh0)). The "₹100 cr+" label is therefore plausible as a cumulative figure but unverified as annual revenue.

The funnel (free content, then a paid community, then fee-only RIA advice, then AI) is the clearest Indian template. Its co-founder calls the AI CFO the first step toward a "trust layer" that holds a person's full financial context. There is also a warning sign: Ankur Warikoo shut a roughly ₹100 crore courses business, citing AI's impact ([LiveIndia](https://liveindia.tv/business/ankur-warikoo-shuts-down-rs-100-crore-courses-business-after-5-years-says-ai-impact-was-huge/)).

**Verdict:** the moat is audience and trust, which a new founder lacks. 1% Club is now a direct competitor in "AI CFO" for the mass affluent. The lesson to borrow is sequencing: earn trust with a concrete win before asking to manage money. Creators are also a distribution partner, not a model to imitate.

### Claim 5: the MF pilot. Right domain, wrong sequence.

**Scraping "every law, data source and plan" is fine and cheap.**

- NAV and scheme data are free and machine-readable (AMFI, mfapi.in, an open-source archive of all historical NAVs ([GitHub](https://github.com/captn3m0/historical-mf-data))).
- The legal corpus is a few thousand pages.
- Third-party ratings from Value Research or Morningstar must be licensed, not scraped.
- Regulatory Q&A is already commoditised: SEBI runs its own GenAI investor chatbot, SEVA ([Cafemutual](https://cafemutual.com/news/industry/32720-sebi-launches-generative-ai-for-investors)).

**Fine-tuning a small model is the wrong first move.**

- On FinanceBench, fine-tuning the generator **lowered faithfulness from 0.700 to 0.625**, while retrieval-side improvements helped more ([arXiv](https://arxiv.org/html/2404.11792)).
- Frontier models already score **70.4%–89.7% zero-shot** on IndiaFinBench, a set of questions drawn from SEBI and RBI documents ([arXiv](https://arxiv.org/pdf/2604.19298)).
- LLMs are weak at Indian tax computation without tools: one model scored 13.33% on Direct Tax Laws questions from the CA exam ([Moonlight review](https://www.themoonlight.io/de/review/large-language-models-acing-chartered-accountancy)).
- **Inference:** the right architecture is retrieval over versioned documents plus deterministic tools for every number.

**"Validate correctness with 50–70 users" conflates two tests.** Users cannot check a capital-gains figure. Correctness needs a 300–500 item expert-graded golden set; users test usefulness and willingness to pay. The plan also contradicts itself: claim 3 says users do not want a chatbot, yet the pilot ships one.

**"An agent that never touches money" is already mandatory, not a differentiator.** Pooling has been banned since 2022. What actually binds is the licence:

- Naming a fund for a specific user is investment advice and needs SEBI RIA registration.
- Placing orders needs an RIA, ARN, EOP or broker licence.
- An unregistered startup paid by an AMC or broker exposes that partner to SEBI's 2024 rules barring regulated entities from associating with unregistered advisers ([Nishith Desai](https://nishithdesai.com/research-and-articles/hotline/technology-law-analysis/securities-market-regulators-continued-quest-against-unfiltered-financial-advice-15193)).

SEBI impounded **₹546 crore** from a finfluencer whose "trading academy" was found to be unregistered advisory ([Storyboard18](https://www.storyboard18.com/amp/how-it-works/sebi-bans-finfluencer-avadhut-sathe-impounds-rs-546-crore-for-running-unregistered-advisory-85392.htm)).

**Verdict:** flip the plan into licence-aware, outcome-first, retrieval plus tools. As redesigned, the MF idea scores 3.50 (rank 8). It is a credible later module, not the best first product.

## Licences, not models, are the binding constraint

### India: what each kind of product needs

SEBI's December 2024 overhaul made adviser registration far cheaper ([Taxguru](https://taxguru.in/sebi/sebi-eases-rules-investment-advisers-research-analysts-2024-overhaul.html)):

- A graduate degree is enough; the experience requirement was removed.
- A **₹1 lakh deposit** replaces net worth for up to 150 clients.
- SEBI fees are ₹2,000 to apply and ₹3,000 to register for individuals ([SEBI FAQ](https://www.sebi.gov.in/sebi_data/faqfiles/aug-2025/1755174193178.pdf)).

The constraints that matter are these:

- **AI liability.** Since February 2025 any SEBI-regulated entity is solely responsible for AI outputs, whether the AI was built in-house or bought ([Fox Mandal](https://foxmandal.in/News/regulated-entities-responsible-for-output-of-ai-usage-sebi/)).
- **AI disclosure.** Advisers must disclose their AI use to clients.
- **Upcoming AI rules.** SEBI said in August 2026 that tiered AI rules with human oversight and kill switches are coming "shortly" ([ANI](https://aninews.in/news/business/sebi-to-soon-issue-aiml-guidelines-for-capital-markets-mandate-human-oversight-kill-switch-controls-chairman-pandey20260819121850/)). No final circular had been found as of October 2026.

| Product activity | Minimum registration | Cost / time (dated) | Binding constraints |
|---|---|---|---|
| Education chatbot, no scheme picks for a specific user | None | ₹0 | No security-specific recommendations. Education content may only use price data at least 3 months old (Jan 2025) ([Business Standard](https://www.business-standard.com/markets/news/sebi-finfluencer-circular-live-stock-data-market-education-rules-125013000571_1.html)) |
| Personalised fund advice | SEBI Investment Adviser | About ₹5k fees plus ₹1 lakh deposit (≤150 clients); 21–90 days, per consultants | Fee cap; no distribution commission for the same family or group; per-trade consent; AI disclosure and liability |
| Direct-plan execution | RIA for own clients via BSE StAR MF, or EOP Cat-1 (₹1 cr net worth) / Cat-2 (broker) | RIA has nil BSE fee | No pooling; EOPs may not advise or advertise |
| Regular-plan distribution | AMFI ARN (NISM V-A) plus empanelment with each AMC | Low | Earns commission; cannot call itself an "adviser" |
| Algo or trade calls | Broker plus exchange-empanelled vendor; RA for black-box strategies | High | Per-strategy registration |
| Portfolio aggregation via AA | Regulated entity acting as data user (FIU) | ₹5–25 lakh and 5–10 months (vendor estimate) ([CASParser](https://casparser.in/blog/state-of-account-aggregator-2026/)) | CAS-PDF upload needs no licence |
| Insurance comparison or sales for commission | IRDAI web aggregator (₹25 lakh capital), broker or corporate agent ([IRDAI regs](https://financialservices.gov.in/beta/sites/default/files/2024-11/IRDAI%20(Insurance%20Web%20Aggregators)%20Regulations,%202017.pdf)) | High | Acko fined ₹1 cr for paying an unlicensed referral partner |
| Insurance claim and grievance help | None found; Insurance Samadhan operates on success fees | ₹0 | Ombudsman representation rules **not verified**; never take insurer money |
| Loan referral | Lending Service Provider for a regulated lender, under RBI Digital Lending Directions 2025 ([Mondaq](https://www.mondaq.com/india/fin-tech/1636908/digital-lending-directions-2025)) | Medium | Lending app must be reported on RBI's portal; cooling-off period; no third-party fund flows |
| Payments started by an agent | Via a licensed payment aggregator (e.g. Razorpay's agentic product on UPI Reserve Pay) | Partner-dependent | Additional authentication for e-mandates, 24-hour pre-debit notice, ₹15,000 thresholds ([MediaNama](https://www.medianama.com/2026/09/223-anthropic-ai-shopping-agents-upi-india/)) |

Three further rules cut across all categories:

- **DPDP Act.** Data-protection duties phase in through about **May 2027**, with penalties of up to ₹250 crore ([Deccan Herald](https://www.deccanherald.com/india/centre-notifies-dpdp-rules-implementation-planned-in-phases-spread-over-12-18-months-3798465); [Uniqus](https://uniqus.com/digital-personal-data-protection-act-timelines/)). The older IT Act data rules apply in the meantime.
- **Agent payments.** NPCI is reportedly building a registry of AI agents that pay over UPI. No specification, limits or liability rules have been published ([TNGlobal](https://technode.global/2026/09/12/india-npci-ai-agent-registry-upi-payments/)).
- **RBI's FREE-AI framework** (August 2025) is non-binding ([KPMG](https://kpmg.com/in/en/insights/2025/08/rbi-free-ai-committee-report-on-framework-for-responsible-and-ethical-enablement-of-artificial-intelligence.html)).

### Globally: education is cheap everywhere; licensed advice is cheapest in the US

| Jurisdiction | Licence for personalised advice | Capital / cost | Time | AI-specific status (Oct 2026) |
|---|---|---|---|---|
| **US** | State RIA. SEC registration via the internet-adviser exemption only if advice is fully automated through an interactive website ([Federal Register](https://www.govinfo.gov/content/pkg/FR-2024-04-09/html/2024-06865.htm)) | State fees of about $50–500; net worth or bond of $10k–50k in some states | Unverified | Proposed SEC rule on predictive analytics withdrawn June 2025 ([Paul Hastings](https://www.paulhastings.com/insights/client-alerts/sec-withdraws-14-pending-rule-proposals)). Enforcement against "AI washing" ([MoFo](https://mofo.com/resources/insights/240320-sec-targets-ai-washing-with-two-new-settled-cases)). Impersonal content may fall under the publisher's exclusion ([Greenberg Traurig](https://www.gtlaw.com/en/insights/2024/8/no-need-for-seeking-alpha-to-seek-registration)). Open-banking rule 1033 enjoined ([Cozen](https://www.cozen.com/news-resources/publications/2026/section-1033-compliance-date-open-banking-rule-enjoined-and-under-reconsideration)) |
| **UK** | Full advice permission, or the new "targeted support" permission (live 6 Apr 2026) ([Freshfields](https://www.freshfields.com/en/our-thinking/blogs/risk-and-compliance/fca-finalises-targeted-support-rules-applications-now-open-102mmq0)) | Targeted support needs at least £500k regulatory capital ([Brodies](https://brodies.com/insights/pensions/fcas-targeted-support-regime/)) | Up to 6 months by statute | Mills Review (July 2026): no new AI-specific rules; a review of the regulatory perimeter is pending ([FCA](https://www.fca.org.uk/publications/corporate-documents/mills-review)) |
| **EU** | MiFID II investment firm | €75k if no client assets are held ([ESMA](https://www.esma.europa.eu/publications-and-data/interactive-single-rulebook/mifid-ii/article-7-procedures-granting-and)) | 6 months by statute | AI Act high-risk obligations for credit scoring moved to 2 Dec 2027 ([Addleshaw Goddard](https://www.addleshawgoddard.com/en/insights/insights-briefings/2026/technology/eu-ai-act-ai-omnibus-formally-adopted/)). Serving EU clients from outside relies on reverse solicitation, which marketing defeats ([Freshfields](https://www.freshfields.com/en/our-thinking/blogs/risk-and-compliance/finally-some-clarity-on-reverse-solicitation-under-micar-and-beyond-esmas-fi-102jrp8)) |
| **Singapore** | Financial adviser licence | S$300–500k base capital ([MAS](https://www.mas.gov.sg/regulation/capital-markets/apply-for-licensing-or-registration-of-capital-market-entities/financial-advisers)) | Unverified; Sandbox Express targets 21 days | AI risk guidelines consulted on to Jan 2026; not yet final |
| **Hong Kong** | SFC Type 4/9 | HK$4,740 per type | 4–6 months | 2024 GenAI circular treats AI investment advice as high-risk ([Linklaters](https://techinsights.linklaters.com/post/102jp7z/key-implications-of-hong-kongs-new-sfc-circular-on-genai-language-models)) |
| **Australia** | AFSL | Fees vary | 70% of applications decided within 150 days ([HSF Kramer](https://www.hsfkramer.com/notes/fsraustralia/2024-posts/funds-update-18-october-2024)) | No AI-specific rule found |
| **Nigeria** | SEC robo-adviser registration | N100M minimum capital from Jan 2026 ([TechCabal](https://techcabal.com/2026/01/16/sec-2-billion-minimum-capital-for-exchanges/)) | Unverified | Algorithm audits required |

**Inference:** for consumer products, document-assist and grievance services avoid investment licensing almost everywhere. That makes "recover money" products structurally easier to take abroad than "advise on money" products.

## Beyond investing, the largest gaps sit where no incumbent is paid to help

The other problem areas share one pattern. Money is lost because the party that could fix it (insurer, bank, buyer, bureau, tax department) has no incentive to do so, and the consumer or small business lacks the time and knowledge to escalate. AI changes the cost of producing a correct, cited, deadline-tracked case file. That is why success-fee and per-job pricing recur below.

| Domain | Sized pain (dated, sourced) | Why still unsolved | What changed 2024–26 | AI end-result wedge | Licence for an MVP |
|---|---|---|---|---|---|
| **Health insurance, India** | ₹26,037 cr rejected or disallowed (FY24). 3.26 cr claims in FY25, 8% repudiated ([Algates/IRDAI AR](https://algatesinsurance.in/irdai-annual-report-2024-25-highlights/)). Bima Bharosa grievances rose 47,658 → 64,365 → 73,729 (FY24, FY25, FY26 to Feb) ([TaxGuru](https://taxguru.in/?p=1035064)) | Insurers bear little cost when a denial goes uncontested. IRDAI cannot break down rejection reasons by insurer ([Insurance Business Asia](https://www.insurancebusinessmag.com/asia/news/life-insurance/irdai-cannot-explain-why-health-insurance-claims-go-unpaid-583814.aspx)). Bima Bharosa and the Ombudsman are not integrated, so people file twice | IRDAI master circular (Aug 2024): cashless decision in 1 hour, discharge in 3 hours, repudiation needs committee approval ([Moneylife](https://moneylife.in/article/health-insurance-decide-cashless-request-in-1-hour-provide-final-authorisation-for-discharge-within-3-hours-says-irdai/74269.html)) | Claim-recovery agent | None if no commission |
| **Life insurance mis-selling, India** | Unfair-practice complaints rose 23,335 → 26,667 (FY24 → FY25). Surrenders reached 38.3% of total life benefits by FY26 ([Moneylife](https://www.moneylife.in/article/life-insurance-early-exits-rise-to-39-percentage-of-total-benefits-due-to-financial-stress-misselling-govt/81241.html)) | Commission-led sales | Surrender-value rules reset in 2024 | Policy audit with IRR, surrender vs paid-up decision, complaint draft | None (analysis only) |
| **Health insurance, US** | 20% of in-network ACA claims denied; fewer than 1% appealed; about 44% of appeals not upheld (2023, [KFF](https://www.kff.org/private-insurance/claims-denials-and-appeals-in-aca-marketplace-plans-in-2023/)) | Appeals cost the patient time and expertise | CMS-0057-F prior-authorisation rules from 2026 | Appeal agent. Rivals are early: Claimable charges $50 a letter ([PYMNTS](https://www.pymnts.com/artificial-intelligence-2/2026/insurance-denials-meet-their-match-in-ai-powered-appeals/)); Counterforce is free ([Axios](https://www.axios.com/local/raleigh/2025/08/20/using-ai-to-fight-back-against-insurance-denials-counteforce)) | HIPAA authorisation. Unauthorised-practice-of-law risk is unsettled (Nippon Life v. OpenAI) ([Techstrong](https://techstrong.ai/features/nippon-life-sues-openai-alleging-chatgpt-engaged-in-unauthorized-practice-of-law/)) |
| **Credit and debt** | Indian card advances ₹2.95 lakh cr; card bad loans ₹6,778 cr (2025) ([Kashmir Life/RS data](https://kashmirlife.net/credit-card-dues-near-rs-3-lakh-cr-bad-loans-write-offs-rise-428522/)). Household debt 45.5% of GDP (Mar 2026; another RBI publication says 45.8%) ([LoansJagat](https://www.loansjagat.com/news/indian-household-debt-increases-to-45-5-percent-of-gdp-in-march-2026-primarily-due-to-non-housing-retail-loans-rbi)) | Issuers profit from customers who carry balances; credit-report data furnishers have no incentive to correct errors | Credit bureaus must pay ₹100 a day for disputes unresolved after 30 days ([CIBIL](https://www.cibil.com/framework-for-compensation)). RBI's lending-app directory ([Medianama](https://www.medianama.com/2025/05/223-rbi-digital-lending-apps-centralised-directory/)) | Dispute and compensation agent; lending-app checker; payoff plan | None unless acting as a loan referral partner. Oolka raised $14M nearby ([Indian Startup News](https://indianstartupnews.com/funding/fintech-startup-oolka-raises-14-million-to-expand-ai-tools-for-credit-and-personal-finance-11783456)) |
| **Fraud and scams** | India 2025: ₹19,813 cr (I4C) or ₹22,495 cr (Parliament reply), **conflicting**; investment scams about 77% of losses ([IANS](https://ianslive.in/indians-lose-over-rs-52976-crore-to-cyber-frauds-over-six-years-report--20260103154943); [Dynamite News](https://www.dynamitenews.com/national/cyber-frauds-mount-to-rs22495-crore-in-2025-over-rs8000-crore-saved-through-rapid-response-system)). US: $15.9B reported to the FTC ([FTC](https://www.ftc.gov/news-events/news/press-releases/2026/03/ftc-testifies-joint-economic-committee-agencys-efforts-combat-fraud)) | Victim-authorised payments; no reimbursement right in India (none found), unlike the UK where 88% of in-scope losses were reimbursed ([A&O Shearman](https://finreg.aoshearman.com/psr-update-on-impact-of-app-fraud-reimbursement-s)) | RBI proposes a 1-hour delay and trusted-person approval (Apr 2026) ([Moneylife](https://moneylife.in/article/digital-payment-frauds-under-watch-rbi-proposes-1hour-delay-transaction-caps-and-kill-switch-to-counter-scams/80179.html)). DoT launched a phone-number fraud-risk indicator ([Business Standard](https://www.business-standard.com/industry/news/dot-launches-financial-fraud-risk-indicator-to-aid-cybercrime-detection-125052101912_1.html)) | WhatsApp "is this a scam?" agent; family guardian | None; risks are Play Store policy and false labels |
| **SMB receivables** | ₹8.1 lakh cr overdue MSME receivables (CR, Recordent) ([Fintechbiznews](https://www.fintechbiznews.com/fintech-technology/rs81-trn-is-locked-up-in-overdue-receivables)). MSME Samadhaan: 2.57 lakh applications, ₹55,244 cr ([Crisil](https://intelligence.crisil.com/en/homepage/newsroom/press-releases/2026/08/executed-well-msme-bill-can-be-an-ibc-moment-for-delayed-payments.html)) | Suppliers have no leverage over buyers | MSMED Amendment Bill passed August 2026, with 90-day mediation and a 75% pre-deposit before appeal ([IANS](https://ianslive.in/parliament-passes-msme-bill--20260807140603); [Vinod Kothari](https://vinodkothari.com/2026/07/strengthening-msme-ecosystem-msmed-amendment-bill/)). Tax rule 43B(h) delays buyers' deductions for late payments ([Business Standard](https://www.business-standard.com/finance/personal-finance/45-day-msme-payment-rule-impact-and-details-of-section-43b-h-explained-124032600333_1.html)) | Receivables agent: chase, file the case, route to the TReDS invoice-discounting platforms | Light |
| **SMB GST** | ₹74,782 cr of fake input-tax-credit detected in FY26 ([Jurishour](https://www.jurishour.in/gst/cgst-detects-fake-itc-fraud-fy26-unearthed/)). No official count of mismatch notices | The buyer bears the cost when a supplier fails to file | GST invoice management system (late 2024); TallyPrime added built-in AI (June 2026) ([CXO Digital Pulse](https://www.cxodigitalpulse.com/?p=39293)) | Reconciliation plus notice-reply desk for CA firms | Through a licensed GST data provider; a CA files |
| **Individual tax** | Over 7 crore ITRs filed for AY2025-26 ([IANS](https://ianslive.in/more-than-7-crore-itrs-filed-so-far-income-tax-department--20250915180800)). Clear: ₹272 cr revenue, ₹96 cr loss ([Entrackr](https://entrackr.com/fintrackr/clear-reports-rs-272-crore-revenue-and-rs-96-crore-loss-in-fy25-10808038)) | Filing is commoditised; notices are not | Automated mismatch notices against tax-department data ([Outlook Money](https://www.outlookmoney.com/tax/why-2025-tax-notices-are-rising-and-what-taxpayers-must-do-now)) | Notice resolver plus monitoring of the annual information statement | E-return intermediary registration for API filing (unverified) |
| **Household admin** | About ₹2.2 lakh cr unclaimed across banks, shares, insurance, EPF and MFs ([Business Today](https://www.businesstoday.in/amp/personal-finance/news/story/rs-22-lakh-crore-unclaimed-funds-lie-idle-across-banks-epf-insurance-stocks-mfs-524958-2026-04-10)). EPF: about 174 lakh of 796 lakh claims rejected in FY25 ([Business Today](https://www.businesstoday.in/personal-finance/news/story/epfos-instant-pf-withdrawal-promise-has-a-catch-one-in-five-claims-still-gets-rejected-541466-2026-07-07)) | Search is free; claiming is paperwork and branch visits | RBI's UDGAM unclaimed-deposit portal covers about 90% of value ([Outlook Money](https://www.outlookmoney.com/banking/udgam-how-to-claim-unclaimed-bank-deposits-through-rbis-portal)) | Family money finder plus a document pack for each institution | None |
| **Cross-border / diaspora** | India received $135.46B in remittances in FY25 ([NewsOnAir](https://www.newsonair.gov.in/remittances-by-indians-working-abroad-scale-record-high-of-135-billion-in-fy25/)). About 34.3M overseas Indians including PIOs ([Indian News Link](https://indiannewslink.co.nz/malayalis-lead-indias-nri-wealth-inflows)) | Two tax systems: India's TDS refunds and treaty credits, plus US PFIC rules on Indian MFs ([Basunivesh, blog](https://www.basunivesh.com/pfic-rules-for-indian-nris-in-usa-tax-impact-solutions/)) | Remittance apps are moving into investing (Aspora, $53M Series B) ([FinTech Futures](https://www.fintechfutures.com/venture-capital-funding/remittance-platform-aspora-raises-53m-series-b)) | NRI tax and compliance autopilot | CA sign-off for Form 15CB; US preparer rules |
| **B2B for intermediaries** | 3.53 lakh ARN holders ([Cafemutual](https://cafemutual.com/news/industry/38695-mutual-fund-distributor-base-rises-to-353-lakh-in-june-b30-markets-drive-growth)); about 1,000 RIAs; about 1,584 RAs; 515+ PMS managers ([Moneylife](https://www.moneylife.in/article/sebi-unveils-sweeping-reforms-for-portfolio-managers-proposes-overseas-investing-simplified-regulations-and-new-mfpms-framework/81148.html)) | Compliance burden is blamed for falling RIA numbers ([The Ken](https://the-ken.com/sebi-registered-advisors-are-an-endangered-species-so-who-guides-retail-investors/)) | SEBI board approved a common advertisement code on 24 Sept 2026: post-publication reporting within 24 hours replaces prior approval ([exchange4media](https://www.exchange4media.com/marketing-news/sebi-relaxes-advertising-norms-keeps-celebrity-endorsements-under-prior-approval-158597.html)) | Ad classifier, reporting and evidence archive; suitability audit trail | None (B2B software) |

Where these stand on funding and competition:

- **Large banks are taken.** Enterprise BFSI voice AI is already owned by well-funded players: Sarvam reported ₹45.1 crore FY26 revenue at a $1.5B valuation ([Inc42](https://inc42.com/buzz/sarvam-becomes-indias-130th-unicorn-after-raising-234-mn/)), and Gnani reported about ₹54 crore ([Business Today](https://www.businesstoday.in/amp/technology/story/gnaniai-raises-10-million-in-funding-from-aavishkaar-capital-to-scale-global-voice-ai-push-523218-2026-03-31)).
- **Direct-to-MSME software loses money.** Vyapar lost ₹63 crore in FY25 ([Entrackr](https://entrackr.com/fintrackr/vyapar-posts-rs-63-cr-loss-in-fy25-cash-reserve-fades-93-10819211)).
- **Incentive problems with a recoverable cash outcome remain open.** Neither of the first two groups covers them.

## Scoring fourteen ideas puts claim recovery first

### Scoring criteria

Each idea was scored 1 (poor) to 5 (strong) on eight criteria, then weighted. The scores are the author's judgement from the evidence above, not sourced facts.

| Criterion | Weight | What a 5 means |
|---|---|---|
| Pain and evidence | 15% | Regulator or official data shows large, recurring losses |
| Revenue ceiling | 15% | Credible path to more than ₹100 cr in annual revenue, or a global market |
| Willingness to pay and monetisation clarity | 15% | Proven price points, or a success fee taken from recovered money |
| End-result agent fit | 10% | Multi-step, rule-based, with a measurable rupee outcome |
| Regulatory ease | 10% | No licence needed for the MVP |
| Competitive white space | 10% | No AI-native or funded incumbent doing the full job |
| Distribution reachability for 1–3 people | 15% | Intent-driven search or a concentrated, reachable buyer channel |
| Build feasibility in 90 days | 10% | Public or user-supplied data; no partner gating |

### Matrix

| Rank | Idea | Pain | Ceiling | WTP | Agent fit | Reg. ease | White space | Distribution | Build | **Weighted /5** |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | **Health-claim recovery agent (India first)** | 5 | 4 | 4 | 5 | 4 | 4 | 3 | 4 | **4.10** |
| 2 | MSME receivables and delayed-payment agent | 5 | 5 | 3 | 5 | 4 | 4 | 2 | 3 | **3.85** |
| 3 | GST reconciliation and notice desk for CA firms | 4 | 4 | 4 | 4 | 4 | 2 | 4 | 3 | **3.70** |
| 4 | Compliance copilot for SEBI intermediaries | 3 | 2 | 4 | 4 | 5 | 4 | 4 | 4 | **3.65** |
| 5 | Family money finder and transmission concierge | 4 | 4 | 3 | 3 | 5 | 4 | 3 | 3 | **3.60** |
| 6= | NRI cross-border tax and compliance autopilot | 4 | 4 | 4 | 4 | 3 | 4 | 3 | 2 | **3.55** |
| 6= | US health-denial appeal agent | 5 | 5 | 3 | 5 | 3 | 2 | 2 | 3 | **3.55** |
| 8 | MF portfolio fixer under an RIA licence (friend's pilot, redesigned) | 5 | 4 | 3 | 5 | 3 | 2 | 2 | 4 | **3.50** |
| 9 | Personal tax-notice resolver and annual-information-statement watcher | 4 | 4 | 3 | 4 | 3 | 3 | 3 | 3 | **3.40** |
| 10 | Scam-check agent plus family guardian | 5 | 3 | 1 | 3 | 4 | 3 | 3 | 4 | **3.20** |
| 11 | Credit-report dispute and compensation agent | 3 | 3 | 2 | 4 | 3 | 3 | 3 | 4 | **3.05** |
| 12 | AI notetaker and CRM for MFDs and RIAs (Jump analog) | 3 | 3 | 2 | 3 | 4 | 2 | 3 | 4 | **2.95** |
| 13 | Fine-tuned MF chatbot leading to an investing agent (friend's pilot as stated) | 3 | 3 | 1 | 2 | 2 | 1 | 2 | 3 | **2.15** |
| 14 | Retail AI-algo trading product | 2 | 2 | 3 | 3 | 1 | 1 | 2 | 2 | **2.05** |

**Sensitivity.** Claim recovery scores 4 or 5 on seven of eight criteria; no other idea does that. It stays first under two alternative weightings tested:

- **Distribution 25%, ceiling 5%:** claim recovery 4.00, then the SEBI compliance copilot at 3.85.
- **Ceiling 25%, distribution 5%:** claim recovery 4.20, then MSME receivables at 4.15.

Founder-specific advantages would change the order:

- A CA-practice network would lift the GST desk.
- An existing audience would lift the MF fixer by roughly 0.3–0.45, because its distribution score would rise from 2 to 4 or 5.

Ideas 13 and 14 sit at the bottom because they fail on licensing, white space and willingness to pay at the same time.

### Idea cards for the leading candidates

**1. Health-claim recovery agent (India first, US later)**

| Field | Detail |
|---|---|
| Problem | Rejected and partially paid health claims: ₹26,037 cr rejected or disallowed in FY24; over 50% of claimants report rejection or partial approval (LocalCircles survey; base unclear) ([Business Today](https://www.businesstoday.in/amp/personal-finance/insurance/story/insurance-claims-over-50-health-cover-claims-faced-rejection-or-partial-approval-says-survey-459394-2025-01-02)) |
| Target user | Urban salaried families with individual or family-floater policies; adult children handling parents' claims. Later: employer HR teams and RIAs/MFDs who offer it to clients |
| Why unsolved | Insurers profit from uncontested deductions. Consumers do not know the escalation ladder: insurer grievance officer, then Bima Bharosa or the Ombudsman after 30 days, then consumer court ([Outlook Money](https://www.outlookmoney.com/insurance/mis-selling-complaints-grew-112-since-2024-value-of-disputed-claims-rose-10-report)). The incumbent, Insurance Samadhan, is human-operated, with about ₹6.2 cr revenue in FY25 ([Inc42](https://inc42.com/company/insurance-samadhan/financials/)) |
| Why now | Long-context LLMs can read policy wordings and discharge summaries. The 2024 IRDAI master circular created citable rules. Grievance volumes are rising. US analogs were funded in 2025–26. Hindi and regional speech-to-text costs about ₹30 an hour (Sarvam) ([Sarvam pricing](https://docs.sarvam.ai/api-reference-docs/getting-started/pricing)) |
| What the agent does end-to-end | 1. Takes in the policy schedule and wording, rejection or settlement letter, discharge summary and bills (WhatsApp or web). 2. Classifies each deduction: room-rent proportionate deduction, waiting period or pre-existing disease, "non-payable" items, documentation gaps. 3. Cites the clause and the IRDAI rule for each. 4. Computes the amount recoverable. 5. Drafts the insurer grievance, then the Bima Bharosa and Ombudsman filings. 6. Walks the user through portal submission with their own OTP. 7. Tracks deadlines and insurer replies; escalates. 8. Logs the outcome to the case database |
| Licensing path | No IRDAI licence for grievance help, provided the product never sells policies or takes insurer or partner commissions. **Legal opinion needed** on representation before the Ombudsman and on the Advocates Act |
| Data / rails | User-supplied documents; insurers' published policy wordings; IRDAI circulars; Ombudsman awards where published; later Bima Sugam (launch targeted Nov 2026, weak source) ([IPO Market](https://www.ipomarket.in/news/bima-sugam-upi-moment-insurance-irdai-not-ipo)) |
| Monetisation | Hypotheses to test: a small upfront filing fee plus a 10–15% success fee; B2B2C licence fees from RIAs and brokers who want claim support for clients; employer plans. Benchmark: Insurance Samadhan's self-reported ₹160 cr recovered across 18,000 complaints, about ₹89k per resolved case (arithmetic on company figures) ([Entrackr](https://entrackr.com/snippets/insurance-samadhan-secures-rs-85-cr-to-boost-tech-infrastructure-9040178)) |
| Competition | Insurance Samadhan (₹8.5 cr raised in 2025); Ditto (an advisory-led broker with claim support; about ₹97.1 cr FY25 revenue, Inc42 estimate) ([Inc42](https://inc42.com/company/ditto-insurance/)); free consumer forums. No AI-native player found |
| Feasibility (1–3 people) | High. The MVP is retrieval over policy text, rules and drafting with human review. Main risks are distribution at the moment of rejection and collecting fees after recovery |

**2. MSME receivables and delayed-payment agent**

| Field | Detail |
|---|---|
| Problem | Small suppliers wait an average of 73 days to be paid ([Telangana Today, Recordent](https://telanganatoday.com/indian-msmes-face-mounting-delayed-payments-recordent-report-reveals)). ₹20,979 cr was still pending in MSME Samadhaan cases as of 14 Aug 2026 ([Crisil](https://intelligence.crisil.com/en/homepage/newsroom/press-releases/2026/08/executed-well-msme-bill-can-be-an-ibc-moment-for-delayed-payments.html)) |
| Target user | Micro and small suppliers with Udyam registration, reached through their CAs |
| Why unsolved | Power asymmetry: suppliers fear losing the customer. Enterprise accounts-receivable AI tools (e.g. Fazeshift, $17M Series A) target mid-market companies ([Pipeline Road](https://pipelineroad.com/news/20260507-fazeshift-secures-17m-series-a-for-ai-driven-accounts-receiv)) |
| Why now | MSMED Amendment 2026 timelines (presidential assent not confirmed); 43B(h) gives a non-hostile lever, since the buyer's tax deduction is at stake; mandatory TReDS onboarding for state-owned companies |
| Agent end-to-end | Ingests invoices, GST data and Tally exports. Scores buyers. Sends escalating multilingual reminders citing 43B(h) and statutory interest. Computes interest. Assembles the Samadhaan or council filing pack at day 45 and above. Routes eligible invoices to TReDS |
| Licensing | Light: the agent acts for the creditor on B2B debt. DPDP consent applies |
| Data / rails | GST returns, Tally, bank feeds via an AA partner, MSME Samadhaan, TReDS |
| Monetisation | 5–15% of recovered amounts (vendor benchmark ([Boostly](https://invoice.boostly.com/blog/best-ai-debt-collection-software))) or a monthly SaaS fee |
| Competition | Recordent (credit data); Xero and Intuit agents (not India-focused); Tally bundling risk |
| Feasibility | High to build; distribution to MSMEs is hard and MSME willingness to pay is weak, so the CA channel is required |

**3. GST reconciliation and notice desk for CA firms**

| Field | Detail |
|---|---|
| Problem | GST return mismatches trigger templated notices; small taxpayers pay CAs case by case |
| Target user | CA practices (98,967 firms; 159,557 members holding practice certificates) ([TaxConcept](https://taxconcept.net/icai/statistics-of-icai-members-students-firms-till-28th-february-2025/)) |
| Why unsolved | Existing tools reconcile but leave the action (chase the supplier, reverse credit, draft the reply) to a person |
| Why now | GST invoice management system; enforcement rising (FY26 fake input-tax-credit detections were double FY24's); US analog Basis valued at $1.15B |
| Agent end-to-end | Continuous reconciliation of purchase data against the books → list of actions per supplier → reminders sent to suppliers → notice intake → evidence assembly → draft reply for CA sign-off |
| Licensing | Data access through a licensed GST data provider; the CA files and represents |
| Monetisation | Price per GSTIN per month plus a per-notice fee. ICAI's member-benefits portal is a proven channel: Suvit is listed there at a 50% discount ([ICAI](https://bs.icai.org/suvit-2/)) |
| Competition | Clear, Suvit, Zoho, Tally's built-in AI, Accu Reco |
| Feasibility | Medium-high; legal accuracy needs a human in the loop |

**4. Compliance copilot for SEBI intermediaries**

| Field | Detail |
|---|---|
| Problem | Advertising, AI-use disclosure and record-keeping duties are pushing advisers out of the industry |
| Target user | About 1,000 RIAs, about 1,500 RAs, 515+ PMS managers, about 3,350 top MFDs ([Cafemutual](https://cafemutual.com/news/industry/38760-top-mfds-count-rises-to-over-3350-in-fy-2026)) |
| Why now | The common advertisement code turns compliance into a logging and evidence problem; a six-month transition was proposed in the draft ([Mondaq](https://www.mondaq.com/india/fund-management-reits/1826178/sebis-proposal-for-a-common-advertisement-code-financial-advertisements-under-the-regulatory-lens)) |
| Agent end-to-end | Classifies every post or broadcast (ad or not; celebrity or not) → checks it against the code → files the 24-hour report → archives evidence → generates suitability rationale and AI-use disclosures |
| Licensing | None |
| Monetisation | ₹20–50k per firm per year. Illustrative ceiling of about ₹7.5 cr a year across RIAs and RAs (**inference**). Expansion to brokers and MFDs, or to the 16,544 US RIAs ([ThinkAdvisor](https://www.thinkadvisor.com/2026/06/03/number-of-rias-sets-new-record-report/)), where Smarsh and Red Oak compete |
| Feasibility | High; but a small market. Best as a second product or a cash-generating side line |

**5. Family money finder and transmission concierge**

| Field | Detail |
|---|---|
| Problem | Unclaimed bank deposits: ₹72,454 cr (Jan 2026) versus ₹86,917 cr (Jun 2026) in different government replies (**conflict**) ([Free Press Journal](https://www.freepressjournal.in/business/unclaimed-bank-deposits-in-rbis-dea-fund-reach-72454-crore-government-promotes-udgam-portal-multiple-nominations); [Outlook Money](https://www.outlookmoney.com/banking/rs-86917-crore-in-unclaimed-bank-deposits-sbi-accounts-for-largest-share)). Unclaimed shares with the government's IEPF: ₹89,004 cr ([Business Today](https://www.businesstoday.in/amp/personal-finance/investment/story/reliance-industries-tops-iepf-unclaimed-shares-rs89000-crore-stuck-across-1671-companies-report-525182-2026-04-12)) |
| Target user | Adult children and NRIs settling a parent's estate |
| Agent end-to-end | Searches UDGAM, IEPF, MF registrar portals and insurer pages → ranked claim list → document pack for each institution (claim forms, indemnities, succession thresholds) → tracking |
| Licensing | None |
| Monetisation | Per-claim fee or success fee. Willingness to pay is untested |
| Feasibility | Medium: some claims require branch visits, and IEPF claims are slow. A strong module to add to idea 1 |

**6. NRI cross-border tax and compliance autopilot**

| Field | Detail |
|---|---|
| Problem | NRIs face TDS on gross gains, refunds only after filing ITR-2, treaty credits, a $1M-per-year cap on repatriating NRO funds ([Finnovate](https://www.finnovate.in/learn/blog/nri-repatriation-rules-explained)), Form 15CA/15CB (CA certificate about ₹3–10k, vendor estimate) ([Belong](https://getbelong.com/blog/returning-nris/repatriation-guide.md)), and US PFIC forms for Indian MFs |
| Target user | US-resident NRIs first: highest pain and income |
| Agent end-to-end | Ingests NRE/NRO statements, CAS, Indian tax data, US 1099s → determines residency → computes treaty credits and TDS refunds → produces a CA-ready Indian return plus a CPA-ready Form 8621/FBAR packet |
| Licensing | CA signature for 15CB; US preparer rules; no SEBI licence if the product does not advise on investments |
| Competition | Aspora, Abound (planning an AI "autopilot" ([IBS Intelligence](https://ibsintelligence.com/ibsi-news/abound-near-ai-build-ai-financial-autopilot-for-nris/))) and Belong ($5M seed) are adjacent, but none files taxes |
| Feasibility | Medium-low for a first product: two tax systems and liability. Strong second product for global reach |

**7. MF portfolio fixer under an RIA licence (the friend's pilot, redesigned)**

| Field | Detail |
|---|---|
| Problem | Regular-plan cost drag, untaxed-gain harvesting, overlap, parents' legacy folios |
| Target user | Salaried 25–45 year-olds with ₹5–50 lakh in MFs; their parents |
| Agent end-to-end | CAS upload → diagnosis in rupees → tax-staged switch plan within the ₹1.25 lakh LTCG exemption → orders through BSE StAR MF under the RIA, with explicit consent per order → payment from the user's own bank → annual harvest run |
| Licensing | Corporate RIA: ₹1 lakh deposit, graduate principal officer; disclose AI use; no commissions |
| Monetisation | Per-job fees (e.g. a migration plan) or an annual RIA fee; the price band is unproven |
| Competition | Groww GR-1, INDmoney, ET Money Genius, 1% Club AI CFO, Novelty Wealth |
| Feasibility | High to build; low distribution without an audience. Recommended as a **later module** for users won through idea 1 |

The US health-denial appeal agent (rank 6=) uses the same engine as idea 1, with US plan documents and KFF-documented denial categories. It is deliberately sequenced after India because HIPAA and the unsettled question of AI as unauthorised legal practice raise the cost of going first there.

## Recommended first MVP: a claim-recovery agent that finishes the job

### Why this, and not the investing idea

This product fits all three of the friend's sound instincts:

- It delivers a finished result (money back), not a chat.
- It builds the trust layer 1% Club describes, starting from a concrete win.
- It never touches money.

It also avoids all three failure modes of the original pilot. It needs no SEBI licence, no fine-tuning and no claim to have trading edge.

The economics are legible. The disputed-value pool is **about ₹26,000 crore a year**. **Illustrative inference:** helping recover 2% of that pool at a 15% fee would be about ₹78 crore of revenue a year in India alone. The US denial market is the second leg.

The bear case is real:

- Insurance Samadhan's revenue of about ₹6.2 crore after years of operation suggests the human-operated version caps out early.
- Demand is episodic.
- Insurers may resist.

The MVP must therefore prove that AI cuts the cost per case enough, and that intent-driven acquisition works.

### Product design and architecture

**User flow.** The user forwards documents on WhatsApp or uploads them on the web. Hindi and regional-language voice notes are accepted. Within minutes the user receives a "claim X-ray":

- each deduction, with the clause cited;
- the amount likely recoverable;
- a recommended route, with the deadline.

On acceptance, the agent drafts the insurer grievance. A human reviewer approves it, and the user submits it with a guided walkthrough using their own login and OTP. If the insurer does not resolve it within 30 days, the agent prepares the Bima Bharosa and Ombudsman filings and keeps a dated case file.

**AI approach (following the technical evidence, not the friend's plan):**

- **Models:** a frontier or mid-tier model accessed by API, with no fine-tuning.
- **Retrieval:** a hybrid search index over a versioned corpus: the top insurers' published policy wordings, starting with the insurers that draw the most Ombudsman complaints (Star Health 12,186 in FY25; Care 4,423; Niva Bupa 3,983) ([Cafemutual](https://cafemutual.com/news/industry/36635-41-of-health-insurance-complaints-were-resolved-in-favour-of-policyholders-in-fy25)), plus IRDAI circulars.
- **Deterministic tools:** for every number (proportionate-deduction maths, sub-limits, waiting periods, deadlines). The model is forbidden from stating any figure that did not come from a tool or a cited clause.
- **Review and logs:** a human-review gate on every outbound letter during the pilot, and an append-only audit log.
- **Cost:** API spend for 70 pilot users is estimated at under $200 a month (inference based on list prices ([braindetox](https://braindetox.kr/en/posts/ai_api_pricing_comparison_2026.html))).

**Legal and compliance checklist before launch:**

1. A written legal opinion on Ombudsman representation, the Advocates Act, and the enforceability of the success-fee contract.
2. A policy that the product takes no money from insurers, brokers or hospitals.
3. A health-data consent and deletion flow that meets the IT Act data rules now and DPDP duties from 2027.
4. Plain disclosure that AI drafts and a human reviews.

### 90-day plan

| Weeks | Workstream | Deliverables | Gate to pass |
|---|---|---|---|
| 0–2 | Discovery and legal | 30 interviews with recently rejected claimants (consumer forums, social groups, RIA/MFD client lists); 100 anonymised rejection files collected with consent; legal opinion commissioned; pricing hypotheses written | At least 20 of 30 interviewees say they would pay to recover the money; no legal blocker |
| 2–5 | Corpus and evaluation | Wordings for the top 8–10 retail health products; IRDAI rules library; deduction taxonomy; **golden set of 200–300 annotated deductions** with ground-truth clause and amount | Golden set signed off by an ex-TPA or claims specialist |
| 3–7 | Build v0 | WhatsApp and web intake, OCR, retrieval, deduction calculator, letter templates (insurer, Bima Bharosa, Ombudsman), deadline tracker, review console | Clause-citation precision ≥95% and zero invented clauses on the golden set; amounts within ±2% |
| 6–12 | Concierge pilot | 50–100 live cases. Founders and the reviewer handle exceptions by hand. Three acquisition channels tested: search landing pages in English and Hindi for "claim rejected"; 3–5 RIA/MFD/insurance-adviser partners offering it to clients; 2 employer HR teams | See validation metrics below |
| 10–13 | Decision | Unit-economics read-out, cohort of insurer responses, decision memo | Continue, pivot to B2B, or stop |

### Validation approach and kill criteria

The 90-day test measures leading indicators, because Ombudsman outcomes can take longer than the pilot. Thresholds are the author's proposals:

| Question | Metric | Continue if | Pivot / stop if |
|---|---|---|---|
| Do people come at the moment of pain? | Share of qualified leads who upload documents | ≥40% | <20% |
| Is the engine correct? | Golden-set clause precision; reviewer edit rate on live letters | ≥95%; edits falling below 30% by week 12 | Persistent invented clauses |
| Does it recover money? | Full or partial reversal at insurer stage within 30 days, across ≥50 filed cases | ≥25% (for context, about 41% of health Ombudsman complaints went the policyholder's way in FY25) | <15% |
| Will they pay? | Share accepting the fee terms; fees actually collected after recovery | ≥30% accept; ≥70% of owed success fees collected | <20% accept |
| Can it scale cheaply? | Acquisition cost per paid case vs expected fee; reviewer minutes per case | Acquisition cost < 30% of expected fee; review time falling below 20 minutes | Acquisition cost exceeds expected fee in every channel |

Pivot paths if the gates fail:

- **Correctness and recovery pass, but consumer acquisition fails:** sell the engine B2B2C to RIAs, MFDs, brokers and HR teams as white-label "claim support".
- **Fee collection fails:** move to a flat per-filing fee.
- **Recovery fails:** stop and redeploy the document-and-escalation engine to idea 5 (family money finder) or idea 9 (tax notices). Both reuse about 70% of the stack (inference).

### Risks and mitigations

| Risk | Mitigation |
|---|---|
| Insurer pushback or blacklisting of templated complaints (the CFPB already flags AI-generated "duplicative and spurious" complaints in the US ([Orrick](https://infobytes.orrick.com/2026-04-10/cfpb-reports-complaint-volume-doubled-in-2025-citing-surge-in-credit-reporting-disputes/))) | Evidence-backed letters written for each case only; human review; no mass filing |
| Legal-practice or representation challenge | Legal opinion first; the user signs and submits; position the product as drafting software plus a service |
| Hallucinated clause or amount | Numbers come only from tools; citations are mandatory; golden-set tests run before every release |
| Episodic demand and high acquisition cost | Intent search, B2B2C partners, employer channel; widen scope to life mis-selling and unclaimed money to raise value per user |
| Regulatory change (e.g. the proposed internal ombudsman inside insurers) | Treat any new forum as another filing route the agent supports |

### Roadmap after day 90 (inference)

- **Months 4–9:** extend into life-insurance mis-selling audits (26,667 unfair-practice complaints in FY25) and the family money finder. The goal is a "household back office" that families trust because it has already returned money.
- **Months 6–12:** port the engine to US health-denial appeals, using user-in-the-loop filing and HIPAA-compliant processing.
- **After product-market fit:** register a corporate RIA and add the MF portfolio fixer as an upsell to users who already trust the brand. This is the friend's mutual-fund vision, reached through distribution the founder has earned rather than through a cold start.

## Conclusion

The evidence moves the question from "which financial product can AI build?" to "where is money lost because no one is paid to fix it?" In Indian investing, the AI features incumbents are converging on (analyst-style insight, portfolio health checks, read-only connectors) are being given away by companies that earn on derivatives and balances. Competing there means fighting Groww's distribution with a weaker licence position.

The durable openings sit in incentive gaps: rejected claims, delayed MSME invoices, unanswered tax notices, forgotten deposits. In each, the counterparty profits from inaction, and an AI that produces a correct, cited, deadline-tracked case file changes the economics of fighting back. This also answers the friend's best instinct. "End results" in regulated finance means a finished case file or an executed order that the human approves with one tap. The first company in India to show it can repeatedly turn documents into recovered rupees will own the trust the friend admired in 1% Club, and can earn the right to manage money afterwards.

---

*Method and confidence note.* This memo synthesises 19 research notes compiled on 7 October 2026. Most figures come from secondary coverage of regulator, parliamentary and company filings, not the primary documents.

Unverified or conflicting items that matter for the decision:

- Insurance Ombudsman representation rules for non-lawyers (unverified).
- FY25 Ombudsman totals: 37,431 versus 53,102 (conflicting).
- India 2025 cyber-fraud losses: ₹19,813 cr versus ₹22,495 cr (conflicting).
- Unclaimed deposit balances, which differ by publication date (conflicting).
- Presidential assent to the MSMED Amendment Bill 2026 (not confirmed).
- Final SEBI AI/ML guidelines (not yet issued).
- The black-box RA requirement in the algo framework (from vendor summaries).
- Bima Sugam's launch date (weak source).

All scores, sizing arithmetic, price hypotheses and thresholds are the author's inferences. Each should be tested in the 90-day pilot before any capital commitment.
