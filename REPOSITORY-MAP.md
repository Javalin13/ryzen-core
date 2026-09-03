# Ryzen Core — Current Repository Map

```yaml
---
type: repository-map
status: current-navigation
created: 2026-09-03
classification: reality
historical_numbering_preserved: true
amendable: true-additively
---
```

## Purpose

This is the current navigation map. Older files may accurately describe earlier 11/12/13-folder states; those counts are historical snapshots and should not be used as the current structure count.

## Current top-level structure

| Path | Current role |
|---|---|
| `00-foundation/` | Foundation/governance integration for this repo |
| `01-founder/` | Maps to Founder canonicals |
| `02-ryzen/` | Ryzen definition/architecture maps |
| `03-recovery-integration/` | Recovery evidence integration |
| `04-rebuild-integration/` | Rebuild-spec integration |
| `05-adrs/` | Ryzen Core architectural decisions |
| `06-runtime-roadmap/` | Historical/planned runtime roadmap |
| `07-runtime-scaffolding/` | Future runtime scaffolding; do not infer implementation from directory presence |
| `08-observability/` | Observability scaffolding |
| `09-cadences/` | Operating/review/intake cadence templates |
| `10-tools/` | Utility/support tooling |
| `10-lessons-learned/` | Operational lessons layer |
| `11-fleet-arc-intake/` | Fleet-specific validated ARC intelligence accumulation |
| `12-arc-productization/` | ARC commercial, capacity, provisioning, pilot and prototype-experience accumulation |
| `CURRENT-REALITY-2026-09.md` | Current operational reality overlay |
| `README.md` | Historical foundation entry point + links to current overlays |

## Reading order for a new maintainer/agent

1. `README.md`
2. `CURRENT-REALITY-2026-09.md`
3. `REPOSITORY-MAP.md`
4. Relevant ADRs in `05-adrs/`
5. `12-arc-productization/README.md` for current ARC product work
6. Historical runtime/rebuild files only as needed

## Rule

Do not “fix” historical numbering by deleting/renaming old folders. Preserve history and use this map as the current navigation layer.
