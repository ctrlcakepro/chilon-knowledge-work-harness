# Codex Harness Public / Codex 公共 Harness

**中文**：这是一个面向长期知识工作、可复用工作流、项目启动引导，以及项目级 `AGENTS.md` 生成的分层 Codex Harness。

**English**: A layered Codex harness for long-term knowledge work, reusable workflows, project bootstrapping, and project-specific `AGENTS.md` generation.

**中文**：本仓库提供了我的 Codex Harness 系统的公开版本。它的目标是让 Codex 不再只是一次性聊天助手，而是更像一个可复用、可迁移、适合多项目协作的工作系统。

**English**: This repository provides a public version of my Codex harness system. It is designed to make Codex behave less like a one-off chat assistant and more like a reusable, portable working system for collaboration across multiple projects.

## 这个仓库包含什么 / What This Repository Includes

- `AGENTS.md`
  - **中文**：全局协作规则，包括任务路由原则、交付标准、可靠性边界和协作方式。
  - **English**: Global collaboration rules, including task-routing principles, delivery standards, reliability boundaries, and collaboration style.

- `knowledge-workbench/`
  - **中文**：面向重复性知识工作的模块化工作台，包含模板、剧本、风格指南、质量门、评分、校准和基准测试流程。
  - **English**: A modular workbench for recurring knowledge-work workflows, including templates, playbooks, style guidance, quality gates, scoring, calibration, and benchmark routines.

- `skills/project-harness-bootstrap/`
  - **中文**：一个可复用技能，可根据项目描述生成项目根目录下的 Harness 文件，例如 `AGENTS.md` 和 `PROJECT-WORKFLOW.md`。
  - **English**: A reusable skill that turns a project description into project-root harness files such as `AGENTS.md` and `PROJECT-WORKFLOW.md`.

## 这个 Harness 想解决什么 / What This Harness Tries To Do

- **中文**：保持全局层小而稳定。
  **English**: Keep the global layer small and stable.

- **中文**：把详细工作流下沉到可复用模块中，避免顶层指令膨胀。
  **English**: Push detailed workflows into reusable modules instead of bloating top-level instructions.

- **中文**：帮助 Codex 少问模糊问题，更直接地推进任务。
  **English**: Help Codex ask fewer vague questions and move work forward more directly.

- **中文**：在写作、审阅、演示文稿和结构化知识工作中维持稳定输出质量。
  **English**: Preserve output quality for writing, review, presentations, and structured knowledge work.

- **中文**：让新项目更容易从一个可用的项目级 Harness 起步。
  **English**: Make it easier to start a new project with a usable project-level harness.

## 架构 / Architecture

**中文**：这个 Harness 采用分层结构。

**English**: This harness uses a layered structure.

1. **全局层 / Global layer**

   - **中文**：`AGENTS.md` 保存跨项目稳定规则，例如协作风格、任务路由、交付期望和可靠性约束。
   - **English**: `AGENTS.md` holds stable cross-project rules, such as collaboration style, task routing, delivery expectations, and reliability constraints.

2. **工作台层 / Workbench layer**

   - **中文**：`knowledge-workbench/` 保存可复用构件，包括：
   - **English**: `knowledge-workbench/` holds reusable building blocks, including:

   - `templates/`
     - **中文**：常见输出结构模板。
     - **English**: Common output structures.
   - `playbooks/`
     - **中文**：任务路由、交付、质量控制和失败恢复流程。
     - **English**: Routing, delivery, quality-control, and failure-recovery workflows.
   - `style/`
     - **中文**：审美方向、表达风格和风格转换规则。
     - **English**: Aesthetic direction, writing style, and style-translation guidance.
   - `architecture/`
     - **中文**：规则优先级、评分机制和 Harness 治理原则。
     - **English**: Rule precedence, scoring, and harness-governance principles.
   - `benchmarks/`
     - **中文**：校准和回归检查。
     - **English**: Calibration and regression checks.

3. **项目层 / Project layer**

   - **中文**：每个项目都可以根据自身目标、交付物和重复工作流，定义自己的项目根目录 `AGENTS.md` 和 `PROJECT-WORKFLOW.md`。
   - **English**: Each project can define its own root `AGENTS.md` and `PROJECT-WORKFLOW.md` based on its actual purpose, outputs, and recurring workflows.

## 适合谁使用 / Who This Is For

**中文**：如果你使用 Codex 处理以下任务，这个仓库会尤其有用：

**English**: This repository is especially useful if you use Codex for:

- **中文**：知识工作  
  **English**: knowledge work
- **中文**：写作与修改  
  **English**: writing and revision
- **中文**：研究与审阅  
  **English**: research and review
- **中文**：演示文稿与 Deck 准备  
  **English**: presentation and deck preparation
- **中文**：多项目工作流搭建  
  **English**: multi-project workflow setup
- **中文**：长期 Agent 协作  
  **English**: long-term agent collaboration

## 安装 / Installation

**中文**：将文件复制到你的 Codex 主目录中。

**English**: Copy the files into your Codex home directory.

**中文**：推荐目录结构如下：

**English**: Recommended layout:

```text
~/.codex/
  AGENTS.md
  knowledge-workbench/
  skills/
    project-harness-bootstrap/
```

**中文**：建议按以下顺序安装：

**English**: Install in this order:

1. **中文**：将 `AGENTS.md` 复制到 `~/.codex/AGENTS.md`  
   **English**: Copy `AGENTS.md` into `~/.codex/AGENTS.md`

2. **中文**：将 `knowledge-workbench/` 复制到 `~/.codex/knowledge-workbench/`  
   **English**: Copy `knowledge-workbench/` into `~/.codex/knowledge-workbench/`

3. **中文**：将 `skills/project-harness-bootstrap/` 复制到 `~/.codex/skills/project-harness-bootstrap/`  
   **English**: Copy `skills/project-harness-bootstrap/` into `~/.codex/skills/project-harness-bootstrap/`

**中文**：如果你已经有自己的全局 `AGENTS.md`，请谨慎合并，不要直接覆盖。

**English**: If you already have your own global `AGENTS.md`, merge carefully instead of overwriting it blindly.

## 快速开始 / Quick Start

**中文**：安装完成后，全局 Harness 会在各个项目中影响 Codex 的行为。

**English**: After installation, the global harness will shape Codex behavior across projects.

**中文**：创建新项目时，可以用一段简短的项目描述调用 bootstrap skill。

**English**: For a new project, use the bootstrap skill with a short project description.

**中文**：英文示例：

**English**: Example in English:

```text
Use $project-harness-bootstrap to create a project-root harness from this project description.

This is a research and writing project about...
The recurring tasks are...
The main deliverables are...
The preferred tools are...
Actions that require confirmation are...
```

**中文**：中文示例：

**English**: Example in Chinese:

```text
用 $project-harness-bootstrap 根据下面这段项目描述，在项目根目录生成 AGENTS.md 和 PROJECT-WORKFLOW.md。

这个项目是做……
核心重复任务有……
主要交付物有……
希望优先使用的工具有……
需要确认的边界有……
```

## Bootstrap Skill 会生成什么 / What The Bootstrap Skill Generates

**中文**：默认情况下，这个 skill 会创建或更新以下文件：

**English**: By default, the skill creates or updates the following files:

- `AGENTS.md`
  - **中文**：项目专属 Codex Harness，用于改变 Codex 在该项目中的行为。
  - **English**: A project-specific Codex harness that changes Codex behavior inside that project.

- `PROJECT-WORKFLOW.md`
  - **中文**：面向人的快速开始说明和项目工作流地图。
  - **English**: A human-readable quickstart and workflow map for the project.

**中文**：这个 skill 的设计目标是：

**English**: The skill is designed to:

- **中文**：继承你的全局规则  
  **English**: inherit your global rules
- **中文**：避免重复复制全局 Harness  
  **English**: avoid duplicating the global harness
- **中文**：保持项目指令简洁  
  **English**: keep project instructions compact
- **中文**：快速把项目描述转化为可执行工作流  
  **English**: turn project descriptions into usable workflows quickly

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

- **中文**：保持全局层小而稳定。  
  **English**: Keep the global layer small.

- **中文**：保持项目工作流与具体项目强相关。  
  **English**: Keep project workflows project-specific.

- **中文**：优先使用路由，而不是重复堆叠规则。  
  **English**: Prefer routing over repetition.

- **中文**：优先使用可复用 playbook，而不是冗长的顶层 prompt。  
  **English**: Prefer reusable playbooks over long top-level prompts.

- **中文**：优先使用明确交付标准，而不是模糊的质量描述。  
  **English**: Prefer explicit delivery standards over vague quality language.

- **中文**：优先使用修复循环和基准测试，而不是无止境添加更多规则。  
  **English**: Prefer repair loops and benchmarks over endlessly adding more rules.

## 不包含什么 / What Is Not Included

**中文**：这个公开包有意排除了私人本地状态，例如：

**English**: This public package intentionally excludes private local state, such as:

- **中文**：个人配置文件  
  **English**: personal config files
- **中文**：认证文件  
  **English**: auth files
- **中文**：插件缓存  
  **English**: plugin caches
- **中文**：会话数据  
  **English**: session data
- **中文**：本地数据库  
  **English**: local databases
- **中文**：API 密钥  
  **English**: API keys
- **中文**：机器专属自动化脚本或配置  
  **English**: machine-specific automations

## 建议的后续步骤 / Suggested Next Steps

**中文**：如果你想把它发布为自己的仓库，可以考虑补充以下内容：

**English**: If you want to publish this as your own repository, consider adding:

- **中文**：示例和变更记录  
  **English**: examples and a changelog
- **中文**：一个简短的 `CHANGELOG.md`  
  **English**: a short `CHANGELOG.md`
- **中文**：项目描述示例  
  **English**: example project descriptions
- **中文**：项目级 Harness 生成结果示例  
  **English**: example generated project-level harness outputs
