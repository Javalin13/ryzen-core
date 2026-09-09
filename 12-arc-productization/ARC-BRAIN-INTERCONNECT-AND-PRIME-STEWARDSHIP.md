# ARC Brain Interconnect & PRIME Stewardship Standard

```yaml
---
type: arc-brain-interconnect-standard
status: founder-directed-additive-architecture
created: 2026-09-09
classification: approved-architecture + runtime-governance
scope: autonomous ARC nodes, Brain registries, PRIME stewardship, future RYZ3N convergence
canonical_refs:
  - Javalin13/ryzen-continuity/02-ryzen/RYZEN-CANONICAL.md
  - Javalin13/ryzen-continuity/02-ryzen/architecture/HIERARCHY.md
  - Javalin13/ryzen-continuity/02-ryzen/architecture/CONVERGENCE-LAYER.md
  - Javalin13/ryzen-continuity/03-hermes/RELATIONSHIP-TO-RYZEN.md
---
```

## Decision

Normal Brain-to-Brain runtime communication must **not** use the PRIME ↔ Luxcalibur bridge.

The PRIME ↔ Luxcalibur bridge is a review/governance/audit channel. It remains appropriate for material drift, architecture review, constitutional checks, evidence disputes, blockers, and Founder-routed review. It is not the runtime nervous system of ARC Brains.

The runtime structure is:

```text
ARC Definition / Framing
  ↓
ARC Runtime Instance
  ↓
BRAINS/
  ├── specialist Brain A
  ├── specialist Brain B
  └── specialist Brain N
       ↓
     Agents
       ↓
     Execution
```

Brain cooperation inside one ARC occurs through a bounded ARC-local interconnect contract. Cross-ARC interaction is promoted upward as generalized evidence/signals and stewarded by PRIME today, later by native RYZ3N convergence.

## Source-of-truth placement

Each client/project ARC owns the canonical implementation record of its specialist Brains in its own repository, for example:

`VONDA-Corporation/arc/BRAINS/COACHING/`

A Brain folder represents a stable reasoning specialization, not merely a workflow or prompt.

PRIME keeps a **supervision mirror**, not a full private fork:

```text
prime-vps-migration/
├── BRAINS/
│   └── BRAIN-STEWARD/
└── ARCS/
    └── <ARC-ID>/
        ├── README.md
        ├── SOURCE-POINTER.md
        ├── BRAIN-REGISTRY.md
        ├── INTERCONNECT.md
        ├── HEALTH.md
        ├── DRIFT.md
        └── EVIDENCE.md
```

The supervision mirror may contain source commit pointers, Brain identities/statuses, health, dependency metadata, generalized evidence, checkpoints, and drift. It must not duplicate client-private memory, live secrets, raw confidential payloads, or unrestricted client documents.

## BRAIN STEWARD

`PRIME/BRAINS/BRAIN-STEWARD` is an operational stewardship function, not a new canonical tier and not a canonical Brain above other Brains.

It must:

- keep ARC/Brain registry coherence;
- verify every Brain has one owning ARC and bounded reasoning scope;
- prevent Brain-to-Brain circular authority or silent ARC reframing;
- validate Agent ownership and external side-effect authority;
- track dependencies and conflict between Brains;
- preserve upward evidence flow;
- classify what may converge toward RYZ3N and what stays private;
- trigger the constitutional three-pass check after material structural change;
- keep PRIME as supervisor, not hidden RYZ3N replacement.

## ARC-local Brain interconnect contract

A Brain may request context or reasoning from another Brain only through a bounded envelope containing at least:

- `source_brain_id`
- `target_brain_id`
- `arc_instance_id`
- `purpose`
- `requested_context_class`
- `allowed_data_scope`
- `expected_output`
- `decision_owner`
- `side_effect_allowed: true|false`
- `evidence_return_path`
- `correlation_id`

No Brain may silently gain the target Brain's full memory or permissions.

For external execution, the receiving Brain still delegates through an Agent contract. Brain-to-Brain communication itself is reasoning/context exchange, not execution authority.

## Cross-ARC rule

Direct private Brain-to-Brain cross-client memory access is prohibited.

Cross-ARC flow should normally be:

```text
Execution evidence
  ↑
Brain
  ↑
ARC
  ↑
PRIME BRAIN STEWARD / generalized evidence envelope
  ↑
RYZ3N-readable convergence
```

Only generalized, authorized, non-confidential patterns move into shared intelligence unless an explicit integration contract authorizes a scoped cross-ARC exchange.

## Bridge boundary

Use PRIME ↔ Luxcalibur bridge for:

- material architecture review;
- constitutional compliance audits;
- unresolved drift/contradiction;
- review-worthy Brain creation or role changes;
- evidence disputes;
- significant security/isolation changes;
- Founder-directed review.

Do not use it for:

- normal Brain-to-Brain messages;
- routine runtime context exchange;
- task delegation inside one ARC;
- high-frequency event transport;
- private client data movement.

## Constitutional mapping

The architecture preserves:

`Creator → RYZ3N → ARCs → Brains → Agents → Execution`

Current runtime mirror:

`Founder intent → PRIME supervision → autonomous ARC instance → Brains → Agents → Execution`

PRIME stewardship is implementation infrastructure around the hierarchy, not an inserted ontology layer.

## Three-pass requirement

After a material Brain creation, interconnect change, Agent delegation change, cross-ARC integration, or stewardship change:

1. **Reality** — verify what actually exists/runs.
2. **Implementation** — compare against Founder intent + canonical hierarchy + approved scope.
3. **Evidence** — prove material claims with current evidence.

After correction, rerun all three on the final state.

## Founder rule

> Specialist Brains live with their ARC. PRIME keeps a bounded supervision mirror. BRAIN STEWARD guards coherence. The PRIME↔Lux bridge reviews the architecture; it does not carry the architecture's everyday nervous-system traffic.
