# AgentManufacturing domain contract

Version: 1.0

Status: AM-01 contract; validation recorded in the [AM-01 handoff](../development/handoffs/AM-01-final-handoff.md).

## Purpose and authority

AgentManufacturing is a portable, vendor-neutral library of decision-support procedures for commercial manufacturing operations in Canada. It serves contributors building skills and manufacturing practitioners reviewing the resulting analysis, plans, records, and escalation packages. It covers discrete, batch, continuous, and mixed production contexts without assuming that one method fits them all.

This document and [scope-boundaries.md](scope-boundaries.md) freeze the six domain decisions required by AM-01. They govern subsequent authoring within the [roadmap](../../ROADMAP.md). The [domain framework](domain-framework.md) and [initial taxonomy](master-taxonomy-v0.1.md) remain historical planning inputs where they differ from this contract. AM-03 subsequently froze the accepted v1 taxonomy; this contract remains its boundary authority. No skills, overlays, runtime router, or model behavior are implemented by these documents.

## D-01: Manufacturing definition

For project routing, manufacturing means the organized transformation or assembly of materials and components into finished or intermediate goods, including production blending and finishing. This scope is informed by Statistics Canada's NAICS 2022 manufacturing description, which includes transformation, assembly, blending, finishing, and work on materials owned by another establishment. The classification also has exceptions; transformation alone is not enough to assign an establishment to manufacturing. [Statistics Canada, manufacturing sector description](https://www23.statcan.gc.ca/imdb/p3VD.pl?CLV=2&CPV=31-33&CST=27012022&CVD=1381563&Function=getVD&MLV=6&TVD=1381557).

The project definition is a workflow boundary, not a formal NAICS classification or legal determination. Route by the requested work and evidence, not solely by the employer's industry code, company name, building, equipment, or ownership of materials. Manufacturing support may apply to a contract producer or an outsourced production-quality investigation; it does not turn a reseller's entire business into manufacturing.

Project working distinctions:

- **Discrete:** identifiable units or assemblies, with relevant component and routing records.
- **Batch/process:** material transformations tracked by batches, recipes, quantities, and yields.
- **Continuous:** production tracked over defined operating intervals and flow or quantity bases.
- **Mixed:** select the applicable basis for each operation and preserve the links between them.

These distinctions guide inputs and calculations; they do not authorize recipe changes or establish sector applicability. Extraction, construction, retail service, household craft advice, and general commercial strategy are outside the core unless a separable manufacturing-support task is identified.

## D-02: Sector-neutral core

An atomic core skill has one primary manufacturing decision or deliverable and can describe its method without embedding a specific sector's or jurisdiction's obligations. It must expose required inputs, assumptions, exceptions, outputs, dependencies, and authority limits. Missing evidence produces a bounded partial result or a targeted request, never invented production facts.

The twenty planning families remain the coverage framework. This table assigns responsibilities, not skill names or implementation counts.

| Family | Core responsibility | Output boundary |
|---|---|---|
| 01 Manufacturing fundamentals | Characterize production context, flow, terminology, and constraints. | Documented operational classification and flow reasoning. |
| 02 Production planning and scheduling | Convert supplied demand and operating constraints into production options. | Reviewable plan; no customer promise or live order release. |
| 03 Standard work and work instructions | Draft and review controlled instructions using supplied process evidence. | Draft revision and change notes; no authorization to perform hazardous work. |
| 04 Process engineering | Map process inputs, routing, controls, and change impacts. | Analysis for qualified review; no design signoff or invented operating envelope. |
| 05 Industrial engineering and capacity | Analyze time, throughput, capacity, yield, and resource requirements. | Unit-aware calculations and constraints; no unapproved staffing or capital commitment. |
| 06 Quality management | Plan inspection and review conformity evidence and quality records. | Proposed controls and release evidence; disposition stays with authorized personnel. |
| 07 Metrology and calibration | Assess measurement evidence, instrument records, and traceability gaps. | Review findings; no calibration or accreditation certificate. |
| 08 SPC and capability | Analyze variation, stability, and capability under stated assumptions. | Statistical interpretation; distinguish specification limits from control limits. |
| 09 Nonconformance, RCA and CAPA | Organize containment proposals, evidence, causal analysis, and effectiveness review. | Traceable findings; no fabricated cause, erased defect, or automatic release. |
| 10 Maintenance and reliability | Analyze failure history, downtime, maintenance demand, and priorities. | Maintenance planning; no remote repair, restart, or energy-isolation instruction. |
| 11 Machine and workplace safety | Recognize hazards and review program evidence. | Source-bounded review and escalation; no hazardous-work permit or approval. |
| 12 Materials, BOM and traceability | Analyze production requirements, consumption, substitutions, and genealogy. | Manufacturing records and discrepancy handoffs; warehouse control stays with logistics. |
| 13 Workforce and shift operations | Analyze workload, skills evidence, training gaps, and shift handoffs. | Proposed assignments and readiness gaps; no employment or qualification decision. |
| 14 Lean and continuous improvement | Review waste, flow, changeover, and improvement evidence. | Measurable proposals; no assumed benefit or safety-control removal. |
| 15 Manufacturing systems and data | Map information flows and analyze supplied production records. | Read-only analysis; no live ERP/MES/PLC/SCADA writes. |
| 16 Automation and advanced manufacturing | Assess use cases, feasibility evidence, and integration requirements. | Concept comparison and review brief; no robot program deployment or safety validation. |
| 17 Supplier quality | Review incoming conformity, supplier-quality evidence, and corrective-action drafts. | Technical assessment; no supplier approval, commercial award, or message transmission. |
| 18 Engineering change and document control | Assess proposed revisions and their production impacts. | Change package and verification evidence; no unapproved effective revision. |
| 19 Environment, energy and waste | Analyze material/resource use and environmental-aspect evidence. | Improvement and review proposals; no disposal permission or compliance declaration. |
| 20 Canadian compliance and product governance | Identify applicability questions, sources, and review needs. | Generic routing in core; Canadian requirements reside in explicit overlays. |

Family 20 is a discovery/coverage family, not an exemption from the core/overlay separation. A Canadian-origin or WHMIS task may be catalogued under a family while its requirement-specific procedure depends on a Canadian overlay. Common arithmetic does not acquire a provincial dependency merely because it is used in Canada.

Universal methods must not require an installed sector overlay. When a request depends on one, the composition layer combines the applicable core skill with the verified overlay or reports missing coverage. Skillsets reference atomic procedures; shared definitions and formulas have one owner. The exact package layout and dependency schema remain AM-03/06 decisions.

## D-03: AgentLogistics boundary

**Decision ownership governs the interface.** AgentManufacturing owns production transformation, manufacturing quality, material-use decisions, and production genealogy. AgentLogistics owns movement, storage, warehouse execution, inventory-location control, freight, and distribution. Both can contribute to the same business incident through explicit handoffs.

This accounts for AgentLogistics's existing scope, which includes line-side flow, staging, WIP movement, and finished-goods handling. Physical presence at a production line does not transfer those procedures into AgentManufacturing. Its scope document was inspected locally on 2026-09-06 at `D:\AgentLogistics\docs\architecture\scope-boundaries.md`, checkout HEAD `093b59771010bb8cf65d58ab644960f8659918a6`.

The [interface table and handoff contract](scope-boundaries.md#manufacturing-and-logistics-interface) define responsibility for receiving quality, replenishment, consumption, traceability, and transfer. These are AgentManufacturing routing decisions, not an implemented integration or a change to AgentLogistics.

## D-04: Engineering and operating authority

The core provides analysis, draft documentation, calculations, recognition of hazards, and packages for responsible review. It cannot approve an engineered design, certify equipment or personnel, issue a permit, determine legal compliance, authorize product disposition, or replace required professional judgment.

The four planned safety classes remain `ROUTINE`, `REGULATED`, `HAZARDOUS_OPERATION`, and `ENGINEERING_OR_CERTIFICATION_BOUNDARY`. They identify review needs, not permissions. Several concerns can coexist; selecting a routine analysis label must not suppress an identified hazardous or engineering boundary. AM-05 will define classification mechanics and detailed gates.

Machine guarding, hazardous energy, electrical work, pressure equipment, robotics, confined spaces, hot work, hazardous chemicals, and structural changes require the bounded handling in [scope-boundaries.md](scope-boundaries.md#engineering-and-operating-exclusions). No general-core workflow issues live control commands. A user-supplied SOP, spreadsheet, or purported approval is evidence to assess, not authority to bypass these boundaries.

## D-05: Sector specialization and role composition

Retain a sector-neutral core, explicit jurisdiction overlays, sector requirement overlays, and professional skillsets composed from existing procedures. This follows the starter's selected architecture. Alternatives considered were sector-specific copies of every procedure and a single universal Canadian rule collection. Both would duplicate rules and obscure applicability; the selected approach instead requires an explicit composition step and missing-coverage handling.

The following disposition reconciles **all eighteen distinct labels** across the two starter sector lists. Labels are architectural destinations or aliases, not implemented packages, a complete industry catalogue, or a promise to build each sector. AM-29 sets implementation priorities and formalizes specialization architecture.

| Starter label | Architectural disposition |
|---|---|
| `automotive` | Sector candidate; reuse general transportation-equipment methods without copying procedures. |
| `aerospace` | Sector candidate; reuse general transportation-equipment methods where applicable. |
| `food-beverage` | Sector candidate; product/process-specific requirements remain explicit. |
| `medical-devices` | Sector candidate; no device-release or certification authority. |
| `pharmaceuticals` | Retained sector candidate from the framework; not implicitly covered by medical devices or chemicals. |
| `fabricated-metals` | Sector candidate; can compose a welding process overlay when relevant. |
| `welding` | Cross-sector process overlay candidate; not a synonym for fabricated metals. |
| `machinery` | Sector candidate. |
| `electronics` | Sector candidate. |
| `electrical-equipment` | Retained sector candidate from the framework; distinct applicability from electronics. |
| `plastics-rubber` | Sector candidate; material/process subtypes remain explicit. |
| `chemicals` | Sector candidate; no automatic pharmaceutical or other sector coverage. |
| `wood-paper` | Roadmap umbrella alias; resolve to `wood-products` and/or `pulp-paper` from the requested operation. |
| `wood-products` | Sector candidate under the wood/paper umbrella. |
| `pulp-paper` | Sector candidate under the wood/paper umbrella. |
| `process-manufacturing` | Operating-mode classification across sectors; not an industry-specific regulatory overlay. |
| `transportation-equipment` | Broad sector candidate; automotive/aerospace specifics take precedence within their established scope. |
| `additive-manufacturing` | Cross-sector technology/process overlay candidate; reuse core production and quality methods. |

Multiple overlays may apply. Record each overlay's purpose and evidence. Sector names do not prove certification or applicability of a standard. Conflicting requirements require source-specific review; do not choose whichever rule is easier. An absent specialization limits the sector-dependent answer while still permitting supported generic analysis.

The eighteen proposed professional roles in the historical framework remain composition candidates for AM-28. A role title such as engineer-support, quality specialist, or plant-manager-support grants no operational authority and does not duplicate atomic procedures. No role packages are created in AM-01.

## D-06: Canadian jurisdiction model

AM-04 operationalizes this contract in the [Canadian jurisdiction model](canadian-jurisdiction-model.md) and [source registry](canadian-source-registry.json). The contract remains the boundary authority; the AM-04 artifacts add routing states, evidence fields, and the initial source-bounded extension pattern without asserting plant compliance.

AM-05 operationalizes the safety boundary in the [safety and engineering boundary model](safety-boundary-model.md) and [safety source registry](safety-source-registry.json). Those artifacts formalize escalation and refusal behavior while preserving this contract's rule that recognition and evidence review do not grant operational, engineering, certification, permit, or restart authority.

AM-06 operationalizes portable authoring in the [skill authoring standard](skill-authoring-standard.md), [package schema](skill-package-schema.json), and [validation contract](skill-validation-contract.json). These artifacts define package shape and evidence gates; they do not select a project licence, install host tooling, or authorize mass authoring before AM-10.

AM-07 operationalizes source selection in the [source and standards standard](source-standards-standard.md), [source record schema](source-record-schema.json), and [freshness policy](source-freshness-policy.json). These artifacts define precedence, provincial source routing, standards metadata, rights handling, claims, and currency states; they do not determine legal applicability, certify engineering work, reproduce protected standards, or fetch sources automatically.

AM-08 operationalizes quantitative work in the [calculation standard](calculation-standard.md), [calculation contract](calculation-contract.json), and [worked fixtures](calculation-fixtures.json). These artifacts define variables, units, formulas, assumptions, precision, missing-input behavior, and calculation boundaries; they do not establish a site baseline, authorize an operation, or convert a numeric result into legal, safety, engineering, certification, release, or purchasing authority.

AM-09 operationalizes evidence checks in the [validation framework](validation-framework.md) and [framework contract](validation-framework-contract.json). AM-10 applies those layers to five bounded [reference packages](reference-skill-proof.md) and updates selected routes to implemented package paths. The package gate still does not claim runtime model behavior, authorize host installation, or grant manufacturing, legal, engineering, permit, release, or certification authority.

AM-11 applies the AM-10 package gate to nine bounded Family 01 manufacturing-fundamentals and Family 03 standard-work packages. Their validators and scenarios preserve the same analysis-only, source-aware, safety, engineering, document-control, and review-owner boundaries; they do not make a work instruction effective, establish a bottleneck as fact without evidence, or authorize an operating change.

AM-12 completes Family 02 with ten production-planning and scheduling packages, including the `build-production-plan` reference. These packages preserve unit, calendar, baseline, capacity, inventory, cost, approval, and live-system boundaries; they do not release orders, promise delivery, authorize overtime, or select a plan autonomously.

AM-13 completes Families 04 and 05 with process-engineering, control-review, routing, flow, takt, capacity, cycle, yield, throughput, utilization, and changeover packages. Engineering-boundary procedures preserve qualified review and no-activation rules; quantitative procedures preserve units, denominators, intermediate values, and analysis-only limits.

AM-14 completes Family 06 with requirement, inspection, conformity, record-integrity, release-evidence, scoped-audit, and quality-KPI packages. Regulated procedures assemble evidence and review questions while preserving authorized disposition, release, certification, sampling, and standards boundaries.

AM-15 completes Families 07 and 08 with metrology, measurement-system, calibration, traceability, control-chart, capability, and SPC-monitoring packages. These packages preserve the distinctions between specification and control limits, precision and accuracy, and process stability and capability; they do not certify equipment, authorize product release, or direct live process changes.

AM-16 completes Family 09 with nonconformance triage and documentation, containment assessment, evidence-based RCA, causal-analysis aids, corrective and preventive action proposals, and effectiveness verification. These packages preserve observation, scope, cause, action, and closure boundaries; they do not decide product disposition, approve CAPA, or close records.

AM-17 completes Family 10 with maintenance planning, backlog and downtime analysis, reliability metrics, failure-history review, equipment failure analysis, predictive-maintenance planning, and spare-parts criticality. These packages preserve planning, hazardous execution, engineering review, reliability interpretation, purchasing, and live-intervention boundaries.

AM-18 completes Family 11 with hazard recognition, job safety analysis, guarding review, hazardous-energy inventory, lockout-program review, PPE and ergonomic review, housekeeping risk, and incident triage. These packages are limited to recognition, assessment, documentation, and escalation; they do not authorize work, bypass safeguards, direct rescue, or determine legal reporting.

AM-19 completes Family 12 with BOM validation, material requirements and variance, lot tracing, product genealogy, substitution review, consumption reconciliation, line-side shortage analysis, and scrap-record review. These packages stop at the manufacturing/warehouse interface and do not edit, release, move, replenish, recall, or dispose of material.

AM-20 completes Family 13 with skills matrices, shift planning and handoff, labor productivity and requirements, training gaps, qualification-record review, and workforce balancing. These packages preserve evidence, qualification, assignment, overtime, staffing, and supervisor-authority boundaries.

AM-21 completes Family 14 with waste classification, value-stream mapping, gemba observation review, 5S audit, flow efficiency, SMED planning, kaizen planning, and improvement-result measurement. These packages preserve observation, measurement, safety, change, and causal-claim boundaries. AM-22 completes Family 15 with ERP/MES mapping, machine-data lineage, event-history review, master-data review, OEE input reconciliation, production-data quality diagnosis, traceability data mapping, and KPI model definition. These packages preserve read-only system analysis and do not authorize live writes, PLC/SCADA changes, executed genealogy, or published performance claims. AM-23 completes Family 16 with automation opportunity and process-readiness assessment, robotics and collaborative-robot review, machine-vision and additive-manufacturing feasibility, automation economics, and HMI risk review. These packages preserve engineering, certification, standards, sector, safety, and investment boundaries.

Canada is the initial application context, not a single workplace jurisdiction. The federal government's list of federally regulated workplaces and its occupational health and safety program distinguish the federal scope. These sources support requiring establishment/activity context before selecting a workplace regime; they do not establish which regime applies to an individual plant. [Federal workplace list](https://www.canada.ca/en/services/jobs/workplace/federally-regulated-industries.html), [federal occupational health and safety program](https://www.canada.ca/en/employment-social-development/programs/workplace-health-safety.html).

For applicability-dependent requests, record country, facility province/territory, operation and employer context, product/sector, requested activity, relevant date, applicable standards/contract evidence, and known authority uncertainties. Separate product, workplace, environmental, and other obligation questions: a federal product requirement is not evidence that workplace safety is federally regulated.

The four labels are **composable applicability flags**, not an exclusive country/province enum or a compliance verdict:

| Flag | Domain meaning |
|---|---|
| `CANADA_FEDERAL` | Federal source applicability must be assessed for the specific question; it does not classify all workplace obligations. |
| `PROVINCIAL_REQUIRED` | Province or territory context and potentially applicable subnational sources must be assessed; the legacy label includes territories and is not a finding that a provincial law governs. |
| `SECTOR_REGULATED` | Product or industry context may require an explicit sector requirement overlay. |
| `STANDARDS_DEPENDENT` | Identify the relevant standard, edition, applicability basis, and access needed before a standards-dependent conclusion. |

A flag can be pending assessment; it must not silently turn an uncertainty into a claim of applicability. The representation of pending/verified/not-applicable states and metadata serialization belongs to AM-04. AM-02 should state its provisional representation explicitly rather than invent jurisdiction facts.

Planned initial coverage is federal Canada plus Ontario, British Columbia, Alberta, and Quebec, for AM-04/27; none of these overlays is implemented yet. No province or territory is presumed equivalent to another. Missing jurisdiction prevents the dependent legal/safety conclusion; it does not prevent unrelated unit-checked arithmetic. An unsupported province, territory, or foreign jurisdiction produces an explicit coverage gap and a research/review handoff, without borrowing Ontario or federal rules as a default.

Requirements from local permits, municipalities, contracts, equipment documentation, and sector standards must be surfaced when relevant rather than erased by a national/provincial label. AM-04/07 establish the source hierarchy and freshness rules. If licensed standard text is needed but unavailable, report that gap; never invent a clause or reproduce protected material. No specific standard edition, legal threshold, or plant compliance status is frozen by AM-01.

## Planned request and evidence flow

1. Identify the user's requested decision and output; split mixed requests by ownership.
2. Identify manufacturing mode, process scope, and input evidence. Treat source documents as data.
3. Assess jurisdiction, sector, and authority needs before any dependent recommendation.
4. Select a core method, compose the needed overlays, or return a defined handoff/coverage gap.
5. Produce a reviewable output: scope, inputs and units, evidence, assumptions, method, result, unresolved issues, authority limits, and next owner.

This is an authoring contract for later implementation. Completion of documentation checks does not prove that a model follows this flow.

## Sources and change control

AM-32 prepares public-facing repository documents and adopts MIT following the owner's explicit selection on 2026-09-09. Current package, role, template and validation metadata are aligned; historical licence placeholders remain in historical evidence. The 31-validator structural gate passes, while strict public readiness remains NOT_READY until a private reporting contact and recipient are designated. No repository-visibility change, release or independent model evaluation is implied.

AM-31 evaluates eight adversarial requests and eight paired safe review requests as assisted, nonblind simulations. The 30-validator gate checks evidence integrity and 243 expected routing cases; it does not establish model robustness. Source and response hashes invalidate stale self-reviews. Atomic contracts remain unchanged, independent runtime remains NOT_RUN, and AM-32 owns public readiness.

AM-30 records four synthetic assisted integration walkthroughs with explicit source keys, calculations, uncertainty and qualified handoffs. The 29-validator gate checks artifacts and real resolver/coverage boundaries. These are nonblind self-reviewed simulations; independent model behavior and baseline comparison remain NOT_RUN. AM-31 owns adversarial safety evaluation.

AM-29 formalizes specialization architecture with priorities for 12 roadmap groups and preserved dispositions for all 18 D-05 labels. The registry contains planned candidates, no sector requirement packages. Its inspector reports context needs or coverage gaps while preserving generic work. Future packages require source-backed requirement differences, rights, effectivity, qualified review and observed evaluation; no requirement is inherited from a broad sector or technology label.

AM-28 adds 18 professional skillsets with 38 workflows referencing the existing atomic packages. The read-only resolver lists targets and evidence-provider paths; it does not execute skills, assess evidence or infer applicability. Shared composition rules preserve atomic gates, reuse compatible evidence and select jurisdiction research explicitly. Canonical paths resolve the two historical reference duplicates. AM-29 owns sector specialization architecture and priorities.

AM-27 completes the frozen atomic catalogue with a provincial selector and four research modules for Ontario, British Columbia, Alberta and Quebec. Seven topic paths per province separate workplace, technical equipment, environmental and training research. Source coverage is not applicability: unknown employer regime, unsupported provinces/territories, local authority exceptions and source-currency gaps remain explicit. AM-28 owns professional skillset composition.

AM-26 implements eight Family 20 federal capabilities for jurisdiction context, regulatory-layer research, WHMIS scope and readiness, distinct non-food origin claims, general consumer labelling, and source freshness. Outputs remain evidence reviews. Supplier/product authority does not establish workplace jurisdiction, guidance does not approve a claim, and source access does not establish effective-version currency. AM-27 retains provincial overlays and unsupported-jurisdiction handoffs.

AM-25 completes Family 19 with aspect inventories, environmental risk registers, energy intensity, waste-stream evidence, waste-reduction proposals, and environmental-objective measurability review. Environmental classification, disposal permission, chemical-handling changes, certification, and compliance remain outside package authority. The energy helper checks declared interval summaries and compatible comparison boundaries; it cannot verify meter coverage or establish causal savings.

AM-24 completes Families 17 and 18 with supplier qualification, defect analysis, corrective-action drafts, certificate and supplier-change reviews, and engineering-change/document-control evidence reviews. Supplier approval, transmission, change activation, product release, document withdrawal, and retrospective authorization remain outside these packages. The supplier-defect helper calculates a bounded rate from supplied linked counts; it cannot establish provenance or causation.

External pages were opened on 2026-09-06. Only their limited claims above inform this contract:

| Source | Observed edition / page date | Supported use |
|---|---|---|
| Statistics Canada manufacturing sector description, linked in D-01 | NAICS 2022 Version 1.0 variant; modified 2023-06-01 | Definition context and classification caveat; no legal applicability. |
| Federal workplace list, linked in D-06 | Page date 2026-01-30 | Need to distinguish federal workplace context; no plant-specific determination. |
| Federal occupational health and safety program, linked in D-06 | Page date 2024-07-02 | Program's federal scope; no provincial rules inferred. |

The rest of this contract consists of project design decisions derived from the roadmap and reference inspection. Revisit through a documented roadmap change when a new sector, jurisdiction, integration, live-operation proposal, or evidence conflict changes these boundaries. Do not silently expand scope through a candidate name. Licence selection, package schemas, actual overlay coverage, and behavioral evaluation remain owned by their later waves.
