# operations-manager

Compare production and improvement evidence for management review.

Status: `STRUCTURALLY_READY`; Runtime model behavior: `NOT_RUN`. This is a role composition, not an additional atomic skill or professional authorization.

## Select a workflow

| Workflow | Use when | Required evidence | Deliverable | Boundary |
|---|---|---|---|---|
| `operations-review` | Review plan adherence, quality and labor evidence. | Comparable production plan, actuals, quality records and labor basis. | Operational exceptions and evidence gaps. | No workforce commitment or performance judgment from unverified data. |
| `improvement-review` | Compare production options and measured results. | Scenario assumptions, constraints, baseline and follow-up evidence. | Management review of options and measured outcomes. | No automatic prioritization across safety/quality constraints. |

Read the [manifest](skillset.yaml) for workflow membership and the [composition contract](../composition-contract.json) for shared boundaries. The manifest uses JSON-compatible YAML for dependency-free parsing.

## Atomic entry points

- [analyze-schedule-adherence](../../skills/family-02-production-planning/analyze-schedule-adherence/SKILL.md).
- [analyze-quality-kpis](../../skills/family-06-quality-management/analyze-quality-kpis/SKILL.md).
- [analyze-labor-productivity](../../skills/family-13-workforce-shift/analyze-labor-productivity/SKILL.md).
- [compare-production-scenarios](../../skills/family-02-production-planning/compare-production-scenarios/SKILL.md).
- [measure-improvement-result](../../skills/family-14-lean-improvement/measure-improvement-result/SKILL.md).
- [review-environmental-objective](../../skills/family-19-environment-energy-waste/review-environmental-objective/SKILL.md).

## Evidence handoff

Select the user's workflow, inspect its atomic inputs and reuse compatible existing evidence before requesting new work. Preserve product/process, facility, period, units, source revision and uncertainty across steps. Do not treat the resolver's ordered list as an instruction to execute every skill or as proof that prerequisites passed.

Use the contract's jurisdiction, source, provincial or WHMIS routes when the requested conclusion needs them; explicitly select the route in the resolver. Automatic legal applicability is not implemented. Missing sector coverage remains a research handoff.

Return the requested deliverable, per-skill status, unsupported conclusions and review owners. A partial or blocked prerequisite blocks the dependent conclusion even if later skills appear in the manifest. Generic supported work may continue. No role title grants release, engineering, regulatory, operating or business-commitment authority.

## Resolve references

From the repository root:

```powershell
python scripts/resolve-skillset.py operations-manager operations-review
```

Add `--overlay provincial` or another named overlay only when that research is selected. The command emits paths and evidence dependencies; it does not run skills, call a model, install files or change live systems. [Acceptance evidence](../../tests/evaluations/AM-28-professional-skillsets-acceptance.md) separates structural verification from runtime behavior.
