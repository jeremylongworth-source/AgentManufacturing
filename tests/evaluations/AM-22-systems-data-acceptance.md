# AM-22 manufacturing systems and data acceptance

Status: `READY_FOR_REVIEW`

Evidence date: 2026-09-07

This record documents structural and routing evidence for Family 15. Runtime model behavior is not evaluated by repository checks.

| Skill | Acceptance evidence | Runtime model behavior |
|---|---|---|
| `map-erp-mes-flow` | ERP/MES object, identity, ownership, and reconciliation gaps remain read-only findings. | `NOT_RUN` |
| `map-mes-machine-data-flow` | Machine-event lineage is separated from PLC/SCADA control changes. | `NOT_RUN` |
| `analyze-production-event-history` | Timestamp, identity, duplicate, and missing-event uncertainty is preserved. | `NOT_RUN` |
| `review-production-master-data` | Master-data defects are reported without activating live corrections. | `NOT_RUN` |
| `analyze-oee-data` | OEE inputs are reconciled before any calculation and overlapping states remain visible. | `NOT_RUN` |
| `diagnose-production-data-quality` | Dataset-quality defects retain scope, denominator, and remediation ownership. | `NOT_RUN` |
| `map-manufacturing-traceability-data` | Traceability lineage is distinguished from an executed genealogy or product release. | `NOT_RUN` |
| `build-manufacturing-kpi-model` | KPI definitions preserve lineage, denominators, units, exclusions, and conflicting bases. | `NOT_RUN` |

Hard-test distinctions covered by the AM-22 scenario suite are ERP/MES mapping versus live writes, machine data versus PLC/SCADA control, chronology versus history repair, master-data review versus activation, OEE input reconciliation versus OEE calculation, data-quality diagnosis versus record mutation, traceability architecture versus executed genealogy, and KPI definition versus published performance.

Residual risk: package checks prove structure, metadata, references, and expected routing only. They do not prove system completeness, data correctness, live integration, trace execution, production control safety, or runtime model behavior. Qualified system and process owners must review operational use.
