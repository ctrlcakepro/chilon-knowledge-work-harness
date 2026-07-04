# Chilon Knowledge Work Harness

<p align="center">
  <b>A portable AI workbench for reading, writing, studying, summarizing, and long-term knowledge work.</b>
</p>

<p align="center">
  把 AI 从一次性聊天窗口，变成可复用、可维护、可迁移的知识工作台。
</p>

---

## Why Chilon

Chilon is for people who use AI for real knowledge work, not just quick answers. If you often ask an AI to read materials, summarize chapters, organize notes, plan papers, compare theories, prepare presentations, polish documents, or continue work across many sessions, you eventually run into the same problem: a single long prompt becomes messy, memory becomes unreliable, and every new task starts to feel like rebuilding the workspace from zero.

Chilon solves this by turning your AI workspace into a layered harness. The top layer stays light. Workflows, memory, reusable structures, delivery rules, regression cases, and maintenance scripts live in their own places. Instead of making one prompt longer and heavier, Chilon gives your AI a working structure that can keep producing usable outputs over time.

Chilon 不是一个“更长的提示词合集”。它是一套面向长期知识工作的 AI 工作台结构。它适合那些会反复发生的真实任务：读书、整理课堂材料、写论文、做摘要、搭提纲、准备汇报、修改文档、沉淀偏好、复用模板、检查交付质量。它的核心目标不是让模型一次说更多，而是让模型在有限上下文里，更稳定地交付可以继续使用的结果。

---

## What You Can Use It For

- Reading summaries and textbook review
- Study notes and concept cards
- Literature summaries and comparison tables
- Paper, assignment, and essay outlines
- Presentation and slides planning
- Document rewriting and polishing
- Reusable knowledge-work templates
- Long-term project memory and decision records
- AI workspace maintenance and regression checks

Chilon is especially useful when you do not want another vague answer. You want a structured note, a usable outline, a comparison table, a draft you can revise, or a workflow that remembers how you prefer to work.

---

## Editions

Chilon now has one primary edition and one lightweight adapter.

| Edition | Best for | What it includes |
|---|---|---|
| **Chilon for Codex** | Full local harness, repository-style AI workspace, automation-aware maintenance | `AGENTS.md`, `PROJECT-WORKFLOW.md`, `.project-memory/`, tools, regression cases, automation templates, installers |
| **Chilon for Claude Desktop** | Claude Project users who want a lighter setup for reading, writing, notes, and long-term study work | Project instructions, custom instructions, importable workflow / memory / delivery files |

The Codex edition is the full version. The Claude Desktop adapter is not a separate project; it is a portable version of the same Chilon idea for users who work mainly inside Claude Desktop.

---

## Quick Start

### Option 1: Use Chilon with Codex

Clone the repository and install the harness into your target project.

On Windows, the easiest way is to double-click:

```text
install.cmd
```

Or run manually:

```powershell
powershell -ExecutionPolicy Bypass -File .\install.ps1 -TargetDir "C:\path\to\your\project"
```

On macOS or Linux:

```bash
chmod +x ./install.sh
./install.sh --target /path/to/your/project
```

The installer copies the core harness files into your target project and backs up existing files before overwriting them.

### Option 2: Use Chilon with Claude Desktop

Open:

```text
adapters/claude-desktop/
```

Recommended setup:

1. Create a Claude Project, for example `Chilon Knowledge Work`.
2. Copy `adapters/claude-desktop/project-instructions.md` into the Project instructions field.
3. Upload the files under `adapters/claude-desktop/import-files/` as Project Knowledge.
4. Start with a real task, such as summarizing a chapter, planning a paper, or refining a document.

For a lighter non-project setup, copy `adapters/claude-desktop/custom-instructions.md` into Claude Desktop custom instructions.

---

## How It Works

Chilon is built around a simple idea: do not load everything all the time. Keep the stable rules close, keep the details organized, and only bring in what the current task needs.

### 1. Top Layer

`AGENTS.md` defines the basic collaboration protocol: task routing, output style, questioning boundaries, reliability rules, and default behavior. It should stay light and stable.

### 2. Workflow Layer

`PROJECT-WORKFLOW.md` maps common requests into repeatable workflows: reading summary, knowledge organization, comparison, writing, presentation planning, revision, fact checking, and file-style delivery.

### 3. Explicit Memory Layer

`.project-memory/` stores durable project context: user preferences, project state, decisions, reusable assets, delivery rules, capability routing, and knowledge cache. It is not meant to remember everything. It is meant to remember what will actually improve future work.

### 4. Governance Layer

`tools/check_harness.py` and `tools/auto_cold_layer_maintenance.py` help keep the harness from becoming heavy, inconsistent, or full of broken references. The point is not only to build a workspace, but to keep it maintainable.

### 5. Regression Layer

`harness-regression/` stores small cases and drills that help you check whether high-frequency behavior still works after changing rules or restructuring files.

---

## Project Structure

```text
.
├─ AGENTS.md
├─ PROJECT-WORKFLOW.md
├─ .project-memory/
│  ├─ README.md
│  ├─ user-preferences.md
│  ├─ project-state.md
│  ├─ decision-log.md
│  ├─ reusable-assets.md
│  ├─ tool-delivery-routing.md
│  └─ knowledge-cache/
├─ tools/
│  ├─ check_harness.py
│  └─ auto_cold_layer_maintenance.py
├─ harness-regression/
│  ├─ cases/
│  └─ drills/
├─ automations/
│  ├─ weekly-harness-maintenance.toml
│  └─ monthly-harness-deep-audit.toml
├─ adapters/
│  └─ claude-desktop/
│     ├─ README.md
│     ├─ project-instructions.md
│     ├─ custom-instructions.md
│     └─ import-files/
│        ├─ workflow-guide.md
│        ├─ memory-guide.md
│        └─ delivery-style.md
├─ install.ps1
├─ install.sh
└─ install.cmd
```

---

## Example Prompts

After installing Chilon, try requests like these:

```text
把这篇文章整理成适合复习的笔记。先给主线，再给关键概念、易混点和速记版。
```

```text
比较这两个理论。先列比较维度，再用表格整理，最后给适用场景判断。
```

```text
帮我把这份材料改成 8 分钟课堂汇报结构。重点是讲述顺序和每页主旨。
```

```text
检查这份文档是否像一个可提交版本。先指出主要问题，再给修改方向。
```

---

## Who This Is For

Chilon is built for individual users who rely on AI as a long-term study, research, writing, or knowledge-management partner.

It is especially suitable for:

- students and researchers
- writers and note-takers
- people building personal AI workflows
- users who work with textbooks, papers, documents, notes, and presentations
- anyone who wants their AI workspace to become more stable without becoming bloated

It is probably not the best fit if you only need occasional one-line answers or a fully automated production agent framework.

---

## Design Principles

- Keep the top layer light.
- Do not turn every idea into a global rule.
- Store durable context explicitly.
- Load only the context needed for the current task.
- Prefer usable outputs over process explanations.
- Treat memory as something to maintain, not something to blindly accumulate.
- Make the harness portable across AI workspaces where possible.

---

## Roadmap

- [x] Public Codex harness package
- [x] Claude Desktop adapter
- [ ] Cherry Studio adapter
- [ ] Fuller example workflows
- [ ] GitHub Actions health check
- [ ] Short demo walkthrough

---

## Why Star This Project

Star this project if you are interested in building AI workspaces that are lighter than full agent frameworks, more durable than one-off prompts, and more practical than vague productivity advice.

Chilon is an attempt to make everyday AI knowledge work more structured, more reusable, and easier to maintain.

---

## License

Use this project as a starting point for your own knowledge-work harness. Before publishing your own modified version, remove private paths, account information, local project state, and any personal material from `.project-memory/`.
