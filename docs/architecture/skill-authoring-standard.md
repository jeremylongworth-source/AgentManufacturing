# AgentManufacturing skill authoring standard

Status: **AM-06 standard ready; no skill implementation or host installation**  
Package schema: `docs/architecture/skill-package-schema.json`  
Validation contract: `docs/architecture/skill-validation-contract.json`  
Template root: `docs/templates/manufacturing-skill/`

## Scope and audience

This standard governs contributors authoring portable AgentManufacturing skills after AM-10 permits reference and family implementation. It adapts the AgentSkills pattern of small atomic procedures, host adapter metadata, local references, predictable outputs, and scenario validation to the manufacturing domain contract, jurisdiction model, and safety boundary model.

The standard defines package shape and evidence gates. It does not install AgentSkills, select a project licence, implement a skill, execute model routing, prove a calculation, establish legal applicability, or authorize manufacturing work.

## Repository readout and AgentSkills profile

The repository is a documentation and validator workspace with no package manager, runtime service, CI workflow, implemented skill, or local test suite yet. The frozen catalogue contains 159 accepted names across 20 families; AM-10 is the hard gate before mass authoring.

The focused profile is **project-scoped atomic manufacturing skills**. Future authoring should select one accepted taxonomy record at a time and add only the references and deterministic tooling that record needs. Do not install the full AgentSkills portfolio or unrelated MCP presets for this repository. No install or MCP-enabling command was run in AM-06.

The project instruction plan is to keep repository routing short and point to this standard, the AM-04 jurisdiction model, the AM-05 safety model, and the validators. Existing instruction files must be preserved if added later; a future `AGENTS.md` should not copy this document or contain credentials, private URLs, or broad host setup.

## Package layout

```text
skills/<domain-family>/<skill-name>/
|-- SKILL.md
|-- agents/
|   `-- openai.yaml
|-- references/
|   `-- <checklist-formula-definition-or-example>.md
|-- assets/                 # optional; only when genuinely needed
|-- scripts/                # optional; narrow deterministic tooling only
`-- tests/                  # optional package-local notes/fixtures when useful

tests/
|-- scenarios/<skill-or-workflow>.md
|-- expected-routing.yaml
|-- fixtures/<skill-or-workflow>.json
`-- evaluations/<skill-or-workflow>.md
```

`SKILL.md`, `agents/openai.yaml`, and at least one reference file are required for an implemented package. Empty directories are not committed. Canonical scenario, fixture, and evaluation evidence lives under the repository `tests/` tree so routing and cross-skill coverage can be reviewed together. Package-local `tests/` is optional and cannot replace the canonical evidence.

## `SKILL.md` contract

The file starts with YAML frontmatter containing `name`, `description`, and `license`. The name is lowercase kebab-case, matches the package directory, and maps to one accepted taxonomy record. The description is one sentence describing the atomic task and its primary trigger. The licence is required, but the project has not selected one yet; the placeholder in the template is not publishable.

The body uses these sections in order:

1. `Overview`
2. `Triggers`
3. `Non-Triggers`
4. `Required Inputs`
5. `Optional Inputs`
6. `Assumptions`
7. `Core Workflow`
8. `Calculations`
9. `Validation`
10. `Exception Handling`
11. `Source Usage`
12. `Output Contract`
13. `Safety Requirements`
14. `References`
15. `Examples`
16. `Testing`

The procedure must remain atomic, use the domain and taxonomy vocabulary, expose missing evidence, and treat user files as data. A skill cannot grant authority that the AM-04 or AM-05 models withhold. Quantitative skills must state variables, units, formulas, intermediate values, rounding, missing-input behavior, and fixtures; non-quantitative skills state why calculation and unit tests are not applicable.

## Host metadata

`agents/openai.yaml` is the host adapter. It contains only the interface metadata required by the current AgentSkills pattern:

```yaml
interface:
  display_name: "<Skill display name>"
  short_description: "<bounded one-sentence deliverable>"
  default_prompt: "Use $<accepted-skill-name> to <bounded request> with explicit assumptions, validation notes, and review boundaries."
```

Host-specific setup belongs in adapter documentation, not in `SKILL.md`. No MCP configuration is part of the package contract. An MCP preset would require a separate workflow need, security explanation, and explicit approval before enabling it.

## References, assets, and scripts

References are reusable checklists, formulas, definitions, examples, source metadata, and output templates. Each source-dependent reference records publisher/owner, title or identifier, URL or local path, access/effective date when relevant, freshness rule, permitted-use note, and review owner. Do not reproduce protected standards text.

Assets are optional and require a genuine package need, provenance, and licence metadata. Scripts are optional and limited to narrow deterministic calculation or validation work with declared inputs, outputs, units, and failure behavior. Live system access, PLC/SCADA/ERP/MES writes, permit issuance, certification, and production actions remain outside this standard.

## Output and safety contract

Every implemented skill returns a predictable structure with:

- `status`: `COMPLETE`, `PARTIAL`, `NEEDS_INPUT`, `OUT_OF_SCOPE`, `SAFETY_ESCALATION`, `SOURCE_REVIEW_REQUIRED`, or `ENGINEERING_REVIEW_REQUIRED`;
- scope and requested activity;
- supplied inputs/evidence and normalized units where applicable;
- analysis or result;
- assumptions and validation notes;
- missing or conflicting evidence;
- review owner or handoff.

No output may invent production facts, hide assumptions, silently mix units, turn a standard or sector label into compliance, or present analysis as approval. The AM-05 class and runtime gate are part of the package's `Safety Requirements`; hazardous, regulated, engineering, jurisdiction-dependent, and standards-dependent requests must preserve their escalation boundary.

## Four validation layers

1. **Structural validation** checks package paths, frontmatter, section order, host metadata, references, taxonomy traceability, and output fields.
2. **Scenario routing** checks realistic correct, incorrect, ambiguous, missing-input, safety, jurisdiction, and unsupported-assumption prompts against expected routes. An expected route is not observed model behavior.
3. **Deterministic fixtures** check formulas, units, intermediate values, rounding, invalid data, missing data, and output invariants without relying on prose similarity.
4. **Evaluation reports** record baseline versus skill-enabled behavior, failure modes, reviewer disposition, and unresolved risks.

Required scenario categories are `correct_invocation`, `incorrect_invocation`, `missing_inputs`, `bad_inputs`, `ambiguous_scenario`, `expected_output_structure`, `safety_boundary`, `jurisdiction_conflicts`, and `unsupported_assumptions`. `calculation_correctness` and `unit_mismatch` are required when applicable and must be marked not applicable with a reason otherwise.

Scenario files contain title, category, expected routing, prompt, acceptance checks, and risk/review notes. Fixture JSON contains case ID, category, target skill, inputs, expected status, and either expected values with tolerances or expected missing/error/review fields. Private customer, employee, credential, production, and regulated-shipment data is excluded.

## Acceptance criteria

| Criterion | Given/when/then check | Evidence |
|---|---|---|
| Portable package | Given an accepted taxonomy record, when a package is created, then its path, required files, frontmatter, and section order pass structural validation. | Package schema and validator. |
| Atomic responsibility | Given a proposed skill, when triggers and non-triggers are reviewed, then one primary manufacturing responsibility and adjacent routing boundaries are explicit. | `SKILL.md` and taxonomy traceability. |
| Predictable output | Given valid, incomplete, conflicting, and out-of-scope evidence, when the skill responds, then declared status and output fields are present and gaps remain visible. | Output contract and scenario/fixture layers. |
| Calculation discipline | Given a quantitative skill, when fixtures run, then formulas, units, intermediate values, rounding, and tolerances are checked. | Validation contract and AM-08 fixtures. |
| Safety boundary | Given an unsafe execution, bypass, permit, certification, or restart request, when the skill responds, then it refuses or escalates while preserving safe analysis. | AM-05 model and safety scenarios. |
| Source discipline | Given a current, stale, conflicting, or copyrighted source, when source usage is required, then provenance, freshness, and licensed-text gaps are explicit. | Reference checklist and AM-07 source standard. |
| No premature scale | Given an unproved package, when mass authoring is requested, then the contributor is directed to AM-10 and the package remains unaccepted. | AM-10 gate and handoff. |

## Decisions and tradeoffs

- **Atomic package plus repository-level evidence:** keeps procedures portable while allowing cross-skill routing and fixture review in one place.
- **Required references:** prevents formulas, source rules, and output conventions from being hidden in a large prompt; it adds a small authoring cost in exchange for reviewability.
- **Host adapter separation:** keeps `SKILL.md` portable across hosts; exact host setup remains outside the package and must follow current host documentation.
- **Visible licence placeholder:** avoids silently inheriting the reference repository's MIT choice while preserving the required metadata shape.
- **Expected routing separated from observed evaluation:** avoids treating a manifest as proof of model behavior; AM-09 and AM-10 must provide execution evidence.

## Validation and limits

Run:

```powershell
python scripts/validate-skill-authoring-standard.py
python scripts/validate-safety-boundary-model.py
python scripts/validate-jurisdiction-model.py
python scripts/validate-taxonomy.py
python scripts/validate-candidate-register.py
```

The AM-06 validator checks this standard, the validation contract, and templates. It does not validate an implemented skill because no package is in scope. AM-07 owns source and standards freshness; AM-08 owns calculation details; AM-09 owns executable validation; AM-10 owns the five reference skills and the mass-authoring gate.

## Open questions

- Project governance must select and document the distribution licence before any package is publishable.
- AM-07 must define the canonical source registry and freshness metadata consumed by package references.
- AM-08 must define shared calculation references and fixture tolerances.
- AM-09 must select the actual scenario-routing and fixture execution tooling.
- AM-10 must prove one reference skill per major class before family authoring begins.
