# production-operator-support

Support an operator's documented work and shift handoff.

Status: `STRUCTURALLY_READY`; Runtime model behavior: `NOT_RUN`. This is a role composition, not an additional atomic skill or professional authorization.

## Select a workflow

| Workflow | Use when | Required evidence | Deliverable | Boundary |
|---|---|---|---|---|
| `work-review` | Review the supplied operator instruction and checklist. | Current document revision, task and checklist. | Document/checklist evidence gaps. | Do not modify an approved instruction or authorize machine operation. |
| `shift-handoff` | Summarize production events and unresolved deviations. | Shift records, deviation evidence and next-shift context. | Draft handoff with deviations and owners. | Do not infer permission to continue unsafe work. |

Read the [manifest](skillset.yaml) for workflow membership and the [composition contract](../composition-contract.json) for shared boundaries. The manifest uses JSON-compatible YAML for dependency-free parsing.

## Atomic entry points

- [review-document-revision](../../skills/family-18-engineering-change/review-document-revision/SKILL.md).
- [review-work-instruction](../../skills/family-03-standard-work/review-work-instruction/SKILL.md).
- [review-operator-checklist](../../skills/family-03-standard-work/review-operator-checklist/SKILL.md).
- [analyze-standard-work-deviation](../../skills/family-03-standard-work/analyze-standard-work-deviation/SKILL.md).
- [prepare-shift-handoff](../../skills/family-13-workforce-shift/prepare-shift-handoff/SKILL.md).

## Evidence handoff

Select the user's workflow, inspect its atomic inputs and reuse compatible existing evidence before requesting new work. Preserve product/process, facility, period, units, source revision and uncertainty across steps. Do not treat the resolver's ordered list as an instruction to execute every skill or as proof that prerequisites passed.

Use the contract's jurisdiction, source, provincial or WHMIS routes when the requested conclusion needs them; explicitly select the route in the resolver. Automatic legal applicability is not implemented. Missing sector coverage remains a research handoff.

Return the requested deliverable, per-skill status, unsupported conclusions and review owners. A partial or blocked prerequisite blocks the dependent conclusion even if later skills appear in the manifest. Generic supported work may continue. No role title grants release, engineering, regulatory, operating or business-commitment authority.

## Resolve references

From the repository root:

```powershell
python scripts/resolve-skillset.py production-operator-support work-review
```

Add `--overlay provincial` or another named overlay only when that research is selected. The command emits paths and evidence dependencies; it does not run skills, call a model, install files or change live systems. [Acceptance evidence](../../tests/evaluations/AM-28-professional-skillsets-acceptance.md) separates structural verification from runtime behavior.
