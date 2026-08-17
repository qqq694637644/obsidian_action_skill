#!/usr/bin/env python3
"""Map learning-graph skills to optional micro-schema fluency drills.

The clean personal Vault starts with no mappings. Configure
`config/micro_schema_map.json` after adding a subject adapter:

{
  "exercise_to_schemas": {"42": ["schema_id"]},
  "topic_hints": [{"pattern": "keyword", "schemas": ["schema_id"]}]
}

Usage:
  python micro_bridge.py
  python micro_bridge.py --for 42 43
  python micro_bridge.py --list
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(errors="replace")

VAULT = Path(__file__).resolve().parent
CONFIG_PATH = VAULT / "config" / "micro_schema_map.json"


def load_mapping() -> tuple[dict[int, list[str]], list[tuple[str, list[str]]]]:
    try:
        raw = json.loads(CONFIG_PATH.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        raw = {}

    by_id: dict[int, list[str]] = {}
    for key, value in (raw.get("exercise_to_schemas") or {}).items():
        try:
            exercise_id = int(key)
        except (TypeError, ValueError):
            continue
        schemas = [str(item).strip() for item in value or [] if str(item).strip()]
        if schemas:
            by_id[exercise_id] = schemas

    hints: list[tuple[str, list[str]]] = []
    for item in raw.get("topic_hints") or []:
        pattern = str(item.get("pattern", "")).strip()
        schemas = [str(value).strip() for value in item.get("schemas") or [] if str(value).strip()]
        if pattern and schemas:
            hints.append((pattern, schemas))
    return by_id, hints


EXERCISE_TO_SCHEMAS, TOPIC_HINTS = load_mapping()


def schemas_for(exercise_id: int, name: str = "") -> list[str]:
    if exercise_id in EXERCISE_TO_SCHEMAS:
        return list(EXERCISE_TO_SCHEMAS[exercise_id])
    low = (name or "").lower()
    for pattern, schemas in TOPIC_HINTS:
        try:
            matched = re.search(pattern, low, re.IGNORECASE)
        except re.error:
            matched = pattern.lower() in low
        if matched:
            return list(schemas)
    return []


def suggest_for_ids(ids_with_names: list[tuple[int, str]]) -> list[dict]:
    out = []
    seen = set()
    for exercise_id, name in ids_with_names:
        schemas = schemas_for(exercise_id, name)
        if not schemas:
            continue
        key = (exercise_id, tuple(schemas))
        if key in seen:
            continue
        seen.add(key)
        command = "python micro_trainer/train.py " + " ".join(schemas) + " --count 20"
        out.append({
            "id": exercise_id,
            "name": name,
            "schemas": schemas,
            "cmd": command,
        })
    return out


def main() -> None:
    args = sys.argv[1:]
    if "--list" in args:
        if not EXERCISE_TO_SCHEMAS and not TOPIC_HINTS:
            print("No micro-schema mappings configured in config/micro_schema_map.json.")
            return
        for exercise_id in sorted(EXERCISE_TO_SCHEMAS):
            print(f"  {exercise_id:>4}: {', '.join(EXERCISE_TO_SCHEMAS[exercise_id])}")
        for pattern, schemas in TOPIC_HINTS:
            print(f"  /{pattern}/: {', '.join(schemas)}")
        return

    if "--for" in args:
        index = args.index("--for")
        ids = []
        for value in args[index + 1:]:
            if value.startswith("--"):
                break
            try:
                ids.append(int(value))
            except ValueError:
                pass
        for suggestion in suggest_for_ids([(number, "") for number in ids]):
            print(f"#{suggestion['id']}: {suggestion['schemas']} -> {suggestion['cmd']}")
        if not ids or not suggest_for_ids([(number, "") for number in ids]):
            print("No mapped drills for the requested skill IDs.")
        return

    sys.path.insert(0, str(VAULT))
    import flow_diagnostic as diagnostic

    exercises, _ = diagnostic.scan_vault()
    built = diagnostic.build_diagnostic(exercises, {})
    pairs = []
    for item in list(built.get("flow_zone", []))[:15] + list(built.get("stalled", []))[:10]:
        if isinstance(item, tuple) and len(item) >= 2:
            number, exercise = item[0], item[1]
            pairs.append((int(number), exercise.get("name", "")))

    suggestions = suggest_for_ids(pairs)
    print("=== MICRO-SCHEMA BRIDGE ===\n")
    if not suggestions:
        print("  (no subject-adapter mappings for current flow-zone items)")
        return
    for suggestion in suggestions:
        print(
            f"  #{suggestion['id']:<4} {suggestion['name'][:40]:<40} -> "
            f"{', '.join(suggestion['schemas'])}"
        )
        print(f"         {suggestion['cmd']}")


if __name__ == "__main__":
    main()
