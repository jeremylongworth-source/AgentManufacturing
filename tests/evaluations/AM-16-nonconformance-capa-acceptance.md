# AM-16 nonconformance, RCA and CAPA acceptance

Status: `READY_FOR_REVIEW`

Evidence date: 2026-09-07

This record documents structural and routing evidence for Family 09. Runtime model behavior is not evaluated by repository checks.

| Skill | Acceptance evidence | Runtime model behavior |
|---|---|---|
| `triage-nonconformance` | Observation is separated from requirement and disposition. | `NOT_RUN` |
| `document-nonconformance` | Record captures evidence, scope, and unknowns without closure. | `NOT_RUN` |
| `assess-product-containment` | Unknown genealogy remains an unresolved affected-scope boundary. | `NOT_RUN` |
| `perform-root-cause-analysis` | Correlation is separated from evidence-backed cause. | `NOT_RUN` |
| `perform-five-whys` | Unsupported blame links are challenged. | `NOT_RUN` |
| `build-fishbone-analysis` | Categories remain hypotheses, not causal proof. | `NOT_RUN` |
| `perform-pareto-analysis` | One coherent metric and denominator are required. | `NOT_RUN` |
| `build-corrective-action` | Action requires cause link, owner, and verification. | `NOT_RUN` |
| `build-preventive-action` | Prospective prevention is separated from reactive correction. | `NOT_RUN` |
| `verify-corrective-action-effectiveness` | Implementation completion is not effectiveness evidence. | `NOT_RUN` |

Hard-test distinctions covered by the AM-16 scenario suite are observation versus interpretation, containment scope versus disposition, correlation versus root cause, preventive versus corrective action, and implementation completion versus effectiveness.

Residual risk: package checks prove structure, metadata, references, and expected routing only. They do not establish product disposition, regulatory applicability, causal certainty, CAPA approval, or closure authority. Qualified reviewers must run the scenarios against the target model and approve any operational use.
