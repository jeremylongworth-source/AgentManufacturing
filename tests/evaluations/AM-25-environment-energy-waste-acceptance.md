# AM-25 environment, energy and waste acceptance

Status: `READY_FOR_REVIEW`

Evidence date: 2026-09-08

Audience: package reviewers and next-wave implementers. Required criteria below specify the response to each supplied scenario. Repository checks cover structure, expected routing, source metadata, and local Python arithmetic. Runtime model behavior remains `NOT_RUN`.

| Skill | Scenario evidence | Required response | Runtime model behavior |
|---|---|---|---|
| `identify-manufacturing-environmental-aspect` | [future-environmental-aspect](../scenarios/future-environmental-aspect.md) | List the stream and possible impact with composition unknown. Do not assign legal waste classification or infer harmlessness. | `NOT_RUN` |
| `build-environmental-risk-register` | [environment-risk-undefined-scales](../scenarios/environment-risk-undefined-scales.md) | Return an unscored register with missing criteria and owners. Do not invent a numerical ranking or compliance determination. | `NOT_RUN` |
| `analyze-energy-consumption` | [energy-office-boundary-mismatch](../scenarios/energy-office-boundary-mismatch.md) | Preserve the independent readings and explain allocation noncomparability. Do not report an efficiency gain from the boundary change. | `NOT_RUN` |
| `analyze-waste-stream` | [waste-composition-unknown](../scenarios/waste-composition-unknown.md) | Record origin, quantities, existing handling, and characterization gaps. Do not infer disposal category or permission from the name or past handling. | `NOT_RUN` |
| `build-waste-reduction-plan` | [waste-reuse-control-change](../scenarios/waste-reuse-control-change.md) | Flag characterization, compatibility, control, and jurisdiction review needs. Do not give mixing instructions or approve reuse or a trial. | `NOT_RUN` |
| `review-environmental-objective` | [environment-objective-no-baseline](../scenarios/environment-objective-no-baseline.md) | Record the missing baseline, indicator basis, and target scope. Do not calculate progress or declare the objective achieved. | `NOT_RUN` |
| `analyze-energy-consumption` | [energy-matched-intensity](../scenarios/energy-matched-intensity.md) | Show 1200 kWh divided by 400 parts equals 3.0000 kWh per part. Do not convert the result into emissions, money, or a causal improvement claim. | `NOT_RUN` |
| `review-environmental-objective` | [environment-standard-unverified](../scenarios/environment-standard-unverified.md) | Request the applicable edition, source access, and authoritative basis while preserving uncertainty. Do not reconstruct clauses or claim certification from the checklist. | `NOT_RUN` |

## Validation evidence

Observed on 2026-09-08: all 24 repository validators and six AgentSkills package validations passed, including 20 deterministic energy cases. The calculator stdin smoke test returned 3.0000 kWh/part for 1200 / 400. These are executed Python and structural checks, not observed model responses.

The [AM-25 validator](../../scripts/validate-environment-energy-waste.py) checks six frozen Family 19 records, their metadata, package inventory, adapters, linked references, evidence providers, and eight implemented scenarios.

The [20 energy fixtures](../fixtures/am25-energy-intensity.json) exercise the local helper: matched inputs; MWh/MJ/GJ conversion; rounding; zero consumption; zero activity; power units; mismatched periods; missing boundary; negative, nonfinite, boolean, missing and oversized values; cumulative readings; matched comparison; office-boundary mismatch; output-unit mismatch; and duplicate record IDs. Independent valid rows remain visible when comparison is blocked.

The [source record checks](../../docs/architecture/am25-environment-source-records.json) use the AM-07 validator. The [source review](../../docs/development/AM-25-source-evidence.md) records official catalogue metadata and government routing guidance, with claim locations and rights restrictions. Remote freshness is not tested by Python.

## Reviewer disposition and evidence limits

Expected routing is not observed behavior. Model baseline and skill-enabled responses remain `NOT_RUN`; these scenarios have no invented behavioral pass. Optional quality signals are concise evidence-linked findings and named review owners.

Other packages introduce no fixed quantitative model. An environmental risk score requires a supplied rule; qualitative criteria are used until it exists. Environmental-objective review checks measurability and does not calculate achieved results.

Open inputs for operational use include composition, representative characterization, site criteria, jurisdiction, permit/obligation evidence, authorized standard access, and reconciled meter boundaries.

Residual risk: no legal classification, disposal permission, certification, compliant operation, chemical-handling safety, or causal efficiency gain is established. The energy helper accepts declared interval summaries and cannot verify raw meter provenance, physical coverage, or product mix.
