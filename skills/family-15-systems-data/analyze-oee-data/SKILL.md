---
name: analyze-oee-data
description: Reconcile supplied OEE counts, states, planned time, and ideal-rate definitions before any OEE calculation.
license: PENDING_PROJECT_GOVERNANCE
---

# Analyze OEE Data

**Taxonomy metadata:** family `15` Manufacturing Systems & Data; tier `CORE`; safety class `ROUTINE`; jurisdiction `GENERIC_METHOD_ONLY`; priority `P1`; status `TAXONOMY_ACCEPTED_NOT_IMPLEMENTED`.

## Overview
Review whether OEE inputs use consistent asset, period, state, count, and rate definitions.

## Triggers
- Exported counts and states, planned-time rules, ideal-rate definitions, and mapping scope are supplied.

## Non-Triggers
- Replacing the OEE calculator, choosing hidden conventions, or changing source data.

## Required Inputs
- Asset, period, planned time, run states, total and good counts, ideal-rate basis, and unit definitions.

## Optional Inputs
- Stop-code dictionary, rejects, rework, downtime reason, and event lineage.

## Assumptions
- Reconciliation findings must precede arithmetic when definitions overlap or conflict.

## Core Workflow
1. Align asset, period, population, and units.
2. Reconcile availability, performance, and quality inputs to their source events.
3. Return conflicts, missing exposure, and handoff to the approved calculation owner.

## Calculations
No OEE value is calculated here; retain supplied denominators and expose any arithmetic readiness gaps.

## Validation
- Check planned versus unplanned time, count basis, ideal rate, quality disposition, and overlap.

## Exception Handling
- Overlapping stop categories return `SOURCE_REVIEW_REQUIRED`.
- A request to alter source events returns `OUT_OF_SCOPE`.

## Source Usage
- Apply `references/oee-data-checklist.md` and AM-08 calculation rules.

## Output Contract
Return `status`, input reconciliation, definitions, conflicts, readiness, assumptions, and handoff.

## Safety Requirements
AM-05 class: `ROUTINE`. Do not direct production or rewrite OEE source records.

## References
- `references/oee-data-checklist.md`

## Examples
If a stop code overlaps planned shutdown, flag the classification conflict instead of silently recalculating OEE.

## Testing
Cover correct invocation, overlapping stop code, missing denominator, expected output structure, and source-edit refusal. Expected routing is not observed behavior.
