# Daily Snapshot — Template

```yaml
---
id: YYYY-MM-DD
date: YYYY-MM-DD
week: YYYY-WNN
month: YYYY-MM
founder_present: yes | no
projects_touched: [project1, project2, ...]
adrs_proposed: [NNNN, NNNN, ...]
adrs_accepted: [NNNN, NNNN, ...]
adrs_referenced: [NNNN, NNNN, ...]
lessons_recorded: [YYYY-MM-DD-slug, YYYY-MM-DD-slug, ...]
risks_open: [N]
amendable: true-additively
---

# YYYY-MM-DD — Daily Snapshot

## 1. Completed work

- [project] Description of work completed. Reference file paths.
- [project] Description of work completed. Reference file paths.
- **[ADDITIVE — SAME DAY]** [project] Description of additive work completed (when applicable).

## 2. Decisions

- ADR NNNN — <title> (status).
- **[ADDITIVE — SAME DAY]** ADR NNNN — <title> (status).
- Founder decision — <description> (date, scope).

## 3. Open issues

- <issue> — owner.
- *(none)* if no open issues.

## 4. Risks

- <risk> — mitigation.
- *(none open)* if no open risks.

## 5. Lessons learned

- `10-lessons-learned/YYYY-MM-DD-slug.md` — <one-line summary>.
- **[ADDITIVE — SAME DAY]** `10-lessons-learned/YYYY-MM-DD-slug.md` — <one-line summary>.

## 6. Strategic insights

- <insight> — context.
- **[ADDITIVE — SAME DAY]** <insight> — context.

## 7. Next priorities

1. <priority> — owner.
2. <priority> — owner.

## 8. Traceability

- ADRs touched: `NNNN`, `NNNN`
- Canonical documents touched: `<path>`, `<path>`
- Lessons touched: `YYYY-MM-DD-slug`, `YYYY-MM-DD-slug`
- Recovery archive touched: `04-recovery-archive/<file>` (when applicable)
- Rebuild spec touched: `RYZEN-REBUILD-SPECIFICATION-v1.0.md` (when applicable)
- Remote: `<remote URL>` (when applicable)
- Linked daily snapshots: *(none yet — this is the first)*

---

## Template Notes

- Daily snapshots are **additive**: each new snapshot is a new file; the previous snapshot is not modified.
- The "ADDITIVE — SAME DAY" marker is used for changes that are appended to the same day's snapshot after the initial commit (per the continuity repo's pattern).
- The Traceability section is **required**: every daily snapshot must reference the ADRs, canonicals, lessons, and (when applicable) the recovery archive and rebuild spec that were touched.
- The 8 sections (Completed work, Decisions, Open issues, Risks, Lessons learned, Strategic insights, Next priorities, Traceability) are **fixed**: they do not change between snapshots. New content is added to the existing sections, not by adding new sections.
