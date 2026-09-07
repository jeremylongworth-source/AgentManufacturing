# AgentManufacturing domain framework

**Status:** Initial planning framework; not implemented or frozen. This document preserves the framework from the referenced “Branch · Plan AgentLogistics Skills” conversation for Codex development. It is not an engineering approval, regulatory determination, or statement that a roadmap wave is complete. Saved on 2026-09-06 from conversation `6a9d881b-9330-83ea-b887-26309d52536d`. See [ROADMAP.md](../../ROADMAP.md) for execution order, completion tokens, execution protocol, first Codex prompt, and current status.

**AM-01 supersession note (2026-09-06):** The [domain contract](domain-contract.md) and [scope boundaries](scope-boundaries.md) now govern manufacturing scope, logistics handoffs, engineering limits, sector composition, and the Canadian jurisdiction model. The remaining text is the preserved initial proposal, including its original directory snapshot and unresolved-at-the-time statements. Its sector list is reconciled in D-05 of the contract. It is not the current execution ledger or evidence of implemented skills.

## Scope and architecture

AgentManufacturing is the proposed Canadian manufacturing counterpart to AgentLogistics. Its audience is Codex contributors building a portable, vendor-neutral library of manufacturing decision-support skills for commercial operations in Canada, covering discrete and process manufacturing.

The architecture is a sector-neutral core of atomic skills, composed into professional skillsets, with Canadian jurisdiction and sector overlays. Each skill should have explicit inputs, outputs, dependencies, safety boundaries, and scenario validation. Skillsets compose existing procedures rather than duplicating them. The [initial master taxonomy](master-taxonomy-v0.1.md) defines 20 families and representative candidates; the candidate count remains an audit outcome, not a production target.

The proposed flow is: classify the operation and request → identify jurisdiction and sector → classify safety and authority limits → route to atomic skills or a composed skillset → produce a reviewable output with assumptions, evidence, and required escalation. This is a planned routing model, not an implemented runtime.

The core includes production planning, standard work, process and industrial engineering support, quality, metrology, SPC, CAPA, maintenance, safety program review, production materials and traceability, shift operations, continuous improvement, manufacturing data, automation assessment, supplier quality, change control, environmental performance, and cross-sector Canadian governance.

## Canadian jurisdiction model

The proposed jurisdiction labels are:

| Label | Planning purpose |
|---|---|
| `CANADA_FEDERAL` | Identify and verify applicable federal sources and obligations. |
| `PROVINCIAL_REQUIRED` | Require province or territory context and the applicable workplace or other local regulatory overlay. |
| `SECTOR_REGULATED` | Route sector-dependent requirements to the relevant specialization. |
| `STANDARDS_DEPENDENT` | Identify the applicable standard, edition, access requirements, and verification status. |

AM-04 will formalize the source hierarchy and an initial extension pattern for federal Canada, Ontario, British Columbia, Alberta, and Quebec. That starter pattern is not a complete statement of Canadian coverage. Requirements must be routed by the actual operation, jurisdiction, and sector; the repository must not rely on one universal Canadian rule file.

WHMIS, origin claims, non-food labelling, and provincial safety overlays are proposed research and review areas. Their applicable legal details and current official sources must be verified during the corresponding work. This framework does not preserve time-sensitive thresholds or standard-edition claims as verified current facts.

## Safety and engineering boundaries

| Safety class | Representative activity | Boundary |
|---|---|---|
| `ROUTINE` | OEE calculations, production plans, scrap analysis | Expose data limitations, assumptions, and interpretation. |
| `REGULATED` | WHMIS readiness or Canadian-origin claim review | Verify applicable sources and jurisdiction; provide review support within the defined authority limits. |
| `HAZARDOUS_OPERATION` | Lockout program, machine guarding, or confined-space program review | Support hazard identification and program review; require qualified review for hazardous execution. |
| `ENGINEERING_OR_CERTIFICATION_BOUNDARY` | Machine safety approval, electrical or pressure-system design, robot safety validation, structural changes | Planning and escalation only; no substitute for required engineering or certification authority. |

AM-05 must explicitly gate machine guarding, hazardous energy, electrical work, pressure equipment, robotics, confined spaces, hot work, hazardous chemicals, and structural changes. Skills must not impersonate an authorized inspector, engineer, certification body, or other required qualified professional. Quality-release packages support authorized decisions. Live production controls and live robot or PLC modification remain outside the general core.

Quantitative skills must expose variables, units, assumptions, formula, and interpretation. SPC must distinguish specification limits from process control limits and test that distinction. Root-cause work should follow symptom → containment → evidence → root cause → corrective action → verification → standardization.

## AgentLogistics boundary

| Repository | Primary operational responsibility |
|---|---|
| AgentManufacturing | BOM → line-side → production → finished product |
| AgentLogistics | Receiving → storage → warehouse → freight → distribution |

Manufacturing materials work concerns BOM integrity, component use, line-side shortages, production consumption, lots, and genealogy. Warehouse and freight depth belongs to AgentLogistics. Future interoperability should define handoffs and shared references without duplicating either repository's core procedures.

## Professional skillsets

The proposed skillset layer contains these 18 compositions; none is implemented by this starter framework:

```text
production-operator-support
manufacturing-technician
production-supervisor
production-planner
process-technician
manufacturing-engineer-support
industrial-engineering-specialist
quality-technician
quality-engineer-support
metrology-specialist
supplier-quality-specialist
maintenance-planner
reliability-analyst
continuous-improvement-specialist
manufacturing-data-analyst
ehs-coordinator-support
operations-manager
plant-manager-support
```

## Standards and sector overlays

Do not copy licensed standards into the repository. Preserve reference metadata and verify freshness before describing an edition as current:

```yaml
standard:
edition:
status:
jurisdiction:
official_source:
last_verified:
licensed_text_required:
used_by:
```

Sector standards and specialized requirements belong in the relevant overlay. The source proposal identifies IATF 16949, ISO 13485, AS9100, CWB/CSA welding requirements, and food-safety systems as examples requiring sector-specific treatment, not automatic applicability across the core.

Future sector overlays proposed in the conversation:

```text
automotive
aerospace
food-beverage
medical-devices
pharmaceuticals
fabricated-metals
welding
machinery
electronics
electrical-equipment
plastics-rubber
wood-products
pulp-paper
chemicals
process-manufacturing
transportation-equipment
additive-manufacturing
```

## Repository structure

The starter workspace at `D:\AgentMfg` contains only the practical planning documents:

```text
D:\AgentMfg\
├── README.md
├── ROADMAP.md
└── docs/
    └── architecture/
        ├── master-taxonomy-v0.1.md
        └── domain-framework.md
```

The larger structure below is proposed for later roadmap work. These paths are not a request to create empty directories or bulk-author skills:

```text
AgentManufacturing/
├── README.md, ROADMAP.md, AGENTS.md
├── CONTRIBUTING.md, CHANGELOG.md, SECURITY.md, LICENSE
├── docs/
│   ├── architecture/
│   ├── standards/
│   ├── development/
│   ├── evaluation/
│   └── research/
├── skills/
│   ├── manufacturing-fundamentals/
│   ├── production-planning/
│   ├── standard-work/
│   ├── process-engineering/
│   ├── industrial-engineering/
│   ├── quality-management/
│   ├── metrology/
│   ├── spc-capability/
│   ├── nonconformance-capa/
│   ├── maintenance-reliability/
│   ├── manufacturing-safety/
│   ├── materials-traceability/
│   ├── workforce-shift-operations/
│   ├── lean-continuous-improvement/
│   ├── manufacturing-systems-data/
│   ├── automation-advanced-manufacturing/
│   ├── supplier-quality/
│   ├── engineering-change/
│   ├── environment-energy-waste/
│   └── canada-compliance/
├── skillsets/
├── specializations/
│   ├── canada/                  # Federal and initial provincial overlays
│   └── <sector>/                # Sector candidates listed above
├── shared/
├── tests/
└── scripts/
```

Atomic packages are planned around `SKILL.md`, `agents/openai.yaml`, `references/`, optional `assets/`, and tests. Later waves must define the exact authoring contract, shared responsibilities, dependencies, and validation rules before broad implementation.

## Validation and unresolved decisions

This is a preservation and organization of the conversation's proposal, with time-sensitive legal and standards claims excluded from the framework summary. No candidate skill, jurisdiction model, safety gate, or professional skillset has been implemented or validated here.

AM-00 must inspect the workspace and relevant AgentSkills/AgentLogistics patterns. Subsequent waves must settle the domain contract, candidate atomicity and naming, dependency order, source freshness, sector applicability, testability, and qualified-review boundaries. Revisit this summary when those artifacts are approved or when a later wave changes the scope. Saving this document does not complete AM-01 through AM-05.
