# manufacturing-technician

Support technical troubleshooting and controlled documentation.

Status: `STRUCTURALLY_READY`; Runtime model behavior: `NOT_RUN`. This is a role composition, not an additional atomic skill or professional authorization.

## Select a workflow

| Workflow | Use when | Required evidence | Deliverable | Boundary |
|---|---|---|---|---|
| `troubleshooting` | Review a production issue using event and parameter evidence. | Equipment/process identity, event history and supplied parameter limits. | Troubleshooting evidence brief. | Do not change live setpoints or bypass controls. |
| `instruction-change` | Draft a controlled work-instruction update for review. | Approved method, source revision and proposed change. | Draft instruction and validation gaps. | No document release or engineering approval. |

Read the [manifest](skillset.yaml) for workflow membership and the [composition contract](../composition-contract.json) for shared boundaries. The manifest uses JSON-compatible YAML for dependency-free parsing.

## Atomic entry points

- [analyze-production-event-history](../../skills/family-15-systems-data/analyze-production-event-history/SKILL.md).
- [review-process-parameter-control](../../skills/family-04-process-engineering/review-process-parameter-control/SKILL.md).
- [review-document-revision](../../skills/family-18-engineering-change/review-document-revision/SKILL.md).
- [draft-work-instruction](../../skills/family-03-standard-work/draft-work-instruction/SKILL.md).
- [review-work-instruction](../../skills/family-03-standard-work/review-work-instruction/SKILL.md).

## Evidence handoff

Select the user's workflow, inspect its atomic inputs and reuse compatible existing evidence before requesting new work. Preserve product/process, facility, period, units, source revision and uncertainty across steps. Do not treat the resolver's ordered list as an instruction to execute every skill or as proof that prerequisites passed.

Use the contract's jurisdiction, source, provincial or WHMIS routes when the requested conclusion needs them; explicitly select the route in the resolver. Automatic legal applicability is not implemented. Missing sector coverage remains a research handoff.

Return the requested deliverable, per-skill status, unsupported conclusions and review owners. A partial or blocked prerequisite blocks the dependent conclusion even if later skills appear in the manifest. Generic supported work may continue. No role title grants release, engineering, regulatory, operating or business-commitment authority.

## Resolve references

From the repository root:

```powershell
python scripts/resolve-skillset.py manufacturing-technician troubleshooting
```

Add `--overlay provincial` or another named overlay only when that research is selected. The command emits paths and evidence dependencies; it does not run skills, call a model, install files or change live systems. [Acceptance evidence](../../tests/evaluations/AM-28-professional-skillsets-acceptance.md) separates structural verification from runtime behavior.
