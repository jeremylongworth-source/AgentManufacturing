# AM-20 workforce and shift acceptance

Status: `READY_FOR_REVIEW`

Evidence date: 2026-09-07

This record documents structural and routing evidence for Family 13. Runtime model behavior is not evaluated by repository checks.

| Skill | Acceptance evidence | Runtime model behavior |
|---|---|---|
| `build-manufacturing-skills-matrix` | Task/revision requirements are separated from qualification and assignment. | `NOT_RUN` |
| `build-shift-production-plan` | Shift allocation preserves readiness, capacity, and overtime boundaries. | `NOT_RUN` |
| `prepare-shift-handoff` | Current status and owners are transferred without implicit rescheduling. | `NOT_RUN` |
| `analyze-labor-productivity` | Output and labor exposure require a coherent population and units. | `NOT_RUN` |
| `identify-training-gap` | Revision conflicts remain evidence gaps, not automatic qualification decisions. | `NOT_RUN` |
| `review-operator-qualification-record` | Expiry and applicable-rule gaps block authorization claims. | `NOT_RUN` |
| `balance-workforce` | Skill infeasibility remains visible without assignment or overtime authorization. | `NOT_RUN` |
| `calculate-production-labor-requirement` | Labor standard revision and units remain explicit before staffing interpretation. | `NOT_RUN` |

Hard-test distinctions covered by the AM-20 scenario suite are skills evidence versus qualification, shift allocation versus horizon scheduling, handoff versus implicit rescheduling, productivity versus worker ranking, training gap versus qualification verdict, qualification record review versus authorization, workforce balance versus assignment, and labor requirement versus hiring/overtime approval.

Residual risk: package checks prove structure, metadata, references, and expected routing only. They do not establish qualification, labor policy, employment decisions, overtime approval, staffing sufficiency, or runtime model behavior. Authorized supervisors, HR, training, and safety owners remain responsible.
