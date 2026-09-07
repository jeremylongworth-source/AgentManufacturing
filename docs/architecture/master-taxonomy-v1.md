# AgentManufacturing master taxonomy v1

Version: 1.0

Status: **TAXONOMY_FROZEN_NOT_IMPLEMENTED**. Completion evidence is in the [AM-03 handoff](../development/handoffs/AM-03-final-handoff.md).

The accepted catalogue contains **159 skills across twenty families**: 153 sector-neutral core methods and six Canadian requirement overlays. This freezes names, primary families, architectural tiers, responsibility boundaries, draft provenance, and the evidence-reuse graph. It does not implement skills, grant operational authority, or establish production readiness.

## Source of truth

[taxonomy-index.yaml](taxonomy-index.yaml) is the canonical structured index. It uses JSON syntax within YAML 1.2 so the repository's Python standard-library validator can read it without a third-party package. It contains all accepted records, 162 per-draft audit records covering all eight required dimensions, 166 original-name routes, requirements, graph edges, and dependency order. The tables in this document and the [dependency map](dependency-map.md) are checked projections of that index.

The [AM-02 register](candidate-register-v0.1.json) and [draft notes](candidate-taxonomy-v0.1.md) remain unchanged historical input. The [domain contract](domain-contract.md) and [scope boundaries](scope-boundaries.md) continue to govern the catalogue. See the [audit report](taxonomy-audit-v1.md) for changed responsibilities, the completed audit queue, and limits.

## Frozen decisions and implementation boundaries

- `CORE` denotes a reusable manufacturing method or generic applicability-routing method. `CANADA_OVERLAY` denotes an explicitly Canadian requirement review. Family membership is discovery/ownership, not a dependency on jurisdiction-specific rules.
- Each skill has one primary deliverable with defined input evidence and authority limits. Broad outputs such as a production allocation, causal assessment, or cross-functional impact matrix are bounded to that deliverable; they do not autonomously execute every contributing workflow.
- `review-product-conformity` replaces the draft `review-production-conformity` name and absorbs supplier-product evidence comparison. `build-inspection-plan` accepts incoming/in-process/final scope; `analyze-quality-kpis` accepts supplier population/grouping. Former supplier-specific duplicates become aliases, not packages.
- Within/overall capability calculations, measurement-method/instrument/study reviews, root-cause methods, change-package/impact reviews, and plan/shift allocation remain separate because their required evidence and primary decisions differ. Per-record distinctions and future scenario expectations are preserved in the index.
- Priority P0 identifies exactly the five AM-10 reference skills. P1 and P2 describe family implementation emphasis; none overrides roadmap order. Taxonomy acceptance does not authorize mass authoring before AM-10.
- Provisional jurisdiction flags and primary safety classes are retained as **baseline review classifications pending AM-04/05 formalization**. They remain applicability questions, not verified legal conclusions. The freeze does not prevent those scheduled refinements; they must preserve provenance and update affected records explicitly.
- Sector-specific dependent conclusions require the relevant source/overlay evidence or a stated coverage gap. No new sector package is frozen by AM-03. The AM-01 sector model and AM-29 specialization wave remain in force.

## Inputs, outputs, and reuse

Each accepted record retains explicit inputs, a primary output, boundaries, source names, contributing draft names, a discriminating audit note, and a future acceptance scenario. `acceptance_status: SPECIFIED_NOT_EXECUTED` makes the limit explicit: a documented case is not an observed model result.

The [dependency map](dependency-map.md) contains 76 directed **evidence-reuse** edges. A provider's result can inform a consumer; equivalent supplied evidence can satisfy the input instead. These are not mandatory package/runtime dependencies. This distinction allows the five reference skills to be proved in AM-10 using supplied fixtures and the earlier shared calculation/source standards, without prematurely implementing later family skills.

Seven shared/evidence/authority/handoff requirement IDs remain planned for the appropriate waves: CALC, REVIEW, STANDARDS, JURIS, SOURCE, FEDERAL, LOGISTICS. Existing AM-01 authority and logistics boundaries already apply even where formal implementation is planned. No core skill directly requires a Canadian overlay.

## Validation and change control

Run both checks from the repository root:

```powershell
python scripts/validate-candidate-register.py
python scripts/validate-taxonomy.py
```

The draft check preserves AM-02 evidence. The v1 check covers canonical record integrity, audit/provenance coverage, graph ordering and isolation, reference priorities, and document projections. Neither check proves formula correctness, actual agent routing, safe behavior, legal applicability, or complete industry coverage.

New tasks, scope expansions, aliases, or graph changes require a documented audit amendment, updated index/projections, and relevant later-wave checks. Do not silently replace the preserved AM-02 data or treat an absent specialist capability as authorization to improvise.

## Accepted catalogue

Family, tier, safety class, priority, and primary output below project the canonical index. Safety classes are baseline review classifications, not permissions.

<!-- accepted-index:start -->
| Accepted skill | Family | Tier | Safety class | Priority | Primary output |
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
| build-inspection-plan | 06 | CORE | REGULATED | P1 | Stage-scoped inspection-plan draft preserving supplier/lot context and missing acceptance or sampling evidence |
| review-product-conformity | 06 | CORE | REGULATED | P1 | Product conformity evidence assessment across incoming in-process or finished scope, with source conflicts and unresolved requirements |
| review-quality-record | 06 | CORE | ROUTINE | P1 | Record completeness and integrity findings preserving original values |
| prepare-quality-release-package | 06 | CORE | REGULATED | P1 | Release evidence package with unresolved holds for authorized disposition |
| audit-quality-process | 06 | CORE | REGULATED | P2 | Evidence-linked process gap report without certification or audit approval |
| analyze-quality-kpis | 06 | CORE | ROUTINE | P2 | Definition-based quality metric comparison with population/supplier grouping and denominator comparability gaps |
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
| analyze-supplier-defect | 17 | CORE | ROUTINE | P2 | Supplier-defect pattern analysis separating supplier attribution from assumptions |
| draft-supplier-corrective-action | 17 | CORE | ROUTINE | P1 | Draft supplier corrective-action request for human review; no transmission |
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
<!-- accepted-index:end -->
