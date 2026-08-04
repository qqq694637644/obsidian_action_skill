# Getting Started

The repository ships with a **clean personal Vault**. It contains the engine,
configuration, templates, and GPT Skills, but no demo subject, no inherited mastery,
no review history, and no question bank.

## Requirements

- Python 3.10+
- Obsidian
- the `obsidian_action_skill` gateway for GPT-driven operation
- Dataview is recommended for the index views

## 1. Verify the clean engine

```powershell
git clone https://github.com/qqq694637644/obsidian_action_skill
Set-Location obsidian_action_skill/learning_engine/vault
python scripts/verify_engine.py
python morning.py
```

`morning.py` should report zero learning nodes and zero reviews until you add your
first domain. This is expected.

Open `learning_engine/vault/` as an Obsidian Vault and read `START_HERE.md`.

## 2. Build the first learning domain with GPT Action

Run the gateway from the repository root with:

```dotenv
WORKSPACE_ROOT=C:/path/to/obsidian_action_skill/learning_engine
```

The gateway includes the learning Skills in its bundled Skill directory and compiles
their metadata into GPT Instructions:

- `knowledge-graph`
- `error-triage`
- `vault-maintenance`

Give GPT a concrete source and outcome:

> Use the `knowledge-graph` Skill. Build my first learning graph for Python
> concurrency from these notes and this course outline. Reuse existing notes,
> create observable skill nodes, validate the DAG, and add the resulting IDs to
> the `personal` course profile.

The build pipeline is:

1. Extract a curriculum or scope into `{id, name, domain, topic, subskills[]}`.
2. Generate numbered skill notes using `vault/templates/Skill Note.md`.
3. Mine and validate typed prerequisite edges.
4. Apply edges to note frontmatter and `.engine/prerequisite_edges.json`.
5. Update `config/course_catalog.json` and the Master Index.
6. Run `python scripts/verify_engine.py`, then `python morning.py`.

See `docs/02-build-pipeline.md` for the detailed methodology.

## 3. Daily loop

```powershell
Set-Location learning_engine/vault
python morning.py
python log_error.py <skill-id-or-context> "what went wrong"
python evening.py
```

The equivalent GPT requests are:

- “今天学什么？” → `vault-maintenance`
- “把这个概念加入学习系统” → `knowledge-graph`
- “记录这道错题” → `error-triage`
- “分析未处理的错题” → `error-triage`

## 4. Optional Learning Cockpit

```powershell
python cockpit_app.py
```

The Cockpit starts clean. The Today and Courses views work as soon as skill nodes
and course targets exist. Guided question sessions require your own
`papers/question_bank.json` or a configured bank in `config/course_catalog.json`.
There is no fallback demo question bank.

## 5. What belongs in this Vault

Numbered root notes are learnable skills:

```text
42 - async-task-lifecycle.md
```

Ordinary references, reading notes, meeting notes, project notes, and articles may
also live in the Vault, but without a numeric filename they are not interpreted as
learning nodes.

Cumulative subjects such as mathematics, science, programming, and professional
skills fit prerequisite graphs best. Flat domains can still use the FSRS portion
without forcing artificial HARD prerequisite edges.

## Optional pipelines

- Past papers and question banks: `docs/05-paper-pipeline.md`
- Course overlays: `docs/09-course-overlays-and-learning-guide.md`
- Subject adapters: `docs/11-subject-adapters.md`
- Operational pitfalls: `docs/07-pitfalls.md`
