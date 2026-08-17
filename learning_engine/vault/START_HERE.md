# Personal Learning OS

This Vault is intentionally empty. It contains the learning engine, GPT Skills,
configuration, templates, and state stores, but no demo subject and no inherited
study history.

## First setup

1. Open this `vault/` folder in Obsidian.
2. Start the GPT Action gateway with `WORKSPACE_ROOT` pointing to `learning_engine/`.
3. Give GPT a concrete first domain and source, for example:

   > Use the `knowledge-graph` Skill. Build my first learning graph for Python
   > concurrency from these notes and this course outline. Reuse existing notes,
   > create observable skill nodes, validate prerequisite edges, and update the
   > `personal` course profile.

4. After GPT creates the first numbered skill notes, run:

   ```powershell
   Set-Location vault
   python scripts/verify_engine.py
   python morning.py
   ```

5. Optionally start the local UI:

   ```powershell
   python cockpit_app.py
   ```

## What belongs in the graph

Create numbered skill notes only for abilities you intend to learn, practise, or
retain. Ordinary references, meetings, articles, and project notes may live in the
Vault without numeric filenames and are not treated as learning nodes.

A learning node uses the format:

```text
<number> - <slug>.md
```

Use `templates/Skill Note.md` as the schema. The numeric prefix is the stable graph
ID; subskill checkboxes are the units tracked by mastery and SRS.

## Daily commands

```powershell
python morning.py
python log_error.py <skill-id-or-context> "what went wrong"
python evening.py
```

Or ask GPT to use:

- `knowledge-graph` to add or reorganize learnable knowledge;
- `error-triage` to record and analyse mistakes;
- `vault-maintenance` for today's plan, mastery, FSRS, FIRe, and maintenance.

## Engine-owned and generated files

Do not manually maintain these during normal use:

- `.obsidian/srs_state.json`
- `.engine/prerequisite_edges.json`
- `00 - Flow Zone Diagnostic.md`
- `00 - Review Grader.md`
- `00 - SRS Review Tracker.md`
- generated files under `practice/` and `papers/`

The current clean state is expected to report zero skills and zero reviews until
your first knowledge graph is added.
