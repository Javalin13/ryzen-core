# apps/kernel-api/ — NOT IMPLEMENTED

```yaml
---
type: scaffolding
status: NOT-IMPLEMENTED
created: 2026-06-15
implements_concept: C1 (Cognition Loop) and C4 (Governance Middleware) — the operational surface
rebuild_phase: R1
classification: approved-architecture
amendable: true-additively
---

## Status: NOT IMPLEMENTED

This directory is **scaffolded, not implemented**. Per the founder's direction 2026-06-15, no runtime code is written at this stage. The actual code will be added in **R1 (Ryzen Core Kernel MVP, ~1 month after R1 begins)**.

## What will go here (in R1)

This directory will contain the **Kernel API** — the FastAPI service that exposes the 5 canonical endpoints:

1. `GET /health` — health check
2. `POST /kernel/execute` — execute a task through the CognitionLoop
3. `POST /arcs/create` — create a new ARC from a topology
4. `POST /fleet/initialize` — initialize the Fleet ARC
5. `POST /fleet/request` — submit an operational request to the Fleet ARC
6. `GET /governance/audit` — retrieve the governance audit trail (R2)

The Kernel API is the **operational surface** of the runtime. It is the boundary between the runtime and its consumers (FleetConnect's business operations, the Fleet ARC's operational requests, the founder's CLI).

## Recovered evidence (in continuity's recovery archive)

The lost original runtime's Kernel API is recovered in:

- `Javalin13/ryzen-continuity/blob/main/04-recovery-archive/RECOVERED-CODE-INVENTORY.md` §"ryzen/apps/kernel_api/" — describes the 2 files (`main.py`, `__init__.py`)
- `Javalin13/ryzen-continuity/blob/main/04-recovery-archive/RECOVERED-CODE-INVENTORY.md` §"Recovered Files (detail) → apps/kernel_api/" — describes the 5 endpoints in detail

The recovered code shows:
- `main.py` is **101 LOC** (50 LOC of which are tests)
- The 5 endpoints use the FastAPI framework
- The runtime target is `http://localhost:8000`
- The recovered tests cover: health, execute authorized, execute forbidden scope, max recursion, missing task_id (5 tests)

## Recovered concept (C1 — The 5-stage Cognition Loop pattern)

The Kernel API exposes the 5-stage Cognition Loop as the `/kernel/execute` endpoint. The 5 stages are:

1. **Input** — receive the task input
2. **Governance Validation** — call `GovernanceMiddleware.validate_action`
3. **Memory Context Retrieval** — call `MemoryFederationLayer.retrieve_*`
4. **Recursive Verification** — call `RecursiveVerificationEngine.execute_cycle`
5. **Memory Persistence** — call `MemoryFederationLayer.store_memory`
6. **Output** — return the structured result

The 5-stage pattern is the *load-bearing design pattern* of the runtime. See `00-foundation/FOUNDATION.md` §"The 8 Reusable Concepts" and `04-rebuild-integration/RS-PHASES.md` for the full mapping.

## Rebuild spec reference

See `04-rebuild-integration/RS-PHASES.md` §"R1 — Ryzen Core Kernel MVP" for the full R1 deliverables.

## Cross-References

- `Javalin13/ryzen-continuity/blob/main/04-recovery-archive/RECOVERED-CODE-INVENTORY.md` — the recovered code inventory
- `Javalin13/ryzen-continuity/blob/main/RYZEN-REBUILD-SPECIFICATION-v1.0.md` §"R1 — Ryzen Core Kernel MVP" — the rebuild spec
- `00-foundation/FOUNDATION.md` — the foundation doctrine
- `04-rebuild-integration/RS-PHASES.md` — the rebuild spec integration map
