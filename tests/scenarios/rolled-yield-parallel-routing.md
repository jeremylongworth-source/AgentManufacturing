# Rolled yield with parallel alternatives

Category: `incorrect_invocation`
Expected routing: `implemented:calculate-rolled-throughput-yield`

Prompt:

> Combine the supplied first-pass yields. The routing diagram shows two parallel alternative operations, not sequential steps; reject the sequential multiplication and request the routing interpretation.

Acceptance checks:

- Identify the parallel-versus-sequential conflict.
- Do not multiply the parallel alternatives as if they were sequential.
- Preserve the routing review handoff.

Risk and review notes:

- Rolled yield depends on routing structure and population basis.
