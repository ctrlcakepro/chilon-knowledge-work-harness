# Codex Harness Public

Codex Harness Public 是一套面向长期知识工作的分层 Codex harness，适合用于可复用工作流、项目启动、项目级协作规范生成，以及多项目知识工作的持续沉淀。它的目标不是把 Codex 变成一次性的聊天助手，而是让它更像一套可以反复调用、可以跨项目迁移、也可以逐步校准的工作系统。

Codex Harness Public is a layered Codex harness for long-term knowledge work, reusable workflows, project bootstrapping, project-specific collaboration rules, and sustained multi-project knowledge work. Its goal is not to make Codex behave like a one-off chat assistant, but to turn it into a reusable working system that can be applied across projects, carried forward over time, and calibrated through repeated use.

## 仓库内容 / What This Repository Includes

这个仓库包含三类核心内容。`AGENTS.md` 提供全局协作规则、任务路由原则、交付标准和可靠性边界；`knowledge-workbench/` 提供一套模块化知识工作台，用于承载模板、playbook、风格指引、质量门槛、评分、校准和基准测试流程；`skills/project-harness-bootstrap/` 则是一项可复用 skill，可以把一段项目描述转化为项目根目录下的 harness 文件，例如 `AGENTS.md` 和 `PROJECT-WORKFLOW.md`。

This repository contains three core parts. `AGENTS.md` defines global collaboration rules, task-routing principles, delivery standards, and reliability boundaries. `knowledge-workbench/` provides a modular workbench for reusable knowledge-work routines, including templates, playbooks, style guidance, quality gates, scoring, calibration, and benchmark routines. `skills/project-harness-bootstrap/` is a reusable skill that turns a project description into project-root harness files such as `AGENTS.md` and `PROJECT-WORKFLOW.md`.

## 这个 Harness 想解决什么 / What This Harness Tries To Do

这套 harness 的核心思路是把全局层保持得尽可能小而稳定，把复杂、细碎、重复出现的工作流下沉到可复用模块里，而不是不断堆进顶层提示词。它希望帮助 Codex 减少模糊追问，更直接地推进任务，同时在写作、审阅、展示、结构化知识工作和项目启动等场景中保持较稳定的输出质量。

The core idea of this harness is to keep the global layer small and stable, while moving detailed and recurring workflows into reusable modules instead of bloating top-level instructions. It is designed to help Codex ask fewer vague questions, move work forward more directly, and preserve output quality across writing, review, presentation, structured knowledge work, and project bootstrapping.

同时，它也希望让新项目的启动更轻量。你只需要给出项目目标、重复任务、主要交付物、偏好的工具和需要确认的边界，就可以快速生成一个可用的项目级 harness，让 Codex 在该项目中拥有更明确的工作方式。

It also aims to make new project setup lighter. With a short description of the project goal, recurring tasks, main deliverables, preferred tools, and confirmation boundaries, you can quickly generate a usable project-level harness that gives Codex a clearer way to work inside that project.

## 架构 / Architecture

这套 harness 采用分层结构。第一层是全局层，由 `AGENTS.md` 承担，负责保存跨项目稳定生效的规则，例如协作风格、任务路由、交付预期和可靠性约束。它应该尽量短、稳定、可长期维护。

This harness uses a layered structure. The first layer is the global layer, handled by `AGENTS.md`. It stores stable cross-project rules such as collaboration style, task routing, delivery expectations, and reliability constraints. This layer should stay compact, stable, and easy to maintain over time.

第二层是 workbench 层，由 `knowledge-workbench/` 承担。它保存可复用的工作组件，包括用于常见输出结构的 `templates/`，用于路由、交付、质量控制和失败恢复的 `playbooks/`，用于审美方向和风格转换的 `style/`，用于规则优先级、评分和 harness 治理的 `architecture/`，以及用于校准和回归检查的 `benchmarks/`。

The second layer is the workbench layer, handled by `knowledge-workbench/`. It stores reusable building blocks, including `templates/` for common output structures, `playbooks/` for routing, delivery, quality control, and failure recovery, `style/` for aesthetic direction and style translation, `architecture/` for rule precedence, scoring, and harness governance, and `benchmarks/` for calibration and regression checks.

第三层是项目层。每个项目都可以根据自己的实际目标、输出形式和重复工作流，在项目根目录中定义自己的 `AGENTS.md` 和 `PROJECT-WORKFLOW.md`。这样，全局规则负责稳定性，项目规则负责具体性，workbench 则提供可复用的中间能力。

The third layer is the project layer. Each project can define its own root-level `AGENTS.md` and `PROJECT-WORKFLOW.md` based on its actual purpose, output formats, and recurring workflows. In this structure, the global layer provides stability, the project layer provides specificity, and the workbench provides reusable intermediate capabilities.

## 适合谁使用 / Who This Is For

如果你经常用 Codex 做知识工作、写作与改写、研究与审阅、展示文稿准备、多项目工作流搭建，或者希望和 agent 进行长期协作，那么这个仓库会比较有用。它尤其适合那些不想每次都重新解释工作方式，而是希望把协作习惯、质量标准和常见流程沉淀下来的使用场景。

This repository is most useful if you use Codex for knowledge work, writing and revision, research and review, presentation or deck preparation, multi-project workflow setup, or long-term collaboration with an agent. It is especially useful when you do not want to re-explain your working style every time, and instead want to preserve collaboration habits, quality standards, and recurring workflows in a reusable form.

## 安装 / Installation

把这些文件复制到你的 Codex home directory 中即可。推荐目录结构如下：

Copy the files into your Codex home directory. The recommended layout is:

```text
~/.codex/
  AGENTS.md
  knowledge-workbench/
  skills/
    project-harness-bootstrap/
```

建议按下面的顺序安装：先把 `AGENTS.md` 复制到 `~/.codex/AGENTS.md`，再把 `knowledge-workbench/` 复制到 `~/.codex/knowledge-workbench/`，最后把 `skills/project-harness-bootstrap/` 复制到 `~/.codex/skills/project-harness-bootstrap/`。如果你已经有自己的全局 `AGENTS.md`，不要直接覆盖，应该先仔细合并两边内容。

Install the files in this order: first copy `AGENTS.md` to `~/.codex/AGENTS.md`, then copy `knowledge-workbench/` to `~/.codex/knowledge-workbench/`, and finally copy `skills/project-harness-bootstrap/` to `~/.codex/skills/project-harness-bootstrap/`. If you already have your own global `AGENTS.md`, do not overwrite it blindly; merge the contents carefully instead.

## 快速开始 / Quick Start

安装完成后，全局 harness 会开始影响 Codex 在各个项目中的行为。对于一个新项目，你可以用 bootstrap skill，并提供一段简短的项目描述，让它在项目根目录中生成对应的 harness 文件。

After installation, the global harness will shape Codex behavior across projects. For a new project, use the bootstrap skill with a short project description so it can generate the corresponding harness files in the project root.

```text
用 $project-harness-bootstrap 根据下面这段项目描述，在项目根目录生成 AGENTS.md 和 PROJECT-WORKFLOW.md。

这个项目是做……
核心重复任务有……
主要交付物有……
希望优先使用的工具有……
需要确认的边界有……
```

```text
Use $project-harness-bootstrap to create a project-root harness from this project description.

This is a research and writing project about...
The recurring tasks are...
The main deliverables are...
The preferred tools are...
Actions that require confirmation are...
```

## Bootstrap Skill 会生成什么 / What The Bootstrap Skill Generates

默认情况下，bootstrap skill 会创建或更新两个文件。`AGENTS.md` 是项目专用的 Codex harness，用来改变 Codex 在该项目中的行为；`PROJECT-WORKFLOW.md` 则是面向人的快速上手文档和工作流地图，方便你理解并维护这个项目的协作方式。

By default, the bootstrap skill creates or updates two files. `AGENTS.md` is the project-specific Codex harness that changes Codex behavior inside that project. `PROJECT-WORKFLOW.md` is a human-readable quickstart and workflow map that helps you understand and maintain the collaboration pattern for the project.

这个 skill 的设计目标是继承全局规则、避免重复复制全局 harness、让项目说明保持紧凑，并尽快把项目描述转化为可以实际使用的工作流。

The skill is designed to inherit your global rules, avoid duplicating the global harness, keep project instructions compact, and quickly turn project descriptions into usable workflows.

## 仓库结构 / Repository Structure

```text
codex-harness-public/
  AGENTS.md
  README.md
  knowledge-workbench/
    architecture/
    benchmarks/
    playbooks/
    questioning/
    style/
    templates/
  skills/
    project-harness-bootstrap/
      SKILL.md
      agents/
      references/
```

## 设计原则 / Design Principles

这套 harness 的设计原则是：全局层要小，项目工作流要贴合项目本身；能通过路由解决的，不要反复写重复规则；能沉淀成 playbook 的，不要塞进冗长的顶层提示词；交付标准要明确，不要只写模糊的“高质量”；与其不断增加规则，不如建立修复循环、校准方法和 benchmark。

The design principles behind this harness are: keep the global layer small, keep project workflows specific to the project, prefer routing over repetition, prefer reusable playbooks over long top-level prompts, prefer explicit delivery standards over vague quality language, and prefer repair loops, calibration routines, and benchmarks over endlessly adding more rules.

## 不包含什么 / What Is Not Included

这个公开版本会刻意排除私人本地状态和敏感配置，例如个人配置文件、认证文件、插件缓存、会话数据、本地数据库、API keys，以及与特定机器绑定的自动化脚本。这些内容不适合出现在公开仓库中，也不应该和可复用 harness 混在一起。

This public package intentionally excludes private local state and sensitive configuration, such as personal config files, auth files, plugin caches, session data, local databases, API keys, and machine-specific automations. These materials do not belong in a public repository and should not be mixed into a reusable harness package.

## 建议的下一步 / Suggested Next Steps

如果你准备把这个项目发布成自己的公开仓库，可以考虑继续补充 examples、`CHANGELOG.md`、项目描述示例，以及由 bootstrap skill 生成的项目级 harness 示例。这样读者会更容易理解它的使用方式，也更容易判断这套结构是否适合自己的工作流。

If you plan to publish this as your own repository, consider adding examples, a short `CHANGELOG.md`, sample project descriptions, and example project-level harness outputs generated by the bootstrap skill. These additions will make it easier for readers to understand how the harness is used and decide whether this structure fits their own workflow.
