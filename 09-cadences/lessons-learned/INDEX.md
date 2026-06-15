# Lessons Learned — Index

Additive, chronological, with topic tags. New rows are appended; never reordered, never removed.

## Format

```
YYYY-MM-DD — <short slug>
  Tags: <#tag #tag>
  Projects: <project list>
  Related ADRs: <NNN ...>
  One-line summary: <one sentence>
```

---

## 2026-06-15

*No lessons recorded at the foundation stage. The first lessons will be recorded when the foundation is committed, tagged, and (optionally) pushed to the remote.*

---

## Template Notes

- The lessons INDEX is **additive**: each new lesson is appended; no row is ever reordered or removed.
- The format is **fixed**: every row has the same 5 fields (slug, tags, projects, related ADRs, one-line summary).
- The lessons INDEX is **per-repository**: it tracks lessons for this implementation-successor repository only. Lessons for the continuity repo (the canonical doctrine layer) are tracked in `Javalin13/ryzen-continuity/blob/main/10-lessons-learned/INDEX.md`.
- Each lesson has a corresponding file at `09-cadences/lessons-learned/YYYY-MM-DD-<slug>.md` with the full content.
- Lessons are **operational**: they are the lessons the team would tell a future implementer ("we made these mistakes; do not repeat them"). They are not philosophy; they are guidance.

## Cross-References

- Continuity lessons INDEX: `Javalin13/ryzen-continuity/blob/main/10-lessons-learned/INDEX.md`
- Continuity lesson pattern: `Javalin13/ryzen-continuity/blob/main/10-lessons-learned/2026-06-15-recovered-doctrine-is-the-durable-capital.md` (the lesson the recovery archive embodies)
