# AgentManufacturing

Portable AI skill packages for manufacturing analysis, documentation and qualified review. The library combines sector-neutral methods with Canadian jurisdiction overlays and professional role workflows.

Use it to structure production planning, quality analysis, maintenance reviews and evidence handoffs. Each skill defines its required inputs, method, outputs and review boundaries.

**Development status:** This is a public development library. A stable v1 release is deferred pending independent model evaluation and qualified source review. See the [release-candidate audit](docs/development/AM-33-release-candidate-audit.md) for the full assessment.

## Explore the library

- **159 distinct skills across 20 families**, covering production, quality, reliability, safety and other manufacturing functions.
- **18 professional skillsets with 38 workflows** that compose relevant skills for a role.
- **Canadian jurisdiction overlays** kept separate from generic manufacturing methods.
- **Repository validators and synthetic examples** for checking contracts, calculations and expected routing.

Start with the [Wiki](https://github.com/jeremylongworth-source/AgentManufacturing/wiki), browse the [skill catalogue](https://github.com/jeremylongworth-source/AgentManufacturing/wiki/Skill-Catalogue), or choose a [professional skillset](https://github.com/jeremylongworth-source/AgentManufacturing/wiki/Professional-Skillsets).

Sector specializations are planned; no sector requirement packages are implemented.

## Get started

You need Git and Python. Validation runs in CI with Python 3.14 on Linux and Windows and uses only the Python standard library.

```shell
git clone https://github.com/jeremylongworth-source/AgentManufacturing.git
cd AgentManufacturing
python scripts/validate-all.py
```

To find the skills for a production-planning workflow:

```shell
python scripts/resolve-skillset.py production-planner horizon-plan
```

The resolver returns `REFERENCES_RESOLVED` with paths to the relevant SKILL.md files. Read those instructions and their references, then gather the required evidence before applying the methods in your chosen agent host.

The resolver lists references; it does not execute skills or assess the supplied evidence. This workflow provides no automatic agent installer, and host compatibility must be verified separately.

Continue with the [worked example](https://github.com/jeremylongworth-source/AgentManufacturing/wiki/Using-a-Skill) or [troubleshooting guide](https://github.com/jeremylongworth-source/AgentManufacturing/wiki/FAQ-and-Troubleshooting).

## Scope and limitations

These skills support analysis and qualified handoffs. They do not authorize machine operation, isolation or restart, safety-circuit changes, engineering signoff, product release or legal conclusions. Do not use model output to bypass safeguards or fabricate manufacturing records.

Establish current sources, jurisdiction, units, populations and review authority for each conclusion. Generic calculations and successful reference resolution do not establish sector or legal applicability. Read the [safety boundaries](docs/architecture/safety-boundary-model.md) and [source rules](docs/architecture/source-standards-standard.md).

The repository includes 243 expected routing cases and assisted, self-reviewed evaluations. These are not independent measurements of model reliability. Baseline comparisons, repeated model trials and multi-turn robustness tests remain unperformed. The [validation guide](https://github.com/jeremylongworth-source/AgentManufacturing/wiki/Validation-and-Evaluation) explains what each check establishes.

## Repository guide

| Location | Purpose |
|---|---|
| [skills/](skills/) | Atomic instructions, references and host metadata |
| [skillsets/index.json](skillsets/index.json) | Professional roles and workflow manifests |
| [composition contract](skillsets/composition-contract.json) | Canonical skill paths and evidence-reuse rules |
| [specializations/registry.json](specializations/registry.json) | Planned sector coverage |
| [domain contract](docs/architecture/domain-contract.md) | Architecture and jurisdiction separation |
| [tests/](tests/) | Expected scenarios, synthetic fixtures and evaluation evidence |
| [docs/wiki/](docs/wiki/) | Maintained Wiki source |

There are 161 package directories for 159 distinct skills because two historical duplicates are preserved. Use the canonical paths in the composition contract. Some YAML files intentionally use JSON syntax for dependency-free parsing.

## Contributing and reporting

Read [CONTRIBUTING.md](CONTRIBUTING.md) for proposing changes, validation and evidence requirements. Agent-assisted contributors should also read [AGENTS.md](AGENTS.md).

For sensitive vulnerabilities, follow [SECURITY.md](SECURITY.md). For community concerns, follow [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md). Do not include sensitive reports, credentials or confidential plant records in public issues or pull requests. No support response time is guaranteed.

## Roadmap

The initial development roadmap is complete for its documented scope. Remaining work includes independent evaluation, qualified source and standards review, merge-gate policy, and host and support scope. See the [roadmap](ROADMAP.md), [audit follow-ups](docs/development/AM-33-release-candidate-audit.md) and [changelog](CHANGELOG.md).

## Licence and support

AgentManufacturing is licensed under [MIT](LICENSE). Third-party references retain their own rights; citation does not grant permission to reproduce protected standards or other source material.

You can support the maintainer through [GitHub Sponsors](https://github.com/sponsors/jeremylongworth-source).
