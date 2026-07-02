---
name: project-harness-bootstrap
description: Create or refresh a project-specific Codex harness from a user-supplied project description. Use when the user asks to generate a project's AGENTS.md, project harness, workflow file, project rules, startup scaffold, or reusable working style for a new or existing project, especially when the files should be written into the project root.
---

# Project Harness Bootstrap

Create a project-root harness that fits the specific project while inheriting the user's global Codex behavior.

## Default deliverables

By default, create or update these files in the target project root:

1. `AGENTS.md`
2. `PROJECT-WORKFLOW.md`

If the user explicitly asks for only one file, follow that narrower scope.

`AGENTS.md` is the durable machine-facing harness.  
`PROJECT-WORKFLOW.md` is the human-readable workflow map and quickstart.

Before writing either file, read `references/output-contract.md`.

## Step 1: Locate the target project root

1. Use an explicitly supplied project path first.
2. Otherwise use the current workspace root.
3. Treat a single-folder workspace as the project root even when it is not a Git repository.
4. If there are multiple plausible roots and the difference matters, ask one concise question.

## Step 2: Inspect before writing

Always inspect these before making project files:

1. Global `~/.codex/AGENTS.md`
2. Existing project-root `AGENTS.md` if present
3. Existing `PROJECT-WORKFLOW.md` if present
4. A small set of high-signal project files such as `README`, proposal, spec, syllabus, notes, or current file list

Do not broadly read unrelated files.

Your main job is to separate:

- global stable rules
- project-specific workflow
- temporary task context

Do not duplicate global rules unless the project intentionally overrides them.

## Step 3: Clarify only the missing project-shaping facts

If the user already gave enough description, proceed directly.

Ask questions only when the missing information would materially change:

- the project's role
- the recurring workflows
- the main deliverables
- the tool surface
- the safety boundary

If you must ask, do it in one short batch and prefer options.

Useful things to pin down:

- What kind of project this is
- What repeatable jobs it must handle
- What outputs matter most
- Which tools or files it should prefer
- What actions require confirmation

## Step 4: Classify the project before drafting

Classify the project into one primary archetype and, if needed, one secondary archetype.

Read `references/project-archetypes.md` when:

- the project description is broad
- the project mixes research, writing, coding, design, or operations
- you need help deciding which workflows belong in `AGENTS.md`

Do not try to make every project share one giant workflow. Keep only the workflows that are stable for this project.

## Step 5: Write the two root files

### A. `AGENTS.md`

Write a compact project-specific harness that changes Codex behavior inside this project.

Use direct instructions addressed to Codex.

Only include sections that materially help this project, such as:

- project purpose and scope
- Codex's role in this project
- core recurring workflows
- output conventions
- source or evidence rules
- file and folder conventions
- confirmation and safety boundaries

Keep it operational:

- replace vague aspirations with observable behavior
- use verified paths and filenames only
- prefer short workflow bullets over long essays
- keep project-specific rules in the project layer
- keep global preferences out unless this project overrides them

### B. `PROJECT-WORKFLOW.md`

Write a quickstart map for the human and the agent to align on how this project runs.

This file should explain:

- what this project is trying to do
- what the main workstreams are
- what a typical request should turn into
- what the common deliverables are
- how to start work quickly inside this project

Prefer practical structure over prose. Include example request shapes when useful.

## Step 6: Update surgically when files already exist

If the target file already exists:

1. Preserve useful project-specific content.
2. Integrate new rules into the right section instead of appending duplicates.
3. Remove obvious overlap with the global harness.
4. Do not replace the whole file unless it is clearly just a rough stub or the user asked for a rewrite.

## Step 7: Quality checks before finishing

Before delivering, confirm:

1. The files were written to the correct project root.
2. The project `AGENTS.md` does not repeat the global harness unnecessarily.
3. The workflows are project-specific rather than generic.
4. The instructions are actionable and not just aspirational.
5. The main deliverables and confirmation boundaries are clear.
6. The harness is compact enough to stay readable and maintainable.

## Editing rules

- Use `apply_patch` for manual edits.
- Preserve the existing file language when practical.
- Default to Chinese for this user unless the project clearly runs in another language.
- Do not modify the global `~/.codex/AGENTS.md` while using this skill.
- Do not create extra documentation files beyond the requested harness and workflow unless the user explicitly asks.

## Finish

Report briefly:

1. Which root files were created or updated
2. The core workflows now defined
3. Any assumptions that still need confirmation
