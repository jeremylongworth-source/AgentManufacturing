# plant-manager-support

Assemble cross-functional review evidence and decisions for responsible owners.

Status: `STRUCTURALLY_READY`; Runtime model behavior: `NOT_RUN`. This is a role composition, not an additional atomic skill or professional authorization.

## Select a workflow

| Workflow | Use when | Required evidence | Deliverable | Boundary |
|---|---|---|---|---|
| `plant-review` | Review plant KPI, readiness and qualification evidence. | KPI model, production readiness, qualification records and unresolved issues. | Plant review brief with unresolved decisions and owners. | Do not certify workers or release operations from a summary. |
| `investment-change-review` | Review an automation case and proposed change evidence. | Readiness, option costs, technical basis and change package. | Investment/change evidence and qualified handoff. | No budget commitment, purchase, engineering signoff or automation deployment. |

Read the [manifest](skillset.yaml) for workflow membership and the [composition contract](../composition-contract.json) for shared boundaries. The manifest uses JSON-compatible YAML for dependency-free parsing.

## Atomic entry points

- [build-manufacturing-kpi-model](../../skills/family-15-systems-data/build-manufacturing-kpi-model/SKILL.md).
- [review-production-order-readiness](../../skills/family-02-production-planning/review-production-order-readiness/SKILL.md).
- [review-operator-qualification-record](../../skills/family-13-workforce-shift/review-operator-qualification-record/SKILL.md).
- [build-automation-business-case](../../skills/family-16-advanced-manufacturing/build-automation-business-case/SKILL.md).
- [review-change-package](../../skills/family-18-engineering-change/review-change-package/SKILL.md).
- [build-engineering-change-impact-assessment](../../skills/family-18-engineering-change/build-engineering-change-impact-assessment/SKILL.md).

## Evidence handoff

Select the user's workflow, inspect its atomic inputs and reuse compatible existing evidence before requesting new work. Preserve product/process, facility, period, units, source revision and uncertainty across steps. Do not treat the resolver's ordered list as an instruction to execute every skill or as proof that prerequisites passed.

Use the contract's jurisdiction, source, provincial or WHMIS routes when the requested conclusion needs them; explicitly select the route in the resolver. Automatic legal applicability is not implemented. Missing sector coverage remains a research handoff.

Return the requested deliverable, per-skill status, unsupported conclusions and review owners. A partial or blocked prerequisite blocks the dependent conclusion even if later skills appear in the manifest. Generic supported work may continue. No role title grants release, engineering, regulatory, operating or business-commitment authority.

## Resolve references

From the repository root:

```powershell
python scripts/resolve-skillset.py plant-manager-support plant-review
```

Add `--overlay provincial` or another named overlay only when that research is selected. The command emits paths and evidence dependencies; it does not run skills, call a model, install files or change live systems. [Acceptance evidence](../../tests/evaluations/AM-28-professional-skillsets-acceptance.md) separates structural verification from runtime behavior.
