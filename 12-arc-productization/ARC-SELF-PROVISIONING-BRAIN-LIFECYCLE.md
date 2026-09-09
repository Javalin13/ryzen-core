# ARC Self-Provisioning Brain Lifecycle Standard

```yaml
---
type: arc-brain-lifecycle-standard
status: founder-directed-additive-architecture
created: 2026-09-09
classification: approved-architecture + runtime-governance
scope: autonomous ARC nodes, specialist Brain creation, GitHub continuity, PRIME stewardship, future RYZ3N inheritance
canonical_refs:
  - Javalin13/ryzen-continuity/00-governance/INTERPRETATION-PROTOCOL.md
  - Javalin13/ryzen-continuity/02-ryzen/RYZEN-CANONICAL.md
  - Javalin13/ryzen-continuity/02-ryzen/architecture/HIERARCHY.md
  - Javalin13/ryzen-continuity/02-ryzen/architecture/CONVERGENCE-LAYER.md
  - Javalin13/ryzen-continuity/03-hermes/HERMES-CANONICAL.md
  - Javalin13/ryzen-continuity/03-hermes/RELATIONSHIP-TO-RYZEN.md
---
```

## Founder decision

Specialist Brains are not prebuilt as a fixed catalogue.

An autonomous ARC runtime instance (for example VONDA ARC) develops and creates the specialist Brains it actually needs in order to fulfil the intent, needs and outcomes of its Maker/Owner, while remaining inside the ARC framing and the RYZ3N constitutional hierarchy.

Canonical invariant:

`Creator / Owner intent → ARC framing → Brain reasoning specialization → Agents → Execution`

A Brain exists because a stable reasoning specialization becomes necessary, not because the architecture has an empty slot to fill.

## Self-provisioning rule

When an ARC repeatedly encounters a class of reasoning that is materially distinct from its existing reasoning responsibilities, the ARC may propose and, within its delegated authority, create a new Brain specialization.

Examples:

- `BRAINS/COACHING/`
- `BRAINS/COMMUNICATION/`
- `BRAINS/OPERATIONS/`

These names are examples only. The actual Brain taxonomy must emerge from real owner needs and observed ARC work.

No speculative Brain catalogue is required.

## Trigger conditions

A new Brain should be created only when one or more of the following are true:

1. a recurring owner request requires a stable reasoning specialization;
2. an existing Brain is becoming too broad or mixes materially different reasoning responsibilities;
3. repeated workflow evidence shows a distinct reasoning pattern with its own memory, rules, decision boundary or Agent delegation needs;
4. the Owner/Founder explicitly requires a new specialization;
5. a material integration or operational domain requires independent reasoning governance.

A one-off task, prompt, document, tool call, reminder or simple workflow is not enough by itself.

## Mandatory creation sequence

The ARC should follow:

`need observed → candidate Brain proposed → scope check → GitHub Brain folder created → Brain contract seeded → PRIME BRAIN STEWARD registered → runtime routing/usage enabled if needed → evidence accumulated → three-pass validation → status promoted`

## GitHub source-of-truth requirement

Every Brain created by an ARC must produce a durable Brain folder in that ARC's own repository.

Standard shape:

```text
arc/BRAINS/<SPECIALIZATION>/
├── README.md
├── SCOPE.md
├── MEMORY-CONTRACT.md
├── AGENTS.md
├── INTERCONNECT.md
├── DECISIONS.md
└── EVIDENCE.md
```

The minimum initial artifact is `README.md` plus a declared status. Other files may be created as soon as the specialization becomes materially real.

The Brain folder must record at minimum:

- `brain_id`
- owning `arc_definition_id` / `arc_instance_id`
- status: `candidate | prepared | active | validated | deprecated`
- reason for creation
- Owner/Founder intent it serves
- reasoning scope
- explicit non-scope
- permitted memory/data classes
- Agent delegation boundary
- interconnect dependencies
- evidence / validation state
- current version/checkpoint

## Autonomy and authority

The ARC may autonomously create or evolve a Brain only inside its delegated operational scope.

A Brain may not:

- invent Owner/Founder strategic intent;
- redefine the ARC framing;
- rewrite RYZ3N canon;
- grant itself new credentials or external authority;
- gain unrestricted access to another Brain's memory;
- gain cross-ARC private data access;
- silently turn a reasoning specialization into an execution authority.

If the proposed Brain would materially change commercial scope, security posture, external access, legal/contractual boundaries, cross-ARC data rights or canonical architecture, the ARC must stop at proposal/prepared state and escalate upward.

## Brain evolution

Brains are expected to evolve through reality rather than be frozen at birth.

Allowed lifecycle:

`candidate → prepared → active → validated → deprecated/superseded`

Promotion must be evidence-based. Deprecation/supersession is additive: preserve prior records and point to the successor.

## Brain interconnection

Brains inside the same ARC may cooperate through the ARC-local interconnect contract.

No Brain-to-Brain communication should depend on the PRIME↔Lux bridge for normal runtime operation.

The bridge is reserved for material review, drift, unresolved architectural questions, evidence disputes, security/isolation changes and constitutional review.

## PRIME BRAIN STEWARD relationship

PRIME does not create client Brains as their owner and does not become their reasoning layer.

PRIME BRAIN STEWARD:

- observes new Brain registrations;
- keeps a bounded supervision mirror;
- verifies ownership, scope, Agent authority and interconnect coherence;
- detects duplicate or conflicting Brain scopes;
- checks that new Brain creation serves actual Owner intent;
- triggers constitutional checks after material changes;
- preserves upward evidence/convergence without copying private client memory;
- records drift when a Brain exceeds its authority;
- makes the pattern transferable to future native RYZ3N stewardship.

## Three-pass validation

After creation or material evolution of a Brain:

### PASS 1 — Reality
Verify what actually exists and is being used.

### PASS 2 — Implementation alignment
Verify that the Brain serves Owner/Founder intent, remains within ARC framing, has bounded scope and delegates execution correctly.

### PASS 3 — Evidence
Verify that the claimed specialization, runtime state and usefulness are supported by current evidence.

If any pass fails, the Brain may remain candidate/prepared but may not be reported as validated.

## Future RYZ3N inheritance

The mature RYZ3N runtime should eventually provide native support for:

- Brain registration;
- Brain lifecycle/versioning;
- Brain-template contracts;
- interconnect routing;
- Agent ownership validation;
- evidence convergence;
- drift detection;
- Brain Steward functionality.

The ARC must not need to be redesigned when this responsibility moves from PRIME-mediated stewardship to native RYZ3N orchestration.

## Founder principle

> Brains emerge from need. The ARC creates the specialization required to fulfil its Owner's intent, records it durably, proves it against reality, and remains inside the constitution.

> Do not prebuild intelligence taxonomy. Let reality generate the Brain map.
