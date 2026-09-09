---
name: build-product-genealogy
description: Build input/output lot relationships from supplied records while stopping before warehouse movement and product disposition.
license: MIT
---

# Build Product Genealogy

**Taxonomy metadata:** family `12` Materials, BOM & Traceability; tier `CORE`; safety class `ROUTINE`; jurisdiction `GENERIC_METHOD_ONLY`; priority `P1`; status `TAXONOMY_ACCEPTED_NOT_IMPLEMENTED`.

## Overview
Assemble a traceable graph of lot, process, and product relationships.

## Triggers
- Input/output lot records, process events, product identity, and relationship keys are supplied.

## Non-Triggers
- Querying a specific exposure, moving product, or approving genealogy completeness for release.

## Required Inputs
- Lot IDs, process/event IDs, input-output relationships, dates, and source records.

## Optional Inputs
- Rework, scrap, substitutions, shipments, and confidence flags.

## Assumptions
- A graph is only as complete as its supplied relationship records.

## Core Workflow
1. Normalize identities and relationship direction.
2. Link input, process, output, and exception events.
3. Mark breaks, duplicates, and warehouse-interface boundaries.

## Calculations
No calculation; relationship counts preserve direction and source scope.

## Validation
- Check unique IDs, dates, direction, duplicates, and source completeness.

## Exception Handling
- Missing relationship keys return `NEEDS_INPUT`.
- Warehouse movement or disposition request returns `OUT_OF_SCOPE`.

## Source Usage
- Apply `references/product-genealogy-checklist.md`.

## Output Contract
Return `status`, nodes, relationships, breaks, source scope, assumptions, and handoff.

## Safety Requirements
AM-05 class: `ROUTINE`. Stop at the manufacturing/warehouse interface; do not direct movement or disposition.

## References
- `references/product-genealogy-checklist.md`

## Examples
A warehouse transaction can be linked as an external boundary without directing the movement.

## Testing
Cover correct invocation, duplicate IDs, direction mismatch, expected output structure, and warehouse-interface refusal. Expected routing is not observed behavior.
