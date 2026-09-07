---
name: identify-line-side-shortage
description: Compare production need and timing with usable line-side supply while stopping before warehouse movement or replenishment decisions.
license: PENDING_PROJECT_GOVERNANCE
---

# Identify Line-Side Shortage

**Taxonomy metadata:** family `12` Materials, BOM & Traceability; tier `CORE`; safety class `ROUTINE`; jurisdiction `GENERIC_METHOD_ONLY`; priority `P1`; status `TAXONOMY_ACCEPTED_NOT_IMPLEMENTED`.

## Overview
Screen a line-side shortage claim against production need, timing, and usable supply evidence.

## Triggers
- Production order, required component, timing, line-side quantity, and usability status are supplied.

## Non-Triggers
- Moving material, replenishing stock, expediting, or changing production schedule.

## Required Inputs
- Order/operation, component, required quantity/time, usable supply, and unit basis.

## Optional Inputs
- Holds, substitutes, scrap, replenishment lead time, and warehouse status.

## Assumptions
- A shortage signal is not a warehouse instruction.

## Core Workflow
1. Reconcile need timing and usable line-side supply.
2. Flag holds, unit gaps, and unknown availability.
3. Return production and materials-owner handoff.

## Calculations
`shortfall = required usable quantity - usable line-side quantity`; preserve units and timing.

## Validation
- Check order, component, units, timing, usability, and status evidence.

## Exception Handling
- Missing usable quantity returns `NEEDS_INPUT`.
- Movement or replenishment request returns `OUT_OF_SCOPE`.

## Source Usage
- Apply `references/line-side-shortage-checklist.md` and AM-08 rules.

## Output Contract
Return `status`, need, usable supply, shortfall, holds, assumptions, and owner handoff.

## Safety Requirements
AM-05 class: `ROUTINE`. Stop at the manufacturing/warehouse interface; do not direct movement or replenishment.

## References
- `references/line-side-shortage-checklist.md`

## Examples
Held material is not usable supply until its status is resolved by the owner.

## Testing
Cover correct invocation, missing status, unit mismatch, expected output structure, and warehouse-action refusal. Expected routing is not observed behavior.
