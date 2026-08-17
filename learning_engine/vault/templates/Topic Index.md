---
type: topic-index
domain: "{{domain}}"
topic: "{{topic}}"
---
# {{topic}}

## Purpose

Describe the scope of this topic and what belongs here.

## Skills

```dataview
TABLE exercise, name, mastery
FROM ""
WHERE type = "skill" OR contains(tags, "skill")
WHERE topic = this.topic
SORT exercise ASC
```

## References

Link source notes, books, courses, papers, and projects here.
