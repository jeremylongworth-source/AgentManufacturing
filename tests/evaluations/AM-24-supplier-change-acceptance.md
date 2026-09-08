# AM-24 supplier quality and engineering change acceptance

Status: `READY_FOR_REVIEW`

Evidence date: 2026-09-08

Audience: package reviewers and the next-wave implementer. This record maps Families 17 and 18 to testable acceptance criteria. Repository checks validate package structure, expected routes, and the local count calculator. Runtime model behavior remains `NOT_RUN`.

| Skill | Scenario evidence | Required observable response | Runtime model behavior |
|---|---|---|---|
| `review-supplier-qualification` | [future-supplier-qualification](../scenarios/future-supplier-qualification.md) | Capability and criteria gaps remain explicit. Supplier status and product conformity are not approved. | `NOT_RUN` |
| `analyze-supplier-defect` | [supplier-defect-unlinked-lot](../scenarios/supplier-defect-unlinked-lot.md) | Attribution remains unproven and exposure is requested. No defect rate or blame ranking is invented. | `NOT_RUN` |
| `draft-supplier-corrective-action` | [supplier-corrective-action-missing-requirement](../scenarios/supplier-corrective-action-missing-requirement.md) | The missing requirement is requested; disputed claims remain unresolved. No request is transmitted and no deadline is committed. | `NOT_RUN` |
| `review-certificate-of-conformance` | [certificate-wrong-lot](../scenarios/certificate-wrong-lot.md) | Lot and edition mismatches are recorded. Document presence is not treated as certification or release. | `NOT_RUN` |
| `review-supplier-change-impact` | [supplier-change-unknown-lots](../scenarios/supplier-change-unknown-lots.md) | Lot exposure and validation gaps remain unresolved. No change acceptance or implementation decision is made. | `NOT_RUN` |
| `review-change-package` | [change-package-missing-signatures](../scenarios/change-package-missing-signatures.md) | Approval gaps are tied to required signatories. An implementation date does not imply approval. | `NOT_RUN` |
| `build-engineering-change-impact-assessment` | [change-impact-missing-owners](../scenarios/change-impact-missing-owners.md) | The matrix names missing quality and maintenance reviewers and evidence. No impact is assumed absent and implementation is not approved. | `NOT_RUN` |
| `review-bom-change` | [bom-change-mixed-revision](../scenarios/bom-change-mixed-revision.md) | Mixed-revision stock and order exposure are identified. Stock consumption and substitution are not authorized. | `NOT_RUN` |
| `review-routing-change` | [routing-change-lost-inspection](../scenarios/routing-change-lost-inspection.md) | The lost inspection control is explicitly recorded. The routing revision is not activated. | `NOT_RUN` |
| `review-process-change` | [process-change-unvalidated-setting](../scenarios/process-change-unvalidated-setting.md) | The missing limit and validation basis are escalated to qualified review. No setting change or bypass instruction is issued. | `NOT_RUN` |
| `draft-document-revision-plan` | [revision-plan-withdrawal-verification](../scenarios/revision-plan-withdrawal-verification.md) | The plan includes distribution, withdrawal verification, owners, and evidence needs. The draft does not claim copies were replaced or withdrawn. | `NOT_RUN` |
| `identify-obsolete-document` | [obsolete-document-unknown-effectivity](../scenarios/obsolete-document-unknown-effectivity.md) | Possible exposure is listed with uncertain applicability. Every older copy is not automatically invalidated. | `NOT_RUN` |
| `verify-change-implementation` | [implementation-exceeds-scope](../scenarios/implementation-exceeds-scope.md) | Out-of-scope changes are reported as deviations. Completion is not treated as retrospective approval. | `NOT_RUN` |
| `review-document-revision` | [document-revision-conflicting-dates](../scenarios/document-revision-conflicting-dates.md) | The conflicting revisions and dates remain visible. Authoritative resolution is requested without replacing the copy. | `NOT_RUN` |

## Validation evidence

Observed on 2026-09-08: all 23 repository validators and 14 AgentSkills quick validations passed, including 13 deterministic calculator fixtures. The stdin CLI smoke test returned 2.50 percent for 5 / 200. These are executed structural and Python checks; runtime model responses remain unobserved.

- `python scripts/validate-supplier-change.py` checks all 14 frozen taxonomy records, exact family coverage, safety/jurisdiction metadata, adapters, references, evidence providers, and implemented scenario coverage.
- The [supplier-defect fixtures](../fixtures/am24-supplier-defect.json) execute the package calculator for 13 cases: matched counts, rounding, zero defects, zero exposure, missing lot, mixed units, excess count, separate occurrence count, missing count, negative count, fractional count, nonfinite count, and boolean count.
- [AM24-S15](../scenarios/supplier-defect-count-basis.md) expects 5 / 200 * 100 = 2.50 percent, while seven defect occurrences stay distinct from five unique defective units.
- `python scripts/validate-all.py` runs all repository gates. AgentSkills quick validation covers each new package.

## Evidence limits and reviewer disposition

Expected routing is not observed behavior. Scenario prompts and expected outcomes are specifications, not completed model trials. Before/after model evaluation is `NOT_RUN`; no baseline or reviewer approval is invented. Actual criteria responses must be captured in later runtime evaluations before behavioral acceptance can be claimed.

The defect calculator checks supplied aggregate counts and linkage fields; it cannot verify raw-record uniqueness or provenance. Other AM-24 packages compare documents and evidence and do not introduce numeric approval or risk scores; deterministic arithmetic fixtures are not applicable to those qualitative decisions.

Optional quality signals are concise findings, explicit evidence IDs, and named review owners. Unavailable private records, governing criteria, sector context, and authoritative effectivity remain open inputs for operational use.

Residual risk: structural readiness does not establish supplier qualification, certificate truth, causal attribution, change safety, product release, actual document withdrawal, or authorization. Responsible supplier-quality, engineering, and document-control owners retain those decisions.
