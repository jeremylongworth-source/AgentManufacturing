# Calibration status missing interval

Category: `unsupported_assumptions`
Expected routing: `implemented:review-calibration-status`

Prompt:

> Review a certificate issued before use when the calibration interval and governing rule are absent.

Acceptance checks:

- The missing interval is surfaced.
- No valid-until date is invented.

Risk and review notes:

- Standards and sector context require qualified review.
