---
name: assess-product-containment
description: Assess proposed affected scope and containment evidence while reserving custody, release, and disposition decisions.
license: PENDING_PROJECT_GOVERNANCE
---

# Assess Product Containment

**Taxonomy metadata:** family `09` Nonconformance, RCA & CAPA; tier `CORE`; safety class `REGULATED`; jurisdiction `PENDING_CONTEXT` with `SECTOR_REGULATED`; priority `P1`; status `TAXONOMY_ACCEPTED_NOT_IMPLEMENTED`.

## Overview
Map suspected affected product, evidence boundaries, and containment gaps.

## Triggers
- A nonconformance, product genealogy, inventory scope, or containment proposal is supplied.

## Non-Triggers
- Physically segregating product, releasing product, or approving disposition.

## Required Inputs
- Issue identity, lot or genealogy scope, status locations, and containment evidence.

## Optional Inputs
- Shipment status, customer exposure, inspection results, and custody owner.

## Assumptions
- Missing genealogy leaves affected scope uncertain.

## Core Workflow
1. Map evidence to potentially affected units and locations.
2. Separate known, suspected, and excluded scope.
3. Return containment questions and authorized owner handoff.

## Calculations
Count only traceable units; do not estimate affected quantity from incomplete genealogy.

## Validation
- Check lot identity, time boundary, custody, genealogy, and status.

## Exception Handling
- Missing scope returns `NEEDS_INPUT`.
- Release or custody instruction returns `SAFETY_ESCALATION`.

## Source Usage
- Apply `references/product-containment-checklist.md` and AM-07 jurisdiction rules.

## Output Contract
Return `status`, issue, known/suspected scope, evidence map, gaps, proposed review owner, and boundary note.

## Safety Requirements
AM-05 class: `REGULATED`. Do not release, move, quarantine, or dispose of product.

## References
- `references/product-containment-checklist.md`

## Examples
Unknown genealogy is an unresolved scope boundary, not proof that unaffected units are safe.

## Testing
Cover correct invocation, missing genealogy, jurisdiction context, expected output structure, and release refusal. Expected routing is not observed behavior.
