---
name: indicator-design
description: Design, select, define and quality-assure monitoring, evaluation and learning (MEL) indicators for development, humanitarian and public-sector programmes. Use this skill whenever the user is building or reviewing a results framework, logframe, theory of change, M&E plan, performance measurement framework, results chain, indicator matrix, indicator reference sheet / PIRS, KPI set, baseline or target values, disaggregation plan, or data collection plan — and also when they simply say things like "how do we measure this outcome", "what indicators should we use for this project", "our indicators aren't working", "help me write a logframe", "we need SMART indicators", or "review our M&E framework", even if the word "indicator" is never used. Applies to donor-funded work (World Bank, EU/DG INTPA, UN agencies, FCDO, USAID, GIZ, AfDB, IsDB, philanthropies), government sector plans, and NGO proposals alike.
---

# Indicator Design for Development Programmes

Indicators are the sensory organs of a programme. Badly chosen ones do not merely fail to inform — they actively distort behaviour, because implementers manage toward what is counted. The purpose of this skill is to produce indicator sets that are *few, honest, affordable to collect, and actually used in decisions*.

The most common failure in practice is not technical. It is that indicators are written to satisfy a donor template at proposal stage and then never used again. Design against that outcome from the first minute.

---

## Before drafting anything: establish the commissioning context

Ask the user for these, or make the assumption explicit in the output if the user cannot answer. Do not silently guess — the wrong assumption here invalidates everything downstream.

1. **Whose framework governs?** Donor (World Bank Results Framework, EU Results Framework / logframe, UNDAF-UNSDCF, USAID ADS 201, FCDO, Global Fund M&E Toolkit) or national (sector plan, NDP, SDG VNR reporting)? Each imposes vocabulary, mandatory core indicators, and reporting cadence.
2. **What level is being measured?** Activity/output, outcome, impact, or a corporate/portfolio roll-up. Roll-up requirements force standardisation; project-specific learning favours tailoring.
3. **Who decides what, using this data?** Name the decision and the decision-maker. An indicator with no named user is a candidate for deletion.
4. **What data systems already exist?** Routine administrative/MIS data (EMIS, HMIS/DHIS2), national surveys (DHS, MICS, LSMS, labour force survey), partner records, or nothing at all. Existing systems are almost always cheaper and more sustainable than bespoke surveys.
5. **What is the M&E budget and cycle?** A useful benchmark is roughly 3–10% of programme budget for MEL. If the indicator set implies more, it will not survive contact with implementation.
6. **What is the programme duration and reporting frequency?** Outcome-level change rarely moves annually; do not promise annual measurement of something that shifts over five years.

---

## The workflow

### Step 1 — Anchor every indicator in the results chain, never in the activity list

Start from the theory of change / results chain, not from "what can we count".

```
Inputs → Activities → Outputs → Outcomes → Impact
                  (control)  (influence)  (contribution only)
```

For each result statement, first ask: **"If this result were achieved, what would be observably different, for whom, and where would that difference show up?"** The answer is the indicator's raw material. Write the result statement first and lock it; the indicator measures the result, it does not restate it.

Attribution weakens as you climb. Outputs are attributable to the programme; outcomes are influenced; impact is contributed to alongside many actors. Say so explicitly in the framework rather than over-claiming — this is the single most frequent criticism in independent evaluations and Bank ICR reviews.

### Step 2 — Harvest before you invent

Bespoke indicators are expensive and non-comparable. Search established banks first and adopt or adapt. See `references/indicator-sources.md` for the catalogue (SDG global indicator framework, World Bank Corporate Results Indicators, MICS/DHS, WHO Global Reference List of 100 Core Health Indicators, EU Results Framework, USAID standard foreign assistance indicators, Global Fund, humanitarian indicator registry, Washington Group questions, and sector-specific sets).

Adopt a standard indicator unchanged when it fits — the comparability and the ready-made metadata are worth more than a marginally better custom wording. Adapt only when the standard indicator misses the programme's specific mechanism of change, and document what was changed and why.

### Step 3 — Write the indicator statement in disciplined grammar

An indicator is a **variable**, not a target and not a result statement. Use this structure:

```
[Unit of measurement] + [characteristic being measured] + [unit of analysis / population] + [qualifiers: place, time, condition]
```

**Good:** *Percentage of women aged 15–49 in target LGAs who report making decisions about their own healthcare, alone or jointly with their partner*

**Bad and why:**
| Draft | Problem |
|---|---|
| Improved access to clean water | Result statement, not a variable — contains direction |
| 500 boreholes drilled | Target, not an indicator — strip the value |
| Number of trainings held | Activity count masquerading as output; measures effort, not product |
| Number of farmers trained and adopting improved seed | Double-barrelled — split into two indicators |
| Level of community empowerment | Undefined construct — specify the observable manifestation and scale |
| Number of beneficiaries reached | "Reached" is undefined; define the threshold of contact that counts |

Rules that prevent most rework:
- No directional words (increased, improved, strengthened, reduced) in the indicator itself.
- No numbers in the indicator itself — numbers belong in baseline/target.
- One idea per indicator; if "and" or "/" appears, consider splitting.
- Prefer percentages/rates over raw counts at outcome level, and always define numerator and denominator.
- Name the population precisely; "beneficiaries" is not a population.

### Step 4 — Test quality against a recognised standard

Do not apply all frameworks at once. Choose by context and say which one you used:

- **SMART** (Specific, Measurable, Achievable, Relevant, Time-bound) — the common default; strongest when the target, not the indicator, is under review.
- **CREAM** (Clear, Relevant, Economic, Adequate, Monitorable) — Schiavo-Campo, adopted in Kusek & Rist's *Ten Steps to a Results-Based M&E System* (World Bank). Best for public-sector and government systems work because *Economic* forces the cost question.
- **RACER** (Relevant, Accepted, Credible, Easy to monitor, Robust) — EU Better Regulation Toolbox; strongest for policy and regulatory interventions. *Accepted* is the criterion others omit and the one that determines whether the indicator survives.
- **SPICED** (Subjective, Participatory, Interpreted, Cross-checked, Empowering, Diverse) — Roche/Oxfam; use alongside the above for participatory, rights-based, empowerment and social-accountability programming where SMART alone strips out what matters.

Then apply four blunt tests that catch what acronyms miss:

1. **The "so what" test.** If this number moved by 20 points, what would we *do* differently? No answer → delete the indicator.
2. **The gaming test.** How would a rational, pressured implementer make this number look good without producing the result? (Goodhart's law.) If gaming is cheap, add a quality qualifier or a counter-indicator.
3. **The two-analyst test.** Would two independent analysts, given the definition and raw data, compute the identical value? If not, the metadata is incomplete.
4. **The affordability test.** Estimate the cost and elapsed time of one measurement round. Multiply by the number of rounds. Is it defensible against the same money spent on delivery?

Full checklist and scoring rubric: `references/quality-criteria.md`.

### Step 5 — Write the metadata before the framework is signed off

An indicator without a reference sheet is an argument waiting to happen. Every indicator needs a definition sheet — variously called an *Indicator Reference Sheet*, *Performance Indicator Reference Sheet (PIRS)* (USAID ADS 201), *indicator passport*, or *metadata sheet* (SDG/UNSD).

Minimum fields: precise definition; numerator and denominator; unit of measure; disaggregation; data source; collection method and instrument; frequency; responsible person; baseline (value, date, source); targets and milestones; known limitations; rationale/link to result; date and version.

Use the template in `assets/indicator-reference-sheet.md`. Populate it during design, not after — the act of filling it in exposes half the flaws.

### Step 6 — Set baselines and targets honestly

- **No baseline, no target.** If a baseline cannot be established before implementation starts, record "TBD at baseline study, [date]" rather than inventing a number. A fabricated baseline is the most common audit finding.
- Derive targets from evidence: comparable programmes, historical trend in the same geography, coverage arithmetic (reach × expected conversion rate), or benchmark performance — and state which method you used.
- Set **milestones** for each reporting period, not just an end-line target; a single terminal target gives no early warning.
- Account for counterfactual trend: if the outcome is already rising 2% annually without the programme, a 3% target is nearly meaningless. Say what the target is net of.
- Distinguish cumulative from non-cumulative, and stock from flow. Ambiguity here corrupts more datasets than any other single error.

### Step 7 — Build in disaggregation deliberately

Aggregates conceal exactly the inequities most programmes exist to address, and the Leave No One Behind commitment makes this non-optional for SDG-aligned work.

Standard dimensions: sex; age band (aligned to the sector's convention — e.g. 0–5, 6–11, 12–14, 15–17, 18–24); disability (use the **Washington Group Short Set**, not self-declared status); geography/administrative unit; wealth quintile; urban/rural; displacement status; and context-relevant markers (ethnicity, language, caste, religion) — collected only where lawful, safe, and consented.

Decide disaggregation at design, because it drives sample size, instrument design and data system architecture. Retrofitting it is usually impossible. Where a dimension is sensitive or risks harm, record the decision not to collect it and the reasoning.

### Step 8 — Balance and prune the set

Apply portfolio-level judgement, not per-indicator judgement:

- **Coverage.** Is every significant result statement measured? Is anything measured twice?
- **Balance.** Quantitative and qualitative; results and process; intended and unintended effects; at least one indicator that could reveal *failure*, not only success.
- **Parsimony.** As a working heuristic, 1–2 indicators per output and 2–3 per outcome; a project-level framework beyond roughly 20–25 indicators is usually reporting theatre. Where a donor mandates more, separate a small "management dashboard" subset that is actually reviewed.
- **Cost.** Sum the measurement cost across the set and check it against the MEL budget.
- **Sustainability.** How many indicators rely on the programme's own bespoke data collection versus national systems? A high bespoke share means measurement dies when the programme does.

### Step 9 — Plan for data quality, use and revision

- Specify how each indicator will be verified: source documents, data quality assessments against **validity, reliability, precision, integrity and timeliness** (the USAID DQA criteria, widely reused), spot checks, third-party monitoring.
- Name the forum where the data is reviewed and the decision it feeds (quarterly review, steering committee, adaptive management pause-and-reflect).
- Version the framework. Indicators change; undocumented changes destroy trend comparability. Record every revision with date, rationale and approver.

---

## Output formats

### Indicator matrix (default deliverable)

| # | Results level | Result statement | Indicator | Unit | Disaggregation | Baseline (value, date) | Milestones | Target (value, date) | Data source | Method | Frequency | Responsible | Assumptions/risks |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|

Deliver as a spreadsheet when the user will maintain it, as a table in the document when it is for a proposal annex.

### Indicator reference sheet

One per indicator, using `assets/indicator-reference-sheet.md`.

### Review / critique deliverable

When the user asks for a review of an existing framework rather than new design, structure the response as: (1) overall verdict in two sentences; (2) issues ranked by severity, each with the specific indicator, the problem, and a rewritten version; (3) indicators recommended for deletion, with reasons; (4) gaps — results with no measurement; (5) quick wins versus structural fixes. Rewrite, don't just diagnose.

---

## Worked examples

**Output level — agriculture extension**
Result: *Smallholder farmers in target wards have access to climate-adapted advisory services.*
Indicator: *Number of smallholder farmers who have received at least three advisory contacts through the programme extension system in the preceding 12 months.*
Note the qualifiers: "at least three" defines the dose, "preceding 12 months" defines the window, and both together defeat the gaming strategy of counting a single SMS as reach.

**Outcome level — education**
Result: *Improved foundational literacy among lower-primary pupils.*
Indicator: *Percentage of Grade 3 pupils in supported schools reading at or above the national grade-level benchmark on the EGRA oral reading fluency subtask.*
Numerator: pupils scoring ≥ benchmark. Denominator: pupils assessed. Disaggregation: sex, disability (WG-CFM), school location, language of instruction. Note the reliance on an established instrument rather than a bespoke test.

**Outcome level — governance, qualitative**
Result: *Civil society organisations meaningfully influence local budget allocation.*
Indicator: *Number of documented instances in which a CSO submission resulted in a traceable amendment to the approved local government budget.*
Verified through a documented case protocol with defined evidence standards. This is a qualitative construct rendered countable without pretending it is a rate — and it is honest about what "meaningful" means: traceability to an amendment.

---

## Common failure modes to check for

- Output indicators dressed as outcomes (counting trainees, claiming capacity).
- Indicator inflation — 60 indicators, none reviewed.
- Percentages with undefined denominators.
- "Number of people reached" with no definition of reach.
- Composite indices built without documented weighting, normalisation or sensitivity testing.
- Targets copied from the proposal budget rather than derived from evidence.
- Indicators that require data the programme has no legal or practical means to obtain.
- Disaggregation promised in the framework but impossible in the instrument.
- Sensitive data (ethnicity, HIV status, displacement) collected without a protection assessment.
- No indicator anywhere in the set capable of registering bad news.

---

## Reference files

Read these as needed rather than upfront:

- `references/indicator-sources.md` — catalogue of standard indicator banks and the guidance documents behind them, by institution and sector. Read at Step 2, always.
- `references/quality-criteria.md` — full SMART/CREAM/RACER/SPICED definitions, the review rubric, and DQA criteria. Read at Step 4 and for any framework review.
- `references/measurement-methods.md` — choosing between routine/administrative data, surveys, sentinel sites, qualitative methods, indices and proxies; sampling and cost implications; when to use proxy indicators and how to justify them. Read when data sources are contested or budget-constrained.
- `assets/indicator-reference-sheet.md` — the metadata template.
- `assets/indicator-matrix-template.csv` — importable matrix skeleton.

## Author
This skill was authored by [The Evidence and Intelligence team at Cloneshouse](https://www.cloneshouse.com/), a team of monitoring and evaluation specialists, software programmers, and AI Architects with over 40 years of experience in development, humanitarian and public-sector programmes. They have designed and reviewed indicator sets for the World Bank, EU/DG INTPA, UN agencies, FCDO, USAID, GIZ, AfDB, IsDB, philanthropies, governments and NGOs.