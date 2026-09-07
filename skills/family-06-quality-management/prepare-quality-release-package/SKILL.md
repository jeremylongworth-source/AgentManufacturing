---
name: prepare-quality-release-package
description: Assemble a reviewable lot-release evidence package with completion, inspection, deviation, hold, and authorization gaps visible.
license: PENDING_PROJECT_GOVERNANCE
---

# Prepare Quality Release Package

## Overview

Assemble evidence for an authorized lot-disposition decision. Preserve open deviations, holds, incomplete records, and missing authorization; never approve or execute release.

**Taxonomy metadata:** family `06` Quality Management & Inspection; tier `CORE`; safety class `REGULATED`; jurisdiction `PENDING_CONTEXT` with `STANDARDS_DEPENDENT`, `SECTOR_REGULATED`; priority `P1`; status `TAXONOMY_ACCEPTED_NOT_IMPLEMENTED`. Dependencies: `review-product-conformity`, `review-quality-record`, `STANDARDS`, `REVIEW`. Audit distinction: assemble one decision-ready evidence package; actual release remains with the authorized owner.

## Triggers

- Lot/production completion, inspection status, open deviations, and authorization requirements are supplied for a release-package draft.

## Non-Triggers

- Releasing product, closing deviations, signing a certificate, or inventing missing inspection evidence.

## Required Inputs

- Lot identity and completion evidence.
- Inspection/conformity status, open deviations/holds, and authorization requirements.

## Optional Inputs

- Traceability, supplier certificates, rework records, record-integrity findings, and decision owner.

## Assumptions

- An open deviation remains a hold or unresolved decision until authorized disposition is supplied.
- Evidence assembly is not approval.

## Core Workflow

1. Confirm lot, scope, completion, inspection, deviation, hold, and authorization evidence.
2. Assemble an evidence index with missing/conflicting items and unresolved dispositions.
3. Return the package to the authorized quality owner without release language.

## Calculations

No calculation required; preserve supplied quantities and statuses.

## Validation

- Check lot identity, inspection completion, open deviations, record integrity, traceability, and authorization.
- Keep hold and missing disposition visible.

## Exception Handling

- Open deviation returns `PARTIAL` or `NEEDS_INPUT`.
- Conflicting evidence returns `SOURCE_REVIEW_REQUIRED`.
- Release/certificate requests return `OUT_OF_SCOPE`.

## Source Usage

- Use `references/release-package-checklist.md` and AM-07 source rules.
- Record source, revision, date, owner, and retention/rights metadata.

## Output Contract

Return `status`, lot scope, completion/inspection evidence, deviations/holds, authorization matrix, missing/conflicting evidence, assumptions, validation notes, and authorized-owner handoff. Allowed statuses include `PARTIAL`, `NEEDS_INPUT`, `OUT_OF_SCOPE`, and `SOURCE_REVIEW_REQUIRED`.

## Safety Requirements

AM-05 class: `REGULATED`. Do not release product, close a hold, certify, or sign a disposition.

## References

- `references/release-package-checklist.md`

## Examples

Read the checklist for a complete lot with an open deviation.

## Testing

Cover correct invocation, open deviation, missing inspection evidence, conflicting records, expected output structure, and release/certificate refusal. Expected routing is not observed behavior.
