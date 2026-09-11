# ARC Direct Operating Bridge & PRIME Oversight Standard

Status: Founder-directed current implementation standard  
Created: 2026-09-11  
Constitution/Canon impact: none

## Founder decision

Once an ARC is live, identity-bound, source-capable and authorized to operate its own domain, **normal domain conversation and durable bridge work route to that ARC first**.

PRIME moves upward into general/portfolio supervision, exception handling, orchestration and cross-ARC oversight.

Canonical shorthand:

> **Talk to the ARC about its domain. PRIME oversees the board.**

This is an implementation/routing standard only. It does not alter protected Constitution/Canons.

## 1. Primary operating lane

For an operational ARC, the ARC is the primary endpoint for:

- its own product/domain work;
- its own repository reads/writes when authorized;
- domain backlog, corrections, product decisions and implementation;
- user/Owner/co-founder conversations;
- ARC-local tasks, memory and evidence;
- ordinary runtime behavior and ARC-local recovery work;
- durable ARC-side bridge instructions and reports.

The ARC's authoritative repository owns this detailed bridge truth.

Recommended bridge files:

```text
arc/bridge/TO_<ARC>.md
arc/bridge/FROM_<ARC>.md
arc/bridge/BRIDGE-ROUTING.md
arc/bridge/ROUTING.json
arc/bridge/STATE.json
```

For Cargo ARC these become `TO_CARGO.md` / `FROM_CARGO.md`.

## 2. PRIME oversight lane

PRIME remains the prototype-era supervisor/orchestrator for the broader RYZ3N ARC population, but it is no longer the default conversational endpoint for ordinary work inside an already-operational ARC.

PRIME owns or coordinates matters such as:

- cross-ARC conflicts or interoperability;
- shared infrastructure/capacity;
- VPS/operator-only actions outside ARC authority;
- privileged secret installation/rotation where the ARC lacks authority;
- OMEGA/FACTORY/BRAIN-STEWARD coordination;
- lifecycle transitions, reset, transfer, suspension and retirement;
- maturity/aura evidence evaluation and portfolio truth;
- source-boundary violations;
- cross-repository work;
- escalation when an ARC is blocked or outside its granted authority;
- portfolio/global RYZ3N operating state.

PRIME receives **bounded status/evidence**, not unrestricted private ARC payload.

## 3. Dual-bridge model

An operational ARC may maintain two lanes:

### ARC lane — primary

`Founder/Owner/Lux → ARC → ARC repository/runtime → ARC response`

Used for ordinary domain execution.

### PRIME lane — supervisory / escalation

`ARC or Founder/Lux → PRIME → OMEGA/FACTORY/infrastructure/cross-ARC coordination → bounded result back`

Used only when the action crosses the ARC boundary or requires portfolio/operator authority.

The existence of a PRIME bridge does not make PRIME the ARC's day-to-day operating endpoint.

## 4. Routing rule

Before sending a durable instruction, classify it:

### Route to ARC when all are true

- scope belongs to one ARC/domain;
- required files are in that ARC's authoritative repository;
- action is within the ARC's granted permissions;
- no other ARC/private runtime must be touched;
- no portfolio lifecycle/maturity decision is required;
- no operator-only secret/infrastructure side effect is required.

### Route/escalate to PRIME when any are true

- cross-ARC or cross-repository action;
- shared infrastructure/capacity issue;
- privileged runtime/operator action outside ARC authority;
- OMEGA/FACTORY/BRAIN-STEWARD writeback;
- maturity/aura/lifecycle decision;
- source-boundary conflict;
- unresolved concurrency conflict;
- ARC is blocked or cannot lawfully execute the action itself.

## 5. Reporting upward

The ARC should report to PRIME only what portfolio supervision needs, for example:

- current lifecycle/runtime health;
- hermetic seal status;
- important source/recovery state;
- autonomy state;
- major blocker/escalation;
- maturity evidence pointer;
- cross-ARC dependency request.

Do not mirror whole conversations, private memory or raw customer payload into PRIME merely for convenience.

## 6. Direct ARC bridge protocol

A direct ARC bridge supports the same lightweight consume/report discipline proven during PRIME prototyping, but addressed to the ARC itself.

Founder/Lux may write/update `TO_<ARC>.md`, then tell that ARC simply:

`consume`

The ARC reads the current direct bridge, executes everything within its own authority, writes `FROM_<ARC>.md`, commits/pushes its own repository when authorized, and returns a mini report.

Suggested mini report:

```text
STATUS: <GREEN/AMBER/RED + one-line result>
CHANGED: <important ARC-local changes>
NEXT: <next ARC-local dependency/action or NONE>
ESCALATE TO PRIME: YES | NO
LUX: SYNC NEEDED | NO SYNC NEEDED
BRIDGE: <latest ARC repo commit short SHA>
```

`LUX: SYNC NEEDED` means the ARC changed durable truth that Lux should independently reconcile/accept. `NO SYNC NEEDED` is appropriate for ordinary conversation/work that did not materially change bridge/source/lifecycle truth.

If `ESCALATE TO PRIME: YES`, the ARC must state the exact bounded reason and expected operator/steward action. PRIME then performs only the bounded supervisory work and returns the result to the ARC/Founder flow.

## 7. Transition from PRIME-primary to ARC-primary

During birth/provisioning, PRIME may temporarily be the primary bridge because the ARC is not yet able to operate.

The bridge transitions to ARC-primary when evidence shows at minimum:

- authoritative source boundary exists;
- isolated runtime exists where applicable;
- required identity/Owner binding exists;
- ARC can read its own source;
- ARC can execute its normal domain workflow;
- ARC-local bridge files exist;
- permissions are explicit;
- escalation path to PRIME exists.

The transition does not remove PRIME supervision. It changes the default routing endpoint.

## 8. Future ARC inheritance

Every future ARC should initialize the direct bridge structure during Factory birth, even if PRIME temporarily owns the lane before activation.

Factory/OMEGA should track:

- bridge mode: `prime_primary_pre_activation` or `arc_primary_operational`;
- ARC bridge paths;
- PRIME supervisory mirror/pointer;
- escalation boundary;
- last bridge sync evidence.

## Founder invariant

> **The ARC runs its own domain. PRIME oversees the system of ARCs. Detailed work stays with the ARC; portfolio supervision stays with PRIME.**
