# Wave

AM-02: Master taxonomy draft. Closed 2026-09-06.

## Objective

Enumerate candidate atomic skills across all twenty families under the AM-01 contract, make their inputs/outputs and dependencies reviewable, and preserve every starter name's disposition before the AM-03 final audit.

## Verdict

**READY** for the AM-02 draft-register acceptance criteria. AM-03 is next. The taxonomy is not frozen, no skill is implemented, and AM-03 through AM-33 remain NOT_STARTED.

## Completion Token

`AGENTMANUFACTURING_AM_02_TAXONOMY_DRAFT_READY`

## Scope Completed

IN SCOPE: candidate enumeration, eleven required fields, provisional vocabulary, provenance, overlap/naming review, a focused data validator, a human-readable index, scope checks, and the next-wave handoff.

- Created 162 candidate records: 156 core methods and six Canadian overlays.
- Accounted for all 166 representative source names: 141 KEEP, twelve MERGE, twelve RENAME, one MOVE. Eight additions cover topics already stated in the starter proposal.
- Each record has explicit inputs, one primary output, a primary family, tier, pending/generic jurisdiction context, provisional safety class, conditional sector behavior, dependencies, and priority.
- Preserved the five AM-10 reference skills as P0 without advancing their implementation.
- Separated seven candidate reuse edges from seven named shared/evidence/authority/handoff requirements. No core candidate directly depends on a Canadian overlay.
- Recorded proposed overlap decisions, manual boundary review, and eight AM-03 audit themes.
- Added a validator for the draft data and its review index. This is not the future general skill or behavior validation framework.

## Files Added

- [candidate-register-v0.1.json](../../architecture/candidate-register-v0.1.json): canonical draft records, families, requirement registry, and source dispositions.
- [candidate-taxonomy-v0.1.md](../../architecture/candidate-taxonomy-v0.1.md): vocabulary, reasoning, boundaries, audit queue, and synchronized 162-row review index.
- [validate-candidate-register.py](../../../scripts/validate-candidate-register.py): read-only standard-library validator.
- [AM-02-final-handoff.md](AM-02-final-handoff.md): this handoff.

## Files Modified

- [master-taxonomy-v0.1.md](../../architecture/master-taxonomy-v0.1.md): draft pointers/status and record-contract wording; original representative lists and source narrative retained.
- [README.md](../../../README.md): draft entry points, validation command, and AM-03 next step.
- [ROADMAP.md](../../../ROADMAP.md): version 0.4, AM-02 closure, and AM-03 execution target; original wave definitions retained.

AM-00/01 artifacts, the domain contract, scope boundaries, and historical framework were not edited. No external reference project or Git/remote configuration was changed.

## Research Performed

Inspected current files, the AM-01 handoff and contract, and the original taxonomy. Extracted the 166 representative names from numbered family sections and reviewed their intended responsibility against the AM-01 boundaries. The eight additions derive from already listed production-planning and quantitative topics rather than new domain scope.

No current legal rule, standard edition, formula implementation, or vendor behavior is asserted by these records. External domain research was therefore not required for this catalogue wave. Requirement-specific candidates explicitly require future authoritative verification; historical threshold/edition claims were not copied into their inputs/outputs as facts.

## Sources

- [Original taxonomy](../../architecture/master-taxonomy-v0.1.md): original names, families, and topic coverage.
- [Domain contract](../../architecture/domain-contract.md) and [scope boundaries](../../architecture/scope-boundaries.md): core/overlay/authority decisions.
- [AM-01 handoff](AM-01-final-handoff.md) and [AM-00 audit](../AM-00-baseline-audit.md): required metadata, known overlap, and validation limitations.
- Local AgentSkills applied: `acceptance-criteria-mapper`, `architecture-docs`, and `concise-technical-writing`. No skill package was changed or installed.

## Validation Performed

| Criterion | Evidence | Result |
|---|---|---|
| All twenty families have candidate records. | Family counts validated against canonical records. | PASS |
| Every candidate contains the eleven required fields and review metadata. | Field, type, enum, nonempty-input, and primary-output checks. | PASS |
| Every original name is accounted for exactly once. | Source extraction compared with dispositions and reverse `source_names`; all 166 traced. | PASS |
| Added and changed responsibilities have reasons. | Eight addition rationales; proposed merge/rename/move decisions with target references. | PASS |
| Dependencies resolve and preserve core/overlay separation. | Seven candidate edges, requirement registry, no self/cyclic edges, no direct core-to-overlay dependency. | PASS |
| Draft statuses cannot claim implementation or legal applicability. | Register/candidate status checks and pending/generic context states. | PASS |
| Review index matches canonical records. | Exact name/family/tier/safety/priority/output row comparison. | PASS |
| Reference-class priorities remain aligned with AM-10. | Exactly five required P0 names; no skill files created. | PASS |
| Changed files preserve bounded scope and source definitions. | Snapshot comparison, local links, original wave/representative-list checks, final file inventory. | PASS |

The manual input/output review established proposed responsibility boundaries, not final per-candidate atomicity approval. The AM-03 audit queue includes broad/orchestrated outputs, inspection/measurement overlap, dependency completeness, metadata refinement, and remaining safety-topic coverage questions.

## Tests

Run from `D:\AgentMfg`:

```powershell
python scripts/validate-candidate-register.py
```

Result: 162 draft candidates and twenty families validated; all 166 source names traced. Sixteen in-memory negative mutation probes correctly rejected missing input fields, duplicate names, invalid naming, unknown candidate/requirement references, cycles, core-to-overlay dependencies, lost forward/reverse provenance, missing families, false readiness/applicability, unexplained additions, reference-priority drift, malformed safety metadata, and multiple primary outputs.

Two additional index probes rejected a missing delimiter and a stale candidate row. Mutation probes changed only temporary in-memory copies; the canonical register remained valid. These eighteen probes validate the checker’s failure behavior, not manufacturing calculations or agent responses.

Documentation checks and pre-edit snapshot comparisons passed: thirteen scoped files, 77 local Markdown links, four additions, three modified files, fifteen required handoff sections, and all thirty-four wave definitions. The source lists and original wave definitions remain intact; AM-00/01 contracts and handoffs are byte-for-byte unchanged. No empty package tree, general test suite, live system action, model evaluation, or dependency outside the Python standard library was introduced.

Canonical register SHA-256 at closure: `41e01db1c42f78981a1b84a5cbd38c9661678a695141e8853d9ca469a06653f5`.

## Regulatory / Safety Review

Canadian origin, labelling, WHMIS, and provincial-selection candidates are explicit overlays. Core safety/quality methods use supplied criteria and conditional evidence requirements; none asserts legal applicability from its label. All records preserve analysis/draft limits, and hazardous/engineering records include qualified-review boundaries. Logistics handoffs remain distinct from manufacturing decisions. No operating recipe, bypass, approval, certification, product release, or data-falsification capability was created.

## Known Limitations

- Atomicity, full domain coverage, safety classification, specialization scope, and dependency completeness require AM-03 audit; structure checks do not settle them.
- Only seven candidate reuse edges are proposed; many tasks accept equivalent supplied evidence. AM-03 must assess whether further reusable procedures are needed.
- Context flags and tiers are provisional; AM-04/05/06 own formal metadata and authoring decisions. Conditional sector flags are questions, not legal findings.
- Shared requirements are planned, not implemented assets. AM-01 authority limits already apply.
- There are no manufacturing skill packages, formula fixtures, actual routing results, or source-freshness evidence for regulated candidate outputs.
- Licence selection remains unresolved before distribution. Local files remain uncommitted and unpushed.

## Explicitly Not Completed

OUT OF SCOPE: AM-03 v1 freeze/index/dependency-map artifacts; AM-04/05 detailed jurisdiction/safety rules; authoring/source/calculation/behavior standards; the five reference skills; family skill authoring; sector packages; professional skillsets; publication, commit, push, or release. The AM-10 mass-authoring gate remains unchanged.

## Recommended Next Wave

**AM-03: Taxonomy audit and v1 freeze.** Read this handoff, the draft vocabulary/index and JSON, the source dispositions, the domain contract, scope boundaries, and current roadmap. Inspect current workspace truth before editing.

1. Audit each candidate against atomicity, duplicate responsibility, naming, dependency order, regulatory scope, engineering boundary, testability, and specialization need. Record an explicit per-candidate verdict and reason.
2. Resolve the eight audit themes in the draft review notes. Do not preserve 162 as a quota or accept a candidate merely because its required fields exist.
3. Document every retained, changed, merged, split, or deferred draft record with traceability. Confirm the reference classes required by AM-10 still have viable owners.
4. Freeze accepted names, families, tier definitions, boundaries, and dependency relationships into `docs/architecture/master-taxonomy-v1.md`, `docs/architecture/dependency-map.md`, and `docs/architecture/taxonomy-index.yaml` only when the audit supports them.
5. Check dependency ordering, index agreement, provenance, family coverage, naming, and the boundary decisions. Keep any future jurisdiction/safety metadata refinement explicitly assigned to AM-04/05.
6. Run the existing draft validator, adapt validation to the actual new artifacts as needed, review the diff, and produce `docs/development/handoffs/AM-03-final-handoff.md`. Award AM-03’s completion token only after its acceptance criteria pass.

Do not create skills during taxonomy freeze or bypass the AM-10 reference-skill gate. A frozen catalogue is not evidence of implemented behavior or production readiness.
