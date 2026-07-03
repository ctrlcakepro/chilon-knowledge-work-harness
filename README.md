Knowledge Work Harness for Codex

> A layered, maintainable, and automation-aware Codex harness for real-world knowledge work.

这不是一份为了“提示词更长”而设计的配置包，而是一套为了长期协作而整理出来的工作结构。它服务的不是一次性问答，而是那些真正会反复发生的任务：读书、做笔记、整理课程材料、写论文、搭提纲、准备汇报、精炼文档、修正表达、检查交付质量。你可以把它理解成一套给 Codex 使用的知识工作底座，它试图解决的核心问题不是“怎样回答得更多”，而是“怎样在有限上下文里，持续稳定地做出像成品的结果”。  
This is not a package designed to make prompts longer. It is a working structure shaped for long-term collaboration. It is built for the kinds of tasks that actually repeat in real life: reading, note-taking, organizing course material, writing papers, drafting outlines, preparing presentations, condensing documents, refining expression, and checking deliverable quality. Think of it as a knowledge-work foundation for Codex. Its core concern is not “how to say more,” but “how to keep producing stable, finished-feeling results within a limited context budget.”

很多个人 harness 会在变强之前先变重：规则越来越多，职责越来越乱，最后模型不是忘了执行，就是在不同规则之间摇摆。这套结构的出发点正好相反。它把顶层规则压到只剩那些跨任务稳定成立的部分，把专题 workflow、模板、记忆、回归样例和自动维护都拆到更低层，让系统更像一个有分工的工作台，而不是一个塞满提醒的长提示词。  
Many personal harnesses become heavy before they become strong: more rules, blurrier responsibilities, and eventually a model that either stops following them or keeps oscillating between competing instructions. This project starts from the opposite assumption. It keeps the top layer limited to rules that are truly stable across tasks, while pushing domain workflows, templates, memory, regression examples, and maintenance into lower layers. The result is meant to feel less like an oversized prompt and more like a workbench with clear internal structure.

## Why This Exists

这套 harness 主要面向知识工作，而不是只面向代码工作。它适合的典型场景包括：课程学习中的章节梳理、教材复习、论文和作业提纲、文献阅读摘要、汇报结构设计、PDF 或 Word 文档精炼、内容改写，以及那些“我需要一个能直接继续用的结果，而不是一堆方法解释”的请求。如果你经常在聊天窗口里重复做这些事，那么你真正需要的通常不是更多 prompt，而是更稳定的任务分流、更清楚的结构层次，以及更可靠的交付路径。  
This harness is aimed primarily at knowledge work, not only coding work. Typical use cases include chapter review for courses, textbook revision, paper and assignment outlining, reading summaries for articles and literature, presentation structuring, PDF or Word document condensation, content rewriting, and any request where the real need is “give me something I can keep using,” not “explain the method to me again.” If you keep doing these tasks in chat over and over, what you usually need is not more prompting, but steadier task routing, clearer structural layers, and more reliable delivery paths.

它还有一个更现实的目标：让规则本身可治理。也就是说，这个项目不是默认“规则越多越好”，而是默认规则也需要被审查、收缩、校准和删除。你会在这里看到体检脚本、冷层压缩报告、回归样例、定时维护任务和预算检查，这些都在服务同一个目标：让 harness 长期可用，而不是短期看起来很完整。  
It also has a more practical goal: making the rules themselves governable. In other words, this project does not assume that more rules are better. It assumes rules need review, compression, calibration, and sometimes deletion. That is why the package includes health-check scripts, cold-layer compression reports, regression samples, recurring maintenance jobs, and budget checks. All of these serve the same purpose: keeping the harness usable over time instead of merely making it look comprehensive in the short term.

## Architecture

这套项目采用分层架构，每一层都尽量只承担一种职责。`AGENTS.md` 负责顶层协作协议，定义默认输出风格、提问边界、任务分流原则和可靠性要求；`PROJECT-WORKFLOW.md` 负责项目级默认工作流，把常见请求映射到更具体的处理路径；`.project-memory/` 是显式 memory layer，用来保存长期偏好、项目状态、决策记录、知识缓存和交付规范；`tools/` 放的是治理脚本，用来检查结构、预算和冷层压力；`harness-regression/` 用于保存样例与演练，确保改动后不会悄悄把高频能力做坏。这样拆层的好处是：顶层保持简洁，局部细节按需加载，整个系统更不容易因为上下文过长而失控。  
The project uses a layered architecture, and each layer is designed to carry only one kind of responsibility. `AGENTS.md` holds the top-level collaboration protocol, including default output style, questioning boundaries, task routing principles, and reliability rules. `PROJECT-WORKFLOW.md` handles the project-level default flow, mapping common requests into more concrete processing paths. `.project-memory/` acts as an explicit memory layer for durable preferences, project state, decision logs, knowledge cache, and delivery specs. `tools/` contains governance scripts that inspect structure, budgets, and cold-layer pressure. `harness-regression/` stores examples and drills so changes do not quietly break high-frequency capabilities. The payoff of this layering is simple: the top stays lean, detail loads on demand, and the whole system is less likely to become unstable because too much context was flattened at once.

从技术视角看，这个包已经不只是“几份 markdown”。当前结构里有明确的热路径和冷路径之分。热路径包括 `AGENTS.md`、`PROJECT-WORKFLOW.md`、`.project-memory/README.md` 以及少数几个高频路由文件，它们负责在大多数任务开始时提供最小可用上下文；冷路径则由更细的 memory、delivery spec、knowledge cache 和回归材料组成，只在真正需要时再读取。这种区分直接影响 token 占用：系统默认避免全量平铺，而是通过入口路由和显式索引控制读取范围。  
From a technical perspective, this package is no longer “just a set of markdown files.” The current structure explicitly distinguishes between hot paths and cold paths. The hot path includes `AGENTS.md`, `PROJECT-WORKFLOW.md`, `.project-memory/README.md`, and a small set of high-frequency routing files that provide the minimum viable context at task start. The cold path contains more detailed memory files, delivery specs, knowledge cache, and regression material, which are only read when actually needed. This distinction directly affects token usage: instead of flattening everything into one prompt, the system uses entry routing and explicit indexes to control how much context gets loaded.

## Core Components

`AGENTS.md` 是顶层协议文件，它控制整套 harness 的基本协作气质。这里强调的是任务分流、少而关键的追问、成品感输出、可靠性约束，以及在中等复杂任务里先给出推进路径而不是原地追问。它的作用不是替代所有模板和 workflow，而是作为最稳定的一层，给整个系统定下工作方式。  
`AGENTS.md` is the top-level protocol file. It defines the general collaboration posture of the harness: task routing, minimal but important questioning, deliverable-oriented output, reliability constraints, and the expectation that medium-complexity tasks should start with forward motion instead of premature clarification. Its role is not to replace all templates and workflows, but to serve as the most stable layer that sets the operating style for the whole system.

`PROJECT-WORKFLOW.md` 更像是项目运行说明书。它会告诉模型常见任务怎样进入对应流程，例如阅读总结、知识整理、比较分析、论文写作、展示准备、文本修改和文件交付。和 `AGENTS.md` 相比，它更接近执行面，因此会承担“默认顺序”“默认入口”“高频请求映射”这类工作。  
`PROJECT-WORKFLOW.md` is closer to an operating manual for the project. It explains how common tasks should enter their corresponding flows, including reading summaries, knowledge organization, comparative analysis, academic writing, presentation prep, text revision, and formal file delivery. Compared with `AGENTS.md`, it sits closer to execution, so it handles the default order of work, entry points, and mappings for high-frequency requests.

`.project-memory/` 是这套结构里最关键的一层，因为它把“记忆”从隐性的聊天历史里拉出来，变成显式、可查、可治理的项目资产。这里面既有用户偏好、项目状态和决策记录，也有交付规范、能力回退矩阵、文档精炼模板、知识缓存和自动化索引。重点不在于什么都记，而在于只保存那些会稳定影响后续协作的内容。  
`.project-memory/` is arguably the most important layer in the system because it pulls “memory” out of implicit chat history and turns it into explicit, inspectable, governable project assets. It contains user preferences, project state, decision logs, delivery specs, fallback matrices, document condensation templates, knowledge cache, and automation indexes. The key idea is not to remember everything, but to preserve only what will keep affecting future collaboration in a stable way.

`tools/check_harness.py` 是结构体检脚本。它会检查关键文件是否存在、顶层和中枢文件是否超预算、关键引用是否断裂、旧命名是否残留、误广加载是否过重，以及“如果有人把整套规则全量平铺，会不会明显变重”。这意味着你不需要只凭感觉判断 harness 有没有失控，而是可以用脚本给出一份明确的健康结论。  
`tools/check_harness.py` is the structural health-check script. It verifies that critical files exist, checks whether top-level and central files exceed their budgets, ensures key references are intact, detects legacy naming residue, estimates accidental broad-load pressure, and evaluates how heavy the system would become if someone flattened the whole rule set. In practice, this means you do not have to rely on intuition alone to decide whether the harness is drifting. The script can produce a concrete health verdict.

`tools/auto_cold_layer_maintenance.py` 是自动冷层分析脚本。它会扫描 `.project-memory` 中不属于热路径的文件，估算它们的 tokens、比较引用热度、寻找近重复热点，并输出每周和每月的冷层压缩报告。这个报告不会盲目自动删文件，但会给出清楚的候选排序和治理建议，让自动维护任务优先做那些真正有价值的小修正。  
`tools/auto_cold_layer_maintenance.py` is the automated cold-layer analysis script. It scans the files inside `.project-memory` that are not part of the hot path, estimates their token cost, compares their reference heat, detects near-duplicate hotspots, and produces weekly and monthly cold-layer compression reports. The report does not blindly delete files on its own, but it gives a clear ranking of candidates and concrete governance suggestions so recurring maintenance jobs can focus on the highest-value small fixes first.

`harness-regression/` 是这套系统的安全网。里面既有最小回归样例，也有针对 memory、fallback 和文本选择器的演练脚本。它的意义在于：每次你调整规则、收缩文件或修改路由时，都不需要完全靠主观判断“应该没问题”，而是可以拿具体样例做抽查。  
`harness-regression/` is the safety net for the system. It contains both minimal regression cases and drills around memory, fallbacks, and text selectors. Its purpose is to make sure that whenever you adjust rules, compress files, or change routing, you do not have to depend entirely on subjective confidence. You can spot-check against concrete examples instead.

## Automation and Maintenance

这套包还导出了两个 Codex 自动化配置：每周轻维护和每月深检。它们不是简单地“定时跑一遍脚本”，而是先生成冷层报告，再结合健康检查、回归样例和 memory 边界，决定这轮是应该删重复、并近义、做小幅下沉，还是维持现状。换句话说，这套 harness 从设计上就接受一件事：规则也会老，结构也会长胖，所以维护不是补丁，而是内建能力。  
The package also exports two Codex automation configs: a weekly light-maintenance job and a monthly deep-audit job. These are not just timers that rerun scripts. They first generate cold-layer reports, then combine those reports with health checks, regression samples, and memory-boundary inspection to decide whether the current cycle should deduplicate, merge related files, push material downward, or simply keep the structure as is. In other words, the harness is built around a simple assumption: rules age, structures gain weight, and maintenance should be a built-in capability rather than an afterthought.

现在这套自动维护流程已经接入 `outputs/harness-maintenance/`。每周和每月运行后，都会生成对应的 markdown 和 JSON 报告，用来记录当前冷层文件数、估算 token 压力、候选收缩文件、重复热点和建议动作。对于想把 harness 放到 GitHub 持续演进的人来说，这一点很重要，因为它让结构调整可以被追踪，而不是只存在于一次聊天里。  
The automated maintenance flow now writes into `outputs/harness-maintenance/`. Each weekly or monthly run generates markdown and JSON reports that record current cold-layer file counts, estimated token pressure, candidate files for compression, duplicate hotspots, and recommended actions. This matters a lot if you plan to evolve the harness on GitHub over time, because structural adjustments become trackable artifacts instead of decisions that only existed inside a single chat.

## Installation

如果你只想快速安装，最简单的方法是在 Windows 下直接双击 `install.cmd`。它会调用 `install.ps1`，询问你目标项目目录的绝对路径，然后把这套 harness 安装到那个目录。安装过程中，脚本会自动把目标目录内同名文件和目录备份到 `.harness-install-backup/时间戳/`，因此即使你是在已有项目上覆盖安装，也保留了回退空间。  
If you want the fastest setup path, simply double-click `install.cmd` on Windows. It calls `install.ps1`, asks for the absolute path of your target project directory, and installs the harness there. During installation, any existing files or directories with the same names are backed up into `.harness-install-backup/<timestamp>/`, so even if you install over an existing project, you still keep a rollback path.

如果你更习惯手动执行，可以在 PowerShell 中运行：`powershell -ExecutionPolicy Bypass -File .\install.ps1`。默认情况下，安装脚本会复制 `AGENTS.md`、`PROJECT-WORKFLOW.md`、`.project-memory/`、`harness-regression/` 和 `tools/`，同时把两个自动化配置写入 `~/.codex/automations/weekly-harness-maintenance/automation.toml` 和 `~/.codex/automations/monthly-harness-deep-audit/automation.toml`。如果你暂时不想安装自动化，只要加上 `-SkipAutomations` 即可。  
If you prefer running it manually, use `powershell -ExecutionPolicy Bypass -File .\install.ps1` in PowerShell. By default, the installer copies `AGENTS.md`, `PROJECT-WORKFLOW.md`, `.project-memory/`, `harness-regression/`, and `tools/`, and also writes the two automation configs into `~/.codex/automations/weekly-harness-maintenance/automation.toml` and `~/.codex/automations/monthly-harness-deep-audit/automation.toml`. If you do not want to install the automation layer yet, simply add the `-SkipAutomations` flag.

安装完成后，推荐先做两步。第一步运行 `python tools/check_harness.py`，确认关键文件、引用和预算状态正常；第二步运行 `python tools/auto_cold_layer_maintenance.py --mode weekly`，快速看一眼冷层压力报告。这样你在真正开始使用之前，就能知道这套 harness 当前是“结构健康”“接近扩张边界”还是“已经需要收缩”。  
After installation, two follow-up steps are recommended. First, run `python tools/check_harness.py` to confirm that key files, references, and budget status are healthy. Second, run `python tools/auto_cold_layer_maintenance.py --mode weekly` to get a quick cold-layer pressure report. This gives you an immediate sense of whether the harness is currently “healthy,” “approaching expansion limits,” or “already due for compression” before you start real work with it.

## Package Contents

这个导出包包含当前最核心、最适合同步到 GitHub 的部分：顶层配置、项目工作流、显式 memory layer、结构治理脚本、自动冷层分析脚本、回归样例、演练材料，以及两个 Codex 自动化配置。它不包含 `tmp/`、`outputs/` 中的运行结果、截图、PDF 成品或其他临时缓存，因此更适合作为公开仓库中的“配置源”，而不是整个工作目录的镜像。  
This export bundle contains the parts that are most central and most appropriate for syncing to GitHub: top-level configuration, project workflow, the explicit memory layer, structural governance scripts, automated cold-layer analysis, regression cases, drills, and the two Codex automation configs. It does not include `tmp/`, generated runtime outputs from `outputs/`, screenshots, final PDFs, or other temporary caches, which makes it better suited as the “configuration source” for a public repository rather than a mirror of the entire working directory.

## Closing Note

如果你想要的不是一个“看起来很全”的提示词合集，而是一套能随着真实任务一起成长、并且能自己检查自己有没有变重的工作结构，那么这份包会是一个不错的起点。它不假装已经是一个成熟产品，但它已经把最重要的事情做对了：分层、治理、交付意识、自动维护，以及对上下文预算的尊重。  
If what you want is not a prompt bundle that merely looks comprehensive, but a working structure that can grow alongside real tasks and also check whether it has become too heavy, this package is a solid starting point. It does not pretend to be a finished product, but it already gets the important things right: layering, governance, deliverable awareness, automated maintenance, and respect for context budgets.
