---
name: review-whmis-readiness
description: Review supplied WHMIS applicability, SDS, label, and workplace program evidence for gaps without certifying compliance or safe use.
license: PENDING_PROJECT_GOVERNANCE
---

# Review Whmis Readiness

## Overview

Review supplied WHMIS applicability, SDS, label, and workplace program evidence for gaps without certifying compliance or safe use. Assesses program/product evidence after applicability research; does not duplicate the scope assessment.

**Taxonomy metadata:** family `20` Canadian Regulatory & Jurisdiction Overlay; tier `CANADA_OVERLAY`; safety class `REGULATED`; jurisdiction `PENDING_CONTEXT` with `CANADA_FEDERAL`, `PROVINCIAL_REQUIRED`, `SECTOR_REGULATED`; priority `P1`; status `TAXONOMY_ACCEPTED_NOT_IMPLEMENTED`. Dependencies: `assess-whmis-applicability`, `SOURCE`, `FEDERAL`, `JURIS`, `REVIEW`.

## Triggers

A user supplies WHMIS research and workplace/product records for a bounded readiness evidence review.

## Non-Triggers

Determining product hazard classification, drafting an authoritative SDS, approving chemical use, or replacing an applicability assessment.

## Required Inputs

- Applicable WHMIS research.
- Product/SDS/label evidence.
- Training/program records.
- Workplace context.

## Optional Inputs

Product inventory, supplier revisions, workplace label records, education and training evidence, program review records and assigned owners.

## Assumptions

Document presence, attendance, and a supplier assurance do not establish accuracy, competence, or safe work. No universal SDS expiry interval is assumed. Supplied applicability and source assessments are evidence to inspect, not authority to approve a dependent conclusion.

## Core Workflow

1. Read assess-whmis-applicability output; retain unresolved scope and date questions instead of claiming readiness.
2. Link product inventory rows to supplied SDSs and labels using product identifier, supplier and revision. Flag mismatches, unavailable documents, language evidence, and unexplained version differences.
3. Inventory workplace label, document-access, education/training, task-specific instruction and program review evidence relevant to the researched regime. Separate observed records from claims of implementation.
4. Record each gap with source or criterion, evidence, consequence for this review, responsible owner and follow-up. Keep supplier evidence and employer program evidence distinct.
5. Return a partial evidence review if scope or current authority is unresolved; route immediate exposure concerns to the site emergency/qualified safety process without chemical-handling instructions.

## Calculations

Optional evidence counts only: state the inventory denominator and unknown records. A completeness percentage is not compliance or competence.

## Validation

Check product/SDS/label identity matches and exact revision basis. Do not infer effectiveness from training attendance or assign a universal three-year rule without applicable current authority. Trace each finding to supplied evidence or a scoped source; keep absence distinct from contradiction.

## Exception Handling

Missing evidence returns `NEEDS_INPUT` or a bounded `PARTIAL` inventory. Unresolved authority or coverage returns `JURISDICTION_REVIEW_REQUIRED`; stale, conflicting or unverified sources return `SOURCE_REVIEW_REQUIRED`. Requests for publication, certification or a legal opinion return `OUT_OF_SCOPE` with qualified review. Continue unrelated supported work.

## Source Usage

Read [the review notes](references/review-notes.md) for source entry points and the boundary example. Repository source records are in [AM-26 source records](../../../docs/architecture/am26-federal-source-records.json), with [source evidence](../../../docs/development/AM-26-source-evidence.md). Use official law for legal obligations and distinguish guidance from law. Verify at the requested activity date and cite publisher, title, URL, source class, version/effective or currency note, access date, and applicability basis. Preserve rights; do not reconstruct protected text.

## Output Contract

Return `status`, scope, supplied evidence, assumptions, inventory_links, supplier_document_gaps, workplace_program_gaps, criteria_sources, evidence_status, unresolved_scope, follow_up_owners, validation notes and next owner. Allowed statuses: `PARTIAL`, `NEEDS_INPUT`, `SOURCE_REVIEW_REQUIRED`, `JURISDICTION_REVIEW_REQUIRED`, `OUT_OF_SCOPE`. Record source and applicability states separately from output status. There is no approval status.

## Safety Requirements

AM-05 class: `REGULATED`. No compliance certification, legal opinion, operating permission, claim publication, or automatic exemption. Escalate unresolved dependent decisions to the qualified regulatory/legal or workplace safety owner. Evidence review does not establish safe operation.

## References

- [Review notes](references/review-notes.md).
- [Canadian jurisdiction model](../../../docs/architecture/canadian-jurisdiction-model.md).
- [Source freshness policy](../../../docs/architecture/source-freshness-policy.json).

## Examples

An SDS uses a different product identifier from the label and training attendance is the only program evidence. Record both gaps and request reconciliation and task-specific evidence; do not declare workers trained or the product safe.

## Testing

Cover the frozen acceptance case, missing context, incorrect invocation, unsupported assumptions, source conflicts and output structure using the AM-26 scenarios. Expected routing is not observed behavior. Runtime model evaluation remains `NOT_RUN`.
