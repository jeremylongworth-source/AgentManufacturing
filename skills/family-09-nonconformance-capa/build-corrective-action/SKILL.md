---
name: build-corrective-action
description: Design a cause-linked corrective-action proposal with owner, verification, and residual-risk fields without approving implementation.
license: MIT
---

# Build Corrective Action

**Taxonomy metadata:** family `09` Nonconformance, RCA & CAPA; tier `CORE`; safety class `ROUTINE`; jurisdiction `GENERIC_METHOD_ONLY`; priority `P1`; status `TAXONOMY_ACCEPTED_NOT_IMPLEMENTED`.

## Overview
Translate a supported cause into a reviewable corrective-action proposal.

## Triggers
- Confirmed or qualified cause, problem scope, proposed action, owner, and due basis are supplied.

## Non-Triggers
- Approving action, changing a process, or closing a CAPA.

## Required Inputs
- Problem, cause evidence, action, owner, due date basis, and verification measure.

## Optional Inputs
- Resources, change-control reference, risk, and implementation dependencies.

## Assumptions
- An action without a cause link or verification plan is incomplete.

## Core Workflow
1. Link action to cause and affected scope.
2. Define owner, timing, verification, and residual risk.
3. Return approval questions and handoff.

## Calculations
Preserve supplied risk or effectiveness calculations; do not invent thresholds.

## Validation
- Check cause evidence, owner, due basis, verification, and change control.

## Exception Handling
- Missing cause or verification returns `NEEDS_INPUT`.
- Implementation or closure request returns `OUT_OF_SCOPE`.

## Source Usage
- Apply `references/corrective-action-checklist.md`.

## Output Contract
Return `status`, problem/cause link, action, owner, due basis, verification, residual risk, and approval handoff.

## Safety Requirements
AM-05 class: `ROUTINE`. Do not implement, approve, or close corrective action.

## References
- `references/corrective-action-checklist.md`

## Examples
A training action does not correct a process cause unless evidence links the cause to the training gap.

## Testing
Cover correct invocation, missing cause, absent verification, expected output structure, and implementation refusal. Expected routing is not observed behavior.
