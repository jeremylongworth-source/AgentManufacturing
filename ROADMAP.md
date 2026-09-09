# AgentManufacturing development roadmap

Version: 3.4 (AM-32 public readiness in progress; MIT selected)
Working directory: `D:\AgentMfg`

Source: “Branch · Plan AgentLogistics Skills”, conversation `6a9d881b-9330-83ea-b887-26309d52536d`, manufacturing proposal message `e32c7e5b-7294-4699-b383-0de485378ba7`. Saved on 2026-09-06. This is the initial planning proposal, not evidence of completed development. Conversation-only citation markers have been removed because they do not resolve in repository Markdown. Legal details and standards-edition assertions preserved from the source are planning notes and have not been independently reverified in this handoff; verify official sources before implementation or operational use.

## Current workspace status

**AM-00 through AM-31 are READY as of 2026-09-09. AM-32 is IN_PROGRESS; MIT is selected and private reporting remains unresolved.** See the [v1 taxonomy](docs/architecture/master-taxonomy-v1.md), [audit](docs/architecture/taxonomy-audit-v1.md), [index](docs/architecture/taxonomy-index.yaml), [dependency map](docs/architecture/dependency-map.md), [Canadian jurisdiction model](docs/architecture/canadian-jurisdiction-model.md), [safety boundary model](docs/architecture/safety-boundary-model.md), [skill authoring standard](docs/architecture/skill-authoring-standard.md), [source and standards standard](docs/architecture/source-standards-standard.md), [calculation standard](docs/architecture/calculation-standard.md), [validation framework](docs/architecture/validation-framework.md), [reference-skill proof contract](docs/architecture/reference-skill-proof.md), [source registries](docs/architecture/canadian-source-registry.json), and [latest handoff](docs/development/handoffs/AM-31-final-handoff.md) for evidence and the next-wave brief. The [domain contract](docs/architecture/domain-contract.md) and [scope boundaries](docs/architecture/scope-boundaries.md) govern this work. Local Git remains initialized on `main` with `origin` pointing to [AgentManufacturing](https://github.com/jeremylongworth-source/AgentManufacturing), verified private and empty during AM-00. The owner selected MIT during AM-32; no public release has been made. Roadmap work through AM-31 is committed and pushed, and AM-32 preparation continues.

The v1 catalogue contains 159 accepted records across 20 families: 153 core methods and six Canadian overlays, with audit dispositions for all 162 draft candidates and routes for all 166 representative source names. Names, responsibilities, tiers, provenance, and the evidence-reuse graph are frozen. AM-04 formalizes jurisdiction routing metadata, AM-05 formalizes safety/engineering boundaries, AM-06 formalizes portable package and validation contracts, and AM-07 formalizes source and standards handling without silently reclassifying the index or implementing skills. The AM-02 draft and original framework remain preserved. Completion tokens in the source wave definitions are acceptance targets; only the execution ledger and supporting handoffs establish earned completion.

| Wave | Status | Evidence / next action |
|---|---|---|
| AM-00 | READY | [Baseline audit](docs/development/AM-00-baseline-audit.md); `AGENTMANUFACTURING_AM_00_BASELINE_READY` |
| AM-01 | READY | [Domain contract](docs/architecture/domain-contract.md), [scope boundaries](docs/architecture/scope-boundaries.md), and [handoff](docs/development/handoffs/AM-01-final-handoff.md); `AGENTMANUFACTURING_AM_01_DOMAIN_CONTRACT_READY` |
| AM-02 | READY | [Draft taxonomy](docs/architecture/candidate-taxonomy-v0.1.md), [register](docs/architecture/candidate-register-v0.1.json), and [handoff](docs/development/handoffs/AM-02-final-handoff.md); `AGENTMANUFACTURING_AM_02_TAXONOMY_DRAFT_READY` |
| AM-03 | READY | [v1 taxonomy](docs/architecture/master-taxonomy-v1.md), [audit](docs/architecture/taxonomy-audit-v1.md), [index](docs/architecture/taxonomy-index.yaml), [dependency map](docs/architecture/dependency-map.md), and [handoff](docs/development/handoffs/AM-03-final-handoff.md); `AGENTMANUFACTURING_AM_03_MASTER_TAXONOMY_READY` |
| AM-04 | READY | [Canadian jurisdiction model](docs/architecture/canadian-jurisdiction-model.md), [source registry](docs/architecture/canadian-source-registry.json), [validator](scripts/validate-jurisdiction-model.py), and [handoff](docs/development/handoffs/AM-04-final-handoff.md); `AGENTMANUFACTURING_AM_04_JURISDICTION_MODEL_READY` |
| AM-05 | READY | [Safety boundary model](docs/architecture/safety-boundary-model.md), [source registry](docs/architecture/safety-source-registry.json), [validator](scripts/validate-safety-boundary-model.py), and [handoff](docs/development/handoffs/AM-05-final-handoff.md); `AGENTMANUFACTURING_AM_05_SAFETY_BOUNDARY_READY` |
| AM-06 | READY | [Skill authoring standard](docs/architecture/skill-authoring-standard.md), [package schema](docs/architecture/skill-package-schema.json), [validation contract](docs/architecture/skill-validation-contract.json), [templates](docs/templates/manufacturing-skill/), [validator](scripts/validate-skill-authoring-standard.py), and [handoff](docs/development/handoffs/AM-06-final-handoff.md); `AGENTMANUFACTURING_AM_06_SKILL_STANDARD_READY` |
| AM-07 | READY | [Source and standards standard](docs/architecture/source-standards-standard.md), [source schema](docs/architecture/source-record-schema.json), [freshness policy](docs/architecture/source-freshness-policy.json), [examples](docs/architecture/source-record-examples.json), [validator](scripts/validate-source-standards-standard.py), and [handoff](docs/development/handoffs/AM-07-final-handoff.md); `AGENTMANUFACTURING_AM_07_SOURCE_STANDARD_READY` |
| AM-08 | READY | [Calculation standard](docs/architecture/calculation-standard.md), [calculation contract](docs/architecture/calculation-contract.json), [worked fixtures](docs/architecture/calculation-fixtures.json), [validator](scripts/validate-calculation-standard.py), and [handoff](docs/development/handoffs/AM-08-final-handoff.md); `AGENTMANUFACTURING_AM_08_CALCULATION_STANDARD_READY` |
| AM-09 | READY | [Validation framework](docs/architecture/validation-framework.md), [framework contract](docs/architecture/validation-framework-contract.json), [scenario suite](tests/scenarios/), [routing manifest](tests/expected-routing.yaml), [fixture manifest](tests/fixtures/am09-fixture-manifest.json), [evaluation template](tests/evaluations/AM-09-evaluation-template.md), [validator](scripts/validate-validation-framework.py), [validation gate](scripts/validate-all.py), and [handoff](docs/development/handoffs/AM-09-final-handoff.md); `AGENTMANUFACTURING_AM_09_VALIDATION_FRAMEWORK_READY` |
| AM-10 | READY — hard gate passed | [Reference-skill proof contract](docs/architecture/reference-skill-proof.md), five reference packages under `skills/`, [acceptance record](tests/evaluations/AM-10-reference-skill-acceptance.md), [validator](scripts/validate-reference-skills.py), updated [routing scenarios](tests/scenarios/), and [handoff](docs/development/handoffs/AM-10-final-handoff.md); `AGENTMANUFACTURING_AM_10_REFERENCE_SKILLS_READY` |
| AM-11 | READY | Nine Family 01 and 03 packages, [acceptance record](tests/evaluations/AM-11-core-acceptance.md), [validator](scripts/validate-implemented-skills.py), [routing scenarios](tests/scenarios/), and [handoff](docs/development/handoffs/AM-11-final-handoff.md); `AGENTMANUFACTURING_AM_11_MANUFACTURING_CORE_READY` |
| AM-12 | READY | Ten Family 02 packages including the reference planner, [acceptance record](tests/evaluations/AM-12-production-planning-acceptance.md), [validator](scripts/validate-production-planning.py), [routing scenarios](tests/scenarios/), and [handoff](docs/development/handoffs/AM-12-final-handoff.md); `AGENTMANUFACTURING_AM_12_PRODUCTION_PLANNING_READY` |
| AM-13 | READY | Eighteen Family 04/05 packages, [acceptance record](tests/evaluations/AM-13-process-engineering-acceptance.md), [validator](scripts/validate-process-engineering.py), [routing scenarios](tests/scenarios/), and [handoff](docs/development/handoffs/AM-13-final-handoff.md); `AGENTMANUFACTURING_AM_13_PROCESS_ENGINEERING_READY` |
| AM-14 | READY | Seven Family 06 packages, [acceptance record](tests/evaluations/AM-14-quality-management-acceptance.md), [validator](scripts/validate-quality-management.py), [routing scenarios](tests/scenarios/), and [handoff](docs/development/handoffs/AM-14-final-handoff.md); `AGENTMANUFACTURING_AM_14_QUALITY_MANAGEMENT_READY` |
| AM-15 | READY | Sixteen Family 07/08 packages, [acceptance record](tests/evaluations/AM-15-metrology-spc-acceptance.md), [validator](scripts/validate-metrology-spc.py), [routing scenarios](tests/scenarios/), and [handoff](docs/development/handoffs/AM-15-final-handoff.md); `AGENTMANUFACTURING_AM_15_PROCESS_QUALITY_READY` |
| AM-16 | READY | Ten Family 09 packages, [acceptance record](tests/evaluations/AM-16-nonconformance-capa-acceptance.md), [validator](scripts/validate-nonconformance-capa.py), [routing scenarios](tests/scenarios/), and [handoff](docs/development/handoffs/AM-16-final-handoff.md); `AGENTMANUFACTURING_AM_16_CAPA_READY` |
| AM-17 | READY | Ten Family 10 packages, [acceptance record](tests/evaluations/AM-17-maintenance-reliability-acceptance.md), [validator](scripts/validate-maintenance-reliability.py), [routing scenarios](tests/scenarios/), and [handoff](docs/development/handoffs/AM-17-final-handoff.md); `AGENTMANUFACTURING_AM_17_RELIABILITY_READY` |
| AM-18 | READY | Nine Family 11 packages, [acceptance record](tests/evaluations/AM-18-manufacturing-safety-acceptance.md), [validator](scripts/validate-manufacturing-safety.py), [routing scenarios](tests/scenarios/), and [handoff](docs/development/handoffs/AM-18-final-handoff.md); `AGENTMANUFACTURING_AM_18_SAFETY_READY` |
| AM-19 | READY | Nine Family 12 packages, [acceptance record](tests/evaluations/AM-19-materials-traceability-acceptance.md), [validator](scripts/validate-materials-traceability.py), [routing scenarios](tests/scenarios/), and [handoff](docs/development/handoffs/AM-19-final-handoff.md); `AGENTMANUFACTURING_AM_19_MATERIAL_TRACEABILITY_READY` |
| AM-20 | READY | Eight Family 13 packages, [acceptance record](tests/evaluations/AM-20-workforce-acceptance.md), [validator](scripts/validate-workforce-shift.py), [routing scenarios](tests/scenarios/), and [handoff](docs/development/handoffs/AM-20-final-handoff.md); `AGENTMANUFACTURING_AM_20_WORKFORCE_READY` |
| AM-21 | READY | Eight Family 14 packages, [acceptance record](tests/evaluations/AM-21-continuous-improvement-acceptance.md), [validator](scripts/validate-lean-improvement.py), [routing scenarios](tests/scenarios/), and [handoff](docs/development/handoffs/AM-21-final-handoff.md); `AGENTMANUFACTURING_AM_21_CONTINUOUS_IMPROVEMENT_READY` |
| AM-22 | READY | Eight Family 15 packages, [acceptance record](tests/evaluations/AM-22-systems-data-acceptance.md), [validator](scripts/validate-systems-data.py), [routing scenarios](tests/scenarios/), and [handoff](docs/development/handoffs/AM-22-final-handoff.md); `AGENTMANUFACTURING_AM_22_SYSTEMS_DATA_READY` |
| AM-23 | READY | Eight Family 16 packages, [acceptance record](tests/evaluations/AM-23-advanced-manufacturing-acceptance.md), [validator](scripts/validate-advanced-manufacturing.py), [routing scenarios](tests/scenarios/), and [handoff](docs/development/handoffs/AM-23-final-handoff.md); `AGENTMANUFACTURING_AM_23_ADVANCED_MANUFACTURING_READY` |
| AM-24 | READY | Fourteen Family 17/18 packages, [acceptance record](tests/evaluations/AM-24-supplier-change-acceptance.md), [validator](scripts/validate-supplier-change.py), [fixtures](tests/fixtures/am24-supplier-defect.json), and [handoff](docs/development/handoffs/AM-24-final-handoff.md); `AGENTMANUFACTURING_AM_24_SUPPLIER_CHANGE_CONTROL_READY` |
| AM-25 | READY | Six Family 19 packages, [acceptance record](tests/evaluations/AM-25-environment-energy-waste-acceptance.md), [validator](scripts/validate-environment-energy-waste.py), [source evidence](docs/development/AM-25-source-evidence.md), and [handoff](docs/development/handoffs/AM-25-final-handoff.md); `AGENTMANUFACTURING_AM_25_ENVIRONMENTAL_READY` |
| AM-26 | READY | Eight Family 20 capabilities, [acceptance record](tests/evaluations/AM-26-federal-capabilities-acceptance.md), [validator](scripts/validate-canadian-federal.py), [source evidence](docs/development/AM-26-source-evidence.md), and [handoff](docs/development/handoffs/AM-26-final-handoff.md); `AGENTMANUFACTURING_AM_26_CANADA_FEDERAL_READY` |
| AM-27 | READY | Provincial selector, four modules, [acceptance record](tests/evaluations/AM-27-provincial-acceptance.md), [validator](scripts/validate-provincial-overlays.py), [source evidence](docs/development/AM-27-source-evidence.md), and [handoff](docs/development/handoffs/AM-27-final-handoff.md); `AGENTMANUFACTURING_AM_27_PROVINCIAL_BASELINE_READY` |
| AM-28 | READY | Eighteen professional skillsets, [composition contract](docs/architecture/professional-skillset-contract.md), [acceptance record](tests/evaluations/AM-28-professional-skillsets-acceptance.md), [validator](scripts/validate-professional-skillsets.py), and [handoff](docs/development/handoffs/AM-28-final-handoff.md); `AGENTMANUFACTURING_AM_28_PROFESSIONAL_SKILLSETS_READY` |
| AM-29 | READY | [Sector framework](docs/architecture/sector-specialization-framework.md), [registry](specializations/registry.json), [acceptance record](tests/evaluations/AM-29-specialization-acceptance.md), [validator](scripts/validate-sector-framework.py), and [handoff](docs/development/handoffs/AM-29-final-handoff.md); `AGENTMANUFACTURING_AM_29_SPECIALIZATION_FRAMEWORK_READY` |
| AM-30 | READY | [Assisted integration evaluation](tests/evaluations/AM-30-integration-acceptance.md), [checker](scripts/validate-integration-evaluation.py), and [handoff](docs/development/handoffs/AM-30-final-handoff.md); independent runtime NOT_RUN; `AGENTMANUFACTURING_AM_30_INTEGRATION_VALIDATED` |
| AM-31 | READY | [Assisted safety evaluation](tests/evaluations/AM-31-safety-acceptance.md), [checker](scripts/validate-adversarial-safety.py), and [handoff](docs/development/handoffs/AM-31-final-handoff.md); independent runtime NOT_RUN; `AGENTMANUFACTURING_AM_31_SAFETY_VALIDATED` |
| AM-32 | IN_PROGRESS | [Public-readiness record](docs/development/AM-32-public-readiness.md), [acceptance](tests/evaluations/AM-32-public-readiness-acceptance.md), and [progress handoff](docs/development/handoffs/AM-32-progress-handoff.md). MIT selected; private reporting contact/recipient pending. |
| AM-33 | NOT_STARTED | Audit after public-readiness prerequisites pass. |

Read the v1 index, audit, and dependency map alongside the AM-01 contract and scope boundaries. The [AM-02 register](docs/architecture/candidate-register-v0.1.json), [initial taxonomy](docs/architecture/master-taxonomy-v0.1.md), and [domain framework](docs/architecture/domain-framework.md) preserve prior planning. AM-10 permits bounded family waves, but each package still requires the same structural, scenario, deterministic, source, and safety evidence.

## Source roadmap

I would use `AM` as the wave prefix.

## AM-00: Repository baseline

Inspect the new repository and relevant patterns from AgentSkills and AgentLogistics.

Required artifact:

```text
docs/development/AM-00-baseline-audit.md
```

Completion:

```text
AGENTMANUFACTURING_AM_00_BASELINE_READY
```

## AM-01: Domain contract

Freeze:

- manufacturing definition
- what is core
- AgentLogistics boundary
- engineering boundaries
- sector-specialization model
- Canadian jurisdiction model

Artifacts:

```text
docs/architecture/domain-contract.md
docs/architecture/scope-boundaries.md
```

Token:

```text
AGENTMANUFACTURING_AM_01_DOMAIN_CONTRACT_READY
```

## AM-02: Master taxonomy v0.1

Enumerate the 20 families into candidate atomic skills.

For each candidate record:

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

Target outcome is an audited taxonomy, not a predetermined skill count.

Token:

```text
AGENTMANUFACTURING_AM_02_TAXONOMY_DRAFT_READY
```

## AM-03: Taxonomy audit and v1 freeze

Audit every candidate for:

- atomicity
- duplicate responsibility
- naming
- dependency order
- regulatory scope
- engineering boundary
- testability
- specialization need

Artifacts:

```text
docs/architecture/master-taxonomy-v1.md
docs/architecture/dependency-map.md
docs/architecture/taxonomy-index.yaml
```

Token:

```text
AGENTMANUFACTURING_AM_03_MASTER_TAXONOMY_READY
```

## AM-04: Canadian jurisdiction model

Define:

```text
CANADA_FEDERAL
PROVINCIAL_REQUIRED
SECTOR_REGULATED
STANDARDS_DEPENDENT
```

Build federal/provincial source hierarchy and the initial Ontario, B.C., Alberta and Quebec extension pattern.

Token:

```text
AGENTMANUFACTURING_AM_04_JURISDICTION_MODEL_READY
```

## AM-05: Safety and engineering boundary

Formalize:

```text
ROUTINE
REGULATED
HAZARDOUS_OPERATION
ENGINEERING_OR_CERTIFICATION_BOUNDARY
```

Explicitly gate:

- machine guarding
- hazardous energy
- electrical work
- pressure equipment
- robotics
- confined spaces
- hot work
- hazardous chemicals
- structural changes

Token:

```text
AGENTMANUFACTURING_AM_05_SAFETY_BOUNDARY_READY
```

## AM-06: Skill authoring standard

Carry forward the AgentSkills approach of small portable skills, output contracts and scenario validation. 

Define:

```text
SKILL.md
agents/openai.yaml
references/
optional assets/
tests
```

Token:

```text
AGENTMANUFACTURING_AM_06_SKILL_STANDARD_READY
```

## AM-07: Source and standards standard

Establish:

- government-source precedence
- standards metadata
- copyrighted-standard handling
- version/freshness controls
- provincial regulatory sourcing
- sector-standard sourcing

Artifacts:

```text
docs/architecture/source-standards-standard.md
docs/architecture/source-record-schema.json
docs/architecture/source-freshness-policy.json
docs/architecture/source-record-examples.json
scripts/validate-source-standards-standard.py
```

Token:

```text
AGENTMANUFACTURING_AM_07_SOURCE_STANDARD_READY
```

## AM-08: Calculation standard

Before quantitative skills scale, define:

- variables
- units
- formulas
- assumptions
- rounding
- missing inputs
- edge cases
- worked fixtures

Reference calculations should include:

```text
takt
capacity
OEE
FPY
scrap
MTBF
MTTR
Cp
Cpk
control limits
```

Artifacts:

```text
docs/architecture/calculation-standard.md
docs/architecture/calculation-contract.json
docs/architecture/calculation-fixtures.json
scripts/validate-calculation-standard.py
```

Token:

```text
AGENTMANUFACTURING_AM_08_CALCULATION_STANDARD_READY
```

## AM-09: Validation framework

Use the AgentSkills pattern of expected-routing scenarios and automated validators. AgentSkills currently uses scenario routing checks against expected routing fixtures. 

Test categories:

```text
correct routing
wrong routing
missing data
wrong units
unsafe request
wrong jurisdiction
stale standard
unsupported engineering signoff
calculation fixture
```

Artifacts:

```text
docs/architecture/validation-framework.md
docs/architecture/validation-framework-contract.json
tests/scenarios/*.md
tests/expected-routing.yaml
tests/fixtures/am09-fixture-manifest.json
tests/evaluations/AM-09-evaluation-template.md
scripts/validate-validation-framework.py
scripts/validate-all.py
```

Token:

```text
AGENTMANUFACTURING_AM_09_VALIDATION_FRAMEWORK_READY
```

## AM-10: Reference skills

Prove one skill from each major class before bulk authoring.

Recommended:

```text
calculate-oee
build-production-plan
triage-nonconformance
review-lockout-program
assess-made-in-canada-claim
```

Hard gate:

```text
NO MASS AUTHORING BEFORE AM-10 READY
```

Token:

```text
AGENTMANUFACTURING_AM_10_REFERENCE_SKILLS_READY
```

## AM-11: Manufacturing fundamentals and standard work

Build Families 01 and 03.

Token:

```text
AGENTMANUFACTURING_AM_11_MANUFACTURING_CORE_READY
```

## AM-12: Production planning and scheduling

Build Family 02.

Token:

```text
AGENTMANUFACTURING_AM_12_PRODUCTION_PLANNING_READY
```

## AM-13: Process and industrial engineering

Build Families 04 and 05.

Token:

```text
AGENTMANUFACTURING_AM_13_PROCESS_ENGINEERING_READY
```

## AM-14: Quality management and inspection

Build Family 06.

Token:

```text
AGENTMANUFACTURING_AM_14_QUALITY_MANAGEMENT_READY
```

## AM-15: Metrology, SPC and capability

Build Families 07 and 08.

Hard test examples:

```text
specification limit ≠ control limit
precision ≠ accuracy
stable process ≠ capable process
```

Token:

```text
AGENTMANUFACTURING_AM_15_PROCESS_QUALITY_READY
```

## AM-16: Nonconformance, RCA and CAPA

Build Family 09.

Token:

```text
AGENTMANUFACTURING_AM_16_CAPA_READY
```

## AM-17: Maintenance and reliability

Build Family 10.

Token:

```text
AGENTMANUFACTURING_AM_17_RELIABILITY_READY
```

## AM-18: Manufacturing safety

Build Family 11.

Focus on recognition, assessment, documentation and escalation.

Do not create skills for bypassing guards, defeating interlocks or unsafe energy-control shortcuts.

Token:

```text
AGENTMANUFACTURING_AM_18_SAFETY_READY
```

## AM-19: Materials, BOM and traceability

Build Family 12.

Explicitly stop at the manufacturing/warehouse interface.

Token:

```text
AGENTMANUFACTURING_AM_19_MATERIAL_TRACEABILITY_READY
```

## AM-20: Workforce and shift operations

Build Family 13.

Token:

```text
AGENTMANUFACTURING_AM_20_WORKFORCE_READY
```

## AM-21: Lean and continuous improvement

Build Family 14.

Token:

```text
AGENTMANUFACTURING_AM_21_CONTINUOUS_IMPROVEMENT_READY
```

## AM-22: Manufacturing systems and data

Build Family 15.

Cover system mapping and data analysis, but not unreviewed live PLC/SCADA control changes.

Token:

```text
AGENTMANUFACTURING_AM_22_SYSTEMS_DATA_READY
```

## AM-23: Automation and advanced manufacturing

Build Family 16.

Cover robotics, machine vision, additive manufacturing and automation assessment. ISED specifically identifies robotics, additive manufacturing and data analytics as major advanced-manufacturing technologies. 

Token:

```text
AGENTMANUFACTURING_AM_23_ADVANCED_MANUFACTURING_READY
```

## AM-24: Supplier quality and engineering change

Build Families 17 and 18.

Token:

```text
AGENTMANUFACTURING_AM_24_SUPPLIER_CHANGE_CONTROL_READY
```

## AM-25: Environment, energy and waste

Build Family 19.

ISO 14001:2026 can serve as an important framework reference without reproducing protected standard text. 

Token:

```text
AGENTMANUFACTURING_AM_25_ENVIRONMENTAL_READY
```

## AM-26: Canadian federal manufacturing compliance

Build Family 20 federal capabilities:

```text
WHMIS framework
origin claims
general non-food labelling
federal/provincial routing
source freshness
```

Token:

```text
AGENTMANUFACTURING_AM_26_CANADA_FEDERAL_READY
```

## AM-27: Initial provincial overlays

Build source-bounded modules for:

```text
ontario
british-columbia
alberta
quebec
```

Focus on:

- OH&S
- machinery
- hazardous energy
- electrical
- pressure equipment
- environmental obligations
- worker training

Do not assume requirements are identical across provinces.

Token:

```text
AGENTMANUFACTURING_AM_27_PROVINCIAL_BASELINE_READY
```

## AM-28: Professional skillsets

Compose the atomic skills into the professional roles listed earlier.

Token:

```text
AGENTMANUFACTURING_AM_28_PROFESSIONAL_SKILLSETS_READY
```

## AM-29: Sector specialization framework

Create architecture and priorities for:

```text
automotive
aerospace
food-beverage
medical-devices
fabricated-metals
welding
machinery
electronics
plastics-rubber
chemicals
wood-paper
transportation-equipment
```

Do not build all of them in this wave.

Token:

```text
AGENTMANUFACTURING_AM_29_SPECIALIZATION_FRAMEWORK_READY
```

## AM-30: Integration evaluation

Test multi-domain scenarios.

**Production shortfall**

```text
schedule
→ cycle time
→ downtime
→ material
→ labor
→ bottleneck
→ recovery plan
```

**Quality escape**

```text
defect
→ containment
→ traceability
→ measurement
→ root cause
→ CAPA
→ effectiveness
```

**Equipment reliability**

```text
downtime
→ failure history
→ MTBF / MTTR
→ maintenance
→ spare parts
→ improvement
```

**Safety-sensitive process change**

```text
engineering change
→ machine hazard
→ guarding / energy
→ jurisdiction
→ qualified review
```

Token:

```text
AGENTMANUFACTURING_AM_30_INTEGRATION_VALIDATED
```

## AM-31: Adversarial safety evaluation

Test requests attempting to:

```text
bypass machine guard
defeat interlock
avoid lockout
modify live PLC unsafely
override safety circuit
conceal nonconformance
falsify inspection data
misrepresent Canadian origin
```

The system should preserve safe analysis while refusing unsafe implementation.

Token:

```text
AGENTMANUFACTURING_AM_31_SAFETY_VALIDATED
```

## AM-32: Public readiness

Required:

```text
README.md
ROADMAP.md
AGENTS.md
CONTRIBUTING.md
SECURITY.md
CODE_OF_CONDUCT.md
CHANGELOG.md
LICENSE
```

Token:

```text
AGENTMANUFACTURING_AM_32_PUBLIC_READINESS_READY
```

## AM-33: v1 release-candidate audit

Audit:

```text
taxonomy coverage
routing
calculations
Canadian sources
standards freshness
quality
safety
provincial isolation
professional skillsets
specialization boundaries
integration
documentation
CI
```

Verdict:

```text
V1_READY
V1_PARTIALLY_READY
V1_BLOCKED
```

Token:

```text
AGENTMANUFACTURING_AM_33_V1_RC_AUDIT_COMPLETE
```

# Codex execution protocol

Every wave should use the same bounded pattern that worked well in AgentLogistics:

```text
1. Read ROADMAP.md and latest handoff
2. Inspect repository truth
3. Declare IN SCOPE / OUT OF SCOPE
4. Research authoritative sources
5. Implement only the wave
6. Run validation
7. Review diff
8. Produce final handoff
```

Recommended handoff:

```text
docs/development/handoffs/AM-XX-final-handoff.md
```

with:

```text
# Wave
# Objective
# Verdict
# Completion Token
# Scope Completed
# Files Added
# Files Modified
# Research Performed
# Sources
# Validation Performed
# Tests
# Regulatory / Safety Review
# Known Limitations
# Explicitly Not Completed
# Recommended Next Wave
```

# First Codex prompt

Historical bootstrap prompt, satisfied by AM-00. For subsequent work, read the latest handoff and execute only the next unfinished wave under the same bounded protocol.

```text
Treat ROADMAP.md as planning authority for AgentManufacturing, but treat
the repository itself as execution truth.

Begin only with AM-00.

Do not implement later waves.

Inspect the repository and establish its actual current state.

Review AgentSkills and AgentLogistics only as architectural references.
Preserve the AgentSkills principles of atomic skills, portable skillsets,
clear output contracts, scenario validation, and reviewable safety boundaries.

Do not copy logistics-specific content into AgentManufacturing.

Produce:

docs/development/AM-00-baseline-audit.md

Do not create the proposed full directory structure unless a directory is
required by actual AM-00 work.

Close AM-00 with READY, PARTIALLY_READY, or BLOCKED.

Include the completion token only when justified:

AGENTMANUFACTURING_AM_00_BASELINE_READY

Produce the required final handoff and recommend AM-01 only after AM-00
is genuinely closed.
```

## Roadmap status

```text
Working project: AgentManufacturing
Roadmap version: 1.1
Initial families: 20
Estimated eventual core taxonomy: ~220-280 atomic skills

Last closed wave: AM-31 (READY, bounded assisted evaluation, 2026-09-09)
Current execution target: AM-32
Accepted v1 catalogue: 159 (153 core; 6 Canadian overlays; not implemented)
Preserved AM-02 draft: 162 candidates
Taxonomy freeze: AM-03
Architecture/validation gate: AM-10 reference packages
Production core: AM-13
Quality core: AM-16
Reliability/safety core: AM-18
Systems/advanced manufacturing: AM-23
Canadian baseline: AM-27
Professional skillsets: AM-28
Integration: AM-30
Safety validation: AM-31
Public readiness: AM-32
v1 decision: AM-33
```
