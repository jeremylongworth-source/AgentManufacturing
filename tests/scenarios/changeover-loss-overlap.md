# Changeover loss with overlapping tasks

Category: `calculation_correctness`
Expected routing: `implemented:analyze-changeover-loss`

Prompt:

> Analyze the supplied changeover timestamps and internal/external task observations. Two tasks overlap for ten minutes; show the overlap convention before summing the loss and keep improvement ideas separate from measured loss.

Acceptance checks:

- Expose the ten-minute overlap and avoid double counting.
- Preserve the approved baseline and event definitions.
- Do not authorize a safety-step reduction or improvement.

Risk and review notes:

- Overlap treatment changes the measured loss.
