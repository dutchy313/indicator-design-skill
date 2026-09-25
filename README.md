# Indicator Design Skill

**A Claude Agent Skill for designing, reviewing and quality-assuring monitoring, evaluation and learning (MEL) indicators for development, humanitarian and public-sector programmes.**

[![License: CC BY 4.0](https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg)](LICENSE)

Indicators are the sensory organs of a programme. Badly chosen ones do more than fail to inform: they distort behaviour, because implementers manage toward what is counted. This skill helps Claude produce indicator sets that are **few, honest, affordable to collect, and actually used in decisions**, rather than written to satisfy a donor template and then forgotten.

---

## What it does

With the skill installed, Claude works like an experienced MEL advisor. It can:

- **Design** an indicator set from a project description, theory of change or logframe
- **Review** an existing results framework and rewrite weak indicators, instead of only diagnosing them
- **Write indicator reference sheets** (PIRS / metadata) for given indicators
- **Fix** one or a few indicators quickly
- **Set or check baselines, targets and milestones** without inventing data

It follows a nine-step method:

1. Anchor every indicator in the results chain, never in the activity list
2. Use standard indicator banks before writing custom indicators (SDG, World Bank CRIs, DHS/MICS, WHO 100 Core, EU RF, USAID F, JMP, Washington Group and others)
3. Write indicators in a consistent grammar: unit + characteristic + population + qualifiers, with a defined numerator and denominator for every percentage
4. Test quality against SMART, CREAM, RACER or SPICED, plus a 10-criterion appraisal rubric
5. Write the metadata before the framework is signed off
6. Set baselines and targets honestly
7. Plan disaggregation at the design stage
8. Balance and prune the set
9. Plan for data quality, use and revision

The skill works for donor-funded programmes (World Bank, EU/DG INTPA, UN agencies, FCDO, USAID, GIZ, AfDB, IsDB, philanthropies), government sector plans and NGO proposals. It adopts the governing donor's vocabulary, for example "PDO indicator" for the World Bank or "PIRS" for USAID.

## When it triggers

Claude loads the skill automatically when you work on a results framework, logframe, theory of change, M&E plan, indicator matrix, PIRS, KPI set, baselines and targets, or a disaggregation or data collection plan. It also triggers on everyday phrasing such as:

> *"How do we measure this outcome?"*
> *"Our indicators aren't working."*
> *"Help me write a logframe for this proposal."*
> *"Review our M&E framework."*

## Repository contents

```
indicator-design-skill/
├── indicator-design/                  # The skill itself
│   ├── SKILL.md                       # Core method: context questions, 9-step workflow, output formats, worked examples, failure modes
│   ├── references/
│   │   ├── indicator-sources.md       # Standard indicator banks and guidance, by institution and sector
│   │   ├── quality-criteria.md        # SMART / CREAM / RACER / SPICED, appraisal rubric, DQA criteria, review order
│   │   └── measurement-methods.md     # Data sources, proxies, composite indices, sampling, attribution, cost
│   └── assets/
│       ├── indicator-reference-sheet.md   # PIRS / metadata template
│       └── indicator-matrix-template.csv  # Indicator matrix column set
├── agent/
│   └── custom-instructions.md         # System prompt for running the method as a standalone agent
├── scripts/
│   └── build_skill.py                 # Rebuilds indicator-design.skill from the folder above
├── indicator-design.skill             # Packaged skill, ready to upload
└── LICENSE
```

## Installation

### Claude apps (claude.ai, desktop)

1. Download [`indicator-design.skill`](indicator-design.skill).
2. In Claude, open **Settings → Capabilities → Skills** and upload the file.
3. Make sure the skill is switched on, then start a conversation about your programme's indicators.

### Claude Code

Copy the `indicator-design/` folder into your skills directory:

```bash
# Available in all your projects
cp -r indicator-design ~/.claude/skills/

# Or for a single project only
cp -r indicator-design .claude/skills/
```

### Claude Projects, custom GPTs and other agent builders

If your tool doesn't support Agent Skills, you can run the same method as a standalone agent:

1. Paste [`agent/custom-instructions.md`](agent/custom-instructions.md) into the agent's system prompt or custom instructions.
2. Upload these files as knowledge files, all at the same level (not in subfolders): `SKILL.md`, the three files in `references/` and the two files in `assets/`.

## Example

> **You:** We're writing an EU proposal for a three-year climate-smart agriculture programme in northern Ghana. Can you draft the outcome and output indicators?

Claude will first confirm the context: the governing framework, the results levels, who uses the data, existing data systems, the MEL budget and the reporting frequency. It then returns:

- a list of its assumptions
- a short results chain
- an indicator matrix, with EU Results Framework indicators used where they fit
- a quality scorecard for each indicator
- a note on measurement cost and data gaps

## Rebuilding the package

After editing anything in `indicator-design/`, regenerate the upload bundle:

```bash
python scripts/build_skill.py
```

## Contributing

Corrections and additions are welcome, especially updated wording for standard indicators and new sector indicator banks. Please open an issue or a pull request, and cite the official source for any standard indicator you add.

## Author

Written by the [Evidence and Intelligence team at Cloneshouse](https://www.cloneshouse.com/). The team brings together monitoring and evaluation specialists, software programmers and AI architects, with over 40 years of experience in development, humanitarian and public-sector programmes.

## License

This work is licensed under the [Creative Commons Attribution 4.0 International License](LICENSE) (CC BY 4.0). You may share and adapt it for any purpose, including commercially, as long as you give appropriate credit to Cloneshouse and indicate if you made changes.
