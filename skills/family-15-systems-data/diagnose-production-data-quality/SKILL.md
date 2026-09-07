---
name: diagnose-production-data-quality
description: Diagnose schema, identity, completeness, and consistency defects in supplied production datasets without deleting or repairing records.
license: PENDING_PROJECT_GOVERNANCE
---

# Diagnose Production Data Quality

**Taxonomy metadata:** family `15` Manufacturing Systems & Data; tier `CORE`; safety class `ROUTINE`; jurisdiction `GENERIC_METHOD_ONLY`; priority `P1`; status `TAXONOMY_ACCEPTED_NOT_IMPLEMENTED`.

## Overview
Create a data-quality defect register from a bounded production dataset and its supplied rules.

## Triggers
- Dataset extract, schema, identity rules, time basis, and requested quality scope are supplied.

## Non-Triggers
- Deleting duplicates, repairing source records, approving a dataset for release, or controlling equipment.

## Required Inputs
- Dataset scope, schema, primary keys, required fields, business rules, and identity/time conventions.

## Optional Inputs
- Source system, extract timestamp, lineage, exception history, and data owner.

## Assumptions
- A defect finding describes evidence and impact; it does not prove the physical cause.

## Core Workflow
1. Establish dataset population, schema, and rule version.
2. Test identity, completeness, validity, consistency, and timeliness conditions.
3. Rank findings by affected scope and assign remediation ownership questions.

## Calculations
Rates or counts retain the exact population and denominator; missing exposure remains a gap.

## Validation
- Check schema version, key uniqueness, null handling, domain values, timestamps, and sample scope.

## Exception Handling
- Missing schema or population returns `NEEDS_INPUT`.
- A request to delete or mutate records returns `OUT_OF_SCOPE`.

## Source Usage
- Apply `references/production-data-quality-checklist.md` and AM-07 source controls.

## Output Contract
Return `status`, dataset scope, rule basis, defect register, impact, ownership questions, and handoff.

## Safety Requirements
AM-05 class: `ROUTINE`. Do not delete, rewrite, or certify production data.

## References
- `references/production-data-quality-checklist.md`

## Examples
Repeated event IDs are reported with their affected population; no row is automatically removed.

## Testing
Cover correct invocation, duplicate ID, missing schema, expected output structure, and record-mutation refusal. Expected routing is not observed behavior.
