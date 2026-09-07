# AM-10 reference-skill acceptance record

Status: `READY_FOR_REVIEW`

Evidence date: `2026-09-07`

## Scope

This record covers the five AM-10 reference packages and their structural, routing, deterministic, and evidence-boundary checks. It is a readiness record; it is not a runtime model evaluation.

## Reference package evidence

| Skill | Class | Deterministic acceptance evidence | Runtime model behavior |
|---|---|---|---|
| `calculate-oee` | quantitative | AM-08 fixture `AM08-F05`; reject good count greater than total count | `NOT_RUN` |
| `build-production-plan` | planning | demand greater than supplied capacity produces partial allocation and explicit unmet demand | `NOT_RUN` |
| `triage-nonconformance` | quality | unknown defect scope remains unknown and routes to a next owner | `NOT_RUN` |
| `review-lockout-program` | hazardous operation | avoid-isolation request is refused and recorded as a program concern | `NOT_RUN` |
| `assess-made-in-canada-claim` | regulated overlay | incomplete cost/transformation evidence produces missing substantiation and no endorsement | `NOT_RUN` |

## Review disposition

The packages are ready for reviewer inspection and are eligible to block mass authoring until the explicit review disposition is recorded. No package is installed on a host. No live ERP/MES/PLC action, permit, certification, legal conclusion, product release, or customer commitment is implied.

## Residual risk

Runtime routing and model output behavior have not been observed. Jurisdictional, standards, sector, and source-freshness questions remain review-dependent. Project licensing remains `PENDING_PROJECT_GOVERNANCE`.
