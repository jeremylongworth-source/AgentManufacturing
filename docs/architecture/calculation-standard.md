# AM-08 calculation standard

## Purpose and status

This standard defines how AgentManufacturing records, normalizes, calculates, rounds, validates, and reports quantitative manufacturing results. It applies before calculation skills scale. It is a calculation contract and evidence standard; it does not make a legal, safety, engineering, certification, permit, release, purchasing, staffing, or customer-commitment decision.

Status: `STANDARD_READY_NOT_IMPLEMENTED`.

The machine-readable contracts are [calculation-contract.json](calculation-contract.json) and [calculation-fixtures.json](calculation-fixtures.json). The [validator](../../scripts/validate-calculation-standard.py) checks the contracts and recomputes the reference fixture arithmetic with decimal precision. It does not test model behavior or prove that a process, asset, or metric is valid for a particular site.

## Calculation record

Every calculation record identifies:

- calculation ID and formula key;
- purpose, decision context, scope, time window, and owner or review handoff;
- variables with original value, original unit, source/origin, and quality note;
- normalized values and conversion factors;
- formula name and expression;
- assumptions, exclusions, and evidence limitations;
- intermediate values;
- raw result, rounded result, output unit, and rounding policy;
- validation checks, missing or contradictory inputs, and review flags; and
- source keys when the calculation depends on a source, standard, policy, or user-provided record.

The calculation result and an operational recommendation are separate fields. A numeric result does not authorize an action. A source or policy may define a threshold or interpretation, but it must be recorded through the AM-07 source and claim contract.

## Variables and units

Name every variable before using it. Preserve the user's original units and values, then show normalization when conversion occurs. Normalize only within a declared dimension:

| Dimension | Supported units | Canonical unit |
| --- | --- | --- |
| Count | `each`, `unit`, `piece`, `batch`, `failure` | `each` |
| Time | `s`, `min`, `h`, `day` | `s` |
| Length | `mm`, `cm`, `m`, `in`, `ft` | `mm` |
| Area | `mm2`, `cm2`, `m2`, `in2`, `ft2` | `mm2` |
| Mass | `g`, `kg`, `lb` | `kg` |
| Volume | `mL`, `L` | `L` |
| Temperature | `C`, `F`, `K` | `C`, with an offset-aware conversion | 
| Pressure | `kPa`, `MPa`, `psi` | `kPa` |
| Dimensionless | `ratio`, `percent` | `ratio` |

Time-per-count units such as `s/each` and `min/each` are valid compound units. A compound conversion must convert the time numerator and preserve the count denominator. Currency, case packs, pallets, density, and other business or physical conversions require supplied conversion data; they are never inferred from a label.

Reject unknown units and incompatible dimensions. Do not silently turn mass into volume, volume into count, time into output, temperature into a ratio, or a currency amount into a production rate. When inputs use different but compatible units, show the factor and normalized value before applying the formula.

## Formula contract

The formula is named and displayed before the result. Each variable has a meaning, unit or dimension, and evidence boundary. Hidden constants are prohibited. If a formula is a simplification, state what it excludes.

The reference set is:

| Formula | Definition | Output | Main boundary |
| --- | --- | --- | --- |
| Takt time | `available production time / required demand` | time per unit | Time window and demand window must match. |
| Gross capacity | `available production time / cycle time` | units | Theoretical output before downtime, speed loss, or scrap. |
| OEE | `availability × performance × quality` | ratio | Same asset, process, period, counts, and ideal cycle definition. |
| First-pass yield | `first-pass good count / units entering operation` | ratio | Reworked units are not first-pass good. |
| Scrap rate | `scrap count / units started` | ratio | Production boundary and scrap disposition must be declared. |
| MTBF | `operating time / failure count` | time per failure | Failure definition and observation window must be explicit. |
| MTTR | `corrective repair time / failure count` | time per failure | Repair start and stop rule must be explicit. |
| Cp | `(USL − LSL) / (6 × within sigma)` | ratio | Stable process evidence, specification limits, subgrouping, and sigma method are required. |
| Cpk | `min((USL − mean) / (3 × within sigma), (mean − LSL) / (3 × within sigma))` | ratio | Centering and within-process variation must be supported. |
| X-bar control limits | `center ± 3 × within sigma / sqrt(subgroup size)` | measurement unit | Chart type, subgrouping, center line, and sigma method must be recorded. |

For OEE, report the intermediate availability, performance, and quality values. For Cp and Cpk, report specification limits and the sigma method. For control limits, report the chart type and the baseline used. Control limits are not specification limits and do not prove capability.

## Assumptions

Assumptions must be stated before interpreting the result. Typical assumptions include:

- the measurement boundary, asset, product, and time window are consistent;
- counts use one declared counting rule;
- cycle time or ideal cycle time is supplied evidence, not a hidden default;
- planned exclusions, downtime, rework, scrap, and repair intervals are declared;
- specification limits come from an identified requirement and are not inferred from sample data;
- capability calculations have stable-process evidence and a declared subgroup/sigma method; and
- the observation period is representative, or the result is flagged as limited.

Do not invent a safety stock, demand rate, cycle time, specification, target, service level, failure definition, or process baseline. If a source, jurisdiction, policy, or standard controls interpretation, cite the AM-07 source key and claim location.

## Rounding and precision

Use exact arithmetic or sufficient precision for intermediate values. Round only the final value unless the formula itself requires stepwise rounding. The supported policies are `NONE`, `DECIMAL_PLACES`, `SIGNIFICANT_FIGURES`, `CEILING`, `FLOOR`, `NEAREST`, `INCREMENT`, and `ORDER_MULTIPLE`.

Countable operating quantities use an explicit rule. A capacity of `647.142857 each` may be reported with a ceiling operating threshold of `648 each`, but the raw value remains visible. Rates, percentages, ratios, cost per unit, and durations remain fractional unless a local policy says otherwise. The default display precision is two decimal places for percentages and four decimal places for ratios; this is display precision, not calculation precision.

## Missing inputs and edge cases

Validation must check missing inputs, unknown or incompatible units, negative values where impossible, zero denominators, contradictory records, stale or non-representative periods, outliers or unstable evidence, unmet formula assumptions, missing rounding policy for countable results, and unresolved source or jurisdiction dependencies.

Do not force a final numeric result. Return valid partial calculations, name the failed check, preserve supplied evidence, and show the review handoff. A zero denominator produces `NOT_APPLICABLE` or `REVIEW_REQUIRED`; it never produces infinity, zero, or an invented denominator. A missing OEE quality count can leave availability and performance as valid partial values while blocking OEE.

Examples of required handling:

| Condition | Result status | Required handling |
| --- | --- | --- |
| Missing required input | `PARTIAL` or `BLOCKED` | Show valid partial values, list the missing field, and request it. |
| Negative time, count, sigma, or cycle time where impossible | `INVALID_INPUT` | Reject the value and preserve the supplied input. |
| Zero denominator | `NOT_APPLICABLE` or `REVIEW_REQUIRED` | Explain the observation boundary and do not divide. |
| Mixed compatible units | `CALCULATED` | Normalize visibly and show the conversion. |
| Incompatible or unknown units | `INVALID_INPUT` or `BLOCKED` | Stop the dependent calculation. |
| Unstable process for Cp/Cpk/control limits | `REVIEW_REQUIRED` | Report arithmetic only if valid, without capability or control interpretation. |
| Stale source or policy | `REVIEW_REQUIRED` | Apply AM-07 freshness handling before an interpretation. |

## Reference calculation notes

### Takt time and capacity

Takt time describes the available time per required unit. Gross capacity describes theoretical units from available time and cycle time. They answer different questions. Gross capacity does not include downtime, speed loss, scrap, staffing constraints, changeover, material availability, or safety limits unless those factors are separately declared and calculated.

### OEE, FPY, and scrap

OEE combines availability, performance, and quality for one declared boundary. FPY counts units accepted without rework on the first pass. Scrap rate uses the declared scrap disposition and started-unit denominator. Do not substitute FPY for final yield, or scrap rate for rework rate, without recording the changed definition.

### MTBF and MTTR

MTBF and MTTR are descriptive metrics for a defined asset population and observation period. A zero failure count cannot produce a finite MTBF or MTTR. The output must preserve the observation window rather than implying infinite reliability or zero repair time.

### Cp, Cpk, and control limits

Cp measures specification width relative to within-process variation. Cpk also reflects process centering. Both require specification limits and a declared sigma method. X-bar control limits describe expected variation around a chart center line under the chosen chart assumptions. They do not replace specifications, legal limits, engineering acceptance criteria, or qualified statistical review.

## Worked fixtures

[calculation-fixtures.json](calculation-fixtures.json) contains sixteen fixtures covering:

- worked calculations for all ten reference formulas;
- time-unit conversion;
- missing OEE data;
- invalid negative sigma;
- zero-denominator FPY;
- countable capacity rounding; and
- expected units, intermediate values, raw values, final values, and tolerances.

Fixtures validate arithmetic and contract shape. They are not evidence that a formula is appropriate for a specific site, asset, product, or regulated decision.

## Output contract

Use this structure for calculation output:

```text
Status: <CALCULATED | PARTIAL | BLOCKED | INVALID_INPUT | NOT_APPLICABLE | REVIEW_REQUIRED>
Scope: <asset/process/product, boundary, and time window>

Inputs:
- <variable>: <original value> <original unit>; normalized: <value> <unit>

Formula:
- <formula name and expression>
- Intermediate values: <named values and units>

Result:
- Raw: <value> <unit>
- Rounded: <value> <unit>, policy: <policy>

Assumptions and validation:
- <assumption, failed check, source key, or evidence limitation>

Review or handoff:
- <owner, missing input, conflict, or qualified review requirement>
```

The output must preserve original inputs, normalization, formula, intermediate values, assumptions, validation notes, raw and rounded results, and review ownership. A calculation result must not be represented as a compliance determination, engineering approval, certification, permit, product release, restart authorization, purchase order, staffing decision, or customer promise.

## Acceptance scenarios

The standard requires coverage for:

1. correct formula and unit routing;
2. wrong or nearby calculation routing;
3. missing input with a valid partial result;
4. invalid negative or contradictory input;
5. unit conversion with visible normalization;
6. incompatible unit rejection;
7. zero denominator;
8. explicit rounding for a countable result;
9. stale or non-representative evidence;
10. unstable process evidence for capability or control limits;
11. expected output structure; and
12. safety, legal, engineering, certification, or operational authorization boundaries.

## Implementation boundary

AM-08 defines calculation records, unit dimensions, formulas, assumptions, precision, edge cases, and worked fixtures. AM-09 owns executable routing and validation framework behavior. AM-10 owns proof of five reference skills before mass authoring. AM-07 remains the source/freshness authority, AM-05 remains the safety boundary, and AM-06 remains the package/output contract.

## Completion token

```text
AGENTMANUFACTURING_AM_08_CALCULATION_STANDARD_READY
```
