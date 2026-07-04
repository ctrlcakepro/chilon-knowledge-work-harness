# Chilon for Claude Desktop

Chilon for Claude Desktop is a lightweight adapter pack that turns the Chilon knowledge-work harness into something Claude Desktop users can set up without Codex.

它不是重新做一套新项目，而是把 Chilon 的核心结构转换成 Claude Desktop 更容易使用的形式：项目指令、可上传知识文件、工作流说明和交付风格约定。适合阅读、总结、复习、论文提纲、文档改写、汇报准备和长期学习协作。

## What You Get

- `project-instructions.md` — paste into Claude Project instructions.
- `custom-instructions.md` — a shorter version for personal Claude custom instructions.
- `import-files/workflow-guide.md` — upload as project knowledge to describe default workflows.
- `import-files/memory-guide.md` — upload as project knowledge to explain what should be remembered or updated.
- `import-files/delivery-style.md` — upload as project knowledge to keep outputs usable and finished-feeling.

## Recommended Setup

1. Create a new Claude Project, for example `Chilon Knowledge Work`.
2. Copy the content of `project-instructions.md` into the Project instructions field.
3. Upload the files in `import-files/` as Project Knowledge.
4. Start with a real task, such as summarizing a chapter, planning a paper, or refining a document.

## When to Use This Adapter

Use this adapter when you want Claude Desktop to behave less like a one-off chatbot and more like a stable knowledge-work partner. It is especially useful when your work repeats across many sessions: reading notes, course materials, literature summaries, paper drafts, comparison tables, presentation outlines, and document revision.

## Difference from the Codex Edition

The Codex edition is the full Chilon harness. It includes local project files, governance scripts, regression cases, and automation-oriented maintenance.

The Claude Desktop adapter is lighter. It focuses on instructions and importable knowledge files. It does not try to reproduce Codex automation, local scripts, or repository-level maintenance inside Claude Desktop.

## First Test Prompt

After setup, try this:

```text
Use the Chilon workflow. Help me turn this material into study notes. First identify the topic, main structure, key concepts, and likely exam points, then produce a concise review version I can continue using.
```
