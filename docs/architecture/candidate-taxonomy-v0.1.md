# AM-02 candidate taxonomy v0.1

Status: **DRAFT_NOT_FROZEN**. AM-02 enumerates candidates; AM-03 must audit and freeze the accepted taxonomy. No skill packages are implemented.

The canonical candidate data is [candidate-register-v0.1.json](candidate-register-v0.1.json). This document explains its provisional vocabulary, scope decisions, and review index. The [domain contract](domain-contract.md) and [scope boundaries](scope-boundaries.md) govern every record. The [original taxonomy](master-taxonomy-v0.1.md) remains the provenance source, including historical claims that have not been promoted into requirements.

## Scope and outcome

AM-02 expands all twenty families, records all eleven required fields per candidate, accounts for every representative name, identifies dependencies, and prepares final audit questions. It does not freeze atomicity, author skills, formalize provincial law, reproduce standards, or implement the AM-09 behavior evaluation framework.

The resulting register has **162 candidates**: 156 `CORE` and six `CANADA_OVERLAY`. The 166 source names have 141 KEEP, twelve MERGE, twelve RENAME, and one MOVE dispositions. Eight additions address topics already present in the starter roadmap. No original name is silently dropped or deferred. The arithmetic is 166 source names minus twelve merged duplicates plus eight additions. The estimate of 220–280 eventual skills was not used as a target.

These are proposed catalogue decisions supported by input/output review. A structural validation pass does not establish that the entire manufacturing domain is exhaustively covered or that a model routes correctly.

## Record contract and provisional vocabulary

Each JSON candidate contains the roadmap's `name`, `family`, `tier`, `jurisdiction`, `safety_class`, `sector_dependency`, `inputs`, `outputs`, `dependencies`, and `priority`, plus a review boundary, source provenance, addition rationale, and draft status.

| Field | AM-02 meaning |
|---|---|
| `name` | Unique lowercase kebab-case candidate name; names describe analysis/drafting rather than unauthorized execution. |
| `family` | Primary responsibility owner, numbered 01–20. Cross-family use does not create a duplicate record. |
| `tier` | `CORE`: reusable manufacturing method or applicability-routing method. `CANADA_OVERLAY`: explicitly Canadian requirement review. Tier is an architectural layer, not skill proficiency or release priority. Sector packages are deferred to AM-29. |
| `jurisdiction.flags` | Zero or more AM-01 applicability questions. A flag is not a finding that a law governs. |
| `jurisdiction.assessment` | `GENERIC_METHOD_ONLY` for no preset applicability flags; `PENDING_CONTEXT` when context must be assessed for dependent conclusions. No record declares legal applicability verified. |
| `safety_class` | Provisional primary review class: `ROUTINE`, `REGULATED`, `HAZARDOUS_OPERATION`, or `ENGINEERING_OR_CERTIFICATION_BOUNDARY`. It is not permission to operate; actual context may add concerns under AM-01. AM-05 owns formal mechanics. |
| `sector_dependency` | `NONE_FOR_GENERIC_METHOD` or `CONDITIONAL_CONTEXT`; sector lists are empty because no specific sector package is a required dependency in this wave. Conditional context requires product/sector review when a conclusion depends on it, not a claim that every sector is regulated. |
| `inputs` | Concrete task data/evidence needed for the primary output. Unknown or conflicting required data yields only supported partial analysis. These are not invented operational facts. |
| `outputs` | One primary reviewable deliverable, with its essential distinctions or limits. Multiple fields within a deliverable do not imply multiple unrelated jobs. |
| `dependencies.candidates` | Another candidate's result may be needed for the stated workflow; equivalent supplied evidence can satisfy the input. These are proposed reuse edges, not installed runtime calls. |
| `dependencies.requirements` | References to named shared methods, authority boundaries, conditional evidence, or external handoffs. The requirement registry gives owner wave and activation condition; these are not missing skill folders. |
| `priority` | `P0`: exactly the five AM-10 reference skills. `P1`: proposed initial family coverage/foundational work. `P2`: subsequent depth within the owning family. Priority never overrides wave order or the AM-10 gate. |
| `boundary` | Analysis/draft-only limits, plus hazardous/engineering and logistics limits where relevant. The full AM-01 contract always applies, including when the class is routine. |
| `source_names` | Reverse links to every source name represented by this candidate. Empty only for a justified addition. |
| `addition_rationale` | Required justification for candidates without a starter name. |
| `status` | Always `CANDIDATE_DRAFT`; not implemented, tested as a skill, or frozen. |

The generic flag combination is intentionally conservative for evidence-sensitive work: `SECTOR_REGULATED` asks whether sector-specific requirements matter. It does not prove a sector obligation. Do not block unrelated arithmetic or evidence organization while waiting for jurisdiction/sector facts. AM-04/05 may refine this provisional metadata after the taxonomy audit.

## Dependencies and portability

There are seven explicit candidate reuse edges. Most candidates consume supplied records directly, so an empty candidate list does not mean the task needs no evidence or that shared methods are implemented. AM-03 must audit omitted, unnecessary, and incorrectly ordered reuse edges instead of assuming this graph is complete.

Seven requirement IDs keep missing implementation distinct from unresolved reference errors:

| ID | Responsibility and activation | Owner |
|---|---|---|
| `CALC` | Unit/formula/assumption/fixture contract for quantitative output. No formulas are implemented here. | AM-08 |
| `REVIEW` | Preserve existing AM-01 authority limits; detailed review gates remain planned. | AM-05 |
| `STANDARDS` | Verify applicability, edition, and access when a conclusion depends on a standard. | AM-07 |
| `JURIS` | Obtain actual workplace/activity context for jurisdiction-dependent conclusions. | AM-04 |
| `SOURCE` | Authoritative source verification and evidence method for source-dependent conclusions. | AM-07 |
| `FEDERAL` | Assess the Canadian federal requirement in question without assigning workplace jurisdiction. | AM-04 |
| `LOGISTICS` | Supplied movement/custody/warehouse evidence or the existing AM-01 handoff; no automatic integration. | AM-19 |

`PLANNED_REQUIREMENT` means later implementation/formalization is still needed. It does not suspend the already applicable AM-01 boundaries. A generic core method must not directly depend on a Canadian overlay candidate. Conditional evidence requirements do not force every invocation to load an overlay.

## Proposed overlap and naming decisions

Every original name has a reason and target in `source_dispositions` in the JSON. The important responsibility distinctions are:

| Group | Proposed decision and rationale |
|---|---|
| Operation and mode classification | Merge `classify-discrete-vs-process-production` into `classify-manufacturing-operation`; mode is part of the same decision. |
| Flow / value stream | Merge `map-production-flow` into Family 04 `map-manufacturing-process`; merge `map-manufacturing-value-stream` into Family 14 `build-value-stream-map`. Process sequence differs from value-stream time/information analysis. |
| Constraints / bottlenecks | Rename the constraints inventory to `analyze-production-constraints` and merge `analyze-process-constraint` there. Retain measured bottleneck identification as a distinct evidence-ranked finding. |
| Changeovers | One loss measurement owner, `analyze-changeover-loss`; `plan-production-changeover` schedules known work, and normalized `build-smed-improvement-plan` proposes reviewed improvements. |
| Process / engineering change | Merge process-change assessment into `review-process-change`. `review-change-package` checks completeness; the impact assessment evaluates affected responsibilities. BOM, routing, and supplier changes retain distinct input scopes for AM-03 audit. |
| Controlled documents / training | Move revision comparison to Family 18 as `review-document-revision`. Plan document activation with `draft-document-revision-plan`. Move standard-work training gaps to Family 13; merge generic training readiness into qualification-record review. |
| Capability / stability | Replace the generic capability calculation name with `review-capability-readiness`; retain separate within/overall variation calculations. Merge process stability interpretation into chart interpretation; special-cause investigation remains hypothesis review. |
| Quality gaps | Merge `identify-quality-control-gap` into `audit-quality-process`; the output is an evidence-linked process gap report, not a certification. |
| Material/environment measurements | Merge material-yield-loss analysis into material variance. Reuse `measure-improvement-result` for environmental before/after metrics while keeping environmental applicability separate. |
| Supplier authority | Use `review-supplier-qualification` and `draft-supplier-corrective-action`; neither approves a supplier nor sends a message. |
| Labor estimate | Move `forecast-labor-requirement` to Family 13 as `calculate-production-labor-requirement`, using supplied workload and time standards. |
| WHMIS | Move readiness from Family 11 to a Family 20 Canadian overlay. Rename obligation review to `assess-whmis-applicability`, whose output informs readiness review. Generic hazard and program review stay in core. |

Eight additions make existing topic coverage explicit: production lead time, production order readiness, lot-size comparison, throughput, capacity utilization, rolled throughput yield, scrap rate, and rework rate. Their individual rationales are in the register. None adds a new industry, legal rule, or live operating workflow.

## Reference and boundary review

These are manual candidate-design checks, not prompts executed against a model:

| Case | Expected candidate / boundary |
|---|---|
| Unit-consistent OEE inputs with no province | `calculate-oee`; core arithmetic does not require a province. Unit/definition validation belongs to later fixtures. |
| Demand exceeds capacity and material evidence is incomplete | `build-production-plan`; expose unmet demand and missing constraints, do not invent feasibility or release orders. |
| Observed defect with unknown lot exposure | `triage-nonconformance`; record uncertainty and next owner without inventing cause or disposition. |
| Review lockout program documents | `review-lockout-program`; program evidence review, conditional jurisdiction/standard sourcing, no equipment-specific isolation or restart steps. |
| Assess proposed non-food Canadian-origin wording | `assess-made-in-canada-claim`; Canadian overlay, evidence and current-source review, no published claim or assumed threshold. |
| Receipt shortage and dimension failure in the same lot | Logistics owns count/custody discrepancy; manufacturing incoming inspection and supplier conformity candidates own manufacturing-quality evidence. |
| Trace a component to a shipped customer lot | Production genealogy/trace candidates produce manufacturing evidence; `LOGISTICS` requests the custody/shipment segment without claiming integration occurred. |
| Work order asks to change the live PLC | Core system-data and change-review candidates provide read-only evidence/review packages; no control-write candidate is introduced. |
| Capability request includes specification limits as control limits | `review-capability-readiness` / `review-control-limits` flag the distinction before a supported calculation. |
| Standards-dependent supplier certificate lacks an edition | Certificate review identifies the missing applicability/edition evidence; no certification conclusion. |

## AM-03 audit queue

1. Audit every record for atomicity, naming, engineering/regulatory scope, testability, and specialization need. Input/output uniqueness is necessary but not enough.
2. Review broad deliverables such as root-cause analysis, production planning, KPI analysis, and engineering-change impacts for orchestration versus atomic responsibility. Keep the five reference names aligned with AM-10 unless an explicit roadmap revision is justified.
3. Recheck inspection/supplier-conformance/certificate overlap and measurement-system versus instrument suitability. Preserve distinct decisions only where evidence and output justify them.
4. Audit all seven candidate edges and potential reuse not captured by supplied-data inputs. Freeze the dependency map only after this review.
5. Revisit provisional safety classes and conditional jurisdiction/sector flags; retain unresolved applicability as such. AM-04/05 remain responsible for formal context/class mechanics.
6. Assess coverage gaps beyond representative names, including whether electrical, pressure, confined-space, hot-work, structural, and chemical program review need their own candidates or shared AM-05 gates. All are already bounded by AM-01; no operational skill is authorized by a taxonomy gap.
7. Decide how reference-class evidence and scenario requirements attach to accepted candidates under AM-06/09. Package validation and actual response evaluation remain separate.
8. Produce `master-taxonomy-v1.md`, `dependency-map.md`, and `taxonomy-index.yaml` only after the final audit. Do not treat this JSON filename or AM-02 token as a v1 freeze.

## Validation and editing

Run from the repository root:

```powershell
python scripts/validate-candidate-register.py
```

The validator checks fields, enums, family counts, source-name coverage in both directions, addition rationale, dependency references/cycles, core/overlay isolation, draft status, and the five reference priorities. It also checks that the review index below agrees with canonical JSON. Edit the JSON and corresponding index rows together; preserve source provenance for proposed changes.

It does not prove safe model behavior, formula correctness, complete domain coverage, legal applicability, or final atomicity. Sixteen negative mutation probes exercised missing inputs, duplicate/invalid names, bad references, cycles, overlay leakage, provenance loss, missing families, false readiness/applicability, unjustified additions, reference-priority drift, malformed metadata, and multiple primary outputs. Evidence and limits are recorded in the [AM-02 handoff](../development/handoffs/AM-02-final-handoff.md).

## Review index

The rows below are a projection of the JSON's name, family, tier, safety class, priority, and primary output. Required inputs, conditional metadata, boundaries, dependencies, and provenance remain in the canonical register.

<!-- candidate-index:start -->
| Candidate | Family | Tier | Safety class | Priority | Primary output |
|---|---|---|---|---|---|
| classify-manufacturing-operation | 01 | CORE | ROUTINE | P1 | Operational classification with manufacturing/non-manufacturing boundary and unresolved facts |
| analyze-product-process-profile | 01 | CORE | ROUTINE | P2 | Product/process fit profile with evidence gaps |
| analyze-production-constraints | 01 | CORE | ROUTINE | P1 | Constraint register distinguishing hypotheses from measured bottlenecks |
| identify-manufacturing-bottleneck | 01 | CORE | ROUTINE | P1 | Evidence-ranked bottleneck finding with sensitivity to data gaps |
| build-production-plan | 02 | CORE | ROUTINE | P0 | Feasible production-plan draft with unmet demand and explicit constraints |
| calculate-production-requirement | 02 | CORE | ROUTINE | P1 | Net production quantity by product with unit basis and unresolved assumptions |
| sequence-production-orders | 02 | CORE | ROUTINE | P1 | Proposed order sequence with conflicts and constraint violations |
| analyze-schedule-adherence | 02 | CORE | ROUTINE | P2 | Schedule-adherence calculation with lateness and exclusion rules |
| identify-capacity-shortfall | 02 | CORE | ROUTINE | P1 | Capacity-gap table by constrained operation |
| plan-production-changeover | 02 | CORE | ROUTINE | P1 | Changeover scheduling window and readiness checklist without operating instructions |
| compare-production-scenarios | 02 | CORE | ROUTINE | P2 | Comparable scenario tradeoff table with rejected infeasible options |
| calculate-production-lead-time | 02 | CORE | ROUTINE | P1 | Production lead-time estimate separating measured and assumed components |
| review-production-order-readiness | 02 | CORE | ROUTINE | P1 | Order readiness gap list without releasing the order |
| compare-production-lot-sizes | 02 | CORE | ROUTINE | P2 | Lot-size comparison with capacity and inventory consequences |
| draft-work-instruction | 03 | CORE | ROUTINE | P1 | Draft controlled work instruction with unresolved process details |
| review-work-instruction | 03 | CORE | ROUTINE | P1 | Instruction defect list tied to ambiguous missing or conflicting steps |
| build-standard-work | 03 | CORE | ROUTINE | P1 | Standard-work draft relating sequence time and allowed WIP |
| analyze-standard-work-deviation | 03 | CORE | ROUTINE | P2 | Deviation analysis separating instruction gaps from execution variance |
| review-operator-checklist | 03 | CORE | ROUTINE | P2 | Checklist coverage and exception-handling findings |
| map-manufacturing-process | 04 | CORE | ROUTINE | P1 | Process map with defined start end and decision points |
| build-process-routing | 04 | CORE | ENGINEERING_OR_CERTIFICATION_BOUNDARY | P1 | Draft product routing with review gaps and no system activation |
| identify-process-inputs-outputs | 04 | CORE | ROUTINE | P1 | Process input/output inventory with units and unverified streams |
| review-process-parameter-control | 04 | CORE | ENGINEERING_OR_CERTIFICATION_BOUNDARY | P1 | Parameter-control evidence gaps without proposing new operating limits |
| compare-process-alternatives | 04 | CORE | ENGINEERING_OR_CERTIFICATION_BOUNDARY | P2 | Process alternative assessment for engineering review |
| build-process-control-plan | 04 | CORE | ENGINEERING_OR_CERTIFICATION_BOUNDARY | P1 | Draft control plan linking characteristics to supplied controls and review owners |
| calculate-takt-time | 05 | CORE | ROUTINE | P1 | Takt result with time basis and missing or zero-demand handling |
| calculate-production-capacity | 05 | CORE | ROUTINE | P1 | Capacity estimate with units assumptions and limiting resource |
| analyze-cycle-time | 05 | CORE | ROUTINE | P1 | Cycle-time distribution summary and observation-quality limitations |
| balance-production-line | 05 | CORE | ROUTINE | P2 | Line-balance proposal with infeasible tasks and workload variation |
| calculate-first-pass-yield | 05 | CORE | ROUTINE | P1 | First-pass yield with numerator denominator and rework distinction |
| calculate-oee | 05 | CORE | ROUTINE | P0 | OEE and component results with definition checks and impossible-value flags |
| analyze-changeover-loss | 05 | CORE | ROUTINE | P1 | Changeover-loss breakdown distinguishing measurement from improvement proposals |
| calculate-throughput | 05 | CORE | ROUTINE | P1 | Throughput rate with explicit quantity and time denominator |
| calculate-capacity-utilization | 05 | CORE | ROUTINE | P2 | Utilization result with capacity definition and non-comparable inputs flagged |
| calculate-rolled-throughput-yield | 05 | CORE | ROUTINE | P2 | Rolled yield estimate with operation basis and assumption limits |
| calculate-scrap-rate | 05 | CORE | ROUTINE | P1 | Scrap-rate result with denominator definition and no unit mixing |
| calculate-rework-rate | 05 | CORE | ROUTINE | P2 | Rework-rate result distinguishing units from repeat rework events |
| review-quality-requirement | 06 | CORE | REGULATED | P1 | Quality-requirement interpretation gaps and review questions |
| build-inspection-plan | 06 | CORE | REGULATED | P1 | Draft inspection plan with acceptance and sampling evidence gaps |
| review-production-conformity | 06 | CORE | REGULATED | P1 | Conformity evidence assessment with unassessed or conflicting requirements |
| review-quality-record | 06 | CORE | ROUTINE | P1 | Record completeness and integrity findings preserving original values |
| prepare-quality-release-package | 06 | CORE | REGULATED | P1 | Release evidence package with unresolved holds for authorized disposition |
| audit-quality-process | 06 | CORE | REGULATED | P2 | Evidence-linked process gap report without certification or audit approval |
| analyze-quality-kpis | 06 | CORE | ROUTINE | P2 | Quality performance analysis with definition and comparability gaps |
| select-measurement-method | 07 | CORE | ENGINEERING_OR_CERTIFICATION_BOUNDARY | P1 | Measurement-method comparison for qualified selection |
| review-measurement-equipment | 07 | CORE | ENGINEERING_OR_CERTIFICATION_BOUNDARY | P1 | Instrument suitability gaps without certifying measurement fitness |
| build-calibration-register | 07 | CORE | ROUTINE | P1 | Calibration register with missing and conflicting records identified |
| review-calibration-status | 07 | CORE | REGULATED | P1 | Calibration-status review with unsupported status claims flagged |
| identify-out-of-calibration-risk | 07 | CORE | REGULATED | P1 | Potentially affected product/measurement exposure list for review |
| analyze-measurement-system | 07 | CORE | ENGINEERING_OR_CERTIFICATION_BOUNDARY | P2 | Measurement-system study assessment with uncertainty and design limitations |
| review-gauge-control | 07 | CORE | REGULATED | P2 | Gauge-control gap report distinct from calibration status |
| assess-measurement-traceability | 07 | CORE | REGULATED | P2 | Traceability-chain assessment with missing links and no accreditation claim |
| build-control-chart | 08 | CORE | ROUTINE | P1 | Draft control chart with calculated limits and assumptions |
| interpret-control-chart | 08 | CORE | ROUTINE | P1 | Signal and stability interpretation without equating signals to proven causes |
| identify-special-cause-variation | 08 | CORE | ROUTINE | P2 | Evidence-ranked special-cause hypotheses and verification needs |
| review-capability-readiness | 08 | CORE | ROUTINE | P1 | Capability-method suitability and missing-prerequisite assessment |
| calculate-cp-cpk | 08 | CORE | ROUTINE | P1 | Cp/Cpk calculations with applicability caveats and no process approval |
| calculate-pp-ppk | 08 | CORE | ROUTINE | P2 | Pp/Ppk calculations with overall-variation basis distinguished from Cp/Cpk |
| review-control-limits | 08 | CORE | ROUTINE | P1 | Control-limit review identifying calculation and specification-limit confusion |
| build-spc-monitoring-plan | 08 | CORE | ROUTINE | P2 | SPC monitoring-plan draft with data and response responsibilities |
| triage-nonconformance | 09 | CORE | ROUTINE | P0 | Prioritized nonconformance triage record with unknowns and next owner |
| document-nonconformance | 09 | CORE | ROUTINE | P1 | Nonconformance record distinguishing observation from interpretation |
| assess-product-containment | 09 | CORE | REGULATED | P1 | Proposed containment scope with unknown exposure and review owners |
| perform-root-cause-analysis | 09 | CORE | ROUTINE | P1 | Causal assessment separating supported conclusions from untested hypotheses |
| perform-five-whys | 09 | CORE | ROUTINE | P2 | Five-whys chain with unverified links and alternative explanations |
| build-fishbone-analysis | 09 | CORE | ROUTINE | P2 | Cause-category hypothesis map without treating brainstorming as proof |
| perform-pareto-analysis | 09 | CORE | ROUTINE | P1 | Ranked Pareto breakdown with metric basis and category limitations |
| build-corrective-action | 09 | CORE | ROUTINE | P1 | Corrective-action proposal with cause linkage and effectiveness criteria |
| build-preventive-action | 09 | CORE | ROUTINE | P2 | Preventive-action proposal tied to a prospective risk rather than an existing defect |
| verify-corrective-action-effectiveness | 09 | CORE | ROUTINE | P1 | Effectiveness assessment with unmet criteria and monitoring needs |
| build-preventive-maintenance-plan | 10 | CORE | HAZARDOUS_OPERATION | P1 | Maintenance-planning draft with qualified execution and isolation review needs |
| prioritize-maintenance-work | 10 | CORE | HAZARDOUS_OPERATION | P1 | Maintenance priority list preserving safety restrictions and authorization gaps |
| analyze-equipment-downtime | 10 | CORE | ROUTINE | P1 | Downtime-loss breakdown with overlapping events and missing codes flagged |
| calculate-mtbf | 10 | CORE | ROUTINE | P1 | MTBF estimate with observation basis and zero-failure limitations |
| calculate-mttr | 10 | CORE | ROUTINE | P1 | MTTR estimate with repair-time basis and missing-event treatment |
| analyze-failure-history | 10 | CORE | ROUTINE | P1 | Failure-pattern analysis with coding and exposure limitations |
| perform-equipment-failure-analysis | 10 | CORE | ENGINEERING_OR_CERTIFICATION_BOUNDARY | P2 | Equipment failure hypothesis assessment for qualified investigation |
| build-predictive-maintenance-plan | 10 | CORE | ENGINEERING_OR_CERTIFICATION_BOUNDARY | P2 | Condition-monitoring plan draft without inventing intervention thresholds |
| review-spare-parts-criticality | 10 | CORE | ROUTINE | P2 | Spare-parts criticality assessment without procurement or substitution approval |
| analyze-maintenance-backlog | 10 | CORE | ROUTINE | P2 | Backlog workload and aging analysis with incomparable estimates flagged |
| identify-manufacturing-hazard | 11 | CORE | HAZARDOUS_OPERATION | P1 | Hazard register with evidence gaps and responsible review needs |
| build-job-safety-analysis | 11 | CORE | HAZARDOUS_OPERATION | P1 | Draft task-hazard analysis for qualified review without work authorization |
| review-machine-guarding-risk | 11 | CORE | ENGINEERING_OR_CERTIFICATION_BOUNDARY | P1 | Machine-guarding concern brief without bypass instructions or safety signoff |
| identify-hazardous-energy-source | 11 | CORE | HAZARDOUS_OPERATION | P1 | Potential energy-source inventory with unverified sources and qualified-review needs |
| review-lockout-program | 11 | CORE | HAZARDOUS_OPERATION | P0 | Lockout-program evidence-gap review without equipment-specific isolation or restart steps |
| review-ppe-requirement | 11 | CORE | HAZARDOUS_OPERATION | P1 | PPE requirement evidence gaps for qualified selection |
| review-ergonomic-risk | 11 | CORE | HAZARDOUS_OPERATION | P2 | Ergonomic concern assessment and review priorities without medical judgments |
| review-housekeeping-risk | 11 | CORE | HAZARDOUS_OPERATION | P2 | Housekeeping hazard findings with evidence and corrective-review ownership |
| triage-manufacturing-incident | 11 | CORE | HAZARDOUS_OPERATION | P1 | Incident information and escalation record without investigation conclusions or rescue instructions |
| validate-bill-of-materials | 12 | CORE | ROUTINE | P1 | BOM consistency findings without certifying product design |
| calculate-material-requirement | 12 | CORE | ROUTINE | P1 | Gross production component requirement with unresolved conversion assumptions |
| analyze-material-variance | 12 | CORE | ROUTINE | P1 | Material variance breakdown separating usage loss and unresolved balance errors |
| trace-production-lot | 12 | CORE | REGULATED | P1 | Targeted upstream/downstream production trace with missing links |
| build-product-genealogy | 12 | CORE | ROUTINE | P1 | Production genealogy graph with orphan or contradictory events |
| review-component-substitution | 12 | CORE | ENGINEERING_OR_CERTIFICATION_BOUNDARY | P1 | Substitution impact package for authorized engineering/quality review |
| reconcile-material-consumption | 12 | CORE | ROUTINE | P1 | Material reconciliation statement with unresolved events and no inventory posting |
| identify-line-side-shortage | 12 | CORE | ROUTINE | P1 | Line-side shortage and production-impact handoff to logistics |
| review-scrap-material-record | 12 | CORE | ROUTINE | P2 | Scrap-record integrity findings without disposal or adjustment approval |
| build-manufacturing-skills-matrix | 13 | CORE | ROUTINE | P1 | Evidence-linked skills matrix with unknown proficiency identified |
| build-shift-production-plan | 13 | CORE | ROUTINE | P1 | Shift allocation draft with unstaffed or unready tasks |
| prepare-shift-handoff | 13 | CORE | ROUTINE | P1 | Shift handoff record with unresolved issues and responsible owners |
| analyze-labor-productivity | 13 | CORE | ROUTINE | P2 | Labor productivity analysis with comparable unit/hour basis |
| identify-training-gap | 13 | CORE | ROUTINE | P1 | Task-specific training gap list without certification decisions |
| review-operator-qualification-record | 13 | CORE | REGULATED | P1 | Qualification-record readiness gaps for responsible employer review |
| balance-workforce | 13 | CORE | ROUTINE | P2 | Workforce allocation proposal with gaps and restrictions preserved |
| calculate-production-labor-requirement | 13 | CORE | ROUTINE | P1 | Labor-hour and staffing-equivalent estimate without hiring or overtime approval |
| identify-eight-wastes | 14 | CORE | ROUTINE | P2 | Evidence-tagged waste opportunity list without assumed savings |
| build-value-stream-map | 14 | CORE | ROUTINE | P1 | Current-state value-stream map with data quality and boundary notes |
| perform-gemba-observation-review | 14 | CORE | ROUTINE | P2 | Observation synthesis separating facts questions and improvement hypotheses |
| perform-5s-audit | 14 | CORE | ROUTINE | P2 | 5S review findings with unsupported scores identified |
| analyze-flow-efficiency | 14 | CORE | ROUTINE | P2 | Flow-efficiency result with classification assumptions |
| build-smed-improvement-plan | 14 | CORE | HAZARDOUS_OPERATION | P2 | SMED improvement proposal preserving guarding energy and task-approval boundaries |
| build-kaizen-plan | 14 | CORE | ROUTINE | P2 | Bounded improvement-event plan with measurement and review ownership |
| measure-improvement-result | 14 | CORE | ROUTINE | P2 | Before/after improvement assessment distinguishing association from proven effect |
| map-erp-mes-flow | 15 | CORE | ROUTINE | P1 | ERP/MES information-flow map with ownership and reconciliation gaps |
| map-mes-machine-data-flow | 15 | CORE | ROUTINE | P1 | Machine/MES data-flow map without control-channel changes |
| analyze-production-event-history | 15 | CORE | ROUTINE | P1 | Production-event chronology with missing duplicated or conflicting events |
| review-production-master-data | 15 | CORE | ROUTINE | P1 | Master-data quality findings without live corrections |
| analyze-oee-data | 15 | CORE | ROUTINE | P1 | OEE input-data reconciliation findings before calculation |
| diagnose-production-data-quality | 15 | CORE | ROUTINE | P1 | Data-quality defect register with impact and remediation ownership |
| map-manufacturing-traceability-data | 15 | CORE | ROUTINE | P1 | Traceability data-lineage map distinguishing architecture from an executed lot trace |
| build-manufacturing-kpi-model | 15 | CORE | ROUTINE | P2 | Manufacturing KPI definition model with lineage denominators and exclusions |
| assess-automation-opportunity | 16 | CORE | ENGINEERING_OR_CERTIFICATION_BOUNDARY | P2 | Automation opportunity assessment with evidence gaps and review needs |
| evaluate-robotics-application | 16 | CORE | ENGINEERING_OR_CERTIFICATION_BOUNDARY | P2 | Robotics concept suitability brief without deployment or safety approval |
| evaluate-cobot-application | 16 | CORE | ENGINEERING_OR_CERTIFICATION_BOUNDARY | P2 | Collaborative-application concern assessment without assuming inherent safety |
| evaluate-machine-vision-application | 16 | CORE | ENGINEERING_OR_CERTIFICATION_BOUNDARY | P2 | Machine-vision feasibility brief with validation gaps and no release authority |
| evaluate-additive-manufacturing-application | 16 | CORE | ENGINEERING_OR_CERTIFICATION_BOUNDARY | P2 | Additive-process suitability brief for engineering/sector review |
| build-automation-business-case | 16 | CORE | ROUTINE | P2 | Automation economic comparison with uncertainty and no investment approval |
| assess-automation-process-readiness | 16 | CORE | ENGINEERING_OR_CERTIFICATION_BOUNDARY | P1 | Automation prerequisite gap assessment before concept selection |
| review-human-machine-interface-risk | 16 | CORE | ENGINEERING_OR_CERTIFICATION_BOUNDARY | P2 | Human-machine interaction concern brief without live interface modification |
| review-supplier-qualification | 17 | CORE | REGULATED | P1 | Supplier technical-qualification evidence review without approving supplier status |
| build-incoming-inspection-plan | 17 | CORE | REGULATED | P1 | Incoming manufacturing-quality inspection draft distinct from receipt-count reconciliation |
| review-supplier-conformance | 17 | CORE | REGULATED | P1 | Supplier conformity evidence gaps and disposition-review needs |
| analyze-supplier-defect | 17 | CORE | ROUTINE | P2 | Supplier-defect pattern analysis separating supplier attribution from assumptions |
| draft-supplier-corrective-action | 17 | CORE | ROUTINE | P1 | Draft supplier corrective-action request for human review; no transmission |
| analyze-supplier-quality-kpis | 17 | CORE | ROUTINE | P2 | Supplier quality comparison with denominator and mix limitations |
| review-certificate-of-conformance | 17 | CORE | REGULATED | P1 | Certificate evidence review with mismatches and unverifiable assertions |
| review-supplier-change-impact | 17 | CORE | ENGINEERING_OR_CERTIFICATION_BOUNDARY | P1 | Supplier-change impact brief for manufacturing change review |
| review-change-package | 18 | CORE | ENGINEERING_OR_CERTIFICATION_BOUNDARY | P1 | Change-package completeness findings distinct from technical impact analysis |
| build-engineering-change-impact-assessment | 18 | CORE | ENGINEERING_OR_CERTIFICATION_BOUNDARY | P1 | Cross-functional change-impact assessment without approving implementation |
| review-bom-change | 18 | CORE | ENGINEERING_OR_CERTIFICATION_BOUNDARY | P1 | BOM-change impact findings for authorized disposition |
| review-routing-change | 18 | CORE | ENGINEERING_OR_CERTIFICATION_BOUNDARY | P1 | Routing-change impact findings without activating routing revisions |
| review-process-change | 18 | CORE | ENGINEERING_OR_CERTIFICATION_BOUNDARY | P1 | Process-change impact and validation-needs brief for qualified review |
| draft-document-revision-plan | 18 | CORE | ROUTINE | P1 | Document revision and withdrawal plan without publishing approved versions |
| identify-obsolete-document | 18 | CORE | ROUTINE | P1 | Obsolete-document exposure list preserving uncertainty about actual use |
| verify-change-implementation | 18 | CORE | ENGINEERING_OR_CERTIFICATION_BOUNDARY | P1 | Change-implementation evidence assessment without retrospective approval |
| review-document-revision | 18 | CORE | ROUTINE | P1 | Revision applicability comparison with unresolved conflicts |
| identify-manufacturing-environmental-aspect | 19 | CORE | REGULATED | P1 | Environmental-aspect inventory with impact hypotheses and missing evidence |
| build-environmental-risk-register | 19 | CORE | REGULATED | P1 | Environmental risk register for responsible review without compliance determination |
| analyze-energy-consumption | 19 | CORE | ROUTINE | P2 | Energy-consumption and intensity analysis with allocation limitations |
| analyze-waste-stream | 19 | CORE | REGULATED | P1 | Waste-stream inventory with characterization gaps; no disposal classification or permission |
| build-waste-reduction-plan | 19 | CORE | REGULATED | P2 | Waste-reduction proposal with material/control changes requiring review |
| review-environmental-objective | 19 | CORE | REGULATED | P2 | Environmental-objective measurability and evidence review |
| identify-manufacturing-jurisdiction | 20 | CORE | REGULATED | P1 | Jurisdiction-context record separating product workplace and other unresolved regimes |
| identify-applicable-regulatory-layer | 20 | CORE | REGULATED | P1 | Applicability research map with unresolved federal subnational sector and local questions |
| assess-whmis-applicability | 20 | CANADA_OVERLAY | REGULATED | P1 | WHMIS applicability research brief with unresolved scope questions |
| review-whmis-readiness | 20 | CANADA_OVERLAY | REGULATED | P1 | WHMIS readiness evidence-gap review without compliance approval |
| assess-made-in-canada-claim | 20 | CANADA_OVERLAY | REGULATED | P0 | Non-food origin-claim evidence assessment for responsible review; no claim publication |
| assess-product-of-canada-claim | 20 | CANADA_OVERLAY | REGULATED | P1 | Product-of-Canada claim evidence assessment without substituting Made-in-Canada criteria |
| review-nonfood-labelling-readiness | 20 | CANADA_OVERLAY | REGULATED | P1 | General non-food label evidence gaps with sector exclusions and review needs |
| verify-regulatory-source-freshness | 20 | CORE | REGULATED | P1 | Source verification record distinguishing accessibility freshness and applicability |
| identify-provincial-safety-overlay | 20 | CANADA_OVERLAY | REGULATED | P1 | Provincial/territorial overlay-selection brief with unknown or unsupported coverage explicit |
<!-- candidate-index:end -->
