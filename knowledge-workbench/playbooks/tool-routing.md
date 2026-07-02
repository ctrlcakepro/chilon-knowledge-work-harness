# 工具硬路由

目标：先把任务送到最合适的 skill 或工具链，再开始做内容，尽量减少走错路、降级交付和重复返工。

## 路由总原则
- 先识别任务真正的交付形态，再决定用什么做。
- 如果任务同时包含两种以上意图，先裁决主任务，再决定工具路由。
- 先用专用 skill 或成熟工具链，再考虑手工实现。
- 如果已有专用能力能满足核心需求，默认不要降级成普通聊天输出。
- 如果不走现成能力，要说明缺了什么，为什么换路。

## 默认判断顺序
1. 先判断这是不是复合任务；如果是，优先参考 `knowledge-workbench/playbooks/composite-task-decision-table.md`。
2. 这是阅读、分析、写作、审稿，还是文件交付任务。
3. 最终要交的是文本、PDF、Word、表格、PPT、HTML 演示，还是浏览器验证结果。
4. 当前环境有没有对应 skill 或成熟工具链。
5. 现成能力是否满足核心功能、格式和审美要求。
6. 只有前面不满足，才进入自定义实现。

## 路由后的默认动作
工具路由一旦确定，默认立刻转到 `knowledge-workbench/playbooks/scoring-routing.md`。

这里不负责展开主评分卡、次评分卡和验收细则，只负责把任务送到正确的 skill / 工具链。

## 任务类型 -> 默认优先路由

### 1. PDF / Word / 正式文档交付
- 源材料是 PDF：优先 `pdf` skill
- 目标是正式排版文档：优先 `documents`
- 需要正式 PDF 成品：走 `pdf` 或 `documents` 对应导出链路
- 适用：论文审稿、研究计划评估、正式报告、审稿意见文档、课程论文排版稿

不要降级成：
- 只在聊天里给口头意见
- 只给 Markdown 或纯文本
- 不检查版式就直接交付
- 不生成用户要求的文件

### 2. 表格、统计表、结构化数据整理
- 优先：`spreadsheets` skill
- 适用：Excel、CSV、评分表、数据整理表、对照清单、批量格式化

不要降级成：
- 只描述应该怎么做
- 用段落替代本该给出的表格结果

### 3. PPT / HTML 演示交付
- 传统 PPT / `.pptx`：优先 `presentations`
- HTML 幻灯片 / 组会演示：优先 `html-ppt`
- 进入演示任务后，默认再参考 `knowledge-workbench/playbooks/presentation-delivery.md`
- 适用：PPT、HTML deck、组会展示、课堂展示、答辩、明天要讲

不要降级成：
- 普通网页
- 长文式讲稿页
- 只有滚动没有翻页的页面
- 没有演讲模式的“假幻灯片”

### 4. 阅读总结、知识整理、课程笔记
- 优先：直接按 `knowledge-workbench/templates/reading-summary.md` 等模板输出
- 如果材料是 PDF：先用 `pdf` skill 抽取和校验
- 适用：文章总结、章节梳理、课堂笔记整理、复习提纲

不要降级成：
- 只复述原文段落
- 不做结构化处理

### 5. 论文、作业、提纲、研究计划写作
- 优先：直接按 `knowledge-workbench/templates/essay-outline.md` 等模板推进
- 如果用户要求正式文档交付：叠加 `documents`
- 如果用户要求 PDF 成品：叠加 `pdf`

不要降级成：
- 只有零散想法
- 结构未成型就直接堆长文

### 6. 审稿、规范评估、方法诊断
- 优先：按 `knowledge-workbench/templates/review-outline.md` 输出判断
- 材料是 PDF 时：先用 `pdf` skill
- 需要正式成品文件时：叠加 `documents` 或 `pdf`

不要降级成：
- 模糊评价
- 只有优点没有问题
- 没有修改建议

### 7. 浏览器交互验证、全屏测试、页面实测
- 优先：浏览器控制 skill
- 当前 Codex 内浏览器：`browser:control-in-app-browser`
- 依赖用户真实 Chrome 状态时：`chrome:control-chrome`

不要降级成：
- 只看代码就断定页面表现
- 不做实际交互检查

### 8. RAG / 知识库 / 语义检索
- 优先：`rag-builder`
- 已有教材型 RAG 数据库问答：优先 `rag-db-manager` 系列 skill

不要降级成：
- 直接把文件堆给普通摘要
- 不建索引就假装能稳定检索

### 9. OpenAI / Codex 官方能力、模型与文档问答
- 优先：`openai-docs` skill
- 适用：模型选择、Codex 使用、OpenAI API 最新官方文档说明

不要降级成：
- 纯记忆作答且不核对官方文档

## 需要显式说明换路原因的情况
- 专用 skill 缺少核心功能
- 专用模板风格明显不符
- 目标成品与默认输出形态冲突
- 自定义实现能明显提升交付质量
- 当前工具链无法完成用户点名的格式或功能

## 最小执行口径
开始执行前，默认在心里过一遍：
- 这到底是什么类型的任务
- 最终交付物是什么
- 现成 skill 能不能直接覆盖
- 我有没有在无意识地把任务降级
