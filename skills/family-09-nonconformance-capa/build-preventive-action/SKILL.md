---
name: build-preventive-action
description: Propose controls for a prospective failure exposure while separating prevention from reactive corrective action.
license: MIT
---

# Build Preventive Action

**Taxonomy metadata:** family `09` Nonconformance, RCA & CAPA; tier `CORE`; safety class `ROUTINE`; jurisdiction `GENERIC_METHOD_ONLY`; priority `P2`; status `TAXONOMY_ACCEPTED_NOT_IMPLEMENTED`.

## Overview
Structure a prospective prevention proposal from a defined risk or weak signal.

## Triggers
- Prospective failure mode, exposure, proposed control, owner, and verification basis are supplied.

## Non-Triggers
- Recasting prevention as a root cause, implementing controls, or closing CAPA.

## Required Inputs
- Failure exposure, affected process, proposed control, owner, and verification.

## Optional Inputs
- Risk ranking, control plan link, due basis, and residual exposure.

## Assumptions
- A prospective control does not prove a past cause was corrected.

## Core Workflow
1. Define exposure and prevention objective.
2. Map control, owner, verification, and residual exposure.
3. Return review and change-control handoff.

## Calculations
Use only a declared risk scale and preserve its definitions.

## Validation
- Check exposure, control mechanism, owner, verification, and residual risk.

## Exception Handling
- Missing exposure or verification returns `NEEDS_INPUT`.
- Implementation request returns `OUT_OF_SCOPE`.

## Source Usage
- Apply `references/preventive-action-checklist.md`.

## Output Contract
Return `status`, exposure, proposed control, owner, verification, residual risk, and handoff.

## Safety Requirements
AM-05 class: `ROUTINE`. Do not implement or approve a preventive control.

## References
- `references/preventive-action-checklist.md`

## Examples
A prospective poka-yoke proposal is prevention evidence, not proof of a prior root cause.

## Testing
Cover correct invocation, missing exposure, residual-risk gap, expected output structure, and implementation refusal. Expected routing is not observed behavior.
