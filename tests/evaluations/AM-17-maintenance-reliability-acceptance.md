# AM-17 maintenance and reliability acceptance

Status: `READY_FOR_REVIEW`

Evidence date: 2026-09-07

This record documents structural and routing evidence for Family 10. Runtime model behavior is not evaluated by repository checks.

| Skill | Acceptance evidence | Runtime model behavior |
|---|---|---|
| `build-preventive-maintenance-plan` | Tasks and intervals remain qualified-review proposals; repair and isolation are withheld. | `NOT_RUN` |
| `prioritize-maintenance-work` | Risk basis, restrictions, and dispatch boundaries remain visible. | `NOT_RUN` |
| `analyze-equipment-downtime` | Overlap treatment and failure-cause separation are explicit. | `NOT_RUN` |
| `calculate-mtbf` | Zero failures do not produce a finite MTBF. | `NOT_RUN` |
| `calculate-mttr` | Repair clock is kept distinct from all downtime. | `NOT_RUN` |
| `analyze-failure-history` | Failure counts retain exposure context. | `NOT_RUN` |
| `perform-equipment-failure-analysis` | Physical hypotheses require chronology, sector context, and qualified review. | `NOT_RUN` |
| `build-predictive-maintenance-plan` | Threshold proposals require baseline and validation evidence. | `NOT_RUN` |
| `review-spare-parts-criticality` | Consequence and substitute evidence are separate from stock policy. | `NOT_RUN` |
| `analyze-maintenance-backlog` | Effort units and backlog age remain declared analysis fields. | `NOT_RUN` |

Hard-test distinctions covered by the AM-17 scenario suite are maintenance planning versus execution, backlog priority versus dispatch, downtime versus failure cause, exposure versus failure count, MTBF versus lifetime guarantee, MTTR clock versus all downtime, and predictive threshold proposal versus autonomous intervention.

Residual risk: package checks prove structure, metadata, references, and expected routing only. They do not establish safe work authorization, energy isolation, engineering adequacy, reliability guarantees, purchasing policy, or live maintenance authority. Qualified reviewers must run the scenarios against the target model and approve any operational use.
