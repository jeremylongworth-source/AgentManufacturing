# ehs-coordinator-support

Coordinate scoped hazard, jurisdiction and environmental evidence reviews.

Status: `STRUCTURALLY_READY`; Runtime model behavior: `NOT_RUN`. This is a role composition, not an additional atomic skill or professional authorization.

## Select a workflow

| Workflow | Use when | Required evidence | Deliverable | Boundary |
|---|---|---|---|---|
| `safety-review` | Prepare hazard and safety-program review evidence. | Task, facility jurisdiction, equipment hazards and existing programs. | Hazard/program gaps and qualified safety handoff. | No operational JSA authorization, isolation steps or guarding approval. |
| `environment-review` | Inventory environmental aspects and review risk evidence. | Facility activities, stream evidence, criteria and jurisdiction. | Environmental evidence register. | No waste classification, disposal or permit approval. |
| `whmis-review` | Review WHMIS scope and program evidence. | Product roles, jurisdiction, current sources, SDS/labels and training. | Role-separated WHMIS evidence gaps. | No classification, chemical-use or compliance certification. |

Read the [manifest](skillset.yaml) for workflow membership and the [composition contract](../composition-contract.json) for shared boundaries. The manifest uses JSON-compatible YAML for dependency-free parsing.

## Atomic entry points

- [identify-manufacturing-hazard](../../skills/family-11-manufacturing-safety/identify-manufacturing-hazard/SKILL.md).
- [build-job-safety-analysis](../../skills/family-11-manufacturing-safety/build-job-safety-analysis/SKILL.md).
- [review-lockout-program](../../skills/family-11-manufacturing-safety/review-lockout-program/SKILL.md).
- [review-machine-guarding-risk](../../skills/family-11-manufacturing-safety/review-machine-guarding-risk/SKILL.md).
- [identify-manufacturing-environmental-aspect](../../skills/family-19-environment-energy-waste/identify-manufacturing-environmental-aspect/SKILL.md).
- [build-environmental-risk-register](../../skills/family-19-environment-energy-waste/build-environmental-risk-register/SKILL.md).
- [analyze-waste-stream](../../skills/family-19-environment-energy-waste/analyze-waste-stream/SKILL.md).
- [assess-whmis-applicability](../../skills/family-20-canadian-compliance/assess-whmis-applicability/SKILL.md).
- [review-whmis-readiness](../../skills/family-20-canadian-compliance/review-whmis-readiness/SKILL.md).

## Evidence handoff

Select the user's workflow, inspect its atomic inputs and reuse compatible existing evidence before requesting new work. Preserve product/process, facility, period, units, source revision and uncertainty across steps. Do not treat the resolver's ordered list as an instruction to execute every skill or as proof that prerequisites passed.

Use the contract's jurisdiction, source, provincial or WHMIS routes when the requested conclusion needs them; explicitly select the route in the resolver. Automatic legal applicability is not implemented. Missing sector coverage remains a research handoff.

Return the requested deliverable, per-skill status, unsupported conclusions and review owners. A partial or blocked prerequisite blocks the dependent conclusion even if later skills appear in the manifest. Generic supported work may continue. No role title grants release, engineering, regulatory, operating or business-commitment authority.

## Resolve references

From the repository root:

```powershell
python scripts/resolve-skillset.py ehs-coordinator-support safety-review
```

Add `--overlay provincial` or another named overlay only when that research is selected. The command emits paths and evidence dependencies; it does not run skills, call a model, install files or change live systems. [Acceptance evidence](../../tests/evaluations/AM-28-professional-skillsets-acceptance.md) separates structural verification from runtime behavior.
