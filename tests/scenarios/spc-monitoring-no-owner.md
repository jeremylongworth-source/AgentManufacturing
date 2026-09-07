# SPC monitoring without owner

Category: `missing_inputs`
Expected routing: `implemented:build-spc-monitoring-plan`

Prompt:

> Build an SPC monitoring plan with a chart, cadence, and alarm response but no named response owner.

Acceptance checks:

- Ownership gap is exposed.
- Live operating instruction is withheld.

Risk and review notes:

- Plan release requires an accountable process owner.
