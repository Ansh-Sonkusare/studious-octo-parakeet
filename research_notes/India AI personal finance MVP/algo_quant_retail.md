# Retail Algo/Quant Trading in India as a Foundation for an AI Product (as of Oct 2026)

Context: This tests a friend's claim: "Quant and algo stays even after the AI boom; build products on top only if you have 5–7 algos that have shown results; train your own model on them and use it for trading." Research date: 7 Oct 2026. Primary SEBI/NSE PDFs could not be fetched directly (403s or empty pages), so many regulatory details come from broker and vendor summaries. These are flagged where relevant.

## 1. SEBI's retail algo trading framework (Feb 2025 circular to April 2026 go-live)

### Takeaway
Retail algo trading is now legal and formally regulated. The framework has been mandatory for all brokers since 1 April 2026. Every algo order goes through a broker, carries an exchange algo-ID, and any third-party algo vendor must be empanelled with the exchanges. Vendors selling black-box strategies (logic not shown to the user) must also register with SEBI as Research Analysts. This puts real compliance cost and liability on any startup that sells "our AI's trades".

### Cited Findings
- **The circular:** SEBI circular "Safer participation of retail investors in Algorithmic trading", No. SEBI/HO/MIRSD/MIRSD-PoD/P/CIR/2025/0000013, dated 4 Feb 2025 — [SEBI](https://www.sebi.gov.in/legal/circulars/feb-2025/safer-participation-of-retail-investors-in-algorithmic-trading_91614.html)
- **Timeline:**
  - The original start date of 1 Aug 2025 was extended to 1 Oct 2025.
  - A 30 Sep 2025 circular then set a glide path. Brokers had to file at least one retail algo product for registration by 31 Oct 2025, complete registration by 30 Nov 2025, and take part in a mock session by 3 Jan 2026.
  - Brokers that missed these milestones were barred from onboarding new retail API-algo clients from 5 Jan 2026.
  - Full applicability to all brokers began 1 Apr 2026.
  - Sources: [TaxGuru](https://taxguru.in/sebi/sebi-extends-algo-trading-implementation-timeline-april-2026.html); [Business Standard, 30 Sep 2025](https://www.business-standard.com/markets/news/sebi-extends-retail-algo-trading-framework-rollout-to-2026-125093000956_1.html); [Angel One](https://www.angelone.in/news/market-updates/sebi-extends-retail-algo-trading-rollout-sets-new-deadlines-for-brokers)
- **Empanelment:** NSE published the current empanelment application documents for algo providers in circular NSE/INVG/73992, dated 30 Apr 2026. Its "Empanelled Algo Providers" list was last updated 22 Sep 2026. I could not extract a provider count from it. — [NSE empanelled algo providers page](https://www.nseindia.com/static/trade/empanelled-algo-providers-exchange); [QuantInsti summary](https://www.quantinsti.com/articles/algorithmic-trading-india/)
- **Principal–agent structure:** Brokers act as principals and algo providers as their agents. Vendors cannot connect to exchanges directly and must be onboarded by a broker. — [Mutwo Labs broker compliance guide (vendor blog)](https://mutwolabs.com/blog/sebi-algo-trading-framework-2026-broker-guide); [Liquide blog](https://blog.liquide.life/sebi-algo-trading-regulations-2026/)
- **White-box vs black-box:**
  - White-box algos have transparent, replicable logic. Black-box algos have proprietary, opaque logic.
  - Black-box providers must register as SEBI Research Analysts (RA).
  - These points come from secondary and vendor summaries. I could not read the primary text.
  - Sources: [AlgoBulls blog](https://algobulls.com/blog/industry-insights-and-updates/sebi-new-algotrading-regulations-for-retail-investors-2026); [Mutwo Labs](https://mutwolabs.com/blog/sebi-algo-trading-framework-2026-broker-guide); [QuantInsti](https://www.quantinsti.com/articles/algorithmic-trading-india/)
- **DIY threshold and static IP:**
  - Individuals who code their own strategies can automate up to 10 orders per second (per segment per exchange) without exchange registration, using a static IP tied to their API key.
  - Above 10 OPS, the algo must be registered and gets a unique algo-ID. Unregistered algos are tagged with a generic ID.
  - Only one API key per user can run an unregistered algo under 10 OPS.
  - Static IPs are needed for order placement, not for data-only use. A backup static IP is needed. Family members may share an IP.
  - Source: [Zerodha Z-Connect overview of NSE circular, 6 May 2025](https://zerodha.com/z-connect/general/a-comprehensive-overview-of-nses-circular-on-the-new-retail-algo-trading-framework)
- **Vendor obligations:**
  - Vendors must register every strategy with the exchange, regardless of order frequency. Broker-offered strategies also need exchange approval.
  - Vendors use their own static IP, so their end users don't need one.
  - All algo access requires OAuth/2FA, and open APIs are banned.
  - Brokers are fully liable for orders placed through their systems, must run RMS checks, and exchanges can terminate rogue algos.
  - Sources: [Zerodha Z-Connect](https://zerodha.com/z-connect/general/a-comprehensive-overview-of-nses-circular-on-the-new-retail-algo-trading-framework); [Nithin Kamath Substack, 6 May 2025](https://nithinkamath.substack.com/p/nses-new-retail-algo-trading-circular)
- **Kamath's view:** Nithin Kamath (Zerodha CEO) said the clarity means "the regulatory risk in offering the product is greatly reduced." He expects brokers to offer pre-approved algos as more user-friendly automation. — [Kamath Substack](https://nithinkamath.substack.com/p/nses-new-retail-algo-trading-circular)
- **Zerodha API pricing:** Order and account APIs have been free since Mar 2025. The data API price was cut from ₹2,000 to ₹500 per month from 6 May 2025. — [Zerodha Z-Connect](https://zerodha.com/z-connect/general/a-comprehensive-overview-of-nses-circular-on-the-new-retail-algo-trading-framework)
- **Prior enforcement:** SEBI was already scrutinising brokers linked to algo platforms that promised guaranteed returns as of Oct 2024. — [Business Standard, Oct 2024](https://www.business-standard.com/amp/markets/news/sebi-scrutinises-brokers-linked-to-algo-trading-with-guaranteed-returns-124100901218_1.html)

### Inferences
- **The friend's plan triggers the heaviest compliance path.** "Train a model on our algos and use it for trading" offered to users is a black-box algo by definition. That means:
  - SEBI RA registration, which brings RA rules on qualifications, net worth or deposit, and fee caps.
  - Exchange empanelment.
  - Registering each strategy, and re-registering when its logic changes.
  - Integrating broker by broker.
  - An ML model that is retrained often may run into the logic-change and re-registration process. This is a practical problem for "continuously learning" AI. I could not verify the exact re-approval rules, so this is inferred.
- **Using it only for personal trading is easy.** If the team trades its own capital only, the DIY route (≤10 OPS, static IP) is simple. But that is a trading operation, not a product business.
- **The framework favours brokers and established vendors.** Brokers carry liability, so they will empanel few vendors. Distribution for a new startup depends on broker partnerships.

### Gaps
- I could not read the primary SEBI circular or the NSE operational-modalities text. The exact RA requirements specific to black-box algos and the empanelment criteria (net worth, fees, audit) are unverified.
- I found no published count of empanelled providers or registered retail algos, and no post-April-2026 reporting on adoption or vendor exits.
- I don't know whether a frequently retrained ML model counts as a "logic change" that needs re-approval.

## 2. SEBI F&O studies: retail losses, Oct 2024 curbs, and 2026 developments

### Takeaway
About 9 in 10 individual F&O traders lose money, consistently, every year. Individuals lost about ₹1.06 lakh crore net in FY25 and about ₹91,685 crore in FY26. SEBI's 2024 study also found that almost all institutional F&O profits come from algorithms. The Oct–Nov 2024 curbs and higher STT cut options contract volumes roughly in half in FY26. The retail F&O trader base, the core market for retail algo tools, is shrinking, and regulators keep tightening.

### Cited Findings
- **Jan 2023 study (FY22):** 89% of individual equity F&O traders lost money. — [Business Standard, Jan 2023](https://www.business-standard.com/amp/article/markets/sebi-study-suggests-89-retail-traders-in-equity-f-o-suffered-losses-123012501466_1.html)
- **Sep 2024 study (FY22–FY24):**
  - About 93% of more than 1 crore individual F&O traders lost money, averaging about ₹2 lakh per trader including costs. Aggregate losses were about ₹1.8 lakh crore.
  - Only 1% earned more than ₹1 lakh after costs.
  - The top 3.5% of loss-makers (about 4 lakh traders) lost about ₹28 lakh each on average.
  - More than 75% of loss-makers kept trading.
  - Individuals spent about ₹50,000 crore on transaction costs, 51% of it on brokerage.
  - Sources: [Moneylife](https://www.moneylife.in/article/93-percentage-of-individual-traders-lost-rs18-lakh-crore-in-equity-fo-in-past-3-years-sebi/75210.html); [Benzinga India](https://in.benzinga.com/24/09/40994647/sebi-study-unveils-93-of-individual-f-o-traders-suffered-losses-between-fy22-and-fy24)
- **Algorithms and institutional profits (same study):**
  - In FY24, prop traders made gross profits of about ₹33,000 crore and FPIs about ₹28,000 crore.
  - 96% of prop profits and 97% of FPI profits came from algorithmic trading.
  - Individuals lost more than ₹61,000 crore gross in FY24 (about ₹75,000 crore net).
  - Sources: [Moneylife](https://www.moneylife.in/article/93-percentage-of-individual-traders-lost-rs18-lakh-crore-in-equity-fo-in-past-3-years-sebi/75210.html); [Business Standard](https://www.business-standard.com/markets/capital-market-news/sebi-study-exposes-massive-losses-for-individual-f-o-traders-in-india-124092400948_1.html)
- **Jul 2025 study (FY25):**
  - 91% of individual traders lost money.
  - Net losses were ₹1,05,603 crore, up 41% from ₹74,812 crore in FY24. The average loss was about ₹1.1 lakh.
  - Unique traders fell 20% YoY. Quarterly participation fell from about 61.4 lakh (Q1 FY25) to about 42.7 lakh (Q4 FY25).
  - The study covered the top 13 brokers, about 96 lakh traders.
  - Sources: [Business Standard, 7 Jul 2025](https://www.business-standard.com/amp/markets/news/net-losses-of-traders-in-fo-widens-in-fy25-sebi-study-125070701221_1.html); [Business Upturn](https://businessupturn.com/finance/stock-market/sebi-study-retail-traders-lose-over-rs-1-lakh-crore-in-fy25-on-derivatives-bets/)
- **Oct 2024 curbs (SEBI circular of 1 Oct 2024):**
  - One weekly index expiry per exchange. NSE kept NIFTY, and BANKNIFTY, FINNIFTY and MIDCPNIFTY weeklies were dropped from 20 Nov 2024.
  - Minimum contract size raised from ₹5 lakh to ₹15 lakh.
  - Upfront collection of option premium.
  - Higher margins on expiry day.
  - Calendar-spread benefit removed on expiry day.
  - Intraday monitoring of position limits.
  - Sources: [Business Standard, 1 Oct 2024](https://www.business-standard.com/markets/news/sebi-announces-six-key-changes-to-curb-speculation-in-derivatives-trading-124100101316_1.html); [Sharekhan](https://www.sharekhan.com/financial-blog/blogs/sebi-fo-rules-impact-nse-to-discontinue-three-weekly-option-contracts)
- **FY26 outcome (Finance Ministry reply to Rajya Sabha, reported 11 Aug 2026):**
  - Unique individuals in equity F&O fell from 98.10 lakh to 78.60 lakh (about −20%).
  - Net losses of individuals fell from ₹1,11,788 crore to ₹91,685 crore.
  - Average loss per person rose from ₹1,13,913 to ₹1,16,654.
  - Equity derivatives turnover fell from ₹213 to ₹202 lakh crore.
  - STT collected on F&O was ₹27,695 crore, against ₹7,893 crore earlier.
  - The FY25 loss figure here (₹1.12 lakh crore) differs from the SEBI study's ₹1.06 lakh crore, probably because of a different scope or methodology.
  - Source: [Outlook Business / PTI, 11 Aug 2026](https://www.outlookbusiness.com/markets/sebi-measures-reduce-equity-fo-losses-for-retail-investors-in-fy26)
- **FY26 volumes:** SEBI's annual report showed options contracts traded down 51.5% in FY26 and futures contracts down about 18%. Premium and notional turnover reportedly still grew. — [Angel One news](https://www.angelone.in/news/market-updates/sebi-report-shows-over-50-drop-in-options-trading-volumes-in-fy26-after-f-o-reforms)
- **Pending proposal (2026):** An Aug 2026 report says regulators are considering removing weekly F&O expiries entirely. This is unconfirmed and not notified. — [Lapaas Voice (low-quality source)](https://lapaasvoice.com/sebi-may-remove-weekly-fo-expiry-to-curb-retail-investor-losses-reports)
- **Higher STT from 1 Apr 2026:** A report says higher STT on F&O took effect 1 Apr 2026 and is expected to push retail volumes down further. — [Multibagg market pulse (secondary)](https://www.multibagg.ai/market-pulse/articles/fo-curbs-retail-trading-india-cmuw634hx000l2yn44pdqyp2a)

### Inferences
- **The friend is half-right.** Algos "stay": institutional algos capture nearly all F&O profits. But the evidence says the winners are well-capitalised prop firms and FPIs with speed and scale advantages, and the losers are retail. A retail AI-algo product sells into the losing side of that trade.
- **The market is shrinking and the regulator is hostile.** The addressable base of active retail F&O traders shrank about 20% in FY26, options contract volumes halved, costs (STT) rose, and SEBI's direction is consistently restrictive. A product built mainly on retail options automation is exposed to further regulatory shocks, such as removal of weekly expiry.

### Gaps
- I could not access the SEBI FY25 study PDF directly. The FY26 loss-making percentage is unverified (a link headline says "nearly 90%").
- I found no official SEBI decision on removing weekly expiry as of Oct 2026.
- I found no data on what share of retail F&O orders are algo- or API-driven after April 2026.

## 3. Incumbent retail algo/quant platforms in India

### Takeaway
The space is crowded with cheap, mostly bootstrapped or lightly funded tools at about ₹300–1,500 per month. Brokers (Zerodha, Upstox, Dhan) increasingly control distribution and give APIs away. The quant-portfolio side (Wright Research, smallcase managers) runs as SEBI-registered RA/PMS businesses, not "AI trading bots". No incumbent shows large disclosed revenue, which points to a small, fragmented market.

### Cited Findings
- **Streak (Zerodha ecosystem):**
  - No-code algo builder that works only with Zerodha.
  - 2026 reviews list plans of about ₹500 / ₹900 / ₹1,400 per month plus GST, about ₹350 per month on annual billing, with a 7-day trial.
  - Older claims of free access for Zerodha users conflict with this.
  - Sources: [TradersUnited review](https://tradersunited.org/blog/zerodha-streak-review-algo-trading); [Chittorgarh](https://www.chittorgarh.com/article/zerodha-streak-review-algo-trading-for-retail/516/)
  - Streak.tech received investment from 3one4 Capital; the date and amount are not in the results. — [Inc42](https://inc42.com/?p=160504)
- **Tradetron:**
  - Multi-broker, no-code platform plus a marketplace where creators sell strategies that users subscribe to.
  - Free tier; paid plans from about ₹300 per month (per AlgoTest's comparison).
  - Self-reported 405k+ traders, about 60k algos created, and about 175k live trades a day. These are older homepage marketing figures.
  - No disclosed funding. Revenue estimates conflict ($0–6M from modelled sources), and I found no filed financials.
  - Sources: [Tradetron](https://tradetron.tech/); [AlgoTest pricing comparison](https://algotest.in/blog/algo-trading-software-price-in-india.md); [Tracxn](https://tracxn.com/d/companies/tradetron/__T78jhhTxXqcdYY12WjAY9586soFz-pT9MbUjJRV7G_o); [Growjo](https://growjo.com/company/Tradetron)
- **AlgoTest:**
  - Options backtesting and algo platform, YC-backed. Raised about $0.5M in Aug 2022.
  - Revenue ₹3.2 Cr+ in FY24 (Inc42 Datalabs). Headcount about 30–35 as of Jul 2026. Secondary-market valuation estimate about $20M (Caplight).
  - Sources: [Inc42 AlgoTest funding](https://inc42.com/company/algotest/funding/); [Caplight](https://www.caplight.com/company/algotest); [CB Insights](https://www.cbinsights.com/company/algotest/financials)
- **Sensibull:** Options trading and analytics platform, seeded with ₹2.5 crore by Zerodha/Rainmatter in 2018. No later rounds found. — [The News Minute](https://www.thenewsminute.com/article/stock-trading-startup-sensibull-raises-rs-25-crore-fintech-fund-rainmatter-87216)
- **uTrade Algos:** Algo automation platform that connects to brokers like Kite. Pricing is unclear; one comparison says it was temporarily free. — [uTrade FAQ](https://www.utradealgos.com/faqs/is-utrade-algos-similar-to-zerodha-or-groww-how-is-it-better); [AlgoTest comparison](https://algotest.in/blog/algo-trading-software-price-in-india.md)
- **AlgoBulls:** Raised funding led by Venture Catalysts and is integrated with more than 35 brokers. Date not captured. — [Inc42](https://inc42.com/?p=371404)
- **Wright Research:**
  - SEBI-registered RA and PMS offering "AI-powered, quantitative portfolios", including through smallcase.
  - Self-reports advising and managing more than ₹1,200 crore and serving more than 2 lakh investors. An older article (about 4 years ago) put it at about ₹200 crore AUA and 40k subscribers.
  - Sources: [Wright Research homepage](https://www.wrightresearch.in/); [Wright PMS page](https://www.wrightresearch.in/portfolio-management-service/); [Wright on smallcase](https://wrightresearch.smallcase.com/)
- **OpenAlgo:** An open-source algo/execution platform, which adds free competition at the tooling layer. — [OpenAlgo](https://openalgo.in/)

### Inferences
- **Price points and scale are low.** Retail algo SaaS sells at about ₹300–1,500 per month, and the best-documented independent player (AlgoTest) had about ₹3 Cr revenue in FY24 after years of operation. A new entrant would face a thin-margin, crowded market, plus new empanelment and broker-integration costs.
- **The scalable regulated model is quant RA/PMS.** Wright Research's growth to a self-reported ₹1,200 crore suggests that "quant + AI" works best as a SEBI-registered advisory or portfolio product (long-only, lower turnover), not as F&O bot automation.

### Gaps
- I found no reliable data on Quantiply, Tejimandi, smallcase's quant-manager AUM, or the Upstox and Dhan API ecosystems' user counts.
- I found no FY25 or FY26 filed revenue for Tradetron, Sensibull or Streak, and no confirmation of which platforms completed exchange empanelment after April 2026.

## 4. Evidence on ML/LLM-driven trading, and whether "train a model on 5–7 algos" is sound

### Takeaway
Rigorous evidence is strongly sceptical. LLM trading "alpha" largely disappears under longer, broader, bias-controlled backtests. Backtests are inflated by look-ahead and memorisation leakage, survivorship and multiple testing. Published anomalies lose about 58% of their returns after publication. Training a model on the outputs of 5–7 strategies is statistically weak: the sample is tiny, the strategies' track records are themselves selected, and the model would amplify any overfitting.

### Cited Findings
- **FINSABER (Li, Kim, Cucuringu, Ma; arXiv 2505.07078, v1 May 2025, rev. Jun 2026; KDD 2026 D&B oral):**
  - In two decades of backtests over more than 100 symbols, previously reported advantages of LLM timing strategies "deteriorate significantly".
  - LLM strategies are too conservative in bull markets (underperforming passive benchmarks) and too aggressive in bear markets (heavy losses).
  - Earlier positive results came from narrow universes with "survivorship and data-snooping biases".
  - Source: [arXiv 2505.07078](https://arxiv.org/abs/2505.07078)
- **Memorisation and look-ahead bias:**
  - LLMs memorise historical outcomes, creating "parametric look-ahead bias" in backtests.
  - The FinCAD paper reports in-sample return corrections as large as −67.1% (model-level mean) after mitigating memorisation.
  - Source: [arXiv 2605.24564](https://arxiv.org/html/2605.24564)
  - Gao, Jiang and Yan propose a statistical test for whether an LLM forecast's predictive power comes from memorisation. — [arXiv 2512.23847](https://arxiv.org/pdf/2512.23847)
- **Agentic-layer leakage:**
  - Point-in-time-trained models are the most rigorous fix but are much smaller than frontier LLMs. Leakage also arises at the agent layer, through LLM-as-judge steps and agent interaction. — [arXiv 2604.02279](https://arxiv.org/pdf/2604.02279)
  - News timestamps without modelled ingestion lag inflate backtests. — [arXiv 2605.19337 survey](https://arxiv.org/html/2605.19337v1)
  - Model knowledge cutoffs are "opaque and not verifiable". — [arXiv 2602.14233](https://arxiv.org/html/2602.14233v1)
- **Backtest overfitting (Bailey, Borwein, López de Prado, Zhu):**
  - Conventional hold-out tests are unreliable for investment backtests. They propose estimating the Probability of Backtest Overfitting (PBO) via combinatorially symmetric cross-validation.
  - The Deflated Sharpe Ratio (Bailey & López de Prado, JPM 2014) corrects for selection bias from multiple trials and for non-normal returns.
  - Sources: [SSRN 2326253](https://papers.ssrn.com/abstract=2326253); [SSRN 2460551](https://papers.ssrn.com/abstract=2460551)
- **Alpha decay (McLean & Pontiff, Journal of Finance 2016):** Across 97 published return predictors, returns are 26% lower out-of-sample and 58% lower post-publication. This is consistent with data mining plus arbitrage by informed investors. — [McLean & Pontiff PDF](https://Www.Gwern.net/doc/economics/2016-mclean.pdf)
- **Institutional dominance:** In India, 96–97% of prop and FPI F&O profits come from algorithms (SEBI FY24 study). Profitable algo trading is dominated by well-resourced institutions. — [Moneylife](https://www.moneylife.in/article/93-percentage-of-individual-traders-lost-rs18-lakh-crore-in-equity-fo-in-past-3-years-sebi/75210.html)

### Inferences
- **"5–7 algos that have shown results" is a weak base for model training:**
  - Five to seven strategy return streams are far too few samples to train a generalisable model.
  - "Shown results" is itself a selection filter: the best of many tried strategies, which is exactly the bias the Deflated Sharpe Ratio and PBO are meant to correct.
  - A meta-model trained on these outputs mostly learns their historical regime-specific behaviour and compounds the overfitting.
  - A defensible version would be a regime-aware ensemble or allocator with strict walk-forward, PBO/DSR testing, transaction-cost and slippage modelling for Indian F&O (STT, exchange fees, impact), and live paper-trading before any capital.
- **The friend's instinct has a valid core.** You need genuine, independently verified out-of-sample edge before building a product on it. But the evidence suggests most retail-built edges will not survive costs and decay. The product should not depend on the team having alpha.
- **LLMs are best used around trading, not as the signal.** Good uses are research, summarising, journaling and risk explanation. LLMs as direct return predictors are where the evidence is weakest.

### Gaps
- I did not verify specific claims that GPT-4o recalls S&P closing prices to under 1% error; they come from a secondary source only.
- I found no India-specific peer-reviewed evidence on ML or LLM strategies in NSE F&O after costs.
- FinGPT and similar open-source finance LLMs were not specifically evaluated here.

## 5. Lower-risk adjacent opportunities

### Takeaway
The evidence favours products that do not promise returns: backtesting and strategy-validation tooling (overfitting checks), risk dashboards, behavioural and loss-prevention copilots for the 9-in-10 who lose, and quant factor portfolios delivered through a registered RA, smallcase or PMS. Each still has regulatory edges, since advice or recommendations trigger RA/IA rules.

### Cited Findings
- **The behavioural problem is large and persistent:**
  - More than 75% of loss-makers kept trading despite repeated losses.
  - The top 3.5% of loss-makers lost about ₹28 lakh each.
  - Individuals spent about ₹50,000 crore on transaction costs in FY22–24.
  - Source: [Moneylife](https://www.moneylife.in/article/93-percentage-of-individual-traders-lost-rs18-lakh-crore-in-equity-fo-in-past-3-years-sebi/75210.html)
- **The tooling market is proven but small:** Backtesting and strategy research already sell (AlgoTest about ₹3.2 Cr revenue in FY24; Streak paid tiers). — [Inc42 AlgoTest](https://inc42.com/company/algotest/funding/); [TradersUnited Streak review](https://tradersunited.org/blog/zerodha-streak-review-algo-trading)
- **The quant-portfolio route has traction:** Wright Research self-reports more than ₹1,200 crore advised or managed through RA/PMS and smallcase distribution. — [Wright Research](https://www.wrightresearch.in/)
- **Cheap infrastructure:** Broker order APIs are now free and data APIs cheap (Zerodha ₹500 per month), which lowers costs for analytics and journaling tools that only read data. — [Zerodha Z-Connect](https://zerodha.com/z-connect/general/a-comprehensive-overview-of-nses-circular-on-the-new-retail-algo-trading-framework)
- **Scientific basis for validation tools:** PBO and the Deflated Sharpe Ratio give a rigorous basis for an "is my backtest overfit?" product. — [SSRN 2326253](https://papers.ssrn.com/abstract=2326253); [SSRN 2460551](https://papers.ssrn.com/abstract=2460551)

### Inferences
- **Read-only, education-style tools carry the least regulatory risk:**
  - Journaling and P&L analytics.
  - Overfitting and cost-realism checks on users' own backtests.
  - Behavioural nudges, such as loss-streak alerts and position-size warnings.
  - These do not execute orders or recommend specific trades, so they likely avoid algo-provider empanelment. Any specific buy/sell recommendation would still raise RA/IA questions. This is inferred and needs legal confirmation.
- **SEBI is pushing retail away from F&O.** Positioning as "loss prevention" fits SEBI's policy direction. Positioning as "AI trading profits" works against it.
- **Quant factor portfolios via RA/smallcase are the most proven monetisable "quant + AI" path for a small team.** They require SEBI RA registration and a credible track record, and they compete with Wright Research and other smallcase managers.

### Gaps
- I found no market-size or revenue data for trading-journal or behavioural-copilot products in India.
- I found no SEBI guidance specifically on AI copilots or LLM chat in trading apps.
- I found no smallcase platform-level data on quant-strategy AUM as of 2026.
