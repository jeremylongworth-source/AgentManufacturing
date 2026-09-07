---
name: trace-production-lot
description: Query supplied genealogy evidence for a target production lot and exposure question without releasing or recalling product.
license: PENDING_PROJECT_GOVERNANCE
---

# Trace Production Lot

**Taxonomy metadata:** family `12` Materials, BOM & Traceability; tier `CORE`; safety class `REGULATED`; jurisdiction `PENDING_CONTEXT` with `SECTOR_REGULATED`; priority `P1`; status `TAXONOMY_ACCEPTED_NOT_IMPLEMENTED`.

## Overview
Trace a target lot through supplied input, process, output, and shipment relationships.

## Triggers
- Target lot, genealogy records, direction, and exposure question are supplied.

## Non-Triggers
- Releasing, recalling, quarantining, or altering product custody.

## Required Inputs
- Lot identity, trace direction, relationship records, date boundary, and question.

## Optional Inputs
- Customer/shipment links, process records, substitutions, and data-quality flags.

## Assumptions
- Missing genealogy leaves exposure unknown; absence of a link is not proof of no relationship.

## Core Workflow
1. Anchor target identity and trace direction.
2. Traverse supplied relationships and mark breaks.
3. Return known, unknown, and owner escalation scope.

## Calculations
No calculation; relationship counts retain source and direction.

## Validation
- Check lot identity, direction, relationship dates, revision, and source completeness.

## Exception Handling
- Missing target or records returns `NEEDS_INPUT`.
- Release, recall, or custody instruction returns `SAFETY_ESCALATION`.

## Source Usage
- Apply `references/production-lot-trace-checklist.md` and AM-07 jurisdiction rules.

## Output Contract
Return `status`, target, direction, trace path, breaks, exposure scope, assumptions, and qualified handoff.

## Safety Requirements
AM-05 class: `REGULATED`. Do not release, recall, quarantine, or move product.

## References
- `references/production-lot-trace-checklist.md`

## Examples
A missing input-lot link remains an unknown branch, not evidence of no exposure.

## Testing
Cover correct invocation, missing genealogy, jurisdiction context, expected output structure, and custody refusal. Expected routing is not observed behavior.
