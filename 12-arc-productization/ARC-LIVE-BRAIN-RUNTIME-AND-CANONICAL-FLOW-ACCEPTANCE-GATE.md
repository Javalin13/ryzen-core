# ARC Live Brain Runtime & Canonical Flow Acceptance Gate

```yaml
---
type: arc-live-runtime-acceptance-gate
status: founder-directed-additive-architecture
created: 2026-09-09
classification: approved-architecture + runtime-governance
scope: autonomous ARC live activation, Brain runtime, PRIME supervision, canonical data/work flows
canonical_refs:
  - Javalin13/ryzen-continuity/00-governance/INTERPRETATION-PROTOCOL.md
  - Javalin13/ryzen-continuity/02-ryzen/architecture/HIERARCHY.md
  - Javalin13/ryzen-continuity/02-ryzen/architecture/CONVERGENCE-LAYER.md
  - Javalin13/ryzen-continuity/03-hermes/HERMES-CANONICAL.md
  - Javalin13/ryzen-continuity/03-hermes/RELATIONSHIP-TO-RYZEN.md
related_standards:
  - 12-arc-productization/ARC-OWNER-DOMAIN-INTENT-ACTIVITY-HIERARCHY.md
  - 12-arc-productization/ARC-SELF-PROVISIONING-BRAIN-LIFECYCLE.md
  - 12-arc-productization/ARC-BRAIN-INTERCONNECT-AND-PRIME-STEWARDSHIP.md
---
```

## Founder decision

An ARC may not be declared `LIVE` merely because its runtime, registry, Brain scaffold, Telegram adapter, or supervision mirror exists.

For live status, the canonical reasoning and evidence mechanisms must actually operate end-to-end in practice, without silent bypasses, dead documentation, lost context, broken upward evidence flow, or PRIME becoming the ARC/Brain.

Required runtime chain for a personal/owner ARC instance:

`Owner input → ARC instance → Domain/Project resolution → Intent resolution → Activity resolution → corresponding Brain selection OR evidence-based Brain creation → Brain reasoning → authorized Agent → Execution → evidence return → Brain → Activity result → Intent progress → Domain/Project state → ARC state → bounded PRIME stewardship/convergence → Founder/Owner visibility`

Canonical ontology remains unchanged:

`Creator → RYZ3N → ARCs → Brains → Agents → Execution`

This gate is an additive runtime implementation standard. It does not amend canonical ontology.

## Hard rule: documentation is not runtime proof

A registry, schema, scaffold, Markdown contract, verifier, or generated mirror is not sufficient evidence that the mechanism actually runs.

Before `LIVE`, the system must prove the real runtime path with controlled end-to-end exercises.

## Mandatory live-runtime mechanisms

### 1. Owner → ARC context intake
The ARC must ingest a real or controlled Owner request and bind it to the correct `arc_instance_id` without leaking another ARC's context.

### 2. Domain / Project resolver
The ARC must resolve or create the relevant Domain/Project context and preserve a truthful status such as:

`idea | planned | preparing | active | validated | paused | closed`

A planned project must never be silently reported as active reality.

### 3. Intent resolver
The ARC must persist what the Owner actually wants to undertake, achieve, change, maintain or decide. Intent must remain traceable to the Owner request and may not be invented by PRIME, a Brain or an Agent.

### 4. Activity resolver
The ARC must translate Intent into a concrete Activity class and maintain an `activity_id` that is traceable through reasoning, execution and evidence return.

### 5. Brain router
For each Activity, the ARC must:
- route to an existing Brain whose scope matches; or
- remain in ARC-level reasoning if no stable specialist Brain is justified; or
- trigger the candidate Brain lifecycle when evidence demonstrates a stable specialization need or explicit Owner/Founder direction requires it.

No Brain may be created merely because a Domain or one-off Activity exists.

### 6. Brain runtime
When a Brain exists, it must be a real runtime reasoning specialization, not only a folder or registry row. It must:
- receive a bounded context envelope;
- load only allowed ARC/Brain memory/data classes;
- reason inside its declared scope;
- return a structured result;
- preserve `arc_instance_id`, `domain_or_project_id`, `intent_id`, `activity_id`, `brain_id`, `correlation_id`, and evidence return path;
- fail closed when required context or permissions are absent.

### 7. Brain-to-Brain interconnect
When two Brains exist and cooperation is materially required, the ARC-local interconnect must be exercised in practice using the bounded envelope defined in `ARC-BRAIN-INTERCONNECT-AND-PRIME-STEWARDSHIP.md`.

It must prove:
- correct source/target Brain identity;
- no silent full-memory sharing;
- allowed data scope enforcement;
- correlation continuity;
- no PRIME↔Lux bridge use for routine Brain traffic;
- no execution authority gained merely through Brain-to-Brain reasoning exchange.

### 8. Agent delegation
External side effects must occur only through an authorized Agent path. Each Agent invocation must preserve parent Brain/ARC ownership, permission boundary, side-effect authority and evidence return path.

### 9. Execution evidence return
Execution must return observable evidence upward. A successful external action without upward evidence is incomplete.

Required upward chain:

`Execution → Agent → Brain → Activity result → Intent progress → Domain/Project state → ARC → PRIME bounded stewardship / RYZ3N-readable convergence → Owner/Founder`

### 10. PRIME ↔ VONDA supervision communication
PRIME must receive only stewardship/control metadata needed to supervise VONDA, including health, lifecycle state, Brain registration/status, evidence references, drift, checkpoint and generalized convergence signals.

PRIME must not:
- become VONDA's reasoning layer;
- ingest unrestricted VONDA private memory;
- carry normal Brain-to-Brain traffic;
- rewrite VONDA's Owner intent;
- silently mutate ARC or Brain source-of-truth state.

Supervision communication must be bidirectionally useful:
- VONDA → PRIME: health, evidence, drift, lifecycle, generalized signal;
- PRIME → VONDA: authorized supervision command, policy/gate result, escalation or Founder-approved instruction.

Every material supervision action must be correlated and auditable.

### 11. Persistence and restart continuity
A runtime restart must not lose the active Domain/Project, Intent, Activity, Brain routing state, authorized workflow checkpoint or evidence chain.

VONDA restart must not restart or corrupt PRIME. PRIME restart/recovery must not merge identities or silently overwrite VONDA private state.

### 12. Failure handling
The live runtime must exercise at least controlled failures for:
- unknown Brain;
- unauthorized data scope;
- invalid interconnect envelope;
- Agent permission denial;
- lost/invalid correlation id;
- unavailable external dependency;
- VONDA restart during an in-flight Activity;
- PRIME supervision unavailable;
- malformed/stale Brain registry mirror.

Each must fail closed where constitution/security requires and preserve enough evidence for diagnosis/recovery.

## Required acceptance exercises before LIVE

At minimum, perform and evidence:

1. ARC-level Activity with zero Brains — request is handled without fabricating a Brain.
2. Candidate Brain creation path — triggered by Founder/Owner-approved stable need; candidate remains non-live until gate passes.
3. First Brain activation — real Brain runtime receives Activity and returns bounded reasoning output.
4. Agent execution path — Brain delegates a safe controlled action and evidence returns all the way upward.
5. Restart-continuity path — restart VONDA mid-checkpoint and prove recovery/continuity without PRIME corruption.
6. PRIME supervision path — prove VONDA→PRIME status/evidence flow and PRIME→VONDA authorized supervision command with correlation/evidence.
7. Privacy-boundary negative test — prove PRIME does not receive prohibited private Brain/ARC payload.
8. Brain-to-Brain path — required only once two justified Brains exist; until then status must remain `DESIGNED / NOT YET EXERCISED`, never falsely `PROVEN`.

## No-fake-live rule

Before the first real Brain exists, VONDA may be `LIVE` as an ARC only if the zero-Brain path is genuinely operational and the system is capable of creating/routing Brains when justified.

However, the Brain mechanism itself may only be reported:
- `READY` when scaffold/runtime hooks/verifiers are implemented;
- `ACTIVE` when at least one real Brain runs in live or controlled production-equivalent runtime;
- `PROVEN` when end-to-end Brain reasoning → Agent → Execution → evidence return has passed;
- `INTERCONNECT-PROVEN` only after two justified Brains successfully exercise bounded ARC-local communication.

## Mandatory live-state triple-check

After activation and after every material Brain/runtime/interconnect change:

### PASS 1 — CANON / REALITY
Read relevant canons and inspect the actual running processes, profiles, registries, routing state, logs, checkpoints, memory boundaries and supervision state.

### PASS 2 — IMPLEMENTATION ALIGNMENT
Verify the actual path matches Founder/Owner intent, canonical hierarchy, approved runtime hierarchy, Brain scope, Agent authority, privacy boundaries, PRIME stewardship boundaries and upward/downward flows.

### PASS 3 — EVIDENCE / FINAL STATE
Prove every material claim with current runtime evidence. If evidence is absent, classify the capability as designed/ready rather than live/proven.

If any pass fails, do not report `LIVE`, `PROVEN`, or `COMPLIANT`; surface drift, correct it, and rerun all three from PASS 1.

## Founder acceptance condition

VONDA live activation is acceptable only when the real system demonstrates that Owner work can travel down the full intended path and evidence can travel back up without loss, bypass, identity mixing, private-data leakage, or silent architectural drift.

> The mechanism must not merely exist on paper. It must run, survive failure, preserve context, preserve evidence, preserve boundaries, and preserve the constitution while doing real work.
