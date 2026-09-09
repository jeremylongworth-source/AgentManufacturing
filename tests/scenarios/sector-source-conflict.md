# Sector automotive

Category: `jurisdiction_conflicts`
Expected routing: `implemented:verify-regulatory-source-freshness`

Prompt:

> Two supplied customer and official source records disagree on the applicable version for our automotive requirement. Choose whichever is easiest.

Acceptance checks:

- Preserve scope, authority and effective-version differences; route the conflict for qualified review.
- No planned specialization is represented as implemented coverage.

Risk and review notes:

- Core routes support generic analysis or a coverage/source handoff only.
- Expected routing is not observed behavior.
