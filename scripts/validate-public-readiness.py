"""Check AM-32 documents and governance; --require-ready rejects open decisions.

Neither mode publishes a release, validates a mailbox or performs AM-33's audit.
"""
import argparse
import copy
import hashlib
import json
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
REQUIRED = {"README.md", "ROADMAP.md", "AGENTS.md", "CONTRIBUTING.md", "SECURITY.md", "CODE_OF_CONDUCT.md", "CHANGELOG.md", "LICENSE"}
MIT_DIGEST = "2b0bdd6e28883595b3a227644730ef9febc409746d910473effd50c8aff461b2"


def need(condition, message):
    if not condition:
        raise ValueError(message)


def read_json(path):
    return json.loads(path.read_text(encoding="utf-8"))


def assess(record, documents, licenses):
    need(record["schema_version"] == "AM-32-public-readiness-1", "readiness schema")
    need(set(record["required_documents"]) == REQUIRED and len(record["required_documents"]) == len(REQUIRED), "document inventory")
    need(set(documents) == REQUIRED and all(text.strip() for text in documents.values()), "missing/empty required document")
    license_record = record["license"]
    need(license_record["status"] == "SELECTED" and license_record["identifier"] == "MIT", "owner-selected licence")
    need(license_record["notice_only"] is False and bool(license_record["decision_record"]), "licence decision evidence")
    actual = hashlib.sha256(" ".join(documents["LICENSE"].split()).encode("utf-8")).hexdigest()
    need(actual == MIT_DIGEST, "MIT licence text differs from the adopted text")
    need(bool(licenses) and all(value == "MIT" for value in licenses.values()), "licence metadata drift")
    need(record["public_release"] == "NOT_AUTHORIZED", "publication boundary")
    need(record["release_candidate_audit"] in {"AM33_NOT_RUN", "AM33_COMPLETE_PARTIAL", "AM33_COMPLETE_BLOCKED", "AM33_COMPLETE_READY"}, "unsupported release audit claim")
    need(record["independent_model_evaluation"] == "NOT_RUN", "unsupported model evaluation claim")
    reporting = record["private_reporting"]
    blockers = []
    if reporting["status"] == "NOT_CONFIGURED":
        need(all(reporting[key] is None for key in ("contact", "recipient", "verification")), "unverified reporting metadata")
        need(all("NOT_CONFIGURED" in documents[p] for p in ("SECURITY.md", "CODE_OF_CONDUCT.md")), "reporting documents hide open decision")
        blockers.append("PRIVATE_REPORTING_NOT_CONFIGURED")
    elif reporting["status"] in {"OWNER_DESIGNATED", "GITHUB_VULNERABILITY_AND_CONDUCT_FORM"}:
        contact, recipient = reporting["contact"], reporting["recipient"]
        if reporting["status"] == "OWNER_DESIGNATED":
            need(isinstance(contact, str) and bool(re.fullmatch(r"[^\s@]+@[^\s@]+\.[^\s@]+", contact)), "private contact must be an owner-supplied email address")
        else:
            need(contact is None, "GitHub/form reporting must not publish a personal email contact")
            need(reporting.get("verification", {}).get("security_channel") == "GITHUB_PRIVATE_VULNERABILITY_REPORTING", "security channel")
            need(reporting.get("verification", {}).get("conduct_channel") == "https://conduct.pmgate.ai/", "conduct channel")
        need(isinstance(recipient, str) and recipient.strip(), "report recipient")
        verification = reporting["verification"]
        need(isinstance(verification, dict) and verification.get("basis") in {"OWNER_CONFIRMATION", "OWNER_CONFIRMATION_AND_GITHUB_SETTING"} and bool(verification.get("date")), "owner designation evidence")
        for path in ("SECURITY.md", "CODE_OF_CONDUCT.md"):
            need((contact is None or contact in documents[path]) and recipient in documents[path] and "NOT_CONFIGURED" not in documents[path], "reporting document/decision mismatch")
    else:
        raise ValueError("unsupported reporting state; do not infer availability from a URL")
    expected = "IN_PROGRESS" if blockers else "READY"
    need(record["status"] == expected, "readiness status contradicts evidence")
    return {"status": "NOT_READY" if blockers else "AM32_READY", "blockers": blockers, "publication": "NOT_AUTHORIZED", "AM33": record["release_candidate_audit"].removeprefix("AM33_")}


def load_evidence():
    record = read_json(ROOT / "docs/development/public-readiness.json")
    documents = {p:(ROOT / p).read_text(encoding="utf-8") for p in REQUIRED}
    licenses = {}
    packages = list((ROOT / "skills").glob("*/*/SKILL.md"))
    need(len(packages) == 161, "atomic package inventory")
    for path in packages + [ROOT / "docs/templates/manufacturing-skill/SKILL.md.template"]:
        match = re.search(r"^license:\s*(\S+)\s*$", path.read_text(encoding="utf-8"), re.MULTILINE)
        need(match is not None, f"missing licence: {path}")
        licenses[path.relative_to(ROOT).as_posix()] = match.group(1)
    roles = list((ROOT / "skillsets").glob("*/skillset.yaml"))
    need(len(roles) == 18, "role inventory")
    for path in roles + [ROOT / "skillsets/composition-contract.json"]:
        licenses[path.relative_to(ROOT).as_posix()] = read_json(path)["license"]
    licenses["authoring-schema"] = read_json(ROOT / "docs/architecture/skill-package-schema.json")["license_policy"]["current_project_status"]
    return record, documents, licenses


def regression_checks(record, documents, licenses):
    # Synthetic metadata only. A passing test fixture is not owner designation.
    pending = copy.deepcopy(record)
    pending["status"] = "IN_PROGRESS"
    pending["private_reporting"] = {"status":"NOT_CONFIGURED", "contact":None, "recipient":None, "verification":None}
    pending_docs = dict(documents)
    for path in ("SECURITY.md", "CODE_OF_CONDUCT.md"):
        pending_docs[path] = "NOT_CONFIGURED"
    need(assess(pending, pending_docs, licenses)["status"] == "NOT_READY", "pending state accepted as ready")
    ready = copy.deepcopy(pending)
    ready["status"] = "READY"
    ready["private_reporting"] = {"status":"OWNER_DESIGNATED", "contact":"reports@example.invalid", "recipient":"Synthetic owner", "verification":{"basis":"OWNER_CONFIRMATION", "date":"2026-09-09"}}
    ready_docs = dict(pending_docs)
    for path in ("SECURITY.md", "CODE_OF_CONDUCT.md"):
        ready_docs[path] = "Synthetic owner: reports@example.invalid"
    need(assess(ready, ready_docs, licenses)["status"] == "AM32_READY", "complete decision fixture rejected")
    mutations = []
    def changed():
        value = copy.deepcopy([pending, pending_docs, licenses])
        mutations.append(value)
        return value
    changed()[0]["status"] = "READY"
    changed()[1]["LICENSE"] = "MIT selected; complete text omitted."
    changed()[2][next(iter(licenses))] = "PENDING_PROJECT_GOVERNANCE"
    changed()[1].pop("SECURITY.md")
    changed()[0]["private_reporting"]["status"] = "VERIFIED_FROM_URL"
    changed()[0]["release_candidate_audit"] = "PASS"
    for value in mutations:
        try:
            assess(*value)
        except ValueError:
            continue
        raise ValueError("false readiness evidence accepted")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--require-ready", action="store_true")
    args = parser.parse_args()
    values = load_evidence()
    result = assess(*values)
    regression_checks(*values)
    print("PASS: AM-32 document/licence consistency, pending/complete decision fixtures and six rejection checks.")
    print(json.dumps(result))
    return 2 if args.require_ready and result["status"] != "AM32_READY" else 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (ValueError, KeyError, TypeError, OSError) as exc:
        print(f"FAIL: AM-32 {exc}", file=sys.stderr)
        raise SystemExit(1)
