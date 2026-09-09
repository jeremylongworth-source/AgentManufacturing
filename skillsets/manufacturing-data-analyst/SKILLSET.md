# manufacturing-data-analyst

Assess manufacturing data lineage and metric definitions.

Status: `STRUCTURALLY_READY`; Runtime model behavior: `NOT_RUN`. This is a role composition, not an additional atomic skill or professional authorization.

## Select a workflow

| Workflow | Use when | Required evidence | Deliverable | Boundary |
|---|---|---|---|---|
| `data-quality` | Review event history, lineage and source data quality. | Source extracts, identifiers, timestamps and declared schema. | Data-quality and lineage gaps. | No live ERP/MES changes or inferred missing events. |
| `kpi-review` | Review OEE data and draft a KPI model. | Event data, KPI definitions, units and aggregation basis. | Metric definitions and OEE evidence review. | Do not publish unvalidated metrics or combine incompatible denominators. |

Read the [manifest](skillset.yaml) for workflow membership and the [composition contract](../composition-contract.json) for shared boundaries. The manifest uses JSON-compatible YAML for dependency-free parsing.

## Atomic entry points

- [map-erp-mes-flow](../../skills/family-15-systems-data/map-erp-mes-flow/SKILL.md).
- [analyze-production-event-history](../../skills/family-15-systems-data/analyze-production-event-history/SKILL.md).
- [diagnose-production-data-quality](../../skills/family-15-systems-data/diagnose-production-data-quality/SKILL.md).
- [analyze-oee-data](../../skills/family-15-systems-data/analyze-oee-data/SKILL.md).
- [build-manufacturing-kpi-model](../../skills/family-15-systems-data/build-manufacturing-kpi-model/SKILL.md).

## Evidence handoff

Select the user's workflow, inspect its atomic inputs and reuse compatible existing evidence before requesting new work. Preserve product/process, facility, period, units, source revision and uncertainty across steps. Do not treat the resolver's ordered list as an instruction to execute every skill or as proof that prerequisites passed.

Use the contract's jurisdiction, source, provincial or WHMIS routes when the requested conclusion needs them; explicitly select the route in the resolver. Automatic legal applicability is not implemented. Missing sector coverage remains a research handoff.

Return the requested deliverable, per-skill status, unsupported conclusions and review owners. A partial or blocked prerequisite blocks the dependent conclusion even if later skills appear in the manifest. Generic supported work may continue. No role title grants release, engineering, regulatory, operating or business-commitment authority.

## Resolve references

From the repository root:

```powershell
python scripts/resolve-skillset.py manufacturing-data-analyst data-quality
```

Add `--overlay provincial` or another named overlay only when that research is selected. The command emits paths and evidence dependencies; it does not run skills, call a model, install files or change live systems. [Acceptance evidence](../../tests/evaluations/AM-28-professional-skillsets-acceptance.md) separates structural verification from runtime behavior.
