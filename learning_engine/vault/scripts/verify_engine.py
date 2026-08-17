#!/usr/bin/env python3
"""Verify the learning engine without depending on live Vault content.

The repository ships with an intentionally empty personal Vault. This verifier
checks the live directory structure and JSON stores, then exercises graph,
mastery, Flow Zone, FIRe, and report rendering against a temporary synthetic
fixture. It never edits the user's live skill notes.
"""
from __future__ import annotations

import io
import json
import sys
import tempfile
from contextlib import contextmanager
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(errors="replace")

VAULT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(VAULT))

import flow_diagnostic as diagnostic


def check(name: str, condition: bool, detail: str = "") -> None:
    status = "PASS" if condition else "FAIL"
    print(f"{status:4}  {name}  {detail}")
    if not condition:
        raise SystemExit(1)


def read_json(path: Path, expected_type: type) -> object:
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        check(f"valid JSON: {path.relative_to(VAULT)}", False, str(exc))
        raise AssertionError("unreachable") from exc
    check(
        f"JSON shape: {path.relative_to(VAULT)}",
        isinstance(value, expected_type),
        f"expected {expected_type.__name__}",
    )
    return value


def skill_note(
    number: int,
    name: str,
    *,
    checked: bool,
    mastery: str,
    prerequisites: list[int] | None = None,
) -> str:
    prerequisites = prerequisites or []
    implicit = prerequisites
    mark = "x" if checked else " "
    return f"""---
exercise: {number}
name: "{name}"
domain: "Synthetic"
topic: "Verification"
mastery: {mastery}
tags: [{mastery}, skill]
prerequisites: {prerequisites}
leads-to: []
implicit_review: {implicit}
---
# {name}

#{mastery}
Mastery: **{mastery}**

- [{mark}] {number}a: Demonstrate {name.lower()}.
"""


@contextmanager
def use_diagnostic_vault(path: Path):
    old_vault = diagnostic.VAULT
    old_srs = diagnostic.SRS_FILE
    old_cache = diagnostic._RETRIEVAL_CACHE
    diagnostic.VAULT = path
    diagnostic.SRS_FILE = path / ".obsidian" / "srs_state.json"
    diagnostic._RETRIEVAL_CACHE = None
    try:
        yield
    finally:
        diagnostic.VAULT = old_vault
        diagnostic.SRS_FILE = old_srs
        diagnostic._RETRIEVAL_CACHE = old_cache


def verify_live_layout() -> None:
    required = [
        VAULT / "START_HERE.md",
        VAULT / "00 - Master Index.md",
        VAULT / "00 - Error Log.md",
        VAULT / "00 - Weak Spots Priority.md",
        VAULT / ".engine" / "prerequisite_edges.json",
        VAULT / ".obsidian" / "srs_state.json",
        VAULT / "config" / "course_catalog.json",
        VAULT / "config" / "causal_bridges.json",
        VAULT / "config" / "micro_schema_map.json",
        VAULT / "templates" / "Skill Note.md",
    ]
    for path in required:
        check(f"required path: {path.relative_to(VAULT)}", path.exists())

    edges = read_json(VAULT / ".engine" / "prerequisite_edges.json", list)
    srs = read_json(VAULT / ".obsidian" / "srs_state.json", dict)
    catalog = read_json(VAULT / "config" / "course_catalog.json", dict)
    read_json(VAULT / "config" / "causal_bridges.json", dict)
    read_json(VAULT / "config" / "micro_schema_map.json", dict)

    check("edge rows are objects", all(isinstance(row, dict) for row in edges))
    check("SRS reviews store exists", isinstance(srs.get("reviews", {}), dict))
    check("course profiles store exists", isinstance(catalog.get("profiles", {}), dict))

    exercises, topics = diagnostic.scan_vault()
    check("live Vault scan succeeds", isinstance(exercises, dict) and isinstance(topics, dict),
          f"({len(exercises)} skill nodes)")
    report = diagnostic.render_markdown_report(diagnostic.build_diagnostic(exercises, topics))
    check("empty/populated report renders", "Flow Zone" in report)


def verify_synthetic_engine() -> None:
    with tempfile.TemporaryDirectory() as temp_dir:
        root = Path(temp_dir)
        (root / ".obsidian").mkdir(parents=True)
        (root / ".obsidian" / "srs_state.json").write_text(
            json.dumps({"last_commit": None, "reviews": {}, "mastery_changes": {}}),
            encoding="utf-8",
        )
        (root / "1 - foundation.md").write_text(
            skill_note(1, "Foundation", checked=True, mastery="proficient"),
            encoding="utf-8",
        )
        (root / "2 - dependent.md").write_text(
            skill_note(
                2,
                "Dependent Skill",
                checked=False,
                mastery="not-started",
                prerequisites=[1],
            ),
            encoding="utf-8",
        )

        with use_diagnostic_vault(root):
            exercises, topics = diagnostic.scan_vault()
            check("synthetic scan finds two skills", len(exercises) == 2)
            check("synthetic mastery is already synchronized",
                  diagnostic.sync_exercise_mastery(exercises) == [])

            fire = diagnostic.compute_fire_scores(exercises, exercises)
            check("FIRe scores dependent skill", fire.get(2, {}).get("total_weight", 0) > 0)

            built = diagnostic.build_diagnostic(exercises, topics)
            flow_ids = {int(row[0]) for row in built.get("flow_zone", [])}
            check("Flow Zone unlocks dependent skill", 2 in flow_ids)
            check("diagnostic contains FIRe data", bool(built.get("fire_data")))

            report = diagnostic.render_markdown_report(built)
            for heading in ("FIRe Multiplier", "SRS Due Today", "Flow Zone", "Topic Mastery"):
                check(f"report section: {heading}", heading in report)

            changes = diagnostic.apply_fire_to_srs(
                exercises,
                srs_path=root / ".obsidian" / "srs_state.json",
            )
            check("FIRe handles empty review state", bool(changes))


def verify_entrypoints() -> None:
    compile(
        (VAULT / "fire_populate.py").read_text(encoding="utf-8"),
        "fire_populate.py",
        "exec",
    )
    check("fire_populate.py compiles", True)

    old_stdout = sys.stdout
    sys.stdout = io.StringIO()
    try:
        diagnostic.main()
        output = sys.stdout.getvalue()
    finally:
        sys.stdout = old_stdout
    check("terminal diagnostic runs", "Flow Zone" in output)


def main() -> None:
    verify_live_layout()
    verify_synthetic_engine()
    verify_entrypoints()
    print("\n" + "=" * 50)
    print("PASS: learning engine structure and synthetic behavior verified.")


if __name__ == "__main__":
    main()
