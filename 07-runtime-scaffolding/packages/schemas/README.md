# packages/schemas/, packages/shared/, infrastructure/docker/, docs/ — NOT IMPLEMENTED

```yaml
---
type: scaffolding
status: NOT-IMPLEMENTED
created: 2026-06-15
implements_concept: Schemas + Shared utilities + Docker infrastructure + Documentation
rebuild_phase: R1
classification: approved-architecture
amendable: true-additively
```

## Status: NOT IMPLEMENTED

These four directories are **scaffolded, not implemented**. Per the founder's direction 2026-06-15, no runtime code is written at this stage. They are part of the **R1** scope but not at the foundation stage.

## What will go here (in R1)

### packages/schemas/ — SQLAlchemy ORM models (7 tables)

In R1, this directory will contain:

- `models.py` — the 7 SQLAlchemy ORM models: `ARC`, `Brain`, `MemoryEntry`, `Task`, `Customer`, `Booking`, `ExecutionTrace`
- `__init__.py` — the package init
- `tests/test_models.py` — the test suite (closes the 0-test gap from the recovered code)

The schemas are the *truth substrate* — every data structure in the kernel is defined here. The recovered code has **0 tests on schemas**; the future build will close this gap.

### packages/shared/ — Structured Logging

In R1, this directory will contain:

- `logging.py` — the JSON-formatted structured logger with `trace_id`, `arc_id`, `brain_id` propagation — **46 LOC** in the recovered code
- `__init__.py` — the package init
- `tests/test_logging.py` — the test suite (closes the 0-test gap from the recovered code)

The structured logging primitive is the *observability substrate* — it is the foundation of all dashboards, alerts, and audit trails.

### infrastructure/docker/ — Docker compose

In R1, this directory will contain:

- `docker-compose.yml` — the **21-LOC** docker-compose.yml from the recovered code (PostgreSQL + pgvector + Redis)
- `README.md` — the infrastructure documentation

The docker-compose is the *deployment substrate* — it is the foundation of the local development environment.

### docs/ — Documentation

In R1, this directory will contain 4 subdirectories (matching the recovered code's structure):

- `canonical/` — cross-cutting canonical documentation
- `architecture/` — architecture documentation
- `governance/` — governance documentation
- `implementation/` — implementation documentation

Each subdirectory will have a `README.md` that documents the runtime's design, architecture, governance, and implementation choices. The recovered code has 4 docs files (**41 LOC** total); the future build will expand on this.

## The "DO NOT IMPLEMENT" Reminder

Per the founder's direction 2026-06-15:

> Do not implement: **Kernel runtime** (schemas + shared utilities are part of the kernel), Memory Federation, ARC Runtime, Governance Middleware, Agent Runtime at this stage.

These four directories are part of the Kernel runtime. They are on the "do not implement" list. These scaffolding READMEs are the *placeholders*, not the implementations.

## Cross-References

- `Javalin13/ryzen-continuity/blob/main/04-recovery-archive/RECOVERED-CODE-INVENTORY.md` — the recovered code inventory
- `Javalin13/ryzen-continuity/blob/main/RYZEN-REBUILD-SPECIFICATION-v1.0.md` §"R1" — the rebuild spec
- `04-rebuild-integration/RS-PHASES.md` — the rebuild spec integration map
