# ARC Self-Provisioning Brain Lifecycle Standard

```yaml
---
type: arc-brain-lifecycle-standard
status: founder-directed-additive-architecture
created: 2026-09-09
updated: 2026-09-11
classification: approved-architecture + runtime-governance
scope: autonomous ARC nodes, specialist Brain creation, GitHub continuity, PRIME stewardship, OMEGA ARC stewardship, future RYZ3N inheritance
canonical_refs:
  - Javalin13/ryzen-continuity/00-governance/INTERPRETATION-PROTOCOL.md
  - Javalin13/ryzen-continuity/02-ryzen/RYZEN-CANONICAL.md
  - Javalin13/ryzen-continuity/02-ryzen/architecture/HIERARCHY.md
  - Javalin13/ryzen-continuity/02-ryzen/architecture/CONVERGENCE-LAYER.md
  - Javalin13/ryzen-continuity/03-hermes/HERMES-CANONICAL.md
  - Javalin13/ryzen-continuity/03-hermes/RELATIONSHIP-TO-RYZEN.md
runtime_refinement:
  - Javalin13/ryzen-core/12-arc-productization/ARC-OWNER-DOMAIN-INTENT-ACTIVITY-HIERARCHY.md
  - Javalin13/ryzen-core/12-arc-productization/OMEGA-ARC-FACTORY-STEWARDSHIP-STANDARD.md
---
```

## Founder decision

Specialist Brains are not prebuilt as a fixed catalogue.

For personal/owner ARC instances, the ARC serves one Owner/Person coherently across multiple Domains and Projects. The ARC first resolves context through:

`ARC instance → Domain/Project → Intent → Activity → Corresponding Brain → Agents → Execution`

An autonomous ARC runtime instance develops and creates the specialist Brains it actually needs to fulfil the Owner's intent while remaining inside the canonical ARC framing and the RYZ3N constitutional hierarchy.

The canonical ontology remains:

`Creator → RYZ3N → ARCs → Brains → Agents → Execution`

The Domain/Project → Intent → Activity chain is an instance-level runtime refinement beneath the ARC layer, not a replacement canonical tier.

PRIME stewardship is now separated operationally into:

- **OMEGA** for ARC-level lifecycle/population stewardship;
- **BRAIN STEWARD** for Brain-level lifecycle/interconnection stewardship.

Neither is a new canonical tier.

## Context-resolution rule

Before routing to or creating a Brain, the ARC must resolve:

1. **Domain/Project** — where in the Owner's reality this belongs;
2. **Intent** — what the Owner wants to undertake, achieve or change;
3. **Activity** — what concrete class of work is required;
4. **Corresponding Brain** — which stable reasoning specialization should handle it.

A Domain/Project may be `idea`, `planned`, `preparing`, `active`, `validated`, `paused` or `closed`. A future project may exist in ARC context without being falsely reported as operational reality.

## Self-provisioning rule

When an ARC repeatedly encounters a class of reasoning that is materially distinct from its existing Brain responsibilities, the ARC may propose and, within delegated authority, create a new Brain specialization.

The Brain is justified by a stable Activity/reasoning need, not by an empty architecture slot.

Examples such as `BRAINS/COACHING/`, `BRAINS/COMMUNICATION/` or `BRAINS/OPERATIONS/` are illustrative only. The actual Brain taxonomy must emerge from real Owner needs, Domains/Projects, Intents and Activities.

## Trigger conditions

A new Brain should be created only when one or more are true:

1. a recurring Activity requires a stable reasoning specialization;
2. an existing Brain is becoming too broad or mixes materially different reasoning responsibilities;
3. repeated workflow evidence shows a distinct reasoning pattern with its own memory, rules, decision boundary or Agent delegation needs;
4. the Owner/Founder explicitly requires a specialization;
5. a material integration or operational activity requires independent reasoning governance.

A one-off prompt, document, reminder, tool call or simple workflow is not enough by itself.

## Mandatory creation sequence

The ARC follows:

`Domain/Project resolved → Owner Intent resolved → Activity identified → reasoning need observed → existing Brain match OR candidate Brain → scope/authority check → GitHub Brain folder/contract → PRIME BRAIN STEWARD bounded registration → OMEGA owning-ARC coherence check → runtime routing if needed → Agent delegation → Execution → evidence returns upward → three-pass validation → status promotion`

OMEGA does not approve the Brain's reasoning. Its role in this sequence is only to verify that the owning ARC identity/lifecycle record remains coherent with BRAIN STEWARD's Brain registration.

## GitHub source-of-truth requirement

Every Brain created by an ARC must produce a durable Brain folder in that ARC's own repository:

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

Minimum initial artifact: `README.md` plus declared status. Additional contract files are added as the specialization becomes materially real.

The Brain folder must record at minimum:

- `brain_id`;
- owning `arc_definition_id` / `arc_instance_id`;
- Domain/Project context served;
- Owner Intent reference;
- Activity class served;
- status: `candidate | prepared | active | validated | deprecated`;
- reason for creation;
- reasoning scope and explicit non-scope;
- permitted memory/data classes;
- Agent delegation boundary;
- interconnect dependencies;
- evidence / validation state;
- version/checkpoint.

## Autonomy and authority

The ARC may autonomously create or evolve a Brain only inside delegated operational scope.

A Brain may not:

- invent Owner/Founder intent;
- redefine the ARC framing;
- rewrite RYZ3N canon;
- grant itself new credentials or external authority;
- gain unrestricted access to another Brain's memory;
- gain cross-ARC private data access;
- silently become an execution authority.

If a proposed Brain would materially change commercial scope, security posture, external access, legal/contractual boundaries, cross-ARC data rights or canonical architecture, the ARC stops at proposal/prepared and escalates upward.

## Brain evolution

Allowed lifecycle:

`candidate → prepared → active → validated → deprecated/superseded`

Promotion is evidence-based. Deprecation/supersession is additive and preserves prior records.

## Brain interconnection

Brains inside the same ARC may cooperate through the ARC-local interconnect contract. Normal Brain-to-Brain operation must not depend on the PRIME↔Lux bridge.

The bridge is reserved for material review, drift, unresolved architecture, evidence disputes, security/isolation changes and constitutional review.

## PRIME BRAIN STEWARD relationship

PRIME does not create client Brains as their owner and does not become their reasoning parent.

PRIME BRAIN STEWARD:

- observes Brain lifecycle registrations;
- keeps bounded Brain supervision metadata;
- verifies Domain/Project → Intent → Activity → Brain mapping without ingesting private payloads;
- verifies Brain ownership, scope, Agent authority and interconnect coherence;
- detects duplicate/conflicting Brain scopes;
- checks that Brain creation serves real Owner intent/activity;
- triggers constitutional checks after material change;
- preserves upward evidence/convergence without copying private client memory;
- records Brain-level drift;
- coordinates the owning ARC identity/lifecycle facts with OMEGA;
- keeps the pattern transferable to future native RYZ3N stewardship.

## OMEGA relationship

OMEGA is PRIME's separate ARC-population steward.

OMEGA does **not** own or reason for specialist ARC Brains. It:

- confirms the Brain belongs to a registered ARC;
- confirms the ARC appears in PRIME's `FACTORY.md` and OMEGA ARC registry;
- receives only the bounded ARC-level lifecycle implications of material Brain changes;
- coordinates ARC-level health/maturity/drift facts with BRAIN STEWARD;
- escalates ARC-level contradictions or orphaned Brain ownership to PRIME.

BRAIN STEWARD remains authoritative for Brain lifecycle supervision; OMEGA remains authoritative for ARC lifecycle supervision.

## Upward evidence flow

Evidence must be able to return:

`Execution → Agent → Brain → Activity result → Intent progress → Domain/Project state → ARC → OMEGA/BRAIN STEWARD bounded stewardship → PRIME/RYZ3N-readable convergence → Owner/Founder`

Private payloads remain ARC-scoped; only authorized/generalized metadata and reusable lessons converge upward.

## Three-pass validation

After creation or material evolution of a Brain or context hierarchy:

### PASS 1 — CANON / REALITY
Read current canonical sources and verify what actually exists and is used.

### PASS 2 — IMPLEMENTATION ALIGNMENT
Verify canonical authority plus the Founder-approved runtime refinement:

`ARC instance → Domain/Project → Intent → Activity → Corresponding Brain → Agents → Execution`

### PASS 3 — EVIDENCE / FINAL STATE
Verify claimed specialization, runtime state, usefulness and classifications with current evidence.

If any pass fails, surface drift, correct it, and rerun all three from PASS 1. A Brain may remain candidate/prepared but may not be reported as validated.

## Future RYZ3N inheritance

Mature RYZ3N should eventually provide native support for:

- Owner/ARC context registry;
- ARC Factory/identity/lifecycle registry;
- Domain/Project state;
- Intent/Activity routing;
- Brain registration/lifecycle/versioning;
- Brain-template contracts;
- interconnect routing;
- Agent ownership validation;
- evidence convergence;
- ARC + Brain drift detection;
- OMEGA-equivalent ARC stewardship;
- Brain Steward functionality.

The ARC must not need redesign when responsibility moves from PRIME-mediated stewardship to native RYZ3N orchestration.

## Founder principle

> One Owner is served by one coherent personal ARC instance. Domains and Projects give context. Intent states what the Owner wants. Activity states what must be done. The corresponding Brain provides specialized reasoning. Agents execute. OMEGA safeguards ARC lifecycle coherence, BRAIN STEWARD safeguards Brain coherence, and reality/evidence determine what deserves to exist.
