# ADR INDEX — Ryzen Core

```yaml
---
type: adr-index
status: foundation-only
created: 2026-06-15
classification: approved-architecture
amendable: true-additively
```

## Purpose

This document is the **Architectural Decision Record (ADR) index** for the `ryzen-core` repository. It is **per-repository** — it tracks ADRs for this implementation-successor repository only. ADRs for the continuity repo (the canonical doctrine layer) are tracked in `Javalin13/ryzen-continuity/blob/main/09-decisions/INDEX.md`.

The format follows the continuity repo's pattern: sequentially numbered (NNNN), fixed status enum (`proposed | accepted | superseded-by-NNNN | deprecated`), additive only.

## Accepted

*No ADRs were accepted before this turn.*

[ADDITIVE — 2026-06-15] 0001 — Establish the Ryzen Core Repository Foundation
  Status: **accepted** (founder-authorized 2026-06-15)
  File: `05-adrs/0001-establish-ryzen-core-repository-foundation.md`
  Tags: #foundation #architecture #integration
  Supersedes: none
  Superseded by: 0002 (refines the strategic posture; does not supersede the foundation itself)

[ADDITIVE — 2026-06-15] 0002 — Clarify the Ryzen Core Foundation's Strategic Posture
  Status: **accepted** (founder-clarified 2026-06-15)
  File: `05-adrs/0002-clarify-strategic-posture-deferred-accumulation-first.md`
  Tags: #foundation #strategic-posture #fleet-arc-intake #accumulation
  Supersedes: none (refines the posture of 0001)
  Superseded by: none

## Proposed

*No proposed ADRs at this time.*

## Superseded

*No superseded ADRs at this time.*

## Deprecated

*No deprecated ADRs at this time.*

## Format

Each ADR has:
- A sequential 4-digit number (NNNN)
- A fixed status enum (proposed | accepted | superseded-by-NNNN | deprecated)
- A one-line title
- A tags list (#founder, #architecture, #integration, etc.)
- A `related_adrs` field (NNN, NNN, ...)
- A `related_docs` field (path, path, ...)
- A classification field (per the Interpretation Protocol's 5 tiers)
- An amendable field (true-additively)
- A body with the 7 sections: Status, Context, Decision, Consequences, Doctrine Compliance, Cross-References, ADR Format Notes

## Cross-References

- ADR Template: `05-adrs/TEMPLATE.md`
- Continuity ADRs: `Javalin13/ryzen-continuity/blob/main/09-decisions/INDEX.md`
- Continuity ADR Template: `Javalin13/ryzen-continuity/blob/main/09-decisions/TEMPLATE.md`
- Foundation Doctrine: `00-foundation/FOUNDATION.md`
- Foundation Governance: `00-foundation/GOVERNANCE.md`
- Foundation Interpretation Protocol: `00-foundation/INTERPRETATION-PROTOCOL.md`
