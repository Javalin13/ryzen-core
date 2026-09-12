# RYZ3N ARC Role Taxonomy & Owner Experience Standard

Status: **CANONICAL — Founder directive 2026-09-12**

> **Supersession note — 2026-09-12:** Owner-facing AI usage-limit messaging is retired. PRIME is the only runtime authorized to use Ollama Cloud MiniMax M3 as its normal primary route. ARCs are local-model-first. Daily/weekly/monthly model-usage-limit messages must not be shown to ARC Owners.

## 1. Canonical human roles

RYZ3N uses two canonical human authorization roles across ARCs:

- `founder` — reserved for the RYZ3N Founder. John / Jan is always Founder in every ARC and ecosystem context.
- `owner` — every non-Founder human who is granted ownership/use of an ARC is an Owner.

Business/domain titles are metadata and do not replace the authorization role.

Examples:

- Narek: `owner`
- Laetitia: `owner`
- Maria: `owner` with Cargo Connect co-founder retained only as business-title metadata
- John / Jan: `founder`

Legacy labels such as `founder_operator`, `founder_test`, `primary_user`, `cargo_cofounder`, or similar role names may exist temporarily during migration only. They are not canonical human role identities going forward.

Founder powers are capability/authority metadata attached to `founder`; they are not a third human role.

## 2. Hard separation

- Founder never consumes an Owner entitlement or Owner activation slot.
- An Owner never receives Founder authority by first contact, title, prompt text, or business title.
- Founder and Owner memory/private namespaces remain separated according to ARC privacy rules.
- Business titles such as co-founder, director, coach, employee, or customer may affect domain behavior but do not redefine the canonical authorization role.

## 3. Direct first-contact role rule

Factory and ARC activation state must arm canonical role `owner` for intended non-Founder users.

The first eligible intended non-Founder inbound may atomically bind `owner` when the specific Owner slot is armed and unbound. The Founder identity must be excluded before any Owner claim attempt.

For current ARCs:

- NARC: Narek -> `owner`
- VONDA: Laetitia -> `owner`
- Cargo: Maria -> `owner`; co-founder remains Cargo business-title metadata only
- Cargo Founder identity: John / Jan -> `founder`

## 4. Owner AI service model — no usage-limit UX

ARC Owners are **not** shown AI model usage-limit counters, daily/weekly/monthly model-limit warnings, provider-credit exhaustion messages, or upgrade prompts caused by model usage.

Current Founder direction:

- PRIME may use Ollama Cloud MiniMax M3 as its primary intelligence route.
- Cargo, NARC, VONDA and future ARCs are local-model-first after the local model passes the required hardware and Hermes capability gates.
- ARC Owner interaction is served from shared local inference infrastructure rather than consuming PRIME's Ollama Cloud MiniMax M3 pool.
- Internal calls/tokens/cost-equivalent usage may still be measured for telemetry and pricing analysis.
- Internal telemetry is not an Owner-facing quota.

Therefore the previous Standard/Pro daily/weekly/monthly AI usage-limit messages are superseded and must not be emitted.

## 5. Commercial tiers remain real but are not model-call counters

Standard / Pro / Business / Dedicated / Enterprise remain commercial product tiers.

They may differ by factors such as:

- managed storage;
- authorized users;
- channels;
- integrations;
- automations;
- support/service level;
- queue/concurrency priority;
- shared vs dedicated compute placement;
- advanced capabilities and future contracted scope.

They do **not** currently require an Owner-facing AI message quota or daily/weekly/monthly model-usage reset message.

Exact prices and tier differentiation remain Founder-approved commercial policy and are refined from Step 17/17B telemetry rather than from provider-session ceilings.

## 6. Capacity pressure is infrastructure state, not Owner usage exhaustion

The runtime may still classify operational conditions internally, for example:

```text
local_capacity_busy
local_queue_saturated
local_model_unavailable
external_free_fallback_active
all_authorized_routes_unavailable
prime_cloud_session_limit_exhausted
prime_cloud_weekly_limit_exhausted
prime_cloud_rate_limited
```

Rules:

- ARC local capacity pressure must not be described as "you reached your usage limit".
- Queueing is preferred over falsely presenting a commercial exhaustion state.
- If an approved ARC fallback is available, use it internally.
- If all ARC routes are unavailable, use only a sanitized temporary service-availability message.
- PRIME cloud-capacity diagnostics are Founder/PRIME-only and do not become Owner messages.

## 7. Owner-facing service messages

Normal Owner experience should remain silent about inference routing.

If local capacity is temporarily busy but the request can queue, use a neutral product message only when necessary, for example:

**English**

> Your ARC is handling higher activity right now. Your request is queued and will continue automatically.

**French**

> Ton ARC gère actuellement une activité plus élevée. Ta demande est mise en file d’attente et continuera automatiquement.

**Dutch**

> Je ARC verwerkt momenteel meer activiteit. Je verzoek staat in de wachtrij en gaat automatisch verder.

If no authorized route is available:

**English**

> Your ARC is temporarily unavailable. Please try again shortly.

**French**

> Ton ARC est temporairement indisponible. Réessaie dans quelques instants.

**Dutch**

> Je ARC is tijdelijk niet beschikbaar. Probeer het over enkele ogenblikken opnieuw.

No usage-limit, provider, model, billing, credits, reset-window, or infrastructure-internal wording is shown to the Owner.

## 8. No provider internals to Owners

Owners must never receive raw infrastructure/provider diagnostics such as:

- provider names;
- model names/IDs;
- HTTP 429/5xx text;
- account credit/billing messages;
- provider upgrade URLs;
- internal `/model` commands;
- provider request/reference IDs;
- API/runtime/profile details;
- credential/authentication details;
- PRIME's Ollama Cloud session/weekly/monthly state.

These are Founder/PRIME telemetry only.

## 9. Founder visibility

The Founder may receive full operational diagnostics through PRIME / Founder dashboards, including:

- PRIME cloud-provider/model state;
- local model health;
- local queue/concurrency pressure;
- fallback status;
- capacity forecasts;
- actual/equivalent costs;
- per-ARC call/token/load telemetry.

This Founder visibility does not alter the Founder role and does not expose Owner-private message content by default.

## 10. Factory inheritance

Every new Factory-created ARC must inherit:

```yaml
roles:
  founder_role: founder
  non_founder_arc_user_role: owner
  business_titles_are_metadata: true
  legacy_role_aliases_allowed_for_migration_only: true

owner_ai_experience:
  primary_inference_class: shared_local
  owner_ai_usage_limit_messages_allowed: false
  provider_internal_leakage_allowed: false
  daily_weekly_monthly_ai_reset_messages_allowed: false
  queue_message_allowed_when_material: true
  sanitized_unavailable_message_allowed: true

telemetry:
  internal_usage_measurement_allowed: true
  owner_visible_model_quota: false
```

## 11. Acceptance criteria

An ARC passes this standard when:

1. John / Jan resolves as Founder, never Owner;
2. intended non-Founder users resolve as Owner, regardless of business title;
3. direct first-contact binds only the armed Owner slot;
4. the ARC uses the verified shared local inference service as its normal primary route;
5. the ARC does not consume PRIME's Ollama Cloud MiniMax M3 pool;
6. no daily/weekly/monthly AI usage-limit message is shown to an Owner;
7. infrastructure pressure is handled through queueing/fallback or sanitized temporary unavailability;
8. provider/runtime errors remain visible only to Founder/PRIME telemetry;
9. internal telemetry remains available for pricing/capacity optimization without becoming an Owner-facing quota.
