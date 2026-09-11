# apps/arc-factory/ — PLANNED / NOT YET OPERATIONAL

```yaml
---
type: scaffolding
status: PLANNED-NOT-YET-OPERATIONAL
created: 2026-06-15
updated: 2026-09-11
implements_concept: ARC Factory (native RYZ3N capability that generates/provisions ARCs)
classification: approved-architecture + active-productization-target
amendable: true-additively
current_execution_mode: manual-evidence-producing-replication-via-PRIME
---
```

## Current status

The native RYZ3N **ARC Factory is not yet an operational runtime capability**.

That statement must now be read together with the September current-reality overlay:

- PRIME currently prototypes bounded ARC provisioning/stewardship;
- VONDA is ARC #1 and the reference proving node;
- the Golden ARC Blueprint v1.1 is the current reusable engineering contract;
- Cargo ARC is ARC #2 and is being instantiated manually/boundedly from that contract;
- the purpose of the first replications is to discover exactly what is repeatable, configurable and safety-critical before automating the Factory.

Historical June text that said no ARC runtime implementation should begin immediately was correct for that phase. It does not mean RYZ3N has abandoned the Factory or that current PRIME-mediated ARC prototypes are architectural forks.

## Target responsibility

The ARC Factory should eventually turn an **authorized ARC creation request + configuration package** into a validated isolated ARC instance without bespoke architectural reconstruction.

Target flow:

```text
authorized ARC request
  → creation/governance validation
  → unique arc_id + instance configuration
  → isolated runtime/profile/workspace/secrets
  → identity + approved-user/channel binding
  → permissions + memory/task/Brain namespaces
  → model-capacity-pool assignment
  → telemetry + health + recovery/checkpoint
  → steward/registry registration
  → isolation + functional validation
  → truthful V1 activation/evidence
```

The mature Factory should implement the principle:

> **Build once, instantiate many. Customize by configuration, not architectural fork.**

## What the Factory must NOT do

The Factory must never:

- create a new PRIME per ARC;
- copy another ARC's private memory, credentials, client payload or maturity evidence;
- prebuild an exhaustive specialist Brain catalogue without necessity evidence;
- auto-bind the first unknown user as Owner/primary user;
- grant cross-ARC authority merely because the same Founder/PRIME operates the provisioning layer;
- hard-code customer/company-specific governance into universal RYZ3N logic;
- claim an aura/maturity that the new ARC has not earned;
- provision empty customer ARCs merely to satisfy a commercial cohort count.

## Input contract — current candidate

Cargo ARC #2 is helping validate the minimum Factory input/config contract. Current candidate fields include:

- `arc_id`;
- display identity/domain/purpose;
- Owner and authorized-user roles;
- channel bindings;
- workspace/state namespace;
- secrets boundary;
- permission/escalation policy;
- language/tone where relevant;
- runtime/service identity;
- model route and `model_capacity_pool`;
- telemetry/health/recovery policy;
- commercial/service tier where applicable;
- source repository / evidence pointers;
- migration/export/reassignment contract;
- initial maturity target (normally truthful V1 Foundation) without pre-awarding evidence.

This remains a **candidate contract until ARC #2+ evidence proves it**.

## Creation / necessity doctrine

Creating a separate ARC still requires a genuine reason under current RYZ3N doctrine: real domain/Owner need, strategic opportunity, durable specialization or another valid creation trigger. A new project or feature does not automatically deserve its own ARC.

Within an ARC, specialist Brains follow a separate necessity/evidence lifecycle and are not pre-populated merely because the Factory can create the ARC shell.

## Relationship to PRIME

Current phase:

```text
Founder authorization
  → PRIME bounded provisioning/operator role
  → ARC instance
  → evidence/lessons
  → RYZ3N productization
```

Target mature phase:

```text
Founder / authorized RYZ3N governance
  → RYZ3N ARC Factory + native orchestration
  → ARC instance

PRIME = supervisor / auditor / mentor / high-trust execution steward
```

The transition should change who provisions/orchestrates the ARC, not the ARC's identity, privacy or lifecycle contract.

## Evidence-driven automation path

The durable active backlog is:

`12-arc-productization/PROVISIONING-BACKLOG.md`

Current rule:

> **Do not automate speculation. Automate what repeats or what is safety-critical.**

Cargo ARC is intentionally being built manually enough to measure:

- provisioning steps and time;
- what parameters are truly instance-specific;
- which isolation/security checks repeat;
- identity/binding friction;
- capacity-pool selection;
- telemetry/recovery setup;
- Founder/operator intervention;
- what should become one idempotent Factory action.

After repeated evidence, these steps should move from manual PRIME-mediated execution into native RYZ3N Factory capability.

## Expected future implementation shape

Exact implementation language/files remain an implementation decision, but mature capability should cover equivalents of:

- create/provision ARC;
- validate creation request/config;
- instantiate standard isolated runtime surfaces;
- register ARC and model-capacity attribution;
- run required isolation/health/functional gates;
- checkpoint/version deployed ARC;
- support idempotent update/rollback/migration;
- output durable evidence and truthful current state.

The old June illustrative names such as `factory.py`, `topology.py` and `constitution.py` are historical scaffolding ideas, not mandatory file names.

## Success condition

The ARC Factory becomes credible when a new real authorized ARC can be created with materially less Founder/operator work than earlier ARCs while preserving:

- identity isolation;
- privacy and secrets boundaries;
- correct user binding/access;
- evidence-derived maturity/aura;
- independent health/recovery;
- capacity attribution;
- channel independence;
- migration/exportability;
- canonical RYZ3N alignment.

ARC #10 should require materially less Founder attention than ARC #1 without degrading reliability or user value.

## Current references

- `CURRENT-REALITY-2026-09.md`
- `12-arc-productization/PROVISIONING-BACKLOG.md`
- `12-arc-productization/PRIME-RYZ3N-ARC-PROTOTYPE-DOCTRINE.md`
- `12-arc-productization/ARC-SELF-PROVISIONING-BRAIN-LIFECYCLE.md`
- `Javalin13/VONDA-Corporation/arc/GOLDEN-ARC-BLUEPRINT.md` v1.1
- `Javalin13/CargoConnect` Cargo ARC creation/evidence surfaces
