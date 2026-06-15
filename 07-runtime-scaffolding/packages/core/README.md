# packages/core/ — NOT IMPLEMENTED

```yaml
---
type: scaffolding
status: NOT-IMPLEMENTED
created: 2026-06-15
implements_concept: C1 (Cognition Loop) + C6 (8-state Task Lifecycle)
rebuild_phase: R1
classification: approved-architecture
amendable: true-additively
```

## Status: NOT IMPLEMENTED

This directory is **scaffolded, not implemented**. Per the founder's direction 2026-06-15, no runtime code is written at this stage. The Cognition Loop and the Task Graph Engine will be added in **R1**.

## What will go here (in R1)

This directory will contain the **Cognition Substrate** — the load-bearing design pattern of the runtime.

In R1, this directory will contain:

- `loop.py` — the `CognitionLoop` class (the **load-bearing** design pattern, **112 LOC** in the recovered code)
- `intent.py` — the `IntentParser` class (structured intent parsing; the canonical airport-pickup example)
- `task_graph.py` — the `TaskGraphEngine` class + the `TaskState` enum (8 states)
- `adapters.py` — the `ExecutionAdapter` ABC + the `MockBookingAdapter`
- `__init__.py` — the package init
- `tests/test_loop.py` — the cognition loop test suite
- `tests/test_intent.py` — the intent parser test suite
- `tests/test_task_graph.py` — the task graph test suite

The `CognitionLoop.run(arc_id, input_data, orchestrator_fn, brain_selector_fn)` is the **central method** of the runtime. It is the *literal* implementation of the canonical execution flow:

```
Input → Governance → Memory Context → Verification (Reasoning → Critique → Validation → Execution) → Memory Persistence → Output
```

## The 8-State Task Lifecycle (C6)

The C6 concept is an 8-state task lifecycle:

```
CREATED → VALIDATED → ASSIGNED → EXECUTING → VERIFIED → PERSISTED → COMPLETED
                                                              └──→ FAILED
```

The 8 states are *doctrine*. They are the lifecycle that every task in the kernel passes through. The state machine is exhaustive and immutable.

## The Canonical Worked Example: Airport Pickup

The recovered code's canonical worked example is the airport pickup:

> "Schedule airport pickup tomorrow at 14:00 from Brussels Airport to Antwerp."

The IntentParser parses this into a `StructuredIntent`:
- `intent = "schedule_booking"`
- `payload = {"from": "Brussels Airport", "to": "Antwerp", "datetime": "2026-MM-DD 14:00"}`
- `metadata = {"confidence": 1.0}`

The TaskGraphEngine decomposes this into a 5-node graph:

1. `validate_request` (depends on: nothing)
2. `check_availability` (depends on: validate_request)
3. `generate_pricing` (depends on: validate_request)
4. `validate_continuity` (depends on: check_availability, generate_pricing)
5. `execute_booking` (depends on: validate_continuity)

This is the *end-to-end cognition cycle* that the kernel actually executes.

## The "DO NOT IMPLEMENT" Reminder

Per the founder's direction 2026-06-15:

> Do not implement: **Kernel runtime**, Memory Federation, ARC Runtime, Governance Middleware, Agent Runtime at this stage.

The Kernel runtime (including the CognitionLoop) is on the "do not implement" list. This scaffolding README is the *placeholder*, not the implementation.

## Cross-References

- `Javalin13/ryzen-continuity/blob/main/04-recovery-archive/RECOVERED-CODE-INVENTORY.md` — the recovered code inventory
- `Javalin13/ryzen-continuity/blob/main/04-recovery-archive/RECOVERED-REUSABLE-CONCEPTS.md` §"C1" and §"C6" — the concepts
- `Javalin13/ryzen-continuity/blob/main/RYZEN-REBUILD-SPECIFICATION-v1.0.md` §"R1" — the rebuild spec
- `04-rebuild-integration/RS-PHASES.md` — the rebuild spec integration map
