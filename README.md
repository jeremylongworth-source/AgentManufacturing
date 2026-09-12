# AgentManufacturing

Portable AI skill packages for manufacturing analysis and qualified review, with a sector-neutral core, Canadian jurisdiction overlays and professional role compositions.

**Development status:** AM-00 through AM-33 are complete for their documented scopes. The release-candidate verdict is **V1_PARTIALLY_READY**; public v1 release is deferred. MIT and owner-designated private reporting are in place. See the [audit and follow-up criteria](docs/development/AM-33-release-candidate-audit.md).

## What is available

- 161 bounded skill package directories representing 159 accepted names across 20 families.
- 18 professional skillsets with 38 workflows referencing the atomic packages.
- 243 expected routing cases, deterministic calculation checks and a dependency-free Python validation gate.
- Four assisted integration walkthroughs and eight adversarial cases paired with eight safe-review controls.

AM-30/31 evaluations are nonblind, self-reviewed simulations. Independent model execution, baseline comparisons, repeated trials and multi-turn robustness remain unperformed. Planned sector specializations contain no implemented sector requirements.

## Get started

With Git and Python available, clone the library and run the examples from its root:

```powershell
git clone https://github.com/jeremylongworth-source/AgentManufacturing.git
cd AgentManufacturing
python scripts/validate-all.py
python scripts/resolve-skillset.py production-planner horizon-plan
python scripts/inspect-sector-coverage.py automotive
python scripts/inspect-sector-coverage.py automotive --generic-only
```

The full gate validates repository artifacts; it does not run a model. The resolver returns `REFERENCES_RESOLVED`, `execution: NOT_EXECUTED` and `evidence_state: NOT_ASSESSED`. Read the returned SKILL.md files and relevant references to understand each method and its required evidence. There is no automatic skill executor or host installation in this workflow.

The sector inspector returns `COVERAGE_GAP` for the planned automotive specialization. With `--generic-only`, it permits unrelated generic analysis while keeping sector conclusions unsupported. Successful reference resolution or generic arithmetic does not establish applicability or operating authority.

Commands were checked locally with Python 3.14.3 on Windows PowerShell and in [hosted Linux/Windows CI](docs/development/AM-33-ci-evidence.json) using Python 3.14. The validators use the Python standard library; no package installation is required. Other AI-host compatibility and independent skill behavior remain unestablished.

The [Wiki documentation source](docs/wiki/Home.md) provides a quickstart, a worked example, the complete skill catalogue, all role workflows and troubleshooting. The [GitHub Wiki](https://github.com/jeremylongworth-source/AgentManufacturing/wiki) is being initialized; the maintained source is available now.

## Public-readiness check

```powershell
python scripts/validate-public-readiness.py
python scripts/validate-public-readiness.py --require-ready
```

Both commands now report `AM32_READY`; strict mode exits 0. This confirms the documented AM-32 prerequisites, including owner-designated reporting, not mailbox delivery or publication authorization. AM-33 is complete with a V1_PARTIALLY_READY verdict; strict AM-32 readiness does not override that release decision.

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

Read [CONTRIBUTING.md](CONTRIBUTING.md) and [AGENTS.md](AGENTS.md) for change scope, validation and evidence requirements. [SECURITY.md](SECURITY.md) and [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md) name Jeremy Longworth at [private contact removed] as the private reporting recipient. Do not publish sensitive reports in issues or pull requests.

[LICENSE](LICENSE) contains the owner's selected MIT licence. Third-party references retain their own rights; citation does not relicense their content. This library is shared for development and reference; the partial v1 audit remains in effect. [CHANGELOG.md](CHANGELOG.md) records development history.

Support the maintainer through [GitHub Sponsors](https://github.com/sponsors/jeremylongworth-source).

## Roadmap and continuation

Use the execution ledger in [ROADMAP.md](ROADMAP.md) and the [AM-33 final handoff](docs/development/handoffs/AM-33-final-handoff.md). The numbered roadmap is complete; follow F01–F04 in the audit for independent evaluation, source/standards review, merge-gate policy and release-scope ownership.

The [AM-00 audit](docs/development/AM-00-baseline-audit.md), [taxonomy audit](docs/architecture/taxonomy-audit-v1.md) and [original framework](docs/architecture/domain-framework.md) preserve planning provenance; those planning statements are not current legal or engineering determinations.
