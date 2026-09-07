# Schedule adherence against a frozen baseline

Category: `unsupported_assumptions`
Expected routing: `implemented:analyze-schedule-adherence`

Prompt:

> Measure schedule adherence against frozen schedule version F-12 and the supplied completion events. A revised schedule R-13 would remove yesterday's lateness; keep F-12 as the baseline, show exclusions, and flag missing event evidence.

Acceptance checks:

- Use the frozen baseline and retain lateness visible under the revised schedule.
- Show numerator, denominator, exclusions, and missing events.
- Do not fabricate 100% adherence from a zero or changed denominator.

Risk and review notes:

- Baseline governance is required for a defensible adherence measure.
