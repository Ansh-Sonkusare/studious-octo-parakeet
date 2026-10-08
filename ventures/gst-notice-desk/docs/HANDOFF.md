# Handoff: GST Reconciliation and Notice Desk for CA Firms

As of 8 October 2026 (evidence cut-off 7 October 2026). Rank 3 of 14, weighted score 3.70/5 ([report, Table 10](research/00-full-research-report.md)).

Labels: **Fact** is sourced and linked. **Assumption** or **estimate** is a working number to replace with pilot data. **Unverified** means background knowledge or a single weak source; confirm before relying on it.

## 1 TL;DR

**What.** An AI agent for Indian chartered-accountant (CA) practices that reconciles purchase data (GSTR-2B and the Invoice Management System, IMS) against the client's books, produces a per-supplier action list with rupees of input tax credit (ITC) at risk, chases suppliers, and ingests GST notices (DRC-01C, DRC-01, DRC-01B, ASMT-10), assembling evidence and drafting replies for CA sign-off.

**For whom.** CA firms: 98,967 firms and 159,557 members with practice certificates (Feb 2025, [TaxConcept](https://taxconcept.net/icai/statistics-of-icai-members-students-firms-till-28th-february-2025/), secondary source). The firm buys; its clients benefit.

**Why now.**
- IMS (late 2024) made invoice acceptance a monthly, invoice-by-invoice decision ([CAalley](https://caalley.com/news-updates/indian-news/itc-fraud-worth-rs-74-782-crore-detected-in-fy26-maharashtra-gujarat-lead)).
- Notices are increasingly machine-generated and templated, so machine-drafted replies are feasible (inference, [research note](research/unsolved_smb_payments.md)).
- Detected fake ITC rose from ₹36,373 cr in FY24 to ₹74,782 cr in FY26, about 2.1x ([Jurishour](https://www.jurishour.in/gst/cgst-detects-fake-itc-fraud-fy26-unearthed/)).
- Agents sold to accounting firms drew the largest 2026 rounds (Basis at $1.15B).

**Core bet.** Existing tools reconcile but leave the action (chase the supplier, reverse credit, draft the reply) to a person. An agent that completes the action, with the CA approving and signing, earns a per-GSTIN subscription plus a per-notice fee.

**Counter-risk.** Competitive white space scored only 2/5; Tally shipped built-in AI in June 2026. The wedge is the action and notice layer, not reconciliation.

**90-day success (assumed targets).** 15 firms active on at least 400 GSTINs, at least 8 paying; reconciliation matching CA-verified answers on at least 99% of golden-set invoices; at least 70% of notice drafts accepted with minor edits; citation precision at least 95%; median time to a CA-ready draft under 30 minutes.

## 2 Problem and evidence

ITC depends on the supplier's filing, not on the buyer's payment or the genuine purchase, so the buyer bears the cost of a supplier's failure ([Tally Solutions](https://tallysolutions.com/gst/gstr-2b-reconciliation-mismatches-how-to-fix/)).

| Evidence | Value | Source |
|---|---|---|
| Fake ITC detected FY24 / FY25 / FY26 | 9,190 cases, ₹36,373 cr / 15,283, ₹58,773 cr / 30,162, ₹74,782 cr (detections, not recoveries) | [Jurishour](https://www.jurishour.in/gst/cgst-detects-fake-itc-fraud-fy26-unearthed/) |
| Evasion detected FY21-FY25 | About ₹7.08 lakh cr, of which fake ITC about ₹1.79 lakh cr | [Outlook Business](https://www.outlookbusiness.com/economy-and-policy/gst-evasion-worth-7trn-detected-over-last-five-years-whats-behind-this-rising-trend) |
| Taxpayer base | 13.8M+ GSTN users (2024) | [FinBox](https://finbox.in/blog/how-gstn-on-account-aggregator-can-help-msme-lenders) |
| Notice types | DRC-01C (ITC in 3B exceeds 2B), DRC-01, DRC-01B (GSTR-1 vs 3B). Demands for FY2024-25 onward mainly under Section 74A; earlier years 73/74 | [TaxGuru](https://taxguru.in/?p=1075080) |
| Notice breadth (Aug 2026, commentary) | Multi-year notices on turnover, ITC, RCM, exports, refunds, e-way bills | [TaxGuru](https://taxguru.in/?p=1075080) |
| Typical causes | Supplier files GSTR-1 after the 11th (IFF after the 13th), missing e-invoice IRN, Section 17(5) blocked credit, RCM errors | [Tally Solutions](https://tallysolutions.com/gst/gstr-2b-reconciliation-mismatches-how-to-fix/) |

**Inference.** Honest small taxpayers are swept up by enforcement aimed at fake-invoice networks, and each notice goes to a CA case by case with long turnaround.

**Evidence gaps (do not cite as fact).** No official count of 2B-mismatch notices to small taxpayers; no independent data on CA cost per notice; the 5% vs 20% tolerance claim in one article is unverified; Gujarat and Calcutta high courts have been approached over GSTR-2B-based restrictions, so the law is open ([ClearTax News](https://news.cleartax.in/fresh-gst-notices-issued-to-taxpayers-for-significant-itc-mismatches/7312/amp)); honest-but-lost ITC is unquantified, so treat it as a feature only. Week 1-2 CA interviews must close the first two gaps.

## 3 Target users, personas and jobs-to-be-done

| Persona | Jobs-to-be-done | Success looks like |
|---|---|---|
| **CA partner** (buyer; signs and represents) | Keep every client's ITC clean before GSTR-3B; never miss a notice deadline; serve more clients per head; limit liability | Monthly ITC-at-risk view per client; drafts that need review, not rewriting; a defensible audit trail |
| **Article assistant** (daily user) | Download 2B, match to Tally, chase suppliers, compile notice annexures | One work queue; pre-filled supplier messages; one-click evidence pack |
| **SME client** (passive beneficiary) | Keep credit, avoid notices, answer the CA quickly | A short WhatsApp request ("approve nudge to Supplier X"), nothing to learn |

Direct-to-SME selling is avoided: MSME bookkeeping apps lose money (Vyapar lost ₹63 cr in FY25, [Entrackr](https://entrackr.com/fintrackr/vyapar-posts-rs-63-cr-loss-in-fy25-cash-reserve-fades-93-10819211)), while a CA serves dozens to hundreds of clients (inference, [B2B note](research/b2b_fintech_gaps.md)).

## 4 Competitive landscape

**India.** Clear, Zoho and Vayana feature sets were **not surveyed** in the research; test them hands-on in week 1.

| Player | Sourced facts | Gap | Threat |
|---|---|---|---|
| **Suvit** | GSTR-1 and 2A/2B reconciliation, ITC reports, filing; ICAI member-benefits listing at 50% discount; 4K+ CAs per ICAI listing vs 10,000+ per own site (conflicting) ([ICAI](https://bs.icai.org/suvit-2/); [Suvit](https://www.suvit.io/post/accounting-with-ai-for-cas)) | Notice drafting and supplier chasing not confirmed | High: owns channel and price anchor |
| **Accu Reco** | Cloud GST ITC reconciliation on ICAI's programme ([ICAI CMP](https://betacmp.icai.org/?p=1502)) | Reconciliation only (as far as known) | Medium |
| **Tally (TallyIra)** | TallyPrime 7.1 (about 23 June 2026) "Docs by Ira" reads documents, including from WhatsApp, and drafts GST entries ([CXO Digital Pulse](https://www.cxodigitalpulse.com/?p=39293)); TallyPrime 5.0 GST interface claimed to save 60-70% of filing time ([Gulf News](https://gulfnews.com/business/corporate-news/tally-solutions-launches-tallyprime-50-with-seamless-multilingual-experience-1.1726137077611)) | Data entry, not exceptions, multi-client dashboards or notices | High: bundled, owns the books |
| **Clear** | ₹272 cr revenue, ₹96 cr loss in FY25 ([Entrackr](https://entrackr.com/fintrackr/clear-reports-rs-272-crore-revenue-and-rs-96-crore-loss-in-fy25-10808038)); GST notice depth unverified | Unknown | High: brand, bundling |
| **Zoho Books** | Not researched | Unknown | Medium |
| **Tally add-ons** (e.g. [AI Accountant](https://www.aiaccountant.com/blog/ultimate-guide-tally-prime-automation)) | Invoice matching, GST verification | Data-entry layer | Low-medium |

**Open ground (inference).** With AI data entry native to Tally, what remains is exception handling, 2B-versus-books reconciliation, multi-client CA dashboards, notice reading and draft replies, and month-end checklists ([B2B note](research/b2b_fintech_gaps.md)).

**Global analogs.**

| Analog | Evidence | Lesson |
|---|---|---|
| **Basis** | $100M Series B at $1.15B (24 Feb 2026); about 30% of top 25 US firms use it (company) ([BusinessWire](https://www.businesswire.com/news/home/20260224020999/en/Basis-Raises-$100M-at-a-$1.15B-Valuation-as-Accounting-Firms-Adopt-End-to-End-Agents-Across-Accounting,-Tax,-and-Audit)) | Agents for accounting firms attract capital |
| **Black Ore** | 75 firms picked from a waitlist of about 4,000 at launch, 29 Apr 2026 ([Street Insider](https://www.streetinsider.com/Press+Releases/Black+Ore+Launches+Tax+Autopilot+for+Broad+Availability/26390608.html)) | Waitlist plus hand-picked cohort |
| **Juno** | $12M seed; claims 500 firms (company) ([CPA Practice Advisor](https://www.cpapracticeadvisor.com/2026/04/13/juno-raises-12m-seed-to-scale-ai-tax-preparation-platform-that-automates-90-of-busy-work/181502/)) | Small firms are reachable |
| **Integral** (Germany) | EUR 18M Series A, Sept 2026; licensed professionals review and sign off ([Vestbee](https://vestbee.com/insights/articles/integral-lands-18-m)) | Human sign-off is a feature |
| **Intuit UK VAT agent** | Beta, drafts for approval ([Intuit](https://quickbooks.intuit.com/uk/press/intuits-all-in-one-platform-introduces-a-virtual-team-of-ai-agents-to-help)) | Platforms ship agents too |

Winners sell to accounting firms, not SMB owners ([global note](research/global_b2b_ai_fintech.md)). Valuations rest on thin disclosed ARR: evidence of interest, not unit economics.

## 5 Product specification

**MVP scope.**

| In | Out |
|---|---|
| Monthly 2B vs purchase-register reconciliation, regular taxpayers | Portal filing of returns or replies (the CA files) |
| IMS accept/reject/pending recommendations | GSTR-1/3B/9 preparation, refunds, exports |
| Per-supplier action list with ₹ at risk | Appeals and tribunal drafting |
| Supplier chasing by WhatsApp and email | Direct-to-SME app |
| Notice intake (DRC-01C, DRC-01, DRC-01B, ASMT-10), evidence pack, draft reply | Income-tax notices (Section 14) |
| Tally and Excel inputs; portal files or a licensed GST data provider; CA review console and audit log | |

**Flow.** Ingest 2B, IMS and purchase register → match → classify mismatches → action list → CA approves → chase suppliers → pre-3B check → notice intake → evidence pack → cited draft → CA edits, signs and files → outcome joins the golden set.

**Agent workflow.**
1. **Ingest** 2B and IMS (provider API or portal files) and the Tally/Excel register.
2. **Normalise and match** deterministically (exact, tolerance, fuzzy). No model decides a number.
3. **Classify** causes: late supplier filing, not in 2B, value difference, missing IRN, 17(5), RCM, IMS pending.
4. **Action list** per supplier, ranked by ₹ at risk, with a recommended step.
5. **CA approves** in bulk; nothing leaves unapproved.
6. **Chase suppliers** with approved templates; track replies; escalate on a cadence.
7. **Pre-3B check:** ITC claimed versus available in 2B, flagging DRC-01C exposure.
8. **Notice intake:** extract type, section, period, demand, deadline; set reminders.
9. **Evidence pack:** ledgers, invoices, 2B rows, supplier status, payments, numbered annexures.
10. **Draft reply:** retrieve law by effective date, compute figures with tools, cite every legal statement.
11. **CA reviews, signs and files.** 12. **Log** outcome and edits.

**Features.**

| Pri | Feature |
|---|---|
| P0 | Deterministic 2B-vs-books engine; cause classifier; per-supplier action list with ₹ at risk |
| P0 | Tally export and Excel import |
| P0 | Notice intake, field extraction, deadline tracker; evidence pack builder |
| P0 | Cited draft reply; CA review console; append-only audit log |
| P1 | WhatsApp/email supplier chasing with cadences |
| P1 | IMS recommendations; pre-3B dashboard; multi-client CA view |
| P1 | Licensed GST data provider auto-fetch |
| P2 | Client WhatsApp approvals; Hindi and regional-language messages |
| P2 | Notice outcome analytics; direct Tally connector |

## 6 Technical architecture

**Components (suggested; aligned with the report's [build table](research/00-full-research-report.md)).**

| Component | Implementation |
|---|---|
| Intake | Web upload, email forward, WhatsApp Cloud API or a BSP (Gupshup, Interakt); frontier models read PDFs and photos directly |
| Store | Postgres with pgvector (e.g. Supabase): ledgers, 2B snapshots, notices, versioned law corpus |
| Reconciliation | Deterministic Python/SQL; every rupee figure originates here |
| Knowledge base | CGST Act and Rules, notifications, circulars, GSTN advisories, judgments, each with effective date; hybrid retrieval with reranker |
| Reasoning | Mid-tier model for drafting, small model for classification and extraction; **no fine-tuning** |
| Tools | `get_2b`, `match_invoices`, `itc_at_risk`, `supplier_status`, `search_law(query, as_of)`, `build_annexure`, `compute_interest`; read-only or draft-only |
| Controls | Review console, role-based access, audit log, eval harness in CI |

**Data access.**
1. **Portal downloads** uploaded by the CA or client: no licence, slower UX. Start here.
2. **Licensed GST data provider (GSP/ASP)** APIs for auto-fetch of 2B, IMS and supplier status, with taxpayer authorisation.
3. **Tally exports**, later a connector; Zoho and Excel secondary.
4. **Account Aggregator** is not the route for 2B: GSTN joined in Nov 2022 with GSTR-1 and 3B data, aimed at lenders, with sole-proprietor limits ([FinBox](https://finbox.in/blog/how-gstn-on-account-aggregator-can-help-msme-lenders)).

**AI approach.** Retrieval over GST law plus deterministic reconciliation. The 2024-26 evidence favours retrieval and tool calls over fine-tuning because rules change and numbers must be exact ([tech note](research/tech_feasibility.md)). The model may state only tool-computed figures or cited provisions. Fine-tune later, if at all, only the embedder or a narrow classifier.

**Evaluation plan.**
- Reconciliation set: about 200 CA-labelled cases (assumed size); exact match on ₹ at risk.
- Notice extraction set: about 100 notices; near-100% on deadline and demand.
- Draft set: citation precision at least 95% (the report's bar for its claim-recovery product), CA acceptance rate, time saved.
- Safety set: out-of-scope and adversarial inputs must escalate.
- Design references: Taxmann.AI and IIT Kharagpur LE-BTL on Indian tax and GST law ([Taxmann](https://www.taxmann.com/post/blog/taxmann-ai-x-iit-kharagpur-llm-evaluation-le-btl-benchmark-study)).
- Run all sets in CI on every prompt, model or corpus change. Pilot users judge usefulness; only the golden set judges correctness.

**Security and privacy.** Tenant isolation per firm and client; encryption in transit and at rest; no storage of portal passwords (the taxpayer or CA handles OTPs); notices and supplier replies treated as untrusted input; consent, retention and deletion flows ahead of DPDP duties phasing in through about May 2027 ([Deccan Herald](https://www.deccanherald.com/india/centre-notifies-dpdp-rules-implementation-planned-in-phases-spread-over-12-18-months-3798465)); no vendor training on customer data (assumption; confirm per vendor).

**Audit logs.** Append-only record of inputs, retrieved sources, tool calls, outputs, model and prompt versions, every human edit and approval, and every outbound message. Retention period to be set with counsel (not in the sources).

## 7 Regulatory and legal

**Data routes (unverified background knowledge; confirm with counsel and GSTN documentation).**
- **A (recommended):** integrate through an existing GSP/ASP with taxpayer authorisation.
- **B:** manual portal files; no GSP dependency.
- **C (not for MVP):** become a GSP/ASP; adds licensing and audit overhead.

**Who signs and represents.** Only authorised professionals (CAs, lawyers) can represent a taxpayer before tax authorities, so the agent drafts and a human files (background knowledge per the research notes, unverified). Product rules: the CA files every reply; the product never sends anything to an authority in the MVP; contracts state that the software is a drafting tool and the CA keeps professional responsibility.

**Data handling.** The CA firm is likely the data fiduciary and the company a processor (assumption, confirm under DPDP). Sign a processing agreement per firm; log client consent for supplier messaging.

**Compliance checklist.**
- [ ] Counsel opinion on drafting versus representation, and on liability caps
- [ ] GSP/ASP agreement and taxpayer-authorisation flow reviewed
- [ ] Processing agreement, privacy notice, consent and deletion flows
- [ ] WhatsApp template approvals and supplier opt-out handling
- [ ] Terms of service with a CA-responsibility clause; indemnity position
- [ ] Private limited company; GST registration once required ([report 10.7](research/00-full-research-report.md))
- [ ] Law-database licensing: use official texts freely, license commercial databases, do not scrape them

## 8 Business model

All numbers are **assumptions** for pilot testing.

**Pricing hypotheses.** ₹250 per GSTIN per month (20-GSTIN minimum) for reconciliation, action lists and chasing; ₹2,500 per notice for evidence pack plus first draft. Suvit's 50% ICAI discount is a price anchor; model 50% as the downside.

**Unit economics, one typical firm.**

| Line | Arithmetic | Result |
|---|---|---|
| Subscription | 40 GSTINs × ₹250 | ₹10,000 / month |
| Notice revenue | 40 × 0.2 notices per year = 8 a year = 0.67 a month × ₹2,500 | ₹1,667 / month |
| **Revenue** | | **₹11,667 / month (₹1.40 lakh / year)** |
| Variable cost per GSTIN-month | LLM ₹10 + WhatsApp 10 × ₹1 + data fee ₹15 + support ₹15 | ₹50, so ₹2,000 |
| Cost per notice | 200k input tokens × $3/M + 20k output × $15/M = $0.90 ≈ ₹81 at ₹90/$, plus ₹150 review | ≈ ₹230, so ₹153 / month |
| **Contribution** | 11,667 − 2,000 − 153 | **≈ ₹9,500 / month (81%)** |
| CAC and payback | ₹15,000 ÷ ₹9,500 | ≈ 1.6 months |
| Lifetime | 3% monthly churn → 33 months × ₹9,500 | ≈ ₹3.1 lakh, about 21x CAC |

Token prices (Sonnet-class) come from third-party aggregators in the [tech note](research/tech_feasibility.md) and need verification; the exchange rate, token counts, data fee, WhatsApp cost, CAC and churn are estimates.

**Scale arithmetic.** 100 firms × ₹1.40 lakh ≈ ₹1.4 cr a year. 2% of 98,967 firms ≈ 1,979 firms ≈ ₹27.7 cr. A ₹100 cr ceiling needs about 7,140 firms (7.2%). Break-even on an assumed ₹6 lakh monthly team cost is about 63 firms.

**Downside.** At ₹125 per GSTIN, contribution falls to about ₹4,500 a month and payback lengthens to about 3.3 months. No price data exists for this segment, so a price test is a day-30 gate.

## 9 Go-to-market

**Principle.** Sell the outcome manually first, charge from the first case, and automate only steps done at least 20 times ([report 10.1](research/00-full-research-report.md)).

1. **ICAI member-benefits portal.** Suvit is listed at a 50% discount ([ICAI](https://bs.icai.org/suvit-2/)) and Accu Reco is also listed ([ICAI CMP](https://betacmp.icai.org/?p=1502)), proving the channel accepts third-party GST tools. Listing criteria and fees are not in the sources. Apply around day 45 with named references.
2. **CA communities** (assumed channels): ICAI branch and study-circle events, WhatsApp, Telegram and LinkedIn CA groups, GST-practitioner forums. Lead with anonymised before-and-after notice cases and a monthly "ITC at risk" benchmark.
3. **Waitlist and cohort launch,** copying Black Ore.
4. **Referral:** a free month for each referred firm.

**First 100 firms.**

| Stage | Target | How |
|---|---|---|
| 0-10 | Day 30 | Warm introductions; free shadow mode on real data, then paid |
| 10-30 | Day 90 | Concierge service, referrals, weekly office hours |
| 30-100 | Months 4-9 | ICAI listing, webinars timed to notice and return seasons, GSP and Tally-consultant partners |

Funnel (assumed rates): 100 firms ÷ 30% pilot-to-paid ≈ 333 pilots; ÷ 50% demo-to-pilot ≈ 667 demos; ÷ 20% outreach-to-demo ≈ 3,300 contacts over 9 months, about 370 a month.

## 10 90-day execution plan

| Phase | Days | Deliverables | Gate |
|---|---|---|---|
| 0. Discovery | 1-14 | 20 CA interviews; teardown of Suvit, Clear, Zoho, Tally, Accu Reco; notice-volume and time-per-notice baseline; GSP/ASP shortlist; counsel brief | At least 8 of 20 CAs confirm a paid pain; GSP route chosen |
| 1. Concierge and recon core | 15-45 | Manual service for 5-10 design partners; engine on uploads; action lists; law corpus v1; 100 golden items | Recon accuracy at least 98%; 5 firms weekly active; 3 agree to pay |
| 2. Notice desk alpha | 46-75 | Notice intake; evidence pack; cited drafts; review console; audit log; WhatsApp chasing | Citation precision at least 95%; at least 60% drafts accepted; no missed deadlines |
| 3. Paid pilot and decision | 76-90 | Price test; 15 firms active; ICAI application; case studies | Section 1 targets met, or pivot per Section 11 |

**Checklist.**
- [ ] Interview 20 CA firms; record notices per client and CA time per notice
- [ ] Hands-on teardown of five competitors
- [ ] Engage counsel; brief on representation, liability, DPDP
- [ ] Select a GSP/ASP and test sandbox access to 2B and IMS
- [ ] Build matching engine and first 100 golden items
- [ ] Collect 50 consented sample notices by day 45
- [ ] Ingest law corpus with effective dates
- [ ] Build review console and audit log
- [ ] Register WhatsApp templates
- [ ] Test prices at ₹150, ₹250, ₹400 per GSTIN
- [ ] Submit ICAI listing application
- [ ] Run day-90 metrics review

**Roles.** Product and GTM lead; full-stack engineer; applied-AI engineer (engine, retrieval, evaluation); part-time CA advisor (labels golden sets, reviews drafts, opens the community); external counsel.

## 11 Success metrics and kill/pivot criteria

Thresholds are assumptions; confirm at day 14.

| Metric | Day-90 target | Kill or pivot trigger |
|---|---|---|
| Paying firms | At least 8 of 15 active | Fewer than 3 paying → reposition or stop |
| Price accepted | At least ₹150 per GSTIN | Only below ₹75 → notice-only fee model |
| Recon accuracy | At least 99% | Below 95% after fixes → freeze features |
| Citation precision | At least 95% | Below 90% by day 75 → extraction and evidence only, no drafting |
| CA draft acceptance | At least 70% | Below 40% → reposition as evidence builder |
| Time to CA-ready draft | Under 30 minutes | No gain over baseline |
| Weekly use | 3 of 4 weeks per firm | Usage lapses after pilot |
| Supplier chase resolution | At least 30% within 30 days | Below 10% → de-scope chasing |
| Incidents | None | Missed deadline or data leak → pause |
| Competitor | n/a | Tally or Clear ships notice drafting and CA dashboards free → niche down or move to income-tax notices |

## 12 Risks and mitigations

| Risk | Likelihood / impact | Mitigation |
|---|---|---|
| **Tally or Clear bundling** (TallyIra shipped June 2026) | High / High | Own the action and notice layer and multi-client workflow; stay Tally-compatible, not dependent; own evidence and audit trail; move fast |
| Suvit price anchor and channel hold | High / Medium | Differentiate on outcomes; early price tests; notice-only plan |
| Wrong citation or advice harms a client | Medium / High | Retrieval with citations, deterministic numbers, mandatory CA review, CI evaluation, indemnity position |
| GSP/ASP cost or dependency | Medium / Medium | Portal-upload path first; abstraction over providers |
| Representation or unauthorised-practice concern | Low-medium / High | Draft-only, CA files, counsel opinion pre-launch |
| CA inertia and trust | Medium / High | Concierge onboarding, shadow mode, CA advisor, visible audit logs |
| Seasonal demand | High / Medium | Lead with monthly reconciliation habit; sell during notice season |
| WhatsApp policy limits | Medium / Medium | Email fallback; opt-in logs; approved templates |
| Data breach or DPDP failure | Low / High | Encryption, isolation, processing agreements, deletion flow, security review |
| Rule and portal changes | High / Medium | Versioned corpus; change monitor; regression suite |
| Unproven demand (no official notice counts) | Medium / Medium | Measure in discovery; gate on pilot data |

## 13 Open questions and decisions needed

**Decisions.**
1. Which GSP/ASP, and the per-fetch budget.
2. Pricing structure: per GSTIN, firm tiers or notice-only.
3. Design-partner depth versus breadth for day 90.
4. CA advisor appointment and compensation.
5. Entity set-up and professional-indemnity cover.

**Open questions.**
- What does the ICAI listing require (criteria, discount, fee, timeline)?
- What notice volume and fee per notice are typical? (No official or independent data.)
- Do Clear, Zoho or Suvit already draft notice replies? (Not surveyed.)
- Which tolerance and section rules govern DRC-01C by period, and how does the corpus track them?
- Who bears liability if a CA relies on a flawed draft, and should contracts cap it?
- What audit-log retention applies?
- Does supplier chasing on a client's behalf need extra consent?
- How will court rulings on GSTR-2B-based restrictions change advice?

## 14 Expansion path

1. **GST depth:** annual-return reconciliation, refunds and e-way bill notices, then appeal drafting once accuracy is proven.
2. **Income-tax notices:** over 7 crore ITRs were filed for AY2025-26 ([IANS](https://ianslive.in/more-than-7-crore-itrs-filed-so-far-income-tax-department--20250915180800)) and automated mismatch notices are rising ([Outlook Money](https://www.outlookmoney.com/tax/why-2025-tax-notices-are-rising-and-what-taxpayers-must-do-now)). Same CA channel and engine: parse the notice (143(1), 139(9), 133(6), 148A), reconcile to AIS/26AS, draft the reply. Do not lead with filing, which is commoditised. E-return intermediary registration for API filing is unverified.
3. **TDS:** TDS credit mismatches and notices are a natural adjacency (hypothesis; not researched).
4. **MSME receivables:** the report says this idea needs the CA channel (Profile 2), and 43B(h) gives a reason to chase buyers.
5. **Other VAT and e-invoicing markets (hypothesis):** the pattern of selling reconciliation and notice agents to accountants may transfer. Signals: Intuit's UK VAT agent in beta; early AI-accounting rounds of $10M or less in Brazil and Colombia beside well-funded incumbents such as Omie ($150M) ([Techleap](https://finder.techleap.nl/news/feed/omie-secures-150m-in-series-d-funding)); Integral in Germany. Country-level regulation is not researched.

## 15 Sources

Repository: `reports/India AI personal finance MVP.md` (Sections 7, 8 Profile 3, 10); `research_notes/India AI personal finance MVP/` files `unsolved_smb_payments.md`, `b2b_fintech_gaps.md`, `global_b2b_ai_fintech.md`, `household_finance_gaps.md`, `tech_feasibility.md`, `ai_fintech_funding_table.md`.

External (all linked inline above): Jurishour; CAalley; Outlook Business; TaxGuru; Tally Solutions; ClearTax News; FinBox; TaxConcept; ICAI benefits portal (Suvit, Accu Reco); Suvit; CXO Digital Pulse; Gulf News; AI Accountant; Entrackr (Clear, Vyapar); BusinessWire (Basis); Street Insider (Black Ore); CPA Practice Advisor (Juno); Vestbee (Integral); Intuit UK; Techleap (Omie); Taxmann (LE-BTL); Deccan Herald (DPDP); IANS; Outlook Money.

Source quality: most figures rest on secondary reporting and vendor claims, as the report's methodology notes. GSP/ASP mechanics and representation rules are background knowledge that counsel must confirm.
