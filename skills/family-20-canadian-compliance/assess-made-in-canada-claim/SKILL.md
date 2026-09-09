---
name: assess-made-in-canada-claim
description: Assess evidence for a proposed non-food Made in Canada claim while preserving source freshness and withholding publication or legal endorsement.
license: PENDING_PROJECT_GOVERNANCE
---

# Assess Made in Canada Claim

## Overview

This reference skill prepares an evidence assessment for a proposed non-food Canadian-origin claim. It checks product context, transformation evidence, direct-cost evidence, qualifying wording, and current official guidance, then identifies missing substantiation and review owners. It does not publish a claim or provide a legal conclusion.

**Taxonomy metadata:** family `20` Canadian Regulatory & Jurisdiction Overlay; tier `CANADA_OVERLAY`; safety class `REGULATED`; jurisdiction `PENDING_CONTEXT` with `CANADA_FEDERAL` and `SECTOR_REGULATED`; priority `P0`; status `TAXONOMY_ACCEPTED_NOT_IMPLEMENTED` before AM-10 reference proof. Dependencies: `identify-applicable-regulatory-layer`, `verify-regulatory-source-freshness`, `SOURCE`, `FEDERAL`, `REVIEW`. Audit distinction: assess the non-food claim basis; food, sector, and other origin claims route separately.

## Triggers

- The user provides a proposed non-food origin claim and asks whether supplied transformation or cost evidence is sufficient for review.
- The user asks for a substantiation checklist or evidence gap assessment against current official guidance.

## Non-Triggers

- Food labelling, sector-specific certification, legal advice, final claim approval, packaging publication, or an enforcement prediction.
- A workplace safety or provincial employment question that is unrelated to the product claim.

## Required Inputs

- Exact proposed wording and product/non-food context.
- Production transformation evidence and direct-cost evidence with definitions and period.
- Product, components, processing, and supply-chain context.
- Current official guidance or permission to retrieve and verify it.

## Optional Inputs

- Cost ledger, manufacturing records, bill of materials, qualifying statement, counsel review, sector overlay, and prior substantiation review.

## Assumptions

- A Canadian address, final assembly, or supplier location alone does not establish a claim.
- Cost percentages are calculated only from supplied, defined, comparable direct-cost evidence; missing components remain missing.
- Official guidance is time-sensitive and does not replace sector-specific or professional review.

## Core Workflow

1. Confirm the exact claim, product category, non-food status, jurisdiction, sector, evidence period, and source freshness.
2. Check whether transformation and direct-cost evidence are complete and comparable; calculate only transparent arithmetic when definitions are supplied.
3. Return an evidence assessment, missing substantiation, source notes, and qualified review handoff without endorsing or publishing the wording.

## Calculations

If the source definitions support it, `Canadian direct-cost percentage = qualifying direct costs incurred in Canada / total direct costs × 100`. Preserve numerator, denominator, inclusions, exclusions, period, currency, product and source. Require finite values, a positive denominator, and a nonnegative numerator no greater than total. Reject mixed currencies, overlapping costs and incomplete ledgers; do not round a ratio up to a threshold. Do not infer a threshold, treat it as a legal safe harbour, or calculate with incomplete definitions.

## Validation

- Confirm current official source, access date, product/non-food scope, exact wording, and qualifying statement evidence.
- Reconcile cost ledger definitions and transformation records; flag missing, stale, or contradictory evidence.
- Keep any arithmetic traceable and separate from the legal or publication decision.

## Exception Handling

- Incomplete cost or transformation evidence returns `NEEDS_INPUT` or `PARTIAL` and lists the missing substantiation; no endorsement is made.
- Food or sector-specific context returns `JURISDICTION_REVIEW_REQUIRED`/`SOURCE_REVIEW_REQUIRED` with the appropriate overlay owner.
- Stale or conflicting guidance returns `SOURCE_REVIEW_REQUIRED`.
- Publication, certification, or legal-opinion requests return `OUT_OF_SCOPE` with qualified review.

## Source Usage

- Use `references/non-food-origin-claim-source-note.md`, `docs/architecture/canadian-jurisdiction-model.md`, `docs/architecture/canadian-source-registry.json`, and `docs/architecture/source-freshness-policy.json`.
- Current official guidance must be cited with publisher, title, URL, access date, source class, and freshness rule. Use paraphrase; do not reproduce protected guidance.
- Treat source indicators as evidence checks, not an automatic legal verdict. Reverify before any decision or publication.

## Output Contract

Return `status`, claim wording, product and jurisdiction scope, evidence inventory, arithmetic trace if applicable, source/freshness notes, missing substantiation, assumptions, validation notes, and qualified review/publication handoff. Allowed statuses are `PARTIAL`, `NEEDS_INPUT`, `OUT_OF_SCOPE`, `SOURCE_REVIEW_REQUIRED`, `JURISDICTION_REVIEW_REQUIRED`, and `ENGINEERING_REVIEW_REQUIRED`; never return an approval status.

## Safety Requirements

AM-05 class: `REGULATED`. Do not certify compliance, approve the claim, publish wording, or provide a legal conclusion. Escalate food, sector-regulated, conflicting, or enforcement-sensitive contexts to the qualified regulatory/legal owner.

## References

- `references/non-food-origin-claim-source-note.md`
- `docs/architecture/canadian-jurisdiction-model.md`
- `docs/architecture/canadian-source-registry.json`

## Examples

Read `references/non-food-origin-claim-source-note.md` for an incomplete-evidence example. The example identifies missing substantiation and does not endorse a label.

## Testing

Cover correct invocation, incorrect invocation, missing inputs, ambiguous scenario, expected output structure, jurisdiction conflicts, stale standards, unsupported assumptions, and incomplete cost/transformation evidence. The acceptance case must identify missing substantiation and withhold endorsement. Expected routing is not observed behavior.
