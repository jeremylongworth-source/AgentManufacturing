---
name: review-capability-readiness
description: Review whether process data are ready for capability analysis while separating specification limits from control limits.
license: PENDING_PROJECT_GOVERNANCE
---

# Review Capability Readiness

**Taxonomy metadata:** family `08` SPC & Capability; tier `CORE`; safety class `ROUTINE`; jurisdiction `GENERIC_METHOD_ONLY`; priority `P1`; status `TAXONOMY_ACCEPTED_NOT_IMPLEMENTED`.

## Overview
Screen stability, distribution, measurement, and specification evidence before capability calculations.

## Triggers
- Specification limits, ordered process data, and measurement context are supplied.

## Non-Triggers
- Declaring capability, accepting product, or adjusting a process.

## Required Inputs
- Specification limits, data population, stability evidence, and measurement basis.

## Optional Inputs
- Distribution assessment, subgrouping, exclusions, and customer criterion.

## Assumptions
- Specification limits are acceptance criteria; control limits describe process behavior.

## Core Workflow
1. Reconcile characteristic, units, specs, and population.
2. Check stability and measurement adequacy.
3. Return readiness, gaps, and calculation handoff.

## Calculations
Do not substitute specification limits for control limits or capability inputs.

## Validation
- Check stable evidence, coherent population, and within/overall variation basis.

## Exception Handling
- Spec limits supplied as control limits returns `NEEDS_INPUT`.
- Acceptance request returns `OUT_OF_SCOPE`.

## Source Usage
- Apply `references/capability-readiness-checklist.md`.

## Output Contract
Return `status`, specs, stability evidence, measurement basis, readiness gaps, assumptions, and handoff.

## Safety Requirements
AM-05 class: `ROUTINE`. Do not authorize product acceptance.

## References
- `references/capability-readiness-checklist.md`

## Examples
Control limits cannot be reconstructed by relabeling specification limits.

## Testing
Cover correct invocation, spec/control confusion, missing stability, expected output structure, and acceptance refusal. Expected routing is not observed behavior.
