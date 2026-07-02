# Output Contract

This skill normally writes two files in the project root:

1. `AGENTS.md`
2. `PROJECT-WORKFLOW.md`

Keep both compact. They should help the project run better, not become a second global harness.

## File 1: `AGENTS.md`

Purpose:

- machine-facing standing instructions for Codex inside this project

Recommended sections:

1. `项目定位`
2. `你的角色`
3. `项目背景与边界`
4. `核心工作流`
5. `输出规范`
6. `文件约定`
7. `事实与可靠性规则`
8. `协作与安全边界`

Writing rules:

- include only sections that materially change project behavior
- do not restate the user's global language, tone, or generic reliability rules unless this project overrides them
- make workflows specific to this project
- prefer short operational bullets over long explanation
- reference real paths only after verifying them

## File 2: `PROJECT-WORKFLOW.md`

Purpose:

- human-readable quickstart and workflow map

Recommended sections:

1. `项目目标`
2. `主要工作流`
3. `默认处理顺序`
4. `高频请求 -> 默认动作`
5. `常见交付物`
6. `启动示例`

Writing rules:

- describe how work flows in this project
- show what common requests should turn into
- include a few example prompt shapes when useful
- avoid repeating every rule already present in `AGENTS.md`

## Compactness rule

If content is generic across many projects, do not write it into the project root.

Instead:

- leave it to global `AGENTS.md`
- leave it to the global knowledge workbench
- or omit it entirely

## Update rule

When either file already exists:

- preserve valid project-specific content
- merge, do not append duplicates
- shorten vague or repetitive sections
- keep the root files readable enough that future edits stay easy
