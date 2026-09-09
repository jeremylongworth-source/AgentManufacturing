# reliability-analyst

Analyze failure and downtime evidence without promising reliability outcomes.

Status: `STRUCTURALLY_READY`; Runtime model behavior: `NOT_RUN`. This is a role composition, not an additional atomic skill or professional authorization.

## Select a workflow

| Workflow | Use when | Required evidence | Deliverable | Boundary |
|---|---|---|---|---|
| `reliability-metrics` | Review failures and calculate supported reliability metrics. | Failure counts, exposure intervals, repair durations and consistent boundaries. | Reliability metrics with population and time basis. | Do not infer future reliability or causal improvement. |
| `failure-review` | Investigate equipment failures and draft predictive monitoring options. | Failure evidence, condition data and available monitoring methods. | Failure review and monitoring proposal. | No machine fitness-for-service or safe-operation approval. |

Read the [manifest](skillset.yaml) for workflow membership and the [composition contract](../composition-contract.json) for shared boundaries. The manifest uses JSON-compatible YAML for dependency-free parsing.

## Atomic entry points

- [analyze-failure-history](../../skills/family-10-maintenance-reliability/analyze-failure-history/SKILL.md).
- [calculate-mtbf](../../skills/family-10-maintenance-reliability/calculate-mtbf/SKILL.md).
- [calculate-mttr](../../skills/family-10-maintenance-reliability/calculate-mttr/SKILL.md).
- [analyze-equipment-downtime](../../skills/family-10-maintenance-reliability/analyze-equipment-downtime/SKILL.md).
- [perform-equipment-failure-analysis](../../skills/family-10-maintenance-reliability/perform-equipment-failure-analysis/SKILL.md).
- [build-predictive-maintenance-plan](../../skills/family-10-maintenance-reliability/build-predictive-maintenance-plan/SKILL.md).

## Evidence handoff

Select the user's workflow, inspect its atomic inputs and reuse compatible existing evidence before requesting new work. Preserve product/process, facility, period, units, source revision and uncertainty across steps. Do not treat the resolver's ordered list as an instruction to execute every skill or as proof that prerequisites passed.

Use the contract's jurisdiction, source, provincial or WHMIS routes when the requested conclusion needs them; explicitly select the route in the resolver. Automatic legal applicability is not implemented. Missing sector coverage remains a research handoff.

Return the requested deliverable, per-skill status, unsupported conclusions and review owners. A partial or blocked prerequisite blocks the dependent conclusion even if later skills appear in the manifest. Generic supported work may continue. No role title grants release, engineering, regulatory, operating or business-commitment authority.

## Resolve references

From the repository root:

```powershell
python scripts/resolve-skillset.py reliability-analyst reliability-metrics
```

Add `--overlay provincial` or another named overlay only when that research is selected. The command emits paths and evidence dependencies; it does not run skills, call a model, install files or change live systems. [Acceptance evidence](../../tests/evaluations/AM-28-professional-skillsets-acceptance.md) separates structural verification from runtime behavior.
