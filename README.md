# AgentManufacturing

Portable AI skill packages for manufacturing analysis and qualified review, with a sector-neutral core, Canadian jurisdiction overlays and professional role compositions.

**Development status:** AM-00 through AM-31 are READY for their documented scopes. **AM-32 is IN_PROGRESS**: MIT is selected and public-readiness documents are prepared, but private reporting remains unresolved. No public release is established. See the [readiness record](docs/development/AM-32-public-readiness.md).

## What is available

- 161 bounded skill package directories representing 159 accepted names across 20 families.
- 18 professional skillsets with 38 workflows referencing the atomic packages.
- 243 expected routing cases, deterministic calculation checks and a dependency-free Python validation gate.
- Four assisted integration walkthroughs and eight adversarial cases paired with eight safe-review controls.

AM-30/31 evaluations are nonblind, self-reviewed simulations. Independent model execution, baseline comparisons, repeated trials and multi-turn robustness remain unperformed. Planned sector specializations contain no implemented sector requirements.

## First use from a checkout

Repository access is required while the project is private. From the repository root, with Git and Python available:

```powershell
python scripts/validate-all.py
python scripts/resolve-skillset.py production-planner horizon-plan
python scripts/inspect-sector-coverage.py automotive
python scripts/inspect-sector-coverage.py automotive --generic-only
```

The full gate validates repository artifacts; it does not run a model. The resolver returns `REFERENCES_RESOLVED`, `execution: NOT_EXECUTED` and `evidence_state: NOT_ASSESSED`. Read the returned SKILL.md files and relevant references to understand each method and its required evidence. There is no automatic skill executor or host installation in this workflow.

The sector inspector returns `COVERAGE_GAP` for the planned automotive specialization. With `--generic-only`, it permits unrelated generic analysis while keeping sector conclusions unsupported. Successful reference resolution or generic arithmetic does not establish applicability or operating authority.

Commands were checked with Python 3.14.3 on Windows PowerShell. The validators use the Python standard library; no package installation is required. Other interpreter versions and AI-host compatibility have not been established by this check.

## Public-readiness check

```powershell
python scripts/validate-public-readiness.py
python scripts/validate-public-readiness.py --require-ready
```

The first command checks consistency of prepared documents and governance evidence. The second currently exits with code 2 (`NOT_READY`) because the private reporting route is unresolved. A passing repository gate must not be presented as publication readiness. AM-33's release-candidate audit remains subsequent work.

## Boundaries

These skills support analysis, documentation, evidence gaps and qualified handoffs. They do not authorize machine operation, isolation/restart, safety-circuit changes, engineering signoff, product release, legal conclusions or claim publication. Do not use model output to bypass safeguards or fabricate manufacturing records.

Current source evidence, jurisdiction, units, populations and review authority must be established for each dependent conclusion. References to third-party guidance or standards do not grant reproduction rights. Read the [safety boundary](docs/architecture/safety-boundary-model.md), [source rules](docs/architecture/source-standards-standard.md) and [scope boundaries](docs/architecture/scope-boundaries.md).

## Find the right material

| Location | Purpose |
|---|---|
| [skills/](skills/) | Atomic instructions, references and host metadata |
| [skillsets/index.json](skillsets/index.json) | Professional roles and workflow manifests |
| [composition contract](skillsets/composition-contract.json) | Canonical package paths, evidence reuse and explicit overlays |
| [specializations/registry.json](specializations/registry.json) | Planned sector coverage and context gaps |
| [taxonomy index](docs/architecture/taxonomy-index.yaml) | Frozen 159-name catalogue and dependency metadata |
| [domain contract](docs/architecture/domain-contract.md) | Architecture, jurisdiction separation and provenance |
| [tests/](tests/) | Expected scenarios, synthetic fixtures and evaluation evidence |
| [scripts/validate-all.py](scripts/validate-all.py) | Ordered repository validation entry point |

Some `.yaml` files deliberately use JSON syntax for dependency-free parsing. Frozen taxonomy status fields are historical acceptance metadata; package and wave evidence describe subsequent implementation. Two historical duplicate packages remain preserved; use the canonical paths in the composition contract for new references.

## Contributing and reporting

Read [CONTRIBUTING.md](CONTRIBUTING.md) and [AGENTS.md](AGENTS.md) for change scope, validation and evidence requirements. [SECURITY.md](SECURITY.md) and [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md) contain draft reporting/handling policies; the private recipient is not yet configured. Do not publish sensitive reports in issues or pull requests.

[LICENSE](LICENSE) contains the owner's selected MIT licence. Third-party references retain their own rights; citation does not relicense their content. The project has not launched publicly and private reporting is still being configured; these operational gates do not restrict MIT's grant. [CHANGELOG.md](CHANGELOG.md) records unreleased development history.

## Roadmap and continuation

Use the execution ledger in [ROADMAP.md](ROADMAP.md) and the [AM-32 progress handoff](docs/development/handoffs/AM-32-progress-handoff.md). AM-31's [final handoff](docs/development/handoffs/AM-31-final-handoff.md) remains the last closed-wave record. Complete AM-32 decisions before claiming its completion marker, then perform AM-33.

The original workspace is `D:\AgentMfg`; commands work from a checkout root without that path. The historical AM-00 bootstrap prompt is not the current task. The [AM-00 audit](docs/development/AM-00-baseline-audit.md), [taxonomy audit](docs/architecture/taxonomy-audit-v1.md) and [original framework](docs/architecture/domain-framework.md) preserve planning provenance; those planning statements are not current legal or engineering determinations.
