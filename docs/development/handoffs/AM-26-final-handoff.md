# AM-26 final handoff: Canadian federal capabilities

Status: `READY`

Completion token: `AGENTMANUFACTURING_AM_26_CANADA_FEDERAL_READY`

Date: 2026-09-08

AM-26 adds seven packages for jurisdiction context, regulatory layers, WHMIS applicability and readiness, Product of Canada claims, non-food consumer labelling, and source freshness. It refreshes the existing Made in Canada reference. Family 20 now has eight implemented capabilities; its provincial safety selector remains AM-27 work.

The repository contains 160 package directories and 158 unique accepted skill names. The difference is two preserved AM-10 reference paths for nonconformance and lockout review. The frozen catalogue remains 159 records; no taxonomy expansion was made.

## Evidence

- [Family 20 packages](../../../skills/family-20-canadian-compliance/).
- [Acceptance record](../../../tests/evaluations/AM-26-federal-capabilities-acceptance.md).
- [AM-26 validator](../../../scripts/validate-canadian-federal.py) and [complete gate](../../../scripts/validate-all.py).
- [Source evidence](../AM-26-source-evidence.md) and [source records](../../architecture/am26-federal-source-records.json).
- [Routing manifest](../../../tests/expected-routing.yaml): 184 scenarios, including 15 AM-26 cases and an AM-27 provincial coverage case.

## Validation and limits

Observed on 2026-09-08: all 25 repository validators and all eight AgentSkills package checks passed. Local links in the Family 20 packages and new evidence documents resolved. Run `python scripts/validate-all.py` for the complete gate and AgentSkills quick_validate.py for the eight Family 20 packages.

Expected routing is not observed behavior. Runtime model evaluation remains `NOT_RUN`. The legal landing pages displayed currency to 2026-06-21 when accessed on 2026-09-08; their records remain `PENDING_REVIEW` for current-date legal claims. Guidance observations and source checks do not establish applicability.

Residual risk: these packages provide research and evidence-gap reviews, not legal opinions, compliance certification, WHMIS classification, safe-use approval, origin-claim endorsement, or packaging release. A reachable URL does not establish freshness; a supplier rule does not establish workplace jurisdiction; Made in Canada evidence cannot automatically substantiate Product of Canada wording.

## Next wave

AM-27 builds initial source-bounded Ontario, British Columbia, Alberta and Quebec overlays, including the frozen identify-provincial-safety-overlay capability. Inspect the existing Canadian jurisdiction model and source registry before adding modules. Research OH&S, machinery, hazardous energy, electrical, pressure equipment, environmental and training authority paths for each supported jurisdiction. Keep employer-regime evidence, source versions, unsupported jurisdictions and qualified-review needs explicit. Do not treat provinces as interchangeable or infer territory coverage.
