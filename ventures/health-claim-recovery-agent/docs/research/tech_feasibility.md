# Technical feasibility & build blueprint: AI mutual-fund assistant/agent (India)

Research date: 2026-10-07. Proposal being assessed: "Scrape every law, data source, market feed and plan for mutual funds, fine-tune a small model, build a chatbot and test its correctness with 50–70 users, then build an agent that lets users invest in these funds. The agent never touches money."

Overall view: the data and the transaction rails both exist and are reachable by a 1–3 person team. The weak part of the plan is "fine-tune a small model". The 2024–2026 evidence favours retrieval (RAG) plus deterministic tool calls on a frontier or mid-tier model. "Agent never touches money" is already how the rails work: SEBI forbids distributors from handling funds or units, and payments flow through the clearing corporation or AMC. The binding constraint is licensing (ARN/MFD, RIA or EOP), not the technology.

## 1. Data sources: what exists, how to get it, licensing and scraping legality

### Takeaway
Core NAV and scheme data is free and machine-readable. Sources are AMFI, mfapi.in, and open-source archives such as captn3m0/historical-mf-data with 20M+ NAV rows. Portfolio holdings are published monthly by every AMC and aggregated on AMFI, but each AMC uses its own Excel layout, so expect a per-AMC parser. Value Research and Morningstar publish no API or licence terms, so their data must be licensed by negotiation and must not be scraped. Regulatory text (SEBI circulars, SID/KIM/SAI) is public and suits RAG.

### Cited Findings
- mfapi.in is a free, keyless JSON API. Endpoints: list of all funds, full NAV history per scheme at `/mf/{scheme-code}`, and search at `/mf/search?q=`. One guide says data updates 6 times a day. Rate limits and terms of use were not confirmed. — [plus2net guide](https://www.plus2net.com/python/bs4-automate-mutual-fund-nav-tracking-mfapi.php); [qveris guide](https://qveris.ai/guides/free-mutual-fund-data-api/)
- The amfipy Python client downloads AMFI's flat file NAVAll.txt for any date. — [PyPI amfipy](https://pypi.org/project/amfipy/)
- captn3m0/historical-mf-data archives all historical Indian MF NAVs as a compressed SQLite release (funds.db.zst, versioned MAJOR.MINOR.YYYYMMDD). It keeps AMFI's data-quality problems: invalid ISINs such as "NOTAPP" or "IINF" prefixes, and NAV values such as "#N/A" or "#DIV/0!". — [GitHub captn3m0/historical-mf-data](https://github.com/captn3m0/historical-mf-data)
- InertExpert2911/Mutual_Fund_Data publishes a daily scheme snapshot CSV and a Parquet NAV history with more than 20 million records, adding about 6,000 a day. — [GitHub](https://github.com/InertExpert2911/Mutual_Fund_Data)
- Other scrapers: AmruthPillai/AMFI-NAV-History-Scraper, and mftool-based exporters. — [GitHub AmruthPillai](https://github.com/AmruthPillai/AMFI-NAV-History-Scraper); [GitHub Himangshu4Das](https://github.com/Himangshu4Das/AMFI-NAV-data-using-mftool)
- AMFI's Research & Information page lists monthly portfolio files in Excel and PDF, grouped by financial year. — [AMFI](https://www.amfiindia.com/research-information/amfi-monthly)
- SEBI requires AMCs to disclose portfolios with ISINs as of month-end on their websites by the 10th of the next month. Half-yearly disclosures must be in a "user-friendly and downloadable spreadsheet format" on both the AMC and AMFI sites. — [Baroda BNP Paribas MF disclaimer](https://www.barodabnpparibasmf.in/efactsheet/Jan2025/Innerpages/Disclaimer.html); [HSBC MF periodic disclosure](https://www.assetmanagement.hsbc.co.in/assets/documents/mutual-funds/en/b7b15941-f284-4191-a34b-a1fc7e3f03dc/periodic-disclosure.pdf)
- Value Research and Morningstar India: no published API, pricing or licence terms were found. A forum thread says VR aggregates AMC disclosures and sells data, and names CRISIL, ACE MF and Accord as other vendors (unverified). Morningstar India pages carry a notice that its ESG data is not intended for India-based users as of Dec 2023, which suggests restrictive distribution terms. — [TradingQnA thread](https://tradingqna.com/t/where-does-valueresearchonline-get-its-mf-data-from/151389); [Morningstar India factsheet page](https://morningstar.in/mutualfunds/f00000pdzc/hdfc-value-fund--direct-plan-payout-inc-dist-cum-cap-wdrl-opt/fund-factsheet.aspx)
- SEBI runs its own GenAI investor chatbot, "SEVA", in beta. It answers questions on securities-market information and the latest master circulars. This shows that regulatory-text Q&A is already a commodity. — [Taxmann](https://www.taxmann.com/post/blog/sebi-launches-chatbot-seva-for-investors/); [Cafemutual](https://cafemutual.com/news/industry/32720-sebi-launches-generative-ai-for-investors)

### Inferences
- A practical data stack for the MVP:
  - NAVs: AMFI NAVAll.txt daily, or mfapi.in, with the captn3m0 SQLite release as the history backfill.
  - Scheme master and categorization: AMFI.
  - Holdings: AMC monthly portfolio Excel files from AMFI or AMC sites.
  - Regulatory corpus: SEBI master circulars, SID/KIM/SAI PDFs and AMFI documents, chunked and versioned with effective dates.
  - TER: AMFI publishes it, though this was not separately verified (see Gaps).
- Third-party ratings and analytics from Value Research, Morningstar or CRISIL should be licensed, not scraped. Commercial use of scraped VR/MS content is the main legal risk in "scrape everything". Regulator, AMFI and AMC disclosures are public statutory disclosures and are lower risk, but check the site terms and robots.txt.
- "Scrape every law" is a bounded, tractable job: SEBI MF Regulations, the MF master circular, the IA/RA regulations, Income-tax sections relevant to MF capital gains, and AMFI's code of conduct. It is a RAG corpus of a few thousand pages, not a pretraining-scale dataset.
- Budget engineering time for data cleaning. Invalid ISINs, scheme merges and renamed schemes, IDCW/growth/direct/regular variants, and per-AMC portfolio layouts are known issues.

### Gaps
- The exact AMFI NAVAll.txt URL, the TER disclosure page and AMFI's terms of use and robots.txt were not fetched in this session. (From general knowledge, the URL is `amfiindia.com/spages/NAVAll.txt`; verify it.)
- mfapi.in's rate limits, SLA and licence are unknown.
- Kaggle datasets were not checked.
- No source documents how the column layouts of AMC portfolio Excel files differ.

## 2. Portfolio import: CAS parsing, MF Central, CDSL/NSDL eCAS, Account Aggregator

### Takeaway
There are three viable routes, in increasing order of effort:
1. User uploads a password-protected CAS PDF, parsed with the open-source casparser. This is free and fast, and suits the MVP.
2. The MFCentral CAS API, using PAN plus an OTP. It is gated and requires production access, usually through a licensed intermediary or integrator.
3. Account Aggregator as an FIU. Holdings come from CAMS/KFintech acting as FIPs. Becoming an FIU needs a regulated-entity licence plus Sahamati onboarding, and costs are negotiated (roughly ₹2.5–₹20 per fetch in the few public data points).

### Cited Findings
- casparser (codereverser/casparser) is a Python library and CLI. It parses CAMS, KFintech, NSDL and CDSL CAS PDFs, given a file path and password, into JSON or CSV with typed pydantic models and JSON Schema. It can produce capital-gains reports and CSVs for ITR Schedule 112A. It does not support re-printed PDFs. Since v1.0 it is built on pypdfium2 (Apache-2.0/BSD-3), which avoids the AGPL issues of the older PyMuPDF backend. — [GitHub casparser](https://github.com/codereverser/casparser); [PyPI](https://pypi.org/project/casparser/0.4.5/)
- MFCentral, run by CAMS and KFintech, offers APIs for CAS, transactions (financial and non-financial) and information-only data such as capital gains. Distributors and RIAs use them to build consolidated holdings views. — [MProfit MF Central CAS API terms](https://www.mprofit.in/mfcentral-cas-api-terms/); [equitiesindia glossary](https://equitiesindia.com/glossary/mf-central)
- The MFCentral CAS fetch needs PAN, email, mobile and an OTP sent to the investor's registered contact. Integrators must "procure production access with MF Central". — [MProfit terms](https://www.mprofit.in/mfcentral-cas-api-terms/); [Geojit FundsGenie support](https://support.geojit.com/support/solutions/articles/89000018852-how-to-fetch-my-central-consolidated-account-statement-cas-from-fundsgenie-)
- Fold (a wealth app) skips the AA route for MF holdings and uses MFCentral with OTP consent instead. — [Fold help](https://help.fold.money/hc/en-us/articles/17257917644690-How-do-you-fetch-my-investment-data)
- CAMS and KFintech have announced a 50:50 JV to spin MFCentral out as a separate entity. No date was found. — [Angel One news](https://www.angelone.in/news/share-market/cams-and-kfintech-launch-joint-venture)
- AA pricing (no official MF-specific rate card exists):
  - Perfios FIU Lite: ₹1,000/month billed annually, including 100 fetches, then ₹20 per fetch with a minimum of 200, plus GST. — [Perfios](https://perfios.ai/in/products/fiu-lite/)
  - Finvu: ₹3–6 per account and about ₹2.50 per fetch, from a third-party page updated May 2026 that cites no named source. Unverified. — [productgrowth.in Finvu](https://productgrowth.in/tools/banking-api/finvu/)
  - Typical Setu deployments: ₹3L–₹2Cr a year (platform-level figure, third party). — [productgrowth.in Setu](https://productgrowth.in/tools/banking-api/setu/)
  - Sahamati has a committee studying FIP-side pricing, so data-pull costs may rise. — [Sahamati Pricing FIPs Committee ToR](https://sahamati.org.in/wp-content/uploads/2023/11/Pricing-FIPs-Committee-ToR.pdf)
- CDSL is listed as an FIP on the AA network. — [CDSL FIP page](https://www.cdslindia.com/Investors/FIP.html)

### Inferences
- MVP (50–70 users): CAS PDF upload plus casparser. Engineering is about 1–3 days, the marginal cost is zero, and no licence is needed for read-only analysis. UX friction: users must request a detailed CAS from CAMS, KFintech or MFCentral by email and enter the PDF password. Store parsed data encrypted and allow deletion (DPDP Act consideration).
- Post-licence: the MFCentral CAS API (OTP-based) gives the best UX for MF-only holdings. AA is worth adding only if the product expands to bank, equity or insurance aggregation. FIU status requires being a regulated entity, such as a SEBI RIA or a broker.
- Effort estimates (inference, not sourced): AA integration via a TSP such as Setu, Finvu or OneMoney is about 2–6 weeks plus legal and Sahamati onboarding. The MFCentral API depends on gated partner access, so the timeline is driven by BD, not engineering.

### Gaps
- No public MFCentral developer docs, pricing or eligibility criteria were found.
- No official AA per-fetch tariff for CAMS/KFintech MF data.
- OneMoney and CAMS Finserv AA pricing were not found.
- No CDSL/NSDL eCAS API terms for third parties were found.

## 3. Transaction execution: rails, partners, and which licence the startup needs

### Takeaway
The agent can only place orders as, or through, a licensed entity. There are three legal paths:
- **(a) ARN/MFD:** become an AMFI-registered distributor (NISM V-A plus ARN) and transact on BSE StAR MF or NSE NMF II, directly or via an API layer such as Fintech Primitives/Cybrilla POA. This route sells regular plans and earns trail commission, and advice must stay incidental.
- **(b) SEBI RIA:** fee-based advice on direct plans, with execution via BSE StAR MF (RIAs are allowed) or an API partner.
- **(c) EOP:** a Category 1 EOP registered with AMFI as an AMC agent, or Category 2 via a stock-broker licence, for execution-only direct plans with no advice.

An AI "advisor" that recommends specific funds is advice and pushes towards RIA. An "execution + information" agent fits EOP or MFD.

In every structure, money moves from the investor's bank to the clearing corporation or AMC through UPI, netbanking or mandates. Distributors are barred from handling pay-in or payout, so "agent never touches money" is the default, not a differentiator.

### Cited Findings
- **BSE StAR MF:**
  - Applicants need a valid AMFI ARN. Corporates need ₹1 lakh net worth or paid-up capital.
  - A listed lifetime MFD fee is ₹16,854. Another BSE page calls activation "free of cost". The sources conflict; confirm with BSE.
  - BSE issued a master circular for StAR MF transactions on 29 Apr 2026 (updated to 31 Mar 2026). It covers onboarding/KYC, order placement, cut-offs, NAV applicability and payments. — [BSE MFD registration](https://bseindia.com/static/members/Mutual_Fund_Distributor_Registration.aspx); [BSE Annexure1_MFD](https://www.bseindia.com/downloads1/Annexure1_MFD.doc); [TeamLease RegTech summary](https://teamleaseregtech.com/updates/article/55308/bse-notified-regarding-the-master-circular-for-transactions-on-bse-star-mf-platform/)
- SEBI's framework says distributors "shall not handle payout and pay in of funds as well as units on behalf of investors". — [BSE MFD registration page](https://bseindia.com/static/members/Mutual_Fund_Distributor_Registration.aspx)
- BSE StAR MF launched Aadhaar and video-KYC onboarding integrated with KRAs in May 2020. — [NSE intimation of BSE release, 2020](https://nsearchives.nseindia.com/corporate/BSE_26052020155025_NSEIntimation.pdf)
- RIAs can use the BSE StAR MF platform (since Nov 2019). — [Cafemutual](https://cafemutual.com/news/industry/6751-rias-can-start-using-bse-star-mf-platform-from-november-4)
- An older open-source wrapper (utkarshohm/mf-platform-bse, about 2017) described the BSE API as SOAP, with some functions such as order-status tracking available only on the web portal. This is dated, so verify the current API spec. — [GitHub mf-platform-bse](https://github.com/utkarshohm/mf-platform-bse)
- **NSE NMF II:**
  - Open to trading members and AMFI-registered distributors, who need limited-purpose membership with NSE.
  - Supports purchase, redemption, SIP, SWP, STP and switches.
  - An API links a distributor's website to NSE's payment gateway (undated trade press). — [NSE NMF II FAQ](https://www.nseindia.com/products/content/equities/mutual_funds/NMF_II_FAQ.pdf); [NSE NMF Operating Guidelines](https://www.nseindia.com/products/content/equities/mutual_funds/NMF_Operating_Guidelines.pdf); [Cafemutual](https://cafemutual.com/news/industry/4758-nse-mf-ii-introduces-multiple-sip-registration-facility-for-distributors)
- **Fintech Primitives (FP, by Cybrilla):**
  - A PaaS whose APIs cover KYC status, digital KYC, investor profiles and bank verification; lumpsum, redemption, switch, SIP/SWP/STP with pause; payments via netbanking, UPI, eNACH and UPI Autopay; portfolio and capital-gains reports; and a sandbox for the Cybrilla POA gateway.
  - The pricing model is "pay as you use", with no figures published.
  - It markets "distribute mutual funds online in just 3 weeks". — [FP docs](https://docs.fintechprimitives.com/); [FP home](https://fintechprimitives.com/)
- Cybrilla POA is marketed to distributors with no payment-gateway charges, no annual or maintenance API fee, no ops cost and no KYC cost, under a single agreement for multiple AMCs. This is vendor or directory marketing and not independently verified. — [The Wealth Mosaic: Cybrilla POA](https://www.thewealthmosaic.com/vendors/cybrilla/cybrilla-poa/); [FP vs Cybrilla POA](https://docs.fintechprimitives.com/fp-cybrillapoa-gateway/fp-vs-cybrillapoa)
- FP docs have an "advisory" section, which suggests RIA-oriented flows. The page returned 403 and was not read. — [FP advisory overview](https://docs.fintechprimitives.com/advisory/overview)
- **EOP framework:** SEBI circular SEBI/HO/IMD/IMD-PoD-1/P/CIR/2023/86 (13 Jun 2023), effective 1 Sep 2023.
  - Category 1 EOP: agent of AMCs, registered with AMFI.
  - Category 2 EOP: agent of investors, registered as a stock broker.
  - EOPs provide no investment advice.
  - IA and broker platforms such as Groww, Zerodha Coin and Paytm Money were exempt from separate EOP registration. — [Taxmann](https://www.taxmann.com/post/blog/sebi-introduces-framework-for-execution-only-platforms-for-investing-in-direct-plans-of-mf-schemes/); [Khaitan & Co](https://khaitanco.com/thought-leaderships/SEBIs-framework-facilitating-mutual-fund-direct-plans-invested-through-execution-only-platforms); [AZB](https://www.azbpartners.com/bank/sebi-introduces-comprehensive-framework-on-execution-only-platforms-for-transactions-in-direct-plans-of-mf-schemes/)
- **MFD vs RIA boundary:**
  - An ARN requires NISM V-A plus KYD, and certification is valid for 3 years.
  - An MFD earns trail commission on regular plans and may give only suitability guidance "incidental to distribution". It cannot charge for advice and cannot offer financial planning that needs risk profiling or goal setting.
  - Since 2020, MFDs cannot call themselves "IFA" or "wealth adviser", and individual RIAs cannot distribute. — [Morningstar India](https://morningstar.in/posts/59666/can-cant-mutual-fund-distributor.aspx); [Wealthy partner blog](https://www.wealthy.in/partner-desk/partner-blog/mutual-fund-distributor-meaning-role-534); [Cafemutual](https://cafemutual.com/news/industry/18456-distributors-cannot-call-themselves-ifas-or-wealth-advisor-sebi?page=2); [SEBI 2017 consultation](https://www.sebi.gov.in/sebi_data/attachdocs/jun-2017/1498123540574.pdf)
- **SEBI AI/ML:**
  - A June 2025 consultation paper proposed guidelines covering model governance, investor disclosure, testing, fairness/bias, and data privacy/cyber security.
  - Intermediaries would need skilled internal oversight teams and must disclose AI use in advisory work to clients.
  - Intermediaries stay liable even when the AI is outsourced. Comments closed 11 Jul 2025.
  - Since January 2025, research analysts must disclose AI tool use.
  - Secondary sources say AI-using advisers are solely responsible for the accuracy of AI output, and that a broader "AI accountability framework" with audit logs was in preparation in 2026. No final consolidated circular was found. — [IndiaCorpLaw](https://indiacorplaw.in/2025/07/16/from-algorithms-to-accountability-analysing-sebis-ai-ml-governance-framework/); [TaxGuru](https://taxguru.in/sebi/sebi-proposes-guidelines-responsible-usage-ai-ml-indian-securities-markets.html); [Mondaq 2026](https://www.mondaq.com/india/securities/1759228/sebis-new-digital-compliance-rules-what-investment-advisers-must-know-in-2026); [CAalley](https://caalley.com/news-updates/indian-news/sebi-proposes-5-point-ai-rulebook-for-securities-market-check-details)

### Inferences
- Fastest legal path for a 1–3 person team: one founder obtains NISM V-A and an ARN (weeks, low cost), and the team integrates through Fintech Primitives/Cybrilla POA or BSE StAR MF.
  - This means selling regular plans with commission. The AI must frame outputs as information or suitability, not personalised advice.
  - FP's "3 weeks" claim is plausible for basic order flows; plan 4–8 weeks including KYC, mandates and reconciliation.
- If the value proposition is "AI tells me which fund to buy", that is investment advice. It needs SEBI RIA registration, with its qualification, net-worth and fee rules (not researched here), and direct plans.
  - Under SEBI's AI proposals, the RIA stays fully liable for the AI's output, which raises the bar for evaluation and audit logs.
- A Category 1 EOP (AMFI-registered, execution-only for direct plans) fits an "information + execution, no advice" agent. Its registration requirements and timelines were not researched here.
- Agent design implication: the LLM should never submit an order autonomously. It drafts an order object (scheme ISIN, amount, plan, folio). The UI shows a deterministic confirmation screen, the user authenticates via the platform's 2FA/OTP, and payment happens through UPI or a mandate on the user's own bank app. Log every step immutably.

### Gaps
- Not researched or not found: current product pages and pricing for Zerodha Coin (no public third-party MF order API is known), Kuvera B2B, Smallcase Gateway (mainly stocks/ETFs), Dhan and Upstox developer APIs for MF, MF Utilities (MFU) API access, Wealthy/FundsIndia B2B, Tarrakki and Upwardly.
- FP and Cybrilla per-transaction pricing is not published.
- Current BSE StAR MF API spec (REST vs SOAP) and sandbox access were not verified.
- RIA registration requirements (NISM X-A/X-B, net worth, fee caps) and EOP Category 1 eligibility were not fetched in this session.
- No final SEBI AI/ML circular was located; status as of Oct 2026 is uncertain.

## 4. AI approach: fine-tuning a small model vs RAG + tool use with a frontier model

### Takeaway
For a domain whose facts change daily (NAVs) or monthly (holdings, TER, circulars), and where answers are numerical, fine-tuning a small generator is the wrong first move:
- In the main FinanceBench study, it lowered faithfulness.
- It does not keep up with new facts.
- Frontier models already score 70–90% on Indian regulatory-text QA zero-shot.

Use RAG over versioned documents plus deterministic tools for every number: NAV lookup, XIRR, overlap, capital-gains tax. A frontier or mid-tier model orchestrates. Consider fine-tuning only later, and only for the retriever/embedder or for narrow classifiers such as intent and advice-boundary detection.

### Cited Findings
- Nguyen et al., FinanceBench (human-judged accuracy):
  - Generic RAG 37%, fine-tuned generator 43%, fine-tuned retriever 54%, fully fine-tuned RAG 59%. An iterative-reasoning layer (OODA) reached 85%.
  - Fine-tuning the generator lowered faithfulness from 0.700 to 0.625, and full fine-tuning lowered it to 0.512. — [arXiv 2404.11792](https://arxiv.org/html/2404.11792)
- Retrieval-side improvements (query preprocessing, embedder fine-tuning, hybrid retrieval, reranking) improve financial QA. FinSage's DPO-tuned reranker reported +24.06% accuracy over the best baseline on FinanceBench. — [arXiv 2503.15191](https://arxiv.org/pdf/2503.15191); [FinSage arXiv 2504.14493](https://arxiv.org/pdf/2504.14493)
- Zero-shot retrieval improvements alone are "not enough for highly accurate systems". — [arXiv 2404.07221](https://arxiv.org/pdf/2404.07221)
- FinTradeBench chose RAG over fine-tuning because fine-tuning would be costly to repeat on every data refresh. — [arXiv 2603.19225](https://arxiv.org/html/2603.19225v4)
- Fine-tuning vs RAG on multi-hop QA: on new, post-training knowledge (a 2024 events dataset), RAG more than doubled accuracy while unsupervised fine-tuning gave marginal gains. Supervised fine-tuning won on static knowledge (QASC). — [arXiv 2601.07054](https://arxiv.org/html/2601.07054v1)
- A self-improving RAG system reported 86% on FinanceBench; most of the gain came from prompt escalation. — [arXiv 2608.26706](https://arxiv.org/html/2608.26706)
- IndiaFinBench: 406 expert-annotated QA pairs from SEBI and RBI documents, covering interpretation, numerical reasoning, contradiction detection and temporal reasoning. Twelve models scored 70.4% (Gemma 4 E4B) to 89.7% (Gemini 2.5 Flash) zero-shot, against a non-specialist human baseline of 60%. — [arXiv 2604.19298](https://arxiv.org/pdf/2604.19298)
- CA-Ben (ICAI exam questions): Llama 3.1 405B averaged 49.79% but scored only 13.33% on Direct Tax Laws and 20% on Taxation. LLMs are weak on Indian tax computation without tools. — [Moonlight review of "LLMs Acing Chartered Accountancy"](https://www.themoonlight.io/de/review/large-language-models-acing-chartered-accountancy)
- Taxmann.AI × IIT Kharagpur LE-BTL study benchmarked 12 LLMs on Indian Income Tax, GST and FEMA law using IRAC+ scoring. — [Taxmann](https://www.taxmann.com/post/blog/taxmann-ai-x-iit-kharagpur-llm-evaluation-le-btl-benchmark-study)
- IndFin-Bench: 100 questions built from Indian listed-company filings, on Hugging Face. — [CompoundingAI Substack](https://compoundingai.substack.com/p/introducing-indfin-bench-a-pioneering)

### Inferences
- Recommended architecture, from the evidence above:
  - A frontier or mid-tier LLM such as Claude Sonnet/Haiku or Gemini Flash as orchestrator.
  - Hybrid retrieval (BM25 plus embeddings plus reranker) over a versioned corpus of SEBI/AMFI/SID/KIM/tax documents with effective dates.
  - Python tools for every numeric output, with the LLM forbidden to state a number that did not come from a tool or a cited document.
  - Citations rendered to the user.
- Fine-tuning a 1–8B model (Llama, Qwen, Gemma) would mean 2–6 weeks of data curation, recurring retraining as NAVs, TER and tax rules change, and possibly lower faithfulness. It does not fix numeric hallucination; tools do.
  - Defensible later uses: (i) fine-tuning the embedder or reranker on MF queries; (ii) a small, cheap classifier or router for intent, PII and the advice-boundary guardrail; (iii) distilling a cheaper model once there are thousands of logged, verified conversations.
- "Check correctness with 50–70 users" is not an evaluation method. Users cannot judge whether a tax figure or an expense-ratio claim is right. Correctness needs an offline golden set graded by experts (see section 5), with users testing usefulness and UX.

### Gaps
- No study was found that directly compares a fine-tuned small model with frontier RAG on Indian MF/personal-finance Q&A.
- No India-specific MF or tax-computation benchmark exists on arXiv. The LE-BTL and CA-Ben details are from secondary pages.

## 5. Evaluation, guardrails and agent patterns (tools, MCP, human-in-the-loop, audit)

### Takeaway
Build a golden evaluation set of about 300–500 items before any user testing. It should cover NAV/returns lookups, XIRR, overlap, LTCG/STCG tax under current rules, SID/KIM facts, regulatory questions, and adversarial "which fund should I buy" prompts. Score numbers by exact or tolerance matching against tool outputs, and score text by expert or LLM-judge rubric for faithfulness and citation.

MCP is a convenient way to expose tools; Zerodha's official Kite MCP server exists, but its MF coverage is thin. Execution must be human-in-the-loop with a deterministic confirmation step and immutable audit logs, which SEBI's AI proposals also point towards.

### Cited Findings
- The official zerodha/kite-mcp-server is Go, MIT-licensed, supports stdio and streamable-HTTP, implements most Kite Connect endpoints, and has hosted and self-hosted options. Its MF tool coverage was not confirmed. Third-party forks expose `get_mf_holdings` and MF SIP listing (marked experimental). — [claudemarketplaces: zerodha/kite-mcp-server](https://claudemarketplaces.com/mcp/zerodha/kite-mcp-server); [glama: Sundeepg98 fork](https://glama.ai/mcp/servers/Sundeepg98/kite-mcp-server); [glama: Kshitij-21 Zerodha MCP](https://glama.ai/mcp/servers/@Kshitij-21/MCP-Server)
- IndiaFinBench, the FinanceBench literature and CA-Ben/LE-BTL provide templates and baselines for task types: regulatory interpretation, numerical reasoning, temporal reasoning, tax. — [arXiv 2604.19298](https://arxiv.org/pdf/2604.19298); [arXiv 2404.11792](https://arxiv.org/html/2404.11792); [Taxmann LE-BTL](https://www.taxmann.com/post/blog/taxmann-ai-x-iit-kharagpur-llm-evaluation-le-btl-benchmark-study)
- SEBI's proposed AI/ML guidelines include a testing framework, client disclosure of AI use, and intermediary liability for outsourced AI. Secondary 2026 commentary mentions audit-log expectations. — [IndiaCorpLaw](https://indiacorplaw.in/2025/07/16/from-algorithms-to-accountability-analysing-sebis-ai-ml-governance-framework/); [Mondaq 2026](https://www.mondaq.com/india/securities/1759228/sebis-new-digital-compliance-rules-what-investment-advisers-must-know-in-2026)
- casparser already produces capital-gains and Schedule 112A outputs, which can serve as a deterministic tax tool and a reference for eval. — [GitHub casparser](https://github.com/codereverser/casparser)

### Inferences
- Tool set for the agent:
  - `get_nav(isin, date)`
  - `get_scheme_facts(isin)` covering category, TER, exit load, benchmark and riskometer
  - `get_portfolio(isin, month)`
  - `compute_xirr(cashflows)`
  - `portfolio_overlap(isins)`
  - `capital_gains(lots, sale_date)`, with current equity/debt rules versioned by date
  - `search_regulations(query, as_of)`
  - `parse_cas(pdf)`
  - Execution tools behind confirmation: `draft_order` and `submit_order(order_id, user_otp)`, plus a mandate flow.
- Ship read-only tools as an internal MCP server so they can be swapped between Claude, GPT and Gemini.
- Guardrails:
  - A classifier flags personalised-recommendation requests. As an MFD, respond with category-level suitability and factual comparisons and avoid "buy X".
  - As an RIA, allow recommendations only after a stored risk profile, with a disclosure that AI is used.
  - Refuse return predictions.
  - Attach a "past performance" disclaimer and source citations to every number.
- Audit: an append-only log of prompts, retrieved docs, tool calls and outputs, model version and user confirmations, kept for regulatory record-keeping. The SEBI retention period for AI logs was not confirmed.
- Eval cadence: run the golden set on every prompt or model change in CI. Track numeric exact-match, citation precision, refusal correctness on advice-bait prompts, and latency. Then run the 50–70-user pilot for usefulness and comprehension, with spot audits by a NISM-certified person or a CA.

### Gaps
- No public Indian MF-specific golden dataset was found.
- No production MF-transaction MCP server was found for BSE, FP or Cybrilla.
- Full tool listings for the Kite MCP server were not verified.

## 6. Indicative costs and timeline; Indic language and voice

### Takeaway
For 50–70 pilot users, running costs are small: LLM API spend of roughly $0.10–$2 per active user per month (estimate), and CAS parsing is free. AA (₹2.5–₹20 per fetch plus a platform fee) and data licences are the meaningful costs post-licence.

Sarvam AI speech-to-text costs ₹30 per audio hour, which makes Hindi or regional-language voice affordable.

A 1–3 person team can ship a read-only RAG+tools assistant in about 6–10 weeks. Transaction capability needs a further 1–3 months, dominated by licensing (ARN is quick; RIA or EOP is slower) and partner onboarding.

### Cited Findings
- LLM list prices (third-party aggregators; verify on the official pages):
  - Claude Haiku 4.5: $1 input / $5 output per million tokens.
  - Claude Sonnet 4.6: $3 / $15.
  - Gemini 2.5 Flash: $0.30 / $2.50.
  - Gemini 3.5 Flash: $1.50 / $9.
  - Gemini Batch API: 50% discount. — [braindetox 2026 comparison](https://braindetox.kr/en/posts/ai_api_pricing_comparison_2026.html); [costbench](https://costbench.com/compare/gemini-api-vs-claude/); [siliconanalysts](https://siliconanalysts.com/data/llm-pricing)
- Sarvam AI STT: ₹30/hour, billed per second. ₹45/hour with diarization. STT plus translate: ₹30/hour. ₹1,000 of free credits per the official page (a third-party blog says ₹100). — [Sarvam pricing docs](https://docs.sarvam.ai/api-reference-docs/getting-started/pricing); [smallest.ai blog](https://smallest.ai/blog/sarvam-ai-speech-to-text-pricing)
- AA: Perfios FIU Lite costs ₹1,000/month (100 fetches) plus ₹20 per extra fetch. The Finvu figure of about ₹2.50 per fetch is unverified. — [Perfios](https://perfios.ai/in/products/fiu-lite/); [productgrowth.in](https://productgrowth.in/tools/banking-api/finvu/)
- BSE MFD fee: ₹16,854 lifetime (older page), against "free of cost" activation on another BSE page. — [BSE Annexure1_MFD](https://www.bseindia.com/downloads1/Annexure1_MFD.doc); [BSE MFI page](https://www.bseindia.com/Static/Markets/MutualFunds/MFI.aspx)
- FP: "pay as you use"; Cybrilla POA is marketed as free of API, PG and KYC charges for distributors (vendor claim). — [FP home](https://fintechprimitives.com/); [Wealth Mosaic](https://www.thewealthmosaic.com/vendors/cybrilla/cybrilla-poa/)

### Inferences
- LLM cost per user (illustrative, not sourced):
  - Assumptions: 20 sessions/month × 5 turns, about 6k input tokens per turn (RAG context plus tools) and about 500 output tokens.
  - Usage: about 600k input and 50k output tokens per user per month.
  - Haiku-class: about $0.85/user/month. Sonnet-class: about $2.55. Gemini 2.5 Flash: about $0.31.
  - Prompt caching and routing (a small model for simple turns) can cut these by half or more.
  - A 70-user pilot is therefore under $200/month in LLM spend.
- Hosting: a managed Postgres with pgvector, one app server and object storage for CAS PDFs is likely ₹3–10k/month at pilot scale (estimate).
- Indic language and voice:
  - Sarvam STT at ₹30/hr means a 3-minute voice query costs about ₹1.5.
  - Frontier LLMs handle Hindi and major Indic languages reasonably well. Sarvam's own LLM, TTS pricing and Bhashini (government, free) were not researched here.
- Timeline for 1–3 people (estimate):
  - Weeks 0–3: data pipeline (AMFI/mfapi/captn3m0 NAVs, scheme master, portfolio parser for the top 10–15 AMCs, regulatory corpus).
  - Weeks 2–6: RAG plus tools (XIRR, overlap, tax via casparser) and the golden eval set.
  - Weeks 6–10: pilot with 50–70 users, read-only, with CAS upload.
  - In parallel: obtain NISM V-A and ARN, or start RIA/EOP registration.
  - Months 3–5: execution via FP/Cybrilla or BSE StAR MF, with KYC, mandates, confirmation UX and audit logging.
  - Skipping fine-tuning saves about 3–6 weeks and GPU spend.

### Gaps
- No official, dated LLM price pages were fetched. The Claude Sonnet 5 introductory price ($2/$10 through 31 Aug 2026) appeared in one aggregator; current rates are unconfirmed.
- Not researched: Bhashini API terms and Sarvam LLM/TTS pricing.
- No hosting cost benchmarks from sources.
- No FP, Cybrilla or BSE per-order fees for API usage.
