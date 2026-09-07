# AM-10 final handoff — reference skill gate

## Wave

AM-10: Reference skills

## Objective

Prove one bounded AgentSkills package in each selected major class before family-scale authoring: quantitative performance, production planning, quality triage, hazardous-operation program review, and Canadian regulated overlay review.

## Verdict

**READY** for AM-10 package proof. Five reference packages, their host metadata and references, deterministic acceptance evidence, scenario routes, and the aggregate validation gate pass offline. Runtime model behavior remains `NOT_RUN`; this handoff does not authorize host installation, mass authoring, live production action, legal approval, certification, or release.

## Completion token

```text
AGENTMANUFACTURING_AM_10_REFERENCE_SKILLS_READY
```

## Scope completed

- Added `calculate-oee` under family 05 with AM-08 formula and fixture linkage, impossible-input rejection, unit preservation, and bounded output contract.
- Added `build-production-plan` under family 02 with capacity-limited allocation, explicit unmet demand, and no invented capacity or live order release.
- Added `triage-nonconformance` under family 09 with evidence-based priority, unknown-scope preservation, and quality-owner handoff.
- Added `review-lockout-program` under family 11 with document-level evidence-gap review and refusal of equipment-specific isolation, bypass, and restart instructions.
- Added `assess-made-in-canada-claim` under family 20 with current-source metadata, transformation/cost evidence checks, and no claim endorsement or publication.
- Added `reference-skill-proof-contract.json`, the AM-10 proof record, and `validate-reference-skills.py` for package structure, taxonomy traceability, adapter metadata, references, deterministic evidence, and runtime-evaluation boundary checks.
- Updated routing scenarios so implemented reference routes are distinct from the remaining future `calculate-takt-time` route; added production-planning and nonconformance scenarios.
- Updated the roadmap, README, and domain contract to record AM-10 closure and AM-11 as the next bounded wave.

## Files added

- `skills/family-05-performance/calculate-oee/`
- `skills/family-02-production-planning/build-production-plan/`
- `skills/family-09-quality/triage-nonconformance/`
- `skills/family-11-safety/review-lockout-program/`
- `skills/family-20-canadian-compliance/assess-made-in-canada-claim/`
- `docs/architecture/reference-skill-proof-contract.json`
- `docs/architecture/reference-skill-proof.md`
- `scripts/validate-reference-skills.py`
- `tests/scenarios/production-plan-capacity.md`
- `tests/scenarios/nonconformance-unknown-scope.md`
- `tests/evaluations/AM-10-reference-skill-acceptance.md`

## Files modified

- `tests/expected-routing.yaml` — implemented reference routes and remaining future route.
- `tests/scenarios/*.md` — route labels and AM-10 review boundary wording.
- `scripts/validate-validation-framework.py` — nested package route lookup, expanded scenario count, and post-AM-10 status handling.
- `scripts/validate-all.py` — nine-validator aggregate gate.
- `ROADMAP.md`, `README.md`, and `docs/architecture/domain-contract.md` — AM-10 closure and AM-11 pointer.

## Validation performed

```text
python scripts/validate-all.py
PASS: all 9 repository validators completed.
PASS: AM-10 reference packages; five taxonomy records, package contracts, references, and review evidence validated; runtime model behavior remains NOT_RUN.
```

The gate also passed the AM-00 through AM-09 validators, including 14 scenarios across all 11 required categories and all 17 AM-08 fixtures mapped exactly once.

## Known limitations

- No host or model was called, so route selection and output behavior are not observed evidence.
- The deterministic production, quality, safety, and regulated acceptance cases are declared in package contracts and review records; they are not a substitute for reviewer-owned runtime runs.
- `PENDING_PROJECT_GOVERNANCE` remains the package licence placeholder.
- Canadian and provincial source applicability, safety adequacy, engineering adequacy, and legal conclusions remain context-dependent and require qualified review.

## Recommended next wave

Proceed to AM-11: implement a small, reviewable manufacturing fundamentals and standard-work wave using the five AM-10 packages as composition and evidence examples. Keep package count bounded, add canonical scenarios and deterministic fixtures where applicable, and run the full nine-validator gate before closing the wave.
