---
name: vault-maintenance
description: "Operate and maintain the personal learning Vault: produce today's study plan, process review grades, synchronize mastery state, maintain FSRS and FIRe, diagnose backlog or bad scheduling, regenerate dashboards, update course/index views, and run morning or evening workflows. Use when the user asks what to study, reports a review result, sees wrong mastery, or says the learning engine is inconsistent."
---

# Learning Vault Maintenance

Use this Skill for an existing learning Vault. Use `knowledge-graph` instead when the main task is creating or restructuring learnable knowledge.

## Locate the engine

Do not assume a fixed machine path. Find the directory containing `morning.py`, `srs_fsrs.py`, `flow_diagnostic.py`, and `.obsidian/srs_state.json`. The Workspace may be that directory or may contain it as a child.

Run commands from the engine directory. Use actual Workspace-relative paths in file Actions.

## Daily planning

For “what should I study today?” prefer the engine's current state over a plan invented from note titles.

Typical sequence:

```powershell
python morning.py
python study_today.py --top 12
```

Explain the returned priorities in terms of due review, unfinished work, Flow Zone readiness, weak spots, and unlock leverage. If the Vault is empty, say so and direct the user to `knowledge-graph` rather than fabricating tasks.

## Review grading

Use the engine's exact card or subskill key. Supported ratings are normally:

```text
Again | Hard | Good | Easy
```

Do not infer `Good` merely because a checkbox is checked. Grade based on the user's retrieval quality. Use the existing grade command, then regenerate the relevant state or reports.

A failure on a prerequisite can place downstream skills behind a relearning lock. Preserve this behavior unless the user explicitly requests an engine change.

## Mastery synchronization

Mastery may be represented in several places consumed by different parts of the system:

- `mastery:` frontmatter;
- frontmatter tags;
- body mastery tag;
- human-readable mastery line;
- subskill checkboxes and FSRS evidence.

Do not repair these copies independently when the engine provides a sync command. Prefer:

```powershell
python flow_diagnostic.py --sync-mastery
```

Checkbox completion alone normally caps a skill at `proficient`; `mastered` requires delayed successful retrieval evidence.

## FSRS and FIRe upkeep

Useful diagnostics typically include:

```powershell
python srs_fsrs.py --stats
python srs_fsrs.py --due
python scripts/srs-backlog.py
python fire_populate.py
python flow_diagnostic.py --apply-fire
```

Do not trust “0 due” alone. Check card counts, states, stability distribution, and due-date clustering before concluding the schedule is healthy.

`implicit_review` should be consistent with validated prerequisite relationships unless an intentional custom weight is documented. Do not grant implicit-review credit from a merely related skill.

## Catch-up planning

When the user is behind:

1. measure the real backlog and oldest due cohorts;
2. identify which weak prerequisites block unfinished skills;
3. rank ready new skills by direct unlock value;
4. preserve a small honest direct-review floor so FSRS remains calibrated;
5. treat a catch-up plan as a prioritized menu, not a rigid calendar unless the user requests scheduling.

Use generic ID scoping only when the user's course/profile requires it:

```powershell
python study_today.py --id-min 100 --id-max 999
python scripts/unlock_priority.py --id-min 100 --id-max 999
```

## Generated and manual files

Regenerate engine-owned dashboards rather than hand-editing them when commands exist. These commonly include Flow Zone, Review Grader, SRS tracker, and generated practice notes.

Human indexes, course profiles, and weak-spot summaries may require local edits, but preserve their current format and derive facts from actual skill nodes and engine output.

Do not manually edit `.obsidian/srs_state.json` during normal operation unless the task is an explicit migration or repair and the user has requested it.

## Validation

After maintenance, run the checks appropriate to the change. Typical commands:

```powershell
python scripts/verify_engine.py
python srs_fsrs.py --stats
python study_today.py --top 12
python evening.py
```

For a simple grade, a narrower verification is sufficient. For bulk edits or repairs, verify graph, mastery, review state, and generated outputs.

## Completion report

Report:

- commands run and their terminal status;
- files changed or regenerated;
- study/review state changes;
- diagnosed cause of any inconsistency;
- remaining backlog, uncertainty, or manual review needed.
