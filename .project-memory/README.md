# Project Memory Index

`.project-memory/` 是 Chilon 的显式 memory layer。它保存可复用、可审计、可迁移的项目状态与协作规范，但不应该保存私人绝对路径、账号凭据或一次性聊天内容。

## 核心文件
- `user-preferences.md`：长期输出偏好。
- `project-state.md`：项目阶段、当前目标与待办状态。
- `decision-log.md`：稳定成立的架构判断与纠偏记录。
- `reusable-assets.md`：可复用模板、素材与入口。
- `knowledge-cache/`：可复用概念卡、比较维度、结构骨架与 `knowledge-cache/index.md`。

## 能力与交付路由
- `automation-entrypoints.md`：高频请求入口。
- `tool-delivery-routing.md`：不同主交付物的默认能力路由。
- `plugin-mcp-governance.md`：插件、MCP、浏览器验证与专用能力边界。
- `capability-registry.md`：当前高优先级能力清单。
- `capability-fallback-matrix.md`：能力不可用时的回退路径。
- `text-selector-questioning-protocol.md`：文本选择器追问协议。

## 治理与维护
- `weekly-maintenance-report-template.md`：每周维护报告模板。
- `rule-deletion-guidelines.md`：规则删除与收缩准则。
- `memory-write-thresholds.md`：memory 写入门槛。
- `memory-retention-and-expiry.md`：memory 保留与过期复查规则。
- `memory-audit-playbook.md`：memory 审计入口。
- `document-condense-template.md`：文档精炼模板。
- `expansion-budget-policy.md`：扩张预算策略。
- `validation-pre-delivery.md`：交付前轻量自检。
- `validation-harness-health.md`：harness 健康检查维度。

## 使用原则
1. 先读索引，再按任务只加载必要文件。
2. 先复用既有文件，再考虑新增文件。
3. 先删重复、并近义、下沉细节，再补空白。
4. 所有路径默认使用相对路径，公开模板不得绑定本机目录。
