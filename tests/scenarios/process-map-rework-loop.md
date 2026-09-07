# Process map with rework loop

Category: `correct_invocation`
Expected routing: `implemented:map-manufacturing-process`

Prompt:

> Map the supplied operations from material receipt through final inspection. Inspection failure returns the unit to the earlier finishing operation; preserve that rework loop, decision point, start/end boundary, and unresolved transitions.

Acceptance checks:

- Show the rework loop returning to the supplied earlier operation.
- Keep branch criteria and process boundaries explicit.
- Do not invent cycle times, capacity, or operating instructions.

Risk and review notes:

- Flattening the loop would misrepresent the process.
