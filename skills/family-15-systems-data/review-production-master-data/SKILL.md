---
name: review-production-master-data
description: Review supplied manufacturing master data for identity, revision, routing, and reference defects without making live corrections.
license: MIT
---

# Review Production Master Data

**Taxonomy metadata:** family `15` Manufacturing Systems & Data; tier `CORE`; safety class `ROUTINE`; jurisdiction `GENERIC_METHOD_ONLY`; priority `P1`; status `TAXONOMY_ACCEPTED_NOT_IMPLEMENTED`.

## Overview
Assess durable item, BOM, routing, resource, and revision records against supplied field rules.

## Triggers
- A master-data export, revision basis, reference rules, and affected object scope are supplied.

## Non-Triggers
- Editing records, activating a revision, releasing a routing, or approving a design.

## Required Inputs
- Object IDs, revisions, effective dates, BOM/routing references, field rules, and source environment.

## Optional Inputs
- Change history, duplicate reports, status codes, ownership, and downstream references.

## Assumptions
- A detected defect is a review finding, not proof that a production record is safe to replace.

## Core Workflow
1. Establish object and revision scope.
2. Check identities, references, dates, statuses, and required fields.
3. Return defect evidence, impact questions, and correction ownership.

## Calculations
Counts of defects preserve the export population and rule version; no capacity or release result is inferred.

## Validation
- Check uniqueness, referential integrity, revision/effectivity, status, and environment.

## Exception Handling
- Missing rule or revision basis returns `SOURCE_REVIEW_REQUIRED`.
- A live correction request returns `OUT_OF_SCOPE`.

## Source Usage
- Apply `references/production-master-data-checklist.md` and AM-07 source controls.

## Output Contract
Return `status`, object scope, rule basis, findings, impact questions, owners, and handoff.

## Safety Requirements
AM-05 class: `ROUTINE`. Do not activate, delete, or correct live master data.

## References
- `references/production-master-data-checklist.md`

## Examples
An obsolete routing reference is reported with its affected objects; no replacement is activated.

## Testing
Cover correct invocation, obsolete reference, missing revision basis, expected output structure, and live-correction refusal. Expected routing is not observed behavior.
