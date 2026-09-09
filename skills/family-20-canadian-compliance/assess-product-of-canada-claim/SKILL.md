---
name: assess-product-of-canada-claim
description: Assess substantiation for a proposed non-food Product of Canada claim using its distinct guidance and evidence basis.
license: MIT
---

# Assess Product Of Canada Claim

## Overview

Assess substantiation for a proposed non-food Product of Canada claim using its distinct guidance and evidence basis. Keeps Product-of-Canada claim evidence distinct from Made-in-Canada criteria.

**Taxonomy metadata:** family `20` Canadian Regulatory & Jurisdiction Overlay; tier `CANADA_OVERLAY`; safety class `REGULATED`; jurisdiction `PENDING_CONTEXT` with `CANADA_FEDERAL`, `SECTOR_REGULATED`; priority `P1`; status `TAXONOMY_ACCEPTED_NOT_IMPLEMENTED`. Dependencies: `identify-applicable-regulatory-layer`, `verify-regulatory-source-freshness`, `SOURCE`, `FEDERAL`, `REVIEW`.

## Triggers

A proposed non-food Product of Canada claim needs transformation, direct-cost, wording, and source evidence review.

## Non-Triggers

Food claims, customs origin or tariff eligibility, automatic reuse of a Made in Canada conclusion, claim publication, or legal endorsement.

## Required Inputs

- Proposed non-food claim.
- Transformation and cost evidence.
- Product scope.
- Current official guidance.

## Optional Inputs

Bill of materials, ledger reconciliation, supplier origin evidence, qualifying wording, brand imagery, and qualified review notes.

## Assumptions

A Made in Canada assessment does not establish a Product of Canada claim. Supplier location or final assembly alone does not establish transformation or qualifying costs. Supplied applicability and source assessments are evidence to inspect, not authority to approve a dependent conclusion.

## Core Workflow

1. Confirm exact wording and imagery, non-food scope, product/market, evidence period, and source currency. Route food or unknown sector scope separately.
2. Reuse regulatory-layer and freshness evidence. Retrieve the specific Product of Canada guidance, preserving its distinction from Made in Canada and the authority limits of guidance.
3. Inventory last substantial transformation evidence and a reconciled ledger of qualifying Canadian and total direct costs using the source definitions. Do not infer missing components.
4. Calculate only supported arithmetic. Compare to guidance indicators only after source and evidence checks, and preserve transformation and overall-impression questions separately.
5. Return substantiation gaps and a regulatory/legal review handoff. A percentage meeting an indicator is not claim approval or a publication instruction.

## Calculations

Canadian direct-cost percentage = qualifying Canadian direct costs / total direct costs × 100. Require the same product, period, currency, accounting basis and included-cost definitions; denominator must be positive, numerator nonnegative and no greater than total, with finite values. Reject mixed currencies, overlapping costs, incomplete ledgers and rounding up to a threshold. Preserve raw values, precision and exclusions. This package has no automatic eligibility calculator.

## Validation

Use the claim-specific source and transformation evidence. Do not substitute a Made in Canada threshold, round a near-threshold ratio into eligibility, or label an incomplete numerator as zero. Trace each finding to supplied evidence or a scoped source; keep absence distinct from contradiction.

## Exception Handling

Missing evidence returns `NEEDS_INPUT` or a bounded `PARTIAL` inventory. Unresolved authority or coverage returns `JURISDICTION_REVIEW_REQUIRED`; stale, conflicting or unverified sources return `SOURCE_REVIEW_REQUIRED`. Requests for publication, certification or a legal opinion return `OUT_OF_SCOPE` with qualified review. Continue unrelated supported work.

## Source Usage

Read [the review notes](references/review-notes.md) for source entry points and the boundary example. Repository source records are in [AM-26 source records](../../../docs/architecture/am26-federal-source-records.json), with [source evidence](../../../docs/development/AM-26-source-evidence.md). Use official law for legal obligations and distinguish guidance from law. Verify at the requested activity date and cite publisher, title, URL, source class, version/effective or currency note, access date, and applicability basis. Preserve rights; do not reconstruct protected text.

## Output Contract

Return `status`, scope, supplied evidence, assumptions, claim_wording, product_market_scope, transformation_evidence, cost_ledger_basis, arithmetic_trace, guidance_comparison, source_status, missing_substantiation, review_handoff, validation notes and next owner. Allowed statuses: `PARTIAL`, `NEEDS_INPUT`, `SOURCE_REVIEW_REQUIRED`, `JURISDICTION_REVIEW_REQUIRED`, `OUT_OF_SCOPE`. Record source and applicability states separately from output status. There is no approval status.

## Safety Requirements

AM-05 class: `REGULATED`. No compliance certification, legal opinion, operating permission, claim publication, or automatic exemption. Escalate unresolved dependent decisions to the qualified regulatory/legal or workplace safety owner. Evidence review does not establish safe operation.

## References

- [Review notes](references/review-notes.md).
- [Canadian jurisdiction model](../../../docs/architecture/canadian-jurisdiction-model.md).
- [Source freshness policy](../../../docs/architecture/source-freshness-policy.json).

## Examples

Only a prior Made in Canada assessment is supplied for proposed Product of Canada wording. Return NEEDS_INPUT for the claim-specific transformation and direct-cost substantiation, preserving the earlier assessment as evidence only.

## Testing

Cover the frozen acceptance case, missing context, incorrect invocation, unsupported assumptions, source conflicts and output structure using the AM-26 scenarios. Expected routing is not observed behavior. Runtime model evaluation remains `NOT_RUN`.
