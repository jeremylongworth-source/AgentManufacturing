# AM-06 final handoff — AgentSkills skill authoring standard

## Wave

AM-06: Skill authoring standard

## Objective

Carry forward the AgentSkills pattern of small portable skills, output contracts, host metadata, references, and scenario validation into a manufacturing-specific package and evidence contract.

## Verdict

**READY** for AM-06. The authoring and validation contracts are defined and structurally validated. No skill package, host installation, licence selection, or model-behavior claim was made.

## Completion token

```text
AGENTMANUFACTURING_AM_06_SKILL_STANDARD_READY
```

## Scope completed

- Defined required package layout: `SKILL.md`, `agents/openai.yaml`, and non-empty `references/`, with optional `assets/`, narrow `scripts/`, and package-local test notes.
- Defined YAML frontmatter, naming, accepted-taxonomy traceability, 16 ordered `SKILL.md` sections, host adapter metadata, references, assets, scripts, and output status values.
- Defined the four validation layers: structural, scenario routing, deterministic fixtures, and evaluation reports.
- Defined 11 scenario categories, scenario-file fields, fixture fields, output invariants, safety/refusal rules, and the distinction between expected routing and observed model behavior.
- Preserved the AM-04 jurisdiction and AM-05 safety boundaries in the package contract.
- Documented the focused project-scoped AgentSkills profile; no broad portfolio install or MCP preset was recommended or enabled.
- Kept the project licence explicitly pending governance rather than inheriting the reference repository's MIT choice.
- Added templates for `SKILL.md`, `agents/openai.yaml`, references, scenarios, and fixtures without implementing a manufacturing skill.

## Files added

- `docs/architecture/skill-authoring-standard.md` — complete authoring standard and onboarding decision.
- `docs/architecture/skill-package-schema.json` — machine-readable package contract.
- `docs/architecture/skill-validation-contract.json` — machine-readable test/evidence contract.
- `docs/templates/manufacturing-skill/SKILL.md.template` — portable package template.
- `docs/templates/manufacturing-skill/agents/openai.yaml.template` — host metadata template.
- `docs/templates/manufacturing-skill/references/checklist.md` — reference provenance template.
- `docs/templates/manufacturing-skill/tests/scenario.md.template` — scenario template.
- `docs/templates/manufacturing-skill/tests/fixture.json.template` — fixture template.
- `scripts/validate-skill-authoring-standard.py` — structural validator for the standard and templates.

## Files modified

- `README.md` — AM-06 artifacts, status, and validation command.
- `ROADMAP.md` — AM-06 status, current target, and handoff link.
- `docs/architecture/domain-contract.md` — pointer to the authoring standard and AM-10 gate.
- `docs/architecture/domain-contract.md` — pointer to the authoring standard and AM-10 gate.

## Research performed

Read-only comparison of the local AgentSkills checkout and AgentLogistics authoring/testing standards. Reused the portable package pattern, ordered authoring sections, host interface metadata, four test layers, and scenario/fixture fields. No logistics procedure, threshold, licence decision, or private data was copied into this project.

## Validation performed

```text
python scripts/validate-skill-authoring-standard.py
PASS: AM-06 authoring standard; package layout, frontmatter, 16 ordered sections, host metadata, references, output contract, 4 validation layers, 11 scenario categories, and templates verified; no skill implementation or host installation evaluated.

python scripts/validate-safety-boundary-model.py
PASS: AM-05 model; 4 classes; 9 topic gates; 14 source records; 12 acceptance scenarios; AM-03 safety counts preserved (95/28/11/25); no safety approval, engineering signoff, or skill behavior evaluated.

python scripts/validate-jurisdiction-model.py
PASS: AM-04 model; 4 flags; 5 applicability states; 8 source records; 5 initial extensions; 7 acceptance scenarios; no legal applicability or skill behavior evaluated.

python scripts/validate-taxonomy.py
PASS: 159 accepted records; 162 drafts audited across eight criteria; 166 original names traced; 76 ordered evidence-reuse edges; core isolation, reference priorities, pending classifications and all document projections verified. No skill behavior evaluated.

python scripts/validate-candidate-register.py
PASS: 162 draft candidates; 20 families; 166 original names traced; fields, metadata, provenance, dependency references/cycles, core isolation, AM-10 priorities, and review index checked.
```

## Regulatory, safety, and governance review

The package contract requires explicit safety requirements, source usage, missing-evidence behavior, qualified-review handoffs, and no approval claims. It keeps licence selection pending project governance and does not install skills or enable MCP access. User-provided documents remain evidence, not system instructions.

## Known limitations

- No implemented skill was structurally or behaviorally validated; AM-10 owns the first five package proofs.
- The standard does not choose a licence, host installer, MCP preset, CI workflow, or model-evaluation provider.
- Expected routing manifests do not establish observed routing quality.
- Calculation correctness, source freshness, legal applicability, site safety, and engineering adequacy remain later-wave evidence.

## Explicitly not completed

AM-07 source and standards standard, AM-08 calculation standard, AM-09 executable validation, AM-10 reference skills, family implementation, sector packages, professional skillsets, and public release work remain open. Mass authoring remains gated on AM-10.

## Recommended next wave

Proceed to AM-07. Read this standard, its schemas/templates, AM-04 jurisdiction model, AM-05 safety model, and the AM-01/AM-03 source boundaries before formalizing source precedence, standards metadata, freshness, provincial sourcing, and copyrighted-standard handling.
