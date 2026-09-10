# RYZ3N Core — Current Reality Overlay (2026-09)

```yaml
---
type: current-reality-overlay
status: active-reference
created: 2026-09-03
last_verified: 2026-09-10
classification: reality + active-execution + approved-architecture + commercial-validation
historical_docs_preserved: true
amendable: true-additively
---
```

## Purpose

This file reconciles the June 2026 foundation/rebuild assumptions with the operational reality that exists in September 2026. It does not erase historical doctrine. It is the current reading layer for Founder, Luxcalibur, PRIME and future agents.

Historical statements such as “no implementation begins today”, “bridge deferred”, old pricing figures, or the earlier `VONKA` typo describe an earlier state and must not be treated as the current operating truth when a later Founder-directed standard exists.

Current project spelling is **RYZ3N**. Legacy canonical files may still use `Ryzen`.

## Canonical architecture — unchanged

The canonical ecosystem remains:

```text
Creator → RYZ3N → ARCs → Brains → Agents → Execution
```

PRIME is not inserted into this hierarchy. PRIME is the current prototype operator/steward while native RYZ3N orchestration is not yet the production control plane.

Current prototype view:

```text
Founder / Owner
  ↓
PRIME steward / operator
  ↓
ARC runtime instance
  ↓
Domain / Project → Intent → Activity → Brain → Agents / Tools → Execution
```

This is an implementation view, not a replacement ontology.

## Proven / operational as of 2026-09-10

- PRIME operates as the Founder's execution/operator node on the VPS and is reachable through Telegram.
- PRIME uses durable repository/state/checkpoint patterns rather than relying only on transient chat context.
- The Founder ↔ Luxcalibur ↔ PRIME GitHub bridge is active and proven. Detailed engineering reports travel through GitHub; Founder receives only the command/mini-report view.
- VONDA is the first external/reference ARC proving node.
- VONDA has a separate Hermes profile/runtime/gateway boundary with privacy/isolation controls.
- The unsafe “first unknown sender auto-binds as primary user” behavior was rejected and replaced by a fail-closed pending-candidate + explicit operator-approval pattern.
- Task persistence, onboarding preparation, steward/event patterns and V1 release preparation have been exercised in the VONDA reference implementation.
- Privacy-safe per-ARC model-capacity telemetry is live and evidence-backed for VONDA.
- Live VONDA telemetry has captured real gateway model request, success, latency and token/usage observations without storing client message payload in steward telemetry.
- Simulated telemetry evidence is explicitly separated from real production telemetry.
- `VONDA_CAPACITY_TELEMETRY = GREEN` is closed.
- `Javalin13/VONDA-Corporation/arc/GOLDEN-ARC-BLUEPRINT.md` is frozen as the current reusable **v1.1** engineering contract for future ARC replication; v1.1 aligns the inherited maturity gates to canonical RYZ3N V1→V6 doctrine and generalizes VONDA-specific identifiers.
- The Golden Blueprint includes identity/isolation, fail-closed access, onboarding, memory/Brain boundaries, ARC↔stewardship, scoped credentials, recovery, capacity telemetry, the 10-Standard-ARC model-pool safety ceiling, V1→V6 maturity/aura, form/aura separation, ownership-transfer reset semantics and real-vs-simulated evidence distinction.

## Active commercial validation

ARC is now being productized for solo/starting entrepreneurs and very small business owners who value AI but do not want to install or maintain the underlying agent/model/server stack.

Current customer-facing position:

> **ARC — Your AI operating partner. It grows with you.**

Initial launch model:

- VONDA remains the reference/tutorial ARC and exceptional founding pilot.
- The next commercial validation cohort is **Founding 20**: recruit 10–20 real paying entrepreneurs primarily through trusted/direct channels before broad paid acquisition.
- Founding-20 working offer: **€49/month**, rate locked while continuously subscribed, within Standard scope/fair-use rules.
- Normal ARC Standard pricing remains **€50/month or €500/year**.
- Standard includes predictable normal AI usage; customers should not need to manage their own API keys or receive surprise pass-through model bills.
- Standard is **not unlimited AI** and does not include structurally heavy autonomous/bulk workloads, unlimited custom integration work, dedicated model capacity or unlimited human support.
- Paid acquisition should scale only after repeatable onboarding, retained usage, support burden, model capacity and unit economics are evidenced.

Canonical commercial operating plan:

`12-arc-productization/ARC-COMMERCIALIZATION-LAUNCH-AND-OPERATING-PLAN.md`

Cross-repo A→Z map:

`12-arc-productization/ARC-A2Z-ALIGNMENT-MAP-2026-09-10.md`

## Capacity / usage reality

Founder safety rule:

> **Maximum 10 Standard ARCs per Ollama/Hermes model-capacity pool until production telemetry proves another ceiling preserves service quality.**

The ceiling is an operational safety/commercial rule, not a technical claim that the provider can only support ten ARCs.

Capacity must split earlier when telemetry shows recurring throttling, retry pressure, latency degradation, concurrency pressure, provider headroom/quota risk, incidents or disproportionate usage.

The ceiling may be lowered immediately for reliability. It may only be raised from real production evidence.

## Maturity / lifecycle reality

ARC billing tier and ARC maturity are distinct.

Maturity ladder:

`V1 Blue → V2 Cyan → V3 Violet → V4 Gold → V5 Platinum → V6 Sovereign/Prismatic`

Maturity/aura is evidence-derived; it cannot simply be purchased.

Founder lifecycle rule:

> **Form is Owner-resettable. Aura is maturity-derived.**

A cosmetic factory-form reset does not change maturity/aura. Ownership transfer alone does not automatically force V1; however, a transfer that genuinely empties/removes the owner-specific competence/evidence supporting the mature state returns that ARC to **V1 Foundation / Blue** for the new Owner.

## Still not proven — do not overclaim

The following remain open evidence gates:

- full `VONDA_REFERENCE_ARC_COMPLETE = GREEN`, because it still requires Laetitia's real primary-user cycle;
- automated bulk ARC provisioning for ARC #2+;
- operational replication of Fleet ARC and Cargo ARC from the Golden Blueprint;
- safe real multi-ARC VPS density under meaningful concurrent use;
- real capacity behavior with 5–10 simultaneously active Standard ARCs;
- 30/60/90-day retention for a paid external entrepreneur cohort;
- support minutes/intervention burden at cohort scale;
- measured CAC/payback from paid advertising;
- fully loaded contribution margin at scale;
- broad production legal/privacy/compliance packaging;
- native RYZ3N runtime orchestration replacing PRIME's current prototype/operator role.

The Golden Blueprint is a major reusable engineering milestone. It is **not** evidence that mass provisioning, retention or multi-tenant scale are already solved.

## Current execution priority

1. Keep VONDA ready and await the real primary-user cycle without manufacturing new gates.
2. Prepare repeatable commercial onboarding/provisioning from the current Golden Blueprint.
3. Recruit real Founding customers deliberately; do not pre-create 20 empty ARCs.
4. Measure provisioning time, support time, usage, latency, incidents, retention and direct/allocated costs from the first customer onward.
5. Promote only generalized, privacy-safe lessons into shared RYZ3N productization.
6. Automate repeated work before adding avoidable human operations.
7. Scale distribution only when evidence supports it.

## Source-of-truth order for current work

1. Founder decisions + canonical doctrine in `Javalin13/ryzen-continuity`.
2. This current-reality overlay and `12-arc-productization/ARC-A2Z-ALIGNMENT-MAP-2026-09-10.md`.
3. Current Founder-directed standards inside `12-arc-productization/`.
4. `Javalin13/VONDA-Corporation/arc/GOLDEN-ARC-BLUEPRINT.md` **v1.1 or later** for the frozen reusable reference implementation contract.
5. Active VONDA bridge files for the current reference-ARC execution round.
6. PRIME current SOUL/comms/ARCS stewardship files for prototype execution behavior.
7. Historical June roadmap/migration/foundation files as provenance, interpreted through the current overlays.

## Core guardrail

> **Proof before scale. Canon before prototype hierarchy. Product promise must match runtime evidence. Share capability, not private payload. Founder receives the command view; PRIME and Lux exchange the engineering view through the bridge.**
