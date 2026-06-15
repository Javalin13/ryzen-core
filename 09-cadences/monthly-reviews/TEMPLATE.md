# Monthly Review — Template

```yaml
---
id: YYYY-MM
date_start: YYYY-MM-01
date_end: YYYY-MM-LAST
quarter: YYYY-QN
year: YYYY
projects_reviewed: [project1, project2, ...]
adrs_proposed: [NNNN, NNNN, ...]
adrs_accepted: [NNNN, NNNN, ...]
lessons_recorded: [YYYY-MM-DD-slug, ...]
amendable: true-additively
---

# YYYY-MM — Monthly Review (date_start to date_end)

## 1. Month in Summary

<One-paragraph summary of the month's work. The summary should answer: "What did we accomplish this month? What changed at the architecture level? What was the most important decision? What phase of the rebuild are we in?">

## 2. ADRs Accepted This Month

- ADR NNNN — <title> (status, date).
- ADR NNNN — <title> (status, date).

## 3. Weekly Reviews (chronological)

- `09-cadences/weekly-reviews/YYYY-WNN.md` — <one-line summary>.
- `09-cadences/weekly-reviews/YYYY-WNN.md` — <one-line summary>.

## 4. Daily Snapshots (chronological, abbreviated)

<list of all daily snapshots this month, with one-line summaries>

## 5. Lessons Learned (chronological)

<list of all lessons recorded this month, with one-line summaries>

## 6. Doctrine Compliance Check (monthly aggregate)

### Founder Reality Check Protocol (7-dimension scorecard, month average)

| Dimension | Average score this month | Trend vs last month |
|---|---|---|
| Revenue potential | <Low/Medium/High> | <up/down/same> |
| Execution cost | <Low/Medium/High> | <up/down/same> |
| Time cost | <Low/Medium/High> | <up/down/same> |
| Complexity cost | <Low/Medium/High> | <up/down/same> |
| Opportunity cost | <Low/Medium/High> | <up/down/same> |
| Strategic alignment | <Low/Medium/High> | <up/down/same> |
| Current priority alignment | <Low/Medium/High> | <up/down/same> |

**Overall: <ACCEPT / DEFER / DECLINE>** (per the founder canonical).

### Interpretation Protocol (5-tier classification, month totals)

- Total files: <count>
- Tier breakdown: <Reality: N, Active Execution: N, Approved Architecture: N, Strategic Vision: N, Research & Exploration: N>
- Files promoted: <count> (this month)
- Files demoted: <count> (this month)

### Founder Capability Model (7 execution risks, month review)

- Risks realized: <list, with actual outcomes>
- Risks mitigated: <list, with mitigations applied>
- New risks identified: <list>

## 7. Foundation Health (month-end)

- Foundation completeness: <percentage or status>
- Scaffolding placeholders: <count> directories, <count> READMEs
- ADRs (proposed/accepted/superseded): <count> / <count> / <count>
- Daily snapshots: <count>
- Lessons recorded: <count>
- 3 open founder decisions: <status of D1, D2, D3>
- Rebuild phase status: <Phase 0 / R1 / R2 / R3 / R4> and progress percentage

## 8. Strategic Insights (month-level)

- <insight> — context, impact, next steps.
- <insight> — context, impact, next steps.

## 9. Next Month's Priorities

1. <priority> — owner, target date.
2. <priority> — owner, target date.

## 10. Open Questions for the Founder

1. <question> — context, why it matters.
2. <question> — context, why it matters.

## 11. Cross-References

- All weekly reviews this month: <paths>
- All ADRs touched this month: <NNN, NNN, ...>
- All lessons recorded this month: <slugs>
- Canonical doctrine referenced: `Javalin13/ryzen-continuity/...`
- Recovery archive referenced: `Javalin13/ryzen-continuity/blob/main/04-recovery-archive/...`
- Rebuild spec referenced: `Javalin13/ryzen-continuity/blob/main/RYZEN-REBUILD-SPECIFICATION-v1.0.md`

---

## Template Notes

- Monthly reviews are **additive**: each new review is a new file; the previous review is not modified.
- The 11 sections are **fixed**: they do not change between reviews. New content is added to the existing sections.
- The Doctrine Compliance Check is **required**: every monthly review must include the 7-dimension scorecard, the 5-tier classification, and the 7 execution risks check.
- The "Open Questions for the Founder" section is the *founder-facing* section: the questions that need the founder's input. The 3 open founder decisions (D1, D2, D3) are surfaced here if they remain unresolved.
- The "Rebuild phase status" is the most important single piece of information: it tells the founder (and the team) where the runtime is in the 4-phase rebuild sequence.
