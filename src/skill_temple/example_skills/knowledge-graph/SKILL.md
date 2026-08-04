---
name: knowledge-graph
description: "Add learnable knowledge to the personal learning system or build, extend, validate, and repair a prerequisite knowledge graph. Use when the user wants to turn notes, a course, syllabus, book, or concept into observable skill nodes; add prerequisite relationships; update course targets; re-mine edges; or audit graph quality. Do not use for ordinary reference-note capture that is not intended for practice or mastery."
---

# Learning Knowledge Graph

Use this Skill for knowledge the user intends to **learn, practise, retain, or prove**. Ordinary articles, meeting notes, project records, and reference material remain normal Obsidian notes unless the user explicitly wants them converted into learnable skills.

## Locate the learning Vault

Do not assume a fixed machine path. Inspect the Workspace and locate the Vault by its markers, normally:

- `START_HERE.md`
- `templates/Skill Note.md`
- `.engine/prerequisite_edges.json`
- `flow_diagnostic.py`
- `scripts/graph_pipeline/`

The Workspace may be the Vault itself or may contain a `vault/` child. Use the discovered path consistently. Run Python commands from the directory containing the engine scripts.

## Core model

A learnable skill is one root Markdown file named:

```text
<number> - <slug>.md
```

The numeric prefix is the stable graph ID. Lettered checkboxes are observable subskills and the unit of mastery/SRS tracking.

Use `templates/Skill Note.md` when available. Required concepts include:

```yaml
exercise: 42
name: "Create and cancel an asyncio task"
domain: "Programming"
topic: "Python concurrency"
mastery: not-started
tags: [not-started, skill]
prerequisites: []
leads-to: []
implicit_review: []
```

New skills start as `not-started` unless the user supplies evidence for a different state.

## Workflow

1. **Inspect before creating.** Search existing skill titles, IDs, aliases, topic indexes, and nearby reference notes. Reuse or extend an existing node when it represents the same observable capability.
2. **Define the outcome.** A node should answer “what can the learner demonstrably do?” Avoid chapter-sized nodes, vague concepts, and pure definitions unless recall of that definition is itself the intended skill.
3. **Create subskills.** Add a small set of checkable behaviors. Split a node when its subskills require substantially different prerequisites or assessment methods.
4. **Assign a stable ID.** Follow the existing ID convention. Never reuse an ID belonging to another node. Ignore `00 -` system notes; ID 0 is reserved for dashboards and indexes.
5. **Create or patch the note.** Preserve useful source links and connect the skill to supporting reference notes without copying entire source documents into the skill node.
6. **Add typed edges.** Canonical edges live in `.engine/prerequisite_edges.json` and are mirrored into note frontmatter:
   - `HARD_PREREQ`: must be usable first; gates Flow Zone.
   - `SOFT_PREREQ`: helpful but not gating.
   - `IMPLICIT_REVIEW`: practising the dependent naturally rehearses the earlier skill.
7. **Update navigation and course scope.** Patch topic indexes, `00 - Master Index.md`, and `config/course_catalog.json` only when the new skill belongs in those views or course targets.
8. **Validate.** Run the graph and engine checks appropriate to the change.

## Edge rules

Direction is prerequisite to dependent:

```text
from = prerequisite
to   = dependent
```

Every edge needs a concise reason. Add a HARD edge only when inability in the source skill would materially block learning or performing the target skill.

Reject or fix:

- cycles;
- dangling IDs;
- duplicate edges;
- A→C when a clear HARD path A→B→C already expresses the dependency;
- excessive fan-in caused by a node that is too broad;
- “related to” relationships mislabeled as prerequisites;
- duplicate skill notes created for different courses instead of one canonical node with multiple course overlays.

Cross-domain edges are allowed and often valuable, but require the same evidence standard.

## Batch construction from a source

For a course, syllabus, book, PDF, or existing note collection:

1. establish the source of truth and desired scope;
2. normalize candidates to `{id, name, domain, topic, subskills[]}`;
3. review granularity before generating many files;
4. generate notes in a small batch first;
5. mine prerequisite candidates in bounded batches while providing a compact master index;
6. merge, deduplicate, cycle-check, reduce transitive HARD edges, and inspect cross-domain edges;
7. apply validated edges and update course targets;
8. run final verification and inspect the resulting Flow Zone for a beginner and a partially progressed learner.

Do not silently turn every source heading into a skill. References may support many skills without becoming graph nodes themselves.

For a worked example built from an official exam specification and companion PDFs,
read `references/tmua-vault-case-study.md` only when that pattern is relevant.

## Validation commands

Discover available scripts rather than inventing paths. In the integrated engine these normally include:

```powershell
python scripts/verify_engine.py
python scripts/graph_pipeline/prereq_batch_processor.py --stats
python flow_diagnostic.py --markdown
python study_today.py --top 12
```

After bulk generation, also verify unique positive IDs, frontmatter shape, edge parity, zero cycles, zero dangling IDs, and a sensible Flow Zone.

## Completion report

Report:

- created and updated skill paths;
- IDs and observable outcomes;
- added or changed edges with reasons;
- course/index changes;
- validation results;
- any candidate edges or source ambiguities left for review.
