---
name: review-nonfood-labelling-readiness
description: Review general prepackaged non-food consumer label evidence with product exclusions and sector-specific coverage kept explicit.
license: PENDING_PROJECT_GOVERNANCE
---

# Review Nonfood Labelling Readiness

## Overview

Review general prepackaged non-food consumer label evidence with product exclusions and sector-specific coverage kept explicit. Reviews general non-food label scope/evidence; sector-specific label rules remain explicit overlays.

**Taxonomy metadata:** family `20` Canadian Regulatory & Jurisdiction Overlay; tier `CANADA_OVERLAY`; safety class `REGULATED`; jurisdiction `PENDING_CONTEXT` with `CANADA_FEDERAL`, `SECTOR_REGULATED`; priority `P1`; status `TAXONOMY_ACCEPTED_NOT_IMPLEMENTED`. Dependencies: `identify-applicable-regulatory-layer`, `verify-regulatory-source-freshness`, `SOURCE`, `FEDERAL`, `REVIEW`.

## Triggers

A Canadian prepackaged non-food consumer product label draft needs a scoped evidence-gap review.

## Non-Triggers

Food, drugs, medical devices or other specialized label approval; WHMIS supplier labels; customs origin; artwork publication; a universal checklist for every manufactured product.

## Required Inputs

- Label draft.
- Product/market scope.
- Packaging facts.
- Applicable current sources.

## Optional Inputs

Panel dimensions and layout, bilingual text, quantity measurement basis, dealer information, market provinces, exemption rationale and specialist reviews.

## Assumptions

Non-food alone does not establish general consumer-labelling scope. Industrial-only and sector-specific products need explicit scope research; an exemption here does not remove other obligations. Supplied applicability and source assessments are evidence to inspect, not authority to approve a dependent conclusion.

## Core Workflow

1. Confirm product class, consumer versus commercial/industrial/institutional channel, prepackaging, domestic versus export market, sale location and review date. Reuse authority-layer and freshness records.
2. Research scope and exclusions using current Act/regulations and official guidance. Retain unknown or sector-specific scope as a coverage gap rather than applying a universal checklist.
3. For supported scope, map supplied product identity, net quantity and units, dealer information, language, placement, legibility and display evidence to source-specific criteria. Do not invent font sizes, tolerances or language exemptions.
4. Separate origin/marketing claims from mandatory label evidence; route claims to their distinct skills and provincial language questions to qualified research.
5. Return an annotated evidence-gap table and reviewer handoff. Missing artwork dimensions or measurement support remain gaps; no print, sale or packaging release.

## Calculations

Only transparent quantity/unit conversions with supplied measurement basis. Do not infer legal tolerances, type-size limits or required units from an image.

## Validation

Every checklist item needs a scope and source. Do not mark unknown, food or specialized products compliant with generic non-food guidance. Trace each finding to supplied evidence or a scoped source; keep absence distinct from contradiction.

## Exception Handling

Missing evidence returns `NEEDS_INPUT` or a bounded `PARTIAL` inventory. Unresolved authority or coverage returns `JURISDICTION_REVIEW_REQUIRED`; stale, conflicting or unverified sources return `SOURCE_REVIEW_REQUIRED`. Requests for publication, certification or a legal opinion return `OUT_OF_SCOPE` with qualified review. Continue unrelated supported work.

## Source Usage

Read [the review notes](references/review-notes.md) for source entry points and the boundary example. Repository source records are in [AM-26 source records](../../../docs/architecture/am26-federal-source-records.json), with [source evidence](../../../docs/development/AM-26-source-evidence.md). Use official law for legal obligations and distinguish guidance from law. Verify at the requested activity date and cite publisher, title, URL, source class, version/effective or currency note, access date, and applicability basis. Preserve rights; do not reconstruct protected text.

## Output Contract

Return `status`, scope, supplied evidence, assumptions, product_channel_scope, exclusions_research, label_evidence_table, mandatory_information_gaps, language_layout_questions, separate_claim_routes, review_handoff, validation notes and next owner. Allowed statuses: `PARTIAL`, `NEEDS_INPUT`, `SOURCE_REVIEW_REQUIRED`, `JURISDICTION_REVIEW_REQUIRED`, `OUT_OF_SCOPE`. Record source and applicability states separately from output status. There is no approval status.

## Safety Requirements

AM-05 class: `REGULATED`. No compliance certification, legal opinion, operating permission, claim publication, or automatic exemption. Escalate unresolved dependent decisions to the qualified regulatory/legal or workplace safety owner. Evidence review does not establish safe operation.

## References

- [Review notes](references/review-notes.md).
- [Canadian jurisdiction model](../../../docs/architecture/canadian-jurisdiction-model.md).
- [Source freshness policy](../../../docs/architecture/source-freshness-policy.json).

## Examples

A package is sold only for industrial use, and the user asks for consumer-label approval. Record the channel and scope question and route applicable product/sector research; do not approve the label or imply that no label rules apply.

## Testing

Cover the frozen acceptance case, missing context, incorrect invocation, unsupported assumptions, source conflicts and output structure using the AM-26 scenarios. Expected routing is not observed behavior. Runtime model evaluation remains `NOT_RUN`.
