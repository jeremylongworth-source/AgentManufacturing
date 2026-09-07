# AgentManufacturing master taxonomy v0.1

Status: The AM-02 candidate register is drafted; the taxonomy is not frozen.

Current draft: [candidate-taxonomy-v0.1.md](candidate-taxonomy-v0.1.md) and [candidate-register-v0.1.json](candidate-register-v0.1.json). They contain 162 candidate records across all twenty families and explicit dispositions for the 166 representative names preserved below. See the [AM-02 handoff](../development/handoffs/AM-02-final-handoff.md) for validation and the AM-03 audit brief. The remaining source proposal is historical provenance, not implemented procedures or verified current regulatory/standards guidance.

Working directory: `D:\AgentMfg`

Source: “Branch · Plan AgentLogistics Skills”, conversation `6a9d881b-9330-83ea-b887-26309d52536d`, manufacturing proposal message `e32c7e5b-7294-4699-b383-0de485378ba7`. Saved on 2026-09-06. This is the initial planning proposal, not evidence of completed development. Conversation-only citation markers have been removed because they do not resolve in repository Markdown. Legal details and standards-edition assertions preserved from the source are planning notes and have not been independently reverified in this handoff; verify official sources before implementation or operational use.

This file preserves the original family overview, representative names, and supporting design notes. The estimated 220–280 eventual skills is not a quota. Names are candidates, not implemented skills. Family numbering and source naming variations are retained pending AM-02/AM-03 review; for example, `build-smED-improvement-plan` requires normalization, and similar value-stream/changeover candidates require an atomicity and duplication audit.

See [ROADMAP.md](../../ROADMAP.md) for milestones and execution instructions and [domain-framework.md](domain-framework.md) for jurisdiction, safety, role composition, and repository boundaries.

## Candidate register contract for AM-02

AM-02 supplies the following fields for each candidate in the linked JSON register. The representative lists below retain their original names for provenance; use `source_dispositions` to find their draft targets:

```text
name
family
tier
jurisdiction
safety_class
sector_dependency
inputs
outputs
dependencies
priority
```

AM-03 audits atomicity, duplicate responsibility, naming, dependency order, regulatory scope, engineering boundaries, testability, and specialization need before freezing `master-taxonomy-v1.md`, `dependency-map.md`, and `taxonomy-index.yaml`.

## Source framework and family overview

The project should focus on **commercial manufacturing operations in Canada**, covering both discrete and process-oriented manufacturing without trying to encode every industry-specific rule in the core.

Statistics Canada classifies manufacturing broadly as the physical, chemical, or mechanical transformation of materials into new finished or semi-finished products, including assembly, blending and finishing. The sector spans food, wood, chemicals, plastics, metals, machinery, electronics, transportation equipment and many other subsectors, which strongly argues for a sector-neutral core plus specializations. 

I recommend **20 initial knowledge families**.

| # | Family | Core capability |
|---|---|---|
| 01 | Manufacturing Fundamentals | Understand production systems, flow and terminology |
| 02 | Production Planning & Scheduling | Plan what, when, where and how much to make |
| 03 | Standard Work & Work Instructions | Define repeatable controlled processes |
| 04 | Process Engineering | Map and improve manufacturing processes |
| 05 | Industrial Engineering & Capacity | Cycle time, takt, utilization, line balancing |
| 06 | Quality Management | QMS, inspection, conformity and release support |
| 07 | Metrology & Calibration | Measurement systems and equipment control |
| 08 | SPC & Process Capability | Control charts, variation, Cp/Cpk, stability |
| 09 | Nonconformance, RCA & CAPA | Investigate defects and prevent recurrence |
| 10 | Maintenance & Reliability | PM, PdM, downtime, MTBF/MTTR and asset health |
| 11 | Machine & Workplace Safety | Hazard assessment, guarding, hazardous energy |
| 12 | Materials, BOM & Traceability | Production materials and genealogy |
| 13 | Workforce & Shift Operations | Training, skills, handoffs and staffing |
| 14 | Lean & Continuous Improvement | Waste reduction and operational excellence |
| 15 | Manufacturing Systems & Data | ERP, MES, SCADA, historians and production data |
| 16 | Automation & Advanced Manufacturing | Robotics, additive manufacturing, sensing and AI |
| 17 | Supplier Quality | Incoming quality, suppliers and corrective action |
| 18 | Engineering Change & Document Control | ECO/ECN, revisions, controlled documentation |
| 19 | Environmental, Energy & Waste | EMS, resources, waste and environmental performance |
| 20 | Canadian Compliance & Product Governance | WHMIS, jurisdiction routing, claims and standards |

A later taxonomy audit will probably result in roughly **220 to 280 atomic skills**, but that should be an outcome, not a target.

## 1. Manufacturing fundamentals

Representative skills:

```text
classify-manufacturing-operation
map-manufacturing-value-stream
map-production-flow
identify-production-constraints
analyze-product-process-profile
classify-discrete-vs-process-production
identify-manufacturing-bottleneck
```

This gives every other skill a shared operational language.

## 2. Production planning and scheduling

Core knowledge should include:

- demand requirements
- MPS concepts
- production orders
- routings
- lead time
- WIP
- batch/lot sizing
- sequencing
- changeovers
- finite capacity
- bottleneck scheduling
- overtime
- schedule adherence

Representative skills:

```text
build-production-plan
calculate-production-requirement
sequence-production-orders
analyze-schedule-adherence
identify-capacity-shortfall
plan-production-changeover
compare-production-scenarios
```

## 3. Standard work and work instructions

This deserves a dedicated family because controlled manufacturing depends on repeatable documented execution.

```text
draft-work-instruction
review-work-instruction
build-standard-work
analyze-standard-work-deviation
review-operator-checklist
verify-document-revision
review-training-against-standard-work
```

AgentSkills' emphasis on explicit output contracts fits particularly well here. 

## 4. Process engineering

```text
map-manufacturing-process
build-process-routing
identify-process-inputs-outputs
analyze-process-constraint
review-process-parameter-control
compare-process-alternatives
assess-process-change
build-process-control-plan
```

This should support engineers without implying professional engineering approval.

## 5. Industrial engineering and quantitative operations

This should be one of AgentManufacturing's strongest differentiators.

Calculations should include:

```text
takt time
cycle time
throughput
capacity
utilization
efficiency
yield
first-pass yield
rolled throughput yield
scrap rate
rework rate
changeover time
labor productivity
line balance
OEE
downtime
```

Representative skills:

```text
calculate-takt-time
calculate-production-capacity
analyze-cycle-time
balance-production-line
calculate-first-pass-yield
calculate-oee
analyze-changeover-loss
forecast-labor-requirement
```

Every calculation skill should expose variables, units, assumptions, formula and interpretation.

## 6. Quality management

The generic QMS architecture should be standards-aware rather than pretending every manufacturer is ISO-certified.

ISO 9001 remains the central general quality-management framework. As of September 2026, ISO lists the new 2026 edition as under publication, which is an excellent example of why AgentManufacturing needs standards-version freshness metadata. 

Core skills:

```text
review-quality-requirement
build-inspection-plan
review-production-conformity
review-quality-record
identify-quality-control-gap
prepare-quality-release-package
audit-quality-process
analyze-quality-kpis
```

The AI may support release decisions but should not impersonate a required authorized inspector, engineer or certification body.

## 7. Metrology and calibration

```text
select-measurement-method
review-measurement-equipment
build-calibration-register
review-calibration-status
identify-out-of-calibration-risk
analyze-measurement-system
review-gauge-control
assess-measurement-traceability
```

Later sector specializations can add MSA, gauge R&R and sector-specific metrology requirements.

## 8. SPC and process capability

This should be its own quantitative family:

```text
build-control-chart
interpret-control-chart
identify-special-cause-variation
calculate-process-capability
calculate-cp-cpk
calculate-pp-ppk
review-control-limits
analyze-process-stability
build-spc-monitoring-plan
```

The repository must distinguish **specification limits** from **process control limits**.

That should become an explicit test case.

## 9. Nonconformance, root cause and CAPA

```text
triage-nonconformance
document-nonconformance
assess-product-containment
perform-root-cause-analysis
perform-five-whys
build-fishbone-analysis
perform-pareto-analysis
build-corrective-action
build-preventive-action
verify-corrective-action-effectiveness
```

A strong reasoning chain is:

```text
SYMPTOM
   ↓
CONTAINMENT
   ↓
EVIDENCE
   ↓
ROOT CAUSE
   ↓
CORRECTIVE ACTION
   ↓
VERIFICATION
   ↓
STANDARDIZATION
```

## 10. Maintenance and reliability

This needs more depth than simply preventive maintenance.

```text
build-preventive-maintenance-plan
prioritize-maintenance-work
analyze-equipment-downtime
calculate-mtbf
calculate-mttr
analyze-failure-history
perform-equipment-failure-analysis
build-predictive-maintenance-plan
review-spare-parts-criticality
analyze-maintenance-backlog
```

## 11. Manufacturing safety

This needs a **Canadian jurisdiction layer**, not one universal rule file.

WHMIS is coordinated across federal, provincial and territorial legislation, with federal supplier obligations under the Hazardous Products Act and Hazardous Products Regulations and workplace obligations implemented through occupational health and safety systems. 

Manufacturing also presents machinery and hazardous-energy risks. CCOHS explicitly highlights machine guarding and lockout for maintenance and repair work. 

Core decision-support skills:

```text
identify-manufacturing-hazard
build-job-safety-analysis
review-machine-guarding-risk
identify-hazardous-energy-source
review-lockout-program
review-whmis-readiness
review-ppe-requirement
review-ergonomic-risk
review-housekeeping-risk
triage-manufacturing-incident
```

These skills should support hazard identification and program review, not replace qualified machine-safety, electrical, engineering, or occupational-safety professionals.

## 12. Materials, BOM and production traceability

Keep this scoped to **manufacturing execution**, leaving warehouse and freight depth to AgentLogistics.

```text
validate-bill-of-materials
review-material-requirement
analyze-material-variance
trace-production-lot
build-product-genealogy
review-component-substitution
reconcile-material-consumption
identify-line-side-shortage
review-scrap-material-record
```

Boundary:

```text
AgentManufacturing:
BOM → line-side → production → finished product

AgentLogistics:
receiving → storage → warehouse → freight → distribution
```

The repositories can later interoperate, but neither should duplicate the other's core procedures.

## 13. Workforce and shift operations

```text
build-manufacturing-skills-matrix
review-training-readiness
build-shift-production-plan
prepare-shift-handoff
analyze-labor-productivity
identify-training-gap
review-operator-qualification-record
balance-workforce
```

## 14. Lean and continuous improvement

```text
identify-eight-wastes
build-value-stream-map
perform-gemba-observation-review
perform-5s-audit
analyze-flow-efficiency
analyze-changeover
build-smED-improvement-plan
build-kaizen-plan
measure-improvement-result
```

Lean should remain evidence-driven rather than becoming generic "optimize everything" advice.

## 15. Manufacturing systems and data

Core systems:

```text
ERP
MRP
MES
SCADA
PLC context
historian
CMMS
QMS
LIMS
Andon
barcode/RFID
```

Skills:

```text
map-erp-mes-flow
map-mes-machine-data-flow
analyze-production-event-history
review-production-master-data
analyze-oee-data
diagnose-production-data-quality
map-manufacturing-traceability-data
build-manufacturing-kpi-model
```

Live production controls should remain outside the general core.

## 16. Automation and advanced manufacturing

ISED specifically identifies robotics, additive manufacturing and data analytics as important advanced-manufacturing technologies for Canadian industry. 

Candidate skills:

```text
assess-automation-opportunity
evaluate-robotics-application
evaluate-cobot-application
evaluate-machine-vision-application
evaluate-additive-manufacturing-application
build-automation-business-case
assess-automation-process-readiness
review-human-machine-interface-risk
```

Again, assessment and integration planning, not unsafe live robot/PLC modification.

## 17. Supplier quality

```text
qualify-manufacturing-supplier
build-incoming-inspection-plan
review-supplier-conformance
analyze-supplier-defect
issue-supplier-corrective-action
analyze-supplier-quality-kpis
review-certificate-of-conformance
review-supplier-change
```

## 18. Engineering change and document control

This was important enough in the cannabis framework that I would make it first-class here too.

```text
review-engineering-change
build-engineering-change-impact-assessment
review-bom-change
review-routing-change
review-process-change
control-document-revision
identify-obsolete-document
verify-change-implementation
```

## 19. Environment, energy and waste

ISO 14001:2026 is now published and provides a current environmental-management framework around environmental performance, compliance obligations, resource use and continual improvement. 

Skills:

```text
identify-manufacturing-environmental-aspect
build-environmental-risk-register
analyze-energy-consumption
analyze-waste-stream
analyze-material-yield-loss
build-waste-reduction-plan
review-environmental-objective
measure-environmental-improvement
```

## 20. Canadian compliance and product governance

This should contain only genuinely cross-sector Canadian requirements.

One particularly useful capability is Canadian-origin claim review. Current Competition Bureau guidance says a non-food **Made in Canada** claim generally requires the last substantial transformation to occur in Canada, at least 51% of direct production/manufacturing costs to be incurred in Canada, and an appropriate qualifying statement. **Product of Canada** uses a much higher 98% threshold. 

Candidate skills:

```text
identify-manufacturing-jurisdiction
identify-applicable-regulatory-layer
review-whmis-obligation
assess-made-in-canada-claim
assess-product-of-canada-claim
review-nonfood-labelling-readiness
verify-regulatory-source-freshness
identify-provincial-safety-overlay
```
