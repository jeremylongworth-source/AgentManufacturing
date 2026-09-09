---
name: analyze-material-variance
description: Explain planned-versus-actual material usage from reconciled events without assigning blame or changing standards.
license: MIT
---

# Analyze Material Variance

**Taxonomy metadata:** family `12` Materials, BOM & Traceability; tier `CORE`; safety class `ROUTINE`; jurisdiction `GENERIC_METHOD_ONLY`; priority `P1`; status `TAXONOMY_ACCEPTED_NOT_IMPLEMENTED`.

## Overview
Compare planned and actual usage after establishing a coherent event balance.

## Triggers
- Planned usage, actual issues/returns/scrap, units, period, and product population are supplied.

## Non-Triggers
- Changing standards, blaming operators, or authorizing material adjustment.

## Required Inputs
- Product/lot, plan basis, actual event states, units, and period.

## Optional Inputs
- Yield, scrap, rework, substitutions, and variance thresholds.

## Assumptions
- Variance interpretation follows reconciliation; raw issue quantity alone is insufficient.

## Core Workflow
1. Reconcile issues, returns, scrap, and work-in-process states.
2. Compare the result to declared plan basis.
3. Return drivers, gaps, and owner questions.

## Calculations
`variance = reconciled actual usage - planned usage`; preserve sign and units.

## Validation
- Check event completeness, units, population, period, and plan revision.

## Exception Handling
- Unbalanced events return `NEEDS_INPUT`.
- Standard or disposition change returns `OUT_OF_SCOPE`.

## Source Usage
- Apply `references/material-variance-checklist.md` and AM-08 rules.

## Output Contract
Return `status`, plan/actual basis, reconciliation, variance, drivers, assumptions, and handoff.

## Safety Requirements
AM-05 class: `ROUTINE`. Do not alter standards or authorize material disposition.

## References
- `references/material-variance-checklist.md`

## Examples
An issue transaction without returns or scrap cannot support a complete variance explanation.

## Testing
Cover correct invocation, unbalanced events, unit mismatch, expected output structure, and adjustment refusal. Expected routing is not observed behavior.
