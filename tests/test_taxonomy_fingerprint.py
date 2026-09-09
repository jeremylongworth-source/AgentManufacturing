"""Regression for the Linux CI failure against AM-03's frozen Windows hash."""
import importlib.util
import json
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("taxonomy", ROOT / "scripts/validate-taxonomy.py")
taxonomy = importlib.util.module_from_spec(spec)
spec.loader.exec_module(taxonomy)


class DraftFingerprintTests(unittest.TestCase):
    def setUp(self):
        self.raw = (ROOT / "docs/architecture/candidate-register-v0.1.json").read_bytes()
        self.expected = json.loads((ROOT / "docs/architecture/taxonomy-index.yaml").read_text(encoding="utf-8"))["draft_sha256"]

    def test_linux_checkout_matches_frozen_hash(self):
        self.assertEqual(taxonomy.draft_fingerprint(self.raw.replace(b"\r\n", b"\n")), self.expected)

    def test_windows_checkout_matches_frozen_hash(self):
        windows = self.raw.replace(b"\r\n", b"\n").replace(b"\n", b"\r\n")
        self.assertEqual(taxonomy.draft_fingerprint(windows), self.expected)

    def test_content_change_does_not_match(self):
        self.assertNotEqual(taxonomy.draft_fingerprint(self.raw.replace(b'"', b'X', 1)), self.expected)


if __name__ == "__main__":
    unittest.main()
