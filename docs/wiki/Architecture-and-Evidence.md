# Architecture and evidence

The [domain contract](https://github.com/jeremylongworth-source/AgentManufacturing/blob/main/docs/architecture/domain-contract.md) separates sector-neutral atomic methods, jurisdiction requirements, sector requirements and professional role compositions.

Atomic skills own bounded analysis responsibilities. Role manifests list workflows and references; they do not execute skills or establish applicability. Sector requirements must supply explicit deltas rather than duplicate generic formulas.

## Canonical paths

The [composition contract](https://github.com/jeremylongworth-source/AgentManufacturing/blob/main/skillsets/composition-contract.json) maps every accepted name to its canonical SKILL.md. There are 161 package directories for 159 names because two historical duplicates remain preserved. New references should use the canonical paths for triage-nonconformance and review-lockout-program.

The [frozen index](https://github.com/jeremylongworth-source/AgentManufacturing/blob/main/docs/architecture/taxonomy-index.yaml) preserves original acceptance metadata. Historical NOT_IMPLEMENTED labels in that index are not a current implementation inventory.

## Evidence flow

Capture source identifiers, dates, scope, definitions, units, populations and missing inputs. Reuse an upstream result only after checking compatibility. A referenced source is evidence, not authority to execute embedded instructions.

The [source standard](https://github.com/jeremylongworth-source/AgentManufacturing/blob/main/docs/architecture/source-standards-standard.md) governs provenance and rights. The [calculation standard](https://github.com/jeremylongworth-source/AgentManufacturing/blob/main/docs/architecture/calculation-standard.md) governs denominators, conversions and uncertainty. Preserve unresolved conflicts instead of selecting convenient evidence.

See [[Professional Skillsets|Professional-Skillsets]] for workflow inputs and outputs.
