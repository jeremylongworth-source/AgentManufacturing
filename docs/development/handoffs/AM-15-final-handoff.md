# AM-15 final handoff: metrology, SPC and capability

Status: `READY`

Completion token: `AGENTMANUFACTURING_AM_15_PROCESS_QUALITY_READY`

Date: 2026-09-07

AM-15 adds sixteen bounded packages across Family 07 Metrology & Measurement Systems and Family 08 SPC & Capability. The packages cover method comparison, equipment and calibration evidence, measurement-system study structure, gauge control, traceability, control charts, signal review, special-cause screening, capability readiness, Cp/Cpk, Pp/Ppk, control-limit review, and SPC monitoring plans.

The hard boundaries are explicit: specification limits remain separate from control limits; resolution/precision remains separate from accuracy; and stability remains a prerequisite question rather than an implication of capability indices. Packages are analysis and review aids. They do not certify instruments, release product, adjust a process, or authorize live operations.

Evidence:

- [AM-15 acceptance record](../../tests/evaluations/AM-15-metrology-spc-acceptance.md)
- [Family 07 packages](../../skills/family-07-metrology/)
- [Family 08 packages](../../skills/family-08-spc-capability/)
- [AM-15 validator](../../scripts/validate-metrology-spc.py)
- [Routing manifest](../../tests/expected-routing.yaml) with 74 scenarios across all required categories and a future AM-16 documentation route

Validation command:

```powershell
python scripts/validate-all.py
python C:/Users/jerem/.codex/skills/.system/skill-creator/scripts/quick_validate.py skills/family-07-metrology skills/family-08-spc-capability
```

Residual risk remains reviewer-owned: repository validation does not prove runtime model behavior, standards applicability, measurement-system fitness, capability, certification, or operating authority. AM-16 is the next target: nonconformance, root-cause analysis, and CAPA.
