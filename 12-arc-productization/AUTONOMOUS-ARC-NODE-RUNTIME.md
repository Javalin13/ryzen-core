# Autonomous ARC Node Runtime — Founder Runtime Standard

```yaml
---
type: arc-runtime-standard
status: founder-directed-additive-doctrine
created: 2026-09-09
classification: approved-strategic-architecture + bounded-runtime-guidance
runtime_implementation_authorized: founding-pilot preparation
amendable: true-additively
canonical_parent: PRIME-RYZ3N-ARC-PROTOTYPE-DOCTRINE.md
---
```

## Purpose

This document fixes the intended runtime shape of a client ARC.

A client ARC is **not** merely another chat/session inside PRIME's own client runtime. It is an **autonomous child runtime node** connected under PRIME supervision.

The current Founder target is:

```text
Founder
  ↓
PRIME control/supervision plane
  ↓
Autonomous ARC node
  ├── own Hermes runtime identity
  ├── own Hermes gateway/service lifecycle
  ├── own Telegram bot/gateway adapter
  ├── own workspace + memory
  ├── own secrets + permissions
  ├── own logs + checkpoints
  └── own client workflows/state
```

For the VONDA Founding Pilot, PRIME and VONDA may run on the **same physical VPS host initially**, but they must not be treated as the same runtime identity or the same client session.

The ARC must be portable later to a dedicated VPS without changing its conceptual identity, memory contracts, permissions, workflows or client-facing behavior.

## Canonical boundary

This standard does not alter the immutable ecosystem hierarchy:

```text
Creator → RYZ3N → ARCs → Brains → Agents → Execution
```

PRIME remains outside that canonical tree as the current high-trust execution/operator/supervision arm.

Current runtime relationship:

```text
Founder intent
  ↓
PRIME supervisor / control plane
  ↓
ARC runtime nodes
  ↓
client execution channels
```

Future runtime relationship:

```text
RYZ3N native orchestration/governance
  ↓
ARC runtime nodes

PRIME = supervisor / auditor / mentor / high-trust execution arm
```

## Minimum autonomous-node boundary

Each ARC must have a logically independent deployment unit with, at minimum:

1. **Hermes runtime identity** — the ARC does not impersonate PRIME and does not share PRIME's conversational identity.
2. **Gateway/service lifecycle** — independently startable, stoppable, restartable and health-checkable without requiring PRIME's client session to restart.
3. **Channel adapter identity** — its own Telegram bot token/gateway binding for Telegram pilots.
4. **Workspace boundary** — predictable ARC-specific filesystem/state namespace.
5. **Memory boundary** — ARC-specific user/business/operational memory; no cross-client recall.
6. **Secrets boundary** — ARC-specific environment/secrets; no exposure of PRIME/shared master secrets.
7. **Permissions boundary** — client/tool/action permissions explicit and least-privilege.
8. **Logs/observability boundary** — ARC-tagged health/events without merging private payloads into PRIME memory.
9. **Checkpoint/recovery boundary** — known-good state, restart path and rollback reference specific to the ARC.
10. **Configuration/version boundary** — template version + client overlay/version traceable.
11. **Commercial/policy boundary** — client scope, prices, access/data/IP/portability rules loaded separately from personal memory.
12. **Escalation boundary** — security, contract, isolation or operational incidents can signal PRIME without granting PRIME unrestricted client-memory mixing.

## Same-host rule

Sharing one VPS host is allowed for early Standard/Founding Pilot operation **only if runtime isolation is proven**.

Same host does not mean same runtime.

Acceptable early pattern:

```text
VPS host
├── PRIME Hermes runtime/service
│   ├── PRIME identity
│   ├── PRIME secrets
│   └── PRIME logs/state
└── VONDA Hermes runtime/service
    ├── VONDA identity
    ├── VONDA secrets
    ├── VONDA Telegram adapter
    ├── VONDA memory/workspace
    └── VONDA logs/checkpoints
```

PRIME must be able to supervise VONDA health/security and execute recovery within authorized scope, while VONDA remains independently restartable and client-isolated.

## Dedicated-VPS portability

Every ARC should be deployable later as:

```text
Dedicated VPS
└── ARC Hermes runtime/service
    ├── own gateway
    ├── own channel adapters
    ├── own state/memory
    ├── own secrets
    └── own observability/recovery
```

Moving from shared host to dedicated host should change infrastructure placement, not ARC meaning.

Required portability package:

- ARC identity/config package;
- client overlay/config;
- secrets inventory/reference (never committed in plaintext);
- memory/state export contract;
- service/gateway config;
- Telegram/channel adapter config;
- template/runtime version;
- checkpoints and migration history;
- health/acceptance tests;
- rollback procedure.

## PRIME supervision contract

PRIME is the control/supervision plane, not the user-facing VONDA runtime.

PRIME may:

- provision/start/stop/restart an ARC node;
- verify health and isolation;
- inspect non-sensitive operational metadata and ARC-tagged evidence;
- receive security/contractual/operational escalation signals;
- coordinate recovery and rollback;
- promote generalized reusable lessons into RYZ3N productization;
- request Founder decision for material scope/credential/access changes.

PRIME must not:

- silently merge client memory into PRIME memory;
- reuse ARC secrets across clients;
- expose one ARC's context to another ARC;
- silently change commercial/contractual policy;
- treat the ARC as merely another PRIME chat;
- make the Telegram bot identity the ARC source of truth.

## Telegram rule

Telegram is a channel adapter attached to the autonomous ARC node.

For a Telegram Founding Pilot, each ARC should have:

- its own Telegram bot token;
- explicit authorized-user/chat binding;
- independently testable routing;
- no fallback to another ARC/PRIME identity on routing failure;
- fail-closed behavior on unknown/unauthorized chat identity;
- safe token handling and rotation procedure.

The ARC's identity, memory and state remain channel-independent.

## VONDA Founding Pilot target

VONDA ARC is the first external node intended to prove this standard.

Target deployment:

```text
prime-vps-01 (initial shared physical host)
├── PRIME Hermes runtime/service — Founder/operator control plane
└── VONDA ARC Hermes runtime/service — autonomous client node
    └── VONDA Telegram bot/gateway — Laetitia-facing channel
```

VONDA must have its own runtime/service identity, workspace, memory, secrets, policy/config, logs, checkpoints and restart lifecycle.

It must be possible to stop/restart VONDA without restarting PRIME.

It must be possible to migrate VONDA later to a dedicated VPS without redesigning the client-facing ARC.

## Readiness test

An ARC is not `READY` merely because files exist.

Before Telegram activation, prove:

- ARC Hermes runtime/service can start independently;
- ARC Hermes runtime/service can stop/restart independently;
- unique ARC identity is returned;
- unique Telegram route binds only the authorized user/chat;
- memory persists inside ARC scope;
- PRIME/other ARC context cannot be retrieved;
- secrets do not cross boundaries;
- logs/checkpoints are ARC-specific;
- security/contract escalation reaches PRIME through a bounded signal path;
- rollback to known-good checkpoint works;
- host-level failure/restart behavior is documented;
- migration package is structurally separable from PRIME.

## Founder doctrine

> **An ARC is an autonomous runtime node under supervision, not a chat branch pretending to be autonomous.**

> **Same VPS is allowed; same runtime identity is not.**

> **PRIME supervises the node. It does not become the node.**

> **Later RYZ3N inherits orchestration without forcing the ARC to be rebuilt.**
