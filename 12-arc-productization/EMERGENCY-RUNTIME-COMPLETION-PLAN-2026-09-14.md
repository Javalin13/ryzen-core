# RYZ3N Emergency Runtime Completion Plan — 2026-09-14

**Status:** ACTIVE EMERGENCY BOOTSTRAP PLAN  
**Scope:** close M3 Cargo, restore stable PRIME execution, then accelerate M4 NARC and M5 VONDA  
**Founder direction:** finish the runtime mission quickly without abandoning the canonical architecture.

## Core diagnosis

The system is not suffering a fundamental Telegram, VPS, NVIDIA-auth or ARC-identity failure. The current delay comes from two coupled issues:

1. **Ultra provider instability / overload** in the default interactive lane. Real evidence showed Ultra returning HTTP 503 after ~56.96s while Super returned HTTP 200 in ~0.68s.
2. **Bootstrap paradox in the control plane.** PRIME is being asked to engineer the capability router / mission controller while its current top-level model behavior is itself unstable. Hermes recursion remains available, but mission completion is still too dependent on current-model obedience until the deterministic mission controller is implemented.

The correct emergency response is therefore to **stabilize PRIME and ARC execution externally first**, using source-controlled deterministic changes, and only then let PRIME resume self-hosted implementation.

## Emergency principle

> Do not ask an unstable control plane to rebuild itself under live load.

Use Lux + GitHub source truth + minimal deterministic runtime edits as the bootstrap authority. Once the runtime is stable, hand execution back to PRIME through the canonical `TO_PRIME.md` / `FROM_PRIME.md` bridge.

## Emergency target runtime

During bootstrap recovery:

```text
FAST / NORMAL EXECUTION -> NVIDIA Nemotron Super
DEEP REASONING          -> Ultra only as an explicit/selective lane after stability
MULTIMODAL              -> Omni perception
EMERGENCY CONTINUITY    -> local Qwen 0.6B
```

Ultra must not remain in the automatic ordinary-interaction retry path during emergency stabilization.

## Emergency phases

### E0 — Freeze and bootstrap

- no new architecture redesign;
- preserve current repos, Owner bindings, aura, maturity, memory and business logic;
- use current GitHub source truth and backups;
- externally change only the minimum runtime routing required for stability.

Acceptance: PRIME and Cargo use a stable fast execution path without repeated Ultra waits.

Target: 10–15 min.

### E1 — PRIME + Cargo fast-path proof

Prove both with real user paths:

- simple response;
- structured response;
- one Hermes tool/function call;
- no persona drift;
- no Ultra 503 retry wait in normal interaction;
- Omni path unchanged;
- local Qwen continuity still configured.

Acceptance: PRIME and Cargo both respond normally in seconds-class latency under healthy Super availability.

Target: 10–15 min.

### E2 — Accelerated NARC + VONDA migration

Apply the same proven bootstrap template to NARC then VONDA while preserving each profile's secrets, identity, Owner slot, memory and ARC-local bridge.

For each ARC:

- backup config/env;
- apply Super fast primary + Omni perception + Qwen emergency continuity;
- preserve Ultra as future/selective deep lane, not ordinary default;
- preserve Telegram runtime invariant where required;
- validate YAML/config;
- launch only that ARC;
- real Founder technical smoke without consuming an Owner slot;
- record real Owner proof as separate gate where external Owner participation is required.

Target technical runtime: 10–15 min per ARC if no new blocker.

### E3 — Minimal deterministic mission guard

After PRIME is stable, implement the smallest model-independent mission-control bootstrap before advanced dynamic routing:

- `consume` resolves current GitHub source first;
- durable mission state: PENDING / ACTIVE / VERIFYING / GREEN / BLOCKED / RECOVERING / FAILED;
- mission cannot close only because the model says `done`;
- required receipt/acceptance gates must be satisfied;
- session/provider reset resumes from GitHub/checkpoint rather than restarting mission context;
- generic persona prose and tool-free premature completion count as non-evidence;
- `FROM_PRIME.md` push remains mandatory for master engineering closure.

Target: 20–30 min for minimum viable guard after stable Super execution.

### E4 — Close receipts and return to canonical development

- update `FROM_PRIME.md` / ARC-local bridge receipts;
- update current execution pointer;
- update private Founder performance evidence;
- return PRIME to normal supervised execution;
- continue the richer capability router/circuit breaker and M6 capacity work from a stable base.

Target: 5–10 min.

## Expected emergency timeline

If no new infrastructure blocker appears:

- M3 Cargo technical GREEN: ~20–30 min from bootstrap start;
- M4 NARC technical GREEN: +10–15 min;
- M5 VONDA technical GREEN: +10–15 min;
- minimum mission guard + durable receipts: +20–30 min.

Practical target for technical runtime completion: roughly **60–90 minutes**.

External Owner-binding proofs remain separate external dependencies and must not be falsely marked complete if the actual Owner has not participated.

## What is already proven and must not be reopened

- NVIDIA credential works;
- Ultra, Super and Omni hosted endpoints have each returned successful direct tests;
- Super direct benchmark was ~0.68s in the real Cargo environment;
- Telegram raw API / HTTPX / PTB fundamentals are proven;
- PRIME real Founder -> PRIME -> Founder Telegram path is proven;
- Cargo real Founder -> Cargo -> Founder path is proven;
- Hetzner IPv6 / DNS64 / NAT64 investigation is closed context;
- `HERMES_TELEGRAM_DISABLE_FALLBACK_IPS=true` is a proven runtime invariant where required;
- current failure is not evidence of a fundamental Telegram/VPS architecture failure.

## Emergency authority boundary

During E0–E2, Lux may act as external bootstrap architect/controller through deterministic source-controlled runtime changes because PRIME is not yet a reliable controller for its own repair.

PRIME resumes engineering authority after the stable execution lane and mission guard are proven.

Founder remains final authority. Founder is never an ARC Owner merely for testing.
