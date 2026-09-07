# AM-20 final handoff: workforce and shift operations

Status: `READY`

Completion token: `AGENTMANUFACTURING_AM_20_WORKFORCE_READY`

Date: 2026-09-07

AM-20 adds eight bounded Family 13 packages for skills matrices, shift production plans, shift handoffs, labor productivity, training gaps, operator qualification records, workforce balancing, and production labor requirements.

The packages preserve the boundaries between evidence and qualification, shift allocation and scheduling, handoff and rescheduling, productivity and worker ranking, workforce balance and assignment, and labor requirement and staffing approval. They do not certify operators, assign personnel, approve overtime, hire, or direct unsafe work.

Evidence:

- [AM-20 acceptance record](../../tests/evaluations/AM-20-workforce-acceptance.md)
- [Family 13 packages](../../skills/family-13-workforce-shift/)
- [AM-20 validator](../../scripts/validate-workforce-shift.py)
- [Routing manifest](../../tests/expected-routing.yaml) with 146 scenarios across all required categories and a future Family 17 supplier-quality route

Validation command:

```powershell
python scripts/validate-all.py
python C:/Users/jerem/.codex/skills/.system/skill-creator/scripts/quick_validate.py skills/family-13-workforce-shift/build-manufacturing-skills-matrix
```

Residual risk remains reviewer-owned: repository validation does not prove qualification, staffing sufficiency, employment policy, overtime approval, safety adequacy, or runtime model behavior. AM-21 through AM-23 are now closed; AM-24 is the next target: supplier quality and engineering change.
