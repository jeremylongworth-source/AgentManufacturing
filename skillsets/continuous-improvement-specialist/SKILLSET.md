# continuous-improvement-specialist

Shape improvement experiments from observed flow and loss evidence.

Status: `STRUCTURALLY_READY`; Runtime model behavior: `NOT_RUN`. This is a role composition, not an additional atomic skill or professional authorization.

## Select a workflow

| Workflow | Use when | Required evidence | Deliverable | Boundary |
|---|---|---|---|---|
| `flow-review` | Map flow and identify improvement opportunities. | Process boundary, observations, timings and waste evidence. | Flow evidence and candidate opportunities. | Do not assume every observed delay is removable. |
| `changeover-improvement` | Draft and evaluate a bounded changeover improvement. | Changeover records, baseline, proposed actions and comparable follow-up. | Improvement proposal and measurement comparison. | No trial activation or causal savings without evidence. |

Read the [manifest](skillset.yaml) for workflow membership and the [composition contract](../composition-contract.json) for shared boundaries. The manifest uses JSON-compatible YAML for dependency-free parsing.

## Atomic entry points

- [build-value-stream-map](../../skills/family-14-lean-improvement/build-value-stream-map/SKILL.md).
- [identify-eight-wastes](../../skills/family-14-lean-improvement/identify-eight-wastes/SKILL.md).
- [analyze-flow-efficiency](../../skills/family-14-lean-improvement/analyze-flow-efficiency/SKILL.md).
- [analyze-changeover-loss](../../skills/family-05-performance/analyze-changeover-loss/SKILL.md).
- [build-smed-improvement-plan](../../skills/family-14-lean-improvement/build-smed-improvement-plan/SKILL.md).
- [build-kaizen-plan](../../skills/family-14-lean-improvement/build-kaizen-plan/SKILL.md).
- [measure-improvement-result](../../skills/family-14-lean-improvement/measure-improvement-result/SKILL.md).

## Evidence handoff

Select the user's workflow, inspect its atomic inputs and reuse compatible existing evidence before requesting new work. Preserve product/process, facility, period, units, source revision and uncertainty across steps. Do not treat the resolver's ordered list as an instruction to execute every skill or as proof that prerequisites passed.

Use the contract's jurisdiction, source, provincial or WHMIS routes when the requested conclusion needs them; explicitly select the route in the resolver. Automatic legal applicability is not implemented. Missing sector coverage remains a research handoff.

Return the requested deliverable, per-skill status, unsupported conclusions and review owners. A partial or blocked prerequisite blocks the dependent conclusion even if later skills appear in the manifest. Generic supported work may continue. No role title grants release, engineering, regulatory, operating or business-commitment authority.

## Resolve references

From the repository root:

```powershell
python scripts/resolve-skillset.py continuous-improvement-specialist flow-review
```

Add `--overlay provincial` or another named overlay only when that research is selected. The command emits paths and evidence dependencies; it does not run skills, call a model, install files or change live systems. [Acceptance evidence](../../tests/evaluations/AM-28-professional-skillsets-acceptance.md) separates structural verification from runtime behavior.
