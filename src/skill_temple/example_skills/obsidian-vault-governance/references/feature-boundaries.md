# Feature Boundaries

## 1. 文件夹、标签、属性的分工

| 维度 | 推荐承载方式 | 适用条件 | 不建议做法 |
| --- | --- | --- | --- |
| 生命周期 | 文件夹 / 属性 | 需要稳定落点或归档规则 | 同时用文件夹、标签、属性三套状态 |
| 主题 | 标签 / 链接 | 轻量分类、跨目录检索 | 用深层目录取代所有主题关系 |
| 结构化字段 | 属性 | 需要排序、过滤、视图、统计 | 用标签编码高基数字段 |
| 别名 / 缩写 | aliases | 同一实体多叫法 | 新建平行笔记 |
| 关系 | 内链 / 反链 | 知识网络与上下文跳转 | 用文件夹表达所有关系 |

## 2. Markdown / Bases / Dataview / Canvas 的边界

| 层 | 推荐角色 | 适用前提 | 不建议角色 |
| --- | --- | --- | --- |
| Markdown note | 主记录、主内容、主上下文 | 一切 vault | 只当视图缓存 |
| Properties | 主记录上的结构化字段 | 字段稳定、可枚举 | 大段正文、复杂嵌套结构 |
| Bases | 原生交互式视图 | 已有稳定 properties | 另一套主数据源 |
| Dataview | 查询 / 报表 / 派生视图 | 用户已标准化启用插件 | 写时主记录 |
| Canvas | 空间整理、演示、关系图 | 视觉化需求强 | 唯一事实来源 |

## 3. 推荐的最小笔记类型集合

| 类型 | 目的 | 推荐目录 | 最小字段 |
| --- | --- | --- | --- |
| inbox | 暂存未分流输入 | `00 Inbox/` | `note_type`, `created` |
| daily | 当天日志与捕获 | `10 Daily/` | `date`, `note_type` |
| project | 协调项目状态与决策 | `20 Projects/` | `status`, `owner?`, `review_date?` |
| meeting | 单次会议记录 | `20 Projects/...` 或 `30 Meetings/` | `date`, `project?`, `participants?` |
| reference | 资料摘录、来源笔记 | `40 References/` | `source_type`, `source`, `status?` |
| permanent | 稳定知识结论 | `50 Notes/` | `created`, `updated?` |
| template | 模板 | `90 Templates/` | 无固定要求 |
| archive | 已完成、只读保留 | `99 Archive/` | `archived`, `archived_from?` |
| temp | 验证、试写、一次性产物 | `98 Temp/` | `expires_on?`, `cleanup_after?` |

## 4. 默认的 AI 协同原则

1. 未找到明确规范时，先沿用已存在模式，不自创新风格。
2. 未确认是新实体前，先搜索是否已有对应笔记。
3. 需要长期保存的内容写入 durable note；临时验证写入 temp 区。
4. 结构化字段只使用受控词表中的名称。
5. 做视图前先稳住字段；做迁移前先做审计。
