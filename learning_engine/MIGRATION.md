# Migration Record

The `learning_engine/` directory was imported from:

- Repository: `qqq694637644/obsidian-learning-engine`
- Source commit: `9b4e15ed02201f87e68ef316df26b0b3bacb4f39`
- Imported into: `qqq694637644/obsidian_action_skill`

The original directory structure is retained under this directory:

- `vault/` contains the clean personal Obsidian vault, engine scripts, templates, and the original learning Skills.
- `docs/` contains the learning-engine handbook.
- `automation/` contains the optional watcher and multi-vault utilities.

Integration-specific changes in the destination repository are intentionally small:

1. The Action gateway loads the original `knowledge-graph`, `error-triage`, and `vault-maintenance` Skills alongside its general Obsidian Skills.
2. The documented Action workspace root is `learning_engine/`; learning-engine commands change directory to `vault/` before execution.
3. Gateway prompt, configuration examples, tests, and Skill descriptions describe the integrated paths and routing.
4. `vault/micro_bridge.py` has its `from __future__ import annotations` statement in the valid module position so the migrated study planner can load it.
5. The Algebra demo nodes, demo question bank, inherited SRS history, and demo micro-trainer progress were removed; engine verification now uses a temporary synthetic fixture.

The source repository remains the provenance for the imported implementation. Future development in this repository should update the integrated copy directly or perform another explicit, reviewable synchronization.
