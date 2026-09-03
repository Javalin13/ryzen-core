# Ryzen Core — Current Reality Overlay (2026-09)

```yaml
---
type: current-reality-overlay
status: active-reference
created: 2026-09-03
classification: reality + active-execution + approved-architecture
historical_docs_preserved: true
amendable: true-additively
---
```

## Purpose

This file reconciles the June 2026 foundation/rebuild assumptions with the operational reality that now exists in September 2026. It does not delete or rewrite historical doctrine. It provides the current reading layer for future Founder/agent decisions.

## Current reality

### Proven / operational

- PRIME operates as the Founder's execution/operator node on a VPS.
- PRIME is reachable through Telegram.
- PRIME uses durable repository/state patterns rather than relying only on transient chat context.
- The PRIME ↔ Luxcalibur GitHub bridge has been proven as an operational review/coordination mechanism.
- The current ARC productization effort is derived from patterns proven through PRIME, not from a fully implemented Ryzen kernel.

### Active commercial experiment

- VONKA is the first external ARC Founding Pilot proposal.
- Target: validate a second PRIME-derived ARC node for a real external entrepreneur.
- Commercial baseline: 6-month free pilot, then ARC Standard at €500/year or €50/month if continued.

### Still not proven

- A general ARC Factory is not yet proven or authorized as a production runtime.
- Safe density of multiple ARC nodes on one VPS is not yet measured.
- Multi-tenant isolation, usage attribution, support burden and automated provisioning still require live evidence.
- Higher ARC tiers and enterprise pricing remain working commercial hypotheses until market validated.

## Strategic implication

The old roadmap must not be executed mechanically just because it exists. Future Ryzen implementation decisions should first ask:

> What has PRIME and the real ARC pilots already proven, and which formerly planned components are therefore unnecessary, simplified or still missing?

This creates a **proof-first reconciliation loop**:

`historical architecture → PRIME evidence → external ARC pilot evidence → reusable requirements → only then future Ryzen/ARC Factory implementation`.

## Source-of-truth order for current work

1. `Javalin13/ryzen-continuity` — canonical doctrine/history.
2. This file — current reality overlay for September 2026 onward.
3. `12-arc-productization/` — commercial/product/pilot accumulation.
4. `11-fleet-arc-intake/` — Fleet-specific ARC intelligence.
5. `06-runtime-roadmap/ROADMAP.md` — historical/planned rebuild map, interpreted through this reality overlay.

## Guardrail

Historical documents remain valid evidence of prior intent, but historical statements such as “runtime deferred/not imminent” or old top-level folder counts must not be mistaken for a complete description of current operational reality.
