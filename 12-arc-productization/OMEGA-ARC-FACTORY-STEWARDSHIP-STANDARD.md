# OMEGA ARC Factory & Stewardship Standard

```yaml
---
type: prime-arc-stewardship-standard
status: founder-directed-additive-architecture
created: 2026-09-11
classification: approved-architecture + runtime-governance
scope: PRIME ARC stewardship, ARC creation registry, lifecycle oversight, future RYZ3N inheritance
canonical_refs:
  - Javalin13/ryzen-continuity/02-ryzen/RYZEN-CANONICAL.md
  - Javalin13/ryzen-continuity/02-ryzen/architecture/HIERARCHY.md
related_standards:
  - 12-arc-productization/ARC-BRAIN-INTERCONNECT-AND-PRIME-STEWARDSHIP.md
  - 12-arc-productization/ARC-SELF-PROVISIONING-BRAIN-LIFECYCLE.md
  - 12-arc-productization/ARC-FORM-AURA-AND-TRANSFER-RESET-STANDARD.md
---
```

## Founder decision

PRIME requires a dedicated ARC-population stewardship capability named **OMEGA** and a separate master ARC creation/lifecycle register named **FACTORY**.

OMEGA is **not an ARC** and must never be described as one.

OMEGA is a PRIME-owned stewardship Brain/function that supervises the ARC population on PRIME's behalf during the current prototype era.

FACTORY is not a Brain and not an authority layer. It is the durable master record of ARC creation, identity, provenance and lifecycle state.

The canonical ontology remains unchanged:

`Creator → RYZ3N → ARCs → Brains → Agents → Execution`

PRIME, OMEGA, BRAIN STEWARD and FACTORY are current implementation/stewardship infrastructure around that ontology. Native RYZ3N is intended to inherit equivalent capability later without inserting a new canonical tier.

## Responsibility split

### PRIME
PRIME remains the current supervisor/orchestrator. PRIME receives material reports, exceptions, constitutional drift, unresolved conflicts and Founder-routed decisions. PRIME must not become the day-to-day manual registry operator for every ARC lifecycle event.

### OMEGA
OMEGA owns ARC-population stewardship for PRIME.

OMEGA must:

- supervise every known ARC instance across its lifecycle;
- coordinate registration of newly created ARCs;
- maintain the authoritative ARC supervision registry in PRIME;
- ensure every ARC has one stable `arc_id`, source pointer and ownership record;
- verify every new ARC receives the required isolation, governance and supervision contracts;
- track lifecycle status, health, maturity/evidence state, form/aura state, ownership-transfer state and retirement state;
- coordinate with BRAIN STEWARD for Brain-level facts without taking over Brain reasoning;
- detect missing, duplicate, orphaned or contradictory ARC registrations;
- detect ARC-level drift and escalate material issues to PRIME;
- produce portfolio-level ARC status/reporting for PRIME and the Founder;
- record lifecycle events in FACTORY;
- ensure resets/transfers are truthfully reflected in maturity/aura state;
- preserve the controlled-mirror/privacy boundary;
- preserve history rather than silently rewriting ARC provenance;
- prepare the stewardship pattern for eventual native RYZ3N inheritance.

OMEGA may not:

- invent Founder/Owner intent;
- redefine RYZ3N canon;
- become a canonical tier above ARCs;
- act as the reasoning parent of client ARC Brains;
- ingest unrestricted private ARC memory or secrets;
- silently execute external side effects outside delegated authority;
- falsely promote maturity or aura;
- erase prior ownership/reset/provenance history.

### BRAIN STEWARD
BRAIN STEWARD remains responsible for the Brain population inside ARCs: Brain lifecycle, scope, interconnect, Agent ownership, evidence and constitutional coherence.

OMEGA asks: **Which ARCs exist, who owns them, what state are they in, and what requires PRIME attention?**

BRAIN STEWARD asks: **Which Brains exist inside those ARCs, why do they exist, and are their reasoning/Agent boundaries coherent?**

Neither replaces the other.

### FACTORY
`FACTORY.md` is PRIME's master ARC creation and lifecycle register.

For every ARC, FACTORY must retain at minimum:

- `arc_id`;
- display name/type;
- creation/genesis timestamp or first known registration date;
- source repository/path;
- source/genesis version or commit pointer where available;
- Owner/entity identity class and current ownership state;
- origin/template/blueprint version;
- current lifecycle status;
- runtime/provisioning status;
- current maturity/version and evidence status;
- current maturity aura;
- form baseline / factory-form version;
- Brain registry pointer;
- PRIME supervision mirror pointer;
- OMEGA registration status;
- model-capacity-pool assignment where applicable;
- transfer history;
- factory-reset history;
- maturity/capacity reset history;
- retirement/suspension history;
- latest known-safe checkpoint/evidence pointer;
- material drift/incidents;
- current source-of-truth pointer.

FACTORY is a registry, not a private-memory mirror. It must not store raw client conversations, unrestricted documents, secrets, credentials or other unnecessary private payloads.

## ARC birth gate

A newly created ARC is not considered fully registered/provisioned merely because a repository or runtime folder exists.

Every new ARC must pass the following birth sequence:

`Founder/authorized creation intent → ARC identity reserved → source repository/runtime prepared → OMEGA registration → FACTORY entry → PRIME supervision mirror → isolation/governance checks → runtime provisioning → evidence gate → truthful lifecycle status`

Minimum birth artifacts:

1. stable `arc_id`;
2. ARC-side identity/instance record;
3. source repository pointer;
4. OMEGA registration pointer/status;
5. FACTORY entry;
6. PRIME `ARCS/<ARC-ID>/` supervision entry;
7. Brain-registry location, even if empty;
8. form/aura/maturity baseline;
9. ownership and privacy boundary;
10. current lifecycle status and evidence state.

An ARC may remain `prepared` or `provisioning_pending`; the birth gate requires truthful registration, not false activation.

## New-ARC inheritance requirement

Every future ARC blueprint/template must include OMEGA/FACTORY registration as part of creation. No future ARC should require a later retrofit merely to become visible to PRIME.

Each ARC-side source should expose a bounded registration artifact or equivalent metadata containing at least:

- `arc_id`;
- source repository;
- Owner/entity class;
- creation/registration date;
- lifecycle state;
- maturity/aura state;
- form baseline;
- OMEGA steward pointer;
- FACTORY pointer;
- PRIME supervision-mirror pointer;
- Brain registry pointer;
- privacy-safe evidence/checkpoint pointer.

## Form, aura, reset and transfer logging

Founder invariant remains:

> **Form is Owner-resettable. Aura is maturity-derived.**

A normal factory-form/look reset may restore the visual/form baseline without changing earned maturity or aura.

A sale/transfer does not automatically force V1. However, if transfer/reset genuinely removes or invalidates the Owner-specific state, competence or evidence that supported maturity and the ARC becomes effectively empty for the new Owner, the truthful state becomes:

`V1 Foundation → Blue aura`

OMEGA must record every material form reset, ownership transfer, competence/capacity reset and resulting maturity/aura decision in FACTORY with provenance/evidence pointers.

Aura may never be manually reset as an independent Owner cosmetic choice.

## Supervision mirror rule

PRIME keeps a bounded supervision mirror under `ARCS/<ARC-ID>/`.

OMEGA maintains ARC-level lifecycle coherence in that mirror. BRAIN STEWARD maintains Brain-level coherence.

The client/ARC repository remains the detailed source for private ARC implementation state. PRIME does not become an unrestricted duplicate data store.

## Reporting and escalation

OMEGA should handle routine ARC-population reporting and only escalate material matters to PRIME, including:

- missing or contradictory identity/ownership records;
- failed isolation or security boundary;
- orphaned ARC or missing source pointer;
- material health failure or inability to recover;
- maturity/aura contradiction;
- disputed transfer/reset consequence;
- cross-ARC privacy breach;
- constitutional drift;
- unresolved conflict between ARC-level state and Brain-level evidence;
- Founder-directed review.

Routine lifecycle registration should not require Founder micromanagement.

## Current implementation mapping

During the PRIME prototype era:

```text
PRIME
├── FACTORY.md
├── BRAINS/
│   ├── OMEGA/
│   │   ├── README.md
│   │   └── ARC-REGISTRY.md
│   └── BRAIN-STEWARD/
└── ARCS/
    └── <ARC-ID>/
```

The intended authority flow remains canonical. This layout is operational infrastructure only.

## Future RYZ3N inheritance

Native RYZ3N should eventually absorb the proven functions of:

- ARC identity reservation;
- ARC Factory/provisioning registry;
- ARC lifecycle/version tracking;
- ownership/transfer/reset state;
- maturity/aura verification;
- ARC health/drift supervision;
- portfolio reporting;
- Brain Steward interoperability;
- controlled convergence/evidence routing.

OMEGA and FACTORY therefore must be implemented as transferable contracts, not permanent shadow hierarchy.

## Founder principle

> PRIME supervises. OMEGA watches the ARC population. BRAIN STEWARD watches the Brains. FACTORY remembers every ARC that was created and what happened to it. None of them replace RYZ3N canon.
