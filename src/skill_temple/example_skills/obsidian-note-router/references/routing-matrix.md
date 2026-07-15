# Routing Matrix

## 1. 输入到笔记类型的默认映射

| 输入类型 | 默认去向 | 何时改为别的类型 |
| --- | --- | --- |
| 当天碎片、随手记录 | daily / inbox | 如果已经确认属于某项目或来源 |
| 项目状态更新 | project note | 如果其实是一次单独会议或周报 |
| 单次会议纪要 | meeting note | 如果用户明确只要写进 daily |
| 网页 / 论文 / 书籍摘录 | reference note | 如果只是极短摘抄且用户习惯先入 daily |
| 稳定知识结论 | permanent note | 如果仍处于资料摘录阶段 |
| AI 试写稿 / 中间转换产物 | temp note | 如果用户明确要求保留到 inbox |
| 无法判断去向但值得保留 | inbox note | 如果已有强匹配主笔记 |

## 2. 追加 vs 新建

| 条件 | 动作 |
| --- | --- |
| 同一实体、同一主记录、同一生命周期 | 追加 |
| 新事件、新来源、新时间片 | 新建 |
| 匹配不充分、重复风险高 | inbox / linked note / proposal only |
| 只是试验或验证 | temp |

## 3. 推荐的最小写入形式

- 更新旧笔记时：优先新增一个带标题的新 section。
- 新建 durable note 时：至少补 `note_type`、日期或来源、以及一条有效内部链接。
- 新建 temp note 时：文件名里加入 `tmp`、日期或工单标识，并定义清理条件。
