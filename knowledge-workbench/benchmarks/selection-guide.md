# Benchmark 选题映射

目标：把“体检后要不要跑 benchmark、该跑哪几个 task”变成固定动作，而不是每次临时拍脑袋。

## 什么时候使用
- 做完一次中等或结构体检后
- 刚改了 `AGENTS.md`、`architecture/`、`playbooks/`、`style/` 或 `templates/` 的关键入口
- 想验证这次改造是真的增强稳定性，而不是只多了规则

## 默认决策
### 1. 轻量体检后
- 默认不跑完整 benchmark
- 只有当这次修改碰到了 `tool-routing`、`composite-task-decision-table`、`scoring-routing`、`presentation-delivery` 这类核心入口时，才补跑 2 到 3 个探针任务

### 2. 中等体检后
- 默认跑 2 到 4 个任务
- 重点是验证这次修改所在的那一层有没有把主任务识别、验收判断或交付形态带偏

### 3. 结构体检后
- 默认跑 5 到 8 个任务
- 至少覆盖：一个理解类任务、一个正式交付任务、一个复合任务、一个失败闭环任务

## 按修改文件选题
### 1. 路由层改动
适用文件：
- `playbooks/tool-routing.md`
- `playbooks/composite-task-decision-table.md`

优先跑：
- Task 2 比较判断
- Task 6 演示交付
- Task 8 文件交付
- Task 9 复合任务

### 2. 评分与验收层改动
适用文件：
- `playbooks/scoring-routing.md`
- `playbooks/scoring-output-format.md`
- `architecture/scoring-layer.md`
- `playbooks/quality-gates.md`

优先跑：
- Task 4 写作成稿
- Task 5 评估诊断
- Task 6 演示交付
- Task 9 复合任务

### 3. 模板层改动
适用文件：
- `templates/*`

优先跑：
- Task 1 阅读总结
- Task 4 写作成稿
- Task 5 评估诊断

### 4. 审美与呈现层改动
适用文件：
- `style/*`
- `playbooks/presentation-delivery.md`

优先跑：
- Task 6 演示交付
- Task 7 审美翻译
- 必要时补 Task 8 文件交付

### 5. 校准与治理层改动
适用文件：
- `playbooks/calibration-replays.md`
- `playbooks/calibration/*`
- `playbooks/failure-closure-loop.md`
- `playbooks/rule-governance.md`
- `playbooks/health-check-trigger.md`
- `playbooks/health-check-report-template.md`

优先跑：
- Task 5 评估诊断
- Task 9 复合任务
- Task 10 失败闭环

### 6. 全局入口或架构层改动
适用文件：
- `AGENTS.md`
- `architecture/*`
- `knowledge-workbench/README.md`

优先跑：
- Task 1 阅读总结
- Task 3 查询核对
- Task 5 评估诊断
- Task 6 演示交付
- Task 9 复合任务
- Task 10 失败闭环

## 最小跑法
- 只改了一层：跑 2 到 4 个最相关任务
- 同时改了两层以上：跑 4 到 6 个任务
- 改了全局入口或做了结构体检：跑 5 到 8 个任务

## 结果回灌原则
- 如果失败集中在同一层，先修那一层，不要同时往多层加规则
- 如果同一类任务连续两轮 benchmark 都失败，优先补底层规则或重写入口判断
- 如果 benchmark 已经过线，不要因为“还可以再加一点规则”继续扩写文件
