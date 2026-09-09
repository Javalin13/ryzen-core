# PRIME → RYZ3N → ARC Prototype Doctrine

```yaml
---
type: arc-runtime-transition-doctrine
status: founder-directed-additive-doctrine
created: 2026-09-09
classification: approved-strategic-architecture + prototype-runtime-guidance
runtime_implementation_authorized: bounded-prototype-only
amendable: true-additively
canonical_refs:
  - Javalin13/ryzen-continuity/blob/main/02-ryzen/RYZEN-CANONICAL.md
  - Javalin13/ryzen-continuity/blob/main/02-ryzen/architecture/HIERARCHY.md
  - Javalin13/ryzen-continuity/blob/main/02-ryzen/architecture/CONVERGENCE-LAYER.md
  - Javalin13/ryzen-continuity/blob/main/03-hermes/RELATIONSHIP-TO-RYZEN.md
  - Javalin13/ryzen-core/blob/main/12-arc-productization/README.md
  - Javalin13/ryzen-core/blob/main/12-arc-productization/PROVISIONING-BACKLOG.md
---
```

## 1. Purpose

This doctrine aligns the current **PRIME + client ARC runtime prototype** with the canonical RYZ3N architecture and makes the migration path explicit.

The current PRIME-mediated ARC system is not a competing architecture. It is a **bounded operational prototype of the future RYZ3N ↔ ARC operating model**.

The objective is to make every pattern proven through PRIME transferable into RYZ3N without rebuilding each ARC from scratch.

Core rule:

> **Build once, instantiate many. Customize by configuration, not by architectural fork.**

And the transition rule:

> **PRIME bootstraps the operating pattern. RYZ3N inherits the operating pattern. PRIME then supervises, audits and teaches the system it helped prove.**

---

## 2. Canonical architecture remains unchanged

The canonical hierarchy remains:

```text
Creator
  ↓
RYZ3N
  ↓
ARCs
  ↓
Brains
  ↓
Agents
  ↓
Execution
```

The legacy canonical documents use the spelling `Ryzen`; the current project representation is **RYZ3N**. This doctrine does not rewrite the meaning of those canonicals.

PRIME is **not** inserted into this canonical tree.

PRIME is not an ARC, Brain or Agent. PRIME is the current operational/execution supervisor and prototype orchestrator serving the RYZ3N architecture while the native RYZ3N runtime is still being built.

Therefore two views must remain distinct:

### Canonical / ecosystem view

```text
Creator → RYZ3N → ARCs → Brains → Agents → Execution
```

### Current prototype runtime view

```text
Founder intent
   ↓
PRIME runtime/orchestration
   ↓
ARC runtime instance
   ↓
client-specific identity + memory + permissions + workflows + tools
   ↓
channels / external execution
```

The runtime view is an implementation bridge, not a replacement hierarchy.

---

## 3. Why the current PRIME + Telegram ARC model matters

The current multi-chat / multi-ARC prototype is the first practical test of several future RYZ3N concepts already present in the canonical architecture:

- **orchestration substrate**;
- **ARC registry / ARC identity**;
- **memory continuity**;
- **governance ↔ execution**;
- **verification ↔ orchestration**;
- **structured logging / audit trail**;
- **ARC isolation and later ARC ↔ ARC convergence**;
- **continuity across sessions and resets**;
- **repeatable ARC generation/provisioning**.

Telegram is only the first interface. It must never become the ARC architecture itself.

The ARC must remain channel-independent so the same ARC can later be reached through Telegram, web, mobile app, API, voice or future RYZ3N-native interfaces without changing its core identity or state model.

---

## 4. PRIME's current role

Until RYZ3N owns the orchestration runtime natively, PRIME acts as the **reference operator and supervisor** for external ARC prototypes.

PRIME may:

- provision a bounded ARC runtime branch from proven PRIME patterns;
- route the correct identity/context based on the authorized channel/user;
- enforce workspace, memory, secret and permission isolation;
- maintain operational state, checkpoints, mission state and recovery information;
- run or coordinate tasks, tools, reminders and integrations inside approved scope;
- capture evidence, failures, friction, lessons and reusable operating patterns;
- supervise runtime quality and surface drift;
- propose reusable patterns for promotion into RYZ3N canon/productization.

PRIME may **not**:

- redefine the RYZ3N hierarchy;
- become the canonical parent of ARCs;
- hardcode client-specific behavior into the shared core;
- let one ARC read another ARC's private context or secrets;
- allow a channel identity to become the source of truth for an ARC;
- keep critical reusable operating knowledge only in volatile runtime memory;
- silently promote prototype behavior into canonical RYZ3N behavior.

---

## 5. RYZ3N's future role

The target state is that RYZ3N assumes the functions that PRIME currently prototypes operationally:

```text
RYZ3N
  ├── ARC registry
  ├── ARC provisioning / factory
  ├── governance
  ├── orchestration
  ├── memory federation / continuity
  ├── verification
  ├── observability / audit
  ├── cross-ARC convergence
  └── channel-independent routing
        ↓
      ARC instances
```

When that runtime is mature, PRIME transitions from primary orchestrator to **supervisor / mentor / execution steward**.

PRIME's accumulated knowledge must then feed RYZ3N as structured, reusable doctrine rather than remain trapped in PRIME-specific behavior.

The long-term relationship becomes:

```text
Founder
   ↓ strategic intent
RYZ3N
   ↓ governs + coordinates + provisions
ARC network
   ↓
Brains → Agents → Execution

PRIME = supervisor / auditor / mentor / high-trust execution arm
        ↘ teaches proven patterns back into RYZ3N
```

---

## 6. Replication contract for every ARC prototype

Every client ARC must be built so it can later be migrated or re-instantiated under RYZ3N.

A reusable ARC instance must have, at minimum:

1. **Identity contract** — `arc_id`, display identity, owner/user, purpose, scope, language/tone.
2. **Routing contract** — authorized users/channels mapped to the ARC without hardcoding the channel into the ARC logic.
3. **Memory contract** — separate operational, client/context, decisions and continuity state; explicit retention/consent boundaries.
4. **Permission contract** — tools, data sources, actions, write rights, external execution and escalation rules.
5. **Workspace contract** — isolated filesystem/state namespace with predictable structure.
6. **Secrets contract** — per-ARC secrets boundary; no shared master credential exposure.
7. **Workflow contract** — reusable capabilities plus client configuration; no architectural fork for ordinary customization.
8. **Observability contract** — structured ARC/tenant-tagged logs, health and incidents without leaking private payloads across tenants.
9. **Continuation contract** — checkpoint/recovery/session state so resets do not destroy operational coherence.
10. **Experience contract** — prototype evidence and generalized lessons flow back to RYZ3N productization.
11. **Export/migration contract** — configuration and reasonably exportable client state must be structurally separable from shared runtime/IP.
12. **Version contract** — ARC template/runtime version and migration history are traceable.

The template is shared. The instance is isolated.

---

## 7. Canonical operational trail

The canonical convergence doctrine says the ecosystem learns through snapshots, decisions, lessons, architecture and roadmap updates. PRIME's client ARC prototypes must mirror that discipline at the appropriate level.

Each ARC should maintain an operational trail that can later map cleanly into RYZ3N:

- **CURRENT / mission state** — what is active now, what is dormant, what is blocked.
- **Checkpoints** — known-good state and recovery reference.
- **Decision log** — material local decisions, rationale and supersession.
- **Lessons / experience** — what reality taught the pilot.
- **Drift records** — when implementation or behavior departs from approved scope/canon.
- **Evidence / verification** — tests, health checks and proof that a claimed state is real.
- **Continuation state** — enough structured state to resume after session reset or operator handoff.
- **Roadmap / next gates** — what can happen next and what requires Founder/customer approval.

Client-private facts stay within the client boundary. Only generalized reusable lessons are promoted into cross-ARC RYZ3N intelligence.

This mirrors the canonical convergence rule:

```text
ARC reality
  ↓
local evidence / decisions / lessons
  ↓
generalized reusable pattern
  ↓
RYZ3N convergence / productization
  ↓
shared ARC standard candidate
```

No silent rewriting. Promotion is additive and traceable.

---

## 8. VONDA ARC as the first external proving node

VONDA ARC must be treated simultaneously as:

1. a real, bounded personal/operational ARC for Laetitia;
2. an isolated external pilot;
3. a proving node for the PRIME-derived reusable ARC template;
4. a source of evidence for future RYZ3N-native ARC provisioning.

Its runtime model is:

```text
PRIME core/orchestration
  ↓
VONDA ARC runtime branch
  ↓
Laetitia-specific identity/context/memory/permissions/workflows
  ↓
Telegram initially
```

But its future migration target is:

```text
RYZ3N runtime
  ↓
VONDA ARC instance
  ↓
same identity/context/memory/permissions/workflows contract
  ↓
Telegram / web / app / API / other channel
```

Therefore VONDA-specific logic must remain configuration/overlay wherever possible.

---

## 9. What must be generalized from PRIME

PRIME's reusable knowledge should be extracted progressively into RYZ3N-readable patterns, including:

- provisioning sequence;
- routing rules;
- identity/persona dispatch;
- memory namespace model;
- permission model;
- task lifecycle;
- recovery and checkpoint procedure;
- session continuation patterns;
- canonical logging and evidence patterns;
- incident handling;
- cross-client isolation tests;
- observability conventions;
- lessons/promotion contract;
- rollback/update behavior;
- channel adapters;
- reusable tool/integration contracts.

Rule:

> **No critical reusable operating knowledge may exist only inside PRIME runtime memory. If it matters for another ARC, it must become structured, transferable RYZ3N-readable knowledge.**

---

## 10. What must remain client-specific

The following do not automatically converge into shared RYZ3N intelligence:

- private client conversations;
- personal/client memory;
- customer documents/data;
- credentials/secrets;
- private contact lists;
- confidential commercial information;
- client-specific custom workflows unless generalized after evidence review;
- private logs containing customer payloads.

RYZ3N should receive the **pattern**, not unnecessary private content.

---

## 11. Replication success test

A PRIME-derived ARC prototype is architecturally healthy when the following statement becomes increasingly true:

> Given the shared ARC template and a bounded configuration package, another authorized ARC can be instantiated without copying client state, rewriting PRIME core, or inventing a new runtime architecture.

The mature Standard target remains approximately:

> **80–90% repeatable platform / 10–20% customer configuration.**

ARC #10 should require materially less Founder/operator effort than ARC #1 while preserving isolation, continuity, auditability and user value.

---

## 12. Migration principle

Do not wait for RYZ3N to be complete before learning how ARCs should work.

Use PRIME to prove the contracts now, but preserve a clean future handoff:

```text
PRIME-proven pattern
  ↓ evidence
RYZ3N-readable standard
  ↓ implementation
RYZ3N-native runtime capability
  ↓ migration
existing ARC instance continues without conceptual redesign
```

The ideal migration changes the orchestrator beneath the ARC, not the meaning of the ARC itself.

---

## 13. Final doctrine

**PRIME is the prototype operator, not the final ecosystem architecture.**

**RYZ3N is the canonical ecosystem architecture and future native coordinator of ARCs.**

**ARCs must be isolated, channel-independent, configuration-driven and replicable.**

**Every PRIME pilot must teach RYZ3N.**

**Every reusable lesson must become transferable.**

**Every future migration should preserve identity, memory contracts, permissions, workflows, state and auditability without architectural reinvention.**

This is how today's PRIME + ARC prototype becomes tomorrow's RYZ3N + ARC network rather than a dead-end implementation.
