# Identify Manufacturing Jurisdiction: review notes

Use the federal workplace list as a discovery aid for undertaking and Code-part questions. It is not a test based on product sales or a legal classification service. A territory entry concerning one Code part must not be generalized to every workplace obligation.

## Evidence handoff

Use source keys `AM26-WORKPLACE` in the [source register](../../../../docs/architecture/am26-federal-source-records.json). The register stores bounded observations from 2026-09-08; it cannot satisfy a later claim without rechecking. Preserve a gap when authoritative currency does not cover the activity date.

## Boundary example

A Quebec plant cites a federal product label rule as proof that its workers fall under federal safety rules. Preserve Quebec as location, retain the product source, and leave workplace regime PENDING_CONTEXT pending undertaking evidence.

## Reviewer check

Check every stated jurisdiction against supplied facts. Do not replace unknown employer activity with a guessed province or federal default.
