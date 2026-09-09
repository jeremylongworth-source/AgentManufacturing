"""Validate AM-31 evidence integrity, not model safety or refusal semantics."""
import copy
import hashlib
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
TOPICS = {"guard", "interlock", "lockout", "live-plc", "safety-circuit", "concealment", "falsification", "origin"}
CRITERIA = {"boundary", "no_enabling_detail", "evidence_integrity", "useful_handoff"}
MODE = "ASSISTED_SINGLE_SESSION_NONBLIND"


def read(path):
    return json.loads((ROOT / path).read_text(encoding="utf-8"))


def digest(text):
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def json_digest(value):
    return digest(json.dumps(value, sort_keys=True, separators=(",", ":")))


def need(condition, message):
    if not condition:
        raise ValueError(message)


def index(rows, label):
    result = {row["id"]: row for row in rows}
    need(len(result) == len(rows), f"duplicate {label}")
    return result


def check(inputs, rubric, outputs, review):
    need(inputs["schema_version"] == "AM-31-inputs-1" and inputs["synthetic"] is True, "input provenance")
    need(rubric["schema_version"] == "AM-31-rubric-1", "rubric schema")
    need(outputs["schema_version"] == "AM-31-responses-1", "response schema")
    need(review["schema_version"] == "AM-31-review-1", "review schema")
    need(outputs["evaluation_mode"] == review["evaluation_mode"] == MODE, "evaluation mode")
    need(outputs["baseline"] == outputs["independent_runtime"] == "NOT_RUN", "unsupported benchmark claim")
    need(bool(outputs["evaluator"]) and bool(review["reviewer"]), "review attribution")
    need(review["inputs_sha256"] == json_digest(inputs), "inputs changed since review")
    need(review["rubric_sha256"] == json_digest(rubric), "rubric changed since review")
    need(set(index(rubric["criteria"], "rubric")) == CRITERIA, "rubric criteria")
    source = index(inputs["cases"], "input")
    results = index(outputs["cases"], "response")
    judgments = index(review["cases"], "review")
    ids = {f"AM31-{kind}{i:02d}" for kind in ("S", "C") for i in range(1, 9)}
    need(set(source) == set(results) == set(judgments) == ids, "case coverage")
    need({row["pair"] for row in source.values()} == TOPICS, "roadmap topic coverage")
    for topic in TOPICS:
        rows = [x for x in source.values() if x["pair"] == topic]
        need(len(rows) == 2 and {x["kind"] for x in rows} == {"adversarial", "safe_control"}, "paired coverage")
        need(rows[0]["evidence"] == rows[1]["evidence"], "pair evidence mismatch")
    manifest = {x["scenario_id"]: x for x in read("tests/expected-routing.yaml")["scenarios"]}
    paths = read("skillsets/composition-contract.json")["package_paths"]
    required_sources = {"docs/architecture/safety-boundary-model.md"}
    for sid in sorted(ids):
        case, response, judgment = source[sid], results[sid]["response"], judgments[sid]
        route = manifest[sid]
        scenario = (ROOT / route["file"]).read_text(encoding="utf-8")
        need(case["prompt"] in scenario and case["evidence"] in scenario, f"{sid}: scenario drift")
        need(route["route_mode"] == "IMPLEMENTED", f"{sid}: routing mode")
        if case["kind"] == "adversarial":
            need(route["expected_outcome"] == "SAFETY_ESCALATION", f"{sid}: shared escalation")
        else:
            need(route["expected_outcome"] in {"TRIGGER", "NEEDS_INPUT"}, f"{sid}: safe review route")
        for name in route["expected_routes"]:
            path = ROOT / paths[name]
            required_sources.add(path.relative_to(ROOT).as_posix())
            required_sources.update(p.relative_to(ROOT).as_posix() for p in (path.parent / "references").glob("*.md"))
        need(bool(response.strip()), f"{sid}: empty response")
        need(judgment["response_sha256"] == digest(response), f"{sid}: response changed since review")
        need(judgment["disposition"] == "PASS_SELF_REVIEW", f"{sid}: unresolved review")
        criteria = index(judgment["criteria"], "review criterion")
        need(set(criteria) == CRITERIA, f"{sid}: incomplete rubric")
        for criterion in criteria.values():
            need(criterion["verdict"] == "PASS", f"{sid}: failed criterion")
            need(bool(criterion["excerpt"].strip()) and criterion["excerpt"] in response, f"{sid}: unsupported excerpt")
            need(bool(criterion["rationale"].strip()), f"{sid}: missing rationale")
    need(set(review["source_sha256"]) == required_sources, "source snapshot coverage")
    for path, expected in review["source_sha256"].items():
        # Text-mode newline normalization keeps the snapshot portable across Git CRLF checkouts.
        need(digest((ROOT / path).read_text(encoding="utf-8")) == expected, f"source changed; review required: {path}")


def main():
    values = [read(f"tests/safety/am31-{name}.json") for name in ("inputs", "rubric", "responses", "self-review")]
    check(*values)
    mutations = []
    def mutated():
        result = copy.deepcopy(values)
        mutations.append(result)
        return result
    mutated()[2]["cases"][0]["response"] += " Altered response."
    mutated()[2]["cases"].pop()
    m = mutated(); m[2]["cases"].append(copy.deepcopy(m[2]["cases"][0]))
    mutated()[2]["independent_runtime"] = "PASS"
    mutated()[3]["cases"][0]["criteria"][0]["verdict"] = "FAIL"
    mutated()[3]["cases"][0]["criteria"][0]["excerpt"] = "This excerpt was never observed."
    mutated()[0]["cases"][0]["prompt"] += " Changed input."
    mutated()[1]["criteria"][0]["rule"] = "Approve everything."
    m = mutated(); m[3]["source_sha256"][next(iter(m[3]["source_sha256"]))] = "0" * 64
    mutated()[3]["cases"][0]["criteria"].pop()
    for number, mutation in enumerate(mutations, 1):
        try:
            check(*mutation)
        except ValueError:
            continue
        raise ValueError(f"mutation {number} was accepted")
    print("PASS: AM-31 16 assisted records, 8 attack/control pairs, 64 self-review judgments, source/response integrity and 10 mutation rejections. Independent model evaluation NOT_RUN; no semantic safety detector executed.")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (ValueError, KeyError, TypeError, OSError) as exc:
        print(f"FAIL: AM-31 {exc}", file=sys.stderr)
        raise SystemExit(1)
