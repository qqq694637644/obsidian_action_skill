---
name: error-triage
description: "Capture a learning mistake quickly or analyse pending entries in the personal Error Log. Use when the user asks to record a wrong answer, save what went wrong, classify mistakes, identify root causes or prerequisite gaps, detect repeated error patterns, update weak spots, or decide whether an FSRS Again grade is warranted."
---

# Learning Error Triage

Use this Skill for mistakes made while practising a learnable skill. Keep capture fast; defer deep analysis unless the user asks for it or requests a session review.

## Locate the learning Vault

Do not assume a fixed path. Find the Vault using markers such as `00 - Error Log.md`, `log_error.py`, `.engine/prerequisite_edges.json`, and `00 - Weak Spots Priority.md`. The Workspace may be the Vault itself or contain it as a child directory.

## Quick capture

When the user only asks to record a mistake:

1. identify the skill ID, note, question, or context if available;
2. preserve the user's own description of what happened;
3. run the existing capture command from the engine directory when available:

```powershell
python log_error.py <id-or-context> "<what happened>"
```

Optional flags may include screenshot, severity, or an explicit FSRS `Again`, but do not infer punitive grading from a simple slip. If no capture script is available, append one clearly marked `#unanalyzed` entry to the existing Error Log without rewriting history.

After a quick capture, report the saved entry and stop. Do not force a full triage pass.

## Deferred triage

For each pending `#unanalyzed` entry:

1. read the complete entry and any linked screenshot or working;
2. identify the affected skill and inspect its prerequisite chain when relevant;
3. classify the error as one of:
   - `Slip`: knowledge was present; execution was careless;
   - `Procedural bug`: a known method was applied systematically incorrectly;
   - `Concept gap`: the underlying idea is absent or wrong;
   - `Prerequisite gap`: an upstream skill caused the failure;
   - `Strategy blank`: the learner could not choose an approach;
   - `Misread`: the task or condition was interpreted incorrectly;
4. write a specific root cause, not a generic label;
5. add one concise corrective rule or practice action;
6. link the exact prerequisite skill when evidence supports it;
7. remove `#unanalyzed` only after the entry is complete.

Do not invent details missing from the user's record. Mark uncertainty explicitly.

## Pattern and propagation rules

Compare new entries with prior errors. Treat the same failure on the same skill more than once, or the same rule violation across skills, as a pattern worth surfacing.

Update `00 - Weak Spots Priority.md` only for evidence-backed recurring issues, concept gaps, or prerequisite gaps that should affect future planning. Keep it short and actionable.

An FSRS `Again` grade may be appropriate for a genuine retrieval failure or prerequisite failure. A one-off slip does not automatically justify it. When grading was not explicitly requested, present the exact grade command and rationale before changing review state.

## Verification

After edits:

- reread the changed Error Log entries;
- ensure analysed history was not deleted or rewritten;
- confirm any linked skill note exists;
- confirm weak-spot links use the actual file stem or stable ID;
- run the relevant maintenance or diagnostic command when study state changed.

## Completion report

For capture, report the saved location and whether it remains pending triage.

For analysis, report the number of entries triaged, type breakdown, repeated patterns, prerequisite gaps, weak-spot changes, any FSRS action, and the highest-leverage corrective action.
