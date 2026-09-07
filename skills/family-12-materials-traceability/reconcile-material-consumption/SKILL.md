---
name: reconcile-material-consumption
description: Reconcile material issue, return, scrap, and work-in-process events into a coherent consumption balance without changing records.
license: PENDING_PROJECT_GOVERNANCE
---

# Reconcile Material Consumption

**Taxonomy metadata:** family `12` Materials, BOM & Traceability; tier `CORE`; safety class `ROUTINE`; jurisdiction `GENERIC_METHOD_ONLY`; priority `P1`; status `TAXONOMY_ACCEPTED_NOT_IMPLEMENTED`.

## Overview
Establish a coherent consumption balance from declared event states.

## Triggers
- Issue, return, scrap, WIP, product, lot, units, and period records are supplied.

## Non-Triggers
- Editing inventory, moving material, or deciding disposition.

## Required Inputs
- Population, event types, quantities, units, timestamps, and reconciliation rule.

## Optional Inputs
- Rework, substitutions, yield, adjustment approvals, and system status.

## Assumptions
- Unreconciled transactions remain gaps rather than being silently netted.

## Core Workflow
1. Normalize event type, identity, units, and period.
2. Reconcile issue, return, scrap, and WIP states.
3. Return balance, breaks, and owner handoff.

## Calculations
`consumption = issues - returns - recoverable WIP`; apply only the declared event rule.

## Validation
- Check units, timestamps, duplicates, event completeness, and approvals.

## Exception Handling
- Missing event state returns `NEEDS_INPUT`.
- Inventory adjustment or movement request returns `OUT_OF_SCOPE`.

## Source Usage
- Apply `references/material-consumption-reconciliation-checklist.md` and AM-08 rules.

## Output Contract
Return `status`, population, events, formula, intermediates, balance, breaks, and handoff.

## Safety Requirements
AM-05 class: `ROUTINE`. Stop at the manufacturing/warehouse interface; do not alter or move inventory.

## References
- `references/material-consumption-reconciliation-checklist.md`

## Examples
An unapproved adjustment remains a reconciliation gap, not a corrected balance.

## Testing
Cover correct invocation, missing event state, unit mismatch, expected output structure, and inventory-change refusal. Expected routing is not observed behavior.
