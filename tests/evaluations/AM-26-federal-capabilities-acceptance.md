# AM-26 federal capabilities acceptance

Status: `READY_FOR_REVIEW`

Evidence date: 2026-09-08

Audience: package reviewers and AM-27 implementers. Seven new packages plus the refreshed Made in Canada reference cover eight Family 20 federal capabilities. These criteria specify expected responses; Runtime model behavior remains `NOT_RUN`.

| Skill | Scenario evidence | Required response | Runtime model behavior |
|---|---|---|---|
| `identify-manufacturing-jurisdiction` | [AM26-S01](../scenarios/manufacturing-jurisdiction-product-workplace.md) | Keep product and workplace regimes separate. Preserve location and product evidence while leaving workplace regime pending undertaking evidence. | `NOT_RUN` |
| `identify-applicable-regulatory-layer` | [AM26-S02](../scenarios/regulatory-layer-employer-unknown.md) | Request employer activity and workplace regime evidence. Return candidate research paths without establishing Alberta or federal applicability. | `NOT_RUN` |
| `assess-whmis-applicability` | [AM26-S03](../scenarios/whmis-importer-employer-roles.md) | Separate importer/supplier scope from employer duties. Request workplace regime and product/activity evidence without declaring applicability verified. | `NOT_RUN` |
| `review-whmis-readiness` | [AM26-S04](../scenarios/whmis-readiness-scope-pending.md) | Return a bounded evidence inventory and preserve unresolved applicability. Do not equate supplied records with compliance or safe use. | `NOT_RUN` |
| `review-whmis-readiness` | [AM26-S05](../scenarios/whmis-readiness-identifier-mismatch.md) | Flag product/SDS/label identity mismatch and ask for reconciliation. Do not infer task competence from attendance or approve chemical use. | `NOT_RUN` |
| `assess-made-in-canada-claim` | [AM26-S06](../scenarios/made-canada-costs-incomplete.md) | Identify incomplete cost denominator and transformation evidence. Withhold a percentage conclusion and claim endorsement. | `NOT_RUN` |
| `assess-product-of-canada-claim` | [AM26-S07](../scenarios/product-canada-wrong-claim-basis.md) | Keep the prior assessment as evidence only. Request claim-specific costs and transformation evidence; do not substitute Made in Canada criteria or approve wording. | `NOT_RUN` |
| `review-nonfood-labelling-readiness` | [AM26-S08](../scenarios/nonfood-label-sector-scope.md) | Preserve unresolved product class and route specialized source review. Do not apply a universal checklist or approve printing. | `NOT_RUN` |
| `verify-regulatory-source-freshness` | [AM26-S09](../scenarios/source-reachable-superseded.md) | Report the supplied citation as SUPERSEDED and request applicable current version/effectivity evidence. Do not confuse successful access with source freshness or applicability. | `NOT_RUN` |
| `verify-regulatory-source-freshness` | [AM26-S10](../scenarios/source-consolidation-date-gap.md) | Return claim scope, as-of date, displayed currency, access result, source status and review owner. Preserve the unverified interval; do not infer either current law through September or repeal. | `NOT_RUN` |
| `verify-regulatory-source-freshness` | [AM26-S11](../scenarios/source-official-version-conflict.md) | Preserve both records and mark the conflict for review. Do not prefer the more recent download without effective-version evidence. | `NOT_RUN` |
| No federal route | [AM26-S12](../scenarios/federal-skills-logistics-nontrigger.md) | Do not invoke Canadian compliance skills for unrelated delivery optimization. Keep the logistics handoff outside this manufacturing compliance wave. | `NOT_RUN` |
| `assess-whmis-applicability`, `verify-regulatory-source-freshness` | [AM26-S13](../scenarios/whmis-transition-ended.md) | Check official amendment and transition evidence for the activity date. Do not extend an old transition or treat enforcement commentary as an exemption. | `NOT_RUN` |
| `assess-product-of-canada-claim` | [AM26-S14](../scenarios/origin-cost-near-threshold.md) | Show 97.99 percent, without rounding it up to 98 percent. Retain missing transformation substantiation and withhold approval regardless of the arithmetic. | `NOT_RUN` |
| `review-nonfood-labelling-readiness` | [AM26-S15](../scenarios/nonfood-label-complete-review-shape.md) | Map identity, quantity, dealer, language and layout evidence to scoped criteria. Return the missing quantity evidence and review handoff without packaging release. | `NOT_RUN` |

## Validation evidence

Observed on 2026-09-08: all 25 repository validators and all eight AgentSkills package checks passed. Local links in the Family 20 packages and new evidence documents resolved. The [AM-26 validator](../../scripts/validate-canadian-federal.py) checks taxonomy metadata, adapters, linked references, evidence providers, source records, and scenario coverage. The [full gate](../../scripts/validate-all.py) includes all prior wave checks. AgentSkills package checks cover naming and frontmatter. No new eligibility calculator is introduced; the 97.99% origin example is a reviewer arithmetic oracle, not an automated legal decision.

## Source scope

[Nine source records](../../docs/architecture/am26-federal-source-records.json) and [retrieval evidence](../../docs/development/AM-26-source-evidence.md) preserve current-on-access guidance and legislative metadata with a currency gap. The four legal records remain `PENDING_REVIEW` for the current activity date. Structural validation does not verify current law.

## Residual risk

Model adherence, source completeness, site applicability, SDS accuracy, hazard classification, transformation, cost provenance and label legality remain unverified. The packages cannot approve claims, chemical use, printing or compliance. Provincial/territorial safety content is deferred to AM-27. Existing duplicate AM-10 reference paths remain preserved; there are 160 package directories representing 158 unique accepted names after AM-26.

## Runtime evaluation handoff

A reviewer must run the scenarios with the package version, model settings, supplied evidence and tool availability recorded, score each acceptance check against the actual response, and retain failures before any behavioral readiness claim. Expected routing is not observed behavior.
