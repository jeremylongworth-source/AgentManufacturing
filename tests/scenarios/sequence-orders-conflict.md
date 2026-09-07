# Sequence orders with a shared-resource conflict

Category: `correct_invocation`
Expected routing: `implemented:sequence-production-orders`

Prompt:

> Sequence two existing orders due in the same window when both require the same machine. Use the supplied priorities, routing durations, availability, and changeover matrix. Return a non-overlapping proposal or infeasibility; do not dispatch or release the orders.

Acceptance checks:

- No shared resource is assigned overlapping work.
- Due-date, priority, duration, and changeover conflicts remain visible.
- The output is a proposal rather than a dispatch command.

Risk and review notes:

- The planner must resolve any infeasibility before live scheduling.
