# supplier-quality-specialist

Review supplier evidence and draft corrective-action requests.

Status: `STRUCTURALLY_READY`; Runtime model behavior: `NOT_RUN`. This is a role composition, not an additional atomic skill or professional authorization.

## Select a workflow

| Workflow | Use when | Required evidence | Deliverable | Boundary |
|---|---|---|---|---|
| `supplier-review` | Review qualification and conformity documentation. | Supplier scope, qualification records, certificate and product requirements. | Supplier evidence gaps. | No supplier approval or certificate validation by assertion. |
| `supplier-action` | Analyze defects and draft a supplier corrective action. | Linked defect counts, nonconformance and supplier context. | Defect review and supplier-action draft. | Do not send the request or approve supplier changes. |

Read the [manifest](skillset.yaml) for workflow membership and the [composition contract](../composition-contract.json) for shared boundaries. The manifest uses JSON-compatible YAML for dependency-free parsing.

## Atomic entry points

- [review-supplier-qualification](../../skills/family-17-supplier-quality/review-supplier-qualification/SKILL.md).
- [review-certificate-of-conformance](../../skills/family-17-supplier-quality/review-certificate-of-conformance/SKILL.md).
- [analyze-supplier-defect](../../skills/family-17-supplier-quality/analyze-supplier-defect/SKILL.md).
- [draft-supplier-corrective-action](../../skills/family-17-supplier-quality/draft-supplier-corrective-action/SKILL.md).
- [review-supplier-change-impact](../../skills/family-17-supplier-quality/review-supplier-change-impact/SKILL.md).

## Evidence handoff

Select the user's workflow, inspect its atomic inputs and reuse compatible existing evidence before requesting new work. Preserve product/process, facility, period, units, source revision and uncertainty across steps. Do not treat the resolver's ordered list as an instruction to execute every skill or as proof that prerequisites passed.

Use the contract's jurisdiction, source, provincial or WHMIS routes when the requested conclusion needs them; explicitly select the route in the resolver. Automatic legal applicability is not implemented. Missing sector coverage remains a research handoff.

Return the requested deliverable, per-skill status, unsupported conclusions and review owners. A partial or blocked prerequisite blocks the dependent conclusion even if later skills appear in the manifest. Generic supported work may continue. No role title grants release, engineering, regulatory, operating or business-commitment authority.

## Resolve references

From the repository root:

```powershell
python scripts/resolve-skillset.py supplier-quality-specialist supplier-review
```

Add `--overlay provincial` or another named overlay only when that research is selected. The command emits paths and evidence dependencies; it does not run skills, call a model, install files or change live systems. [Acceptance evidence](../../tests/evaluations/AM-28-professional-skillsets-acceptance.md) separates structural verification from runtime behavior.
