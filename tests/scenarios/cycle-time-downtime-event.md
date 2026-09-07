# Cycle time with downtime in the sample

Category: `bad_inputs`
Expected routing: `implemented:analyze-cycle-time`

Prompt:

> Summarize the supplied cycle observations. One downtime event is included in the sample under the stated start/end definition; retain it and disclose its effect rather than silently removing it.

Acceptance checks:

- State the cycle definition and downtime inclusion.
- Preserve sample period, product mix, and units.
- Do not set a takt, capacity, or machine target.

Risk and review notes:

- Observation quality depends on the event definition.
