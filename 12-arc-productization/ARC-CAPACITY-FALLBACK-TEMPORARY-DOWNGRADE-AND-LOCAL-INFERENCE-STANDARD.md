# RYZ3N ARC Local-First Inference & Resilience Standard

**Status:** CANONICAL — Founder directive 2026-09-12  
**Scope:** PRIME, Cargo, NARC, VONDA, OMEGA/Factory inheritance, and every future ARC.

> **Supersession note — 2026-09-12:** Ollama Cloud MiniMax M3 is PRIME-only as the normal cloud primary. ARCs are local-model-first. Previous ARC Owner usage-limit / temporary-downgrade messaging tied to daily/weekly/monthly AI allowances is retired.

## 1. Purpose

RYZ3N separates the intelligence route used by PRIME from the route used by Owner-facing ARCs.

Target architecture:

```text
Founder → PRIME
          ├─ primary: Ollama Cloud MiniMax M3
          ├─ fallback: verified shared local model
          └─ fallback: Founder-authorized verified-free external route(s)

Owners → Cargo / NARC / VONDA / future ARCs
          ├─ primary: verified shared local model
          ├─ fallback: Founder-authorized verified-free external route(s)
          └─ unavailable: sanitized service message
```

The Owner-facing ARC fleet must not consume PRIME's Ollama Cloud MiniMax M3 pool during normal operation.

## 2. Canonical roles remain unchanged

- John / Jan = `founder` everywhere.
- Every non-Founder human receiving/using an ARC = `owner`.
- Business/domain titles are metadata only.

Inference routing must never alter role state, Owner binding, private namespaces, form, aura or maturity.

## 3. Local inference is the ARC normal route

After the required hardware and Hermes capability gates are GREEN:

- Cargo primary model route = shared local inference service.
- NARC primary model route = shared local inference service.
- VONDA primary model route = shared local inference service.
- future Factory-created ARCs inherit shared-local-primary compatibility by default.
- ARC configs must not point to `ollama-cloud/minimax-m3:cloud` unless the Founder explicitly creates a future exception.

The local model is installed once and served as shared inference infrastructure. ARC isolation remains in runtime/profile/memory/repository state, not duplicate model weights.

## 4. PRIME route

PRIME remains the only normal consumer of the Founder-authorized Ollama Cloud MiniMax M3 subscription capacity.

PRIME route order:

```text
1. ollama-cloud / minimax-m3:cloud
2. verified shared local model
3. Founder-authorized verified-free external route(s)
4. fail closed + Founder diagnostic
```

PRIME cloud session/weekly/monthly/rate-limit conditions are Founder-operational telemetry only.

## 5. ARC route

ARC route order:

```text
1. verified shared local model
2. Founder-authorized verified-free external route(s)
3. sanitized temporary unavailability
```

ARC route rules:

- Ollama Cloud MiniMax M3 is not part of the normal ARC route chain.
- No ARC may autonomously add a paid cloud route.
- A free external fallback must be re-verified as eligible before use.
- If local capacity is busy, queueing is preferred where technically safe.
- If local capacity is unavailable and an approved free fallback is GREEN, fail over internally.
- If no route is available, fail closed without leaking infrastructure details.

## 6. No Owner AI usage-limit messaging

ARC Owners are not shown model-usage quotas or daily/weekly/monthly AI reset messages.

Do not emit messages such as:

- "you reached your daily usage limit";
- "you reached your weekly usage limit";
- "you reached your monthly usage limit";
- "upgrade because your model allowance is exhausted";
- provider/session/credit exhaustion text.

The local-first architecture means model/provider capacity is an infrastructure concern, not an Owner-facing quota UX.

Commercial tiers remain real, but their current differentiation is not expressed as a visible model-call counter.

## 7. Owner experience during load or outage

Routing details should normally be invisible.

### Queue pressure

Only when useful:

**EN:** `Your ARC is handling higher activity right now. Your request is queued and will continue automatically.`

**FR:** `Ton ARC gère actuellement une activité plus élevée. Ta demande est mise en file d’attente et continuera automatiquement.`

**NL:** `Je ARC verwerkt momenteel meer activiteit. Je verzoek staat in de wachtrij en gaat automatisch verder.`

### All authorized routes unavailable

**EN:** `Your ARC is temporarily unavailable. Please try again shortly.`

**FR:** `Ton ARC est temporairement indisponible. Réessaie dans quelques instants.`

**NL:** `Je ARC is tijdelijk niet beschikbaar. Probeer het over enkele ogenblikken opnieuw.`

Never expose provider/model names, HTTP status, billing/credits, reset windows, provider URLs, internal commands, request IDs or runtime details.

## 8. Local hardware gate

Do not cut the ARC fleet over to a local model until PRIME verifies actual VPS resources:

- total and available RAM;
- swap;
- CPU model and vCPU/core count;
- GPU/VRAM if present;
- free disk and storage type;
- baseline PRIME/Cargo/NARC/VONDA resource use;
- local inference runtime/version.

The Founder remembers approximately 40 GB total VPS capacity, but the resource type must be measured rather than assumed.

## 9. Local model selection

Preferred first candidate remains `gpt-oss:20b`, subject to real hardware validation.

If it does not fit safely, select the strongest model that preserves production headroom.

Required acceptance tests:

- general reasoning;
- structured output;
- Hermes tool/function calling;
- EN/FR/NL interaction quality;
- latency;
- stable memory pressure;
- zero marginal API fee;
- coexistence with PRIME + all live ARC runtimes.

The selected model name is implementation metadata, not permanent product truth.

## 10. Local safety defaults

Until telemetry proves more capacity safe:

- one active local inference request at a time;
- queue additional requests;
- Owner interactive work receives highest ordinary queue priority;
- Founder interactive work receives high priority;
- critical recovery may pre-empt background work;
- background ARC/Brain/batch work pauses or queues under pressure;
- start with a conservative context window around 8K–16K unless measured evidence supports more;
- local inference endpoint remains localhost/protected internal only;
- no public inference endpoint.

## 11. Operational state model

Recommended internal states:

```text
prime_cloud_normal
prime_local_fallback
arc_local_normal
arc_external_free_fallback
local_queue_busy
all_authorized_routes_unavailable
```

These are internal operational states. They are not Owner commercial usage states.

No route transition changes ARC identity, memory, form, aura, maturity or ownership.

## 12. Cost boundary

No ARC, PRIME, OMEGA or Factory process may autonomously:

- purchase credits;
- top up an account;
- upgrade a plan;
- enable a new paid provider;
- change billing;
- create additional paid capacity.

Additional paid capacity requires explicit Founder authorization.

The existing Ollama Pro authorization applies to PRIME's MiniMax M3 primary use only under this architecture.

## 13. Telemetry requirements

Internal non-content telemetry remains mandatory because local inference still has real infrastructure cost and capacity implications.

Record where available:

- runtime / ARC ID;
- human turns;
- model invocations;
- model calls per human turn;
- tool-loop calls;
- background/system calls;
- tokens;
- latency;
- queue time;
- local CPU/RAM pressure;
- local concurrency;
- fallback reason;
- fallback from/to;
- external fallback duration;
- actual provider cost;
- equivalent model cost;
- shared VPS/inference allocation;
- service incidents.

Do not centralize raw prompts/responses, Owner-private memory/files, transport IDs, pairing material, credentials or secrets.

Telemetry informs capacity planning and Step 17B pricing. It is not an Owner-visible model quota.

## 14. Factory inheritance

Every Factory-created ARC must inherit:

```yaml
roles:
  founder: founder
  owner: owner
  business_titles_are_metadata: true

inference:
  primary_class: shared_local
  ollama_cloud_minimax_primary_allowed: false
  approved_free_external_fallback_ready: true
  owner_usage_limit_messages_allowed: false
  provider_internal_leakage_allowed: false
  telemetry_required: true

safety:
  local_hardware_gate_required: true
  autonomous_paid_capacity_changes_allowed: false
```

Factory creation does not imply the local model is already healthy; runtime-ready status requires the shared local inference layer to pass its evidence gates.

## 15. PRIME / OMEGA responsibilities

PRIME supervises:

- its own Ollama Cloud MiniMax health;
- shared local model health;
- ARC queue pressure;
- free-fallback eligibility;
- capacity telemetry;
- recovery and Founder escalation.

OMEGA may observe portfolio-level operational capacity state without receiving unrestricted Owner-private content.

## 16. Pricing relationship

Step 17B should refine Standard / Pro / Business economics using real local-inference evidence:

- CPU/RAM/time per Owner;
- queue pressure and concurrency;
- calls/tokens per Owner;
- fallback frequency;
- VPS/inference allocation;
- support/incident burden;
- storage/integration/automation load;
- contribution margin.

Do not reintroduce an Owner-facing daily/weekly/monthly AI usage-limit message merely because telemetry exists. Any future model-usage quota would require a new explicit Founder decision.

## 17. Acceptance criteria

The architecture is GREEN when:

1. PRIME uses Ollama Cloud MiniMax M3 as its normal primary route;
2. Cargo/NARC/VONDA use one verified shared local model as their normal primary route;
3. future ARCs inherit local-primary routing;
4. ARCs do not consume PRIME's Ollama Cloud MiniMax pool;
5. the local model passed real VPS hardware and Hermes tool/function gates;
6. local queue/concurrency safeguards work;
7. approved free external fallback works where authorized;
8. no Owner receives daily/weekly/monthly AI usage-limit messaging;
9. raw provider/runtime internals never leak to Owners;
10. no autonomous spend occurs;
11. telemetry records real local capacity/economic evidence without Owner-private payloads.
