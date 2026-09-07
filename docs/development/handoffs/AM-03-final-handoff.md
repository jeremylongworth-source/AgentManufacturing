# Wave

AM-03: Taxonomy audit and v1 freeze. Closed 2026-09-06.

## Objective

Audit every AM-02 candidate across the eight roadmap dimensions and freeze accepted names, responsibilities, tiers, provenance, and dependency relationships before jurisdiction formalization.

## Verdict

**READY** for the AM-03 catalogue freeze. AM-04 is next. No implemented-skill, operational, regulatory, or release-readiness verdict is issued. AM-04 through AM-33 remain NOT_STARTED.

## Completion Token

`AGENTMANUFACTURING_AM_03_MASTER_TAXONOMY_READY`

## Scope Completed

IN SCOPE: every-candidate taxonomy audit, resolution of the draft audit queue, accepted index, dependency semantics/order, future scenario specifications, validation, status updates, and this handoff.

- Audited all 162 draft records across atomicity, duplicate responsibility, naming, dependency order, regulatory scope, engineering boundary, testability, and specialization need.
- Accepted 159 records across twenty families: 153 core methods and six Canadian overlays.
- Recorded 156 RETAIN, two EXPAND_SCOPE, one RENAME_AND_EXPAND, and three MERGE draft dispositions. All 166 original source names remain routed to accepted targets.
- Merged incoming inspection planning into general inspection planning, supplier product conformity into renamed `review-product-conformity`, and supplier metric comparison into general quality KPI analysis. Supplier/stage evidence is preserved in the accepted inputs/outputs.
- Expanded the dependency review to 76 evidence-reuse edges with a valid topological order and no core-to-overlay dependencies. Equivalent supplied evidence is explicit, preserving bounded AM-10 implementation.
- Specified distinct future scenario expectations per audited draft record, marked `SPECIFIED_NOT_EXECUTED`.
- Assigned recognition/review ownership for all nine planned safety gate topics without inventing specialist operational capability.
- Preserved the AM-02 draft and existing domain contracts byte-for-byte.

## Files Added

- [master-taxonomy-v1.md](../../architecture/master-taxonomy-v1.md): freeze decisions and accepted catalogue.
- [dependency-map.md](../../architecture/dependency-map.md): edge semantics, shared requirements, ordering, and edge table.
- [taxonomy-index.yaml](../../architecture/taxonomy-index.yaml): canonical accepted records, audit evidence, source routes, and graph. YAML 1.2 expressed with JSON syntax for standard-library parsing.
- [taxonomy-audit-v1.md](../../architecture/taxonomy-audit-v1.md): dispositions, audit-queue resolutions, safety-topic matrix, and per-draft review projection.
- [validate-taxonomy.py](../../../scripts/validate-taxonomy.py): read-only index/audit/graph/projection validator.
- [AM-03-final-handoff.md](AM-03-final-handoff.md): this handoff.

## Files Modified

- [README.md](../../../README.md): v1 entry points, validation commands, current status and AM-04 next step.
- [ROADMAP.md](../../../ROADMAP.md): version 0.5, AM-03 ledger entry and next target. Original wave definitions and AM-10 gate preserved.

No AM-00/01/02 artifact, source narrative, reference repository, installed skill, Git configuration, or remote content was changed.

## Research Performed

Local review of all draft candidate inputs/outputs, earlier dispositions, AM-01 domain and boundary decisions, and the AM-02 audit queue. Responsibility and scenario judgments were authored per record; scripts serialize the decisions and check structure, not make independent domain acceptance decisions.

No current legal rule, standards edition, formula implementation, or vendor behavior was introduced. Jurisdiction and safety classes remain baseline review metadata pending their scheduled formalization. External regulatory/source research belongs to AM-04/07 and relevant implementation waves.

## Sources

- [AM-02 register](../../architecture/candidate-register-v0.1.json), preserved SHA-256 `41e01db1c42f78981a1b84a5cbd38c9661678a695141e8853d9ca469a06653f5`.
- [AM-02 notes](../../architecture/candidate-taxonomy-v0.1.md) and [handoff](AM-02-final-handoff.md).
- [AM-01 domain contract](../../architecture/domain-contract.md) and [scope boundaries](../../architecture/scope-boundaries.md).
- [Roadmap](../../../ROADMAP.md) and original-name provenance retained in the draft source dispositions.
- Local AgentSkills applied: `acceptance-criteria-mapper`, `architecture-docs`, and `concise-technical-writing`.

## Validation Performed

| Criterion | Evidence | Result |
|---|---|---|
| Every draft candidate is audited. | 162 unique audit records, each with all eight criteria, a disposition, evidence, and accepted target. | PASS |
| Accepted responsibilities and names are consistent. | 159 unique accepted records; three parameter-only duplicates merged; distinct retained decisions explained per record. | PASS |
| All source names remain traceable. | 166 original routes through preserved draft dispositions; forward/reverse accepted provenance checked. | PASS |
| Dependencies resolve and order correctly. | 76 evidence-reuse edges; all providers precede consumers; no self/cyclic or core-to-overlay dependencies. | PASS |
| Scope and authority limits remain explicit. | Per-record boundaries; pending classification status; shared safety-topic ownership; no implemented/legal verification claim. | PASS |
| Testability is specified without overstating evidence. | Concrete scenario expectations and `SPECIFIED_NOT_EXECUTED` statuses; no claimed model runs. | PASS |
| AM-10 reference classes remain viable. | Exactly five P0 names retained; equivalent supplied evidence avoids premature family authoring. | PASS |
| All freeze artifacts agree. | Accepted table, audit table, dependency sequence and edge table checked against the canonical index. | PASS |
| Wave scope and history are preserved. | Pre-edit snapshot comparison, local link checks, file inventory, and unchanged prior-wave artifact checks. | PASS |

The eight AM-02 audit themes are resolved in the audit report. Later work on actual source applicability, detailed safety mechanics, formulas, package authoring and behavior testing is explicitly assigned to later waves; it is not silently declared complete by this freeze.

## Tests

Run from `D:\AgentMfg`:

```powershell
python scripts/validate-candidate-register.py
python scripts/validate-taxonomy.py
```

Both checks passed. V1 validation covered 159 accepted records, 162 draft audits across eight criteria, 166 source routes, 76 ordered evidence-reuse edges, core isolation, P0 preservation, pending classifications, and all four document projections.

Twenty-four in-memory negative probes passed: missing audit/criterion, duplicate accepted name, broken original/draft/source provenance, missing inputs, unknown providers, self-cycle, core/overlay leakage, mandatory-runtime edge type, stale graph edge list, false implementation/test/applicability status, missing family, unresolved audit criterion, stale draft hash, P0 drift, four stale document projections, and duplicate serialized keys. These are validator checks, not manufacturing behavior tests.

Documentation and snapshot checks passed. Earlier contracts, draft data, handoffs, and validators remain unchanged. No skill packages, formula fixtures, model evaluations, production actions, or external Python dependencies were introduced.

## Regulatory / Safety Review

Catalogue acceptance does not verify a legal regime, permit, current standard, certification, or safe operating procedure. Baseline classifications retain `BASELINE_PENDING_AM04_AM05_FORMALIZATION`. Generic evidence recognition and qualified handoffs cover the nine planned safety gate topics at the stated scope; specialist operational evaluation is not claimed. No pressure/electrical/structural approval, guard bypass, live PLC/robot change, or product release is authorized.

## Known Limitations

- Taxonomy and scenario review is manual design evidence, not observed model behavior or independent external certification.
- AM-04/05 must formalize context and safety metadata and explicitly revise affected index records if needed.
- The evidence-reuse graph describes permissible method reuse; it is not an implemented orchestrator or compulsory package order.
- Shared methods, source standards, calculations and skills remain unimplemented. Sector packages remain AM-29 scope.
- Catalogue scope does not imply exhaustive coverage of all manufacturing industries or specialist disciplines.
- Licence selection remains unresolved; files remain local, uncommitted and unpushed.

## Explicitly Not Completed

OUT OF SCOPE: AM-04 Canadian source hierarchy and provincial extension details; AM-05 safety mechanics; AM-06–AM-09 standards/frameworks; AM-10 reference skills; family implementation; sector packages; professional skillsets; integration/adversarial model evaluation; public readiness, commit, push, or release.

## Recommended Next Wave

**AM-04: Canadian jurisdiction model.** Read this handoff, the v1 index/audit/dependency map, the AM-01 contract, and current roadmap; inspect workspace truth before changing files.

1. Formalize composable `CANADA_FEDERAL`, `PROVINCIAL_REQUIRED`, `SECTOR_REGULATED`, and `STANDARDS_DEPENDENT` flags, applicability states, required context fields, missing-context behavior, and evidence requirements. Preserve the distinction between product and workplace obligations.
2. Research current authoritative sources for the federal/provincial source hierarchy and initial Ontario, British Columbia, Alberta, and Quebec extension pattern. Record scope, official publisher, source/effective dates where available, access date, and unresolved applicability.
3. Define unsupported-province/territory/foreign-context handling without using Ontario or federal rules as a fallback. A missing jurisdiction must not block unrelated supported arithmetic.
4. Define overlay composition and conflict handling without assuming a standard or sector label proves compliance. Keep licensed-text access and freshness requirements visible; AM-07 formalizes the broader source standard.
5. Review the accepted index's pending classifications against the new model. If metadata changes are required, preserve the AM-02 draft, record the AM-04 amendment, and synchronize affected index/audit/projection records with appropriate validation.
6. Validate representative federal/product-versus-workplace, multi-province, unknown/unsupported, conflicting-source, and standards-dependent cases at the documented evidence level. Do not create regulatory skills or claim plant-specific legal determinations.
7. Produce `docs/development/handoffs/AM-04-final-handoff.md`, update the ledger, and award AM-04's token only when its source-backed model and extension-pattern criteria pass.

Proceed to AM-05 only after AM-04 closes. Mass authoring remains gated on AM-10.
