---
name: calculate-material-requirement
description: Expand product quantities into gross component requirements from a declared BOM and lot basis without planning replenishment.
license: PENDING_PROJECT_GOVERNANCE
---

# Calculate Material Requirement

**Taxonomy metadata:** family `12` Materials, BOM & Traceability; tier `CORE`; safety class `ROUTINE`; jurisdiction `GENERIC_METHOD_ONLY`; priority `P1`; status `TAXONOMY_ACCEPTED_NOT_IMPLEMENTED`.

## Overview
Calculate component need for a declared product quantity and BOM revision.

## Triggers
- Product quantity, BOM, revision, component quantities, and unit basis are supplied.

## Non-Triggers
- Netting inventory, replenishing warehouse stock, or releasing a purchase/order.

## Required Inputs
- Product quantity, BOM revision, component quantity per unit, units, and yield/scrap basis if applicable.

## Optional Inputs
- Order mix, alternates, rounding, and lot-size constraints.

## Assumptions
- Gross component need is distinct from net requirement and warehouse availability.

## Core Workflow
1. Validate one product/BOM population and units.
2. Expand component quantities with visible intermediates.
3. Return gross need, assumptions, and planning handoff.

## Calculations
`gross component need = product quantity × component quantity per product unit`; apply only supplied factors.

## Validation
- Check BOM revision, units, zero/negative quantities, factors, and rounding.

## Exception Handling
- Missing BOM or units returns `NEEDS_INPUT`.
- Replenishment or purchase request returns `OUT_OF_SCOPE`.

## Source Usage
- Apply `references/material-requirement-checklist.md` and AM-08 rules.

## Output Contract
Return `status`, inputs, formula, intermediates, gross requirements, assumptions, and handoff.

## Safety Requirements
AM-05 class: `ROUTINE`. Do not plan warehouse movement, replenishment, or purchasing.

## References
- `references/material-requirement-checklist.md`

## Examples
Gross need remains separate from available inventory and warehouse replenishment.

## Testing
Cover correct invocation, mixed units, zero quantity, expected output structure, and replenishment refusal. Expected routing is not observed behavior.
