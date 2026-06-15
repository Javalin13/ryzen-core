# apps/arc-factory/ — NOT IMPLEMENTED

```yaml
---
type: scaffolding
status: NOT-IMPLEMENTED
created: 2026-06-15
implements_concept: ARC Factory (the capability that generates ARCs)
rebuild_phase: R1
classification: approved-architecture
amendable: true-additively
```

## Status: NOT IMPLEMENTED

This directory is **scaffolded, not implemented**. Per the founder's direction 2026-06-15, no runtime code is written at this stage. The ARC Factory will be added in **R1**.

## What will go here (in R1)

This directory will contain the **ARC Factory** — the capability that generates ARCs from a topology.

In R1, this directory will contain:

- `factory.py` — the `ARCFactory` class with the `create_arc` method
- `topology.py` — the topology data structure (a Python constant or a YAML config)
- `constitution.py` — the constitutional validation (the ARC Creation Doctrine's 4 validation triggers)
- `__init__.py` — the package init
- `tests/test_factory.py` — the test suite

The ARC Factory is the *first real Ryzen capability* — it is the system that turns a *topology* (a set of brains with roles and specializations) into a *running ARC*.

## The ARC Creation Doctrine (4 Validation Triggers)

The canonical ARC Creation Doctrine codifies 4 validation triggers that an ARC must pass *before* it is created:

1. **Operational necessity** — there is a real operational need that no existing ARC can serve.
2. **Strategic opportunity** — creating the ARC unlocks a strategic opportunity (e.g., a new market, a new domain).
3. **Knowledge gap** — creating the ARC fills a knowledge gap in the system.
4. **Long-term specialization need** — the work is *recurring* and *specialized*; it deserves its own ARC.

The first 3 first-generation ARCs (FleetConnect, Earth, FamilieKompas) are *already canonical*. The next ARC creation requires one of the 4 triggers.

## Recovered evidence (in continuity's recovery archive)

The lost original runtime's ARC Factory is recovered in:

- `Javalin13/ryzen-continuity/blob/main/04-recovery-archive/RECOVERED-CODE-INVENTORY.md` §"ryzen/apps/arc_factory/" — describes the 1 file (`factory.py`, 44 LOC)
- The recovered factory is the *seed* for R1; R1 will write a *clean-slate implementation* informed by the recovered design.

## The "DO NOT IMPLEMENT" Reminder

Per the founder's direction 2026-06-15:

> Do not implement: Kernel runtime, Memory Federation, **ARC Runtime**, Governance Middleware, Agent Runtime at this stage.

The ARC Runtime is on the "do not implement" list. The ARC Factory is the *generator* of ARCs; it is part of the ARC Runtime substrate. This scaffolding README is the *placeholder*, not the implementation.

## Cross-References

- `Javalin13/ryzen-continuity/blob/main/04-recovery-archive/RECOVERED-CODE-INVENTORY.md` — the recovered code inventory
- `Javalin13/ryzen-continuity/blob/main/02-ryzen/RYZEN-CANONICAL.md` §"ARC Creation Doctrine" — the canonical ARC Creation Doctrine
- `Javalin13/ryzen-continuity/blob/main/RYZEN-REBUILD-SPECIFICATION-v1.0.md` §"R1" — the rebuild spec
- `04-rebuild-integration/RS-PHASES.md` — the rebuild spec integration map
