# M3 Performance System Completion Lock — 2026-09-15

Status: **ACTIVE / MUST CONTINUE UNTIL FULL ACHIEVEMENT**
Master: **M3/16 — Cargo ARC GREEN**
Owner authority: Founder
Architecture/acceptance control: Lux

## Founder directive

Keep the RYZ3N model-independent performance/cache/capacity execution line active until the system reaches successful full achievement. Do not stop at partial benchmarks, telemetry proof, stable-prefix identification, one fast model response, or a provider-specific workaround.

## Canonical architecture

See:

`12-arc-productization/ARC-MODEL-INDEPENDENT-PERFORMANCE-CACHE-AND-CAPACITY-STANDARD.md`

That standard is binding for future interventions unless explicit contradictory evidence and Founder-governed architectural review justify a revision.

## Current proven checkpoint

- E1.17 cache/runtime surface: GREEN
- E1.18 middleware/telemetry seam: GREEN
- E1.19 Cache Controller shadow telemetry: GREEN
- E1.20 stable-prefix continuity: GREEN
- E1.21 repeated-context/provider-cache measurement: GREEN

E1.21 evidence:
- stable prefix: 32,837 chars
- stable share of message payload: 98.7965%
- stable share of full request chars: 98.1029%
- successful Laguna/NVIDIA full PRIME turn: 4.747837s
- provider input tokens: 20,192
- provider-reported cached input: 0
- output discipline still imperfect (`/think*` leakage observed)

## E1.22 correction / implementation rule

A local hash or local cache does **not** by itself reduce remote stateless inference input. A hosted model cannot obey instructions it never receives unless the provider/runtime exposes a persistent-context or prefix/KV reuse mechanism.

Therefore E1.22 must not implement a fake cache reference such as `hash -> omitted prompt` and call it acceleration.

The provider-independent intervention is a **verified runtime context compiler**:

1. retain the full canonical PRIME/ARC source as authority;
2. identify the smallest always-on constitutional/runtime kernel that must be present on every turn;
3. classify stable material into always-on, task-relevant retrievable, tool/capability-derived, state/mission-derived, redundant/legacy, and optional/deep-context blocks;
4. compile a shorter deterministic runtime kernel;
5. inject additional doctrine/context only when the request/capability requires it;
6. version and fingerprint compiled output;
7. prove semantic/constitutional parity before production activation;
8. measure before/after request chars, actual provider input tokens, latency and behavior;
9. preserve rollback to the full authoritative prompt;
10. combine this with native provider prefix/KV reuse whenever the provider actually supports it.

## Completion sequence

After E1.22, continue without architectural drift through:

- context-compiler parity proof;
- measured token/request-pressure reduction;
- in-flight duplicate coalescing;
- safe result-cache eligibility gates;
- health-aware routing and circuit breaker;
- bounded retries/fallbacks;
- exact output discipline / hidden-reasoning leakage prevention;
- realistic PRIME interactive + tool-bearing acceptance;
- Cargo parity and isolation proof;
- NARC/VONDA/future ARC inheritance template;
- capacity-dashboard normalization;
- Ollama dependency removal once replacement continuity is proven;
- A→Z regression, rollback and recovery proof;
- Reliable Excellence production receipt.

Until those applicable gates are GREEN, the performance system remains **ACTIVE / INCOMPLETE**.
