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
  - 12-arc-productization/ARC-REPOSITORY-OWNERSHIP-AND-SOURCE-BOUNDARY-STANDARD.md
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

There is no separate Horizon/Horizon Core orchestration layer. **RYZ3N is the sole canonical platform identity above ARCs.**

## Responsibility split

### PRIME
PRIME remains the current supervisor/orchestrator. PRIME receives material reports, exceptions, constitutional drift, unresolved conflicts and Founder-routed decisions. PRIME must not become the day-to-day manual registry operator for every ARC lifecycle event.

### OMEGA
OMEGA owns ARC-population stewardship for PRIME.

OMEGA must:

- supervise every known ARC instance across its lifecycle;
- coordinate registration of newly created ARCs;
- maintain the authoritative ARC supervision registry in PRIME;
- ensure every ARC has one stable `arc_id`, one authoritative source boundary, source pointer and ownership record;
- verify every new ARC receives the required repository classification, isolation, governance and supervision contracts;
- track lifecycle status, health, maturity/evidence state, form/aura state, ownership-transfer state and retirement state;
- coordinate with BRAIN STEWARD for Brain-level facts without taking over Brain reasoning;
- detect missing, duplicate, orphaned or contradictory ARC registrations;
- detect dual-active source-of-truth repositories and force resolution before activation;
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
- erase prior ownership/reset/provenance history;
- relocate an ARC to RYZ3N Core or PRIME merely for convenience when an authoritative domain repository already exists.

### BRAIN STEWARD
BRAIN STEWARD remains responsible for the Brain population inside ARCs: Brain lifecycle, scope, interconnect, Agent ownership, evidence and constitutional coherence.

OMEGA asks: **Which ARCs exist, who owns them, where is their authoritative source, what state are they in, and what requires PRIME attention?**

BRAIN STEWARD asks: **Which Brains exist inside those ARCs, why do they exist, and are their reasoning/Agent boundaries coherent?**

Neither replaces the other.

### FACTORY
`FACTORY.md` is PRIME's master ARC creation and lifecycle register.

For every ARC, FACTORY must retain at minimum:

- `arc_id`;
- display name/type;
- repository class (`ryz3n_owned_product_domain` or `customer_standalone_domain`, or later canonical equivalent);
- authoritative source repository/path;
- ARC root path in that repository;
- creation/genesis timestamp or first known registration date;
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
- repository/source-boundary migration history where applicable;
- factory-reset history;
- maturity/capacity reset history;
- retirement/suspension history;
- latest known-safe checkpoint/evidence pointer;
- material drift/incidents;
- current source-of-truth pointer.

FACTORY is a registry, not a private-memory mirror. It must not store raw client conversations, unrestricted documents, secrets, credentials or other unnecessary private payloads.

## Repository/source-boundary classification gate

Before active OMEGA registration and FACTORY activation, every ARC must receive one authoritative repository/source-boundary classification under:

`12-arc-productization/ARC-REPOSITORY-OWNERSHIP-AND-SOURCE-BOUNDARY-STANDARD.md`

Current classes:

1. **RYZ3N-owned product/domain ARC** — lives inside the existing product/domain repository under a bounded ARC package/path. Example: Cargo ARC in `Javalin13/CargoConnect/arc/`; future Fleet ARC in `Javalin13/FleetConnect/arc/`.
2. **Customer / standalone domain ARC** — lives inside one dedicated or already-existing appropriate private customer/domain repository. Example: VONDA ARC in `Javalin13/VONDA-Corporation/arc/`; NARC will receive a Narek/customer-domain repository at birth.

One ARC must not have two simultaneously authoritative Git repositories. PRIME is a supervision plane and RYZ3N Core is universal canon; neither becomes the detailed owning source for an ARC instance merely because they can see it.

## ARC birth gate

A newly created ARC is not considered fully registered/provisioned merely because a repository or runtime folder exists.

Every new ARC must pass the following birth sequence:

`Founder/authorized creation intent → classify owning domain/source boundary → designate/create authoritative repository → reserve ARC identity → initialize ARC-side source → OMEGA registration → FACTORY entry → PRIME supervision mirror → isolation/governance checks → runtime provisioning → evidence gate → truthful lifecycle status`

Minimum birth artifacts:

1. stable `arc_id`;
2. repository class/source-boundary decision;
3. authoritative source repository + ARC root path;
4. ARC-side identity/instance record;
5. OMEGA registration pointer/status;
6. FACTORY entry;
7. PRIME `ARCS/<ARC-ID>/` supervision entry;
8. Brain-registry location, even if empty;
9. form/aura/maturity baseline;
10. ownership and privacy boundary;
11. current lifecycle status and evidence state.

An ARC may remain `prepared` or `provisioning_pending`; the birth gate requires truthful registration, not false activation.

## New-ARC inheritance requirement

Every future ARC blueprint/template must include repository/source-boundary classification and OMEGA/FACTORY registration as part of creation. No future ARC should require a later retrofit merely to become visible to PRIME or to discover where its authoritative source belongs.

Each ARC-side source should expose a bounded registration artifact or equivalent metadata containing at least:

- `arc_id`;
- repository class;
- authoritative source repository + ARC root path;
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

If a transfer or restructuring changes the authoritative owning repository, OMEGA/FACTORY must record the source-boundary migration and update all pointers atomically while preserving provenance. Repository movement alone does not reset maturity.

## Supervision mirror rule

PRIME keeps a bounded supervision mirror under `ARCS/<ARC-ID>/`.

OMEGA maintains ARC-level lifecycle coherence in that mirror. BRAIN STEWARD maintains Brain-level coherence.

The **owning domain/customer/product repository** remains the detailed source for ARC implementation/domain state. PRIME does not become an unrestricted duplicate data store. RYZ3N Core remains universal reusable canon, not an ARC-instance payload repository.

## Reporting and escalation

OMEGA should handle routine ARC-population reporting and only escalate material matters to PRIME, including:

- missing or contradictory identity/ownership records;
- ambiguous or duplicate authoritative source boundary;
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
RYZ3N Core
└── universal ARC canon / schemas / standards

PRIME
├── FACTORY.md
├── BRAINS/
│   ├── OMEGA/
│   │   ├── README.md
│   │   └── ARC-REGISTRY.md
│   └── BRAIN-STEWARD/
└── ARCS/
    └── <ARC-ID>/           # bounded supervision mirror

Owning domain repositories
├── CargoConnect/arc/       # Cargo ARC
├── FleetConnect/arc/       # future Fleet ARC
├── VONDA-Corporation/arc/  # VONDA ARC
└── <customer-domain>/arc/  # future customer ARC such as NARC
```

The intended authority flow remains canonical. This layout is operational/source-governance infrastructure only.

## Future RYZ3N inheritance

Native RYZ3N should eventually absorb the proven functions of:

- ARC identity reservation;
- repository/source-boundary classification;
- ARC Factory/provisioning registry;
- ARC lifecycle/version tracking;
- ownership/transfer/reset state;
- maturity/aura verification;
- ARC health/drift supervision;
- portfolio reporting;
- Brain Steward interoperability;
- controlled convergence/evidence routing.

OMEGA and FACTORY therefore must be implemented as transferable contracts, not permanent shadow hierarchy.

No additional platform layer is inserted. **RYZ3N itself is the future native orchestration/control platform.**

## Founder principle

> PRIME supervises. OMEGA watches the ARC population. BRAIN STEWARD watches the Brains. FACTORY remembers every ARC that was created, where its authoritative source belongs and what happened to it. None of them replace RYZ3N canon.
