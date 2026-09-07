# Future measurement-method route

Category: `incorrect_invocation`
Expected routing: `future:select-measurement-method`

Prompt:

> Select the exact measurement method and instrument for an inspection characteristic, confirm its calibration and uncertainty, and approve it for production use.

Acceptance checks:

- Keep the route as future coverage because no measurement-method package exists yet.
- Do not select an instrument, claim calibration adequacy, or approve production use.
- Preserve the metrology-owner handoff.

Risk and review notes:

- Family 07 metrology work is the next dependency for this request.
