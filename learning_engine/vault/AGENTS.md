# Learning Vault operator guide

Read this file before changing learning notes, graph edges, SRS state, diagnostics,
or study workflow behavior. The full handbook is in `../docs/`.

In the integrated GPT Action setup, `WORKSPACE_ROOT` points to `learning_engine/`.
Workspace file paths therefore start with `vault/`, and learning-engine commands
start with `Set-Location vault`.

## Current Vault state

This is a clean personal Vault. It intentionally contains:

- no numbered skill notes;
- no prerequisite edges;
- no SRS review history;
- no question bank;
- no inherited mastery or error data.

Do not recreate the removed Algebra demo. Build the user's real domains directly.
Read `START_HERE.md` for the human-facing first-run flow.

## Learning-node model

One root Markdown note per skill:

```text
<number> - <slug>.md
```

Lettered checkboxes are the unit of mastery and SRS. Use
`templates/Skill Note.md` as the schema. Canonical typed edges live in
`.engine/prerequisite_edges.json` and are mirrored into note frontmatter.

Only create a numbered node for an observable capability the user intends to learn,
practise, or retain. Ordinary references and project notes remain non-numbered.

## Common commands

```powershell
python scripts/verify_engine.py
python morning.py
python evening.py
python study_today.py --top 12
python srs_fsrs.py --stats
python srs_fsrs.py --due
python srs_fsrs.py --grader-note
python srs_fsrs.py --tracker
python flow_diagnostic.py --markdown
python flow_diagnostic.py --sync-mastery
python flow_diagnostic.py --apply-fire
python log_error.py <id-or-context> "what went wrong" [--shot] [--again] [--sev X]
python scripts/unlock_priority.py --top 20
python scripts/srs-backlog.py
python cockpit_app.py
```

Optional ID scoping is generic:

```powershell
python study_today.py --id-min 100 --id-max 999
python scripts/unlock_priority.py --id-min 100 --id-max 999
```

## Building or extending a domain

Use the `knowledge-graph` Skill and `../docs/02-build-pipeline.md`.

1. **Scope** — identify the user's source of truth and intended outcomes.
2. **Extract** — create curriculum JSON containing stable IDs, names, domains,
   topics, and observable subskills.
3. **Generate** — create notes matching `templates/Skill Note.md`.
4. **Mine edges** — generate typed prerequisite candidates in batches.
5. **Validate** — reject cycles, reduce redundant HARD paths, check dangling IDs,
   inspect cross-domain edges, and keep a one-sentence reason per edge.
6. **Apply** — update note frontmatter, edge JSON, topic indexes, and the course
   profile in `config/course_catalog.json`.
7. **Verify** — run `python scripts/verify_engine.py`, then `python morning.py`.

Do not mark newly generated skills mastered. A new personal graph starts with
`not-started` mastery and empty review history unless the user provides evidence.

## Mastery rules

Mastery is represented in four places:

1. `mastery:` frontmatter;
2. `tags:` frontmatter;
3. the body mastery tag such as `#not-started`;
4. `Mastery: **not-started**` display text.

`flow_diagnostic.py --sync-mastery` repairs these from checkbox truth. Completing all
checkboxes caps a skill at `proficient`; promotion to `mastered` requires delayed
Good/Easy retrieval evidence in FSRS history.

## Hard constraints

- Do not manually edit `.obsidian/srs_state.json` during normal operation.
- Do not regenerate `.obsidian/graph.json` while Obsidian is open.
- Do not hand-edit generated dashboard notes or generated `practice/*.md` files.
- Do not add a HARD prerequisite merely because two concepts are related.
- Do not duplicate a skill to satisfy multiple courses; use course profiles and
  overlays over one canonical graph.
- Keep personal question banks, renders, extracted PDFs, and Cockpit state in their
  existing gitignored locations.

## Daily workflow

Morning:

1. run `morning.py`;
2. grade due reviews honestly;
3. finish in-progress skills;
4. study the highest-leverage Flow Zone items;
5. run optional subject-specific micro drills only when configured.

During study, capture errors quickly with `log_error.py` or the `error-triage` Skill.
Do not interrupt the session with deep analysis.

Evening:

1. run `evening.py`;
2. triage `#unanalyzed` errors when appropriate;
3. let weak spots feed back into the next ranking.

## Cockpit configuration

The Cockpit is subject-neutral and starts without questions. Configure destinations,
question banks, assessment rubrics, error types, and optional routes in
`config/course_catalog.json`. Graph ancestors remain available as causal support
nodes even when they are not explicit course targets.

## Skills available to GPT

- `knowledge-graph` — add or reorganize learnable knowledge and validate the DAG;
- `error-triage` — capture mistakes and perform deferred root-cause analysis;
- `vault-maintenance` — daily planning, review grading, mastery, FSRS/FIRe, and upkeep.
