# Audit Rubric

## 1. 严重度定义

| 等级 | 定义 | 典型例子 |
| --- | --- | --- |
| high | 直接影响搜索、链接、视图、任务、路由或导致重复写入 | `status/state/stage` 并存、项目主页重复、正式区混入 temp |
| medium | 持续制造维护成本，但短期不致命 | 标签层级漂移、模板字段过多、归档边界模糊 |
| low | 主要影响观感或局部一致性 | 日期格式偶有轻微变体、少量旧命名残留 |

## 2. 推荐审计维度

1. 命名与别名
2. 目录与落点
3. 标签词表
4. 属性名称与类型
5. 链接网络与孤儿笔记
6. 模板执行效果
7. 任务分布与闭环性
8. temp / scratch / generated 文件残留
9. archive 规则
10. Bases / Dataview / Canvas 依赖一致性

## 3. AI 污染信号

- 新属性名增长过快
- 同主题新建笔记过密
- 无来源总结大量落盘
- 旧笔记被局部接触后发生无关规范化改动
- temp 文件停留时间过长

## 4. 建议输出格式

- Findings summary
- High severity
- Medium severity
- Low severity
- Not worth fixing
- Suggested next skill
