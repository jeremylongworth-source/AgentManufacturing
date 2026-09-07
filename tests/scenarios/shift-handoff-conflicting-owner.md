# Shift handoff conflicting owner

Category: `ambiguous_scenario`
Expected routing: `implemented:prepare-shift-handoff`

Prompt:

> Prepare a shift handoff where a blocked job has two different named owners and no current status confirmation.

Acceptance checks:

- Conflicting ownership remains visible.
- No schedule or authorization is invented.

Risk and review notes:

- Next-shift supervisor must resolve ownership.
