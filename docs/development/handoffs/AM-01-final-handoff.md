# Wave

AM-01: Domain contract. Closed 2026-09-06.

## Objective

Freeze the manufacturing definition, sector-neutral core, AgentLogistics interface, engineering boundaries, sector-specialization model, and Canadian jurisdiction model before candidate enumeration.

## Verdict

**READY** for the domain contract. AM-02 is next. AM-02 through AM-33 remain NOT_STARTED; no skill or runtime is implemented.

## Completion Token

`AGENTMANUFACTURING_AM_01_DOMAIN_CONTRACT_READY`

## Scope Completed

IN SCOPE: the six AM-01 domain decisions, concrete handoffs and boundary cases, narrow authoritative-source research, status updates, and this handoff.

- Defined manufacturing-support scope and discrete, batch/process, continuous, and mixed working contexts.
- Assigned responsibilities and output limits to all twenty planning families.
- Resolved the line-side/WIP overlap by decision ownership rather than location; specified nine logistics interfaces and a common evidence handoff.
- Defined engineering, operational, live-control, quality-release, and adjacent-business boundaries.
- Reconciled all eighteen distinct starter sector labels; separated industry, process, technology, operating-mode, and umbrella labels without creating packages.
- Defined composable jurisdiction flags, unknown/unsupported-context handling, and the distinction between product and workplace obligations.
- Reviewed twenty-one contract boundary cases and recorded their expected outcomes. These are manual design checks, not observed model behavior.

## Files Added

- [domain-contract.md](../../architecture/domain-contract.md)
- [scope-boundaries.md](../../architecture/scope-boundaries.md)
- [AM-01-final-handoff.md](AM-01-final-handoff.md)

## Files Modified

- [README.md](../../../README.md): current contract links and AM-02 next step.
- [ROADMAP.md](../../../ROADMAP.md): version 0.3, AM-01 ledger entry, and next target; original wave definitions retained.
- [domain-framework.md](../../architecture/domain-framework.md): explicit supersession note; preserved proposal below it.

The initial taxonomy and both AM-00 artifacts remain unchanged. No reference repository, credential configuration, remote content, or skill installation was modified.

## Research Performed

Read current repository state, the AM-00 handoff, the two starter architecture documents, and the AgentLogistics scope boundary. Opened three authoritative Canadian pages to support the definition and need for jurisdiction context. No standards editions, legal thresholds, or plant-specific applicability were adopted from starter prose.

## Sources

External sources accessed 2026-09-06:

- [Statistics Canada, NAICS 2022 manufacturing sector description](https://www23.statcan.gc.ca/imdb/p3VD.pl?CLV=2&CPV=31-33&CST=27012022&CVD=1381563&Function=getVD&MLV=6&TVD=1381557): transformation and related activity context; classification exceptions. Observed page modification date 2023-06-01.
- [Government of Canada, federally regulated workplaces](https://www.canada.ca/en/services/jobs/workplace/federally-regulated-industries.html): supports distinct federal workplace context. Observed page date 2026-01-30.
- [Government of Canada, occupational health and safety program](https://www.canada.ca/en/employment-social-development/programs/workplace-health-safety.html): identifies the program's federal scope. Observed page date 2024-07-02.

Local references: [AM-00 handoff](AM-00-final-handoff.md), [baseline audit](../AM-00-baseline-audit.md), roadmap, starter taxonomy/framework, and `D:\AgentLogistics\docs\architecture\scope-boundaries.md`. The AgentLogistics baseline checkout identity is recorded in AM-00; no new upstream verification is claimed.

AgentSkills applied: `issue-to-plan`, `acceptance-criteria-mapper`, `architecture-docs`, and `concise-technical-writing`. Existing QA principles informed proportional documentation checks; no new test framework was introduced.

## Validation Performed

| Criterion | Evidence / manual review | Result |
|---|---|---|
| Manufacturing definition and exclusions are explicit. | D-01; source attribution and workflow/classification distinction; BC-18. | PASS |
| Core responsibilities are bounded across all twenty families. | D-02 family table; universal methods separated from requirement overlays. | PASS |
| Logistics interfaces identify owners and exchange evidence. | D-03; nine interface rows, handoff fields, BC-03–09 and BC-21. | PASS |
| Engineering and operating authority cannot be inferred from a role or document. | D-04; nine hazard-topic boundaries; BC-10/11/17/19/20. | PASS |
| Every starter sector label has a disposition without bulk authoring. | D-05 eighteen-label reconciliation; BC-15/16. | PASS |
| Canadian model distinguishes context, applicability, and coverage. | D-06 composable flags; BC-01/12/13/14. | PASS |
| Missing units/evidence do not become invented final results. | D-02, handoff unknown fields, BC-02/06/08/09. | PASS |
| Documentation is internally consistent and bounded to AM-01. | Local links/anchors, ordered decisions/families/cases/waves, handoff sections, source links, change-scope and status checks. | PASS |

Compared README, ROADMAP, and the framework against pre-edit copies using `git diff --no-index`; read both new contracts and this handoff. The pre-edit copies are temporary local review aids, not required project dependencies. Git history remains unborn, so ordinary `git diff` alone cannot show the initial untracked content.

## Tests

The local Python documentation check passed with nine scoped Markdown files, 51 local links including two anchors, six domain decisions, twenty family rows, eighteen reconciled source-sector labels, twenty-one boundary cases, thirty-four ordered wave definitions, and fifteen handoff sections. The initial taxonomy SHA-256 remained unchanged; whitespace, AM-02 status, and the AM-10 gate checks passed.

Documentation integrity and scope checks passed. The twenty-one boundary cases were reviewed against the written contract. No model calls, live manufacturing operations, calculation fixture executions, regulator decisions, or automated behavioral passes are claimed. AM-09 must implement separate structural, deterministic, and observed-behavior evidence layers.

## Regulatory / Safety Review

The contract provides project-level review boundaries. It makes no plant-specific compliance, engineering, certification, personnel-qualification, product-release, or operating approval. Source-dependent conclusions require the relevant context and evidence. Federal product context does not classify workplace jurisdiction. The AM-10 mass-authoring gate remains in force.

## Known Limitations

- Canadian source research supports only the limited definition/context claims; full jurisdiction/source standards remain AM-04/07.
- The sector reconciliation assigns architectural categories, not a complete sector implementation plan or industry classification system.
- Detailed safety-class mechanics, fixture schemas, and metadata serialization remain later-wave work.
- Licence selection remains unresolved before distribution; no licence is inferred from AgentSkills or AgentLogistics.
- Local files remain uncommitted and unpushed, with no runtime, installed manufacturing skills, or behavior evaluation.

## Explicitly Not Completed

OUT OF SCOPE: AM-02 enumeration; AM-03 taxonomy freeze; detailed AM-04/05 rules; skill/source/calculation/validation standards; reference skills; professional skillsets; sector implementation; live integration; publication, commit, push, or release. No standards-edition assertion from the original proposal was verified or promoted into this contract.

## Recommended Next Wave

**AM-02: Master taxonomy draft.** Read this handoff, the domain contract, scope boundaries, original taxonomy, and current roadmap; inspect workspace truth before editing.

1. Enumerate candidate atomic tasks across all twenty families. Preserve traceability to the representative starter names; justify additions, splits, mergers, normalization, or deferrals.
2. For each record supply `name`, `family`, `tier`, `jurisdiction`, `safety_class`, `sector_dependency`, `inputs`, `outputs`, `dependencies`, and `priority`. Define provisional tier/priority values and how pending jurisdiction assessment is represented; do not imply AM-04 has been implemented.
3. Assign one primary responsibility and observable output per candidate. Separate a core method from a jurisdiction/sector requirement even when both are grouped under one discovery family.
4. Review likely overlap identified in B-03 of AM-00: value streams, bottlenecks, changeovers, process changes, document revisions, and WHMIS. Normalize the mixed-case SMED candidate explicitly and retain provenance.
5. Check that every candidate respects manufacturing/logistics and authority boundaries. Dependencies must resolve to candidates or clearly identified shared/overlay/external requirements; no installed runtime is implied.
6. Validate required fields, unique names, family coverage, dependency references, and explicit unresolved audit questions. Record the audited candidate count as an outcome, not a quota.
7. Produce `docs/development/handoffs/AM-02-final-handoff.md`, update the execution ledger, and award AM-02's token only when its draft-register acceptance criteria pass. Leave final atomicity audit, dependency ordering, and v1 taxonomy freeze to AM-03.

No mass authoring is authorized by taxonomy completion; the five-class reference-skill gate remains AM-10. Missing licence selection does not block drafting candidate records but must remain visible before skill distribution.
