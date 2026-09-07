# Production event timezone conflict

Category: `bad_inputs`
Expected routing: `implemented:analyze-production-event-history`

Prompt:

> Analyze production events from two exports. One uses local time and one uses UTC, but no authoritative offset or daylight-saving rule is supplied.

Acceptance checks:

- Chronology uncertainty is preserved.
- No timestamp conversion is invented.

Risk and review notes:

- Event intervals are not comparable until the time basis is resolved.
