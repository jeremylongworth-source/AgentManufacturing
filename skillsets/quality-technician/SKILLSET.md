# quality-technician

Prepare inspection and conformity evidence for authorized quality review.

Status: `STRUCTURALLY_READY`; Runtime model behavior: `NOT_RUN`. This is a role composition, not an additional atomic skill or professional authorization.

## Select a workflow

| Workflow | Use when | Required evidence | Deliverable | Boundary |
|---|---|---|---|---|
| `inspection` | Prepare an inspection plan with suitable measurement evidence. | Product requirements, measurement method and inspection scope. | Draft inspection plan and method gaps. | No acceptance criteria invented. |
| `conformity` | Review quality records and record nonconformance. | Applicable requirements, actual records and affected product. | Conformity evidence and nonconformance draft. | No product release or disposition. |

Read the [manifest](skillset.yaml) for workflow membership and the [composition contract](../composition-contract.json) for shared boundaries. The manifest uses JSON-compatible YAML for dependency-free parsing.

## Atomic entry points

- [review-quality-requirement](../../skills/family-06-quality-management/review-quality-requirement/SKILL.md).
- [select-measurement-method](../../skills/family-07-metrology/select-measurement-method/SKILL.md).
- [build-inspection-plan](../../skills/family-06-quality-management/build-inspection-plan/SKILL.md).
- [review-quality-record](../../skills/family-06-quality-management/review-quality-record/SKILL.md).
- [review-product-conformity](../../skills/family-06-quality-management/review-product-conformity/SKILL.md).
- [document-nonconformance](../../skills/family-09-nonconformance-capa/document-nonconformance/SKILL.md).

## Evidence handoff

Select the user's workflow, inspect its atomic inputs and reuse compatible existing evidence before requesting new work. Preserve product/process, facility, period, units, source revision and uncertainty across steps. Do not treat the resolver's ordered list as an instruction to execute every skill or as proof that prerequisites passed.

Use the contract's jurisdiction, source, provincial or WHMIS routes when the requested conclusion needs them; explicitly select the route in the resolver. Automatic legal applicability is not implemented. Missing sector coverage remains a research handoff.

Return the requested deliverable, per-skill status, unsupported conclusions and review owners. A partial or blocked prerequisite blocks the dependent conclusion even if later skills appear in the manifest. Generic supported work may continue. No role title grants release, engineering, regulatory, operating or business-commitment authority.

## Resolve references

From the repository root:

```powershell
python scripts/resolve-skillset.py quality-technician inspection
```

Add `--overlay provincial` or another named overlay only when that research is selected. The command emits paths and evidence dependencies; it does not run skills, call a model, install files or change live systems. [Acceptance evidence](../../tests/evaluations/AM-28-professional-skillsets-acceptance.md) separates structural verification from runtime behavior.
