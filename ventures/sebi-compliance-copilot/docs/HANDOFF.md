# Handoff: Compliance Copilot for SEBI Intermediaries

*Project 4 of the India AI personal-finance research (rank #4 of 14, weighted score 3.65/5). Prepared 8 Oct 2026; research cut-off 7 Oct 2026. Facts come from the sources in section 15. Items tagged **[Assumption]**, **[Inference]** or **[Unconfirmed]** are not sourced facts.*

## 1. TL;DR

- **What.** An AI tool that checks every social post, WhatsApp broadcast, web page and email from a SEBI-regulated intermediary against SEBI's Common Advertisement Code (CAC), prepares the 24-hour post-publication report, archives tamper-evident evidence, and generates AI-use disclosures, suitability rationales and advice audit trails. A CSCRF (cybersecurity framework) compliance kit is the second module.
- **For whom.** Registered investment advisers (RIAs, about 1,000), research analysts (RAs, about 1,500), PMS managers (515-530+), brokers, and the roughly 3,350 "top" mutual-fund distributors (MFDs).
- **Why now.** SEBI's board approved the CAC on 24 Sept 2026. Most ads move from prior approval to reporting within 24 hours, turning compliance into a logging and evidence problem ([exchange4media](https://www.exchange4media.com/marketing-news/sebi-relaxes-advertising-norms-keeps-celebrity-endorsements-under-prior-approval-158597.html)). Notified text and effective date: **[Unconfirmed]**.
- **Core bet.** Small regulated firms will pay ₹20-50k a year for a tool that makes each post provably compliant at issue, reported on time and defensible later. No Indian specialist vendor was found (absence in search, not proof).
- **90-day success.** The CAC rules corpus is live and versioned; at least 5 design-partner firms use the tool weekly; at least 10 firms pay; precision and recall gates in section 11 are met on a labelled set; and the team has decided, on evidence, whether to scale or pivot.

This is a **small-market, high-feasibility** project; the research recommends it as a second product or cash-generating side line (Profile 4).

## 2. Problem and evidence

Advertising, AI-disclosure and record-keeping duties are pushing advisers out. The Ken attributes the RIA decline to compliance burden: advisers needed permission, and payment to a supervisory body, before running ads or messaging clients ([The Ken](https://the-ken.com/sebi-registered-advisors-are-an-endangered-species-so-who-guides-retail-investors/)). On 16 March 2026 the SEBI Chair voiced concern about the falling RIA count ([News On AIR](https://www.newsonair.gov.in/sebi-expresses-concern-over-decline-in-number-of-registered-investment-advisers/)).

**Regulatory timeline**

| Date | Event | Source |
|---|---|---|
| Aug 2024 | CSCRF issued; deadlines later extended to 30 Jun 2025 for most entities (brokers, AMCs, PMS, IAs) | [Zeron](https://zeron.one/sebi-grants-deadline-extension-for-cscrf-compliance-heres-what-you-need-to-know/) |
| 8 Jan 2025 | IA/RA circulars: AI-use disclosure to clients; IA annual audit | [FoxMandal](https://foxmandal.in/news/ras-and-ias-to-take-on-additional-responsibilities/), [Taxguru](https://taxguru.in/sebi/sebi-updates-guidelines-investment-advisers-2025.html) |
| 29 Jan 2025 | Finfluencer circular: "education" content may use only price data at least 3 months old | [Business Standard](https://www.business-standard.com/markets/news/sebi-finfluencer-circular-live-stock-data-market-education-rules-125013000571_1.html) |
| 10 Feb 2025 | Any regulated entity using AI is solely responsible for its outputs, in-house or procured | [Fox Mandal](https://foxmandal.in/News/regulated-entities-responsible-for-output-of-ai-usage-sebi/) |
| 23 Jun 2026 | CAC consultation covering brokers, DPs, IAs, RAs, online bond platforms, PMS, MFs/AMCs | [Mondaq](https://www.mondaq.com/india/fund-management-reits/1826178/sebis-proposal-for-a-common-advertisement-code-financial-advertisements-under-the-regulatory-lens) |
| 19 Aug 2026 | SEBI says tiered AI rules (human oversight, kill switch) will come "shortly"; no final circular found | [ANI](https://aninews.in/news/business/sebi-to-soon-issue-aiml-guidelines-for-capital-markets-mandate-human-oversight-kill-switch-controls-chairman-pandey20260819121850/) |
| 24 Sept 2026 | Board approves CAC (215th meeting); celebrity endorsements keep pre-clearance | [IndianTelevision](https://indiantelevision.com/regulators/sebi-approves-common-advertising-code-allows-celebrity-promotion-by-regulated-entities/) |
| 30 Nov 2026 | CSCRF action-taken/revalidation report due for self-certification, small, mid-size and qualified REs (circular number not fully verified) | [NSE circular](https://nsearchives.nseindia.com/content/circulars/INSP74185.pdf) |
| About H1 2027 | End of a six-month transition, if notified soon **[Inference]** | Mondaq, above |
| About May 2027 | DPDP Act fiduciary duties bind | [Deccan Herald](https://www.deccanherald.com/india/centre-notifies-dpdp-rules-implementation-planned-in-phases-spread-over-12-18-months-3798465) |

Under the CAC, a firm must show every ad was correctly classified, compliant when issued, reported on time and supportable later (Mondaq, above). The draft defines "celebrity" to include finfluencers with more than 500,000 followers, OTT/reality-TV names and AI avatars ([StartupTalky](https://startuptalky.com/sebi-wants-one-ad-code-celebrities-back-finfluencers-on-hook/)). Research reports are not ads unless they promote the RA's own products ([Storyboard18](https://www.storyboard18.com/advertising/research-reports-are-not-ads-clarifies-sebi-46112.htm)). SEBI itself uses AI to monitor social-media advice and review ads ("Project Sudarsan", "SEBI R(AI)DAR") ([Business Today](https://www.businesstoday.in/markets/stocks/story/sebi-annual-report-ai-tools-deployed-to-track-finfluencers-misleading-investors-547810-2026-08-07)).

**Buyer counts (counts conflict; treat as ranges)**

| Segment | Count | Source and caveat |
|---|---|---|
| RIAs | About 941 (Mar 2025); 1,044 (Jun 2026, unverified blog) | [The Ken](https://the-ken.com/sebi-registered-advisors-are-an-endangered-species-so-who-guides-retail-investors/) |
| RAs | 1,584 (Jun 2025), net of 2026 cancellations (29 cancelled Jul-Aug 2026 for unpaid fees) | [Business Standard](https://www.business-standard.com/amp/markets/news/research-analysts-a-fraction-of-the-number-of-brokers-says-sebi-data-119031100045_1.html), [Moneylife](https://www.moneylife.in/article/17-research-analysts-registration-cancelled-by-sebi-for-nonpayment-of-renewal-fees/81261.html) |
| PMS managers | 515 (May 2026); "more than 530" (30 Sept 2026) | [Moneylife](https://www.moneylife.in/article/sebi-unveils-sweeping-reforms-for-portfolio-managers-proposes-overseas-investing-simplified-regulations-and-new-mfpms-framework/81148.html), [NewKerala](https://www.newkerala.com/news/a/pms-regulation-must-evolve-industry-sebi-cut-compliance-779.htm) |
| Top MFDs | More than 3,350 (FY26); 3.53 lakh valid ARN/EUIN holders in total | [Cafemutual](https://cafemutual.com/news/industry/38760-top-mfds-count-rises-to-over-3350-in-fy-2026) |
| Brokers, APs, CSCRF categories | Not researched; **buyer count unknown** | - |
| US RIA firms | 16,544 (2025) | [ThinkAdvisor](https://www.thinkadvisor.com/2026/06/03/number-of-rias-sets-new-record-report/) |

## 3. Target users, personas and jobs-to-be-done

| Persona | Context | Jobs-to-be-done | Likely willingness to pay (**[Inference]**) |
|---|---|---|---|
| Solo RIA | 1-2 people; posts on LinkedIn/Instagram/X; WhatsApp broadcasts | Know before posting whether it is an ad and breaches the code; produce records on request; generate AI-use disclosure and suitability rationale | Moderate; compliance is existential, but the pool is small |
| Research analyst (RA) | Publishes calls and reports; many cash-strapped | Separate research reports (not ads) from promotion; required and AI-use disclosures | Low-moderate |
| PMS compliance officer | Owns performance claims and factsheets; SEBI Chair urged curbs on exaggerated claims ([Cafemutual](https://cafemutual.com/news/cafe-alt/35482-pms-industry-must-curb-exaggerated-performance-claims-sebi-chairman)) | Pre-clear material, evidence every ad, file on time, audit packs | High (₹1-10 lakh a year plausible) |
| Broker compliance team | Many branches/APs and agencies; celebrity endorsements need pre-clearance | Central ad register, celebrity flag, 24-hour filing queue, CSCRF evidence | Moderate, deadline-driven |
| Top MFD | Posts constantly, WhatsApp-heavy; free AI from AssetPlus, Wealthy, ZFunds, Prudent competes | Platform-agnostic check on client communications; archive | Low-moderate (₹10-50k a year plausible for the top tier) |

## 4. Competitive landscape

| Player | Region | What it does | Relevance and gap |
|---|---|---|---|
| Smarsh | US/global | Archive and surveillance; AI Assistant for smaller firms (Mar 2025) ([Smarsh](https://www.smarsh.com/press-release/smarsh-redefines-industry-standards-with-new-compliance-ai-for-small-and-medium-sized-firms)) | Closest analog; built for SEC/FINRA, not SEBI |
| Red Oak | US | Marketing review for FINRA firms with an AI Review module; 2026 combination with MirrorWeb ([summary](https://yespress.io/red-oak.md)). Global Relay (archiving; no primary AI source found) is a further analog | Analog for pre-publication review |
| Jump, Zocks | US | AI notetakers (about $1,200-1,440 per advisor a year); no ad compliance | Show per-seat willingness to pay; adjacent to audit trail |
| CSCRF service firms (Ogma, Qualysec, SecurityHQ, CyberSigma, Zeron) | India | VAPT and audit services ([Ogma](https://ogma.in/blog/sebi-cscrf-compliance-vapt-and-cyber-audit-requirements-for-brokers-exchanges-and-mutual-funds)) | Service-led; no self-serve kit found |
| OnFinance AI | India | Markets "BFSI AI agents for SEBI & RBI"; promotional, unverified | Watch; could move into ad review |
| MFD platforms (AssetPlus, Wealthy, ZFunds ZIVA, Prudent) | India | Free, commission-funded tools adding AI | Could bundle compliance checks; paid tools compete with free |
| Manual process (consultants, spreadsheets, pre-approval) | India | Status quo | The real competitor |

No dominant Indian AI vendor for this was found; verify in the first 20 interviews.

## 5. Product specification

**MVP scope**

| In | Out |
|---|---|
| Ad / not-ad and celebrity classification, rule check against the CAC and related circulars, with cited clauses | Posting content on the firm's behalf |
| Draft check (before publishing) and as-published capture (after) | Investment recommendations to end investors |
| 24-hour report pack plus filing tracker | Full surveillance of all staff communications |
| Evidence archive and audit log | KYC/AML (crowded: Perfios, IDfy, Signzy) |
| AI-use disclosure generator; suitability rationale drafts; advice audit trail (basic) | Call recording infrastructure (import transcripts first) |
| CSCRF-lite kit: policy templates, asset inventory, deadline reminders | VAPT itself (needs a CERT-In auditor) |

**End-to-end flow**

1. The firm connects channels (forward-to email, WhatsApp number, URL list, paste).
2. The tool ingests the item and records a hash and timestamp.
3. It classifies: advertisement or not; celebrity or not; entity type; channel.
4. It retrieves the applicable rules and runs deterministic, then model-judged checks, each with a cited clause.
5. It returns a verdict, suggested fix and confidence. Low-confidence or high-severity items go to a human reviewer.
6. The firm publishes (the tool never posts); the tool captures the as-published version.
7. It prepares the 24-hour report pack and tracks submission.
8. It archives everything with an append-only audit log; registers and audit exports are on demand.

**Agent workflow (human in the loop).** Five agents: ingest, classifier, rule-check, drafting (fixes, disclosures, rationales) and report-pack. A named human approves any filing or regulator-facing document; every step is logged. This matches SEBI's stated direction on human oversight and kill switches.

**Feature list**

| # | Feature | Priority |
|---|---|---|
| 1 | Ad/not-ad classification and celebrity flag | P0 |
| 2 | Rule check with cited clauses and suggested fixes | P0 |
| 3 | Intake: web paste, email forward, WhatsApp number | P0 |
| 4 | Evidence archive (hash, timestamp, snapshot) and audit log | P0 |
| 5 | Human review console and approvals | P0 |
| 6 | 24-hour report pack and deadline tracker | P0 |
| 7 | AI-use disclosure generator (agreement, website, report footers) | P1 |
| 8 | Suitability rationale draft (RIA approves) | P1 |
| 9 | Monthly ad register; annual-audit export | P1 |
| 10 | CSCRF-lite kit: templates, inventory, reminders (30 Nov 2026) | P1 |
| 11 | Website monitoring and profile capture | P1 |
| 12 | Advice audit trail from imported transcripts | P2 |
| 13 | Branch/AP hierarchy; broker admin roles | P2 |
| 14 | Registration verification; platform API | P2 |

## 6. Technical architecture

**Components and stack** (reuses the report's suggested stack, Table 15)

| Component | Implementation |
|---|---|
| Intake | WhatsApp Cloud API or an Indian BSP (Gupshup, Interakt); email forwarding; web app |
| Store | Postgres with pgvector (for example Supabase); object storage with write-once retention |
| Rules corpus | Versioned, structured rule records (see below) |
| Reasoning | Retrieval over the corpus, then a deterministic rule engine; a mid-tier model for judged checks and drafting; a small model for classification. **No fine-tuning** |
| Audit | Append-only, hash-chained log; India-region hosting (**[Assumption]**) |

**Inputs.** Social posts (paste, URL or user-authorised API; platform terms on scraping **[Unconfirmed]**), WhatsApp broadcasts (drafts forwarded before sending, or exported after), websites (sitemap crawl, change detection) and emails (forward-to address).

**Rules corpus.** Sources: the CAC (draft, then notified text), finfluencer circulars (Aug 2024, Oct 2024, Jan 2025), IA/RA circulars of 8 Jan 2025, the IA master circular of 17 Feb 2026, the Feb 2025 AI-liability amendments, and CSCRF circulars with the 30 Apr 2025 clarification. Each rule record holds id, citation, trigger, check type (deterministic, model-judged or human), severity, effective date and status; draft rules display as "advisory, pending notification".

**AI approach.** Deterministic checks first (disclaimers, registration number, banned phrases, follower threshold, 24-hour clock). The model judges only what rules cannot (implied guarantees, performance claims, advice versus education) and must quote the clause it applies. Figures come from code.

**Evaluation plan.** Build a labelled set of at least 500 items **[Assumption]** from public posts, synthetic variants and consented design-partner archives. Two compliance professionals label each item; a third adjudicates. Report precision and recall per rule class and for ad/not-ad and celebrity classification. Targets (**[Assumption]**): high-severity violation recall at least 95%; precision at least 85% to limit alert fatigue; clause-citation precision at least 95% (the same gate the report sets for Profile 1); ad/not-ad F1 at least 0.90. Re-run on every rules or model change.

**Evidence archive and audit logs.** Per item: original content, as-published capture (HTML or screenshot), SHA-256 hash, UTC timestamp, rule-pack version, verdict, reviewer, edits and filing receipt, stored write-once. The retention period must be confirmed from the notified text and IA/RA record-keeping rules (**[Unconfirmed]**).

**Security.** Role-based access, per-firm encryption keys, MFA, zero-retention model terms, prompt-injection filtering of ingested content and a documented incident process. Plan an external penetration test before wide sales (customers will run vendor-risk reviews) and SOC 2 or ISO 27001 later (**[Assumption]**).

## 7. Regulatory and legal

- **Licence.** The product needs no SEBI licence (Profile 4) because it does not advise investors, execute trades or hold client money. Keep it that way: suitability drafts support an RIA's own decision; the tool never selects securities.
- **Liability positioning.** The regulated entity stays solely responsible for AI outputs (Feb 2025 rule). Position it as decision support with evidence of due diligence, never a guarantee of compliance. Terms should cap liability, require human sign-off and disclaim legal advice; consider professional-indemnity and cyber insurance.
- **Data handling.** The firm is the data fiduciary and the team its processor. IT Act rules apply now; DPDP duties bind around May 2027, with penalties up to ₹250 crore ([Uniqus](https://uniqus.com/digital-personal-data-protection-act-timelines/)). Minimise personal data and avoid storing client PAN or holdings unless a feature needs it. Sending data to a foreign LLM API is cross-border processing; CSCRF localisation for small RIAs was not researched.

**Compliance checklist**

- [ ] Commission a legal opinion on the "no licence" position and suitability drafting
- [ ] Draft terms of service, DPA and liability cap, reviewed by counsel
- [ ] Confirm record-retention and data-localisation rules
- [ ] Build consent, retention and deletion flows to DPDP standard
- [ ] Choose zero-retention model vendors; document sub-processors; disclose that AI assists and a human decides
- [ ] Complete an external penetration test before customer data scales

## 8. Business model

**Pricing tiers (per firm, per year; all prices are [Assumption] anchored to ₹20-50k in the research, Investwell's ₹25k base, Tijori enterprise up to ₹5k a month, VAPT at ₹30k-2 lakh)**

| Tier | Target | Price | Includes |
|---|---|---|---|
| Solo | Solo RIA/RA, 1 user, about 100 items a month | ₹20,000 | Check, archive, 24-hour pack, AI disclosure |
| Firm | Small firms and top MFDs, up to 5 users, about 400 items a month | ₹50,000 | Adds suitability drafts, register, audit export |
| Enterprise | PMS, brokers, large firms, about 2,000 items a month | ₹1.5 lakh and up (custom, to about ₹3 lakh) | Adds hierarchy, API, SSO, priority support |
| CSCRF kit add-on | Any | ₹25,000-75,000 | Templates, inventory, committee pack, reminders |

**Unit economics (illustrative; every input is an [Assumption] to be replaced by pilot data)**

- Mix of 100 firms: 60 Solo, 30 Firm, 10 Enterprise at ₹1.5 lakh.
- ARR = 60 × ₹20,000 + 30 × ₹50,000 + 10 × ₹1,50,000 = ₹12 + ₹15 + ₹15 lakh = **₹42 lakh**, or ₹42,000 per firm. If 20 firms add the kit at ₹40,000, ARR is ₹50 lakh. (The research's cruder case: 100 firms × ₹25,000 = ₹25 lakh.)
- Volume: (60 × 100 + 30 × 400 + 10 × 2,000) / 100 = 380 items a month per firm.
- Annual cost per firm: model at ₹2 per item × 380 × 12 = ₹9,120; hosting, storage and messaging ₹3,000; payment fees (2%) ₹840; total about **₹13,000**.
- Gross profit about ₹29,000 per firm: **69% margin**.
- CAC: ₹10,000 blended plus ₹3,000 onboarding (6 hours at ₹500). Payback = ₹13,000 / (₹29,000 / 12) = about **5.4 months**.
- LTV capped at 3 years: ₹29,000 × 3 = about ₹87,000; LTV:CAC about 6.7.
- Break-even: a 3-person team at ₹5 lakh a month (₹60 lakh a year) needs ₹60 lakh / ₹29,000 = **about 207 firms**, which is why the research treats this as a side line.

**Market ceiling (theoretical, 100% penetration; [Assumption] prices)**

| Segment | Count × price | Annual |
|---|---|---|
| RIAs + RAs | 2,500 × ₹30,000 (the research's own estimate) | ₹7.5 crore |
| PMS | 530 × ₹1.5 lakh | about ₹8 crore |
| Top MFDs | 3,350 × ₹20,000 | about ₹6.7 crore |
| Brokers | Count unknown | Not sized |
| **Total** | | **about ₹22 crore** |

At 15% penetration the India ceiling is about ₹3.3 crore a year **[Assumption]**, not venture scale alone. US RIAs (16,544 firms) at an assumed $1,200 a year (the notetaker price band) give about $20 million theoretical, against entrenched vendors.

## 9. Go-to-market

- **Associations and supervisory bodies.** APMI for PMS (it publishes CSCRF clarifications, [APMI](https://apmiindia.org/storagebox/images/Circulars/Clarifications%20on%20CSCRF%20for%20SEBI%20Regulated%20Entities%20-%2030th%20April'25.pdf)); AMFI for MFDs; RIA/RA associations (not identified in the research). Offer a free CAC-readiness webinar.
- **Compliance consultants.** Consultancies already serve RIAs/RAs. Offer a referral fee (about 20% of year-one fees, **[Assumption]**) and a white-label dashboard.
- **SEBI-registered communities.** Cafemutual, LinkedIn, and WhatsApp/Telegram adviser groups. Lead magnet: a free "is this post an ad?" checker, which also builds the labelled set (with consent).

**First-50-customers plan** (targets are **[Assumption]**)

| Source | Customers | How |
|---|---|---|
| Design partners | 5 | Outreach and consultants; free 90 days, then 50% discount |
| Consultant partners | 18 | 8 consultants, 2-3 firms each |
| Association webinars | 12 | 3 webinars, about 100 registrants each, 4% convert |
| Communities and content | 10 | Free checker, LinkedIn, Cafemutual |
| PMS and broker direct | 5 | Compliance officers, 1-3 month cycles |
| **Total** | **50** | Target by about month 6-9, depending on notification date |

## 10. 90-day execution plan

Day 1 is about 12 Oct 2026; day 90 about 10 Jan 2027.

| Phase | Weeks | Deliverables | Gate |
|---|---|---|---|
| 0. Discover | 1-2 | 20 interviews; locate notified CAC text (or confirm not yet notified); legal opinion commissioned; rules corpus v0; concierge checks for 3 firms | 3 design partners signed; 20 interviews done |
| 1. Core build | 3-6 | Intake, classifier, rule engine v1, archive, review console; labelled set of 300+; CSCRF deadline calendar and template (before 30 Nov) | Classification F1 at least 0.85 on the labelled set; 5 firms onboarded |
| 2. Pilot | 7-10 | 24-hour report pack; AI-disclosure generator; suitability drafts; register; 100+ real items processed; pricing tests | Section 11 quality gates met; at least 5 firms using weekly |
| 3. Convert | 11-13 | Penetration test; case studies; consultant programme live; paid conversion | At least 10 paying; scale-or-pivot decision |

**Checklist**

- [ ] Find the notified CAC circular on sebi.gov.in; log effective date and reporting channel
- [ ] Interview 20 compliance owners (RIA, RA, PMS, broker, MFD)
- [ ] Sign 5 design partners with data-use consent
- [ ] Build the rule schema and load v0 rules with sources
- [ ] Label 300, then 500, items with two reviewers plus adjudication
- [ ] Ship intake (web, email, WhatsApp), review console, evidence archive and 24-hour report pack
- [ ] Publish the CSCRF calendar and template before 30 Nov 2026
- [ ] Test prices at ₹20k, ₹35k and ₹50k
- [ ] Commission the penetration test; sign 3 consultant partners

**Team roles (3 FTE plus contractors, [Assumption])**

- Product and compliance lead: rules corpus, interviews, labelling standards (ideally with a former RIA/PMS compliance officer on retainer).
- AI/backend engineer: pipeline, rule engine, evaluation harness, archive.
- Full-stack and GTM lead: console, onboarding, partnerships and webinars.
- Contractors: securities lawyer, two labellers, security tester.

## 11. Success metrics and kill/pivot criteria

| Metric | Day-90 target | Kill or pivot trigger |
|---|---|---|
| Design partners using weekly | At least 5 | Fewer than 3 after 40 qualified conversations: stop or fold into a feature |
| Paying firms | At least 10 | Fewer than 3 by day 90: pivot to the audit-trail / CSCRF kit or pause |
| Median price accepted | At least ₹20,000 a year | Below ₹12,000: bundle with CSCRF or sell to platforms |
| High-severity recall | At least 95% | Below 90% after two iterations: move to AI-assisted service model |
| Precision / citation precision | At least 85% / 95% | Alert fatigue drives override rate above 40% |
| 24-hour packs prepared on time | 100% | Any tool-caused miss: stop and fix before onboarding |
| Notified CAC text | Ingested and mapped | Final text drops the 24-hour report or a free SEBI/exchange tool covers it: pivot to pre-publication check and audit trail |
| Gross margin | At least 65% | Below 50%: re-price or switch models |

## 12. Risks and mitigations

| Risk | Likelihood / impact | Mitigation |
|---|---|---|
| Small market (about 2,500 RIA/RA firms plus PMS and top MFDs) | High / High | Treat as wedge and side line; add PMS, brokers, MFDs, CSCRF; keep burn low |
| Final CAC differs from the draft; notification or effective date slips | High / High | Version rules with status flags; stay useful without the filing step (archive, audit trail, disclosure); watch SEBI weekly |
| False negative (tool clears a breaching post) | Medium / High | Recall gates; human review of high-severity items; terms and positioning as decision support; evidence logs |
| Bundled competition (MFD platforms, OnFinance) or tiered AI rules | Medium / Medium | Platform-agnostic; SEBI depth; human oversight, kill switch, logging from day one |
| Customer cash constraints (RA cancellations) | High / Medium | Annual pre-pay discount; Solo tier; target PMS and brokers |
| Data privacy or CSCRF vendor-review failure | Medium / High | Zero-retention LLM terms, India hosting, penetration test, DPA |
| Platform access limits (WhatsApp, social APIs) | Medium / Medium | Forward-based intake; user-authorised capture; monitor cost per item |

## 13. Open questions and decisions needed

**Open questions (all [Unconfirmed])**

- What is the notified CAC text, and when is it effective? Not found in the research.
- Who receives the 24-hour report (SEBI, an exchange, the supervisory body), in what format, and is there an API or only a portal?
- Are WhatsApp broadcasts to existing clients "advertisements"? How does the final text treat research reports, education content and the 500,000-follower finfluencer threshold?
- Will AMFI adopt similar norms for MFDs? (MFD demand is an inference.)
- What retention period applies to ad and suitability records?
- Do CSCRF or other rules restrict sending client data to offshore LLM APIs?
- How many entities fall in each CSCRF category? No counts were found.

**Decisions needed**

- First customer segment: RIA/RA (reachable, small) or PMS/broker (higher price, longer cycle)?
- Include the CSCRF kit in the MVP or after day 90?
- Launch before the notified text, using draft rules flagged as advisory?
- Hosting region and LLM vendors.
- Standalone company, or side line funding the core product?

## 14. Expansion path

1. **Brokers, DPs, online bond platforms.** In the CAC consultation scope; add branch/AP hierarchy and celebrity pre-clearance.
2. **MFDs and AMCs.** The CAC also covers MFs/AMCs; MFDs follow if AMFI adopts similar norms **[Inference]**.
3. **Insurance intermediaries.** IRDAI advertising rules were not researched; a hypothesis.
4. **US RIAs.** 16,544 firms; marketing-rule and "AI washing" enforcement exist ([MoFo](https://mofo.com/resources/insights/240320-sec-targets-ai-washing-with-two-new-settled-cases)), and FINRA Notice 24-09 applies content standards to AI-written communications ([FINRA](https://finra.org/sites/default/files/2024-06/regulatory-notice-24-09.pdf)). Smarsh and Red Oak are entrenched; a niche is needed.
5. **Finfluencers.** Not direct customers (unpaid finfluencers sit outside the CAC's reach), but a registration-verification feature serves intermediaries vetting partners **[Inference]**.

## 15. Sources

- Research report: `reports/India AI personal finance MVP.md`, sections 6, 8 (Profile 4) and 10.
- Research notes (`research_notes/India AI personal finance MVP/`): `b2b_fintech_gaps.md` (section 2 on regtech; sections 1 and 6 on buyers and willingness to pay), `regulation_and_rails.md`, `global_regulation.md`, `global_b2b_ai_fintech.md`, `ai_native_entrants.md`.
- Other links: [TCSA on VAPT cost](https://www.tcsa.in/resources/vapt-cost-india-2026); all others are cited inline above.
- Caveat: most figures are from secondary coverage (law-firm notes, trade press) gathered on 7 Oct 2026. Verify every rule against sebi.gov.in before building or advertising claims.
