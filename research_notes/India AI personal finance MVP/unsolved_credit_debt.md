# Unsolved consumer credit and debt problems that AI plus new data rails can now address (global, as of Oct 2026)

Method note: roughly 27 searches and 1 page fetch (the NY Fed Q2 2026 release). The search tool returns summaries rather than full pages, so many figures are secondary. Where a figure is old or from a vendor, that is flagged. Product concepts, feasibility and regulatory-path judgments sit under "Inferences" because they are my reasoning, not sourced facts. Items I could not source are under "Gaps".

## Problem 1: Credit invisibles, thin-file and new-to-credit borrowers, and cash-flow underwriting

### Takeaway
The headline "26M US credit invisibles" is out of date: the CFPB itself cut its estimate by about half in June 2025 (7.0M invisible, about 25M unscored). The underlying problem, that bureau files do not capture people's real repayment ability, persists. Cash-flow scores (UltraFICO GA May 2026, Plaid CashScore, Nova Credit) are arriving, but lender and GSE adoption, and the data-access economics, are still the bottleneck. India's AA rail is the most advanced version of this.

### Cited Findings
- CFPB's June 2025 correction puts credit invisible adults at about 7.0M (2.7% of adults) as of Dec 2020. The 2015 report's 25.9M (11.0%, Dec 2010) is now restated as 13.5M (5.8%). The error came from excluding records with only deferred student loans, collections or closed accounts. 9.8% of adults (about 25.3M) are unscored, 5.9% with stale files and 3.9% with too little history. — [PYMNTS on the CFPB correction](https://www.pymnts.com/consumer-finance/2025/cfpb-corrects-invisible-count-as-millions-struggle-to-shake-credit-limbo); [CFPB PDF, June 2025](https://files.consumerfinance.gov/f/documents/cfpb_update-credit-invisibles-estimate_2025-06.pdf)
- The original 2015 CFPB report said 26M were invisible and 19M unscored, skewed to Black and Hispanic consumers and low-income neighbourhoods. — [CFPB 2015 newsroom](https://www.consumerfinance.gov/about-us/newsroom/cfpb-report-finds-26-million-consumers-are-credit-invisible/?1=1)
- Experian and Oliver Wyman (Jan 2022) claimed expanded data could help nearly 50M "credit invisible and unscoreable" Americans. This is a vendor study and the methodology was not verified. — [BusinessWire](https://www.businesswire.com/news/home/20220112005355/en/Experian-and-Oliver-Wyman-Find-Expanded-Data-and-Advanced-Analytics-Can-Improve-Access-to-Credit-for-Nearly-50-Million-Credit-Invisible-and-Unscoreable-Americans)
- FICO announced general availability of the next-generation UltraFICO Score on 20 May 2026. It uses consented bank data via Plaid (12,000+ institutions) and stays on the standard FICO scale. FICO claims a 7% relative increase in approvals at no incremental risk (vendor claim). A Chase page said that as of April 2026 UltraFICO was pilot-only. — [FICO IR release](https://investors.fico.com/news-releases/news-release-details/next-generation-ultraficor-score-now-available/); [Chase](https://www.chase.com/personal/credit-cards/education/credit-score/what-is-an-ultra-fico-score)
- Plaid's Consumer Report (24 months of data) and its CashScore (built with Prism Data) are offered under Plaid's consumer-reporting-agency status. Nova Credit sells Cash Atlas and reportedly raised a $35M Series D in Oct 2025 (secondary source). — [Fintech Nexus on Plaid](https://fintechnexus.com/?p=59956); [Owler on Nova Credit](https://www.owler.com/company/neednova)
- Freddie Mac's LPA and Fannie Mae's underwriting now accept 12+ months of consented cash-flow data, and it can only help the borrower (Freddie). I found no evidence that the GSEs accept a standalone UltraFICO or CashScore. — [National Mortgage News on Freddie](https://www.nationalmortgagenews.com/news/freddie-mac-to-allow-cash-flow-history-in-underwriting)
- FHFA, 22 Apr 2026: an interim phase lets approved lenders deliver loans using either Classic FICO or VantageScore 4.0. Tri-merge remains. FICO 10T is on the path to approval and FHA will allow VantageScore 4.0 and FICO 10T. — [Docutech](https://blog.docutech.com/fhfa-implements-new-credit-score-models); [BHFS](https://www.bhfs.com/insight/fhfa-and-hud-greenlight-credit-scoring-changes/)
- US data-access rail is unstable. The CFPB's section 1033 rule (compliance was due April 2026) is enjoined or under reconsideration. A replacement proposal went to OIRA in early Aug 2026 and publication is expected in Q4 2026 (a prediction). JPMorgan began charging aggregators such as Plaid in 2025 (it cited 1.89B aggregator requests in June 2025, with only about 13% tied to a live customer action). — [Consumer Finance Monitor, Aug 2026](https://www.consumerfinancemonitor.com/2026/08/06/cfpb-sends-new-section-1033-open-banking-proposal-to-oira-for-review/); [PaymentsJournal](https://www.paymentsjournal.com/stripe-leads-pushback-against-jpmorgans-data-access-fees/)
- India: Sahamati reports 500M+ fulfilled AA consents (as of Sep 2026), 1,100+ regulated entities live, and 2.8B+ accounts enabled. AA-enabled lending in FY26 was Rs 3.82 lakh crore across 3.68 crore loans (about 1.08% of GDP), or 8.4% of retail and MSME lending by value and 11.8% by volume. FY25 was about Rs 1.07 trillion across 12.2M loans. These are industry self-reported figures and IMPRI notes that comparable detail is hard to verify. — [Sahamati H1 FY26](https://sahamati.org.in/wp-content/uploads/2026/01/Credit-Reimagined-H1-FY26-Abridged-1.pdf); [Business Standard](https://www.business-standard.com/finance/news/nbfcs-lead-account-aggregator-consents-in-fy25-with-60-share-125100600872_1.html)
- India NTC: TransUnion CIBIL says about 74% of credit-eligible Indians had a formal loan by March 2026 (35% in 2017), but the NTC share of retail originations fell from 32% to 13%. Credit-active consumers rose from 11% to 28%. Only 8% of new card additions were NTC versus 26% a year earlier. A "66 million NTC" headline exists, but I could not date it. — [Business Today, 30 Jul 2026](https://www.businesstoday.in/amp/latest/economy/story/move-over-maharashtra-tamil-nadu-up-mp-and-bihar-are-big-drivers-of-indias-credit-growth-546278-2026-07-30); [IBEF](https://www.ibef.org/news/first-time-borrowers-deepen-credit-reach-credit-uptake-among-eligible-indians-more-than-doubled-to-74-in-march-from-35-in-2017); [Outlook Business](https://www.outlookbusiness.com/news/india-s-new-to-credit-ntc-consumers-rise-to-66-million-millennials-women-lead-report-news-264258)
- Global: Findex 2025 says about 59% of adults in low- and middle-income economies borrowed in 2024, but only about a quarter of adults (two in five borrowers) used formal credit. Over 45% of adults in Sub-Saharan Africa, South Asia and MENA borrowed informally only. — [Nairametrics on Findex 2025](https://nairametrics.com/2025/07/18/world-bank-59-of-adults-in-nigeria-and-others-borrowed-in-2024/); [CGAP](https://www.cgap.org/research/podcast/whats-next-for-financial-inclusion-unpacking-findex-2025)

### Inferences
- The "invisible" problem has shifted from "no file" to "file does not reflect ability to repay". The practical market is the roughly 25M US unscored plus the "thin but present" segment: immigrants, gig workers, and people whose only trace is a derogatory or student-loan record.
- Why it persists: (a) lenders need a score that is portable to secondary markets and GSEs; (b) bureaus have no incentive to cannibalise their own data; (c) bank-data access in the US now carries fees and legal uncertainty; (d) adverse-action explainability (ECOA/Reg B) limits black-box models.
- Product concept ("consumer-side cash-flow passport"): the user links accounts, or in India approves an AA consent. An LLM and ML layer builds a lender-readable underwriting packet (income stability, rent and utility payments, buffer, obligations) and a plain-language explanation. It matches the user to lenders that accept packets, and sends the packet through the lender's existing portal. Revenue comes from lender referral or per-funded-loan fees.
- Feasibility for a small team: in India this is high, because AA is a regulated, standard, low-cost rail with FIU onboarding via a TSP (technology service provider) and AA-licensed partners. In the US it is medium, because Plaid or MX access is feasible but costs are rising and lender integrations are slow. Regulatory path: in India, work as an LSP/DLSA (lending service provider) partnered with an RE (regulated entity) under RBI Digital Lending Directions 2025, and have the RE's DLA appear in the RBI directory. In the US, this likely triggers FCRA consumer-reporting-agency status (Plaid itself uses it) unless the product is purely consumer-facing and the consumer controls onward sharing.

### Gaps
- No post-2020 official US estimate of invisible or unscored consumers.
- No dated, sourced India NTC headcount for 2026.
- No independent audit of Sahamati's lending figures.
- UK, EU, LatAm and Africa cash-flow underwriting adoption not researched in this pass.

## Problem 2: Predatory digital lending apps and recovery harassment (India, Kenya, Nigeria, Indonesia, SEA)

### Takeaway
The regulatory response (India's RBI directory plus Google Play gating, Kenya's CBK licensing, Nigeria's FCCPC registration, Indonesia's Satgas PASTI) is working at the app-listing layer but the harm migrates to sideloaded or cloned apps, and the actual abuse (contact scraping and shaming) happens at the call-centre layer. Borrowers have no cheap way to verify a lender or evidence harassment.

### Cited Findings
- India: the RBI digital-lending-app directory has been live since 1 Jul 2025. It is based on lender self-reporting "as is", without validation by RBI. Google Play required personal-loan apps to be on the list by 28 Jan 2026. A third party (GoCredit, a lender, so treat with caution) reports it fell from 1,034 to 695 unique apps between 7 and 14 Sep 2026, mostly de-duplication. — [Medianama](https://www.medianama.com/2025/05/223-rbi-digital-lending-apps-centralised-directory/); [Google Play policy](https://support.google.com/googleplay/android-developer/answer/16604194); [GoCredit](https://gocredit.money/news/rbi-loan-app-directory-shrinks-by-a-third-20260916)
- India: MeitY had blocked 87 illegal lending apps under IT Act s.69A (Lok Sabha, Dec 2025). The Centre blocked 3,718 fraudulent mobile apps of all types by 30 Jun 2026. An earlier RBI working group found 600 of 1,100 lending apps on 81 app stores were illegal (date unconfirmed). — [Medianama, Dec 2025](https://www.medianama.com/2025/12/223-meity-87-illegal-lending-apps-it-act/); [BankInfoSecurity](https://www.bankinfosecurity.net/more-than-half-indian-loan-apps-illegal-rbi-panel-finds-a-17970)
- India: a May 2026 report names police cases after a student's death in Kerala linked to a loan app (InstaPay). Telangana calls instant-loan-app fraud one of its fastest-growing cybercrimes. Raids hit call centres in Gurugram and Hyderabad taking instructions from Indonesia. — [The Week, May 2026](https://www.theweek.in/news/biz-tech/2026/05/12/digital-loan-app-scams-crackdown.html); [The Quint](https://www.thequint.com/news/india/multicity-crackdown-raids-on-illegal-instant-loan-apps)
- RBI's Trend and Progress report 2024-25 said it would review recovery-agent instructions and issue harmonised norms, and issue norms on mis-selling. — [Deccan Chronicle](https://deccanchronicle.com/business/rbi-to-issue-norms-to-curb-mis-selling-of-financial-products-1927059)
- RBI ombudsman 2024-25: about 2.96 lakh complaints (+0.8%), loans and advances 29.25%, credit cards 17.15%, 91.22% filed digitally, disposal rate fell from 95.10% to 93.07% (third-party analysis of the RBI report, dated Dec 2025). No category cut for digital lending or recovery agents was found. — [Outlook Money](https://www.outlookmoney.com/banking/how-to-file-a-complaint-with-rbi-ombudsman-when-your-bank-isnt-listening); [RBI report page](https://website.rbi.org.in/web/rbi/-/publications/annual-report-of-ombudsman-scheme-2024-25)
- Lookout found nearly 300 Android and iOS apps that took excessive data and used it to shame borrowers. ESET listed SpyLoan apps active in 13 countries including India, Mexico, Indonesia, Kenya and Nigeria (publication dates not given). — [Help Net Security](https://www.helpnetsecurity.com/?p=249733)
- Kenya: the CBK licensed 32 more digital credit providers in April 2026, bringing the total to 227. Under the 2022 regulations lenders must give 30 days' notice before CRB listing and cannot report defaults of Ksh1,000 or less. In 2020 more than 3.2M Kenyans had been negatively listed, many for small mobile loans. Tala and Branch were cited at 152.4% and 132% annualised rates (old data). — [Kenyans.co.ke](https://www.kenyans.co.ke/news/122590-cbk-approves-32-new-digital-lenders-bringing-total-to-227); [Business Daily](https://www.businessdailyafrica.com/economy/Pain-of-Kenyans-blacklisted-foramounts-as-small-as-Sh100/3946234-3374120-r0r2bfz/index.html); [TechCrunch 2022](https://techcrunch.com/2022/11/18/google-clamps-down-on-illegal-loan-apps-in-kenya-nigeria)
- Nigeria: the FCCPC's 2025 digital-lending regulations are restrained by a Federal High Court order (FCCPC statement, June 2026). The approval count is disputed (505 reported, and the FCCPC denied a further 48). 112 apps are on a watchlist and 54 were deleted from Google Play. — [Nairametrics, 28 Jun 2026](https://nairametrics.com/2026/06/28/fccpc-denies-approving-48-loan-apps-rejects-505-lenders-claim/); [IT Edge News](https://www.itedgenews.africa/nigeria-cleans-up-digital-lending-space-as-fccpc-cbn-approve-over-430-loan-apps-in-2026/)
- Indonesia: licensed P2P outstanding was Rp 105.14 trillion in Jun 2026 (+25.88% YoY), with a TWP90 of 4.26% against a 5% limit. 94 licensed lenders (Jul 2026). Satgas PASTI had stopped 951 illegal pinjol in 2026 (the figure was identical across monthly reports, so possibly stale). 12,824 illegal pinjol have been blocked since 2017. 19,169 illegal-pinjol complaints in Jan-Jun 2026. — [Kontan, Jun 2026](https://keuangan.kontan.co.id/news/pembiayaan-fintech-lending-naik-2588-jadi-rp-10514-triliun-hingga-juni-2026); [Infobanknews](https://infobanknews.com/satgas-pasti-tutup-1-220-entitas-keuangan-ilegal-hingga-juli-2026)

### Inferences
- Lists and takedowns are supply-side fixes with whack-a-mole dynamics. Nobody sits on the borrower's phone at the moment of decision or harassment, which is the opening for on-device AI.
- Product concept ("Loan Bodyguard"): (1) a pre-install and pre-borrow checker that cross-references an app or lender against the RBI/CBK/FCCPC/OJK registries, flagging permissions such as contacts and SMS; (2) a harassment-evidence assistant that records and transcribes recovery calls, tags RBI/FDCPA-equivalent violations, and drafts complaints for the RBI CMS/ombudsman, cybercrime.gov.in, or the CBK; (3) a safe-repayment and renegotiation helper. Revenue: B2C freemium, or white-labelled to regulated lenders and CSOs.
- Feasibility: high for (1) and (2) with a small team (LLM plus registry scrapes plus voice-to-text). Risk: call recording consent laws, Play Store permission policy, and legal liability if registry data is wrong. Regulatory path: it is consumer-side so it avoids lender licensing, but a "complaint filing" function should be framed as drafting, not legal advice. Partner with consumer NGOs and cyber-cell channels.

### Gaps
- No 2026 count of Kenyan CRB blacklisting or Nigerian default rates.
- No sourced recovery-agent harassment complaint counts for India (RBI ombudsman data not split).
- No Philippines, Vietnam or Pakistan data in this pass.
- RBI's final recovery-agent norms status not confirmed.

## Problem 3: Revolving credit-card debt spirals and the US consumer debt picture

### Takeaway
US household debt is $18.77T and credit card balances are $1.263T, with card and auto new-delinquency flows still elevated. APRs of about 21 to 22% are stable, the proposed 10% cap has not become law, and most borrowers carry balances because they cannot cheaply switch or pay down, not because of ignorance alone.

### Cited Findings
- NY Fed Q2 2026 (report dated 11 Aug 2026): total household debt $18.771T (-$13B QoQ, +$383B YoY). Credit card $1.263T (+$21B QoQ, +$54B YoY). Auto $1.713T. Student $1.651T. HELOC $459B. 4.7% of debt in some stage of delinquency. Flow into serious delinquency (90+ days), Q2 2025 to Q2 2026: credit card 6.93% to 6.97%, auto 2.93% to 3.00%, mortgage 1.29% to 1.52%, student 12.88% to 7.83% (distorted by re-reporting of defaulted loans). — [NY Fed press release](https://www.newyorkfed.org/newsevents/news/research/2026/20260811)
- Credit card APR: 22.15% on accounts assessed interest in Q2 2026 (21.52% in Q1) per one source on G.19, versus 20.9% on the commercial bank survey. Sources disagree because they measure different bases. — [Zenodo summary](https://zenodo.org/record/20568336); [FRED TERMCBCCALLNS](https://fred.stlouisfed.org/graph/?g=1b5DI)
- A January 2026 White House call for a one-year 10% cap has no enforcement mechanism and needs Congress. Sanders-Hawley S.381 is in committee, with no cap enacted as of the sources found. — [Fox Business](https://www.foxbusiness.com/politics/trump-calls-one-year-10-cap-credit-card-interest-rates); [Outlook Business](https://www.outlookbusiness.com/economy-and-policy/trump-proposes-10-credit-card-rate-cap-offers-no-enforcement-plan)
- Federal Reserve SHED (2025 survey, published May 2026, via secondary sources): about 63% of adults could cover a $400 emergency with cash, about 12% could not cover it by any means. — [Financer summary](https://financer.com/personal-finance/emergency-fund-statistics/); [Federal Reserve SHED page](https://www.federalreserve.gov/consumerscommunities/shed.htm)
- Balance transfers: a 2018 CompareCards survey found 2 in 5 balance-transfer users did not clear the balance before the promo ended. UK Barclaycard: 34% had not cleared. More than 60% paid a fee of 3% or more. — [Benzinga](https://benzinga.com/z/12982700); [Electronic Payments International](https://www.electronicpaymentsinternational.com/news/one-in-three-credit-card-customers-not-clearing-debts-consumer-intelligence-4161671)
- Brazil: 80.4% of families were indebted in March 2026 (CNC PEIC, highest since 2010). Serasa counted 82.8M delinquent people in March 2026 (49% of adults), rising to 83.3M in April. Revolving card interest averaged 442.4% a year in June 2026, despite the Law 14.690/2023 cap that limits total charges to 100% of the original debt. Desenrola 2.0 launched in May 2026 with discounts of up to 90% on Serasa's platform. — [DGABC](https://www.dgabc.com.br/Noticia/4317691/inadimplencia-bate-82-8-milhoes-de-brasileiros-em-marco-segundo-serasa); [Times Brasil](https://timesbrasil.com.br/brasil/juros-cartao-rotativo-4424-junho/)
- UK: Citizens Advice (2023, dated) estimated household arrears of about GBP 22bn and 27% behind on at least one bill. Energy-bill debt was about GBP 6bn in June 2026 with forecasts of GBP 7bn. — [Citizens Advice](https://www.citizensadvice.org.uk/about-us/media-centre/press-releases/one-in-four-people-behind-on-at-least-one-bill-as-uk-households-fall-22-billion-in-the-red/); [IBTimes UK](https://www.ibtimes.co.uk/uk-energy-debt-crisis-unpaid-bills-price-cap-rise-1815973)

### Inferences
- Issuers earn most of their revenue from revolvers, so none has an incentive to push a customer to cheaper credit. Aggregators and personal-finance apps are paid by lead-gen, which biases them toward products rather than payoff plans.
- Product concept ("payoff copilot with agentic execution"): with consented bank and card data, an agent builds a month-by-month payoff plan, finds the cheapest consolidation or balance-transfer route after fees, schedules payments, and negotiates hardship terms by phone or chat on the user's behalf (voice AI). Revenue is subscription or a share of interest saved, not lender commissions, to keep incentives aligned.
- Feasibility: the planning layer is easy. Execution (card-issuer API access for payments, outbound voice negotiation) is hard in the US and India because of data access and call-consent rules. Regulatory path: in the US, avoid holding funds (use issuer pay-by-bank), watch debt-adjusting and debt-settlement state licensing, and treat the voice agent under the TCPA (FCC treated AI voices as "artificial voice" in Feb 2024). Full legal analysis was not found in this pass.

### Gaps
- No sourced figure for the share of US cardholders who revolve, or revolver APR distribution.
- India credit-card revolving-debt data (RBI) not collected.
- EU and UK card-debt data not collected beyond the energy-debt items above.

## Problem 4: BNPL stacking and "phantom debt"

### Takeaway
BNPL debt has been largely invisible to lenders. FICO has now built BNPL-inclusive scores (FICO 10 BNPL and 10 T BNPL) but adoption is voluntary and uneven. The UK brought BNPL under FCA regulation on 15 July 2026, while US federal standardised reporting and dispute rights are still absent.

### Cited Findings
- FICO's BNPL-inclusive scores target "phantom debt". Not every BNPL provider reports, and lenders can opt out. — [HousingWire](https://www.housingwire.com/articles/fico-to-add-buy-now-pay-later-data-to-credit-scores/); [PaymentsJournal](https://www.paymentsjournal.com/credit-bureaus-still-cant-figure-out-bnpl/)
- A CFPB 2025 report reportedly found that over 62% of BNPL users have more than one loan at a time (secondary source, not verified against the CFPB document). LendingTree's 2026 report says 47% of BNPL users paid late at least once in the past year (up from 41%). SuperMoney notes that Afterpay still does not report and that no federal law requires standardised BNPL dispute rights. — [SuperMoney](https://www.supermoney.com/buy-now-pay-later-bnpl-regulations-and-consumer-rights); [Digital Transactions](https://www.digitaltransactions.net/bnpl-offers-big-potential-for-market-share-but-also-flashes-caution-signs-for-the-unwary-a-panel-says/)
- UK: the FCA regime took effect 15 Jul 2026. Firms need authorisation, with proportionate affordability checks, Consumer Duty coverage, signposting to free debt advice, access to the Financial Ombudsman for agreements after 15 Jul 2026, and s.75-style protection for GBP 100 to 30,000 purchases. Some protections were softened after provider lobbying. StepChange's July 2026 YouGov poll: 4% of UK adults (about 2.2M) used BNPL for essentials in the last three months. — [FSTech](https://fstech.co.uk/fst/BNPL_Lenders_Face_FCA_Oversight_From_July_2026.php); [StepChange](https://www.stepchange.org/media-centre/press-releases/BNPL-a-landmark-win.aspx); [Money to the Masses](https://moneytothemasses.com/news/new-buy-now-pay-later-rules-confirmed-to-take-effect-in-july/amp)

### Inferences
- The stacking problem is a data-fragmentation problem. Each BNPL lender sees only its own loan, and bureaus see partial data. A consumer-side aggregator that sees bank outflows across BNPL providers has data the lenders lack.
- Product concept: a "total obligations radar" that uses open-banking/AA transaction data to detect every BNPL, EMI and subscription installment, forecast the next 60 days of cash collisions, and warn before an overdraft or missed payment. It can also generate a lender-readable obligations statement so responsible users are not scored purely by what the bureau sees.
- Feasibility: high where bank data is accessible (UK open banking, India AA). Low-medium in the US because of 1033 uncertainty. The value of the product depends on BNPL usage being observable in bank data, which should be true for the debit-card-funded majority.

### Gaps
- No primary verification of the CFPB 62% figure.
- No sourced BNPL market size or default rate for India, SEA, Africa or LatAm.
- No data on lender uptake of FICO BNPL scores.

## Problem 5: Debt resolution, settlement scams, collections abuse and medical debt

### Takeaway
People in distress face a market where the paid options (debt settlement companies) are often predatory and the free options (nonprofit counselling) are capacity-constrained. In the US, the federal medical-debt reporting rule was vacated in July 2025 and the CFPB is pushing to preempt state bans. AI voice agents are being adopted by collectors faster than by consumers.

### Cited Findings
- KFF (Feb 2024, data from end of 2021): at least $220B of US medical debt. About 14M people (6% of adults) owe over $1,000 and about 3M (1%) over $10,000. Survey-based measures are much higher (KFF survey: about 41% of adults with some medical or dental debt; Commonwealth Fund: 72M working-age adults with bill problems or debt; CFPB: about 15M people with medical collections on credit reports). — [KFF](https://www.kff.org/health-costs/the-burden-of-medical-debt-in-the-united-states/); [Stacker 2026 roundup](https://stacker.com/stories/personal-finance/what-percentage-americans-have-medical-debt-2026)
- CFPB's medical-debt credit-reporting rule was vacated by the E.D. Texas on 11 Jul 2025. 15 states have their own bans, and NCLC says the vacatur does not affect them. The CFPB has since pursued an interpretation that federal law preempts state bans (status as of Oct 2026 not confirmed). The bureaus' voluntary 2022-23 policies remain: no paid medical debt, nothing under $500, a one-year wait. — [BHFS](https://www.bhfs.com/insight/federal-court-vacates-cfpbs-medical-debt-rule-finds-fcra-preempts-state-laws/); [NCLC](https://library.nclc.org/article/latest-keeping-medical-debt-out-credit-reports); [BadCredit.org](https://www.badcredit.org/news/cfpb-federal-law-trumps-state-medical-debt-bans/)
- Debt-relief enforcement: an FTC action in July 2025 against a scheme that targeted seniors and veterans, an FTC and Nevada AG suit in Oct 2025 against tax-debt-relief operators, and a CFPB case with $43M+ in restitution. Credit-union and bank trade groups wrote in Feb 2026 that debt-settlement is growing and that some firms steer customers into default (advocacy source). An older FTC case found that fewer than 2% of customers completed programs. — [FTC](https://www.ftc.gov/node/296338); [America's Credit Unions letter, Feb 2026](https://www.americascreditunions.org/sites/default/files/file/2026-03/Debt%20Settlement%20Jt%20Trades%20%20Letter%202.27.26.pdf)
- Collections rules: Reg F presumes compliance at 7 or fewer calls in 7 days, no calls before 8am or after 9pm. The FCC ruled in Feb 2024 that AI voices count as "artificial voice" under the TCPA. CFPB debt-collection complaints reportedly rose from about 109,900 (2023) to about 207,800 (2024) (a vendor's citation of the CFPB report). — [Retell AI](https://www.retellai.com/blog/fdcpa-compliance-automated-calls); [Sutherland, State of Collections 2026](https://www.sutherlandglobal.com/wp-content/uploads/sites/2/The-State-of-Collections-2026.pdf)
- CFPB 2025 Consumer Response annual report (31 Mar 2026): 6.6M complaints (2x 2024), about 5.8M (88%) about credit or consumer reporting. The CFPB attributed part of the surge to credit-repair organisations and to LLMs and AI agents generating "duplicative and spurious" submissions. — [Orrick, Apr 2026](https://infobytes.orrick.com/2026-04-10/cfpb-reports-complaint-volume-doubled-in-2025-citing-surge-in-credit-reporting-disputes/); [Accounts Recovery](https://www.accountsrecovery.net/2026/04/03/cfpb-complaint-volume-doubles-again-credit-reporting-still-in-spotlight/)

### Inferences
- Unit economics are the structural problem: nonprofit counselling does not scale, and paid settlement makes money from fees and delays, which conflicts with the client's interest. AI cuts the cost of a counsellor-quality plan to near zero, but the paid-for negotiation step (creditor contact) is where value is realised.
- Product concept ("free-first debt triage plus rights engine"): intake by voice or chat, in any local language, that inventories debts, classifies them (time-barred, medical, disputed, secured), picks the legal rights that apply (validation letter, hospital charity-care and itemised-bill requests, state medical-debt protections), generates the letters, and escalates to nonprofit or legal-aid partners. Revenue from nonprofit/health-plan/employer/credit-union sponsorship (B2B2C), never from settlement fees.
- Medical-debt wedge: an AI that audits hospital bills for errors and checks charity-care eligibility is a distinct, high-value niche, but I found no sourced savings rates for it in this pass.
- Regulatory path: generating dispute and validation letters for the user is generally lower-risk, while negotiating on behalf of the user may need debt-adjuster licensing in many US states. Credit-repair-law (CROA) fee rules apply if the product charges for credit disputes. This is my reading, not a sourced legal opinion.
- Feasibility for a small team: high on the letter/rights layer, medium on voice negotiation, low on direct creditor integrations.

### Gaps
- No sourced figure on the size of the US debt-settlement industry or consumer harm.
- UK/EU debt-advice capacity (StepChange, MaPS) not found beyond the BNPL poll.
- India and Africa debt-counselling supply not researched. No sourced data on India's credit-counselling services (RBI-backed).

## Problem 6: Credit-report errors and disputes

### Takeaway
The only large FTC accuracy study is from 2013 (1 in 5 consumers with a confirmed error, about 5% with an error big enough to change terms). Dispute volume has exploded and is now being polluted by credit-repair mills and AI-generated filings, which makes real errors harder to resolve. India now has a hard SLA (30 days, Rs 100 per day compensation) that is enforced.

### Cited Findings
- FTC (Feb 2013): 1 in 5 of 1,001 consumers had at least one error on a report. About 5% had errors that could lead to paying more for credit. 20% of consumers who disputed had a correction made. This is more than a decade old. — [FTC / Auto Remarketing](https://www.autoremarketing.com/?p=43411); [FTC](https://www.ftc.gov/node/46243)
- CFPB 2025 complaints: 6.6M total (2x 2024), 88% credit reporting. The CFPB cautions that part of the surge reflects credit-repair firms and AI-generated duplicates. — [Orrick](https://infobytes.orrick.com/2026-04-10/cfpb-reports-complaint-volume-doubled-in-2025-citing-surge-in-credit-reporting-disputes/)
- India: compensation framework effective 26 Apr 2024. Rs 100 per day if a dispute exceeds 30 days (21 days for the lender, 9 for the bureau). Unresolved bureau complaints can go to the RBI ombudsman (since 1 Sep 2022 under RB-IOS 2021). One report says RBI penalised TransUnion CIBIL, CRIF High Mark and Equifax in orders dated 31 Aug 2026 for not paying owed compensation (not confirmed on the RBI site). — [CIBIL compensation framework](https://www.cibil.com/framework-for-compensation); [Moneylife](https://moneylife.in/article/now-file-unresolved-credit-score-complaints-with-rbi-ombudsman/67997.html); [IndianPayCalculator](https://www.indianpaycalculator.in/govt-news/rbi-fines-credit-bureaus-cibil-equifax-100-per-day-rule-2026)
- India disputes route through the lender: CIBIL forwards to the data furnisher, which verifies and sends the correction back. — [BankBazaar](https://gaadi.bankbazaar.com/cibil/cibil-dispute.html)

### Inferences
- The root cause is that the data furnisher (bank, NBFC, collector) has no incentive to fix records, and bureaus are paid by lenders. In the US, FCRA investigations are typically automated e-OSCAR codes, so rewriting a dispute more convincingly is the lever AI actually has.
- Product concept ("dispute agent"): pull all bureau reports, cross-check each tradeline against the user's bank data and statements (the AA/open-banking rail gives ground truth that the bureau lacks), auto-draft furnisher-specific disputes with evidence, track statutory clocks (30 days FCRA, 30 days India), and claim compensation or escalate to the ombudsman or CFPB. In India the Rs 100/day clock is a ready-made monetisable wedge.
- Risk: the CFPB's AI-spam concern means high-volume, templated disputes can be classed as "frivolous" under FCRA s.611, and credit-repair rules apply. Design for evidence-backed, per-user disputes and keep the human in the loop. Feasibility: high for a small team in India, medium in the US (CROA constraints).

### Gaps
- No post-2013 accuracy study. The 2013 FTC figure is the only systematic one found.
- No India CIBIL dispute volumes or share of complaints about bureaus.
- No UK/EU credit reference agency error data.

## Problem 7: Loan comparison opacity, APR hiding and refinancing inertia

### Takeaway
People systematically fail to refinance even when it is clearly in their interest, and the evidence is robust for mortgages (inattention plus inertia), while personal-loan and card-switching evidence is thinner. Falling-rate environments therefore do not pass through to consumers without an automated switch.

### Cited Findings
- Chicago Booth (Pope, Keys and Pope): about 20% of US households that would benefit from refinancing and appeared able to did not, losing an average of $11,500 each (December 2010 sample). A related summary quotes a median loss of $45,000 over the life of the loan (different method). In one experiment 84% of homeowners who got a pre-approved, no-upfront-cost offer did not respond. — [Chicago Booth Review](https://www.chicagobooth.edu/review/us-homeowners-leave-money-on-the-table); [BYU News](https://news.byu.edu/news/americans-missed-out-54-billion-not-refinancing-study-says)
- Danish mortgage study separates inattention (not responding to incentives) from inertia (psychological cost). Inattention is highest among older, lower-income, lower-education households. The authors suggest automatic refinancing. — [Campbell / Harvard PDF](https://campbell.scholars.harvard.edu/resource/pdf-updated-june-2015-4); [CBS research](https://research.cbs.dk/en/publications/inattention-and-inertia-in-household-finance-evidence-from-the-da/)
- Some non-refinancers are blocked rather than inert: many are delinquent or cannot qualify for a lower rate (CoreLogic analysis cited by NMN). — [National Mortgage News](https://www.nationalmortgagenews.com/articles/failure-to-refi-proves-costly)
- Australia (lender research): about 7% of mortgages refinanced in a year, 22% of mortgage holders said refinancing was too hard. — [Broker News](https://brokernews.com.au/news/breaking-news/only-7-of-people-have-refinanced-says-aussie-home-loans-research-279066.aspx); [MPA](https://www.mpamag.com/au/mortgage-industry/industry-trends/why-customers-arent-refinancing-despite-record-low-interest-rates/308388)
- Balance-transfer evidence (see Problem 3): 33 to 40% fail to clear in the promo window, and a missed payment can reset the 0% rate to a penalty APR as high as 29.99%. — [NerdWallet](https://www.nerdwallet.com/blog/credit-cards/bad-news-balance-transfer-customers-33-repay-balances-interestfree-period)
- Only the mortgage case is evidenced in this pass. The research I found on personal-loan refinancing concerned high-cost lenders (OppFi) whose model builds in repeated refinancing, which is lender-driven churn rather than consumer inertia. — [CRL on OppFi](https://www.responsiblelending.org/research-publication/lost-opportunities-how-oppfi-traps-borrowers-unaffordable-debt)

### Inferences
- Product concept ("refi watchdog"): monitors the user's loans (from bank data or statements), recomputes true APR including fees, and alerts only when a switch saves more than a threshold net of costs, then pre-fills and submits the application. The economic engine is a referral fee from the new lender or a share of savings. This is crowded where comparison sites exist, so the differentiators are continuous monitoring and agentic execution.
- Why it remains unsolved: the incumbent lender profits from inertia; comparison sites are paid per lead and often show teaser rates; the consumer has to do all the paperwork again. LLM document extraction and AA/open-banking data cut that friction.
- Feasibility: medium. Regulatory path: licensed broker or marketplace status is usually required for loan-origination referral, while a pure information/alert service may not be. Need market-specific checks; India has no clear "broker" licence for retail loans beyond DSA arrangements under RBI outsourcing norms (my understanding, not sourced).

### Gaps
- No India or SEA refinancing-inertia data.
- No recent US/UK study quantifying savings missed on personal loans or credit cards.
- APR disclosure rules (India KFS, UK, EU CCD2) were not researched here.

## Problem 8: Student loans (US repayment chaos 2025 to 2026; India education loans)

### Takeaway
The US federal student loan system is mid-transition: SAVE ended, the new Repayment Assistance Plan (RAP) launched on 1 Jul 2026, involuntary collections restarted in 2025 then wage garnishment was paused in January 2026, and large numbers of borrowers are in default or deep delinquency. This is a compliance and navigation problem that AI can address. India's education-loan stock is growing about 15% a year, but I found little borrower-level data.

### Cited Findings
- SAVE was struck down by the courts in March 2026 and ended by the OBBBA on 1 July 2026, covering about 7.5M enrolled borrowers (InvestigateTV via the search summary). RAP and the Tiered Standard Plan became available 1 Jul 2026. RAP payments reportedly run 1 to 10% of AGI with a $10 minimum, a 30-year term, and a $50 per-dependent discount. SAVE borrowers had about 90 days after notice to choose a plan, or default to standard. Sources disagree on whether the cutoff is end of September or October. — [NPR, Dec 2025](https://www.npr.org/2025/12/23/nx-s1-5630504/2026-federal-loans-student-changes-save-plan); [NerdWallet](https://www.nerdwallet.com/student-loans/news/save-plan-switch-ultimatum); [NYC DCA](https://www.nyc.gov/site/dca/talk-money/Student-Loans-Key-Changes.page)
- AEI (Dec 2025): 5.5M borrowers in default, 3.7M more than 270 days late, and 2.7M in early delinquency. Treasury Offset restarted May 2025. The Education Department delayed wage garnishment in January 2026 (up to 15% of disposable pay when active). I could not confirm whether the pause has ended. — [My-CPE summary](https://my-cpe.com/insights/news-and-insights/markets-and-finance/the-student-loan-system-just-took-a-hard-turn); [CBS NY](https://www.cbsnews.com/newyork/news/student-loan-borrowers-default-wages-garnished-2026)
- NY Fed Q2 2026: student loan balance $1.651T, serious-delinquency flow 7.83% (from 12.88%), but distorted by re-reporting of defaulted debt. — [NY Fed](https://www.newyorkfed.org/newsevents/news/research/2026/20260811)
- India: one aggregator reports outstanding education loans rose 15% to a decade-high Rs 8.58 lakh crore in FY26 (low-quality source, verify against RBI). Gross NPA on education loans at public sector banks fell from 7% (FY21) to about 2% (FY25) per the Ministry of Finance citing RBI. The collateral-free limit under the Model Education Loan Scheme is Rs 7.5 lakh. — [Business Standard, Dec 2025](https://www.business-standard.com/markets/capital-market-news/gross-npas-in-outstanding-education-loans-of-psbs-see-sharp-fall-in-recent-years-125121600267_1.html); [BVWD aggregator](https://bvwd.ca.gov/expert-time/Indias-Education-Loans-Surge-15-to-DecadeHigh-858-Lakh-Crore-in-FY26-24-6342)

### Inferences
- Complexity and frequent rule changes create high demand for a navigator. The product concept is "student-loan co-pilot": ingests the servicer data (via StudentAid.gov export or a screenshot or PDF), models RAP versus Tiered Standard versus consolidation versus rehabilitation, handles recertification deadlines, drafts rehabilitation and hardship paperwork, and tracks forgiveness clocks. Revenue is a flat consumer fee or employer benefit (employers can contribute under existing law, to my knowledge, not sourced here).
- Feasibility: high for a small team, because the data is borrower-owned and structured. Regulatory path: the US has a history of student-loan "debt relief" scams, and state student-loan-servicer or debt-adjuster licensing may apply to anyone who submits forms for fees, so partner with a licensed entity or limit to self-service. India: a lender-comparison/advisory tool for abroad-study loans is plausible, but I have no borrower-level evidence of a gap.

### Gaps
- Whether wage garnishment resumed after the January 2026 pause is not confirmed.
- No RAP enrollment numbers or servicer backlog data from the Department of Education.
- No India borrower-level data (default rates for abroad-study loans, private lender share).

## Problem 9: Rent reporting and credit-building

### Takeaway
Rent is most renters' largest monthly payment but still rarely reaches credit files. The new scoring models count it, but the 2026 GSE rollout is limited and optional, and reporting depends on landlords or self-reporting platforms.

### Cited Findings
- TransUnion 2025: 13% of renters have rent reported to credit bureaus (11% in 2024). Landlord-reported share fell to 44% from 48%, partly as free pilot programmes ended. A 2022 CFPB estimate was just 1.7 to 2.3% of adults in rental housing. — [BadCredit.org](https://www.badcredit.org/news/more-consumers-are-self-reporting-rent-payments-to-credit-bureaus/); [Esusu](https://esusurent.com/blog/your-largest-monthly-expense-just-became-your-secret-weapon-state-of-rent-reporting-in-2026)
- FICO 10T and VantageScore 4.0 can use rent and utility data but Classic FICO does not. VantageScore says people without tradelines saw average increases of as much as 67 points, and that nearly 4M renters could qualify for a mortgage from rent history alone (vendor claims). — [BadCredit.org on VantageScore](https://www.badcredit.org/news/vantagescore-says-rent-data-unlocks-777b-mortgage-opportunity/)
- GSE status: 22 Apr 2026 Fannie Mae update allows VantageScore 4.0 only for a limited set of approved lenders, with tri-merge still required. FHA will allow VantageScore 4.0 and FICO 10T "in the coming months". — [CRS, Jul 2026](https://www.everycrsreport.com/files/2026-07-17_IF12588_ccb11200c04e4418208ea3df6c6e9a0ca6e3c8cd.html); [Fannie Mae](https://fanniemae.com/newsroom/fannie-mae-news/credit-score-updates-advance-modernization)

### Inferences
- Rent reporting alone is a feature, not a company (many players, thin margins). The durable value is as an input into a broader cash-flow credit passport (Problem 1). Verifying rent payments from bank data (no landlord cooperation) is where AI/open-banking helps. A rent-only product also depends on whether the lender's chosen score model reads it.

### Gaps
- No UK, EU, India or Africa rent reporting data (India rental credit reporting essentially not researched).
- No evidence on real default-prediction lift from rent data beyond vendor studies.

## Problem 10 (added): Regulatory and data-rail enablers, and what changed recently

### Takeaway
Data rails and rules are moving in opposite directions across regions. India (AA, RBI Digital Lending Directions 2025, bureau compensation SLAs) and the UK (BNPL regulation) are tightening and standardising. The US is in flux on open banking (1033), the CFPB, medical debt and credit-score models. LLM agents are simultaneously a tool for consumers and a cause of regulator-visible spam.

### Cited Findings
- India AA: see Problem 1 figures (500M+ fulfilled consents, 3.68 crore AA loans in FY26). Sahamati says about 1 in 10 personal loans flows through AA. — [Sahamati](https://sahamati.org.in/wp-content/uploads/2026/01/Credit-Reimagined-H1-FY26-Abridged-1.pdf)
- RBI Digital Lending Directions 2025 and DLA directory: see Problem 2. — [RBI press release](https://website.rbi.org.in/web/rbi/-/press-releases/rbi-issues-reserve-bank-of-india-digital-lending-directions-2025)
- US 1033: replacement proposal at OIRA (Aug 2026), JPMorgan charging aggregators. — [Consumer Finance Monitor](https://www.consumerfinancemonitor.com/2026/08/06/cfpb-sends-new-section-1033-open-banking-proposal-to-oira-for-review/)
- UK BNPL regulation live from 15 Jul 2026. — [FSTech](https://fstech.co.uk/fst/BNPL_Lenders_Face_FCA_Oversight_From_July_2026.php)
- CFPB flagged LLM and AI-agent generated complaint spam in its 2025 annual report. — [Orrick](https://infobytes.orrick.com/2026-04-10/cfpb-reports-complaint-volume-doubled-in-2025-citing-surge-in-credit-reporting-disputes/)
- Findex 2025: formal credit reaches about a quarter of adults in low- and middle-income economies. — [Nairametrics](https://nairametrics.com/2025/07/18/world-bank-59-of-adults-in-nigeria-and-others-borrowed-in-2024/)

### Inferences
- Ranking of problems by (pain x data access x regulatory clarity x small-team feasibility), for an India-first MVP: (1) bureau-dispute plus compensation agent and AA-based cash-flow passport, (2) loan-app safety and harassment evidence, (3) total-obligations radar (BNPL/EMI collisions) from AA data, (4) refi watchdog. US-first: student-loan navigator and medical-bill audit have the clearest acute demand but the heaviest licensing questions.
- A common architecture across these: consented data connector (AA or Plaid), a deterministic rules engine for law and regulation, an LLM for extraction, explanation and drafting, and a voice layer for local languages. The main non-technical risks are licensing of any money movement or negotiation, privacy law (DPDP in India, FCRA/GLBA in the US) and liability for wrong advice.

### Gaps
- DPDP Act 2023 rules and consent-manager interplay with AA were not researched.
- EU (PSD3/FiDA, CCD2) not researched.
- LatAm open finance (Brazil, Mexico) and Africa (Kenya, Nigeria open banking) not researched beyond lending-app regulation and Brazil's debt data.
- Philippines, Vietnam, Pakistan, and Mexico debt-app issues not covered.
