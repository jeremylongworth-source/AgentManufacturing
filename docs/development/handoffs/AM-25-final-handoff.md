# AM-25 final handoff: environment, energy and waste

Status: `READY`

Completion token: `AGENTMANUFACTURING_AM_25_ENVIRONMENTAL_READY`

Date: 2026-09-08

AM-25 adds six Family 19 packages: environmental-aspect inventory, risk-register drafting, energy-consumption analysis, waste-stream review, reduction planning, and objective measurability review. The repository now contains 153 packages.

The energy package includes a read-only helper with explicit interval-consumption, period, unit, and allocation checks. Twenty deterministic cases cover valid conversions and intensities, invalid inputs, and comparison boundaries. Other packages retain qualitative evidence and defined review responsibilities; they introduce no default risk score.

## Evidence

- [Family 19 packages](../../../skills/family-19-environment-energy-waste/).
- [Acceptance record](../../../tests/evaluations/AM-25-environment-energy-waste-acceptance.md).
- [AM-25 validator](../../../scripts/validate-environment-energy-waste.py) and [energy fixtures](../../../tests/fixtures/am25-energy-intensity.json).
- [Source evidence](../AM-25-source-evidence.md) and [AM-07-compatible source records](../../architecture/am25-environment-source-records.json).
- [Routing manifest](../../../tests/expected-routing.yaml): 169 scenarios, including eight AM-25 scenarios and a future Family 20 jurisdiction route.

## Validation and limits

Observed on 2026-09-08: all 24 repository validators, all six AgentSkills package checks, and all 20 new energy fixtures passed. The stdin CLI returned 3.0000 kWh/part for 1200 kWh and 400 parts. New local evidence links resolved and `git diff --check` passed.

Run `python scripts/validate-all.py` for the 24-validator repository gate, and AgentSkills `quick_validate.py` for each new package. The focused command is `python scripts/validate-environment-energy-waste.py`.

Expected routing is not observed behavior. Runtime model evaluation remains `NOT_RUN`. Calculator fixtures test Python behavior; source validation tests stored record structure. Official source access verifies the bounded claims in the source record, not site applicability or protected standard clauses.

Residual risk: the packages do not establish legal waste classification, disposal permission, certification, chemical-handling safety, or causal energy improvement. Raw meter coverage, stream characterization, applicable obligations, and supplied criteria require responsible review.

## Next wave

AM-26 builds the Family 20 federal capabilities: WHMIS, origin claims, general non-food labelling, jurisdiction routing, and source freshness. The origin-claim reference skill already exists; inspect accepted taxonomy and package inventory before adding or updating records. AM-27 separately owns initial provincial overlays.
