# Weekly Review — Template

```yaml
---
id: YYYY-WNN
date_start: YYYY-MM-DD
date_end: YYYY-MM-DD
month: YYYY-MM
quarter: YYYY-QN
projects_reviewed: [project1, project2, ...]
adrs_proposed: [NNNN, NNNN, ...]
adrs_accepted: [NNNN, NNNN, ...]
lessons_recorded: [YYYY-MM-DD-slug, ...]
amendable: true-additively
---

# YYYY-WNN — Weekly Review (date_start to date_end)

## 1. Week in Summary

<One-paragraph summary of the week's work. The summary should answer: "What did we accomplish this week? What changed? What was the most important decision?">

## 2. ADRs Accepted This Week

- ADR NNNN — <title> (status, date).
- ADR NNNN — <title> (status, date).

## 3. Daily Snapshots (chronological)

- `09-cadences/daily-snapshots/YYYY-MM-DD.md` — <one-line summary>.
- `09-cadences/daily-snapshots/YYYY-MM-DD.md` — <one-line summary>.

## 4. Lessons Learned (chronological)

- `10-lessons-learned/YYYY-MM-DD-slug.md` — <one-line summary>.

## 5. Doctrine Compliance Check

### Founder Reality Check Protocol (7-dimension scorecard)

| Dimension | Score this week | Trend vs last week |
|---|---|---|
| Revenue potential | <Low/Medium/High> | <up/down/same> |
| Execution cost | <Low/Medium/High> | <up/down/same> |
| Time cost | <Low/Medium/High> | <up/down/same> |
| Complexity cost | <Low/Medium/High> | <up/down/same> |
| Opportunity cost | <Low/Medium/High> | <up/down/same> |
| Strategic alignment | <Low/Medium/High> | <up/down/same> |
| Current priority alignment | <Low/Medium/High> | <up/down/same> |

**Overall: <ACCEPT / DEFER / DECLINE>** (per the founder canonical).

### Interpretation Protocol (5-tier classification)

- New files added this week: <count>
- Tier breakdown: <Reality: N, Active Execution: N, Approved Architecture: N, Strategic Vision: N, Research & Exploration: N>

### Founder Capability Model (7 execution risks)

- Active risks: <list>
- Mitigations applied: <list>
- New risks identified: <list>

## 6. Foundation Health

- Foundation completeness: <percentage or status>
- Scaffolding placeholders: <count> directories, <count> READMEs
- ADRs (proposed/accepted/superseded): <count> / <count> / <count>
- Daily snapshots: <count>
- Lessons recorded: <count>
- 3 open founder decisions: <status of D1, D2, D3>

## 7. Next Week's Priorities

1. <priority> — owner, target date.
2. <priority> — owner, target date.

## 8. Open Questions for the Founder

1. <question> — context, why it matters.
2. <question> — context, why it matters.

## 9. Cross-References

- All daily snapshots this week: <paths>
- All ADRs touched this week: <NNN, NNN, ...>
- All lessons recorded this week: <slugs>
- Canonical doctrine referenced: `Javalin13/ryzen-continuity/...`
- Recovery archive referenced: `Javalin13/ryzen-continuity/blob/main/04-recovery-archive/...`
- Rebuild spec referenced: `Javalin13/ryzen-continuity/blob/main/RYZEN-REBUILD-SPECIFICATION-v1.0.md`

---

## Template Notes

- Weekly reviews are **additive**: each new review is a new file; the previous review is not modified.
- The 9 sections are **fixed**: they do not change between reviews. New content is added to the existing sections.
- The Doctrine Compliance Check is **required**: every weekly review must include the 7-dimension scorecard, the 5-tier classification, and the 7 execution risks check.
- The "Open Questions for the Founder" section is the *founder-facing* section: the questions that need the founder's input. The 3 open founder decisions (D1, D2, D3) are surfaced here if they remain unresolved.
