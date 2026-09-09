---
name: review-quality-requirement
description: Review supplied product or customer quality requirements for applicability, revision, clarity, and unresolved acceptance questions.
license: MIT
---

# Review Quality Requirement

## Overview

Interpret the applicability and clarity of supplied product or customer quality requirements for a requested decision. Preserve conflicting revisions and source gaps; do not select the easier criterion or certify conformance.

**Taxonomy metadata:** family `06` Quality Management & Inspection; tier `CORE`; safety class `REGULATED`; jurisdiction `PENDING_CONTEXT` with `STANDARDS_DEPENDENT`, `SECTOR_REGULATED`; priority `P1`; status `TAXONOMY_ACCEPTED_NOT_IMPLEMENTED`. Dependencies: `STANDARDS`, `REVIEW`. Audit distinction: interpret supplied requirements; conformance compares actual evidence later.

## Triggers

- Product/customer requirements, applicability and revision evidence, and the requested decision are supplied.

## Non-Triggers

- Setting acceptance limits, approving product, releasing a lot, legal interpretation, or creating a new specification.

## Required Inputs

- Requirement documents, product/customer scope, revision/effective evidence, and requested decision.

## Optional Inputs

- Contract hierarchy, sector context, change history, test method, and owner.

## Assumptions

- Conflicting requirements remain conflicting; no criterion is chosen for convenience.
- A standard or customer document is evidence to assess, not automatic applicability.

## Core Workflow

1. Confirm product, customer, sector, jurisdiction, revision, and requested decision.
2. Compare requirements, applicability, definitions, acceptance criteria, and conflicts.
3. Return interpretation gaps, questions, source notes, and qualified owner handoff.

## Calculations

No calculation required.

## Validation

- Check revision, effective date, source authority, scope, units, and conflict resolution owner.
- Separate requirement interpretation from conformance and release.

## Exception Handling

- Missing requirement or applicability returns `NEEDS_INPUT`.
- Conflicting revisions return `SOURCE_REVIEW_REQUIRED`.
- Certification, legal, or release requests return `OUT_OF_SCOPE`/`ENGINEERING_REVIEW_REQUIRED`.

## Source Usage

- Use `references/quality-requirement-review.md` and AM-07 source/freshness rules.
- Record publisher/customer, title, revision, effective date, access date, and permitted use; do not reproduce protected standards text.

## Output Contract

Return `status`, requirement scope, sources/revisions, interpretation, conflicts, unresolved questions, assumptions, validation notes, and qualified handoff. Allowed statuses include `PARTIAL`, `NEEDS_INPUT`, `OUT_OF_SCOPE`, `SOURCE_REVIEW_REQUIRED`, and `ENGINEERING_REVIEW_REQUIRED`.

## Safety Requirements

AM-05 class: `REGULATED`. Do not certify compliance, set limits, approve a release, or provide a legal conclusion.

## References

- `references/quality-requirement-review.md`

## Examples

Read the reference for conflicting customer revisions.

## Testing

Cover correct invocation, conflicting revisions, missing applicability, stale source, expected output structure, and release/certification refusal. Expected routing is not observed behavior.
