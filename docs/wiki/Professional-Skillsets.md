# Professional skillsets

These 18 roles compose 38 workflows. Resolution returns references, not execution or authority. Use exact role names and workflow IDs with `python scripts/resolve-skillset.py ROLE WORKFLOW`.

## production-operator-support

Support an operator's documented work and shift handoff. [Manifest](https://github.com/jeremylongworth-source/AgentManufacturing/blob/main/skillsets/production-operator-support/skillset.yaml).

| Workflow | Required evidence | Output | Review boundary |
|---|---|---|---|
| work-review | Current document revision, task and checklist. | Document/checklist evidence gaps. | Do not modify an approved instruction or authorize machine operation. |
| shift-handoff | Shift records, deviation evidence and next-shift context. | Draft handoff with deviations and owners. | Do not infer permission to continue unsafe work. |

## manufacturing-technician

Support technical troubleshooting and controlled documentation. [Manifest](https://github.com/jeremylongworth-source/AgentManufacturing/blob/main/skillsets/manufacturing-technician/skillset.yaml).

| Workflow | Required evidence | Output | Review boundary |
|---|---|---|---|
| troubleshooting | Equipment/process identity, event history and supplied parameter limits. | Troubleshooting evidence brief. | Do not change live setpoints or bypass controls. |
| instruction-change | Approved method, source revision and proposed change. | Draft instruction and validation gaps. | No document release or engineering approval. |

## production-supervisor

Translate approved plans into shift-level review and handoff. [Manifest](https://github.com/jeremylongworth-source/AgentManufacturing/blob/main/skillsets/production-supervisor/skillset.yaml).

| Workflow | Required evidence | Output | Review boundary |
|---|---|---|---|
| shift-plan | Approved plan, readiness, staffing qualifications and shift window. | Shift allocation proposal with unmet constraints. | Do not approve overtime or unqualified assignments. |
| shift-review | Planned/actual order history and shift records. | Schedule exceptions and next-shift handoff. | No live rescheduling or unsafe-work direction. |

## production-planner

Build and compare evidence-based production planning proposals. [Manifest](https://github.com/jeremylongworth-source/AgentManufacturing/blob/main/skillsets/production-planner/skillset.yaml).

| Workflow | Required evidence | Output | Review boundary |
|---|---|---|---|
| horizon-plan | Demand horizon, capacity, BOM, materials and labor basis. | Production plan proposal and readiness gaps. | No order release, purchasing or business commitment. |
| scenario-review | Order constraints, comparable scenarios and capacity evidence. | Scenario comparison with capacity constraints. | Do not turn a recommendation into dispatch authority. |

## process-technician

Review process records and deviations against controlled evidence. [Manifest](https://github.com/jeremylongworth-source/AgentManufacturing/blob/main/skillsets/process-technician/skillset.yaml).

| Workflow | Required evidence | Output | Review boundary |
|---|---|---|---|
| parameter-review | Process boundary, input/output records and approved parameter criteria. | Parameter-control evidence gaps. | No process setpoint change. |
| deviation-review | Current revision, observation and affected process/product. | Deviation and nonconformance draft. | Do not infer root cause or disposition. |

## manufacturing-engineer-support

Prepare process and change evidence for engineering review. [Manifest](https://github.com/jeremylongworth-source/AgentManufacturing/blob/main/skillsets/manufacturing-engineer-support/skillset.yaml).

| Workflow | Required evidence | Output | Review boundary |
|---|---|---|---|
| process-design-review | Product requirements, process maps, alternatives and constraints. | Process options and draft control plan. | No design validation or engineering signoff. |
| change-review | Change package, technical basis and affected process records. | Change impacts and review handoff. | No change activation, machine release or certification. |

## industrial-engineering-specialist

Analyze production capacity and work balance from declared measurements. [Manifest](https://github.com/jeremylongworth-source/AgentManufacturing/blob/main/skillsets/industrial-engineering-specialist/skillset.yaml).

| Workflow | Required evidence | Output | Review boundary |
|---|---|---|---|
| line-balance | Cycle observations, demand, time units and task constraints. | Balance proposal with measured constraints. | No unsafe pace or workplace redesign approval. |
| capacity-review | Capacity basis, equipment downtime and production context. | Capacity and bottleneck evidence brief. | Do not infer causation from a utilization percentage. |

## quality-technician

Prepare inspection and conformity evidence for authorized quality review. [Manifest](https://github.com/jeremylongworth-source/AgentManufacturing/blob/main/skillsets/quality-technician/skillset.yaml).

| Workflow | Required evidence | Output | Review boundary |
|---|---|---|---|
| inspection | Product requirements, measurement method and inspection scope. | Draft inspection plan and method gaps. | No acceptance criteria invented. |
| conformity | Applicable requirements, actual records and affected product. | Conformity evidence and nonconformance draft. | No product release or disposition. |

## quality-engineer-support

Support quality investigation, capability and release evidence. [Manifest](https://github.com/jeremylongworth-source/AgentManufacturing/blob/main/skillsets/quality-engineer-support/skillset.yaml).

| Workflow | Required evidence | Output | Review boundary |
|---|---|---|---|
| corrective-action | Nonconformance, containment, causal evidence and verification plan. | Causal evidence and action/effectiveness review. | Do not convert a proposed cause into a verified one. |
| capability | Measurement-system evidence, process stability, specs and within sigma. | Readiness gaps or supported capability calculation. | No product acceptance; do not substitute overall sigma. |
| release-evidence | Applicable requirements, product evidence and quality records. | Review package with unresolved evidence. | Only an authorized owner can release product. |

## metrology-specialist

Review measurement suitability, calibration and traceability evidence. [Manifest](https://github.com/jeremylongworth-source/AgentManufacturing/blob/main/skillsets/metrology-specialist/skillset.yaml).

| Workflow | Required evidence | Output | Review boundary |
|---|---|---|---|
| measurement-system | Measurand, method, equipment and measurement-study design. | Measurement suitability and study evidence review. | No invented study results or calibration certification. |
| calibration-risk | Register, calibration documents, use history and traceability. | Calibration evidence and affected-use handoff. | Do not declare affected product acceptable. |

## supplier-quality-specialist

Review supplier evidence and draft corrective-action requests. [Manifest](https://github.com/jeremylongworth-source/AgentManufacturing/blob/main/skillsets/supplier-quality-specialist/skillset.yaml).

| Workflow | Required evidence | Output | Review boundary |
|---|---|---|---|
| supplier-review | Supplier scope, qualification records, certificate and product requirements. | Supplier evidence gaps. | No supplier approval or certificate validation by assertion. |
| supplier-action | Linked defect counts, nonconformance and supplier context. | Defect review and supplier-action draft. | Do not send the request or approve supplier changes. |

## maintenance-planner

Prepare maintenance priorities and plans from backlog and failure evidence. [Manifest](https://github.com/jeremylongworth-source/AgentManufacturing/blob/main/skillsets/maintenance-planner/skillset.yaml).

| Workflow | Required evidence | Output | Review boundary |
|---|---|---|---|
| maintenance-priority | Backlog, risk criteria, resource constraints and equipment context. | Prioritized review list and parts evidence gaps. | No equipment shutdown/startup or procurement authority. |
| preventive-plan | Failure history, manufacturer information and review criteria. | Preventive maintenance proposal. | No safe-to-work declaration or isolation instructions. |

## reliability-analyst

Analyze failure and downtime evidence without promising reliability outcomes. [Manifest](https://github.com/jeremylongworth-source/AgentManufacturing/blob/main/skillsets/reliability-analyst/skillset.yaml).

| Workflow | Required evidence | Output | Review boundary |
|---|---|---|---|
| reliability-metrics | Failure counts, exposure intervals, repair durations and consistent boundaries. | Reliability metrics with population and time basis. | Do not infer future reliability or causal improvement. |
| failure-review | Failure evidence, condition data and available monitoring methods. | Failure review and monitoring proposal. | No machine fitness-for-service or safe-operation approval. |

## continuous-improvement-specialist

Shape improvement experiments from observed flow and loss evidence. [Manifest](https://github.com/jeremylongworth-source/AgentManufacturing/blob/main/skillsets/continuous-improvement-specialist/skillset.yaml).

| Workflow | Required evidence | Output | Review boundary |
|---|---|---|---|
| flow-review | Process boundary, observations, timings and waste evidence. | Flow evidence and candidate opportunities. | Do not assume every observed delay is removable. |
| changeover-improvement | Changeover records, baseline, proposed actions and comparable follow-up. | Improvement proposal and measurement comparison. | No trial activation or causal savings without evidence. |

## manufacturing-data-analyst

Assess manufacturing data lineage and metric definitions. [Manifest](https://github.com/jeremylongworth-source/AgentManufacturing/blob/main/skillsets/manufacturing-data-analyst/skillset.yaml).

| Workflow | Required evidence | Output | Review boundary |
|---|---|---|---|
| data-quality | Source extracts, identifiers, timestamps and declared schema. | Data-quality and lineage gaps. | No live ERP/MES changes or inferred missing events. |
| kpi-review | Event data, KPI definitions, units and aggregation basis. | Metric definitions and OEE evidence review. | Do not publish unvalidated metrics or combine incompatible denominators. |

## ehs-coordinator-support

Coordinate scoped hazard, jurisdiction and environmental evidence reviews. [Manifest](https://github.com/jeremylongworth-source/AgentManufacturing/blob/main/skillsets/ehs-coordinator-support/skillset.yaml).

| Workflow | Required evidence | Output | Review boundary |
|---|---|---|---|
| safety-review | Task, facility jurisdiction, equipment hazards and existing programs. | Hazard/program gaps and qualified safety handoff. | No operational JSA authorization, isolation steps or guarding approval. |
| environment-review | Facility activities, stream evidence, criteria and jurisdiction. | Environmental evidence register. | No waste classification, disposal or permit approval. |
| whmis-review | Product roles, jurisdiction, current sources, SDS/labels and training. | Role-separated WHMIS evidence gaps. | No classification, chemical-use or compliance certification. |

## operations-manager

Compare production and improvement evidence for management review. [Manifest](https://github.com/jeremylongworth-source/AgentManufacturing/blob/main/skillsets/operations-manager/skillset.yaml).

| Workflow | Required evidence | Output | Review boundary |
|---|---|---|---|
| operations-review | Comparable production plan, actuals, quality records and labor basis. | Operational exceptions and evidence gaps. | No workforce commitment or performance judgment from unverified data. |
| improvement-review | Scenario assumptions, constraints, baseline and follow-up evidence. | Management review of options and measured outcomes. | No automatic prioritization across safety/quality constraints. |

## plant-manager-support

Assemble cross-functional review evidence and decisions for responsible owners. [Manifest](https://github.com/jeremylongworth-source/AgentManufacturing/blob/main/skillsets/plant-manager-support/skillset.yaml).

| Workflow | Required evidence | Output | Review boundary |
|---|---|---|---|
| plant-review | KPI model, production readiness, qualification records and unresolved issues. | Plant review brief with unresolved decisions and owners. | Do not certify workers or release operations from a summary. |
| investment-change-review | Readiness, option costs, technical basis and change package. | Investment/change evidence and qualified handoff. | No budget commitment, purchase, engineering signoff or automation deployment. |
