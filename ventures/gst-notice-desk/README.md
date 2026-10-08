# GST Notice Desk

An AI reconciliation and notice desk for Indian chartered-accountant (CA) firms. It matches GSTR-2B and Invoice Management System (IMS) data against clients' books every month, turns the result into a per-supplier action list with rupees of input tax credit (ITC) at risk, chases suppliers, and reads GST notices (DRC-01C, DRC-01, DRC-01B, ASMT-10) to assemble evidence and draft cited replies. **The CA reviews, signs and files; the product never submits anything to an authority.**

**Status: Pre-prototype, planning.** As of 8 October 2026 there is no code. This repository holds the research, the handoff, the build plan and the work items. Ranked 3 of 14 opportunities, weighted score 3.70/5 ([report, Table 10](docs/research/00-full-research-report.md)).

Evidence labels used throughout: **Fact** is sourced and linked. **Assumption** or **estimate** is a working number to replace with pilot data. **Unverified** means background knowledge or a weak source.

## The problem in three numbers

| Number | What it shows | Source |
|---|---|---|
| **INR 74,782 cr** | Fake ITC detected in FY26 across 30,162 cases (detections, not recoveries) | [Jurishour](https://www.jurishour.in/gst/cgst-detects-fake-itc-fraud-fy26-unearthed/) |
| **2.1x** | Growth in detected fake ITC from INR 36,373 cr in FY24 to INR 74,782 cr in FY26, so scrutiny of ordinary buyers rises | [Jurishour](https://www.jurishour.in/gst/cgst-detects-fake-itc-fraud-fy26-unearthed/) |
| **98,967** | CA firms in India (159,557 members with practice certificates, Feb 2025): the buyer pool | [TaxConcept](https://taxconcept.net/icai/statistics-of-icai-members-students-firms-till-28th-february-2025/) (secondary source) |

ITC depends on the supplier's filing, not on the buyer's payment or the genuine purchase, so the buyer bears the cost of a supplier's failure ([Tally Solutions](https://tallysolutions.com/gst/gstr-2b-reconciliation-mismatches-how-to-fix/)). Existing tools reconcile but leave the action (chase the supplier, reverse credit, draft the reply) to a person ([research](docs/research/unsolved_smb_payments.md), Problem 3). No official count of 2B-mismatch notices to small taxpayers exists, so demand for notice work must be measured in discovery.

## How it works

1. **Ingest** 2B, IMS and the purchase register (Excel, JSON, Tally export). Files first; a licensed GST data provider later.
2. **Match deterministically**: exact, tolerance and fuzzy tiers. No model decides a number.
3. **Classify causes**: late supplier filing, not in 2B, value difference, GSTIN mismatch, likely blocked credit, reverse charge, missing IRN, IMS pending.
4. **Action list** per supplier, ranked by rupees at risk. The CA approves in bulk.
5. **Chase suppliers** with approved messages; track replies.
6. **Notice intake**: extract form, section, period, demand and deadline; set reminders.
7. **Evidence pack and cited draft reply**: law retrieved by effective date, figures computed by tools, every legal statement cited.
8. **CA edits, signs and files.** Every step is written to an append-only audit log.

Design principles: sell to CAs, not SMEs; retrieval and tools, not fine-tuning; human sign-off as a feature. See [docs/DECISIONS.md](docs/DECISIONS.md).

## Business hypothesis (all assumptions)

INR 250 per GSTIN per month (20-GSTIN minimum) plus INR 2,500 per notice. For a typical 40-GSTIN firm that is about INR 11,667 revenue and about INR 9,500 contribution a month ([HANDOFF section 8](docs/HANDOFF.md)). No price data exists for this segment; a price test at INR 150, 250 and 400 is planned for the pilot.

## Milestones

Dedicated team of one to three people starting Monday 12 October 2026. Full plan: [docs/PROTOTYPE_AND_MVP_PLAN.md](docs/PROTOTYPE_AND_MVP_PLAN.md).

| Milestone | Window | Due | Outcome | Issues |
|---|---|---|---|---|
| M0 Discovery & legal | 12-23 Oct 2026 | 23 Oct | 20 CA interviews, competitor teardown, 3-5 design partners, counsel engaged | 8 |
| M1 Prototype | 26-30 Oct 2026 | 30 Oct | Engine and drafter on real anonymised partner data; eval harness reports numbers | 10 |
| M2 MVP | 2 Nov-11 Dec 2026 | 11 Dec | Multi-tenant app; CA sign-off gate and audit log; a firm completes a monthly cycle unaided | 14 |
| M3 Pilot & decision | 14 Dec 2026-29 Jan 2027 | 29 Jan 2027 | 10-15 firms, two monthly cycles, price test, go / pivot / stop memo | 8 |

M1 is tight (one week after discovery) and may slip to 6 November if partner data arrives late. Details: [planning/milestones.md](planning/milestones.md).

## Repository map

| Path | Contents |
|---|---|
| [docs/HANDOFF.md](docs/HANDOFF.md) | Market case, product spec, architecture, legal, business model, GTM, risks, kill criteria |
| [docs/PROTOTYPE_AND_MVP_PLAN.md](docs/PROTOTYPE_AND_MVP_PLAN.md) | Week-by-week plan, prototype and MVP specs, technical design, evaluation plan, gates, cost |
| [docs/DECISIONS.md](docs/DECISIONS.md) | Initial architecture and product decision records (ADR-001 to 008) |
| [docs/research/](docs/research/README.md) | Research files behind the handoff, indexed by relevance |
| [planning/milestones.md](planning/milestones.md) | M0-M3 goals, due dates, exit criteria |
| [planning/issues.json](planning/issues.json) | 40 work items with labels and milestones, ready to import as GitHub issues |
| [CONTRIBUTING.md](CONTRIBUTING.md) | Branching, pull request checklist (including eval regression), no real client data |

Planned code layout (not yet created): `apps/api`, `apps/web`, `packages/recon`, `packages/importers`, `packages/notices`, `packages/law`, `tools/anonymise`, `evals/`. See the plan, section 7.

## Key risks

| Risk | Why it matters | Mitigation |
|---|---|---|
| Tally or Clear bundling | Tally shipped built-in AI in June 2026; competitive white space scored only 2/5 | Own the action and notice layer and the multi-client workflow; stay compatible, not dependent |
| Wrong citation or figure harms a client | Legal accuracy and liability | Deterministic numbers, cited drafts, mandatory CA sign-off, CI evals |
| Representation and unauthorised-practice concern | Rules are unverified background knowledge | Draft-only, CA files, counsel opinion before the pilot |
| Unproven demand | No official notice counts; no CA cost-per-notice data | Measure in M0 interviews; kill criteria in HANDOFF section 11 |
| Compressed prototype timeline | One week between discovery and M1 | Build on synthetic data from week 1; recruit partners on day 1 |
| Data protection | Client data in a third-party model | Anonymise at source; processing agreements and vendor terms before real data |

Full list: [HANDOFF section 12](docs/HANDOFF.md) and [plan section 12](docs/PROTOTYPE_AND_MVP_PLAN.md).

## Next actions (week of 12 October 2026)

- [ ] Book 8+ CA interviews and finalise the script
- [ ] Engage counsel and send the brief (representation, liability, DPDP)
- [ ] Appoint the part-time CA advisor
- [ ] Scaffold the repository and CI; build the synthetic 2B and register generator
- [ ] Draft data-sharing terms and the anonymisation protocol
- [ ] Shortlist 10 design-partner candidates

## Links

- Handoff: [docs/HANDOFF.md](docs/HANDOFF.md)
- Research index: [docs/research/README.md](docs/research/README.md)
- Key sources: [Jurishour](https://www.jurishour.in/gst/cgst-detects-fake-itc-fraud-fy26-unearthed/), [TaxGuru](https://taxguru.in/?p=1075080), [Tally Solutions](https://tallysolutions.com/gst/gstr-2b-reconciliation-mismatches-how-to-fix/), [ICAI benefits portal (Suvit)](https://bs.icai.org/suvit-2/), [Basis (BusinessWire)](https://www.businesswire.com/news/home/20260224020999/en/Basis-Raises-$100M-at-a-$1.15B-Valuation-as-Accounting-Firms-Adopt-End-to-End-Agents-Across-Accounting,-Tax,-and-Audit)

This is a drafting and reconciliation tool. It is not legal or tax advice, and responsibility for any reply to an authority stays with the signing CA.
