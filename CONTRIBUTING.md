# Contributing

AgentManufacturing is a development repository licensed under [MIT](LICENSE), selected by the owner during AM-32. The [AM-32 reporting designation](docs/development/AM-32-public-readiness.md) is recorded; public launch and contribution intake remain subject to the subsequent release review. No contributor licence agreement or ownership transfer is established by this document; the launch hold does not add restrictions to MIT's grant.

## Prepare a change

Read [AGENTS.md](AGENTS.md), the [roadmap](ROADMAP.md), [domain contract](docs/architecture/domain-contract.md) and [authoring standard](docs/architecture/skill-authoring-standard.md). Propose one bounded problem with acceptance criteria. Use synthetic examples and preserve evidence provenance, units, dates and review limits. Do not submit material you lack permission to contribute, protected standards text or confidential plant information.

Use the frozen [taxonomy index](docs/architecture/taxonomy-index.yaml) and canonical package map in [composition-contract.json](skillsets/composition-contract.json). Discuss taxonomy changes explicitly; do not repurpose an accepted name or remove historical records to fit an implementation.

## Verify and describe

From the repository root with Python available:

```powershell
python scripts/validate-all.py
git diff --check
```

Include the problem, resulting behavior, affected contracts, focused/full validation results and remaining evidence gaps in the change description. For scenario changes, update [expected routing](tests/expected-routing.yaml) and the matching Markdown case together. For skill changes, inspect the host metadata and references as well as SKILL.md. Use the available official skill validator in addition to repository checks when modifying skill packages.

Report test evidence accurately. Static metadata, arithmetic checks and self-reviewed simulations do not establish independent model performance. Re-evaluate affected AM-31 judgments before changing their source or response snapshots. No live controller, manufacturing-system or publication change is part of a documentation or fixture contribution.

## Review and reporting

Existing authorized collaborators may submit changes through the repository's established review workflow. No external contribution response time, merge promise or support commitment is offered. The project owner must approve governance changes; routine commit access is not publication authority.

Use [SECURITY.md](SECURITY.md) for sensitive vulnerabilities and [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md) for community conduct. Jeremy Longworth receives private security and conduct reports at [private contact removed]. Do not place sensitive reports in public issues or pull requests. Public intake remains a separate launch decision.
