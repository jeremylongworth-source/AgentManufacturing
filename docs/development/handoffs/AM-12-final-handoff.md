# AM-12 final handoff — production planning and scheduling

## Wave

AM-12: Production planning and scheduling

## Objective

Complete Family 02 using the AM-10 `build-production-plan` reference and bounded packages for requirements, sequencing, adherence, capacity, changeover, scenario comparison, lead time, order readiness, and lot-size comparison.

## Verdict

**READY** for AM-12. Ten Family 02 packages, adapters, references, acceptance evidence, routing scenarios, and the aggregate validation gate pass offline. Runtime model behavior remains `NOT_RUN`; this handoff does not authorize ERP/MES writes, order release, dispatch, delivery promises, overtime, procurement, or autonomous plan selection.

## Completion token

```text
AGENTMANUFACTURING_AM_12_PRODUCTION_PLANNING_READY
```

## Scope completed

- Kept the AM-10 `build-production-plan` reference as the family-level planning anchor.
- Added `calculate-production-requirement`, `sequence-production-orders`, `analyze-schedule-adherence`, `identify-capacity-shortfall`, `plan-production-changeover`, `compare-production-scenarios`, `calculate-production-lead-time`, `review-production-order-readiness`, and `compare-production-lot-sizes`.
- Added one canonical scenario for each new package covering held inventory, shared-resource conflicts, frozen-baseline adherence, time-basis mismatch, changeover conflicts, incomparable overtime assumptions, overlap arithmetic, missing order approval, and capacity-violating lot sizes.
- Added `validate-production-planning.py` and the AM-12 acceptance record; the aggregate gate now runs eleven validators.
- Updated the roadmap, README, domain contract, route manifest, and AM-13 pointer.

## Files added

- `skills/family-02-production-planning/calculate-production-requirement/`
- `skills/family-02-production-planning/sequence-production-orders/`
- `skills/family-02-production-planning/analyze-schedule-adherence/`
- `skills/family-02-production-planning/identify-capacity-shortfall/`
- `skills/family-02-production-planning/plan-production-changeover/`
- `skills/family-02-production-planning/compare-production-scenarios/`
- `skills/family-02-production-planning/calculate-production-lead-time/`
- `skills/family-02-production-planning/review-production-order-readiness/`
- `skills/family-02-production-planning/compare-production-lot-sizes/`
- `scripts/validate-production-planning.py`
- `tests/evaluations/AM-12-production-planning-acceptance.md`
- `tests/scenarios/production-requirement-held-inventory.md`
- `tests/scenarios/sequence-orders-conflict.md`
- `tests/scenarios/schedule-adherence-frozen-baseline.md`
- `tests/scenarios/capacity-shortfall-units.md`
- `tests/scenarios/changeover-window-conflict.md`
- `tests/scenarios/compare-scenarios-overtime.md`
- `tests/scenarios/lead-time-overlap.md`
- `tests/scenarios/production-order-readiness.md`
- `tests/scenarios/lot-size-capacity-violation.md`

## Files modified

- `tests/expected-routing.yaml` — nine AM-12 implemented routes.
- `scripts/validate-all.py` — eleven-validator aggregate gate.
- `ROADMAP.md`, `README.md`, and `docs/architecture/domain-contract.md` — AM-12 closure and AM-13 pointer.

## Validation performed

```text
python scripts/validate-all.py
PASS: all 11 repository validators completed.
PASS: AM-12 production planning; ten Family 02 packages, taxonomy traces, adapters, references, and acceptance evidence validated; runtime model behavior remains NOT_RUN.
```

The gate also passed AM-00 through AM-11, including 32 routed scenarios across all required categories and the complete AM-08 fixture map.

## Known limitations

- No host or model was called, so route selection and output behavior are not observed evidence.
- Planning results depend on supplied calendars, inventory, capacity, cost, priorities, baseline versions, and approval records.
- Live system integration, customer promises, order release, procurement, overtime, and autonomous scheduling remain out of scope.
- `PENDING_PROJECT_GOVERNANCE` remains the package licence placeholder.

## Recommended next wave

Proceed to AM-13: build Families 04 and 05 for process and industrial engineering, reusing the package contracts while adding engineering-review boundaries and quantitative process evidence where applicable.
