# packages/brains/ — NOT IMPLEMENTED

```yaml
---
type: scaffolding
status: NOT-IMPLEMENTED
created: 2026-06-15
implements_concept: Brain contracts (BaseBrain, GenericBrain, role-specific brains)
rebuild_phase: R1 (BaseBrain + GenericBrain) + R3 (real brain implementations)
blocked_by: D1 (real brain implementation strategy)
classification: approved-architecture
amendable: true-additively
```

## Status: NOT IMPLEMENTED

This directory is **scaffolded, not implemented**. Per the founder's direction 2026-06-15, no runtime code is written at this stage. The BaseBrain + GenericBrain will be added in **R1**; the real brain implementations (Sales, Operations, Pricing, etc.) will be added in **R3**.

## What will go here (in R1 and R3)

This directory will contain the **Brain contracts** — the standardization for the cognitive units within ARCs.

### R1 (Brain contracts)

In R1, this directory will contain:

- `base.py` — the `BaseBrain` abstract class (the contract) — **58 LOC** in the recovered code
- `generic.py` — the `GenericBrain` concrete class — **placeholder** in R1
- `__init__.py` — the package init
- `tests/test_brains.py` — the test suite

The `BaseBrain` contract has 2 methods:

```python
class BaseBrain(ABC):
    async def execute(self, task_input, context) -> dict: pass
    async def coordinate(self, target_role, request, loop) -> dict:
        # Delegates via the loop (passed in)
```

The `GenericBrain` is a *concrete implementation* that returns a placeholder result. In R1, all 7 Fleet ARC brains (Sales, Operations, Pricing, etc.) are instantiated as `GenericBrain` instances with different `name` and `role` values.

### R3 (Real brain implementations)

In R3, this directory will *extend* with real brain implementations:

- `sales.py` — real Sales brain (D1: function / LLM / external API / hybrid / pluggable)
- `operations.py` — real Operations brain
- `pricing.py` — real Pricing brain
- `customer_continuity.py` — real Customer Continuity brain
- `analytics.py` — real Analytics brain
- `governance.py` — real Governance brain
- `memory_continuity.py` — real Memory Continuity brain

The R3 extensions are *blocked* by the **D1 founder decision** (real brain implementation strategy). Until the founder decides, R1's `GenericBrain` is the *placeholder*.

## The D1 Open Decision

The recovery archive's `OPEN-DECISIONS.md` codifies the **D1 — Real Brain Implementation Strategy** decision. The 5 options:

| Option | Description | Pros | Cons |
|---|---|---|---|
| **Pure function/class** | Each brain is a Python function or class with deterministic logic | Inspectable, testable, no LLM cost | Cannot handle unstructured input, brittle to change |
| **LLM call** | Each brain is a wrapper around an LLM call with a system prompt | Flexible, can handle unstructured input | Cost, latency, non-deterministic, harder to test |
| **Hybrid (LLM with deterministic guardrails)** | LLM call for the core logic, with deterministic pre/post-processing | Flexible + governable | Most complex, hardest to test |
| **External API** | Each brain is a wrapper around a third-party API | Real-world integration | Vendor lock-in, API cost, latency |
| **Pluggable** | A brain is a contract; the implementation can be any of the above | Most flexible | Most architecture; risk of over-engineering |

**Hermes's recommendation:** Hybrid for Sales, Operations, Pricing (the *commercial* brains); external API for CRM, payments, notifications (the *integration* brains); pure function/class for Governance, Memory Continuity, Analytics (the *internal* brains). This matches the doctrine's "different specialization for different roles" principle and keeps each brain as simple as possible.

**Decision required from founder:** Which implementation strategy? Or: which *brains* get which strategy?

## The "DO NOT IMPLEMENT" Reminder

Per the founder's direction 2026-06-15:

> Do not implement: Kernel runtime, Memory Federation, **ARC Runtime** (which includes the brains), Governance Middleware, **Agent Runtime** at this stage.

The brains are part of the ARC Runtime and the Agent Runtime. Both are on the "do not implement" list. This scaffolding README is the *placeholder*, not the implementation.

## Cross-References

- `Javalin13/ryzen-continuity/blob/main/04-recovery-archive/RECOVERED-CODE-INVENTORY.md` — the recovered code inventory
- `Javalin13/ryzen-continuity/blob/main/04-recovery-archive/OPEN-DECISIONS.md` — the 3 open decisions (D1, D2, D3)
- `Javalin13/ryzen-continuity/blob/main/RYZEN-REBUILD-SPECIFICATION-v1.0.md` §"R1" and §"R3" — the rebuild spec
- `04-rebuild-integration/RS-PHASES.md` — the rebuild spec integration map
