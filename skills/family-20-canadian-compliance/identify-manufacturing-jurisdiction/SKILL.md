---
name: identify-manufacturing-jurisdiction
description: Collect manufacturing jurisdiction context for mixed product and workplace questions without deciding legal applicability.
license: PENDING_PROJECT_GOVERNANCE
---

# Identify Manufacturing Jurisdiction

## Overview

Collect manufacturing jurisdiction context for mixed product and workplace questions without deciding legal applicability. Collects context separately from authority selection; not a legal classification service.

**Taxonomy metadata:** family `20` Canadian Regulatory & Jurisdiction Overlay; tier `CORE`; safety class `REGULATED`; jurisdiction `PENDING_CONTEXT` with `SECTOR_REGULATED`; priority `P1`; status `TAXONOMY_ACCEPTED_NOT_IMPLEMENTED`. Dependencies: `SOURCE`.

## Triggers

A manufacturing request mixes location, employer activity, product rules, or workplace jurisdiction and needs a context record.

## Non-Triggers

Selecting particular legal provisions, certifying jurisdiction, or reviewing an already scoped product claim; route those to the relevant layer or claim skill.

## Required Inputs

- Country and facility location.
- Employer/activity context.
- Product and requested obligation.
- Assessment date.

## Optional Inputs

Organization activity description, facility list, market destinations, prior regulator correspondence, and supplied authority determinations.

## Assumptions

A federal product rule, Canadian incorporation, interprovincial sales, or plant address alone does not establish the employer's workplace regime. Supplied applicability and source assessments are evidence to inspect, not authority to approve a dependent conclusion.

## Core Workflow

1. Separate each requested obligation into product, supplier, workplace, environmental, transport, labelling, or other context.
2. Record country, province/territory, actual facility/activity, employer undertaking, product/sector, requested activity, and as-of date. Mark each known, unknown, conflicting, or not applicable; retain its provenance.
3. Keep product regime and employer/workplace regime in separate fields. Flag missing undertaking evidence even when province is known.
4. Return the context record and targeted evidence requests. Hand off authority research to identify-applicable-regulatory-layer; continue unrelated generic analysis.

## Calculations

None. Location and sector labels are evidence fields, not a jurisdiction score.

## Validation

Check every stated jurisdiction against supplied facts. Do not replace unknown employer activity with a guessed province or federal default. Trace each finding to supplied evidence or a scoped source; keep absence distinct from contradiction.

## Exception Handling

Missing evidence returns `NEEDS_INPUT` or a bounded `PARTIAL` inventory. Unresolved authority or coverage returns `JURISDICTION_REVIEW_REQUIRED`; stale, conflicting or unverified sources return `SOURCE_REVIEW_REQUIRED`. Requests for publication, certification or a legal opinion return `OUT_OF_SCOPE` with qualified review. Continue unrelated supported work.

## Source Usage

Read [the review notes](references/review-notes.md) for source entry points and the boundary example. Repository source records are in [AM-26 source records](../../../docs/architecture/am26-federal-source-records.json), with [source evidence](../../../docs/development/AM-26-source-evidence.md). Use official law for legal obligations and distinguish guidance from law. Verify at the requested activity date and cite publisher, title, URL, source class, version/effective or currency note, access date, and applicability basis. Preserve rights; do not reconstruct protected text.

## Output Contract

Return `status`, scope, supplied evidence, assumptions, obligation_domains, context_fields with evidence and uncertainty, product_regime, workplace_regime, assessment_date, unresolved_questions, research_handoff, validation notes and next owner. Allowed statuses: `PARTIAL`, `NEEDS_INPUT`, `SOURCE_REVIEW_REQUIRED`, `JURISDICTION_REVIEW_REQUIRED`, `OUT_OF_SCOPE`. Record source and applicability states separately from output status. There is no approval status.

## Safety Requirements

AM-05 class: `REGULATED`. No compliance certification, legal opinion, operating permission, claim publication, or automatic exemption. Escalate unresolved dependent decisions to the qualified regulatory/legal or workplace safety owner. Evidence review does not establish safe operation.

## References

- [Review notes](references/review-notes.md).
- [Canadian jurisdiction model](../../../docs/architecture/canadian-jurisdiction-model.md).
- [Source freshness policy](../../../docs/architecture/source-freshness-policy.json).

## Examples

A Quebec plant cites a federal product label rule as proof that its workers fall under federal safety rules. Preserve Quebec as location, retain the product source, and leave workplace regime PENDING_CONTEXT pending undertaking evidence.

## Testing

Cover the frozen acceptance case, missing context, incorrect invocation, unsupported assumptions, source conflicts and output structure using the AM-26 scenarios. Expected routing is not observed behavior. Runtime model evaluation remains `NOT_RUN`.
