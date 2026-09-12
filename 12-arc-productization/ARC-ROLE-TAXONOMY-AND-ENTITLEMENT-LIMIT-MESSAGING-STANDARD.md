# RYZ3N ARC Role Taxonomy & Entitlement-Limit Messaging Standard

Status: **CANONICAL — Founder directive 2026-09-12**

## 1. Canonical human roles

RYZ3N uses two canonical human authorization roles across ARCs:

- `founder` — reserved for the RYZ3N Founder. John / Jan is always Founder in every ARC and ecosystem context.
- `owner` — every non-Founder human who is granted ownership/use of an ARC is an Owner.

Business/domain titles are metadata and do not replace the authorization role. Examples:

- Narek: `owner` (domain title/context may describe fitness coach/business owner)
- Laetitia: `owner`
- Maria: `owner` (business title may remain Cargo Connect co-founder)
- John / Jan: `founder`

Legacy authorization labels such as `founder_operator`, `founder_test`, `primary_user`, `cargo_cofounder`, or similar role names may exist temporarily during migration, but they are not canonical role identities going forward.

Where operator powers are required, model them as Founder authority/capability metadata, not as a replacement human role. The Founder remains `founder`.

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
- Cargo: Maria -> `owner`; her Cargo Connect business title may remain co-founder in domain metadata
- Cargo Founder identity: John / Jan -> `founder`

## 4. Commercial entitlement tiers

Canonical Owner-facing usage tiers:

- `Standard` — standard included usage allowance
- `Pro` — higher included usage allowance
- `Business` — unlimited usage entitlement

Exact pricing, reset cadence, rate limits, concurrency rules and fair-use/service-availability terms belong in commercial configuration/contracts and may evolve without redefining the role taxonomy.

## 5. Owner-facing usage-limit message

When, and only when, the Owner's own ARC entitlement has reached the usage limit of the current tier, the ARC must explain that state plainly instead of exposing provider/runtime errors.

Canonical English wording:

> You've reached the usage limit of your Standard plan. You can wait for your allowance to reset, upgrade to Pro for a higher limit, or choose Business for unlimited usage.

Canonical French wording:

> Tu as atteint la limite d’utilisation de ton forfait Standard. Tu peux attendre que ta limite soit réinitialisée, passer à Pro pour une limite plus élevée, ou choisir Business pour une utilisation illimitée.

Canonical Dutch wording:

> Je hebt de gebruikslimiet van je Standard-pakket bereikt. Je kunt wachten tot je limiet opnieuw beschikbaar is, upgraden naar Pro voor een hogere limiet, of Business kiezen voor onbeperkt gebruik.

The tier name must be rendered dynamically. If a Pro Owner reaches the Pro allowance, the message must say `Pro`, not `Standard`, and offer the valid next option(s).

## 6. Provider-capacity exhaustion is NOT Owner entitlement exhaustion

RYZ3N must not tell an Owner that their Standard/Pro allowance is exhausted merely because a shared model/provider pool is rate-limited, out of credits, unavailable, or temporarily exhausted.

The runtime must distinguish:

1. `owner_entitlement_exhausted` — the Owner actually reached their ARC plan allowance. Show the commercial usage-limit message above.
2. `provider_capacity_exhausted` — shared/internal RYZ3N provider capacity is unavailable while the Owner still has entitlement. Attempt Founder-authorized fallback routing internally. Do not upsell based on a false Owner-limit claim.
3. `all_authorized_routes_unavailable` — no approved route can currently serve the request. Tell the Owner the service is temporarily unavailable without provider/model/billing internals and without falsely claiming their plan limit was reached.

## 7. No provider internals to Owners

Owners must never receive raw infrastructure/provider diagnostics such as:

- provider names;
- model names;
- HTTP 429/5xx text;
- account credit/billing messages;
- provider upgrade URLs;
- internal `/model` commands;
- provider request/reference IDs;
- API/runtime/profile details.

These details are Founder/PRIME telemetry only.

## 8. Founder visibility

The Founder may receive full operational diagnostics through PRIME / Founder dashboards, including provider/model, rate-limit class, pool exhaustion, fallback status, capacity forecasts and billing/cost metadata. This Founder diagnostic visibility does not alter the Founder role and does not expose Owner-private message content by default.

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
  business_usage: unlimited
  distinguish_owner_limit_from_provider_capacity: true
  owner_provider_error_leakage_allowed: false
```

## 10. Acceptance criteria

An ARC passes this standard when:

1. John / Jan resolves as Founder, never Owner;
2. intended non-Founder users resolve as Owner, regardless of business title;
3. direct first-contact binds only the armed Owner slot;
4. Owner entitlement exhaustion produces the correct tier-aware Standard/Pro/Business message;
5. provider exhaustion does not falsely consume or blame the Owner's entitlement;
6. raw provider/runtime errors remain visible only to Founder/PRIME telemetry;
7. Business entitlement is represented to the Owner as unlimited usage according to RYZ3N commercial policy.
