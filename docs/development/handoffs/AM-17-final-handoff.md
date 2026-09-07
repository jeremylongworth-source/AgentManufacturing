# AM-17 final handoff: maintenance and reliability

Status: `READY`

Completion token: `AGENTMANUFACTURING_AM_17_RELIABILITY_READY`

Date: 2026-09-07

AM-17 adds ten bounded Family 10 packages for preventive-maintenance planning, backlog prioritization and analysis, downtime, MTBF, MTTR, failure history, equipment failure analysis, predictive maintenance planning, and spare-parts criticality.

The packages preserve the boundaries between planning and hazardous execution, ranking and dispatch, downtime and failure cause, exposure and raw failure count, MTBF and lifetime guarantee, MTTR and all downtime, and threshold proposals and autonomous intervention. Hazardous-operation and engineering-boundary packages are review aids only; they do not direct repair, isolation, live intervention, purchasing, or work authorization.

Evidence:

- [AM-17 acceptance record](../../tests/evaluations/AM-17-maintenance-reliability-acceptance.md)
- [Family 10 packages](../../skills/family-10-maintenance-reliability/)
- [AM-17 validator](../../scripts/validate-maintenance-reliability.py)
- [Routing manifest](../../tests/expected-routing.yaml) with 95 scenarios across all required categories and a future Family 11 safety route

Validation command:

```powershell
python scripts/validate-all.py
python C:/Users/jerem/.codex/skills/.system/skill-creator/scripts/quick_validate.py skills/family-10-maintenance-reliability/build-preventive-maintenance-plan
```

Residual risk remains reviewer-owned: repository validation does not prove runtime model behavior, safe work authorization, engineering adequacy, reliability guarantees, purchasing policy, or live maintenance authority. AM-18 is the next target: manufacturing safety.
