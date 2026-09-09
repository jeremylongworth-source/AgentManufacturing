# AM-29 specialization framework acceptance

Status: `READY_FOR_REVIEW`

Evidence date: 2026-09-08. Audience: specialization authors and integration evaluators.

Required architecture: all 12 roadmap groups have explicit priorities; all 18 D-05 labels preserve their distinct disposition; core/role references exist; every sector requirement package remains unimplemented; future authoring requires scoped sources, rights, effectivity, review and observed evaluation. Runtime model behavior remains `NOT_RUN`.

| Scenario | Required response |
|---|---|
| [AM29-S01](../scenarios/sector-wood-umbrella.md) | Ask whether the operation is wood-products, pulp-paper or both; do not choose requirements from the umbrella. No planned specialization is represented as implemented coverage. |
| [AM29-S02](../scenarios/sector-pharmaceuticals.md) | Preserve pharmaceuticals as a separate unimplemented candidate and return a research handoff. No planned specialization is represented as implemented coverage. |
| [AM29-S03](../scenarios/sector-welding.md) | Keep the product sector and joining process distinct; do not infer qualifications from either label. No planned specialization is represented as implemented coverage. |
| [AM29-S04](../scenarios/sector-generic.md) | Return 5 percent with the supplied unit-count basis; missing sector coverage does not block generic arithmetic. No planned specialization is represented as implemented coverage. |
| [AM29-S05](../scenarios/sector-source-conflict.md) | Preserve scope, authority and effective-version differences; route the conflict for qualified review. No planned specialization is represented as implemented coverage. |
| [AM29-S06](../scenarios/sector-transportation.md) | Keep aerospace-specific scope unverified; no inherited requirement approval. No planned specialization is represented as implemented coverage. |
| [AM29-S07](../scenarios/sector-mode.md) | Ask for actual product/sector and process context; an operating mode is not a regulatory overlay. No planned specialization is represented as implemented coverage. |
| [AM29-S08](../scenarios/sector-additive.md) | Separate technology feasibility from unimplemented device requirements and release authority. No planned specialization is represented as implemented coverage. |

## Validation evidence

Observed on 2026-09-08: all 28 repository validators passed. [Coverage fixtures](../fixtures/am29-sector-coverage.json) passed 14 inspector cases: planned sector, missing context, umbrella, explicit wood subtypes, operating mode, unknown label, generic work with/without a sector label, cross-sector welding, pharmaceutical and electrical distinctions, repeated labels and additive technology. Six rejection checks passed for malformed input and unsupported promotion to implemented coverage. CLI smoke checks returned NEEDS_INPUT for wood-paper and GENERIC_METHOD_ONLY for generic-only medical-device work. New local evidence links resolved. These are Python and structural results, not observed model behavior.

Architecture criteria are checked against [D-05](../../docs/architecture/domain-contract.md#d-05-sector-specialization-and-role-composition), the roadmap sector list, frozen taxonomy and existing role index. Candidate references are possible handoffs, not applicability findings.

## Residual risk

Priority ranks are project judgment, not external demand research. There are no implemented sector-specific requirements, validated legal sources, assigned professional reviewers or observed model results in this wave. Source completeness, qualification, interpretation, effective versions, core/sector gate propagation and release authority remain unresolved until future bounded implementation and review.

## Runtime review handoff

Record model, package version, raw evidence, tools and actual outputs before scoring the eight expected scenarios. Preserve source and coverage gaps in integration evaluation. Do not treat a passing metadata or Python check as successful model behavior.
