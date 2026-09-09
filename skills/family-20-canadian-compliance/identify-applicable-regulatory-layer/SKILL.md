---
name: identify-applicable-regulatory-layer
description: Map authority and source research for a manufacturing obligation from supplied jurisdiction context while preserving unresolved applicability.
license: PENDING_PROJECT_GOVERNANCE
---

# Identify Applicable Regulatory Layer

## Overview

Map authority and source research for a manufacturing obligation from supplied jurisdiction context while preserving unresolved applicability. Maps source/applicability questions from context; source freshness verifies individual evidence separately.

**Taxonomy metadata:** family `20` Canadian Regulatory & Jurisdiction Overlay; tier `CORE`; safety class `REGULATED`; jurisdiction `PENDING_CONTEXT` with `SECTOR_REGULATED`; priority `P1`; status `TAXONOMY_ACCEPTED_NOT_IMPLEMENTED`. Dependencies: `identify-manufacturing-jurisdiction`, `SOURCE`.

## Triggers

Jurisdiction context exists and the user needs an obligation-specific federal, provincial, territorial, sector, or local research map.

## Non-Triggers

Initial context collection alone, source version verification alone, or requests for a binding legal classification.

## Required Inputs

- Jurisdiction-context record.
- Requested obligation.
- Relevant authority evidence.

## Optional Inputs

Prior applicability assessment, local permits, contracts, manufacturer documents, named standards and incorporation evidence.

## Assumptions

Authority can differ between obligations at the same facility. Guidance, a voluntary standard, and a legal instrument have different authority. Supplied applicability and source assessments are evidence to inspect, not authority to approve a dependent conclusion.

## Core Workflow

1. Reuse the jurisdiction-context record and split requested obligations before selecting candidate authorities.
2. For each obligation, map candidate authority, legal instrument, official guidance, scope question, and evidence needed. Separate supplier/product rules from employer/workplace rules.
3. Record applicable-law research separately from standards incorporation, contract obligations, site permissions, and local authority questions. A named standard is not proof of incorporation.
4. Assign applicability_state per row using PENDING_CONTEXT, SOURCE_REVIEW_REQUIRED, COVERAGE_GAP, or CONFLICT_REVIEW_REQUIRED; do not issue a verified-applicability verdict.
5. Hand each source to verify-regulatory-source-freshness. Give unresolved workplace questions to the qualified jurisdiction owner and identify AM-27 provincial coverage as pending when unavailable.

## Calculations

None. Do not rank source authority by recency alone or average conflicting requirements.

## Validation

Each authority candidate must have an obligation, scope rationale, and unresolved evidence. Missing provincial coverage cannot be satisfied with Ontario or federal substitution. Trace each finding to supplied evidence or a scoped source; keep absence distinct from contradiction.

## Exception Handling

Missing evidence returns `NEEDS_INPUT` or a bounded `PARTIAL` inventory. Unresolved authority or coverage returns `JURISDICTION_REVIEW_REQUIRED`; stale, conflicting or unverified sources return `SOURCE_REVIEW_REQUIRED`. Requests for publication, certification or a legal opinion return `OUT_OF_SCOPE` with qualified review. Continue unrelated supported work.

## Source Usage

Read [the review notes](references/review-notes.md) for source entry points and the boundary example. Repository source records are in [AM-26 source records](../../../docs/architecture/am26-federal-source-records.json), with [source evidence](../../../docs/development/AM-26-source-evidence.md). Use official law for legal obligations and distinguish guidance from law. Verify at the requested activity date and cite publisher, title, URL, source class, version/effective or currency note, access date, and applicability basis. Preserve rights; do not reconstruct protected text.

## Output Contract

Return `status`, scope, supplied evidence, assumptions, obligation_map with authority_candidates, source_keys, applicability_basis, applicability_state, conflicts, coverage_gaps, review_owner, validation notes and next owner. Allowed statuses: `PARTIAL`, `NEEDS_INPUT`, `SOURCE_REVIEW_REQUIRED`, `JURISDICTION_REVIEW_REQUIRED`, `OUT_OF_SCOPE`. Record source and applicability states separately from output status. There is no approval status.

## Safety Requirements

AM-05 class: `REGULATED`. No compliance certification, legal opinion, operating permission, claim publication, or automatic exemption. Escalate unresolved dependent decisions to the qualified regulatory/legal or workplace safety owner. Evidence review does not establish safe operation.

## References

- [Review notes](references/review-notes.md).
- [Canadian jurisdiction model](../../../docs/architecture/canadian-jurisdiction-model.md).
- [Source freshness policy](../../../docs/architecture/source-freshness-policy.json).

## Examples

The plant's Alberta address is known, but its employer undertaking is undocumented. Record candidate workplace research paths and request undertaking evidence; do not mark Alberta or federal workplace law established.

## Testing

Cover the frozen acceptance case, missing context, incorrect invocation, unsupported assumptions, source conflicts and output structure using the AM-26 scenarios. Expected routing is not observed behavior. Runtime model evaluation remains `NOT_RUN`.
