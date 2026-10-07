# Unsolved consumer fraud, scams and financial-safety problems (global + India) that AI products can now address — as of Oct 2026

Method note: ~26 web searches/fetches. Most figures come from secondary coverage of primary reports (FTC testimony, FBI IC3, UK Finance, RBI, I4C); I flag where I could not open the primary document. Where sources conflict I say so. Product concepts and feasibility ratings are my inferences, labelled as such.

## 1. How big is the problem globally (GASA, FTC, FBI IC3, UK Finance, India I4C/RBI)?

### Takeaway
Reported scam losses are rising almost everywhere and are dominated by investment/crypto fraud and authorised (victim-initiated) payments. Official counts are heavy undercounts (FTC itself estimates true 2024 cost up to ~$196B vs $12.5B reported). India's reported NCRP losses were about Rs 19.8k–22.9k crore in 2025 (sources differ), with investment schemes ~77% of that.

### Cited Findings
- GASA/Feedzai Global State of Scams 2025: ~$442B lost in 42 markets (survey of 46,000 adults); 57% of adults experienced a scam, 23% lost money; shopping scams affected 54% of victims, investment and "unexpected money" scams 48% each. Figure is a survey-based estimate, not audited; I could not open the full report. — [Feedzai](https://www.feedzai.com/global-state-of-scams-report-2025/), [GASA](https://gasa.org/knowledge-base/blog/global-scams-on-the-rise-over-half-of-adults-worldwide-report-scam-encounters), [Newswire](https://www.newswire.com/news/global-scams-on-the-rise-over-half-of-adults-worldwide-report-scam-22653499)
- GASA: 69% of victims report serious stress; many scams go unreported, uncertainty about where to report is the main barrier; ~3/4 of adults feel confident spotting scams yet many still lose money. — [Newswire](https://www.newswire.com/news/global-scams-on-the-rise-over-half-of-adults-worldwide-report-scam-22653499)
- US FTC (testimony 25 Mar 2026): 2025 consumers filed ~3M fraud reports, losses $15.9B (vs 2.6M reports / >$12B in 2024). Imposter scams most reported (>1M reports, >$3.5B). Investment scams largest losses ($7.9B). — [FTC press release](https://www.ftc.gov/news-events/news/press-releases/2026/03/ftc-testifies-joint-economic-committee-agencys-efforts-combat-fraud)
- FTC: bank payments were the highest aggregate-loss payment method, followed by crypto; credit cards most frequent. Growth driven by more consumers reporting losses of $100k+. FTC estimates 2024 true cost could be as high as $195.9B after underreporting. — [PYMNTS](https://www.pymnts.com/fraud-prevention/2026/consumer-fraud-losses-quintupled-since-2020-ftc-says/), [MLex](https://www.mlexwatch.com/ftcwatch/articles/2463206) (search-result summaries; payment-method detail not on the FTC release page I fetched)
- FBI IC3 2025: 1,008,597 complaints (first year over 1M), losses $20.877B (+26% vs 2024); investment fraud $8.648B (>40% of all losses). — [SOCRadar summary](https://socradar.io/blog/fbi-ic3-2025-internet-crime-report-10-takeaways/), [HousingWire](https://www.housingwire.com/articles/fbi-seniors-cybercrime-2025/); full report mirror: [IC3 2025 PDF](https://ppc.land/content/files/2026/07/2025_IC3Report.pdf) (not opened)
- UK Finance Fraud Report 2026 (published June 2026): total payment fraud £1.28B in 2025 (+4%); APP fraud £576.4M (+19%), 248,070 cases, ~32% of losses; investment scams £221.5M (+40%), purchase scams 71% of APP cases (£118.1M), romance £39.2M (+23%); two-thirds of APP fraud originated online, 17% via telecoms. — [FinTech Futures](https://www.fintechfutures.com/financial-crime-fraud-prevention/uk-payment-fraud-losses-topped-1-28bn-in-2025-new-uk-finance-report-finds), [PaymentExpert](https://paymentexpert.com/2026/06/15/uk-finance-fraud-report-2026/), [UK Finance PDF](https://www.ukfinance.org.uk/system/files/2026-06/UK%20Finance%20Fraud%20Report%202026.pdf) (not opened)
- India, I4C/NCRP data (reported Jan 2026): 2025 losses ~Rs 19,813 crore across ~21.8 lakh cheating complaints; split: investment schemes 77%, digital arrest 8%, credit card fraud 7%, sextortion 4%, e-commerce 3%, app/malware 1%. Maharashtra highest (Rs 3,203 cr), Karnataka Rs 2,413 cr. 2024 figure Rs ~22,845 cr (Lok Sabha reply July 2025) → reported losses fell in 2025 on this basis (my reading). — [IANS via ianslive](https://ianslive.in/indians-lose-over-rs-52976-crore-to-cyber-frauds-over-six-years-report--20260103154943), [The Week/PTI on 2024](https://www.theweek.in/wire-updates/business/2025/07/22/del23-lsq-cyber-fraud.html)
- CONFLICT on India 2025: RBI discussion paper (Apr 2026) cites NCRP fraud cases rising from ~2.6 lakh (2021) to ~28 lakh (2025) with value >Rs 22,900 crore. This differs from the Rs 19,813 cr / 21.8 lakh figure; likely different scope (e.g., CFCFRMS vs NCRP). — [Moneylife](https://moneylife.in/article/digital-payment-frauds-under-watch-rbi-proposes-1hour-delay-transaction-caps-and-kill-switch-to-counter-scams/80179.html) vs [IANS](https://ianslive.in/indians-lose-over-rs-52976-crore-to-cyber-frauds-over-six-years-report--20260103154943)
- India 2025 subset: 1,03,488 senior citizens and 4,63,114 women filed financial cyber-fraud complaints totalling Rs 7,769.63 crore (Rajya Sabha reply). — [Asianet summary](https://newsable.asianetnews.com/india/senior-citizens-women-lost-rs-7-769-crore-to-cyber-fraud-in-2025-articleshow-u9oad8w) (secondary)
- RBI Annual Report 2025-26 (May 2026): bank-reported frauds 10,114 cases / Rs 48,021 cr (vs 23,722 / Rs 32,803 cr), driven by loan/advances fraud (Rs 40,774 cr); card/internet/digital-payment category only 293 cases / Rs 29 cr (vs 13,332 / Rs 517 cr in FY25) — only frauds of Rs 1 lakh+ and by year of reporting, so this badly understates consumer UPI/APP fraud as seen on NCRP. — [Outlook Money](https://www.outlookmoney.com/banking/fraud-cases-fall-but-amount-involved-climbs-to-rs-48021-crore-in-fy26-says-rbi-annual-report), [Outlook Business](https://www.outlookbusiness.com/news/financial-institutions-report-over-10000-cases-of-fraud-involving-48000-cr-in-fy26-rbi-data)
- Meta (Reuters, Nov 2025, internal documents): ~10% of 2024 revenue (~$16B) projected from scam/banned-goods ads; ~15B "higher-risk" scam ads/day; advertisers banned only at ≥95% certainty of fraud. Meta says figure was "rough and overly inclusive". — [Khaleej Times/Reuters](https://www.khaleejtimes.com/business/tech/meta-is-earning-a-fortune-on-a-deluge-of-fraudulent-ads-internal-documents-show), [ACS Information Age](https://ia.acs.org.au/article/2025/meta-relies-on-scam-ads-for-10--of-its-revenues--internal-audit.html)

### Inferences
- Consistent global pattern: investment/crypto "pig-butchering" style fraud is now the single largest loss bucket (FTC ~half, IC3 >40%, UK Finance APP #1 by value, India NCRP 77%), whereas counts are dominated by cheaper scams (shopping, imposter). A product should be sized on loss-weighted categories, not volume.
- Bank-reported fraud stats (RBI Rs 29 cr digital) vs NCRP (Rs ~20k cr) show the loss sits outside banks' fraud ledgers — because APP fraud is "authorised", it is mostly not booked as bank fraud. This is exactly the liability gap.

### Gaps
- Could not open primary GASA, IC3, UK Finance PDFs; no verified India-specific GASA figure; no reconciled India 2025 total (Rs 19.8k vs 22.9k cr).

---

## 2. What regulatory/liability changes happened recently (UK PSR, EU PSR, Australia SPF, India RBI/SC)?

### Takeaway
The liability gap is closing unevenly: UK has mandatory bank reimbursement (live Oct 2024); EU has a provisional deal (Nov 2025) with narrower impersonation refunds and conditional platform liability; Australia has a framework law (Feb 2025) with main obligations ~31 Mar 2027; India is moving by friction/controls (RBI Apr 2026 discussion paper, Supreme Court orders) rather than customer reimbursement.

### Cited Findings
- UK PSR APP reimbursement: effective 7 Oct 2024; cost split 50/50 between sending and receiving PSP; max £85,000 per claim; 5-business-day reimbursement. Year 1 (7 Oct 2024–30 Sep 2025): ~88% of in-scope losses (~£173M) reimbursed; ~269,000 claims (~188,000 in scope); 84% resolved within 5 business days; 71% of victims unaware of the policy (PSR survey). — [A&O Shearman](https://finreg.aoshearman.com/psr-update-on-impact-of-app-fraud-reimbursement-s), [Plenitude summary](https://www.plenitudeconsulting.com/news-insights/psr-publishes-latest-app-scams-reimbursement-dashboard), [FStech](https://fstech.co.uk/fst/PSR_Reveals_88_Of_Money_Lost_To_APP_Scams_Reimbursed.php), [LexisNexis](https://www.lexisnexis.co.uk/legal/news/psr-publishes-2025-app-fraud-survey-latest-data-on-confirmation-of-payee). Detail on awareness/84% figures from secondary summaries.
- UK limits: reimbursement covers payments via Faster Payments/CHAPS only (per scheme); platforms and telcos (the originating channels: two-thirds online, 17% telecom) do not pay. UK Finance is asking tech/telecom firms to contribute financially. — [PaymentExpert](https://paymentexpert.com/2026/06/15/uk-finance-fraud-report-2026/)
- UK platforms: Online Safety Act fraudulent-advertising duties; Ofcom reportedly postponed decisions to mid-2026; Meta challenging category designation; Trading Standards lobbying. I did not verify whether Ofcom has finalised. — [MLex](https://www.mlex.com/mlex/articles/2410607/meta-defends-record-on-fraud-as-uk-watchdog-delays-new-online-safety-act-duties), [Irish Legal News](https://www.irishlegal.com/articles/meta-launches-fresh-legal-challenge-over-uk-online-safety-rules)
- EU PSR/PSD3 provisional deal 27 Nov 2025: PSP must refund in full where fraudster impersonates PSP staff (customer must report to police and PSP); payee name/IBAN verification, refuse on mismatch; receiving PSP must freeze suspicious payments; spending limits/blocking tools; online platforms may have to compensate PSPs if told of fraudulent content and fail to remove it. Formal adoption timetable not confirmed in my sources. — [European Parliament](https://www.europarl.europa.eu/news/en/press-room/20251121IPR31540/payment-services-deal-more-protection-from-online-fraud-and-hidden-fees), [Taylor Wessing](https://www.taylorwessing.com/en/insights-and-events/insights/2025/11/eu-lawmakers-strike-a-deal-on-payments-reforms)
- Australia Scams Prevention Framework Act 2025 (passed 13 Feb 2025; commenced ~21 Feb 2025): covers banks, telcos, digital platforms (designated May 2026); ACCC general regulator, ASIC for banks, ACMA for telcos. Draft codes/rules released May 2026 (consultation to 25 Jun 2026); most obligations from 31 Mar 2027, rest by end-2027; AFCA membership required by 1 Sep 2026. A Treasury position paper proposes automatic reimbursement of verified losses under A$3,000 with equal apportionment between breaching entities. — [HSF Kramer](https://www.hsfkramer.com/insights/2026-06/stage-1-of-the-scams-prevention-framework), [Netcraft](https://www.netcraft.com/blog/australia-scams-prevention-framework-what-the-new-obligations-mean-for-banks), [Corrs](https://corrs.com.au/insights/developing-the-scams-prevention-framework-treasury-consults-on-draft-rules-and-codes), [Ashurst](https://www.ashurst.com/en/insights/scams-prevention-framework-draft-rules-and-codes-released/)
- India, RBI discussion paper "Exploring safeguards in digital payments to curb frauds" (9 Apr 2026; comments to 8 May 2026): (1) 1-hour delay on account-to-account transfers >Rs 10,000 with cancel window (whitelisted beneficiaries exempt); (2) trusted-person authentication for seniors/PwD above Rs 50,000; (3) cap on annual credits (reported Rs 25 lakh) to accounts without enhanced verification; (4) customer-controlled on/off per payment mode, limits, "kill switch". Status of final rules: not confirmed. — [Moneylife](https://moneylife.in/article/digital-payment-frauds-under-watch-rbi-proposes-1hour-delay-transaction-caps-and-kill-switch-to-counter-scams/80179.html), [RBI](https://rbi.org.in/Scripts/PublicationsView.aspx?id=23810), [TaxGuru](https://taxguru.in/rbi/rbi-seeks-public-comments-digital-payment-fraud-safeguards-paper.html)
- India, RBI annual report (May 2026) said it would explore friction for APP fraud and a customer-controlled "kill switch". — [Business Standard](https://www.business-standard.com/finance/news/rbi-digital-payments-fraud-upi-security-frictions-126052900821_1.html) (via search summary; page blocked on fetch)
- India, RBI draft (11 Sep 2026; comments to 2 Oct 2026): up-to-60-day "debit hold" on suspected mule/cyber-fraud accounts with unblocking process. Source is a low-tier site; verify. — [IndianPayCalculator](https://www.indianpaycalculator.in/govt-news/rbi-60-day-debit-hold-mule-cyber-fraud-draft-rules-2026)
- India, Supreme Court suo motu "digital arrest" case: Dec 2025 order gave CBI pan-India mandate (incl. bankers suspected of creating mule accounts); 4 Aug 2026 order told RBI to prepare an SOP within four weeks for mule accounts/freezing with safeguards; flagged SIM issuance negligence by telcos; I4C reported digital-arrest NCRP complaints fell from 1,23,672 (2024) to 58,249 (2025) to 16,377 (to 30 Jun 2026). — [Moneylife](https://www.moneylife.in/article/supreme-court-issues-directions-to-curb-digital-arrest-scams-asks-rbi-to-frame-sop-on-mule-accounts/81256.html), [Verdictum](https://www.verdictum.in/court-updates/supreme-court/supreme-court-orders-cbi-probe-into-digital-arrest-cases-across-india-1599721), [Vision IAS](https://visionias.in/current-affairs/upsc-daily-news-summary/article/2025-12-02/the-hindu/security/supreme-court-gives-cbi-free-hand-to-stop-digital-arrest-scams)
- India, over-freezing risk: Calcutta HC ordered SBI to defreeze a businessman's account frozen since Mar 2026 on mere mule suspicion. — [LiveLaw](https://www.livelaw.in/high-court/calcutta-high-court/rbi-guidelines-do-not-specifically-authorise-banks-to-freeze-accounts-on-mere-suspicion-of-money-mule-activity-calcutta-high-court-549563)
- US: no federal APP reimbursement; Reuters reports an SEC probe into Meta over financial-scam ads. — [Khaleej Times/Reuters](https://www.khaleejtimes.com/business/tech/meta-is-earning-a-fortune-on-a-deluge-of-fraudulent-ads-internal-documents-show)

### Inferences
- India still has no customer reimbursement right for APP/UPI scams (none found in my searches); regulatory energy is on friction + mule freezing. That leaves victims bearing loss, and means consumer-side prevention tools have more value in India than in the UK, where the bank pays.
- In the UK/Australia/EU regimes, banks and (later) platforms/telcos gain a direct financial reason to buy detection tech (B2B demand), and receiving-bank mule detection becomes a cost-sharing issue (UK 50/50).
- Over-freezing (Calcutta HC) + SC safeguards imply demand for explainable mule-scoring, not just binary flags.

### Gaps
- Final status of RBI proposals (1-hour delay etc.) as of Oct 2026 not confirmed. No EU PSR formal adoption/application date found. No official India "zero-liability" scheme found beyond RBI's 2017 unauthorized-transaction rules (not researched).

---

## 3. What are current solutions (India and global) and their limits?

### Takeaway
Existing defences are fragmented: telco/OS-level call and message screening, payee-risk signals (India's FRI), bank-side mule models, and family/trusted-contact features. They are mostly bank- or platform-centric, English-first, and none follows the victim across WhatsApp/Telegram → call → UPI.

### Cited Findings
- India DoT Financial Fraud Risk Indicator (FRI), launched 21 May 2025: grades mobile numbers Medium/High/Very High fraud risk from NCRP, Chakshu and bank intel; RBI advised banks (30 Jun 2025) to integrate; PhonePe declines payments to Very High numbers and warns on others; PhonePe, Paytm, Google Pay (>90% of UPI) integrating. — [Business Standard](https://www.business-standard.com/industry/news/dot-launches-financial-fraud-risk-indicator-to-aid-cybercrime-detection-125052101912_1.html), [Moneylife](https://www.moneylife.in/article/new-fraud-indicator-flags-risky-mobile-numbers-in-realtime-to-thwart-upi-scams/77200.html), [Vixio](https://www.vixio.com/insights/pc-india-launches-financial-fraud-risk-indicator-tackle-upi-scams)
- NPCI/UPI: UPI apps must show only bank-registered beneficiary names (June 2025); UPI Circle (delegated payments: up to 5 secondary users; full delegation max Rs 5,000/txn and Rs 15,000/month per delegation); two-factor requirement for digital payments from 1 Apr 2026 (secondary source, verify). — [Retirement Outlook](https://retirement.outlookindia.com/plan/news/ncpis-new-upi-circle-know-how-this-feature-eases-online-payment-for-you), [M2P](https://m2pfintech.com/blog/upi-fraud-security-guide-npci-m2p-solutions/)
- MuleHunter.AI (RBI Innovation Hub): ML model built on 19 mule patterns; by ~Aug 2025 live at Canara, PNB, BoI, BoB, AU SFB with 15 more banks planned; Finance Secretary urged banks to implement (May 2026); I4C–RBIH MoU (12 May 2026) to share Suspect Registry data to train it. Performance claims (e.g., ~3x manual accuracy) are RBIH's own, no independent evaluation found. — [Business Standard](https://www.business-standard.com/industry/banking/15-more-banks-to-adopt-rbi-s-mulehunter-fraud-detection-tool-by-october-125080101845_1.html), [Moneylife](https://moneylife.in/article/i4c-rbi-innovation-hub-sign-mou-to-use-ai-for-detecting-mule-accounts-and-cyber-frauds/80439.html), [Outlook Business](https://www.outlookbusiness.com/economy-and-policy/rbi-introduces-ai-to-curb-financial-frauds-how-mulehunter-ai-will-tackle-mule-accounts)
- I4C Suspect Registry (launched 10 Sep 2024): reported 27.37 lakh mule accounts identified/shared, Rs 9,518 cr of fraudulent transactions declined (government-linked claim; an earlier cited figure was 24.67 lakh). — [CyberPeace](https://cyberpeace.org/resources/blogs/operation-mule-hunt-2-0-how-ordinary-bank-accounts-became-indias-biggest-cybercrime-weapon), [Chambers](https://gpg-pdf.chambers.com/Financial-Crime-2026/97/)
- Google on-device call screening (Gemini Nano) and Google Pay/Paytm/Navi warnings during screen-share calls in India; Play Protect blocked >115M sideload attempts in India. — [Gulf News](https://gulfnews.com/technology/media/google-ramps-up-ai-scam-protection-in-india-1.500355149)
- Truecaller: AI Call Scanner (English-only at launch, adapting Hindi; listed in US/AU/CA/ZA, beta in India); Scam Checker in India; Truecaller India report: 4,168 crore spam calls, 12,903 crore spam messages, 770 crore fraud calls (2025). Accuracy not publicly quantified. — [TechRepublic](https://www.techrepublic.com/article/news-truecaller-scam-checker-apac-india/), [MediaNama](https://www.medianama.com/2024/05/223-truecaller-ai-voice-scanner-spam-call/), [India TV](https://www.indiatvnews.com/topic/-truecaller)
- Carefull (US, B2B2C elder financial safety): Series A $16.5M (2023), total ~$19.7M; sells to banks/wealth advisors; scans accounts for 50+ aging-related risks; Trusted Contacts; CIBC Innovation Banking investment mid-2025. — [Pulse2](https://pulse2.com/carefull-ai-16-5-million-funding/), [BTW Media](https://btw.media/en/carefull-secures-funding-from-cibc-innovation). New York state / SilverShield text-in scam-check service launching 2026. — [Spectrum News](https://spectrumlocalnews.com/nys/buffalo/politics/2025/12/03/n-y--to-launch-tool-in-2026-to-curtail-elderly-scam-victims)
- RBI Digital Lending Apps directory (from 1 Jul 2025) lets users check an app's tie to a regulated lender; Google Play India requires loan apps to be in it; MeitY says 87 illegal loan apps blocked (July 2026 reply), names not published; 3,718 apps blocked overall by 30 Jun 2026. — [Moneylife](https://www.moneylife.in/article/fraud-alert-desperate-for-a-quick-loan-fake-apps-can-turn-a-5000-need-into-a-nightmare/81353.html), [The Wire/GoCredit](https://m.thewire.in/article/ptiprnews/gocredit-launches-free-loan-app-checker-to-verify-if-a-lending-app-is-real-fake-or-rbi-registered)
- SEBI: #SEBIvsSCAM and advisories warning against WhatsApp/Telegram stock-tip groups, fake apps with forged SEBI registration; "Intermediary Search" for verifying advisers; helpline 1930. — [Business Standard](https://www.business-standard.com/amp/markets/news/sebi-warns-investors-about-stock-market-scams-via-social-media-platforms-125052101612_1.html), [Angel One](https://www.angelone.in/news/market-updates/sebi-warns-investors-against-fake-trading-groups-on-whatsapp-and-other-social-media-platforms)

### Inferences
- Gaps in existing tools: (a) none sees the full chain; (b) FRI only catches numbers already in blacklists — new burner numbers/ new mule accounts are first-use; (c) tools are English/US-first (Truecaller scanner), whereas Indian scams run in Hindi/regional languages and WhatsApp video calls; (d) bank-side tools protect the bank, not the victim, and RBI's own proposed fix is blunt friction (1-hour delay) which scammers can coach victims around; (e) WhatsApp/Telegram groups and fake-trading-app downloads sit entirely outside the banks' view.
- AI plausibly adds value in cross-channel context understanding (screenshot/voice/note → is this a scam?), multilingual dialogue, and generating explainable risk reasons — but this is my judgement, not an evidence-backed performance claim.

### Gaps
- No independent efficacy/accuracy numbers for Truecaller, MuleHunter, FRI. No data on Hiya's deepfake detector or Google "Scam Detection" for messages in India (not found). Aura/Norton consumer products not covered.

---

## 4. Problem-by-problem: APP/UPI fraud and digital arrest / impersonation

### Takeaway
UPI/APP fraud and "digital arrest" are the same structural failure: victim authenticates the payment themselves under coercion, mules cash out within minutes, and no party is liable. Digital-arrest reports in India are falling (123,672 → 58,249 → 16,377 H1-2026) after enforcement, but remain a major severity-per-victim problem (average losses very high, elderly targeted).

### Cited Findings
- Digital arrest India: 2022 Rs 91.14 cr (39,925 cases); 2023 Rs 339 cr (60,676); 2024 Rs 1,935.51 cr (1.23 lakh complaints); Jan–Feb 2025 Rs 210.21 cr (17,718 incidents). — [Inc42](https://inc42.com/?p=504907), [Lawful Legal](https://lawfullegal.in/digital-arrest-scams-%e2%82%b92000-210-crore-explained/)
- 2025 share of digital arrest = ~8% of I4C-reported Rs 19,813 cr (~Rs 1,500+ cr; my arithmetic). NCRP digital-arrest complaints: 1,23,672 (2024) → 58,249 (2025) → 16,377 (to 30 Jun 2026). — [IANS](https://ianslive.in/indians-lose-over-rs-52976-crore-to-cyber-frauds-over-six-years-report--20260103154943), [Moneylife SC](https://www.moneylife.in/article/supreme-court-issues-directions-to-curb-digital-arrest-scams-asks-rbi-to-frame-sop-on-mule-accounts/81256.html)
- Supreme Court (Dec 2025) cited ~Rs 3,000 crore scammed primarily from elderly; CBI probe: one investigation identified 238 victims, 67 first-layer accounts, ~Rs 80 cr, searches at 93 locations in 16 states; June 2026 searches of 80+ locations. — [Storyboard18](https://www.storyboard18.com/digital/supreme-court-grants-cbi-full-authority-to-tackle-nationwide-digital-arrest-scams-85176.htm), [Free Press Journal](https://www.freepressjournal.in/india/digital-arrest-scams-cbi-crackdown-widens-as-supreme-court-keeps-up-pressure)
- DoT: reports >5 crore fake connections disconnected over two years to July 2026 and Rs 1,800 cr+ frauds blocked — unverified against an official release. — [GKToday](https://www.gktoday.in/dot-disconnects-over-five-crore-fake-mobile-connections/)
- UK: APP fraud origin 17% via telecom, 2/3 online. — [PaymentExpert](https://paymentexpert.com/2026/06/15/uk-finance-fraud-report-2026/)
- FTC: bank-transfer payments highest-loss; imposter scams >$3.5B. — [PYMNTS](https://www.pymnts.com/fraud-prevention/2026/consumer-fraud-losses-quintupled-since-2020-ftc-says/), [FTC](https://www.ftc.gov/news-events/news/press-releases/2026/03/ftc-testifies-joint-economic-committee-agencys-efforts-combat-fraud)
- Why unsolved (India): mule accounts and SIMs. SC found "alarming" multiple-SIM issuance negligence; ED traced >Rs 12,000 cr through mule accounts/shell firms/crypto; ~Rs 9,518 cr declined by registry data; Calcutta HC shows legitimate holders get frozen. — [Moneylife SC](https://www.moneylife.in/article/supreme-court-issues-directions-to-curb-digital-arrest-scams-asks-rbi-to-frame-sop-on-mule-accounts/81256.html), [CyberPeace](https://cyberpeace.org/resources/blogs/operation-mule-hunt-2-0-how-ordinary-bank-accounts-became-indias-biggest-cybercrime-weapon)

### Inferences
- Why unsolved: (1) speed of UPI/IMPS (money leaves before report; "golden hour" logic of RBI paper); (2) authorised nature — bank sees valid PIN; (3) no reimbursement duty in India so banks lack incentive to add friction costing UX; (4) cross-border call centres (SE Asia — not researched here) beyond Indian enforcement; (5) telcos/platforms bear no liability.
- Concept A (consumer): "Call Shield" — on-device agent that detects the coercion script (claims of police/CBI/customs/TRAI, "stay on video call", "don't tell anyone", "transfer to RBI safe account") from call transcript/WhatsApp video call screenshot + monitors UPI app screen-share and, at the moment of a large first-time payment, triggers a family-guardian alert. Feasibility for a small team: Medium. Android accessibility/notification permissions and on-device ASR in Hindi/regional languages are doable; iOS is hard; Play Store policies on call recording/accessibility are risks; liability for false negatives.
- Concept B (B2B): "pre-payment coercion check" SDK for UPI apps/neo-banks: session signals (active call, screen-share, new payee, first-time large amount) + 10-second conversational check; leverages FRI. Feasibility: Low-Medium for a small team (long bank/PSP sales cycles; but TPAP/SDK route possible).

### Gaps
- No full-year 2025 official digital-arrest total beyond the 8% share; no data on share of victims who are elderly (SC's 'primarily elderly' is a qualitative statement). Cross-border scam-centre geography not researched in this pass.

---

## 5. Problem-by-problem: pig-butchering / investment scams (fake trading apps, WhatsApp/Telegram stock-tip groups)

### Takeaway
This is the biggest dollar-loss category everywhere (FTC $7.9B; IC3 $8.65B; UK APP £221.5M; India ~77% of NCRP losses) and has the weakest existing defence because it starts on social ads/WhatsApp, unfolds over weeks, and ends in a payment the victim believes is an investment.

### Cited Findings
- Global numbers: see Section 1 (FTC $7.9B, avg loss >$10,000; IC3 $8.648B, >40% of losses; UK £221.5M +40%; India ~77% of Rs 19,813 cr). — [PYMNTS](https://www.pymnts.com/fraud-prevention/2026/consumer-fraud-losses-quintupled-since-2020-ftc-says/), [SOCRadar](https://socradar.io/blog/fbi-ic3-2025-internet-crime-report-10-takeaways/), [FinTech Futures](https://www.fintechfutures.com/financial-crime-fraud-prevention/uk-payment-fraud-losses-topped-1-28bn-in-2025-new-uk-finance-report-finds)
- Playbook (SEBI): unsolicited WhatsApp/Telegram invites to "VIP"/"free trading course" groups; fake experts, fake testimonials, fake SEBI registration; fake apps cloned from legit brokers; early small "profits" and withdrawal blocked behind "tax/brokerage/processing" fees. — [Business Standard](https://www.business-standard.com/amp/markets/news/sebi-warns-investors-about-stock-market-scams-via-social-media-platforms-125052101612_1.html), [Angel One](https://www.angelone.in/news/market-updates/sebi-warns-investors-against-fake-trading-groups-on-whatsapp-and-other-social-media-platforms)
- Scale cue: CloudSEK found >81,000 fraudulent investment groups on WhatsApp in H1 2024 (older data). — via [Angel One/SEBI coverage search](https://www.angelone.in/news/market-updates/sebi-warns-investors-against-fake-trading-groups-on-whatsapp-and-other-social-media-platforms) (figure attributed in search summary; original CloudSEK report not opened)
- India 2026 case examples: Bhopal retiree Rs 3.91 cr (fake app, forged SEBI documents, 20% "processing" fee demand); Bhopal police tally Nov 2025–Jun 2026: 279 complaints / 240 cases / Rs 14.86 cr; Valsad retiree Rs 2.52 cr (YouTube→WhatsApp, Rs 66 lakh "brokerage fee"); Nashik Rs 21.64 cr. — [Free Press Journal](https://www.freepressjournal.in/bhopal/retired-67-year-old-man-loses-391-crore-in-fake-stock-scam-bhopal), [Logical Indian](https://thelogicalindian.com/60-year-old-gujarat-man-loses-rs-2-52-crore-in-youtube-linked-whatsapp-stock-trading-scam-trap/), [UNI](https://www.uniindia.com/-21-64-crore-online-stock-investment-fraud/west/news/3744785.html)
- IC3: 78% of 3,780 crypto-investment victims contacted under Operation Level Up did not know they were being scammed (single blog source; verify). — [Gupta Deepak blog](https://guptadeepak.com/scams-that-cost-americans-2025/)
- Platform side: Meta ad revenue from scam ads (Section 1); EU/UK/AU frameworks start to touch platform liability; India has none found.

### Inferences
- Why unsolved: victim is a willing, repeated payer; each transfer looks like a legitimate broker/bank payment; scammers move faster than blocklists; banks cannot see the social-media grooming. Liability sits nowhere in India.
- Concept C (consumer, strongest): "Investment sanity-check agent" — user forwards/screenshots a tip group, app link or advisor profile to a WhatsApp bot; agent verifies against SEBI intermediary/RIA/broker lists, RBI/SEBI registries, app-store listing and domain age, detects cloned broker apps, and explains red flags in Hindi/regional languages; follows up weeks later ("has the withdrawal been blocked?"). Feasibility for small team: High for MVP (public registries + LLM + WhatsApp Business API; limited data licensing). Risk: users reach out only when already doubtful; distribution via SEBI-regulated broker partners or family-sharing is key. Also false-positive/defamation risk when labelling a named entity as a scam.
- Concept D (B2B): fake-brand/broker-app takedown monitoring for brokers and fintechs (Bolster-style) — mature competitors exist globally; India-specific tailoring (WhatsApp group scraping, APK clones) is an opening. Feasibility: Medium.

### Gaps
- No verified count of Indian victims; no recent (2026) CloudSEK/other national estimate of WhatsApp/Telegram group scams; SEBI loss data not found.

---

## 6. Problem-by-problem: deepfake voice/video and AI-enabled impersonation

### Takeaway
AI impersonation is measurably growing but hard to size: the best-sourced number is an FBI IC3 AI-related elder subset (3,100+ senior complaints, >$352M); broader "deepfake loss" statistics are vendor roundups with inconsistent definitions.

### Cited Findings
- IC3 2025: >3,100 complaints from seniors referencing AI, losses >$352M. — [Agrinews/Senior News Line, HousingWire summary via search](https://www.housingwire.com/articles/fbi-seniors-cybercrime-2025/) (via search summary, not opened)
- Another blog states IC3 logged >22,000 AI-related complaints with >$893M in losses (unverified against IC3). — [search-result roundup](https://trusona.com/blog/deepfake-fraud-statistics-2026)
- Secondary stats (low confidence, vendor/roundup): Deloitte projection of US gen-AI fraud losses $40B by 2027 from $12.3B in 2023; Pindrop-attributed 1,300%+ rise in deepfake fraud attempts in 2024; Signicat: deepfakes ~6.5% of fraud attempts; McAfee claim of 3 seconds of audio to clone a voice at 85% match. — [StationX](https://app.stationx.net/articles/deepfake-statistics), [Trusona](https://trusona.com/blog/deepfake-fraud-statistics-2026)
- Google rolled out on-device call screening and (per one aggregator, June 2026, unverified) fake-call/deepfake detection on Android 12+ starting with Pixel. — [Gulf News](https://gulfnews.com/technology/media/google-ramps-up-ai-scam-protection-in-india-1.500355149), [Westfield summary](https://goodfest.westfield.com/2026/06/google-rolls-out-fake-call-detection-to-protect-against-ai-deepfake-impersonation-scams/)

### Inferences
- Detection of synthetic audio is an arms race and unreliable on compressed phone/WhatsApp audio; the more robust consumer defence is behavioural/procedural (family code word, call-back verification, "stop and verify" before payment) rather than "is this voice fake" classification. A small team should not bet on a deepfake classifier as its moat.
- Concept E: "Family safe-word + verification agent" that sets up a rotating code phrase and a call-back flow between family members and, on a suspicious "relative in trouble" call, nudges the user to verify via a pre-registered channel. Feasibility: High (simple), but low defensibility and requires behavioural adoption.

### Gaps
- No primary source (Pindrop, Deloitte, Resemble) opened; no India-specific deepfake fraud loss number found.

---

## 7. Problem-by-problem: elder financial exploitation

### Takeaway
Older adults are the highest-severity victims: FBI 2025 shows $7.7B losses among 60+ (+59%), averaging $38,500 per victim; India's SC says digital-arrest victims are primarily elderly. Bank-led trusted-contact products exist but are B2B in rich markets; in India the RBI paper itself proposes trusted-person authentication.

### Cited Findings
- FBI IC3 2025, age 60+: 201,266 complaints; ~$7.75B losses (+59%); avg $38,500; >12,400 lost >$100k; investment fraud $3.52B; tech/customer support $1.04B; romance/confidence $584M; BEC $568M; California most complaints (22,157). — [HousingWire](https://www.housingwire.com/articles/fbi-seniors-cybercrime-2025/), [AgriNews](https://www.agrinews-pubs.com/features/2026/06/24/senior-news-line-fbi-report-on-senior-scam-losses/) (via search summaries; not opened)
- India: Rs 7,769.63 cr combined (senior citizens + women) in 2025 — see Section 1; SC: ~Rs 3,000 cr digital-arrest losses mostly elderly. — [Asianet](https://newsable.asianetnews.com/india/senior-citizens-women-lost-rs-7-769-crore-to-cyber-fraud-in-2025-articleshow-u9oad8w), [Storyboard18](https://www.storyboard18.com/digital/supreme-court-grants-cbi-full-authority-to-tackle-nationwide-digital-arrest-scams-85176.htm)
- RBI proposal: trusted-person authentication for seniors/PwD above Rs 50,000. — [Moneylife](https://moneylife.in/article/digital-payment-frauds-under-watch-rbi-proposes-1hour-delay-transaction-caps-and-kill-switch-to-counter-scams/80179.html)
- UPI Circle allows delegation with limits (Rs 5,000/txn full delegation). — [Retirement Outlook](https://retirement.outlookindia.com/plan/news/ncpis-new-upi-circle-know-how-this-feature-eases-online-payment-for-you)
- Carefull and similar products sell to banks/advisors; NY state/SilverShield text-in tool in 2026. — [Pulse2](https://pulse2.com/carefull-ai-16-5-million-funding/), [Spectrum News](https://spectrumlocalnews.com/nys/buffalo/politics/2025/12/03/n-y--to-launch-tool-in-2026-to-curtail-elderly-scam-victims)

### Inferences
- Why unsolved: seniors are isolated, trust authority figures, and hold the assets; adult children (often NRIs or in other cities in India) have no visibility or consent mechanism; banks cannot override a customer's authorised transfer.
- Concept F (strongest for India): "Family Guardian" — adult-child installs/links parent's phone (consent-based); detects risky patterns (long call from unknown number with screen-share app active, new payee, first large UPI transfer, new app installs from APK) and sends a real-time "call your parent" alert; optional parent-side voice nudge in local language; weekly digest of suspicious calls. Feasibility: Medium-High for small team on Android (UPI Circle/trusted-person rules align with RBI direction; Play policy and privacy/DPDP consent are the hard parts; reading UPI app screens needs accessibility permission, which Play restricts). B2C willingness-to-pay uncertain; B2B2C via banks/insurers (cf. Carefull model) may be better.

### Gaps
- No India-specific elderly victim share by value beyond the Rajya Sabha subset; no pricing/WTP data for family-guardian products in India.

---

## 8. Problem-by-problem: identity theft, synthetic identity and account takeover

### Takeaway
Quantification is weak and vendor-driven; the best data point is Javelin (via a vendor summary) putting US account takeover (ATO) losses above $15B in 2025 with >6M victims, while synthetic-ID loss estimates range widely ($20–40B globally). These are largely B2B (bank/fintech) problems, less attractive for a small consumer team.

### Cited Findings
- Javelin 2026 study (vendor summary): US ATO losses >$15B in 2025, down 4%, but victims up to >6M (+18%); new-account fraud victims +31% to 5.4M. Javelin warns that scam-derived data converts into later identity fraud. — [Microblink](https://microblink.com/?p=42037), [Swif](https://www.swif.ai/blog/identity-theft-statistics)
- TransUnion H1 2026 Fraud Trends: US consumers reported $99B digital fraud losses in 2025 with 16% affected; ATO up 37% to 3.14% of suspected digital fraud. — [TransUnion UK PDF](https://www.transunion.co.uk/content/dam/transunion/gb/business/documents/H1-2026-Fraud-Trends-Report.pdf) (via summary; definitions unclear)
- Synthetic identity: BIIA-attributed estimates $30–35B US/yr or $20–40B global; US lenders $3.3B exposure in H1 2025; claims up to 80% of new-account fraud at some institutions. Estimates conflict. — [BIIA](https://www.biia.com/synthetic-identity-fraud-statistics-2026)
- Federal contrast: 5,100+ ATO complaints / $262M (Jan–Nov 2025) — shows reported vs estimated gap. — [Microblink](https://microblink.com/?p=42037)
- India-specific identity/synthetic ID and ATO loss data: not found in this pass.

### Inferences
- For India, the equivalent consumer-facing issues are SIM swap/fraudulent SIMs under victim's Aadhaar (SC flagged multiple SIMs per name), mule accounts opened with rented/stolen KYC, and loan apps misusing contact data. A consumer product could offer "who is using my ID" monitoring (SIMs registered on your Aadhaar via Sanchar Saathi TAFCOP, bank/credit bureau enquiries), but data access is limited — Feasibility: Low-Medium; mostly a B2B (KYC/mule detection for small banks/NBFCs) opportunity.
- Concept G (B2B): mule-account and synthetic-ID detection for small banks, co-op banks, NBFCs and payment banks that cannot build ML teams and are not yet on MuleHunter.AI: transaction-graph + device + KYC signals, explainable scores, and a "freeze with safeguards" workflow aligned to the pending RBI SOP. Feasibility: Medium for a small team technically (open-source graph/GBM approaches), but low data access and long procurement; RBIH offers MuleHunter as a public good, so differentiation must come from explainability, workflow and coverage of non-adopters. Needs labelled data (I4C suspect registry is not public).

### Gaps
- No primary Javelin/TransUnion document opened; no India ATO/synthetic ID figures; no evidence on how many small banks/NBFCs have adopted MuleHunter.AI.

---

## 9. Problem-by-problem: romance scams, fake loan apps, and job/task scams

### Takeaway
These are lower-dollar but high-count, high-harm categories that feed mule networks (task scams) or cause severe distress (loan-app harassment). Task scams grew fast in 2024–25; Indian loan-app harassment is still producing deaths in 2026 despite RBI's DLA directory.

### Cited Findings
- Romance (UK): APP romance scam losses £39.2M in 2025 (+23%). — [FinTech Futures](https://www.fintechfutures.com/financial-crime-fraud-prevention/uk-payment-fraud-losses-topped-1-28bn-in-2025-new-uk-finance-report-finds). US: romance reported as $1.16B in an FTC-sourced article (Feb 2026; I did not open the primary data). — [Global Dating Insights](https://globaldatinginsights.com/2026/02/26/romance-scams-outpace-other-fraud-types-at-1-16-billion/)
- IC3 2025 (seniors): confidence/romance $584M. — [HousingWire](https://www.housingwire.com/articles/fbi-seniors-cybercrime-2025/)
- Job/task scams (US): business and job opportunities $750.6M in 2024 (2nd largest FTC category); job-agency subcategory $90M (2020) → $501M (2024); secondary source cites 110,653 job-scam complaints / $518.2M in Jan–Sep 2025; gamified task scam reports ~20,000 in early 2024 vs 5,000 in all 2023. Pattern: unsolicited WhatsApp/text, fake "product boosting" tasks with fake earnings, deposit in crypto to withdraw. — [Bitdefender on FTC data](https://www.bitdefender.com/en-us/blog/hotforsecurity/job-scams-americans-millions-dollars-2024), [TechBullion](https://techbullion.com/job-scam-statistics-fbi-ftc-data/), [AP via NY1](https://ny1.com/nyc/all-boroughs/ap-top-news/2025/07/09/beware-of-scams-that-promise-good-pay-for-completing-easy-online-tasks)
- India task/part-time-job scams: SC explicitly prioritised digital arrest over "investment frauds and part-time job scams" (i.e., these remain large but separate). I did not find a separate India loss figure for task scams. — [Storyboard18](https://www.storyboard18.com/digital/supreme-court-grants-cbi-full-authority-to-tackle-nationwide-digital-arrest-scams-85176.htm)
- India fake/illegal loan apps: MeitY says 87 illegal loan apps blocked (July 2026 reply); RBI DLA directory (from 1 Jul 2025; reported 1,024 apps as of 1 Sep 2026 from a single report); 2026 suicide/harassment cases in Kerala (Apr 2026, "Insta Pay"), Hyderabad (Jul 2026), etc., all alleged/under investigation. — [Moneylife](https://www.moneylife.in/article/fraud-alert-desperate-for-a-quick-loan-fake-apps-can-turn-a-5000-need-into-a-nightmare/81353.html), [Onmanorama](https://www.onmanorama.com/news/kerala/2026/04/17/nithin-raj-loan-app-suicide-case-kannur-police-insta-pay.amp.html), [Telangana Today](https://telanganatoday.com/hyderabad-man-ends-life-alleges-loan-app-harassment)

### Inferences
- Why unsolved: no single liable party; scam recruits via WhatsApp/Telegram; payments often small enough to evade bank friction; victims later become mules (task-scam workflows launder funds — plausible but not directly sourced here).
- Concept H (consumer): "Loan app / job offer checker" — a WhatsApp bot or Android share-sheet target that checks an APK/package name/website against the RBI DLA directory, Play listing, permissions requested (contacts/gallery), and flags the "pay a deposit to withdraw/earn" pattern for job offers; plus an "I'm being harassed" flow that auto-drafts 1930/NCRP and grievance-officer complaints. Feasibility: High for small team (public directory + permission analysis + LLM chat); defensibility is low and distribution is the main problem; likely a feature of a broader product (Concept C/F) rather than standalone.

### Gaps
- No primary FTC romance/job-scam 2025 table opened; India loss figures for romance, loan apps and task scams not found.

---

## 10. Which concepts are feasible for a small team (ranking) and what are the key risks?

### Takeaway
Best near-term wedge for an India-first small team: a multilingual, WhatsApp-native scam-check agent (investment/loan-app/job/impersonation) plus an optional family-guardian layer. B2B mule detection is higher value but needs data and bank access; deepfake-classifier startups face an arms race.

### Cited Findings
- (Evidence backing the ranking comes from sections above: investment = biggest loss bucket; elderly = highest severity; UK victims unaware of reimbursement (71%); RBI proposes trusted-person authentication and customer-controlled limits; DoT FRI exists for payee screening; Truecaller scanner is English-first and beta in India.) — see sources in Sections 1–9.

### Inferences (my feasibility ranking, not a sourced finding)
1. Concept C + H merged: "Is this a scam?" WhatsApp bot — High feasibility (days–weeks MVP): public registries (SEBI, RBI DLA, Sanchar Saathi/Chakshu), LLM triage on screenshots/voice notes/links, regional languages, follow-up checks. Risks: wrong labels (defamation), adoption only when users are already suspicious, WhatsApp Business API costs/policy, no monetisation (B2B2C with brokers, UPI apps, insurers, or telcos is likelier than subscriptions).
2. Concept F Family Guardian (Android) — Medium-High feasibility; high emotional pull; risks: Play accessibility policy, DPDP Act consent, elderly adoption, iOS limits.
3. Concept A Call Shield (on-device) — Medium; competes with Google/Truecaller; strongest if tuned to Indian digital-arrest scripts in Hindi/regional languages.
4. Concept G mule detection for small banks/NBFCs — Medium technical, hard commercially; aligns with RBI SOP/60-day hold and SC pressure, MuleHunter.AI competition (free public good), data access barrier.
5. Concept E safe-word — trivial, low moat. Deepfake classifier — not recommended as core.
- Where regulation could kill/boost: RBI 1-hour delay and trusted-person rules (if finalised) boost guardian features; an India reimbursement mandate (none found) would shift value to bank-side B2B; Australia/EU/UK regimes create export demand for explainable detection.

### Gaps
- No pricing, willingness-to-pay or CAC evidence collected; no check of regulatory restrictions on reading UPI app screens or call audio in India (DPDP Act, Play policy) — flagged for follow-up; competitive landscape (Bolster, Hiya, BioCatch, Sardine, Trusted Contact products) only lightly covered—Bolster/Hiya/BioCatch/Sardine reports were not found in searches.
