# Playbooks 索引

目标：给 `playbooks/` 提供一个轻量入口，减少每次都在多份规则之间来回翻找。

## 先按任务阶段找
### 1. 先判断怎么走
- [tool-routing.md](tool-routing.md)
适用：要先决定走哪种 skill、工具链或交付路径
- [composite-task-decision-table.md](composite-task-decision-table.md)
适用：一个请求同时包含写作、查询、评估、设计、演示、文件交付等多重意图

### 2. 再判断怎么验收
- [scoring-routing.md](scoring-routing.md)
适用：工具路由后，需要决定主评分卡与次评分卡
- [scoring-output-format.md](scoring-output-format.md)
适用：需要把评分结果稳定说出来
- [quality-gates.md](quality-gates.md)
适用：交付前快速查漏补缺

### 3. 如果任务做偏了
- [calibration-replays.md](calibration-replays.md)
适用：先看反例总索引，再进入对应专题案例
- [failure-closure-loop.md](failure-closure-loop.md)
适用：已经做偏，需要判断偏差类型、修正路径与永久规则落点
- [rule-governance.md](rule-governance.md)
适用：准备继续沉淀规则，但要先判断该不该进全局、该不该下沉或合并
- [health-check-trigger.md](health-check-trigger.md)
适用：需要判断现在是否该做一次轻量或中等体检
- [health-check-report-template.md](health-check-report-template.md)
适用：已经触发体检，需要按统一格式输出结果

### 4. 某类专用交付
- [presentation-delivery.md](presentation-delivery.md)
适用：PPT、HTML deck、组会、课堂展示、答辩、明天要讲

### 5. 任务做完后继续推进
- [next-steps.md](next-steps.md)
适用：任务完成后，给自然续接而不是突然停住

## 最小使用顺序
默认只记这一条：

1. 先看 `tool-routing`
2. 复合任务先看 `composite-task-decision-table`
3. 再看 `scoring-routing`
4. 交付前过 `quality-gates`
5. 需要显式验收就看 `scoring-output-format`
6. 做偏了就走 `calibration-replays -> failure-closure-loop -> rule-governance`
7. 继续扩规则前，先看 `health-check-trigger`
8. 真正开始体检时，按 `health-check-report-template` 输出
9. 如果体检后改了核心入口，再转 `benchmarks/selection-guide`
