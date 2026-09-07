# AM-19 materials, BOM and traceability acceptance

Status: `READY_FOR_REVIEW`

Evidence date: 2026-09-07

This record documents structural and routing evidence for Family 12. Runtime model behavior is not evaluated by repository checks.

| Skill | Acceptance evidence | Runtime model behavior |
|---|---|---|
| `validate-bill-of-materials` | BOM identity, quantities, units, and effectivity are separated from design fitness. | `NOT_RUN` |
| `calculate-material-requirement` | Gross component need is separated from net need and warehouse replenishment. | `NOT_RUN` |
| `analyze-material-variance` | Planned-versus-actual comparison requires reconciled event states. | `NOT_RUN` |
| `trace-production-lot` | Missing genealogy remains an unknown exposure branch. | `NOT_RUN` |
| `build-product-genealogy` | Input/output graph construction stops at the manufacturing/warehouse interface. | `NOT_RUN` |
| `review-component-substitution` | Dimensional similarity is not treated as equivalence or approval. | `NOT_RUN` |
| `reconcile-material-consumption` | Unapproved adjustments remain unresolved events. | `NOT_RUN` |
| `identify-line-side-shortage` | Held material is not counted as usable supply. | `NOT_RUN` |
| `review-scrap-material-record` | Scrap record integrity is separated from disposition authority. | `NOT_RUN` |

Hard-test distinctions covered by the AM-19 scenario suite are BOM consistency versus design fitness, gross requirement versus warehouse replenishment, reconciled usage versus raw transactions, genealogy trace versus custody action, component similarity versus validated equivalence, and line-side shortage analysis versus material movement.

Residual risk: package checks prove structure, metadata, references, and expected routing only. They do not establish design adequacy, inventory truth, genealogy completeness, substitution approval, product disposition, warehouse control, or runtime model behavior. Qualified owners must review operational use.
