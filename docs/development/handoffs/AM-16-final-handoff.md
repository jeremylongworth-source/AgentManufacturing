# AM-16 final handoff: nonconformance, RCA and CAPA

Status: `READY`

Completion token: `AGENTMANUFACTURING_AM_16_CAPA_READY`

Date: 2026-09-07

AM-16 adds ten bounded Family 09 packages for issue triage, evidence-based nonconformance records, product-containment assessment, root-cause analysis, five-whys, fishbone, Pareto, corrective action, preventive action, and corrective-action effectiveness verification.

The packages preserve the boundaries between observation and interpretation, affected scope and disposition, correlation and root cause, preventive and corrective action, and implementation completion and effectiveness. Regulated containment remains a review and evidence aid; it does not release, move, quarantine, dispose of, or otherwise control product.

Evidence:

- [AM-16 acceptance record](../../tests/evaluations/AM-16-nonconformance-capa-acceptance.md)
- [Family 09 packages](../../skills/family-09-nonconformance-capa/)
- [AM-16 validator](../../scripts/validate-nonconformance-capa.py)
- [Routing manifest](../../tests/expected-routing.yaml) with 95 scenarios across all required categories and a future Family 11 safety route

Validation command:

```powershell
python scripts/validate-all.py
python C:/Users/jerem/.codex/skills/.system/skill-creator/scripts/quick_validate.py skills/family-09-nonconformance-capa/triage-nonconformance
```

Residual risk remains reviewer-owned: repository validation does not prove runtime model behavior, causal certainty, standards applicability, product disposition, CAPA approval, or closure authority. AM-17 is the next target: maintenance and reliability.
