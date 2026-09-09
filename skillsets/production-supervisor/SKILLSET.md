# production-supervisor

Translate approved plans into shift-level review and handoff.

Status: `STRUCTURALLY_READY`; Runtime model behavior: `NOT_RUN`. This is a role composition, not an additional atomic skill or professional authorization.

## Select a workflow

| Workflow | Use when | Required evidence | Deliverable | Boundary |
|---|---|---|---|---|
| `shift-plan` | Allocate a supplied approved horizon to a shift. | Approved plan, readiness, staffing qualifications and shift window. | Shift allocation proposal with unmet constraints. | Do not approve overtime or unqualified assignments. |
| `shift-review` | Review schedule performance and hand over unresolved events. | Planned/actual order history and shift records. | Schedule exceptions and next-shift handoff. | No live rescheduling or unsafe-work direction. |

Read the [manifest](skillset.yaml) for workflow membership and the [composition contract](../composition-contract.json) for shared boundaries. The manifest uses JSON-compatible YAML for dependency-free parsing.

## Atomic entry points

- [review-production-order-readiness](../../skills/family-02-production-planning/review-production-order-readiness/SKILL.md).
- [build-shift-production-plan](../../skills/family-13-workforce-shift/build-shift-production-plan/SKILL.md).
- [balance-workforce](../../skills/family-13-workforce-shift/balance-workforce/SKILL.md).
- [analyze-schedule-adherence](../../skills/family-02-production-planning/analyze-schedule-adherence/SKILL.md).
- [prepare-shift-handoff](../../skills/family-13-workforce-shift/prepare-shift-handoff/SKILL.md).

## Evidence handoff

Select the user's workflow, inspect its atomic inputs and reuse compatible existing evidence before requesting new work. Preserve product/process, facility, period, units, source revision and uncertainty across steps. Do not treat the resolver's ordered list as an instruction to execute every skill or as proof that prerequisites passed.

Use the contract's jurisdiction, source, provincial or WHMIS routes when the requested conclusion needs them; explicitly select the route in the resolver. Automatic legal applicability is not implemented. Missing sector coverage remains a research handoff.

Return the requested deliverable, per-skill status, unsupported conclusions and review owners. A partial or blocked prerequisite blocks the dependent conclusion even if later skills appear in the manifest. Generic supported work may continue. No role title grants release, engineering, regulatory, operating or business-commitment authority.

## Resolve references

From the repository root:

```powershell
python scripts/resolve-skillset.py production-supervisor shift-plan
```

Add `--overlay provincial` or another named overlay only when that research is selected. The command emits paths and evidence dependencies; it does not run skills, call a model, install files or change live systems. [Acceptance evidence](../../tests/evaluations/AM-28-professional-skillsets-acceptance.md) separates structural verification from runtime behavior.
