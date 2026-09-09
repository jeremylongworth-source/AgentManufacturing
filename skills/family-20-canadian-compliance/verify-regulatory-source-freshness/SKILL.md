---
name: verify-regulatory-source-freshness
description: Verify a regulatory source's authority, version, effectivity, and claim-specific currency while separating reachability from applicability.
license: PENDING_PROJECT_GOVERNANCE
---

# Verify Regulatory Source Freshness

## Overview

Verify a regulatory source's authority, version, effectivity, and claim-specific currency while separating reachability from applicability. Checks version/effectivity/applicability evidence for a claim; a reachable URL alone is insufficient.

**Taxonomy metadata:** family `20` Canadian Regulatory & Jurisdiction Overlay; tier `CORE`; safety class `REGULATED`; jurisdiction `PENDING_CONTEXT` with `SECTOR_REGULATED`; priority `P1`; status `TAXONOMY_ACCEPTED_NOT_IMPLEMENTED`. Dependencies: `SOURCE`.

## Triggers

A legal, regulatory, standards, or guidance claim depends on whether its cited source is current for a specified activity date.

## Non-Triggers

Generic link checking without a regulatory claim, automatic legal interpretation, selecting a workplace regime without context, or reproducing protected standards.

## Required Inputs

- Source identifiers and publishers.
- Claim scope.
- Version/effective dates.
- Current retrieval evidence.

## Optional Inputs

Earlier snapshots, amendment tables, commencement notices, official gazettes, language versions, incorporation or contract evidence, and rights metadata.

## Assumptions

A successful page load, recent retrieval date or unchanged URL does not prove the cited version is current or applicable. Publication, amendment, commencement, consolidation and access dates differ. Supplied applicability and source assessments are evidence to inspect, not authority to approve a dependent conclusion.

## Core Workflow

1. Record the exact claim, obligation, jurisdiction/sector, requested as-of date, publisher, instrument identifier and cited version. Missing claim/date returns NEEDS_INPUT.
2. Retrieve the authoritative current or point-in-time record. Capture version, amendment and displayed consolidation date, commencement notes, access/verification date and official-language identity.
3. Compare the cited version with applicable effective and supersession evidence. A publisher currency date before the requested date leaves a verification gap unless later official evidence closes it; do not promote a record on reachability alone.
4. Separate source_status from applicability_state and rights. Preserve conflicts between official records; secondary summaries are discovery only and protected text requires authorized access.
5. Return a per-claim verification record, unsupported intervals, specific recheck action and owner. Reverification creates a new current record without overwriting historical evidence.

## Calculations

Date ordering only with unambiguous dates. Do not invent an expiry interval, infer effectivity from publication, or calculate a confidence score.

## Validation

Use AM-07 source states CURRENT, CURRENT_ON_ACCESS, HISTORICAL, SUPERSEDED, STALE, UNKNOWN, CONFLICTING, PENDING_REVIEW. CURRENT requires authority/version/effective evidence tied to the requested date. All blocking states preserve SOURCE_REVIEW_REQUIRED for dependent current claims. Trace each finding to supplied evidence or a scoped source; keep absence distinct from contradiction.

## Exception Handling

Missing evidence returns `NEEDS_INPUT` or a bounded `PARTIAL` inventory. Unresolved authority or coverage returns `JURISDICTION_REVIEW_REQUIRED`; stale, conflicting or unverified sources return `SOURCE_REVIEW_REQUIRED`. Requests for publication, certification or a legal opinion return `OUT_OF_SCOPE` with qualified review. Continue unrelated supported work.

## Source Usage

Read [the review notes](references/review-notes.md) for source entry points and the boundary example. Repository source records are in [AM-26 source records](../../../docs/architecture/am26-federal-source-records.json), with [source evidence](../../../docs/development/AM-26-source-evidence.md). Use official law for legal obligations and distinguish guidance from law. Verify at the requested activity date and cite publisher, title, URL, source class, version/effective or currency note, access date, and applicability basis. Preserve rights; do not reconstruct protected text.

## Output Contract

Return `status`, scope, supplied evidence, assumptions, source_key, claim_scope, as_of, access_result, source_status, verification_date, version_or_currency_note, effective_evidence, applicability_state, rights, unsupported_interval, review_owner_or_handoff, validation notes and next owner. Allowed statuses: `PARTIAL`, `NEEDS_INPUT`, `SOURCE_REVIEW_REQUIRED`, `JURISDICTION_REVIEW_REQUIRED`, `OUT_OF_SCOPE`. Record source and applicability states separately from output status. There is no approval status.

## Safety Requirements

AM-05 class: `REGULATED`. No compliance certification, legal opinion, operating permission, claim publication, or automatic exemption. Escalate unresolved dependent decisions to the qualified regulatory/legal or workplace safety owner. Evidence review does not establish safe operation.

## References

- [Review notes](references/review-notes.md).
- [Canadian jurisdiction model](../../../docs/architecture/canadian-jurisdiction-model.md).
- [Source freshness policy](../../../docs/architecture/source-freshness-policy.json).

## Examples

An official page loads today but its supplied cited edition was superseded. Mark that citation SUPERSEDED and the dependent review SOURCE_REVIEW_REQUIRED. Record the newer edition separately; neither the page load nor a newer edition proves site applicability.

## Testing

Cover the frozen acceptance case, missing context, incorrect invocation, unsupported assumptions, source conflicts and output structure using the AM-26 scenarios. Expected routing is not observed behavior. Runtime model evaluation remains `NOT_RUN`.
