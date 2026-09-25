# Choosing measurement methods, proxies and composite indicators

## 1. Match the data source to the indicator, then to the budget

| Source | Best for | Strengths | Watch for |
|---|---|---|---|
| Routine administrative / MIS (EMIS, HMIS/DHIS2, LMIS, registries) | Output and service-delivery coverage; anything needed frequently | Cheap, continuous, sustainable, strengthens national systems | Completeness and timeliness of reporting; denominator quality; incentive-driven over-reporting |
| Programme records | Outputs, participation, dose | Fully controlled | Only measures what the programme did; no counterfactual; poor for outcomes |
| National household surveys (DHS, MICS, LSMS, LFS, census) | Population outcomes and impact; equity analysis | Representative, comparable, free | Infrequent (3–5 years); rarely powered for programme geography |
| Bespoke programme survey (baseline/midline/endline) | Outcomes at programme scale | Tailored, powered for the target population | Expensive; sampling and attrition risk; dies with the programme |
| Sentinel / panel sites | Trend detection between survey rounds | Cheaper than full surveys; good for early warning | Not representative of the whole; site effects |
| Lot Quality Assurance Sampling (LQAS) | Fast supervisory judgement on coverage by small area | Very small samples; decision-oriented | Classifies, does not estimate precisely |
| Qualitative methods (KII, FGD, case protocol, MSC, outcome harvesting) | Mechanism, meaning, unintended effects, contested outcomes | Explains *why*; captures the unanticipated | Needs an explicit protocol and coding frame to be credible; resist forcing into a rate |
| Direct observation / spot checks | Quality of service, infrastructure functionality | High validity | Costly; observer effects |
| Secondary/administrative data from other actors | Context, impact-level trends | Free | Access, lag, definition mismatch |
| Remote sensing, mobile phone survey, call detail records, satellite imagery | Hard-to-access geographies; high-frequency proxies | Fast, safe, scalable | Coverage bias (phone ownership skews male, urban, wealthier); validation required |

Rule of thumb: measure **outputs from routine systems** and **outcomes from surveys**, and never promise annual survey-based outcome data unless the budget contains an annual survey.

## 2. Proxy indicators — when and how

Use a proxy when the direct measure is impossible, unaffordable, unsafe, or too slow to inform decisions. A proxy is legitimate only if you can state the assumed relationship between proxy and construct, and that assumption is plausible in the specific context.

Document three things whenever a proxy is used:
1. The construct actually of interest.
2. The assumed link ("household expenditure on X is assumed to track Y because …").
3. What would break the assumption, and how you would notice.

Classic examples: asset-based wealth index as a proxy for consumption poverty; mid-upper arm circumference as a rapid proxy for acute malnutrition; night-time lights as a proxy for local economic activity; textbook availability as a proxy for learning inputs. Each is defensible with stated assumptions and indefensible without them.

Avoid proxy stacking. A proxy for a proxy is a rumour.

## 3. Composite indicators and indices

Composites (readiness scores, capacity indices, empowerment indices, resilience scores) are attractive because they compress and communicate. They are also the easiest place to hide arbitrary judgement.

If you build one, document all of:
- **Conceptual framework** — what latent construct the index claims to represent.
- **Component selection** — why these variables, and what was excluded.
- **Normalisation** — min-max, z-score, distance to benchmark, or categorical scoring; state the reference points and whether they are fixed (allowing over-time comparison) or floating (which destroys it).
- **Weighting** — equal, expert-derived, participatory, or statistically derived. Equal weighting is a choice, not the absence of one.
- **Aggregation** — additive (compensatory: strength in one component offsets weakness in another) or geometric/multiplicative (non-compensatory). For constructs where a floor matters — a health system cannot compensate for zero staff with excellent supplies — do not use additive aggregation.
- **Missing data rule.**
- **Sensitivity analysis** — does the ranking change materially under alternative weights? If yes, report the range, not a point estimate.

The OECD/JRC *Handbook on Constructing Composite Indicators* is the standard reference for this and should be cited when a composite is proposed.

Simpler and often better: report the components alongside the index, or use a **milestone/ordinal scale** instead.

## 4. Milestone and scale indicators for qualitative progression

Where change is real but not naturally numeric — institutional capacity, policy reform, system maturity — define an ordered scale with observable, verifiable descriptors for each level. Then the indicator is "stage attained on the [named] scale", and the metadata carries the rubric.

Example structure for a policy reform indicator:
```
0  No draft policy exists
1  Draft prepared and technically reviewed
2  Draft subject to documented public consultation
3  Submitted for formal approval
4  Approved and gazetted
5  Implementation budget allocated and disbursed
```
This is honest about non-linearity, resists the "80% complete" fiction, and is verifiable from documents. Ensure the levels are mutually exclusive and evidence-anchored — otherwise it becomes an opinion survey with numbers on it.

## 5. Sampling and precision — the questions that determine cost

Before committing to a survey-based indicator, settle:
- The **unit of analysis** and the **sampling frame** (and whether the frame excludes exactly the people the programme targets — a frequent and serious problem).
- The **minimum detectable effect** you need to observe, which drives sample size far more than the confidence level does.
- Whether disaggregated estimates are required — powering for sex *and* disability *and* three geographies multiplies sample size and may be unaffordable. Decide the priority disaggregations rather than promising all of them.
- **Design effect** for cluster sampling; ignoring it under-powers the study.
- **Attrition** in panel designs.

If the required sample is unaffordable, change the indicator or the claim — do not run an underpowered study and report the result as if it were informative.

## 6. Attribution, contribution and what a target may claim

Match the strength of the claim to the design:
- **Output indicators** — attribution to the programme is reasonable.
- **Outcome indicators** — use contribution language unless there is a credible counterfactual (RCT, quasi-experimental design, or a well-specified contribution analysis).
- **Impact indicators** — these are almost always context indicators the programme contributes to alongside others. Report them for direction of travel, and be explicit that the target is a shared, not owned, ambition.

Where a target implies causal attribution, the design must support it. Otherwise state the target as programme contribution toward a trend, and record the assumption in the framework's assumptions column. This distinction is where most over-claiming in results reporting originates, and where independent evaluators look first.

## 7. Cost and burden estimation

For each indicator, estimate: instrument development, enumerator days, travel, data entry/cleaning, analysis, and the recurrent cost per round. Sum across the framework and compare against the MEL budget line. Present the total to the programme team before sign-off.

A framework whose measurement cost exceeds its MEL budget will be silently abandoned in year one — and the silence is worse than an honest reduction agreed at design.
