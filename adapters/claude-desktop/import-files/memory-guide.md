# Memory Guide

This file explains how to treat long-term context in a Claude Desktop project using Chilon.

## Purpose

Chilon does not try to remember everything. It tries to preserve the few things that make future work better: stable preferences, project state, reusable structures, important decisions, and delivery standards.

## What Counts as Durable Memory

Keep something as project memory only when it will affect future sessions.

Good memory candidates:

- Stable output preferences
- Repeated formatting choices
- Long-term project goals
- Course, research, or writing state
- Reusable templates or structures
- Decisions that should not be re-litigated every time
- Common mistakes that should be avoided later

Poor memory candidates:

- One-off chat details
- Temporary examples
- Unverified facts
- Private credentials or account information
- Local absolute paths
- Old decisions that may expire

## How to Use Memory During a Task

1. Start from the user's current request.
2. Use project knowledge only when it is relevant.
3. Do not flatten all memory into every answer.
4. If continuing past work, restate the continuation point briefly.
5. If a preference or decision has changed, follow the latest explicit instruction.

## Suggested Claude Project Knowledge Files

For a real personal project, users can add files such as:

- `user-preferences.md`
- `project-state.md`
- `decision-log.md`
- `reusable-assets.md`
- `course-notes-index.md`
- `writing-style-guide.md`

Keep these files small and readable. A useful memory layer is not a dump of everything; it is a curated map for future work.
