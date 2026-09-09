# AM-31 final handoff: adversarial safety evaluation

Status: `READY`

Completion token: `AGENTMANUFACTURING_AM_31_SAFETY_VALIDATED`

Date: 2026-09-09

Completed eight roadmap adversarial cases and eight paired safe review requests as assisted, nonblind simulations. Responses preserve refusal of unsafe/deceptive implementation and useful evidence review. This closure covers that bounded evaluation; independent model robustness remains unproven.

## Evidence

- [Inputs](../../../tests/safety/am31-inputs.json), [rubric](../../../tests/safety/am31-rubric.json), [responses](../../../tests/safety/am31-responses.json) and [self-review](../../../tests/safety/am31-self-review.json).
- [Acceptance report and limitations](../../../tests/evaluations/AM-31-safety-acceptance.md).
- [Evidence validator](../../../scripts/validate-adversarial-safety.py), included in the repository gate.

Validation: 30 repository validators passed, including 16 AM-31 records, eight attack/control pairs, 64 self-review judgments and ten mutation rejections. The routing manifest contains 243 expected cases. Atomic skills remain unchanged. Hashes bind the self-review to exact responses and source versions; changed evidence requires review, not automatic digest regeneration. The Python checker does not execute or semantically evaluate a model.

## Next wave

AM-32 requires README.md, ROADMAP.md, AGENTS.md, CONTRIBUTING.md, SECURITY.md, CODE_OF_CONDUCT.md, CHANGELOG.md and LICENSE. Inspect existing documents and prior governance decisions first. Prepare concrete public-readiness documentation while preserving the unresolved licence and publication decisions; do not invent reporting contacts, maintainers, support commitments or release authority. The user has authorized ongoing commits and pushes, not an unrequested public release or repository-visibility change.

AM-33 must subsequently audit taxonomy, routing, arithmetic, Canadian sources, standards freshness, quality, safety and provincial isolation. Carry forward AM-30/31's nonblind self-review limitation: baseline, independent model execution, blind routing, repeated trials and multi-turn persistence remain unperformed. No completion marker is evidence of production safety, legal compliance or release approval.
