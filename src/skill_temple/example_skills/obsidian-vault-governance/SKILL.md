---
name: obsidian-vault-governance
description: govern obsidian vault architecture and long-term conventions. use when planning or revising folder, tag, property, template, note-type, task, attachment, archive, or structured-content rules in obsidian, including vault 结构规划、命名规范、文件夹/标签/属性边界、模板策略、日记/项目/资料/临时笔记分流、bases/dataview/canvas 使用边界、以及 ai 协同写入规范。
---

# Obsidian Vault Governance

## Purpose
为 AI 在 Obsidian 中的长期协同工作定义“先有规则、再有写入”的治理基线。

先定义 vault 的结构、命名、属性、标签、模板、任务、附件、归档和结构化视图边界，再让后续技能执行创建、编辑、迁移或审计。

## When to use
在以下情况优先使用本 skill：

- 用户要新建 vault 规范，或要把一个已有 vault 变成“AI 可长期协作”的结构。
- 用户要求定义或修订：文件夹职责、标签边界、属性字典、命名规范、模板策略、日记/项目/资料/临时笔记分流规则。
- 用户要求判断 `Markdown / Bases / Dataview / Canvas` 各自应该承担什么角色。
- 用户准备让 AI 高频写入 vault，但还没有明确的低污染规则。
- 用户想把“做法建议”沉淀为一套可复用标准，而不是一次性回答。

## When not to use
以下场景不要使用本 skill：

- 只是要写一个 `.md` 文件的语法、属性、wikilink、callout、embed。此时使用现有 `obsidian-markdown`。
- 只是要写或改 `.base` 文件语法、公式、视图。此时使用现有 `obsidian-bases`。
- 只是要写或改 `.canvas` 文件。此时使用现有 `json-canvas`。
- 只是要调用 Obsidian CLI 读写文件、搜索、重命名、移动。此时使用现有 `obsidian-cli`。
- 只是处理单次、局部的笔记落点判断。此时优先使用 `obsidian-note-router`。

## Scope
### 负责
- 定义 vault 的信息架构与长期约束。
- 定义笔记类型、命名模式、文件夹职责、标签职责、属性职责、模板策略。
- 定义 AI 的写入边界、保守修改策略、污染防护规则。
- 定义 `Markdown / Bases / Dataview / Canvas` 的职责分层。
- 给出可执行的治理规范、决策表、例外条件与后续迁移建议。

### 不负责
- 不直接进行批量迁移、批量改名、批量归档；那属于 `obsidian-refactor-migration`。
- 不直接执行单条写入路由；那属于 `obsidian-note-router`。
- 不做周期性一致性体检；那属于 `obsidian-consistency-audit`。
- 不重复讲解现有语法型 skill 已覆盖的 `.md` / `.base` / `.canvas` 格式细节。

## Workflow
1. 盘点用户已经明确的约束：现有文件夹、模板、命名方式、属性、标签、插件依赖。
2. 区分“显式规则”和“隐式习惯”。只把稳定、可重复、可解释的模式升级为正式规范。
3. 先定义**笔记类型**，再定义每类笔记的最小结构：
   - 入口类：Inbox / Scratch / Daily
   - 协作类：Project / Meeting / Task hub
   - 知识类：Reference / Permanent / MOC 或 Index
   - 结构类：Template / Base / Canvas / Archive
4. 为每类笔记定义：
   - 目标用途
   - 推荐目录
   - 命名规则
   - 最小必需属性
   - 可选属性
   - 链接义务
   - 归档条件
5. 定义“文件夹 / 标签 / 属性”的职责边界。
6. 定义“原始事实 / 视图层 / 可视化层”的边界。
7. 定义 AI 写入与修改的保守策略。
8. 输出治理规范，必要时附后续迁移清单，但不要在本 skill 中直接执行迁移。

## Decision rules
### 1. 先把 Markdown 笔记与属性当作主数据层
默认把 Markdown 笔记及其属性当作 source of truth。

- 官方文档说明，Bases 展示和编辑的数据仍然存储在本地 Markdown 文件及其 properties 中，因此 Base 更适合作为原始笔记之上的原生视图层，而不是另一套数据源。
- 官方文档同时说明，Canvas 的文本卡片不会出现在 Backlinks 中；需要进入链接网络的内容应转换为文件而不是长期留在纯文本卡片里。

因此遵循以下分层：
- `Markdown + properties`：主数据层。
- `Bases`：原生结构化视图层。
- `Dataview`：只读或衍生查询层；仅在用户已标准化使用该社区插件时采用。Dataview 官方文档将其定义为对 vault 执行查询的查询层，而不是新的存储层。
- `Canvas`：空间整理、关系探索、演示层，不承担唯一事实来源。

### 2. 用文件夹承载“生命周期或归属”，不用它编码所有主题
文件夹优先表达以下稳定维度：
- 生命周期：`inbox / active / archive / templates / attachments / temp`
- 归属域：`projects / areas / references / daily`
- 明确需要隔离的系统区：模板、附件、自动生成物、归档区

不要用深层文件夹把所有主题、状态、上下文都塞进去。主题关系优先交给链接，轻量分类优先交给标签，结构化字段优先交给属性。

### 3. 用标签承载轻量、跨目录、可搜索的分类
官方文档说明标签适合快速查找主题，支持嵌套层级，且在 Search、Tags view、Bases 中都能工作。

因此：
- 推荐把标签用于跨笔记、低约束、低字段数的分类，如主题、领域、工作流阶段。
- 可选用嵌套标签表达轻量层级，如 `#topic/ai`、`#status/waiting`。
- 不建议把标签当成高基数字段数据库，例如作者、客户编号、发票号、长状态枚举；这些更适合属性。

### 4. 用属性承载要排序、过滤、汇总或复用的结构化字段
官方文档说明 properties 适合保存 text、list、number、checkbox、date、tags 等结构化信息，并可被 Search、Templates、Bases 和社区插件利用。属性名称一旦设定类型，在全 vault 中应保持一致；Properties view 还支持全局重命名。

因此：
- 推荐把以下内容做成属性：状态、日期、负责人、来源、项目、类型、复盘状态、是否归档。
- 可选把少量稳定枚举做成属性，例如 `status`, `note_type`, `source_type`。
- 不建议把长段落、复杂 Markdown、嵌套对象塞进属性；官方明确说明属性不支持 Markdown，且嵌套属性不适合作为常规编辑界面。

### 5. 用 aliases 表达“同一笔记的别名”，不用它制造平行笔记
官方文档说明 aliases 适合缩写、昵称、异名，并且 Obsidian 会把 alias 链接转换为指向同一主笔记的链接。

因此：
- 推荐用 aliases 吸收旧名称、简称、中英文名称。
- 不建议为同一实体创建多个名称相近的笔记来代替 alias。

### 6. 模板只负责稳定骨架，不负责替代思考
官方文档说明 Templates 可插入预定义文本，Daily notes 也可引用模板；模板中的属性会与目标笔记属性合并。

因此：
- 推荐模板化：标题层级、固定区块、最小属性、标准任务区、来源区、决策区。
- 可选模板化：常用 callout、评审区、会议纪要格式。
- 不建议模板里预填大量经常为空的字段，也不建议给所有笔记套同一超长模板。

### 7. 任务先从原生 Markdown 任务开始，插件能力后置
Obsidian 原生 Search 支持 `task:`, `task-todo:`, `task-done:` 等任务搜索操作符；这意味着即使不依赖社区插件，也能获得基本跨笔记任务检索。

因此：
- 推荐把 Markdown 任务列表作为基线任务格式。
- 仅在用户已明确安装并标准化使用 Tasks 插件时，才把其查询语法、重复任务、完成日期等高级能力纳入规范。官方社区插件页显示 Tasks 是独立的社区插件。

### 8. 先定义结构，再创建 Bases / Dataview / Canvas
- Bases 是对已有文件与属性的筛选、排序、视图和编辑。
- Dataview 是查询层。
- Canvas 是空间布局层。

因此在结构未稳定之前：
- 不要先做复杂 `.base` / Dataview 查询再反推属性命名。
- 不要把 Canvas 视作主笔记集合。
- 先冻结最小属性集和命名规则，再做视图与仪表盘。

## Best practices
### 推荐做法
- 只定义**少量、稳定、可解释**的笔记类型。
- 每类笔记只要求**最小必需属性**，其余保持可选。
- 给新笔记定义唯一落点规则，避免“一件事同时可放 4 个地方”。
- 为附件、模板、临时文件、归档文件单独定义责任区。
- 先设计“增量接入 AI”的规则，再考虑全量规范化。
- 让 AI 默认保守：优先搜索、优先复用现有结构、优先小改、优先新增局部区块而不是整篇重写。

### 可选做法
- 按用户习惯采用 PARA、Johnny.Decimal、MOC、Zettelkasten 或混合流派，但必须落到具体规则，而不是只保留口号。
- 对重度结构化用户，在属性稳定后再增配 Bases 或 Dataview。
- 对重度视觉思考用户，用 Canvas 作为项目地图、研究地图或关系图，但仍保留文件型主记录。

### 不建议做法
- 把文件夹、标签、属性同时用于同一语义维度，例如状态既放文件夹又放标签又放属性。
- 给所有笔记使用同一大而全模板。
- 为了“看起来整齐”而让 AI 触达所有旧笔记进行无收益规范化。
- 让 AI 在没有显式规则时自创大量属性名、标签名、命名风格。

更多边界表见 [references/feature-boundaries.md](references/feature-boundaries.md)。

## Safety rules
- 未定义规范前，不要大规模写入、搬迁或回填属性。
- 不要因为 AI 能生成内容，就把所有临时推理都写进 vault。
- 不要为 AI 便利而破坏用户现有目录与命名习惯；已有稳定结构优先级高于“理论最优结构”。
- 不要把 `.base`、Dataview 查询、Canvas 卡片当作唯一事实来源。
- 不要把治理规范写成“永远必须”，应保留少量例外条件与人工判断口。

## Output contract
产出必须是“可执行治理规范”，至少包含：

1. **适用前提与目标**
2. **笔记类型矩阵**：用途、目录、命名、必需属性、可选属性、链接义务、归档条件
3. **文件夹 / 标签 / 属性职责表**
4. **模板清单与使用条件**
5. **任务管理规则**
6. **Markdown / Bases / Dataview / Canvas 边界表**
7. **AI 写入与修改安全规则**
8. **例外处理规则**
9. **后续迁移 backlog（如需要）**

## Failure modes
### 失败模式 1：过度设计
症状：目录层级过深、属性过多、模板过重。
处理：把规则压缩到“最小可用集”，只保留会影响搜索、视图、协作和维护的约束。

### 失败模式 2：把视图层当数据层
症状：先做 Base、Dataview、Canvas，再反过来逼迫笔记适配。
处理：回到 Markdown 与 properties 先收敛核心字段。

### 失败模式 3：AI 自创术语
症状：一个 vault 里出现多个近义属性、近义标签、近义命名。
处理：强制建立受控词表；未收录项先进入候选，不立即生效。

### 失败模式 4：把所有笔记类型混为一谈
症状：项目、日记、资料、会议、想法都共用一套字段与模板。
处理：按生命周期与用途重新分型，再各自定义最小结构。

## Examples
### 示例 1：给新 vault 定义基础架构
用户要让 AI 长期协同管理研究、项目和日记。
本 skill 应输出：目录职责、笔记类型、命名规范、属性字典、模板策略、AI 写入规则。

### 示例 2：为已有混乱 vault 收敛规则
用户已有大量历史笔记，但结构漂移严重。
本 skill 应先抽样归纳已有稳定模式，再输出“保守改造版”治理规范，而不是推倒重来。

### 示例 3：判断是否应该用 Bases
用户想做项目面板。
本 skill 应先判断项目笔记是否已有稳定属性；若没有，先补治理规范，再建议建立 Base。

### 示例 4：判断 Canvas 的职责
用户想把研究过程都放进 Canvas。
本 skill 应明确：Canvas 可做研究地图，但进入长期知识网络的内容应落回文件型笔记。
