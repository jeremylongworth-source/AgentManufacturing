# production-planner

Build and compare evidence-based production planning proposals.

Status: `STRUCTURALLY_READY`; Runtime model behavior: `NOT_RUN`. This is a role composition, not an additional atomic skill or professional authorization.

## Select a workflow

| Workflow | Use when | Required evidence | Deliverable | Boundary |
|---|---|---|---|---|
| `horizon-plan` | Build a production plan from compatible demand and capacity evidence. | Demand horizon, capacity, BOM, materials and labor basis. | Production plan proposal and readiness gaps. | No order release, purchasing or business commitment. |
| `scenario-review` | Compare production sequences and alternatives. | Order constraints, comparable scenarios and capacity evidence. | Scenario comparison with capacity constraints. | Do not turn a recommendation into dispatch authority. |

Read the [manifest](skillset.yaml) for workflow membership and the [composition contract](../composition-contract.json) for shared boundaries. The manifest uses JSON-compatible YAML for dependency-free parsing.

## Atomic entry points

- [build-production-plan](../../skills/family-02-production-planning/build-production-plan/SKILL.md).
- [review-production-order-readiness](../../skills/family-02-production-planning/review-production-order-readiness/SKILL.md).
- [sequence-production-orders](../../skills/family-02-production-planning/sequence-production-orders/SKILL.md).
- [identify-capacity-shortfall](../../skills/family-02-production-planning/identify-capacity-shortfall/SKILL.md).
- [compare-production-scenarios](../../skills/family-02-production-planning/compare-production-scenarios/SKILL.md).

## Evidence handoff

Select the user's workflow, inspect its atomic inputs and reuse compatible existing evidence before requesting new work. Preserve product/process, facility, period, units, source revision and uncertainty across steps. Do not treat the resolver's ordered list as an instruction to execute every skill or as proof that prerequisites passed.

Use the contract's jurisdiction, source, provincial or WHMIS routes when the requested conclusion needs them; explicitly select the route in the resolver. Automatic legal applicability is not implemented. Missing sector coverage remains a research handoff.

Return the requested deliverable, per-skill status, unsupported conclusions and review owners. A partial or blocked prerequisite blocks the dependent conclusion even if later skills appear in the manifest. Generic supported work may continue. No role title grants release, engineering, regulatory, operating or business-commitment authority.

## Resolve references

From the repository root:

```powershell
python scripts/resolve-skillset.py production-planner horizon-plan
```

Add `--overlay provincial` or another named overlay only when that research is selected. The command emits paths and evidence dependencies; it does not run skills, call a model, install files or change live systems. [Acceptance evidence](../../tests/evaluations/AM-28-professional-skillsets-acceptance.md) separates structural verification from runtime behavior.
