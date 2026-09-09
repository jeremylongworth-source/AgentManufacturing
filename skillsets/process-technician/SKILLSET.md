# process-technician

Review process records and deviations against controlled evidence.

Status: `STRUCTURALLY_READY`; Runtime model behavior: `NOT_RUN`. This is a role composition, not an additional atomic skill or professional authorization.

## Select a workflow

| Workflow | Use when | Required evidence | Deliverable | Boundary |
|---|---|---|---|---|
| `parameter-review` | Map process inputs and review parameter controls. | Process boundary, input/output records and approved parameter criteria. | Parameter-control evidence gaps. | No process setpoint change. |
| `deviation-review` | Review standard-work deviation and document a nonconformance. | Current revision, observation and affected process/product. | Deviation and nonconformance draft. | Do not infer root cause or disposition. |

Read the [manifest](skillset.yaml) for workflow membership and the [composition contract](../composition-contract.json) for shared boundaries. The manifest uses JSON-compatible YAML for dependency-free parsing.

## Atomic entry points

- [identify-process-inputs-outputs](../../skills/family-04-process-engineering/identify-process-inputs-outputs/SKILL.md).
- [review-process-parameter-control](../../skills/family-04-process-engineering/review-process-parameter-control/SKILL.md).
- [analyze-standard-work-deviation](../../skills/family-03-standard-work/analyze-standard-work-deviation/SKILL.md).
- [document-nonconformance](../../skills/family-09-nonconformance-capa/document-nonconformance/SKILL.md).

## Evidence handoff

Select the user's workflow, inspect its atomic inputs and reuse compatible existing evidence before requesting new work. Preserve product/process, facility, period, units, source revision and uncertainty across steps. Do not treat the resolver's ordered list as an instruction to execute every skill or as proof that prerequisites passed.

Use the contract's jurisdiction, source, provincial or WHMIS routes when the requested conclusion needs them; explicitly select the route in the resolver. Automatic legal applicability is not implemented. Missing sector coverage remains a research handoff.

Return the requested deliverable, per-skill status, unsupported conclusions and review owners. A partial or blocked prerequisite blocks the dependent conclusion even if later skills appear in the manifest. Generic supported work may continue. No role title grants release, engineering, regulatory, operating or business-commitment authority.

## Resolve references

From the repository root:

```powershell
python scripts/resolve-skillset.py process-technician parameter-review
```

Add `--overlay provincial` or another named overlay only when that research is selected. The command emits paths and evidence dependencies; it does not run skills, call a model, install files or change live systems. [Acceptance evidence](../../tests/evaluations/AM-28-professional-skillsets-acceptance.md) separates structural verification from runtime behavior.
