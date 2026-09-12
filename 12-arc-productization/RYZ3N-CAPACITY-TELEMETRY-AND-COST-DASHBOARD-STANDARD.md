# RYZ3N Capacity, Telemetry & Cost Dashboard Standard

**Status:** Founder-authorized canonical direction  
**Date:** 2026-09-12  
**Scope:** PRIME, OMEGA, FACTORY, every current ARC, every future ARC, and all model/provider capacity used by the RYZ3N ecosystem.

## 1. Purpose

RYZ3N requires one Founder-facing capacity control plane that answers, in near real time:

- how much model capacity exists;
- which ARC is consuming it;
- which provider/model is serving each workload;
- how much input, cached-input and output usage is being consumed;
- what the usage costs or is estimated to cost;
- how much subscription/included capacity remains;
- how many requests are active, queued, failed or rate-limited;
- how long requests wait and how long they take;
- which fallbacks are being used and why;
- whether current capacity is sufficient for the active ARC population;
- when the Founder should add or change capacity.

This dashboard is a RYZ3N infrastructure/governance surface. It is not an ARC Owner/customer dashboard and must not expose one Owner's private runtime data to another Owner.

## 2. Architectural ownership

### PRIME — runtime capacity steward

PRIME owns ecosystem-level runtime capacity observation, routing health, saturation detection, failover reporting, and Founder escalation. PRIME may recommend a capacity change but may not autonomously purchase credits, upgrade a plan, alter billing, or add a paid provider unless the Founder explicitly authorizes it.

### OMEGA — portfolio capacity oversight

OMEGA consumes aggregated telemetry to understand ARC population demand, growth, pressure, health, and projected capacity requirements. OMEGA does not inspect Owner-private prompt/message content.

### FACTORY — telemetry-by-birth

Every ARC created by the Factory must be born with the standard telemetry emitter/configuration required by this document. Telemetry is part of the ARC production baseline, not an optional later add-on.

### Individual ARCs

Each ARC emits its own bounded operational telemetry. An ARC may inspect its own capacity/usage data but must never read another ARC's Owner-private state or raw conversations.

## 3. Founder dashboard scope

The Founder dashboard must provide both an ecosystem summary and per-runtime drill-down for at least:

- PRIME;
- Cargo ARC;
- NARC;
- VONDA ARC;
- every future ARC registered by OMEGA/FACTORY;
- shared model/provider pools such as Ollama Cloud;
- eligible fallback providers such as NVIDIA routes;
- future providers without redesigning the dashboard.

## 4. Required telemetry per model invocation

Every model invocation should produce a telemetry event with the best data available from the runtime/provider. Required fields where available:

```text
request_id
trace_id
arc_id / runtime_id
workload_class
provider
model
account_or_capacity_pool_id (non-secret logical identifier only)
request_started_at
request_completed_at
latency_ms
queue_wait_ms
status
http_or_provider_status_class
input_tokens
cached_input_tokens
output_tokens
total_tokens
estimated_variable_cost
actual_provider_cost_if_available
currency
fallback_used
fallback_from
fallback_reason
retry_count
rate_limit_event
provider_error_class
active_concurrency_at_start
capacity_limit_known
```

If a provider does not expose a field, store `unknown`/`not_available`; do not fabricate values.

## 5. Privacy and data minimization — HARD

Central telemetry must not contain:

- raw prompts;
- raw responses;
- Telegram chat IDs or user IDs;
- pairing codes;
- passwords, tokens, API keys or secrets;
- Owner-private memories;
- uploaded file contents;
- customer personal data that is not necessary for capacity accounting.

The central dashboard tracks operational metadata, not conversation content.

A per-Owner or per-customer accounting identifier, if commercially needed, must be pseudonymous and scoped to its ARC. Founder/operator access to capacity metadata does not grant Owner-private namespace access.

## 6. Cost model

The dashboard must separate costs into distinct categories instead of presenting one misleading number.

### A. Fixed subscription cost

Examples: an Ollama subscription or another provider plan. Record the monthly fixed price and billing period as Founder-maintained commercial metadata.

### B. Included subscription capacity / credits

Track, where the provider exposes it:

- starting included allowance;
- consumed allowance;
- remaining allowance;
- percentage used;
- reset/billing date.

If provider-side remaining allowance is not programmatically available, show the calculated estimate as `estimated`, not `actual`.

### C. Variable model-equivalent usage

Use versioned provider/model price tables to calculate the theoretical or actual cost of input, cached input and output usage. Pricing must be date/version aware because provider pricing can change.

### D. Marginal paid overage

Show separately from included capacity. RYZ3N must never assume that included usage and incremental billing are the same thing.

### E. Shared infrastructure cost

The dashboard should be extensible to include non-model operational costs such as VPS, storage, email, domains, hosting and other shared infrastructure, but these must remain separately categorized from model usage.

## 7. Required views

### Ecosystem overview

Show:

- active ARCs;
- current provider/model per ARC;
- total requests today / 7d / 30d;
- input tokens;
- cached tokens;
- output tokens;
- total/estimated model cost;
- fixed subscription cost;
- included allowance consumed/remaining where known;
- current concurrent requests;
- configured concurrency ceiling where known;
- queue depth;
- average and p95 queue wait;
- average and p95 model latency;
- successful requests;
- failures;
- fallbacks;
- rate-limit events;
- capacity headroom.

### Per-ARC view

For each ARC show:

- primary and fallback route;
- request volume;
- token volume by type;
- cost attribution;
- latency;
- queue time;
- error rate;
- fallback rate;
- current sessions/workload pressure;
- month-to-date usage;
- forecast month-end usage;
- share of total RYZ3N capacity consumption.

### Provider/capacity-pool view

For each provider/account pool show:

- plan/tier metadata;
- known concurrency limit;
- current concurrency;
- saturation percentage;
- queue depth;
- included capacity/credit metadata where available;
- total usage attributed to the pool;
- per-model usage;
- error/rate-limit history;
- fallback pressure;
- projected exhaustion/saturation date if calculable.

## 8. Capacity priority classes

When shared capacity is constrained, workloads must be classifiable without violating ARC autonomy or Owner privacy.

Recommended baseline:

1. `customer_interactive` — highest ordinary priority;
2. `founder_interactive` — high priority;
3. `critical_runtime_recovery` — high priority during an active incident;
4. `prime_supervision` — normal priority;
5. `background_arc_work` — lower priority;
6. `brain_background` / batch enrichment — lowest ordinary priority.

Priority may control queue order. It must never silently grant access to another ARC's private state.

## 9. Capacity thresholds and Founder escalation

Dashboard thresholds should be configurable. Baseline indicators:

- below 50% sustained pool use: healthy;
- 50–70%: observe trend;
- 70–85%: capacity planning warning;
- 85–95%: Founder attention required;
- above 95% or repeated queue/rate-limit pressure: capacity escalation.

These thresholds are operational guidance, not automatic billing authority.

A capacity escalation may recommend actions such as:

- change workload scheduling;
- move background work out of peak periods;
- use an already-authorized fallback;
- change model choice within Founder-approved policy;
- upgrade/add provider capacity **only after explicit Founder authorization**.

## 10. Hard spend boundary

The dashboard and its agents may observe, calculate, forecast, warn and recommend. They may not autonomously:

- purchase credits;
- top up an account;
- upgrade a subscription;
- change billing details;
- enable a paid overage route;
- create additional paid provider accounts;
- raise a configured spending ceiling.

Existing Founder-authorized capacity may be used within its authorization. Any additional paid capacity requires explicit Founder approval.

## 11. Routing and fallback telemetry

Every fallback event must be visible. The dashboard should distinguish:

- primary healthy;
- primary saturated;
- primary rate-limited;
- primary provider error;
- credential/authentication failure;
- model unavailable/EOL;
- Founder-disabled route;
- fallback success;
- fallback failure;
- all routes exhausted / fail-closed.

Repeated fallback pressure is a capacity signal and must feed OMEGA/PRIME planning.

## 12. Forecasting

The dashboard should calculate, when enough data exists:

- daily/weekly/monthly token trend;
- cost trend;
- request trend;
- concurrency trend;
- projected billing-period consumption;
- projected point at which current capacity becomes inadequate;
- per-ARC marginal cost;
- portfolio cost if N additional ARCs behave like an existing ARC cohort.

Forecasts must be clearly labeled estimates.

## 13. ARC commercial economics

For commercial ARCs, the dashboard should eventually support a Founder-only unit-economics layer:

```text
ARC revenue
- allocated fixed infrastructure share
- variable model-equivalent usage
- marginal paid usage
- other attributable infrastructure
= estimated ARC contribution margin
```

This must not alter customer pricing automatically. It is decision support for RYZ3N governance/commercial planning.

## 14. Telemetry implementation boundary

Telemetry should use a small common event schema across all ARCs. Individual ARC runtimes emit events into an isolated/approved central capacity-telemetry sink. The central sink stores operational metadata only.

The implementation must be multi-provider from day one. Ollama Cloud is a current capacity pool, not a permanent hard-coded architectural dependency.

A provider adapter may enrich events using provider-specific usage/account APIs when available. Provider-derived values must be distinguishable from locally estimated values.

## 15. Minimum dashboard alerts

Founder-facing alerts should exist for:

- sustained concurrency saturation;
- abnormal queue growth;
- unusual cost acceleration;
- 70/85/95% allowance thresholds;
- provider rate-limit spikes;
- repeated fallback use;
- route failure;
- unexpected provider/model change;
- account allowance nearing exhaustion;
- an ARC consuming an anomalously high share of ecosystem capacity;
- missing telemetry from a runtime that should be active.

## 16. Current ecosystem bootstrap

The first implementation should ingest/attribute at least:

```text
PRIME
Cargo ARC
NARC
VONDA ARC
```

and the current model pool policy:

```text
Primary shared capacity: Ollama Cloud
Current primary model: minimax-m3:cloud
Authorized scope: existing Founder-authorized Ollama subscription capacity
Fallbacks: only routes separately authorized/eligible by current routing policy
Autonomous additional spend: NO
```

Exact plan limits, included credits and provider pricing are runtime/commercial metadata and must be read from current provider truth or Founder-entered configuration rather than frozen permanently in this canonical standard.

## 17. Factory inheritance requirement

Future Factory output must include:

- `arc_id` telemetry tag;
- runtime/provider/model tags;
- common capacity event emitter;
- local telemetry health check;
- central-sink registration;
- no-secret/no-content telemetry validation;
- cost-attribution readiness;
- capacity-priority default;
- dashboard registration through OMEGA/PRIME.

An ARC is not fully production-observable until this telemetry path is live.

## 18. Separation from maturity/aura

High usage, low usage, high cost, low cost, plan tier, concurrency allocation or telemetry availability do not themselves determine ARC maturity or aura. Capacity telemetry is an operational/commercial evidence layer, not a maturity shortcut.

## 19. Target Founder experience

The Founder should eventually be able to open one RYZ3N capacity screen and immediately see something equivalent to:

```text
RYZ3N MODEL CAPACITY
Pool health: HEALTHY
Current concurrent: 2 / <known limit>
Queue: 0
Month allowance used: <actual or estimated>
Month allowance remaining: <actual or estimated>
Projected month-end: <estimate>

PRIME   <usage> <cost> <latency> <fallbacks>
CARGO   <usage> <cost> <latency> <fallbacks>
NARC    <usage> <cost> <latency> <fallbacks>
VONDA   <usage> <cost> <latency> <fallbacks>

Provider pools
Ollama Cloud   <health/capacity/cost>
NVIDIA         <health/fallback usage>
...
```

with drill-down by ARC, provider, model and time period.

## 20. Delivery phases

### Phase 1 — telemetry foundation

Common event schema, per-runtime attribution, local collection, privacy validation, token/latency/fallback capture.

### Phase 2 — central capacity service

Aggregator, normalized storage, provider/model price table, pool state and forecasts.

### Phase 3 — Founder dashboard

RYZ3N UI for ecosystem, ARC and provider views plus threshold alerts.

### Phase 4 — Factory/OMEGA enforcement

All new ARCs inherit telemetry automatically; OMEGA can detect missing instrumentation and portfolio capacity pressure.

### Phase 5 — commercial intelligence

Per-ARC unit economics, cohort forecasting and capacity planning for scaled ARC commercialization.

---

**Founder decision:** RYZ3N will use a shared, observable, multi-provider capacity architecture rather than one opaque model account per ARC. Every ARC remains isolated at the identity/memory/runtime layer while capacity consumption is centrally measured as non-content operational telemetry.
