---
name: assess-whmis-applicability
description: Assess WHMIS product, activity, and supplier versus employer scope evidence before a workplace readiness review.
license: PENDING_PROJECT_GOVERNANCE
---

# Assess Whmis Applicability

## Overview

Assess WHMIS product, activity, and supplier versus employer scope evidence before a workplace readiness review. Canadian requirement overlay establishes role/activity questions before readiness review.

**Taxonomy metadata:** family `20` Canadian Regulatory & Jurisdiction Overlay; tier `CANADA_OVERLAY`; safety class `REGULATED`; jurisdiction `PENDING_CONTEXT` with `CANADA_FEDERAL`, `PROVINCIAL_REQUIRED`, `SECTOR_REGULATED`; priority `P1`; status `TAXONOMY_ACCEPTED_NOT_IMPLEMENTED`. Dependencies: `identify-applicable-regulatory-layer`, `verify-regulatory-source-freshness`, `SOURCE`, `FEDERAL`, `JURIS`, `REVIEW`.

## Triggers

A Canadian manufacturing request asks whether or how WHMIS supplier or employer requirements may apply to a product or activity.

## Non-Triggers

SDS authoring, chemical hazard classification from a product name, chemical-handling instructions, or a full program readiness review after scope is established.

## Required Inputs

- Product/activity and supplier/workplace role.
- Jurisdiction context.
- Current official sources.

## Optional Inputs

Supplier correspondence, classification basis from a competent source, proposed exemptions and supporting provisions, intended-use records.

## Assumptions

An SDS on file does not prove applicability, correct classification, or workplace readiness. An apparent supplier exclusion does not remove other workplace duties. Supplied applicability and source assessments are evidence to inspect, not authority to approve a dependent conclusion.

## Core Workflow

1. Reuse the regulatory-layer and source-freshness records. Confirm product identity, intended workplace use, activity date, and whether the entity imports, sells, distributes, manufactures, uses, handles, or stores it.
2. Separate supplier/importer role evidence from employer/worker role evidence. One entity may occupy both roles.
3. Research HPA/HPR product scope and claimed exclusions against current official text and competent classification evidence; retain unknown composition or intended use as gaps.
4. Route employer duties by established workplace regime, not supplier rules. Review amendment/effectivity and any transition evidence for the activity date.
5. Return a role-by-role applicability research brief and open questions. Hand the bounded result to review-whmis-readiness; no verified applicability or compliance conclusion.

## Calculations

None. Do not derive hazard classes or exemption eligibility from quantities or product names.

## Validation

Preserve role, product, workplace, date, exclusions, authority and source status separately. Never treat a supplier document as proof of employer training. Trace each finding to supplied evidence or a scoped source; keep absence distinct from contradiction.

## Exception Handling

Missing evidence returns `NEEDS_INPUT` or a bounded `PARTIAL` inventory. Unresolved authority or coverage returns `JURISDICTION_REVIEW_REQUIRED`; stale, conflicting or unverified sources return `SOURCE_REVIEW_REQUIRED`. Requests for publication, certification or a legal opinion return `OUT_OF_SCOPE` with qualified review. Continue unrelated supported work.

## Source Usage

Read [the review notes](references/review-notes.md) for source entry points and the boundary example. Repository source records are in [AM-26 source records](../../../docs/architecture/am26-federal-source-records.json), with [source evidence](../../../docs/development/AM-26-source-evidence.md). Use official law for legal obligations and distinguish guidance from law. Verify at the requested activity date and cite publisher, title, URL, source class, version/effective or currency note, access date, and applicability basis. Preserve rights; do not reconstruct protected text.

## Output Contract

Return `status`, scope, supplied evidence, assumptions, role_activity_matrix, product_scope_evidence, proposed_exclusions with basis, supplier_research, workplace_research, applicability_state, unresolved_questions, readiness_handoff, validation notes and next owner. Allowed statuses: `PARTIAL`, `NEEDS_INPUT`, `SOURCE_REVIEW_REQUIRED`, `JURISDICTION_REVIEW_REQUIRED`, `OUT_OF_SCOPE`. Record source and applicability states separately from output status. There is no approval status.

## Safety Requirements

AM-05 class: `REGULATED`. No compliance certification, legal opinion, operating permission, claim publication, or automatic exemption. Escalate unresolved dependent decisions to the qualified regulatory/legal or workplace safety owner. Evidence review does not establish safe operation.

## References

- [Review notes](references/review-notes.md).
- [Canadian jurisdiction model](../../../docs/architecture/canadian-jurisdiction-model.md).
- [Source freshness policy](../../../docs/architecture/source-freshness-policy.json).

## Examples

An importer also uses a supplied chemical and says its SDS satisfies all employer duties. Separate importer and employer research, request workplace regime and program evidence, and withhold any applicability or compliance endorsement.

## Testing

Cover the frozen acceptance case, missing context, incorrect invocation, unsupported assumptions, source conflicts and output structure using the AM-26 scenarios. Expected routing is not observed behavior. Runtime model evaluation remains `NOT_RUN`.
