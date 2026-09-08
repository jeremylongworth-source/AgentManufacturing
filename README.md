# AgentManufacturing

Development workspace for open-source, portable AI skills supporting commercial manufacturing operations in Canada. The domain contract defines a sector-neutral manufacturing core, Canadian jurisdiction overlays, sector specializations, and professional skillsets; implementation remains roadmap work.

## Start here

- [ROADMAP.md](ROADMAP.md): AM-00 through AM-33, exact completion tokens, execution protocol, handoff template, first Codex prompt, and current status.
- [Master taxonomy v1](docs/architecture/master-taxonomy-v1.md): 159 accepted records across 20 families, with frozen responsibilities and implementation limits.
- [Taxonomy index](docs/architecture/taxonomy-index.yaml): canonical accepted records, per-draft audit evidence, provenance, and dependency graph.
- [Dependency map](docs/architecture/dependency-map.md): 76 evidence-reuse edges and a valid dependency order.
- [Taxonomy audit](docs/architecture/taxonomy-audit-v1.md): all 162 draft dispositions, merge decisions, safety-topic ownership, and future acceptance scenarios.
- [AM-02 draft taxonomy](docs/architecture/candidate-taxonomy-v0.1.md) and [draft register](docs/architecture/candidate-register-v0.1.json): preserved input to the v1 audit.
- [Original taxonomy](docs/architecture/master-taxonomy-v0.1.md): preserved representative names and planning provenance.
- [Domain contract](docs/architecture/domain-contract.md): manufacturing definition, core responsibilities, sector composition, and Canadian jurisdiction model.
- [Scope boundaries](docs/architecture/scope-boundaries.md): AgentLogistics handoffs, engineering and operating exclusions, and boundary review cases.
- [Domain framework](docs/architecture/domain-framework.md): historical planning framework and proposed structure; the AM-01 contract takes precedence where they differ.
- [AM-00 baseline audit](docs/development/AM-00-baseline-audit.md): inspected workspace, architectural references, gaps, and acceptance evidence.
- [Canadian jurisdiction model](docs/architecture/canadian-jurisdiction-model.md): AM-04 flags, applicability states, source hierarchy, and initial extension pattern.
- [Canadian source registry](docs/architecture/canadian-source-registry.json): official source metadata reviewed for AM-04.
- [Safety and engineering boundary model](docs/architecture/safety-boundary-model.md): AM-05 classes, escalation rules, nine topic gates, and safe-output boundaries.
- [Safety source registry](docs/architecture/safety-source-registry.json): official and delegated-authority source metadata reviewed for AM-05.
- [Skill authoring standard](docs/architecture/skill-authoring-standard.md): AM-06 package layout, output contract, templates, and validation layers.
- [Source and standards standard](docs/architecture/source-standards-standard.md): AM-07 source precedence, rights, provincial systems, standards metadata, and freshness controls.
- [Source record schema](docs/architecture/source-record-schema.json), [freshness policy](docs/architecture/source-freshness-policy.json), and [source examples](docs/architecture/source-record-examples.json): machine-readable AM-07 contracts and metadata-only examples.
- [Calculation standard](docs/architecture/calculation-standard.md): AM-08 variables, units, formulas, assumptions, precision, edge cases, output contract, and safety boundary.
- [Calculation contract](docs/architecture/calculation-contract.json) and [worked fixtures](docs/architecture/calculation-fixtures.json): machine-readable quantitative contract and 17 reference fixtures.
- [Validation framework](docs/architecture/validation-framework.md): AM-09 structural, routing, deterministic-fixture, and evaluation evidence contract.
- [Validation contract](docs/architecture/validation-framework-contract.json), [routing manifest](tests/expected-routing.yaml), [scenario suite](tests/scenarios/), and [fixture manifest](tests/fixtures/am09-fixture-manifest.json): executable framework evidence.
- [Reference-skill proof contract](docs/architecture/reference-skill-proof.md): AM-10 package gate and runtime-evaluation boundary.
- [Reference packages](skills/): five bounded AM-10 examples across quantitative, planning, quality, hazardous-operation, and Canadian-overlay classes.
- [Latest handoff](docs/development/handoffs/AM-25-final-handoff.md): AM-25 closure and the bounded AM-26 execution brief.

## Codex handoff

Use `D:\AgentMfg` as the working directory. Read the roadmap and latest handoff, then execute the next unfinished wave. The roadmap's **First Codex prompt** is the historical AM-00 bootstrap instruction. Treat the roadmap as planning authority and repository contents as execution truth.

Current state: **AM-00 through AM-25 READY** on 2026-09-08; **AM-26 is next**. The v1 taxonomy freezes 159 accepted records: 153 core methods and six Canadian overlays. All 162 draft candidates and 166 starter names remain traceable. AM-04 formalizes jurisdiction routing, AM-05 formalizes safety/engineering boundaries, AM-06 formalizes portable skill packages and evidence layers, AM-07 formalizes source precedence, standards metadata, rights handling, and freshness, AM-08 formalizes unit-safe quantitative calculations, AM-09 formalizes executable evidence checks, AM-10 proves five bounded reference package classes, AM-11 adds nine manufacturing-fundamentals and standard-work packages, AM-12 completes Family 02 production planning and scheduling, AM-13 completes Families 04 and 05 process and industrial engineering, AM-14 completes Family 06 quality management and inspection, AM-15 completes Families 07 and 08 metrology, SPC, and capability, AM-16 completes Family 09 nonconformance, RCA, and CAPA, AM-17 completes Family 10 maintenance and reliability, AM-18 completes Family 11 manufacturing safety, AM-19 completes Family 12 materials, BOM, and traceability, AM-20 completes Family 13 workforce and shift operations, AM-21 completes Family 14 lean and continuous improvement, AM-22 completes Family 15 manufacturing systems and data, AM-23 completes Family 16 automation and advanced manufacturing, AM-24 completes Families 17 and 18 supplier quality and engineering change, and AM-25 completes Family 19 environment, energy, and waste. Runtime model behavior remains unobserved until reviewer-owned evaluation runs.

The workspace contains domain contracts, a preserved draft register, the audited v1 catalogue, 153 bounded packages, focused validators, and wave handoffs. Runtime behavior evaluation, governance, skillsets, and specializations remain roadmap work. Local Git is initialized on `main` with `origin` pointing to [AgentManufacturing](https://github.com/jeremylongworth-source/AgentManufacturing). AM-00 verified the remote as private and empty on 2026-09-06. No release or licence selection has been made; roadmap work through AM-25 is committed and pushed as it closes.

## Taxonomy validation

```powershell
python scripts/validate-candidate-register.py
python scripts/validate-taxonomy.py
python scripts/validate-jurisdiction-model.py
python scripts/validate-safety-boundary-model.py
python scripts/validate-skill-authoring-standard.py
python scripts/validate-source-standards-standard.py
python scripts/validate-calculation-standard.py
python scripts/validate-validation-framework.py
python scripts/validate-reference-skills.py
python scripts/validate-implemented-skills.py
python scripts/validate-production-planning.py
python scripts/validate-process-engineering.py
python scripts/validate-quality-management.py
python scripts/validate-metrology-spc.py
python scripts/validate-nonconformance-capa.py
python scripts/validate-maintenance-reliability.py
python scripts/validate-manufacturing-safety.py
python scripts/validate-materials-traceability.py
python scripts/validate-workforce-shift.py
python scripts/validate-lean-improvement.py
python scripts/validate-systems-data.py
python scripts/validate-advanced-manufacturing.py
python scripts/validate-supplier-change.py
python scripts/validate-environment-energy-waste.py

# Or run the complete gate:
python scripts/validate-all.py
```

Uses the Python standard library to check preserved draft data, the accepted index, audits, provenance, graph ordering, document consistency, the AM-04 model/source registry, the AM-05 safety model/source registry, the AM-06 package/validation contracts and templates, the AM-07 source/standards contracts plus legacy registry compatibility, the AM-08 calculation contract and numeric fixtures, the AM-09 routing/scenario/evaluation framework, the AM-10 reference packages, the AM-11 Family 01/03 packages, the AM-12 Family 02 packages, the AM-13 Family 04/05 packages, the AM-14 Family 06 packages, and the AM-15 Family 07/08 packages. The YAML index uses JSON syntax for dependency-free parsing. A pass is not evidence of runtime model behavior, site safety, engineering adequacy, source freshness, copyright permission, legal approval, or regulatory applicability. See the latest handoff for results and limits.

## Provenance

Preserved from “Branch · Plan AgentLogistics Skills”, conversation `6a9d881b-9330-83ea-b887-26309d52536d`, on 2026-09-06. Source planning statements are not fresh legal, standards, or engineering determinations. Future waves must verify authoritative sources and preserve qualified-review boundaries.
