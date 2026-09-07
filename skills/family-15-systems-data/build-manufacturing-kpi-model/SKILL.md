---
name: build-manufacturing-kpi-model
description: Define manufacturing KPI lineage, denominators, exclusions, and reporting scope without silently merging incompatible measures.
license: PENDING_PROJECT_GOVERNANCE
---

# Build Manufacturing KPI Model

**Taxonomy metadata:** family `15` Manufacturing Systems & Data; tier `CORE`; safety class `ROUTINE`; jurisdiction `GENERIC_METHOD_ONLY`; priority `P2`; status `TAXONOMY_ACCEPTED_NOT_IMPLEMENTED`.

## Overview
Build a reviewable KPI definition model that connects decisions to measures, sources, denominators, and exclusions.

## Triggers
- Decision questions, candidate metrics, source systems, reporting grain, and period basis are supplied.

## Non-Triggers
- Publishing executive results, changing targets, ranking people, or replacing source data.

## Required Inputs
- KPI name, purpose, numerator, denominator, source lineage, grain, period, and exclusions.

## Optional Inputs
- Owner, refresh cadence, confidence, segmentation, benchmark, and calculation formula.

## Assumptions
- Similar labels can represent different measures; definitions must remain distinct until reviewed.

## Core Workflow
1. Link each decision question to a measurable outcome.
2. Define numerator, denominator, units, grain, lineage, exclusions, and comparison basis.
3. Identify conflicts, missing owners, and readiness for qualified review.

## Calculations
Record formulas and units from AM-08 without calculating a result when source definitions or denominators conflict.

## Validation
- Check definition uniqueness, denominator exposure, units, period, grain, lineage, and exclusions.

## Exception Handling
- Unequal or missing denominators return `NEEDS_INPUT`.
- A request to publish or set a target returns `OUT_OF_SCOPE`.

## Source Usage
- Apply `references/manufacturing-kpi-checklist.md` and AM-08 calculation rules.

## Output Contract
Return `status`, KPI definitions, formulas, lineage, denominators, exclusions, conflicts, and handoff.

## Safety Requirements
AM-05 class: `ROUTINE`. Do not publish performance conclusions or authorize target changes.

## References
- `references/manufacturing-kpi-checklist.md`

## Examples
If two departments define yield with different denominators, preserve both definitions and expose the reconciliation decision.

## Testing
Cover correct invocation, unequal denominator, missing lineage, expected output structure, and publication refusal. Expected routing is not observed behavior.
