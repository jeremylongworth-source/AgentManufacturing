# industrial-engineering-specialist

Analyze production capacity and work balance from declared measurements.

Status: `STRUCTURALLY_READY`; Runtime model behavior: `NOT_RUN`. This is a role composition, not an additional atomic skill or professional authorization.

## Select a workflow

| Workflow | Use when | Required evidence | Deliverable | Boundary |
|---|---|---|---|---|
| `line-balance` | Review cycle evidence and propose a line balance. | Cycle observations, demand, time units and task constraints. | Balance proposal with measured constraints. | No unsafe pace or workplace redesign approval. |
| `capacity-review` | Identify capacity and bottleneck evidence. | Capacity basis, equipment downtime and production context. | Capacity and bottleneck evidence brief. | Do not infer causation from a utilization percentage. |

Read the [manifest](skillset.yaml) for workflow membership and the [composition contract](../composition-contract.json) for shared boundaries. The manifest uses JSON-compatible YAML for dependency-free parsing.

## Atomic entry points

- [analyze-cycle-time](../../skills/family-05-performance/analyze-cycle-time/SKILL.md).
- [calculate-takt-time](../../skills/family-05-performance/calculate-takt-time/SKILL.md).
- [balance-production-line](../../skills/family-05-performance/balance-production-line/SKILL.md).
- [calculate-production-capacity](../../skills/family-05-performance/calculate-production-capacity/SKILL.md).
- [identify-manufacturing-bottleneck](../../skills/family-01-fundamentals/identify-manufacturing-bottleneck/SKILL.md).
- [calculate-capacity-utilization](../../skills/family-05-performance/calculate-capacity-utilization/SKILL.md).

## Evidence handoff

Select the user's workflow, inspect its atomic inputs and reuse compatible existing evidence before requesting new work. Preserve product/process, facility, period, units, source revision and uncertainty across steps. Do not treat the resolver's ordered list as an instruction to execute every skill or as proof that prerequisites passed.

Use the contract's jurisdiction, source, provincial or WHMIS routes when the requested conclusion needs them; explicitly select the route in the resolver. Automatic legal applicability is not implemented. Missing sector coverage remains a research handoff.

Return the requested deliverable, per-skill status, unsupported conclusions and review owners. A partial or blocked prerequisite blocks the dependent conclusion even if later skills appear in the manifest. Generic supported work may continue. No role title grants release, engineering, regulatory, operating or business-commitment authority.

## Resolve references

From the repository root:

```powershell
python scripts/resolve-skillset.py industrial-engineering-specialist line-balance
```

Add `--overlay provincial` or another named overlay only when that research is selected. The command emits paths and evidence dependencies; it does not run skills, call a model, install files or change live systems. [Acceptance evidence](../../tests/evaluations/AM-28-professional-skillsets-acceptance.md) separates structural verification from runtime behavior.
