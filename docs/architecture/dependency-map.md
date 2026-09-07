# AgentManufacturing dependency map v1

Status: **TAXONOMY_FROZEN_NOT_IMPLEMENTED**. The canonical graph is in [taxonomy-index.yaml](taxonomy-index.yaml); accepted responsibility boundaries are in the [v1 taxonomy](master-taxonomy-v1.md).

## Edge semantics

All 76 edges are `EVIDENCE_REUSE`: provider result → consumer input. Equivalent supplied evidence can replace executing a provider skill. The graph records method ownership and a valid review/authoring order, not an automatic runtime workflow or a requirement to implement every provider before using a consumer.

For example, `calculate-production-capacity` can supply `build-production-plan`, but the AM-10 production-plan fixture can provide an already established capacity table. The reference wave therefore remains bounded. A graph edge does not permit live system operations, imply an installed integration, or override a missing-data boundary.

All named provider/consumer records exist in the v1 index. No self-dependencies or cycles are accepted; no core consumer directly requires a Canadian overlay. The sequence below is one valid topological ordering, not a replacement for roadmap wave order or P0/P1/P2 priority.

## Shared and conditional requirements

| ID | Use | Implementation/formalization owner |
|---|---|---|
| CALC | Units, variables, assumptions, formulas, invalid inputs, and worked fixtures for quantitative outputs. | AM-08 |
| REVIEW | Existing AM-01 authority boundaries; detailed safety/review gates to follow. | AM-05 |
| STANDARDS | Conditional applicability, edition and licensed-text evidence before a dependent conclusion. | AM-07 |
| JURIS | Conditional facility/employer/activity context; no default province or regime. | AM-04 |
| SOURCE | Authoritative claim/source verification; reachable links alone do not prove freshness or applicability. | AM-07 |
| FEDERAL | Evidence for the Canadian federal question; not automatic federal workplace classification. | AM-04 |
| LOGISTICS | Supplied movement/custody evidence or the AM-01 handoff; no mandatory external repository installation. | AM-19 |

Requirements are named responsibilities rather than unresolved skill references. Source and specialist evidence may be unavailable at invocation; the consumer must return supported partial analysis and an explicit gap. No hypothetical provider result may be invented to satisfy a dependency.

## Ordered records

<!-- dependency-order:start -->
| Order | Accepted skill |
|---|---|
| 1 | classify-manufacturing-operation |
| 2 | analyze-product-process-profile |
| 3 | analyze-production-constraints |
| 4 | calculate-production-capacity |
| 5 | analyze-equipment-downtime |
| 6 | identify-manufacturing-bottleneck |
| 7 | calculate-production-requirement |
| 8 | validate-bill-of-materials |
| 9 | calculate-material-requirement |
| 10 | calculate-production-labor-requirement |
| 11 | build-production-plan |
| 12 | sequence-production-orders |
| 13 | analyze-schedule-adherence |
| 14 | identify-capacity-shortfall |
| 15 | plan-production-changeover |
| 16 | compare-production-scenarios |
| 17 | calculate-production-lead-time |
| 18 | review-production-order-readiness |
| 19 | compare-production-lot-sizes |
| 20 | draft-work-instruction |
| 21 | review-work-instruction |
| 22 | calculate-takt-time |
| 23 | analyze-cycle-time |
| 24 | build-standard-work |
| 25 | review-document-revision |
| 26 | analyze-standard-work-deviation |
| 27 | review-operator-checklist |
| 28 | map-manufacturing-process |
| 29 | build-process-routing |
| 30 | identify-process-inputs-outputs |
| 31 | review-process-parameter-control |
| 32 | compare-process-alternatives |
| 33 | review-quality-requirement |
| 34 | build-process-control-plan |
| 35 | balance-production-line |
| 36 | calculate-first-pass-yield |
| 37 | calculate-oee |
| 38 | analyze-changeover-loss |
| 39 | calculate-throughput |
| 40 | calculate-capacity-utilization |
| 41 | calculate-rolled-throughput-yield |
| 42 | calculate-scrap-rate |
| 43 | calculate-rework-rate |
| 44 | select-measurement-method |
| 45 | build-inspection-plan |
| 46 | review-quality-record |
| 47 | review-product-conformity |
| 48 | prepare-quality-release-package |
| 49 | audit-quality-process |
| 50 | analyze-quality-kpis |
| 51 | review-measurement-equipment |
| 52 | build-calibration-register |
| 53 | review-calibration-status |
| 54 | identify-out-of-calibration-risk |
| 55 | analyze-measurement-system |
| 56 | review-gauge-control |
| 57 | assess-measurement-traceability |
| 58 | build-control-chart |
| 59 | interpret-control-chart |
| 60 | analyze-production-event-history |
| 61 | identify-special-cause-variation |
| 62 | review-capability-readiness |
| 63 | calculate-cp-cpk |
| 64 | calculate-pp-ppk |
| 65 | review-control-limits |
| 66 | build-spc-monitoring-plan |
| 67 | triage-nonconformance |
| 68 | document-nonconformance |
| 69 | build-product-genealogy |
| 70 | trace-production-lot |
| 71 | assess-product-containment |
| 72 | perform-root-cause-analysis |
| 73 | perform-five-whys |
| 74 | build-fishbone-analysis |
| 75 | perform-pareto-analysis |
| 76 | build-corrective-action |
| 77 | build-preventive-action |
| 78 | verify-corrective-action-effectiveness |
| 79 | analyze-failure-history |
| 80 | build-preventive-maintenance-plan |
| 81 | analyze-maintenance-backlog |
| 82 | prioritize-maintenance-work |
| 83 | calculate-mtbf |
| 84 | calculate-mttr |
| 85 | perform-equipment-failure-analysis |
| 86 | build-predictive-maintenance-plan |
| 87 | review-spare-parts-criticality |
| 88 | identify-manufacturing-hazard |
| 89 | build-job-safety-analysis |
| 90 | review-machine-guarding-risk |
| 91 | identify-hazardous-energy-source |
| 92 | review-lockout-program |
| 93 | review-ppe-requirement |
| 94 | review-ergonomic-risk |
| 95 | review-housekeeping-risk |
| 96 | triage-manufacturing-incident |
| 97 | reconcile-material-consumption |
| 98 | analyze-material-variance |
| 99 | review-component-substitution |
| 100 | identify-line-side-shortage |
| 101 | review-scrap-material-record |
| 102 | build-manufacturing-skills-matrix |
| 103 | build-shift-production-plan |
| 104 | prepare-shift-handoff |
| 105 | analyze-labor-productivity |
| 106 | identify-training-gap |
| 107 | review-operator-qualification-record |
| 108 | balance-workforce |
| 109 | identify-eight-wastes |
| 110 | build-value-stream-map |
| 111 | perform-gemba-observation-review |
| 112 | perform-5s-audit |
| 113 | analyze-flow-efficiency |
| 114 | build-smed-improvement-plan |
| 115 | build-kaizen-plan |
| 116 | measure-improvement-result |
| 117 | map-erp-mes-flow |
| 118 | map-mes-machine-data-flow |
| 119 | review-production-master-data |
| 120 | analyze-oee-data |
| 121 | diagnose-production-data-quality |
| 122 | map-manufacturing-traceability-data |
| 123 | build-manufacturing-kpi-model |
| 124 | assess-automation-process-readiness |
| 125 | assess-automation-opportunity |
| 126 | evaluate-robotics-application |
| 127 | evaluate-cobot-application |
| 128 | evaluate-machine-vision-application |
| 129 | evaluate-additive-manufacturing-application |
| 130 | build-automation-business-case |
| 131 | review-human-machine-interface-risk |
| 132 | review-supplier-qualification |
| 133 | analyze-supplier-defect |
| 134 | draft-supplier-corrective-action |
| 135 | review-certificate-of-conformance |
| 136 | review-supplier-change-impact |
| 137 | review-change-package |
| 138 | build-engineering-change-impact-assessment |
| 139 | review-bom-change |
| 140 | review-routing-change |
| 141 | review-process-change |
| 142 | identify-obsolete-document |
| 143 | draft-document-revision-plan |
| 144 | verify-change-implementation |
| 145 | identify-manufacturing-environmental-aspect |
| 146 | build-environmental-risk-register |
| 147 | analyze-energy-consumption |
| 148 | analyze-waste-stream |
| 149 | build-waste-reduction-plan |
| 150 | review-environmental-objective |
| 151 | identify-manufacturing-jurisdiction |
| 152 | identify-applicable-regulatory-layer |
| 153 | verify-regulatory-source-freshness |
| 154 | assess-whmis-applicability |
| 155 | review-whmis-readiness |
| 156 | assess-made-in-canada-claim |
| 157 | assess-product-of-canada-claim |
| 158 | review-nonfood-labelling-readiness |
| 159 | identify-provincial-safety-overlay |
<!-- dependency-order:end -->

## Evidence-reuse edges

<!-- dependency-edges:start -->
| Provider | Consumer | Type |
|---|---|---|
| classify-manufacturing-operation | analyze-product-process-profile | EVIDENCE_REUSE |
| calculate-production-capacity | identify-manufacturing-bottleneck | EVIDENCE_REUSE |
| analyze-equipment-downtime | identify-manufacturing-bottleneck | EVIDENCE_REUSE |
| calculate-production-requirement | build-production-plan | EVIDENCE_REUSE |
| calculate-production-capacity | build-production-plan | EVIDENCE_REUSE |
| calculate-material-requirement | build-production-plan | EVIDENCE_REUSE |
| calculate-production-labor-requirement | build-production-plan | EVIDENCE_REUSE |
| calculate-production-capacity | identify-capacity-shortfall | EVIDENCE_REUSE |
| calculate-takt-time | build-standard-work | EVIDENCE_REUSE |
| analyze-cycle-time | build-standard-work | EVIDENCE_REUSE |
| review-document-revision | analyze-standard-work-deviation | EVIDENCE_REUSE |
| map-manufacturing-process | build-process-routing | EVIDENCE_REUSE |
| review-quality-requirement | build-process-control-plan | EVIDENCE_REUSE |
| map-manufacturing-process | build-process-control-plan | EVIDENCE_REUSE |
| analyze-cycle-time | balance-production-line | EVIDENCE_REUSE |
| calculate-takt-time | balance-production-line | EVIDENCE_REUSE |
| calculate-first-pass-yield | calculate-rolled-throughput-yield | EVIDENCE_REUSE |
| review-quality-requirement | build-inspection-plan | EVIDENCE_REUSE |
| select-measurement-method | build-inspection-plan | EVIDENCE_REUSE |
| review-quality-requirement | review-product-conformity | EVIDENCE_REUSE |
| review-quality-record | review-product-conformity | EVIDENCE_REUSE |
| review-product-conformity | prepare-quality-release-package | EVIDENCE_REUSE |
| review-quality-record | prepare-quality-release-package | EVIDENCE_REUSE |
| build-calibration-register | review-calibration-status | EVIDENCE_REUSE |
| review-calibration-status | identify-out-of-calibration-risk | EVIDENCE_REUSE |
| interpret-control-chart | identify-special-cause-variation | EVIDENCE_REUSE |
| analyze-production-event-history | identify-special-cause-variation | EVIDENCE_REUSE |
| interpret-control-chart | review-capability-readiness | EVIDENCE_REUSE |
| analyze-measurement-system | review-capability-readiness | EVIDENCE_REUSE |
| review-capability-readiness | calculate-cp-cpk | EVIDENCE_REUSE |
| review-capability-readiness | calculate-pp-ppk | EVIDENCE_REUSE |
| trace-production-lot | assess-product-containment | EVIDENCE_REUSE |
| perform-root-cause-analysis | build-corrective-action | EVIDENCE_REUSE |
| analyze-failure-history | build-preventive-maintenance-plan | EVIDENCE_REUSE |
| analyze-maintenance-backlog | prioritize-maintenance-work | EVIDENCE_REUSE |
| analyze-failure-history | build-predictive-maintenance-plan | EVIDENCE_REUSE |
| identify-manufacturing-hazard | build-job-safety-analysis | EVIDENCE_REUSE |
| identify-hazardous-energy-source | review-lockout-program | EVIDENCE_REUSE |
| validate-bill-of-materials | calculate-material-requirement | EVIDENCE_REUSE |
| reconcile-material-consumption | analyze-material-variance | EVIDENCE_REUSE |
| build-product-genealogy | trace-production-lot | EVIDENCE_REUSE |
| calculate-material-requirement | identify-line-side-shortage | EVIDENCE_REUSE |
| build-production-plan | build-shift-production-plan | EVIDENCE_REUSE |
| review-production-order-readiness | build-shift-production-plan | EVIDENCE_REUSE |
| build-manufacturing-skills-matrix | identify-training-gap | EVIDENCE_REUSE |
| review-document-revision | identify-training-gap | EVIDENCE_REUSE |
| calculate-production-labor-requirement | balance-workforce | EVIDENCE_REUSE |
| review-operator-qualification-record | balance-workforce | EVIDENCE_REUSE |
| map-manufacturing-process | build-value-stream-map | EVIDENCE_REUSE |
| analyze-changeover-loss | build-smed-improvement-plan | EVIDENCE_REUSE |
| analyze-production-event-history | analyze-oee-data | EVIDENCE_REUSE |
| assess-automation-process-readiness | assess-automation-opportunity | EVIDENCE_REUSE |
| assess-automation-process-readiness | evaluate-robotics-application | EVIDENCE_REUSE |
| evaluate-robotics-application | evaluate-cobot-application | EVIDENCE_REUSE |
| review-quality-requirement | evaluate-machine-vision-application | EVIDENCE_REUSE |
| assess-automation-opportunity | build-automation-business-case | EVIDENCE_REUSE |
| document-nonconformance | draft-supplier-corrective-action | EVIDENCE_REUSE |
| validate-bill-of-materials | review-bom-change | EVIDENCE_REUSE |
| identify-obsolete-document | draft-document-revision-plan | EVIDENCE_REUSE |
| review-document-revision | identify-obsolete-document | EVIDENCE_REUSE |
| review-change-package | verify-change-implementation | EVIDENCE_REUSE |
| identify-manufacturing-environmental-aspect | build-environmental-risk-register | EVIDENCE_REUSE |
| analyze-waste-stream | build-waste-reduction-plan | EVIDENCE_REUSE |
| analyze-material-variance | build-waste-reduction-plan | EVIDENCE_REUSE |
| identify-manufacturing-jurisdiction | identify-applicable-regulatory-layer | EVIDENCE_REUSE |
| identify-applicable-regulatory-layer | assess-whmis-applicability | EVIDENCE_REUSE |
| verify-regulatory-source-freshness | assess-whmis-applicability | EVIDENCE_REUSE |
| assess-whmis-applicability | review-whmis-readiness | EVIDENCE_REUSE |
| identify-applicable-regulatory-layer | assess-made-in-canada-claim | EVIDENCE_REUSE |
| verify-regulatory-source-freshness | assess-made-in-canada-claim | EVIDENCE_REUSE |
| identify-applicable-regulatory-layer | assess-product-of-canada-claim | EVIDENCE_REUSE |
| verify-regulatory-source-freshness | assess-product-of-canada-claim | EVIDENCE_REUSE |
| identify-applicable-regulatory-layer | review-nonfood-labelling-readiness | EVIDENCE_REUSE |
| verify-regulatory-source-freshness | review-nonfood-labelling-readiness | EVIDENCE_REUSE |
| identify-manufacturing-jurisdiction | identify-provincial-safety-overlay | EVIDENCE_REUSE |
| verify-regulatory-source-freshness | identify-provincial-safety-overlay | EVIDENCE_REUSE |
<!-- dependency-edges:end -->

## Validation

`python scripts/validate-taxonomy.py` checks the index's edge list against accepted records, validates provider-before-consumer ordering, and compares both tables to the canonical data. A graph pass proves structural consistency only. AM-09/10 must validate actual input handling, and AM-30 must evaluate multi-domain behavior.
