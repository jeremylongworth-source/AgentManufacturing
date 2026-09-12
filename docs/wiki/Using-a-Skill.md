# Using a skill

A skill is a bounded instruction package. Read its SKILL.md, required evidence and relevant reference files before using it in your chosen agent host. Host loading and independent behavior have not been established by this repository's resolver.

## Worked example: takt time

Open [calculate-takt-time](https://github.com/jeremylongworth-source/AgentManufacturing/blob/main/skills/family-05-performance/calculate-takt-time/SKILL.md). Use this synthetic input:

- Period: one shift.
- Net available production time: 450 minutes, after explicitly accounted exclusions.
- Customer demand for the same shift: 300 units.

Takt time = net available production time / customer demand = 450 / 300 = **1.5 minutes per unit**, or **90 seconds per unit**.

Record the period, exclusions, numerator, denominator, units and assumptions alongside the result. This is an illustrative calculation, not a recorded independent model evaluation. It does not prove achievable cycle time, capacity, staffing adequacy or a safe machine setting.

## Missing or conflicting evidence

Do not replace gross time with net time silently. If exclusions or demand periods are unknown, request the missing evidence and keep the conclusion partial. Zero demand makes this ratio undefined; do not report zero takt time.

## Handoff

Provide the calculation, evidence gaps and the decision that needs qualified review. Separate supplied facts, assumptions and interpretations. For multi-skill work, reuse evidence only when definitions, periods, units and populations match. Continue with [[Architecture and Evidence|Architecture-and-Evidence]].
