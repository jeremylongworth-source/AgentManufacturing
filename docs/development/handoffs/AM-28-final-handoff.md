# AM-28 final handoff: professional skillsets

Status: `READY`

Completion token: `AGENTMANUFACTURING_AM_28_PROFESSIONAL_SKILLSETS_READY`

Date: 2026-09-08

AM-28 composes all 18 roles preserved in the initial framework into 38 workflows. Each role contains a manifest and guide referencing existing skills. Shared rules preserve evidence reuse, conditional jurisdiction/source research, atomic authority boundaries and unsupported sector coverage.

The resolver emits canonical skill paths and transitive evidence providers in dependency order. It does not execute skills, install packages, call a model, evaluate input evidence or infer legal applicability. Both historical duplicate reference directories remain unchanged. The atomic inventory is still 161 directories representing 159 accepted names.

## Evidence

- [Role index](../../../skillsets/index.json) and [composition contract](../../architecture/professional-skillset-contract.md).
- [Read-only resolver](../../../scripts/resolve-skillset.py) and [12 resolver tests](../../../tests/skillsets/test_resolver.py).
- [Acceptance record](../../../tests/evaluations/AM-28-professional-skillsets-acceptance.md) and [validator](../../../scripts/validate-professional-skillsets.py).
- [Routing manifest](../../../tests/expected-routing.yaml): 219 scenarios including 22 AM-28 cases.

## Validation and limits

Observed on 2026-09-08: all 27 repository validators and 12 resolver tests passed. Every workflow resolves with and without explicit research overlays. Further CLI and local-link checks are recorded in the acceptance evidence.

Expected routing is not observed behavior. Runtime model behavior remains `NOT_RUN`. Reference resolution does not establish prerequisite completion, input compatibility, source currency, legal applicability, skill execution or professional authority. No role authorizes release, certification, operations, live changes or business commitments.

## Next wave

AM-29 defines sector specialization architecture and priorities for the roadmap's 12 sector groups. Inspect D-05 in the domain contract to preserve the reconciliation of the longer original sector list. Define core/sector composition, source and version requirements, dependencies, acceptance criteria and explicit missing coverage. Do not implement every sector in this wave or assume named standards apply merely from the sector label.
