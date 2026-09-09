# Verify Regulatory Source Freshness: review notes

AM-07 uses VERIFY_AT_USE for law, registries and incorporated standards, and VERIFY_BEFORE_RELEASE for guidance and voluntary standards; recheck guidance before a dependent claim review as well. Justice landing pages accessed on 2026-09-08 display currency only to 2026-06-21. This is a gap for a current-date claim, not proof that the instruments changed or are repealed.

## Evidence handoff

Use source keys `AM26-HPR`, `AM26-HPA`, `AM26-CPLA`, `AM26-CPLR` in the [source register](../../../../docs/architecture/am26-federal-source-records.json). The register stores bounded observations from 2026-09-08; it cannot satisfy a later claim without rechecking. Preserve a gap when authoritative currency does not cover the activity date.

## Boundary example

An official page loads today but its supplied cited edition was superseded. Mark that citation SUPERSEDED and the dependent review SOURCE_REVIEW_REQUIRED. Record the newer edition separately; neither the page load nor a newer edition proves site applicability.

## Reviewer check

Use AM-07 source states CURRENT, CURRENT_ON_ACCESS, HISTORICAL, SUPERSEDED, STALE, UNKNOWN, CONFLICTING, PENDING_REVIEW. CURRENT requires authority/version/effective evidence tied to the requested date. All blocking states preserve SOURCE_REVIEW_REQUIRED for dependent current claims.
