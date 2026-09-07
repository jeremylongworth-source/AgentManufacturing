---
name: validate-bill-of-materials
description: Check bill-of-materials identity, quantities, units, and revisions without assessing design fitness or changing the BOM.
license: PENDING_PROJECT_GOVERNANCE
---

# Validate Bill of Materials

**Taxonomy metadata:** family `12` Materials, BOM & Traceability; tier `CORE`; safety class `ROUTINE`; jurisdiction `GENERIC_METHOD_ONLY`; priority `P1`; status `TAXONOMY_ACCEPTED_NOT_IMPLEMENTED`.

## Overview
Reconcile a BOM record to its product, revision, quantities, units, and effectivity evidence.

## Triggers
- Product identity, BOM revision, components, quantities, and source records are supplied.

## Non-Triggers
- Declaring design fitness, editing the BOM, or releasing a production revision.

## Required Inputs
- Product/revision, component identity, quantity, unit, effectivity, and source revision.

## Optional Inputs
- Alternates, scrap factors, engineering change, and plant applicability.

## Assumptions
- A consistent BOM can still be unfit for design or process use.

## Core Workflow
1. Reconcile identity, revision, quantities, units, and effectivity.
2. Flag duplicates, missing components, and conflicts.
3. Return evidence gaps and owner handoff.

## Calculations
Preserve supplied quantity arithmetic and units; do not infer scrap or yield factors.

## Validation
- Check revision, component identity, quantity, unit, effectivity, and source.

## Exception Handling
- Missing revision or component evidence returns `NEEDS_INPUT`.
- Change or release request returns `OUT_OF_SCOPE`.

## Source Usage
- Apply `references/bom-validation-checklist.md`.

## Output Contract
Return `status`, product/revision, component findings, conflicts, assumptions, and qualified handoff.

## Safety Requirements
AM-05 class: `ROUTINE`. Do not edit, approve, or release a BOM.

## References
- `references/bom-validation-checklist.md`

## Examples
A quantity-consistent BOM with stale effectivity remains unresolved.

## Testing
Cover correct invocation, mixed revisions, unit mismatch, expected output structure, and release refusal. Expected routing is not observed behavior.
