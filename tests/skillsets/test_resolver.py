"""Meaningful resolver invariants; no model behavior tested."""
import importlib.util
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[2]
spec = importlib.util.spec_from_file_location("resolver", ROOT / "scripts/resolve-skillset.py")
resolver = importlib.util.module_from_spec(spec)
spec.loader.exec_module(resolver)

class ResolverTests(unittest.TestCase):
    def test_generic_workflow_does_not_add_overlay(self):
        r = resolver.resolve("industrial-engineering-specialist", "line-balance")
        self.assertFalse(r["explicit_overlays"])
        self.assertNotIn("identify-manufacturing-jurisdiction", [x["name"] for x in r["ordered_references"]])
        self.assertEqual(r["execution"], "NOT_EXECUTED")
        self.assertEqual(r["evidence_state"], "NOT_ASSESSED")

    def test_transitive_providers_precede_consumer(self):
        r = resolver.resolve("production-supervisor", "shift-plan")
        names = [x["name"] for x in r["ordered_references"]]
        self.assertLess(names.index("validate-bill-of-materials"), names.index("calculate-material-requirement"))
        self.assertLess(names.index("build-production-plan"), names.index("build-shift-production-plan"))

    def test_overlay_adds_research_not_applicability(self):
        r = resolver.resolve("production-planner", "horizon-plan", ["provincial"])
        self.assertIn("identify-provincial-safety-overlay", r["targets"])
        self.assertEqual(r["status"], "REFERENCES_RESOLVED")
        self.assertEqual(r["evidence_state"], "NOT_ASSESSED")

    def test_repeated_overlay_is_deduplicated(self):
        r = resolver.resolve("ehs-coordinator-support", "whmis-review", ["whmis", "whmis", "source"])
        names = [x["name"] for x in r["ordered_references"]]
        self.assertEqual(len(names), len(set(names)))
        self.assertEqual(r["explicit_overlays"], ["whmis", "source"])

    def test_nonselected_workflow_is_not_loaded(self):
        r = resolver.resolve("quality-engineer-support", "capability")
        self.assertNotIn("prepare-quality-release-package", r["targets"])

    def test_canonical_duplicate_paths(self):
        q = resolver.resolve("quality-engineer-support", "corrective-action")
        e = resolver.resolve("ehs-coordinator-support", "safety-review")
        self.assertIn("family-09-nonconformance-capa", next(x["path"] for x in q["ordered_references"] if x["name"] == "triage-nonconformance"))
        self.assertIn("family-11-manufacturing-safety", next(x["path"] for x in e["ordered_references"] if x["name"] == "review-lockout-program"))

    def test_unknown_role(self):
        with self.assertRaises(ValueError):
            resolver.resolve("../../outside", "anything")

    def test_unknown_workflow(self):
        with self.assertRaises(ValueError):
            resolver.resolve("production-planner", "release-live-orders")

    def test_unknown_overlay(self):
        with self.assertRaises(ValueError):
            resolver.resolve("production-planner", "horizon-plan", ["automatic-approval"])

    def test_unknown_dependency(self):
        with self.assertRaises(ValueError):
            resolver.dependency_order(["missing"], {})

    def test_cycle_rejected(self):
        data = {n: {"dependencies": {"evidence_reuse": [p]}} for n, p in [("a", "b"), ("b", "a")]}
        with self.assertRaises(ValueError):
            resolver.dependency_order(["a"], data)

    def test_path_escape_rejected(self):
        with self.assertRaises(ValueError):
            resolver.read(ROOT, "../outside.json")

if __name__ == "__main__":
    unittest.main()
