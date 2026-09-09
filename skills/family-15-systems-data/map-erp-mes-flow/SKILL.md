---
name: map-erp-mes-flow
description: Map ERP and MES order and master-data handoffs from supplied evidence without changing live records or interfaces.
license: MIT
---

# Map ERP MES Flow

**Taxonomy metadata:** family `15` Manufacturing Systems & Data; tier `CORE`; safety class `ROUTINE`; jurisdiction `GENERIC_METHOD_ONLY`; priority `P1`; status `TAXONOMY_ACCEPTED_NOT_IMPLEMENTED`.

## Overview
Structure an evidence-based map of order, item, routing, and status information between ERP and MES.

## Triggers
- System boundaries, interface evidence, object identities, and known owners are supplied.

## Non-Triggers
- Writing records, activating interfaces, releasing orders, or changing production control.

## Required Inputs
- System names, object identifiers, interface direction, sample payload or field mapping, and ownership.

## Optional Inputs
- Revision history, error handling, cadence, reconciliation logs, and environment labels.

## Assumptions
- A sample message or diagram does not prove complete production coverage.

## Core Workflow
1. Set the system and transaction boundary.
2. Map objects, identifiers, directions, and owners from supplied evidence.
3. Reconcile mismatches, missing handoffs, and unresolved ownership.

## Calculations
No manufacturing result is calculated; counts of mapped fields or interfaces retain their evidence scope.

## Validation
- Check object identity, direction, revision, environment, ownership, and evidence date.

## Exception Handling
- Missing interface evidence returns `NEEDS_INPUT`.
- A request to edit or activate an interface returns `OUT_OF_SCOPE`.

## Source Usage
- Apply `references/erp-mes-flow-checklist.md` and AM-07 source controls.

## Output Contract
Return `status`, system boundary, flow map, identity mappings, ownership, gaps, assumptions, and handoff.

## Safety Requirements
AM-05 class: `ROUTINE`. Do not write ERP/MES records or authorize control changes.

## References
- `references/erp-mes-flow-checklist.md`

## Examples
If ERP and MES use different order identifiers, record the mapping gap rather than choosing a replacement.

## Testing
Cover correct invocation, missing interface evidence, identity conflict, expected output structure, and live-write refusal. Expected routing is not observed behavior.
