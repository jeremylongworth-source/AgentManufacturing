"""Inspect planned sector coverage; never infer applicability or run a skill."""
import argparse
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]

def assess(request, registry):
    if not isinstance(request, dict) or not isinstance(request.get("sector_dependent"), bool):
        raise ValueError("sector_dependent must be an explicit boolean")
    labels = request.get("labels")
    if not isinstance(labels, list) or any(not isinstance(x, str) or not x.strip() for x in labels):
        raise ValueError("labels must be a list of nonempty canonical names")
    labels = list(dict.fromkeys(x.strip() for x in labels))
    candidates = {r["id"]: r for r in registry["candidates"]}
    unknown = [x for x in labels if x not in candidates]
    known = [candidates[x] for x in labels if x in candidates]
    needs_context = not labels or any(r["kind"] in {"umbrella_alias", "operating_mode"} for r in known)
    # This inspector supports the planned baseline only. Promotion needs a new evaluated contract.
    if any(r["implementation_path"] is not None or r["status"] not in {"PLANNED_NOT_IMPLEMENTED", "CONTEXT_REQUIRED", "GENERIC_MODE_ONLY"} for r in known):
        raise ValueError("Registry exceeds the supported planned-coverage contract")
    if not request["sector_dependent"]:
        status = "GENERIC_METHOD_ONLY"
    elif needs_context:
        status = "NEEDS_INPUT"
    else:
        status = "COVERAGE_GAP"
    return {
        "status": status, "requested_labels": labels, "unknown_labels": unknown,
        "generic_analysis_allowed": True, "sector_conclusion_supported": False,
        "candidate_records": [{"id": r["id"], "kind": r["kind"], "status": r["status"], "scope_questions": r["scope_questions"]} for r in known],
        "research_handoff": "Clarify product/process, market, jurisdiction and requested requirement; obtain scoped authoritative evidence and a qualified reviewer.",
        "execution": "NOT_EXECUTED", "applicability": "NOT_ASSESSED",
    }

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("labels", nargs="*")
    parser.add_argument("--generic-only", action="store_true", help="Requested conclusion has no sector dependency")
    args = parser.parse_args()
    try:
        registry = json.loads((ROOT / "specializations/registry.json").read_text(encoding="utf-8"))
        result = assess({"labels": args.labels, "sector_dependent": not args.generic_only}, registry)
    except (OSError, ValueError, KeyError, TypeError) as exc:
        print(json.dumps({"status": "ERROR", "message": str(exc)}), file=sys.stderr)
        return 1
    print(json.dumps(result, indent=2))
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
