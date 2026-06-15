# apps/governance/ — NOT IMPLEMENTED

```yaml
---
type: scaffolding
status: NOT-IMPLEMENTED
created: 2026-06-15
implements_concept: C4 (Governance Middleware) + C7 (Action Authorization Matrix) + C8 (Risk Classification)
rebuild_phase: R1 (C4) + R2 (C7, C8)
classification: approved-architecture
amendable: true-additively
```

## Status: NOT IMPLEMENTED

This directory is **scaffolded, not implemented**. Per the founder's direction 2026-06-15, no runtime code is written at this stage. The C4 Governance Middleware will be added in **R1**; the C7 Action Authorization Matrix and C8 Risk Classification will be added in **R2**.

## What will go here (in R1 and R2)

This directory will contain the **Governance Middleware** — the constitutional enforcement layer.

### R1 (Concept C4 — The Governance Middleware pattern)

In R1, this directory will contain:

- `middleware.py` — the `GovernanceMiddleware` class with the `validate_action` method
- `constitutional_constraints.py` — the 5 allowed action types (`arc_creation`, `task_execution`, `memory_access`, `governance_update`, `brain_execution`)
- `bounded_recursion.py` — the recursion cap (depth > 5 → blocked)
- `identity_continuity.py` — the creator_id validation for ARC creation
- `__init__.py` — the package init
- `tests/test_middleware.py` — the test suite

The C4 Governance Middleware is the *executable constitution* — every action in the kernel passes through `validate_action` before it executes.

### R2 (Concepts C7 and C8)

In R2, this directory will *extend* with:

- `authorization_matrix.py` — the Action Authorization Matrix (C7) — every brain, adapter, and engine declares CAN/CANNOT explicitly
- `risk_classification.py` — the Risk Classification (C8) — every action is classified LOW/MEDIUM/HIGH/CRITICAL
- `escalation.py` — the escalation logic for HIGH and CRITICAL actions
- `tests/test_authorization.py` — the authorization test suite
- `tests/test_risk.py` — the risk classification test suite

The C7 + C8 additions are the *production governance hardening* — they make the kernel safe for production deployment.

## Recovered evidence (in continuity's recovery archive)

The lost original runtime's Governance Middleware is recovered in:

- `Javalin13/ryzen-continuity/blob/main/04-recovery-archive/RECOVERED-CODE-INVENTORY.md` §"ryzen/apps/governance/" — describes the 1 file (`middleware.py`, 49 LOC)
- The recovered middleware is the *seed* for R1; R1 will write a *clean-slate implementation* informed by the recovered design.
- The 2 recovered governance rules (R-GOV-1, R-GOV-2) are documented in `Javalin13/ryzen-continuity/blob/main/04-recovery-archive/RECOVERED-GOVERNANCE-RULES.md` but are **NOT promoted to canonical** per founder direction.

## The "DO NOT IMPLEMENT" Reminder

Per the founder's direction 2026-06-15:

> Do not implement: Kernel runtime, Memory Federation, ARC Runtime, **Governance Middleware**, Agent Runtime at this stage.

The Governance Middleware is on the "do not implement" list. This scaffolding README is the *placeholder*, not the implementation.

## Cross-References

- `Javalin13/ryzen-continuity/blob/main/04-recovery-archive/RECOVERED-CODE-INVENTORY.md` — the recovered code inventory
- `Javalin13/ryzen-continuity/blob/main/04-recovery-archive/RECOVERED-GOVERNANCE-RULES.md` — the 2 recovered rules (NOT promoted)
- `Javalin13/ryzen-continuity/blob/main/RYZEN-REBUILD-SPECIFICATION-v1.0.md` §"R1" and §"R2" — the rebuild spec
- `00-foundation/GOVERNANCE.md` — the 10 foundation governance rules
- `04-rebuild-integration/RS-PHASES.md` — the rebuild spec integration map
