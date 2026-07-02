# Harness 健康检测
日期：2026-07-02

## 当前结论
当前这套 harness 已从“快速扩张期”进入“可治理的成型期”。

整体判断：
- 结构健康度：良好
- 入口负担：已明显下降
- 规则分层：基本清楚
- 主要风险：中层 `playbooks/` 持续增厚

## 当前结构角色
### 1. 中枢层
- `AGENTS.md`
- `architecture/layers.md`
- `architecture/priority-order.md`

职责：
- 只保留分流、优先级、禁降级、成品判断
- 不承载过多案例细节和工具细节

当前状态：
- 健康
- 已从 441 行压到 335 行

### 2. 任务骨架层
- `templates/`

职责：
- 承载高频输出骨架

当前状态：
- 健康
- 文件短、边界清楚、负担轻

### 3. 审美与风格层
- `style/directions.md`
- `style/aesthetic-translator.md`

职责：
- 承担气质翻译、禁忌项、方向判断

当前状态：
- 基本健康
- `aesthetic-translator.md` 较长但仍属合理，因为它替代了全局层的大量重复审美说明

### 4. 执行与验收层
- `playbooks/tool-routing.md`
- `playbooks/composite-task-decision-table.md`
- `playbooks/scoring-routing.md`
- `playbooks/scoring-output-format.md`
- `playbooks/quality-gates.md`

职责：
- 决定怎么走、怎么验、怎么说

当前状态：
- 健康但偏厚
- 是后续最可能继续变胖的区域

### 5. 纠偏与治理层
- `playbooks/calibration-replays.md`
- `playbooks/calibration/*`
- `playbooks/failure-closure-loop.md`
- `playbooks/rule-governance.md`

职责：
- 记录反例
- 把失败沉淀回系统
- 防止规则无限膨胀

当前状态：
- 健康
- 已形成闭环

## 当前主要优点
- 全局入口已变短，不再平铺所有文件
- 复合任务、评分、失败闭环、规则治理已经接成链路
- 演示与审美的重复说明已大幅下沉
- `playbooks/index.md` 已提供轻量导航，降低了检索成本
- 体检后补跑 benchmark 的接口已经建立，不再只有“检完就停”

## 当前主要风险
### 1. 中层 playbooks 继续增厚
风险文件：
- `tool-routing.md`
- `composite-task-decision-table.md`
- `failure-closure-loop.md`
- `calibration-replays.md`
- `playbooks/calibration/*`

风险性质：
- 不是现在就有问题
- 但后续每次加案例、加裁决、加补丁时，最容易继续长

### 2. 局部重复仍存在
主要是：
- `AGENTS.md` 与 `presentation-delivery.md` 之间仍有少量演示提醒重叠
- `tool-routing.md` 与 `scoring-routing.md` 在“主评分卡 / 次评分卡”表达上仍有轻度平行说明

### 3. 回放库未来可能再次变胖
`calibration-replays.md` 已拆成“总索引 + 专题反例”，后续要防止专题文件再次无序膨胀。

## 当前长度观察
### 轻量文件
- `templates/*`
- `style/directions.md`
- `playbooks/next-steps.md`
- `playbooks/quality-gates.md`

### 中等文件
- `presentation-delivery.md`
- `scoring-output-format.md`
- `rule-governance.md`

### 偏重文件
- `tool-routing.md`
- `composite-task-decision-table.md`
- `failure-closure-loop.md`
- `calibration-replays.md`
- `playbooks/calibration/*`
- `architecture/scoring-layer.md`

结论：
- 真正需要控长的不是 `AGENTS.md`
- 而是中层 `playbooks/`

## 当前建议
### 1. 全局层继续严格控长
原则：
- 新经验优先下沉
- 只有跨任务、重复、代价高的规律才升全局

### 2. playbooks 按主题而不是按时间扩展
不要不断往原文件尾部堆补丁。优先做：
- 合并同类项
- 改案例描述为判断句
- 必要时拆成专题文件

### 3. 定期做轻量体检
建议触发时机：
- 新增 3 到 5 条以上规则后
- 某个 playbook 明显超过当前同层文件体量
- 读入口文件时开始需要频繁跳转回找

正式触发时，默认参考 `knowledge-workbench/playbooks/health-check-trigger.md`。

### 4. 中等以上体检后接 benchmark
如果这次体检已经碰到了全局入口、路由、评分或正式交付协议，默认再按 `knowledge-workbench/benchmarks/selection-guide.md` 跑一轮代表性任务，验证修补有没有真正改善行为。

## 下次优先观察点
- `playbooks/tool-routing.md` 是否继续承担过多任务族细节
- `playbooks/calibration/*` 是否再次开始混装多个失败模式
- `AGENTS.md` 是否再次出现整段下层规则回流

## 一句话判断
当前系统不是“越用越胖”的失控状态，而是“已经建立了瘦身机制，但中层文件需要持续控长”的可治理状态。
