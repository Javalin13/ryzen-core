# Runtime Scaffolding — Reliable Excellence Inheritance

Date: 2026-09-14  
Status: **ACTIVE / DEFAULT INHERITANCE CONTRACT**

Governing sources:

- `00-foundation/RELIABLE-EXCELLENCE-ARCHITECTURAL-INVARIANT.md`
- `00-constitution/FOUNDER-CONSTITUTIONAL-AMENDMENT-2026-09-14-RELIABLE-EXCELLENCE.md`

## Rule

Every current and future component under `07-runtime-scaffolding/` inherits RYZ3N Mission Target #1 — **Reliable Excellence** — automatically.

This applies even when a component remains `NOT IMPLEMENTED`. The scaffolding is therefore not quality-neutral: it already carries the quality contract the eventual implementation must satisfy.

No subdirectory requires a separate opt-in.

## Apps

### `apps/arc-factory/`
Must manufacture repeatable, verifiable, recoverable, isolated and evidence-producing ARC packages rather than merely runnable ARC packages.

### `apps/fleet-arc/`
Must inherit the same ARC reliability obligations as every production ARC: correctness, responsiveness, predictable behavior, safe failure, recoverability, observability and truthful state.

### `apps/governance/`
Must enforce quality claims, authorization, state truthfulness, escalation and the minimum quality necessary for trustworthy execution.

### `apps/kernel-api/`
Must treat API availability, compatibility, latency, validation, idempotency where applicable, explicit errors and safe degradation as reliability properties.

### `apps/memory-federation/`
Must protect memory integrity, provenance, scope, isolation, freshness, recoverability and resistance to silent corruption or contamination.

## Packages

### `packages/brains/`
Brain contracts must make scope, competence, uncertainty, evidence and failure behavior explicit enough to evaluate reliability.

### `packages/core/`
Core orchestration and lifecycle mechanisms must be deterministic enough, observable, bounded and recoverable for their role. Core silently failing or silently changing state violates Reliable Excellence.

### `packages/schemas/`
Schemas must encode explicit contracts, validation and compatible evolution rather than allowing ambiguous state to flow downstream.

### `packages/verification/`
Verification is a direct enforcement mechanism for Reliable Excellence. It must test claims against reality and prevent one successful execution from being misrepresented as sustained reliability.

## Future additions

Any new `apps/`, `packages/`, infrastructure, adapters, runtimes or execution components created beneath this scaffolding inherit this file automatically.

A new component's design should state, at minimum:

1. intended behavior;
2. material failure modes;
3. material reliability dimensions;
4. validation/testing approach;
5. observability/diagnostic approach;
6. recovery/rollback behavior where relevant;
7. evidence required before a readiness or reliability claim.

## Standing red thread

**Know-how → High-Quality Execution → Verification → Proven Reliability → Reliable Excellence**

> Runtime implementation is not complete when it merely works. It matures when RYZ3N can trust, observe, recover and prove that it works as intended.
