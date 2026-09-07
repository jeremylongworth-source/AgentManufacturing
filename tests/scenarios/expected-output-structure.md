# OEE output structure request

Category: `expected_output_structure`
Expected routing: `implemented:calculate-oee`

Prompt:

> Prepare an OEE result for one asset and one shift. Include status, scope, original inputs and units, normalized values, formula, intermediate availability/performance/quality, raw and rounded result, assumptions, validation notes, source or evidence references, and the review handoff.

Acceptance checks:

- Every declared output field is present or explicitly marked unavailable.
- Original and normalized units remain distinguishable.
- The result does not claim approval, compliance, certification, or production authorization.

Risk and review notes:

- Output structure is checked as invariants; exact prose is not required.
- The scenario checks the reference package contract; expected routing is not observed model behavior.
