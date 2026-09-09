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
related_standards:
  - 12-arc-productization/ARC-OWNER-DOMAIN-INTENT-ACTIVITY-HIERARCHY.md
  - 12-arc-productization/ARC-SELF-PROVISIONING-BRAIN-LIFECYCLE.md
---
```

## Decision

Normal Brain-to-Brain runtime communication must **not** use the PRIME ↔ Luxcalibur bridge.

The PRIME ↔ Luxcalibur bridge is a review/governance/audit channel. It remains appropriate for material drift, architecture review, constitutional checks, evidence disputes, blockers, and Founder-routed review. It is not the runtime nervous system of ARC Brains.

The canonical ontology remains:

`Creator → RYZ3N → ARCs → Brains → Agents → Execution`

For the personal/owner ARC runtime pattern, context is resolved beneath the ARC layer as:

```text
ARC Runtime Instance
  ↓
Domain / Project
  ↓
Intent
  ↓
Activity
  ↓
Corresponding Brain
  ↓
Agents
  ↓
Execution
```

The ARC may hold multiple Domains/Projects for one Owner without fragmenting into separate personal ARCs merely because the subject changes. Projects may also exist as `idea`, `planned` or `preparing` before real execution begins.

Brains are **not** pre-seeded as a mandatory fixed taxonomy. The ARC selects an existing Brain or creates a new one only when the Activity requires a stable reasoning specialization.

Brain cooperation inside one ARC occurs through a bounded ARC-local interconnect contract. Cross-ARC interaction is promoted upward as generalized evidence/signals and stewarded by PRIME today, later by native RYZ3N convergence.

## Source-of-truth placement

Each client/personal ARC owns the implementation record of its specialist Brains in its own repository, for example:

`VONDA-Corporation/arc/BRAINS/COACHING/`

A Brain folder represents a stable reasoning specialization justified by a real `Domain/Project → Intent → Activity` chain, not merely a workflow or prompt.

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

The supervision mirror may contain source commit pointers, non-sensitive Domain/Project identifiers/status, Brain identities/statuses, Activity classes, health, dependency metadata, generalized evidence, checkpoints and drift. It must not duplicate client-private memory, live secrets, raw confidential payloads or unrestricted client documents.

## BRAIN STEWARD

`PRIME/BRAINS/BRAIN-STEWARD` is an operational stewardship function, not a new canonical tier and not a canonical Brain above other Brains.

It must:

- observe/register self-provisioned Brain lifecycle changes;
- verify every Brain maps to a real Owner Intent and Activity inside an ARC Domain/Project;
- verify Domain/Project state is truthfully classified;
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
- `domain_or_project_id`
- `intent_id`
- `activity_id`
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
Agent
  ↑
Brain
  ↑
Activity result / Intent progress / Domain-Project state
  ↑
ARC
  ↑
PRIME BRAIN STEWARD / generalized evidence envelope
  ↑
RYZ3N-readable convergence
```

Only generalized, authorized, non-confidential patterns move into shared intelligence unless an explicit integration contract authorizes a scoped cross-ARC exchange.

## Bridge boundary

Use PRIME ↔ Luxcalibur bridge for material architecture review, constitutional audits, unresolved drift/contradiction, material Brain role changes, evidence disputes, significant security/isolation changes, or Founder-directed review.

Do not use it for normal Brain-to-Brain messages, routine runtime context exchange, task delegation inside one ARC, high-frequency event transport, private client data movement, or every ordinary self-provisioned Brain creation that remains safely inside delegated ARC scope.

Routine lifecycle events are logged locally and mirrored to BRAIN STEWARD. Only material/review-worthy changes escalate through the bridge.

## Constitutional mapping

The architecture preserves:

`Creator → RYZ3N → ARCs → Brains → Agents → Execution`

Current runtime mirror:

`Founder/Owner → PRIME supervision → autonomous ARC instance → Domain/Project → Intent → Activity → corresponding Brain → Agents → Execution`

PRIME stewardship is implementation infrastructure around the hierarchy, not an inserted ontology layer.

## Three-pass requirement

After a material Brain creation, context-routing/interconnect change, Agent delegation change, cross-ARC integration or stewardship change:

1. **Canon / Reality** — read the relevant canons and verify what actually exists/runs.
2. **Implementation alignment** — compare reality against canonical hierarchy and the Founder-approved runtime refinement.
3. **Evidence / Final state** — prove claims and classifications with current evidence.

After correction, rerun all three from Pass 1.

## Founder rule

> One personal ARC instance serves one Owner coherently across Domains and Projects. Intent defines what the Owner wants. Activity defines what must be done. The corresponding Brain provides specialized reasoning. Agents execute. PRIME safeguards coherence without becoming the ARC or the Brain.
