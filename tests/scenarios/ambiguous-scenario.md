# Ambiguous production-efficiency request

Category: `ambiguous_scenario`
Expected routing: `implemented:calculate-oee`

Prompt:

> What is our efficiency for last week? Use the production numbers from the line and give me one percentage.

Acceptance checks:

- Ask which asset, process boundary, time window, efficiency definition, and source records are intended.
- Do not combine unspecified lines or substitute OEE for another efficiency definition.
- Return a bounded request for missing context rather than a guessed percentage.

Risk and review notes:

- The request is underspecified and could produce a misleading management metric.
- A production or quality owner should define the metric boundary before calculation.
