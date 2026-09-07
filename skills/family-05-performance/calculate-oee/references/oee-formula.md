# OEE formula and evidence note

This local reference records the formula and evidence boundary for `calculate-oee`. The canonical calculation contract is [calculation-standard.md](../../../docs/architecture/calculation-standard.md); deterministic examples are in [calculation-fixtures.json](../../../docs/architecture/calculation-fixtures.json), including fixture `AM08-F05`.

Use one asset and one reporting period. Preserve the supplied definitions and units. Calculate `run_time` from planned production time minus stop time only when those terms are comparable. Then calculate availability, performance, quality, and OEE in that order. Keep every intermediate value and apply rounding only at the end.

Reject or request correction when good count exceeds total count, stop time exceeds planned time, a denominator is zero, or the evidence mixes periods or incompatible units. This reference does not reconcile MES events, determine downtime causes, or authorize a production action.

Source class: local project calculation contract. Permitted use: internal paraphrase and formula application. Review owner: AM-08 calculation standard maintainer. Recheck when the calculation contract or fixture set changes.
