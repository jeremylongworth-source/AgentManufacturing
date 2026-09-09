# Assess Product Of Canada Claim: review notes

Competition Bureau guidance retrieved 2026-09-08 distinguishes Product of Canada (at least 98% Canadian direct costs and last substantial transformation in Canada) from Made in Canada (51%, transformation and qualifying wording). These describe its general enforcement approach, not certification or a legal safe harbour. Reverify the exact guidance and scope at each claim review.

## Evidence handoff

Use source keys `AM26-ORIGIN` in the [source register](../../../../docs/architecture/am26-federal-source-records.json). The register stores bounded observations from 2026-09-08; it cannot satisfy a later claim without rechecking. Preserve a gap when authoritative currency does not cover the activity date.

## Boundary example

Only a prior Made in Canada assessment is supplied for proposed Product of Canada wording. Return NEEDS_INPUT for the claim-specific transformation and direct-cost substantiation, preserving the earlier assessment as evidence only.

## Reviewer check

Use the claim-specific source and transformation evidence. Do not substitute a Made in Canada threshold, round a near-threshold ratio into eligibility, or label an incomplete numerator as zero.
