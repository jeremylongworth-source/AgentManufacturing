"""Validate AM-33 audit traceability; a completed audit may defer release."""
import copy
import hashlib
import json
from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
GATES = {"taxonomy_coverage", "routing", "calculations", "canadian_sources", "standards_freshness", "quality", "safety", "provincial_isolation", "professional_skillsets", "specialization_boundaries", "integration", "documentation", "ci"}


def need(value, message):
    if not value:
        raise ValueError(message)


def read(path):
    return json.loads((ROOT / path).read_text(encoding="utf-8"))


def verdict(gates):
    states = {g["status"] for g in gates}
    need(states <= {"PASS", "PARTIAL", "FAIL"}, "unknown gate status")
    return "V1_BLOCKED" if "FAIL" in states else "V1_PARTIALLY_READY" if "PARTIAL" in states else "V1_READY"


def check_audit(audit):
    need(audit["schema_version"] == "AM-33-audit-1" and audit["audit_status"] == "COMPLETE", "audit identity")
    gates = audit["gates"]
    need(len(gates) == len(GATES) and {g["id"] for g in gates} == GATES, "roadmap audit coverage")
    need(audit["verdict"] == verdict(gates), "verdict contradicts gates")
    need(audit["publication"] == "NOT_AUTHORIZED", "publication authority")
    need(audit["independent_model_evaluation"] == "NOT_RUN", "unsupported model evidence")
    for gate in gates:
        if gate["id"] in {"routing", "quality", "safety", "integration"}:
            need(gate["status"] in {"PARTIAL", "FAIL"}, "unperformed behavioral evaluation marked passed")
    need(audit["release_recommendation"] == "DEFER_PUBLIC_V1", "release recommendation requires new review")
    for gate in gates:
        need(bool(gate["finding"]) and (ROOT / gate["evidence"]).is_file(), "missing gate evidence")
    need(len(audit["followups"]) >= 4, "follow-up coverage")
    for row in audit["followups"]:
        need(all(row.get(k) for k in ("id", "priority", "owner_role", "action", "closure")), "unactionable finding")


def check_workflow(workflow):
    need(workflow["permissions"] == {"contents":"read"}, "CI permissions")
    need(set(workflow["on"]) == {"push", "pull_request", "workflow_dispatch"}, "CI triggers")
    need(workflow["on"]["push"] == workflow["on"]["pull_request"] == {"branches":["main"]}, "CI branch scope")
    need(set(workflow["jobs"]) == {"validate"}, "unexpected CI jobs")
    job = workflow["jobs"]["validate"]
    need(job["timeout-minutes"] == 15 and job["runs-on"] == "${{ matrix.os }}", "CI runtime bounds")
    need(job["strategy"]["matrix"] == {"os":["ubuntu-latest", "windows-latest"]}, "CI host matrix")
    steps = job["steps"]
    need([s["uses"] for s in steps if "uses" in s] == ["actions/checkout@3d3c42e5aac5ba805825da76410c181273ba90b1", "actions/setup-python@5fda3b95a4ea91299a34e894583c3862153e4b97"], "CI pinned actions")
    need(steps[0]["with"]["persist-credentials"] is False, "persisted checkout authority")
    need(steps[1]["with"]["python-version"] == "3.14", "CI interpreter")
    need([s["run"] for s in steps if "run" in s] == ["python scripts/validate-all.py", "python scripts/validate-public-readiness.py --require-ready", "python tests/test_taxonomy_fingerprint.py", "git diff --check"], "CI command scope")


def check_sources(snapshot):
    need(len(snapshot["registers"]) == 6, "source inventory")
    count = 0
    for row in snapshot["registers"]:
        text = (ROOT / row["path"]).read_text(encoding="utf-8")
        need(hashlib.sha256(text.encode("utf-8")).hexdigest() == row["sha256"], "source snapshot changed; reassess")
        data = json.loads(text)
        records = data.get("records", data.get("sources", []))
        need(row["count"] == len(records), "source count")
        need(row["pending_keys"] == [r.get("source_key", r.get("key")) for r in records if r.get("status") == "PENDING_REVIEW"], "pending-source drift")
        if row["kind"] == "OPERATIONAL_REGISTER":
            count += len(records)
    need(count == 49, "operational register scope changed")


def main():
    audit = read("docs/development/am33-audit.json")
    workflow = read(".github/workflows/validate.yml")
    sources = read("docs/development/am33-source-inventory.json")
    check_audit(audit)
    check_workflow(workflow)
    check_sources(sources)
    readiness = read("docs/development/public-readiness.json")
    need(readiness["release_candidate_audit"] == "AM33_COMPLETE_PARTIAL", "AM-32 handoff audit status")
    need(read("tests/safety/am31-responses.json")["independent_runtime"] == "NOT_RUN", "runtime evidence drift")
    ci = read("docs/development/AM-33-ci-evidence.json")
    need(ci["branch_protection"]["status"] == "UNAVAILABLE_OBSERVED_403", "unsupported enforcement claim")
    for run in ci["runs"]:
        need(run["url"].endswith(str(run["id"])) and len(run["head_sha"]) == 40, "CI run provenance")
        need(run["conclusion"] in {"success", "failure", "pending"}, "CI result")
        if run["conclusion"] == "success":
            need(run["jobs"] == {"ubuntu-latest":"success", "windows-latest":"success"}, "unsupported CI success")
    # These reject misleading evidence claims, not unsafe natural-language output.
    bad = copy.deepcopy(audit); bad["verdict"] = "V1_READY"
    missing = copy.deepcopy(audit); missing["gates"].pop()
    write = copy.deepcopy(workflow); write["permissions"] = {"contents":"write"}
    unpinned = copy.deepcopy(workflow); unpinned["jobs"]["validate"]["steps"][0]["uses"] = "actions/checkout@main"
    stale = copy.deepcopy(sources); stale["registers"][0]["sha256"] = "0" * 64
    for check, value in [(check_audit,bad),(check_audit,missing),(check_workflow,write),(check_workflow,unpinned),(check_sources,stale)]:
        try:
            check(value)
        except ValueError:
            continue
        raise ValueError("invalid audit evidence accepted")
    result = subprocess.run([sys.executable, str(ROOT / "tests/test_taxonomy_fingerprint.py")], cwd=ROOT)
    need(result.returncode == 0, "checkout fingerprint regression")
    print("PASS: AM-33 13 audit areas, source inventory, bounded CI, five evidence rejection checks and three checkout regressions; V1_PARTIALLY_READY, public v1 deferred.")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (ValueError, KeyError, TypeError, OSError) as exc:
        print(f"FAIL: AM-33 {exc}", file=sys.stderr)
        raise SystemExit(1)
