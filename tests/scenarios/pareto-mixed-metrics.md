# Pareto mixed metrics

Category: `unit_mismatch`
Expected routing: `implemented:perform-pareto-analysis`

Prompt:

> Rank nonconformance categories using a mixture of event counts, dollars, and downtime minutes in one total.

Acceptance checks:

- Incompatible metrics are not combined.
- A coherent denominator and metric are requested.

Risk and review notes:

- Ranking is not causal attribution.
