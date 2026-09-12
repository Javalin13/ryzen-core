# RYZ3N ARC Role Taxonomy & Entitlement-Limit Messaging Standard

Status: **CANONICAL — Founder directive 2026-09-12**

## 1. Canonical human roles

RYZ3N uses two canonical human authorization roles across ARCs:

- `founder` — reserved for the RYZ3N Founder. John / Jan is always Founder in every ARC and ecosystem context.
- `owner` — every non-Founder human who is granted ownership/use of an ARC is an Owner.

Business/domain titles are metadata and do not replace the authorization role. Examples:

- Narek: `owner`
- Laetitia: `owner`
- Maria: `owner` with Cargo Connect co-founder retained only as business-title metadata
- John / Jan: `founder`

Legacy labels such as `founder_operator`, `founder_test`, `primary_user`, `cargo_cofounder`, or similar role names may exist temporarily during migration only. They are not canonical role identities going forward.

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

## 4. Commercial entitlement tiers

Canonical Owner-facing tiers:

- `Standard` — included high-performance usage allowance
- `Pro` — higher high-performance usage allowance
- `Business` — unlimited Owner usage entitlement

Exact pricing, reset cadence, rate limits, temporary-reduced-capacity behavior, concurrency rules and service-availability terms belong in commercial configuration/contracts and may evolve without redefining the role taxonomy.

## 5. Cadence-aware Owner usage-limit UX

When, and only when, the Owner's own commercial/high-performance entitlement reaches a configured limit, the ARC must identify the correct cadence if known:

- daily;
- weekly;
- monthly.

It must then explain that the ARC has been temporarily downgraded to reduced-capacity mode until the relevant limit resets.

### Standard

**English**

> You've reached the [daily/weekly/monthly] usage limit of your Standard plan. Your ARC has been temporarily downgraded until the limit resets. You can continue using your ARC in reduced-capacity mode, wait for the reset, upgrade to Pro for higher limits, or choose Business for unlimited usage.

**French**

> Tu as atteint la limite d’utilisation [quotidienne/hebdomadaire/mensuelle] de ton forfait Standard. Ton ARC fonctionne temporairement en capacité réduite jusqu’à la réinitialisation de la limite. Tu peux continuer à l’utiliser, attendre la réinitialisation, passer à Pro pour des limites plus élevées, ou choisir Business pour une utilisation illimitée.

**Dutch**

> Je hebt de [dagelijkse/wekelijkse/maandelijkse] gebruikslimiet van je Standard-pakket bereikt. Je ARC werkt tijdelijk in verminderde capaciteit tot de limiet opnieuw wordt ingesteld. Je kunt je ARC blijven gebruiken, wachten op de reset, upgraden naar Pro voor hogere limieten, of Business kiezen voor onbeperkt gebruik.

### Pro

**English**

> You've reached the [daily/weekly/monthly] usage limit of your Pro plan. Your ARC has been temporarily downgraded until the limit resets. You can continue using your ARC in reduced-capacity mode, wait for the reset, or upgrade to Business for unlimited usage.

**French**

> Tu as atteint la limite d’utilisation [quotidienne/hebdomadaire/mensuelle] de ton forfait Pro. Ton ARC fonctionne temporairement en capacité réduite jusqu’à la réinitialisation de la limite. Tu peux continuer à l’utiliser, attendre la réinitialisation, ou passer à Business pour une utilisation illimitée.

**Dutch**

> Je hebt de [dagelijkse/wekelijkse/maandelijkse] gebruikslimiet van je Pro-pakket bereikt. Je ARC werkt tijdelijk in verminderde capaciteit tot de limiet opnieuw wordt ingesteld. Je kunt je ARC blijven gebruiken, wachten op de reset, of upgraden naar Business voor onbeperkt gebruik.

### Business

Business is unlimited at the Owner-entitlement layer and must never receive a false plan-exhaustion message.

If RYZ3N high-performance infrastructure is temporarily constrained, Business may receive a service-state message such as:

> Your ARC is temporarily running in reduced-capacity mode while high-performance capacity resets. You can continue using it, and full performance will return automatically.

Equivalent FR/NL localization is required. If the exact infrastructure cadence is known and product-appropriate, the ARC may say the current high-performance daily/weekly/monthly capacity has reset timing, but it must not imply that the Business commercial entitlement itself is capped.

## 6. Entitlement exhaustion vs provider/internal capacity exhaustion

The runtime must classify at minimum:

1. `owner_entitlement_exhausted`
2. `provider_session_limit_exhausted`
3. `provider_daily_limit_exhausted`
4. `provider_weekly_limit_exhausted`
5. `provider_monthly_limit_exhausted`
6. `provider_concurrency_saturated`
7. `provider_rate_limited`
8. `provider_unavailable`
9. `fallback_active`
10. `all_authorized_routes_unavailable`

Rules:

- Owner entitlement exhausted -> show the correct tier/cadence message and use permitted temporary reduced-capacity mode.
- Provider/internal capacity exhausted while the Owner still has entitlement -> do not blame the Owner and do not falsely upsell; use Founder-authorized fallback internally.
- All authorized routes unavailable -> sanitized temporary-unavailability message only.

Canonical fallback/downgrade behavior is defined in `ARC-CAPACITY-FALLBACK-TEMPORARY-DOWNGRADE-AND-LOCAL-INFERENCE-STANDARD.md`.

## 7. No provider internals to Owners

Owners must never receive raw infrastructure/provider diagnostics such as:

- provider names;
- model names/IDs;
- HTTP 429/5xx text;
- account credit/billing messages;
- provider upgrade URLs;
- internal `/model` commands;
- provider request/reference IDs;
- API/runtime/profile details;
- credential/authentication details.

These are Founder/PRIME telemetry only.

## 8. Founder visibility

The Founder may receive full operational diagnostics through PRIME / Founder dashboards, including provider/model, limit cadence/class, pool exhaustion, fallback status, local inference state, capacity forecasts and billing/cost metadata. This Founder visibility does not alter the Founder role and does not expose Owner-private message content by default.

## 9. Factory inheritance

Every new Factory-created ARC must inherit:

```yaml
roles:
  founder_role: founder
  non_founder_arc_user_role: owner
  business_titles_are_metadata: true
  legacy_role_aliases_allowed_for_migration_only: true

entitlements:
  tiers: [Standard, Pro, Business]
  standard_and_pro_cadence_aware_limits: true
  business_usage: unlimited
  temporary_reduced_capacity_supported: true
  distinguish_owner_limit_from_provider_capacity: true
  owner_provider_error_leakage_allowed: false
```

## 10. Acceptance criteria

An ARC passes this standard when:

1. John / Jan resolves as Founder, never Owner;
2. intended non-Founder users resolve as Owner, regardless of business title;
3. direct first-contact binds only the armed Owner slot;
4. Standard/Pro limit UX identifies the correct configured daily/weekly/monthly cadence;
5. temporary downgrade preserves ARC identity, memory, tools and Owner binding;
6. Business is represented as unlimited at the Owner-entitlement layer;
7. provider exhaustion does not falsely consume or blame the Owner's entitlement;
8. raw provider/runtime errors remain visible only to Founder/PRIME telemetry;
9. full-performance service returns automatically when high-performance capacity recovers.
