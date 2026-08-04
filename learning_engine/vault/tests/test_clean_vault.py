import json
import re
import unittest
from pathlib import Path

import cockpit_engine as engine


VAULT = Path(__file__).resolve().parents[1]


class CleanVaultTests(unittest.TestCase):
    def read_json(self, relative: str):
        return json.loads((VAULT / relative).read_text(encoding="utf-8"))

    def test_starter_vault_has_no_numbered_skill_notes(self):
        numbered = [
            path.name
            for path in VAULT.glob("*.md")
            if (match := re.match(r"^(\d+)\s+-\s+", path.name))
            and int(match.group(1)) > 0
        ]
        self.assertEqual(numbered, [])

    def test_personal_state_starts_empty(self):
        self.assertEqual(self.read_json(".engine/prerequisite_edges.json"), [])
        self.assertEqual(self.read_json(".obsidian/srs_state.json")["reviews"], {})
        self.assertEqual(self.read_json("micro_trainer/progress.json"), {})
        self.assertEqual(self.read_json("config/causal_bridges.json"), {"edges": []})

    def test_no_demo_question_bank_or_fallback(self):
        self.assertFalse((VAULT / "papers" / "demo_question_bank.json").exists())
        self.assertEqual(engine.load_banks(), [])

    def test_cockpit_accepts_empty_personal_vault(self):
        catalog = self.read_json("config/course_catalog.json")
        self.assertIn("personal", catalog["profiles"])
        self.assertEqual(catalog["profiles"]["personal"]["target_inclusions"], [])
        self.assertEqual(engine.parse_nodes(), {})
        snapshot = engine.progress_snapshot()
        self.assertEqual(snapshot["target_nodes"], 0)
        self.assertEqual(snapshot["proficient"], 0)
        self.assertEqual(snapshot["mastered"], 0)

    def test_first_run_files_exist(self):
        for relative in (
            "START_HERE.md",
            "templates/Skill Note.md",
            "templates/Topic Index.md",
            "config/micro_schema_map.json",
        ):
            with self.subTest(relative=relative):
                self.assertTrue((VAULT / relative).is_file())


if __name__ == "__main__":
    unittest.main()
