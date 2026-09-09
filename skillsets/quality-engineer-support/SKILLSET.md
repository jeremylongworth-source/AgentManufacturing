# quality-engineer-support

Support quality investigation, capability and release evidence.

Status: `STRUCTURALLY_READY`; Runtime model behavior: `NOT_RUN`. This is a role composition, not an additional atomic skill or professional authorization.

## Select a workflow

| Workflow | Use when | Required evidence | Deliverable | Boundary |
|---|---|---|---|---|
| `corrective-action` | Build a corrective-action draft from investigation evidence. | Nonconformance, containment, causal evidence and verification plan. | Causal evidence and action/effectiveness review. | Do not convert a proposed cause into a verified one. |
| `capability` | Review capability readiness before calculating indices. | Measurement-system evidence, process stability, specs and within sigma. | Readiness gaps or supported capability calculation. | No product acceptance; do not substitute overall sigma. |
| `release-evidence` | Assemble a quality release review package. | Applicable requirements, product evidence and quality records. | Review package with unresolved evidence. | Only an authorized owner can release product. |

Read the [manifest](skillset.yaml) for workflow membership and the [composition contract](../composition-contract.json) for shared boundaries. The manifest uses JSON-compatible YAML for dependency-free parsing.

## Atomic entry points

- [triage-nonconformance](../../skills/family-09-nonconformance-capa/triage-nonconformance/SKILL.md).
- [perform-root-cause-analysis](../../skills/family-09-nonconformance-capa/perform-root-cause-analysis/SKILL.md).
- [build-corrective-action](../../skills/family-09-nonconformance-capa/build-corrective-action/SKILL.md).
- [verify-corrective-action-effectiveness](../../skills/family-09-nonconformance-capa/verify-corrective-action-effectiveness/SKILL.md).
- [review-capability-readiness](../../skills/family-08-spc-capability/review-capability-readiness/SKILL.md).
- [calculate-cp-cpk](../../skills/family-08-spc-capability/calculate-cp-cpk/SKILL.md).
- [prepare-quality-release-package](../../skills/family-06-quality-management/prepare-quality-release-package/SKILL.md).

## Evidence handoff

Select the user's workflow, inspect its atomic inputs and reuse compatible existing evidence before requesting new work. Preserve product/process, facility, period, units, source revision and uncertainty across steps. Do not treat the resolver's ordered list as an instruction to execute every skill or as proof that prerequisites passed.

Use the contract's jurisdiction, source, provincial or WHMIS routes when the requested conclusion needs them; explicitly select the route in the resolver. Automatic legal applicability is not implemented. Missing sector coverage remains a research handoff.

Return the requested deliverable, per-skill status, unsupported conclusions and review owners. A partial or blocked prerequisite blocks the dependent conclusion even if later skills appear in the manifest. Generic supported work may continue. No role title grants release, engineering, regulatory, operating or business-commitment authority.

## Resolve references

From the repository root:

```powershell
python scripts/resolve-skillset.py quality-engineer-support corrective-action
```

Add `--overlay provincial` or another named overlay only when that research is selected. The command emits paths and evidence dependencies; it does not run skills, call a model, install files or change live systems. [Acceptance evidence](../../tests/evaluations/AM-28-professional-skillsets-acceptance.md) separates structural verification from runtime behavior.
