# metrology-specialist

Review measurement suitability, calibration and traceability evidence.

Status: `STRUCTURALLY_READY`; Runtime model behavior: `NOT_RUN`. This is a role composition, not an additional atomic skill or professional authorization.

## Select a workflow

| Workflow | Use when | Required evidence | Deliverable | Boundary |
|---|---|---|---|---|
| `measurement-system` | Assess a measurement method and study evidence. | Measurand, method, equipment and measurement-study design. | Measurement suitability and study evidence review. | No invented study results or calibration certification. |
| `calibration-risk` | Review calibration status and affected measurement evidence. | Register, calibration documents, use history and traceability. | Calibration evidence and affected-use handoff. | Do not declare affected product acceptable. |

Read the [manifest](skillset.yaml) for workflow membership and the [composition contract](../composition-contract.json) for shared boundaries. The manifest uses JSON-compatible YAML for dependency-free parsing.

## Atomic entry points

- [select-measurement-method](../../skills/family-07-metrology/select-measurement-method/SKILL.md).
- [review-measurement-equipment](../../skills/family-07-metrology/review-measurement-equipment/SKILL.md).
- [analyze-measurement-system](../../skills/family-07-metrology/analyze-measurement-system/SKILL.md).
- [build-calibration-register](../../skills/family-07-metrology/build-calibration-register/SKILL.md).
- [review-calibration-status](../../skills/family-07-metrology/review-calibration-status/SKILL.md).
- [identify-out-of-calibration-risk](../../skills/family-07-metrology/identify-out-of-calibration-risk/SKILL.md).
- [assess-measurement-traceability](../../skills/family-07-metrology/assess-measurement-traceability/SKILL.md).

## Evidence handoff

Select the user's workflow, inspect its atomic inputs and reuse compatible existing evidence before requesting new work. Preserve product/process, facility, period, units, source revision and uncertainty across steps. Do not treat the resolver's ordered list as an instruction to execute every skill or as proof that prerequisites passed.

Use the contract's jurisdiction, source, provincial or WHMIS routes when the requested conclusion needs them; explicitly select the route in the resolver. Automatic legal applicability is not implemented. Missing sector coverage remains a research handoff.

Return the requested deliverable, per-skill status, unsupported conclusions and review owners. A partial or blocked prerequisite blocks the dependent conclusion even if later skills appear in the manifest. Generic supported work may continue. No role title grants release, engineering, regulatory, operating or business-commitment authority.

## Resolve references

From the repository root:

```powershell
python scripts/resolve-skillset.py metrology-specialist measurement-system
```

Add `--overlay provincial` or another named overlay only when that research is selected. The command emits paths and evidence dependencies; it does not run skills, call a model, install files or change live systems. [Acceptance evidence](../../tests/evaluations/AM-28-professional-skillsets-acceptance.md) separates structural verification from runtime behavior.
