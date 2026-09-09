# VONDA ARC — Founding Pilot Foundation Addendum

Date: 2026-09-09
Parent pilot: `VONDA.md`
Status: PREPARATION AUTHORIZED / CLIENT ACTIVATION PENDING

## Official ARC name

Founder decision: the client-facing ARC is named **VONDA ARC**.

## Founder runtime target — autonomous ARC node

VONDA ARC is **not** merely another chat/session inside PRIME's own Hermes runtime.

VONDA is the first external **autonomous Hermes-based ARC node under PRIME supervision**.

Initial topology:

```text
prime-vps-01
├── PRIME Hermes runtime/service
│   └── Founder/operator control + supervision plane
└── VONDA ARC Hermes runtime/service
    ├── own runtime identity
    ├── own gateway/service lifecycle
    ├── own Telegram bot/gateway adapter
    ├── own workspace + memory
    ├── own secrets + permissions
    ├── own logs + checkpoints
    ├── own commercial/access/security policies
    └── own client workflows/state
```

**Same physical VPS is allowed; same runtime identity is not.**

VONDA must be independently startable/stoppable/restartable. PRIME supervises health, isolation, recovery and escalation, but does not become the VONDA client runtime and does not merge Laetitia's private memory into PRIME memory.

Future target: move the same VONDA ARC node to a dedicated VPS without changing its conceptual identity, client-facing behavior, memory contracts, permissions or workflows.

Runtime standard:
`12-arc-productization/AUTONOMOUS-ARC-NODE-RUNTIME.md`

## System boundary

`VONDA website = corporate / B2B presence`

`Systeme.io = funnels + payments + commercial automations`

`VONDA ARC = autonomous internal operational assistant / intelligence node`

## Preparation sequence

`prepare autonomous node → verify runtime + isolation → report → client alignment → Founder final GO → bind Telegram → activate`

The six-month pilot clock does not start during technical preparation.

## Required VONDA ARC baseline

- independent VONDA Hermes runtime/service identity;
- independent gateway/service lifecycle under PRIME supervision;
- VONDA-specific Telegram bot/gateway adapter;
- authorized-user/chat binding with fail-closed unknown-user behavior;
- isolated workspace and memory;
- isolated secrets/env and permissions;
- VONDA Corporation identity seed;
- VONDA-specific logs, health checks, checkpoints and recovery;
- task, priority, reminder, drafting and meeting-prep support;
- first-run onboarding/workflow discovery;
- operational context persistence;
- bounded security/contract escalation path VONDA → PRIME → Founder where material;
- experience capture for generalized RYZ3N product learning;
- strict no-cross-client context boundary;
- no exposure of shared RYZ3N/PRIME credentials or other-project data;
- structural portability from shared host to dedicated VPS.

## Client-facing bootstrap

After Telegram activation, VONDA ARC asks Laetitia for the **3–5 recurring things she most wants VONDA to assist with**, plus language/tone, reminders, memory/retention preferences, permissions, success criteria and what not to store.

Internal PRIME/RYZ3N hierarchy is not a client onboarding topic.

## Commercial / access / security bootstrap

VONDA runtime policy/config must contain the approved proposal/pilot boundaries separately from personal memory, including:

- six-month free Founding Pilot period; thereafter current Standard terms €500/year or €50/month if continued;
- current website pilot inclusion and indicative standalone value;
- Founder onboarding/explanation and FR↔NL support as separately priced Founder-delivered services when requested;
- no unlimited custom work;
- custom integrations/dedicated infrastructure require separate scope/price/Founder decision;
- no disclosure of master/shared credentials, provider secrets or other-project access;
- client data/ownership/portability rights do not imply root/shared-platform access;
- RYZ3N retains reusable platform/IP/orchestration/templates/methods/know-how;
- transfer/access-key/credential requests outside approved scope are referred to the applicable proposal boundary and escalated to the Founder;
- security, isolation or material contractual breaches fail closed and signal PRIME through a bounded escalation path.

VONDA may prepare a request for the Founder; it may not silently waive scope, change prices, expose secrets or promise transfer.

## Product-learning rule

`real VONDA use → observation → generalized EXP record → cross-pilot learning → ARC product improvement`

Client-confidential content does not become generalized RYZ3N product content. Promote reusable patterns, not confidential payloads.

## Readiness definition

`READY` requires proof that:

- VONDA has its own Hermes runtime/service, not merely a namespaced block in PRIME's gateway;
- VONDA can stop/restart without restarting PRIME;
- VONDA Telegram route binds only the authorized Laetitia identity;
- memory/secrets/logs/checkpoints remain VONDA-scoped;
- PRIME/FleetConnect/other-client context is not retrievable;
- onboarding and commercial/access/security policies are loaded;
- bounded escalation reaches PRIME;
- rollback/recovery is tested;
- future dedicated-VPS migration is structurally possible.

Until those are proven, a prior `READY` based on a shared PRIME gateway is superseded by this Founder runtime correction.
