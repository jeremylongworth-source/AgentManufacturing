# AM-14 final handoff — quality management and inspection

## Wave

AM-14: Quality management and inspection

## Objective

Build Family 06 with bounded quality-requirement, inspection, conformity, record-integrity, release-evidence, audit, and KPI packages using the existing package and evidence contracts.

## Verdict

**READY** for AM-14. Seven Family 06 packages, adapters, references, acceptance evidence, routing scenarios, and the aggregate validation gate pass offline. Runtime model behavior remains `NOT_RUN`; this handoff does not authorize inspection execution, sampling selection, product release, deviation closure, certification, legal compliance, or supplier action.

## Completion token

```text
AGENTMANUFACTURING_AM_14_QUALITY_MANAGEMENT_READY
```

## Scope completed

- Added `review-quality-requirement`, `build-inspection-plan`, `review-product-conformity`, `review-quality-record`, `prepare-quality-release-package`, `audit-quality-process`, and `analyze-quality-kpis`.
- Added canonical scenarios for conflicting requirements, missing sampling basis, supplier/measured evidence conflict, overwritten records, open release deviations, narrow audit samples, and unequal supplier exposure.
- Added `validate-quality-management.py` and the AM-14 acceptance record; the aggregate gate now runs thirteen validators.
- Moved `review-quality-requirement` from future to implemented routing and reserved `select-measurement-method` as the explicit future AM-15 route.
- Updated the roadmap, README, domain contract, route manifest, and AM-15 pointer.

## Files added

- `skills/family-06-quality-management/`
- `scripts/validate-quality-management.py`
- `tests/evaluations/AM-14-quality-management-acceptance.md`
- `tests/scenarios/quality-requirement-conflict.md`
- `tests/scenarios/inspection-plan-no-sample-basis.md`
- `tests/scenarios/conformity-supplier-conflict.md`
- `tests/scenarios/quality-record-overwritten.md`
- `tests/scenarios/release-package-open-deviation.md`
- `tests/scenarios/quality-audit-narrow-sample.md`
- `tests/scenarios/quality-kpi-unequal-exposure.md`
- `tests/scenarios/future-measurement-method.md`

## Files modified

- `tests/expected-routing.yaml` — seven AM-14 implemented routes and one explicit future AM-15 route.
- `tests/scenarios/future-quality-requirement.md` — moved to implemented coverage.
- `scripts/validate-validation-framework.py` — future-route target advanced to `select-measurement-method`.
- `scripts/validate-all.py` — thirteen-validator aggregate gate.
- `ROADMAP.md`, `README.md`, and `docs/architecture/domain-contract.md` — AM-14 closure and AM-15 pointer.

## Validation performed

```text
python scripts/validate-all.py
PASS: all 13 repository validators completed.
```

The local AgentSkills quick validator also passes for all seven Family 06 packages. The route suite now contains 58 scenarios across all required categories; AM-08 fixture mapping remains complete.

## Known limitations

- No host or model was called, so route selection and output behavior are not observed evidence.
- Regulated quality conclusions depend on current requirements, sampling authority, measurement methods, record integrity, sector context, and authorized disposition.
- The packages do not execute inspection, release product, close deviations, certify a QMS, or select measurement methods.
- `PENDING_PROJECT_GOVERNANCE` remains the package licence placeholder.

## Recommended next wave

Proceed to AM-15: build Families 07 and 08 for metrology, SPC, and capability, starting with the future `select-measurement-method` route and preserving the distinction between specification limits, control limits, precision, accuracy, stability, and capability.
