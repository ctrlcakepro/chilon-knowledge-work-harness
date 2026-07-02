# Harness Benchmark

目标：用一组固定任务，定期验证 harness 是不是在变强，而不是只是在变复杂。

## 适用场景
- 大幅修改 `AGENTS.md` 后
- 重构 `playbooks/`、`style/`、`templates/` 后
- 连续新增多条规则后
- 触发中等或结构体检后
- 想验证一次改造到底有没有提升稳定性时

## Benchmark 组成
- [task-set.md](task-set.md)
固定任务集，负责测什么
- [selection-guide.md](selection-guide.md)
体检或大改后该优先跑哪些任务，不必每次从头挑
- [report-template.md](report-template.md)
结果记录模板，负责怎么记

## 最小使用方式
1. 如果是体检后的验证，先看 `selection-guide.md`
2. 从 `task-set.md` 里选 2 到 8 个任务
3. 按当前 harness 跑一遍
4. 用 `report-template.md` 记录结果
5. 看失败点是路由、评分、审美、交付，还是治理层问题

## 通过标准
不是要求每个任务都“完美”，而是至少做到：
- 主任务识别正确
- 工具路由不降级
- 主评分卡与次评分卡选择合理
- 结果像成品，而不是聊天碎片
- 如果失败，能明确落到哪一层规则修

## 默认提醒
如果 benchmark 连续两轮都在同一类任务上失败，优先补底层规则，而不是继续堆局部补丁。
