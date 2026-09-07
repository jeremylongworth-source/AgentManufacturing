# AM-15 metrology and SPC acceptance

Status: `READY_FOR_REVIEW`

Evidence date: 2026-09-07

This record documents structural and routing evidence for Families 07 and 08. Runtime model behavior is not evaluated by repository checks.

| Skill | Acceptance evidence | Runtime model behavior |
|---|---|---|
| `select-measurement-method` | Geometry and tolerance remain feasibility gates; no instrument approval. | `NOT_RUN` |
| `review-measurement-equipment` | Resolution is separated from accuracy and uncertainty. | `NOT_RUN` |
| `build-calibration-register` | Duplicate instrument identity remains visible. | `NOT_RUN` |
| `review-calibration-status` | Missing interval does not create a valid-until date. | `NOT_RUN` |
| `identify-out-of-calibration-risk` | Incomplete use history remains unknown exposure. | `NOT_RUN` |
| `analyze-measurement-system` | Missing operators/repetitions block a complete study. | `NOT_RUN` |
| `review-gauge-control` | Calibration evidence does not replace identity/status control. | `NOT_RUN` |
| `assess-measurement-traceability` | Missing reference chain blocks traceability claim. | `NOT_RUN` |
| `build-control-chart` | Missing order blocks signal chronology. | `NOT_RUN` |
| `interpret-control-chart` | Signal is separated from root cause. | `NOT_RUN` |
| `identify-special-cause-variation` | Post-signal event is not accepted as an earlier cause. | `NOT_RUN` |
| `review-capability-readiness` | Specification and control limits remain distinct. | `NOT_RUN` |
| `calculate-cp-cpk` | Overall sigma is not substituted for within-process sigma. | `NOT_RUN` |
| `calculate-pp-ppk` | Mixed specification populations are not combined. | `NOT_RUN` |
| `review-control-limits` | Unsupported baseline exclusions are flagged. | `NOT_RUN` |
| `build-spc-monitoring-plan` | Missing alarm owner remains an actionable gap. | `NOT_RUN` |

Hard-test distinctions covered by the AM-15 scenario suite are specification limit versus control limit, precision versus accuracy, and stable process versus capable process. Additional cases cover geometry reach, calibration identity/status, traceability, signal chronology, within versus overall variation, and monitoring ownership.

Residual risk: package checks prove structure, metadata, references, and expected routing only. They do not establish standards applicability, engineering adequacy, certification, process stability, capability, or live operating authority. Qualified reviewers must run the scenarios against the target model and approve any operational use.
