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
- [Latest handoff](docs/development/handoffs/AM-07-final-handoff.md): AM-07 closure and the bounded AM-08 execution brief.

## Codex handoff

Use `D:\AgentMfg` as the working directory. Read the roadmap and latest handoff, then execute the next unfinished wave. The roadmap's **First Codex prompt** is the historical AM-00 bootstrap instruction. Treat the roadmap as planning authority and repository contents as execution truth.

Current state: **AM-00 through AM-07 READY** on 2026-09-07; **AM-08 is next**. The v1 taxonomy freezes 159 accepted records: 153 core methods and six Canadian overlays. All 162 draft candidates and 166 starter names remain traceable. AM-04 formalizes jurisdiction routing, AM-05 formalizes safety/engineering boundaries, AM-06 formalizes portable skill packages and evidence layers, and AM-07 formalizes source precedence, standards metadata, rights handling, and freshness without implementing skills. Broad authoring remains gated on AM-10.

The workspace contains domain contracts, a preserved draft register, the audited v1 catalogue, focused validators, and wave handoffs. Skill authoring, general behavior validation, governance, skillsets, and specializations remain roadmap work. Local Git is initialized on `main` with `origin` pointing to [AgentManufacturing](https://github.com/jeremylongworth-source/AgentManufacturing). AM-00 verified the remote as private and empty on 2026-09-06. No commit, push, release, or licence selection has been made during AM-00–AM-07.

## Taxonomy validation

```powershell
python scripts/validate-candidate-register.py
python scripts/validate-taxonomy.py
python scripts/validate-jurisdiction-model.py
python scripts/validate-safety-boundary-model.py
python scripts/validate-skill-authoring-standard.py
python scripts/validate-source-standards-standard.py
```

Uses the Python standard library to check preserved draft data, the accepted index, audits, provenance, graph ordering, document consistency, the AM-04 model/source registry, the AM-05 safety model/source registry, the AM-06 package/validation contracts and templates, and the AM-07 source/standards contracts plus legacy registry compatibility. The YAML index uses JSON syntax for dependency-free parsing. A pass is not evidence of implemented skills, model behavior, calculation correctness, site safety, engineering adequacy, source freshness, copyright permission, or regulatory applicability. See the latest handoff for results and limits.

## Provenance

Preserved from “Branch · Plan AgentLogistics Skills”, conversation `6a9d881b-9330-83ea-b887-26309d52536d`, on 2026-09-06. Source planning statements are not fresh legal, standards, or engineering determinations. Future waves must verify authoritative sources and preserve qualified-review boundaries.
