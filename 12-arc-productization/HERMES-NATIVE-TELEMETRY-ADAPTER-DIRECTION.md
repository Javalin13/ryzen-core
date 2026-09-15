# Hermes Native Telemetry Adapter Direction

**Status:** Architectural direction — sidecar to M3 E1 cache implementation
**Date:** 2026-09-15
**Scope:** PRIME, Cargo ARC, NARC, VONDA ARC, future Factory-born ARCs, and the Founder Capacity/Telemetry Dashboard.

## Decision

Use Hermes' native API/request observability as a runtime sensor feeding the existing RYZ3N Capacity, Telemetry & Cost Dashboard standard.

Hermes is an emitter/adapter source, not the owner of the RYZ3N telemetry schema. RYZ3N remains runtime/provider-independent so another agent runtime can emit the same canonical event contract later.

## Proven live Hermes surfaces

The live PRIME Hermes checkout exposes:

- `pre_api_request` and `post_api_request` hooks;
- `api_request_error` path;
- `api_request_id`, task/turn/session context, provider and model identity;
- request-size telemetry including `approx_input_tokens` and `request_char_count`;
- retry/middleware trace fields;
- normalized cache accounting for cached/read/write token shapes across provider adapters;
- session and insights accounting for cache-read/cache-write totals;
- behavior-changing LLM middleware (`llm_request`, `llm_execution`) which can also emit cache/router telemetry.

## Mapping into the existing RYZ3N canonical event

Hermes-native -> RYZ3N canonical:

- `api_request_id` -> `request_id`
- task/turn identifiers -> `trace_id` components
- profile/runtime registration -> `arc_id` / `runtime_id`
- provider/model -> `provider` / `model`
- hook timestamps/duration -> request start/end + `latency_ms`
- request token estimate -> provisional input estimate before completion
- normalized provider usage -> `input_tokens`, `cached_input_tokens`, `output_tokens`, `total_tokens`
- retry/error hook -> `retry_count`, `provider_error_class`, `rate_limit_event`, status class
- route attempt/success sequence -> fallback detection and fallback reason
- middleware trace -> cache/router decision evidence, stripped of content

## Fields RYZ3N must add itself

Hermes alone does not define every capacity field. RYZ3N should calculate or attach:

- `arc_id` / canonical runtime identity;
- workload class / priority;
- logical capacity-pool id;
- active concurrency and RYZ3N queue depth;
- queue wait time;
- known provider/pool ceiling and derived saturation/headroom;
- provider entitlement/allowance state;
- RYZ3N cost attribution and forecast;
- cache-controller metrics such as prefix fingerprint, exact-cache eligibility/hit, in-flight dedup hit, context bytes/tokens avoided, and provider-cache ratio where reported.

## Privacy boundary — HARD

Hermes observer hooks can expose raw request/messages internally. The RYZ3N telemetry adapter MUST discard content before persistence/transport.

Persist metadata only. Never persist through the central telemetry sink:

- prompts or model responses;
- raw conversation history;
- Telegram/chat/user identifiers;
- secrets/tokens/API keys;
- Owner-private memories or files.

Use pseudonymous ARC/runtime identifiers and operational metadata only.

## Cache-controller synergy

E1 cache work and capacity telemetry should share one measurement plane.

For every inference attempt, the cache/router layer should emit enough metadata to calculate:

- raw request tokens/characters before optimization;
- effective request tokens after context compilation;
- provider-reported cached input tokens;
- RYZ3N response-cache hit/miss (only when safe/eligible);
- in-flight dedup/coalescing hit count;
- context tokens/bytes avoided;
- provider call avoided yes/no;
- selected route and route-switch reason;
- endpoint health state at decision time;
- latency and outcome.

This allows the Founder dashboard to measure not only consumption, but **efficiency gained by RYZ3N orchestration**.

## Derived dashboard metrics

Recommended derived calculations include:

- provider cache ratio = cached_input / total_input_before_provider-normalization;
- RYZ3N context reduction ratio = 1 - effective_context / raw_context;
- inference avoidance ratio = avoided_provider_calls / eligible_requests;
- dedup amplification saved = coalesced_waiters served per actual provider call;
- effective capacity multiplier = useful logical requests / physical provider calls;
- ARC capacity share = ARC normalized usage / ecosystem normalized usage;
- pool pressure = active_concurrency / known_capacity_ceiling when known;
- saturation/fallback pressure over rolling windows;
- p50/p95 latency by ARC, provider, model, route and cache state.

Never fabricate provider ceilings or allowance figures; mark unknown when unavailable.

## Architectural placement

```text
Hermes / other runtime
        | native hooks + normalized usage
        v
RYZ3N Telemetry Adapter
        | content-stripped canonical event
        v
RYZ3N Capacity Telemetry Sink
        | aggregations + forecasts
        +--> PRIME runtime stewardship
        +--> OMEGA portfolio oversight
        +--> Founder Capacity Dashboard
```

The RYZ3N Cache Controller and free-endpoint router should publish to the same canonical sink rather than creating a separate observability stack.

## Implementation timing

Do not derail M3 E1 cache implementation. During E1.19+ shadow-mode work, emit telemetry locally first. Reuse those events later for the Phase-1 capacity telemetry foundation and Founder dashboard.

This converts current cache engineering into reusable dashboard instrumentation with almost no duplicate measurement work.
