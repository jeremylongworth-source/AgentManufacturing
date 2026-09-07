# AM-13 process-engineering acceptance record

Status: `READY_FOR_REVIEW`

Evidence date: `2026-09-07`

## Scope

This record covers Families 04 and 05, including the existing OEE reference and eighteen process/industrial-engineering packages. It records structural, routing, and deterministic acceptance evidence; it is not a runtime model evaluation.

## Package evidence

| Skill | Class | Acceptance evidence | Runtime model behavior |
|---|---|---|---|
| `map-manufacturing-process` | process | rework loops and branches remain explicit | `NOT_RUN` |
| `build-process-routing` | engineering | missing work center remains unresolved and inactive | `NOT_RUN` |
| `identify-process-inputs-outputs` | process | unquantified stream is not assigned an invented balance | `NOT_RUN` |
| `review-process-parameter-control` | engineering | observed settings are separated from approved limits | `NOT_RUN` |
| `compare-process-alternatives` | engineering | absent quality validation blocks equivalence | `NOT_RUN` |
| `build-process-control-plan` | engineering | missing reaction owner blocks instruction | `NOT_RUN` |
| `calculate-takt-time` | quantitative | zero demand returns undefined/not applicable | `NOT_RUN` |
| `calculate-production-capacity` | quantitative | mixed product rates retain explicit mix assumptions | `NOT_RUN` |
| `analyze-cycle-time` | quantitative | downtime in sample remains disclosed | `NOT_RUN` |
| `balance-production-line` | planning | unsplittable task overload remains infeasible | `NOT_RUN` |
| `calculate-first-pass-yield` | quantitative | later rework passes remain outside first-pass numerator | `NOT_RUN` |
| `calculate-oee` | quantitative | AM-08 formula and invalid-input evidence remain linked | `NOT_RUN` |
| `analyze-changeover-loss` | quantitative | overlapping tasks are not double counted | `NOT_RUN` |
| `calculate-throughput` | quantitative | quantity and time periods must match | `NOT_RUN` |
| `calculate-capacity-utilization` | quantitative | missing rated-capacity denominator is visible | `NOT_RUN` |
| `calculate-rolled-throughput-yield` | quantitative | parallel routing is not multiplied as sequential | `NOT_RUN` |
| `calculate-scrap-rate` | quantitative | mass/count dimensions require conversion or separation | `NOT_RUN` |
| `calculate-rework-rate` | quantitative | unit and repeated-event counts remain distinct | `NOT_RUN` |

## Review disposition

The eighteen Family 04/05 packages are ready for reviewer inspection and bounded use after review. Engineering-boundary packages do not activate routings, design limits, certify controls, or approve process concepts. Quantitative packages do not create operating targets or production commitments.

## Residual risk

Runtime routing and model output behavior have not been observed. Engineering, standards, sector, site-safety, and source-freshness conclusions remain reviewer-owned. Project licensing remains `PENDING_PROJECT_GOVERNANCE`.
