# manufacturing-engineer-support

Prepare process and change evidence for engineering review.

Status: `STRUCTURALLY_READY`; Runtime model behavior: `NOT_RUN`. This is a role composition, not an additional atomic skill or professional authorization.

## Select a workflow

| Workflow | Use when | Required evidence | Deliverable | Boundary |
|---|---|---|---|---|
| `process-design-review` | Compare process alternatives and draft controls. | Product requirements, process maps, alternatives and constraints. | Process options and draft control plan. | No design validation or engineering signoff. |
| `change-review` | Assess a proposed manufacturing process change. | Change package, technical basis and affected process records. | Change impacts and review handoff. | No change activation, machine release or certification. |

Read the [manifest](skillset.yaml) for workflow membership and the [composition contract](../composition-contract.json) for shared boundaries. The manifest uses JSON-compatible YAML for dependency-free parsing.

## Atomic entry points

- [map-manufacturing-process](../../skills/family-04-process-engineering/map-manufacturing-process/SKILL.md).
- [compare-process-alternatives](../../skills/family-04-process-engineering/compare-process-alternatives/SKILL.md).
- [build-process-control-plan](../../skills/family-04-process-engineering/build-process-control-plan/SKILL.md).
- [review-change-package](../../skills/family-18-engineering-change/review-change-package/SKILL.md).
- [build-engineering-change-impact-assessment](../../skills/family-18-engineering-change/build-engineering-change-impact-assessment/SKILL.md).
- [review-process-change](../../skills/family-18-engineering-change/review-process-change/SKILL.md).

## Evidence handoff

Select the user's workflow, inspect its atomic inputs and reuse compatible existing evidence before requesting new work. Preserve product/process, facility, period, units, source revision and uncertainty across steps. Do not treat the resolver's ordered list as an instruction to execute every skill or as proof that prerequisites passed.

Use the contract's jurisdiction, source, provincial or WHMIS routes when the requested conclusion needs them; explicitly select the route in the resolver. Automatic legal applicability is not implemented. Missing sector coverage remains a research handoff.

Return the requested deliverable, per-skill status, unsupported conclusions and review owners. A partial or blocked prerequisite blocks the dependent conclusion even if later skills appear in the manifest. Generic supported work may continue. No role title grants release, engineering, regulatory, operating or business-commitment authority.

## Resolve references

From the repository root:

```powershell
python scripts/resolve-skillset.py manufacturing-engineer-support process-design-review
```

Add `--overlay provincial` or another named overlay only when that research is selected. The command emits paths and evidence dependencies; it does not run skills, call a model, install files or change live systems. [Acceptance evidence](../../tests/evaluations/AM-28-professional-skillsets-acceptance.md) separates structural verification from runtime behavior.
