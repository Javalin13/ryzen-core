# PRIME / VONDA ARC — Canonical Architecture Assessment

Date: 2026-09-09
Status: architectural assessment
Classification: current-reality + approved-architecture comparison
Scope: RYZ3N canonical thinking layers, PRIME prototype supervision, autonomous VONDA ARC runtime

## Constitutional basis

This assessment treats the RYZ3N canonicals as constitutional invariants, interpreted through:

- `ryzen-continuity/00-governance/INTERPRETATION-PROTOCOL.md`
- `ryzen-continuity/02-ryzen/RYZEN-CANONICAL.md`
- `ryzen-continuity/02-ryzen/architecture/HIERARCHY.md`
- `ryzen-continuity/02-ryzen/architecture/CONVERGENCE-LAYER.md`
- `ryzen-continuity/03-hermes/RELATIONSHIP-TO-RYZEN.md`

Current implementation/reference layers:

- `12-arc-productization/PRIME-RYZ3N-ARC-PROTOTYPE-DOCTRINE.md`
- `12-arc-productization/AUTONOMOUS-ARC-NODE-RUNTIME.md`
- `12-arc-productization/RYZ3N-CONSTITUTION-COMPLIANCE-GATE.md`
- `12-arc-productization/PROVISIONING-BACKLOG.md`
- `12-arc-productization/founding-pilots/VONDA-ARC-FOUNDATION-2026-09-09.md`

Latest runtime evidence supplied by PRIME states that Hermes v0.20.6 profile isolation was proven live for VONDA: independent `HERMES_HOME`, `.env`, `config.yaml`, `state.db`, gateway state, logs, Telegram binding boundary, separate process lifecycle, and clean shutdown, while sharing only the VPS host, Python venv and OS kernel with PRIME.

The Interpretation Protocol governs the rating: reality > doctrine, implementation > aspiration, evidence > theory.

---

## 1. Canonical structure vs current implementation mirror

### Canonical ontology

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

### Current prototype runtime

```text
Founder strategic intent
  ↓
PRIME — Hermes-based supervisor / operational control plane
  ↓
VONDA ARC — autonomous Hermes runtime node
  ↓
VONDA reasoning + workflow components
  ↓
Agents / adapters / tools
  ↓
Telegram + external execution
  ↓
Observed reality / evidence
  ↑
logs + checkpoints + decisions + lessons + incidents
  ↑
PRIME supervision
  ↑
RYZ3N-readable productization / Founder
```

This is not a replacement hierarchy. It is a practical implementation mirror of the canonical hierarchy.

The most important architectural success is that **PRIME is not inserted into the canonical ontology**. PRIME acts as the present operational interpreter/supervisor while RYZ3N's future native runtime is incomplete.

---

## 2. Layer-by-layer fidelity assessment

### 2.1 Creator / Founder layer

**Canonical requirement**
- Founder is the source of strategic intent.
- Final authority remains with the Founder.
- Lower layers may propose and execute, but may not invent strategic intent.

**Current implementation**
- Founder issues explicit GO gates for VONDA activation, commercial scope, access, transfer, credentials, migration and pilot clock.
- PRIME does not independently activate VONDA.
- VONDA is designed to refer material scope/access/contract decisions upward.

**Strength**
Very high fidelity. The Founder remains both constitutional authority and activation authority.

**Weakness / risk**
Too many low-level approvals could become Founder bottlenecks if not later delegated through explicit policy.

**Rating: 9.8/10**

---

### 2.2 RYZ3N layer — architecture, governance, convergence, strategic coordination

**Canonical requirement**
RYZ3N is the ecosystem architecture itself, not Hermes, not a product and not a runtime process.

**Current implementation**
- RYZ3N remains constitutional/canonical architecture.
- PRIME does not claim to be RYZ3N.
- PRIME prototype lessons are structured into `ryzen-core` for future RYZ3N inheritance.
- Canonical changes are not silently written from runtime behavior.

**Strength**
The separation between architecture and implementation is now unusually clean. The system can learn from runtime without confusing runtime with constitution.

**Weakness / risk**
The actual native RYZ3N runtime/orchestrator does not yet exist. Cross-ARC registry, governance enforcement, memory federation, verification and convergence are still largely represented through PRIME + GitHub patterns.

**What still needs building**
- Native ARC registry.
- Native provisioning/factory capability.
- Native governance engine/gates.
- Native convergence ingestion and classification.
- Native observability across ARC nodes without client-memory mixing.
- Native migration from PRIME-supervised control to RYZ3N-supervised control.

**Rating: 9.4/10 architectural fidelity, 4.5/10 native implementation maturity**

---

### 2.3 ARC layer — domain framing + autonomous node

**Canonical requirement**
ARCs hold domain framing. They do not become mere execution agents.

**Current implementation**
VONDA ARC is now modeled as an autonomous node with:
- own Hermes profile/runtime identity;
- own gateway lifecycle;
- own Telegram binding;
- own config/state/memory/secrets/logs/checkpoints;
- own commercial/access/data policies;
- own user/business context;
- bounded escalation to PRIME.

**Strength**
This is one of the strongest areas. The ARC is no longer implemented as a renamed chat/session inside PRIME. The node has its own identity and state boundary, which closely reflects the canonical notion that an ARC is a first-class architectural component.

**Weakness / risk**
The current VONDA ARC still contains some operational-assistant behaviors that conceptually belong below the ARC layer. The distinction between VONDA's domain framing, internal reasoning units ('Brains'), and execution agents has not yet been formalized as separate runtime components.

**What still needs building**
Define VONDA-specific reasoning units without overengineering. Candidate pattern only after evidence:
- Context/Business Brain
- Operations/Priority Brain
- Communication/Drafting Brain
- Governance/Boundary Brain
Then map tool-using execution entities under those Brains.

Do not implement named Brains merely because the canon contains the concept. Promote only when repeated VONDA usage demonstrates stable reasoning boundaries.

**Rating: 9.7/10 node architecture; 7.6/10 internal ARC-layer decomposition maturity**

---

### 2.4 Brain layer — reasoning units

**Canonical requirement**
Brains reason within an ARC's domain frame and do not execute directly.

**Current implementation**
Reasoning exists functionally in VONDA's workflows, memory categories, policies and Hermes intelligence, but is not yet represented as explicit stable Brain components.

**Strength**
The implementation has not prematurely invented a complex Brain hierarchy. This respects the Interpretation Protocol.

**Weakness**
Reasoning boundaries are implicit. As VONDA grows, this can produce monolithic prompt/context behavior and unclear ownership of decisions.

**What still needs building**
- Observe real usage first.
- Identify recurring reasoning classes.
- Create Brain contracts only where reasoning is stable enough to warrant separation.
- Define inputs, outputs, authority, memory visibility and agent delegation per Brain.

**Rating: 7.0/10**

---

### 2.5 Agent layer — execution entities

**Canonical requirement**
Agents execute within Brain framing, observe, and report. They do not invent strategy or architecture.

**Current implementation**
Telegram adapter, reminders, drafting, gateway actions, future integrations and PRIME operational scripts function as execution mechanisms, but a formal Agent registry/contract is not yet present for VONDA.

**Strength**
Execution is bounded by permissions, client scope and escalation policy.

**Weakness**
Agent identity and authority are not yet consistently explicit. It may become unclear whether a workflow is reasoning, policy, adapter or execution.

**What still needs building**
- Minimal Agent contract: identity, Brain owner, allowed tools, allowed writes, evidence output, rollback behavior.
- No generic agent swarm. Create only agents tied to validated recurring workflows.

**Rating: 7.3/10**

---

### 2.6 Execution layer — action against reality

**Canonical requirement**
Execution is the point where actions touch reality. Upward observation must return.

**Current implementation**
- Hermes runtime/process behavior has been tested live.
- VONDA profile starts independently and fails closed without platform credentials.
- Isolation verifier and forged-leak negative test have been reported PASS.
- Telegram live client activation is not yet completed.

**Strength**
The system is now beyond paper architecture: process isolation and lifecycle behavior have been observed.

**Weakness**
The most important client-level execution proof is still pending: real Laetitia ↔ VONDA Telegram interaction under production-like policies and memory.

**What still needs building/testing**
- Telegram bot token injection through secure secret path.
- Authorized `chat_id` binding.
- Live first-run onboarding.
- Memory persistence test.
- Unauthorized-chat fail-closed test.
- Contract/security escalation test to PRIME.
- Reminder/task execution test.
- Restart + continuation test after live state exists.
- Non-destructive rollback test.

**Rating: 8.5/10 pre-live execution maturity**

---

## 3. Hermes / PRIME constitutional relationship

### Canonical
Hermes serves RYZ3N as operational infrastructure. Hermes does not become the ecosystem architecture.

### Present mirror
PRIME is effectively the high-trust Hermes-derived operational supervisor used to prove the runtime model.

```text
RYZ3N constitution / future brain
      ↓ governing architecture
PRIME / Hermes supervisor
      ↓ operationalizes + verifies
VONDA autonomous Hermes node
      ↓ reasons / delegates
Agents + adapters
      ↓
Execution
```

This is structurally coherent with the old canonical mental model of **Founder = will, RYZ3N = brain, Hermes = hands**, provided PRIME remains operational and does not become the source of architecture.

### Strong point
This relationship is now substantially cleaner than the earlier shared-gateway design. VONDA has its own Hermes runtime while PRIME remains supervisor rather than identity host.

### Attention point
PRIME currently combines several practical roles: operator, supervisor, verifier, provisioning authority and escalation receiver. Mature RYZ3N should absorb governance/orchestration functions so PRIME does not become an accidental permanent central monolith.

**Rating: 9.6/10 constitutional relationship fidelity**

---

## 4. Upward/downward information flow

Canonical flow:

```text
Down: Creator → RYZ3N → ARC → Brain → Agent → Execution
Up:   Execution → Agent → Brain → ARC → RYZ3N → Creator
```

Current prototype approximation:

```text
Down:
Founder → PRIME → VONDA policy/context/workflow → adapter/tool → action

Up:
action/test/user reality → VONDA logs/checkpoints/lessons/incidents → PRIME → GitHub productization/convergence → Founder
```

### Strong points
- Checkpoints introduced.
- Decision and lesson structures exist.
- Verification evidence is preserved.
- Drift is explicitly surfaced rather than normalized.
- Security/contract escalation is designed upward to PRIME.

### Weak point
The upward path is still operator-mediated and file-mediated rather than a native RYZ3N convergence system.

### Build next
Standardize a machine-readable ARC evidence envelope later, e.g.:
- `arc_id`
- event/evidence type
- classification
- timestamp
- severity
- privacy class
- generalized/not-generalized flag
- source checkpoint/version

This can later become native convergence input.

**Rating: 9.0/10 conceptual fidelity; 6.5/10 automation maturity**

---

## 5. Interpretation Protocol compliance

### Reality > doctrine
PASS. The architecture was corrected after PRIME demonstrated Hermes `--profile/-p` as the actual native isolation primitive. The implementation was changed to reflect what Hermes truly supports rather than forcing the earlier shared-routing theory.

### Implementation > aspiration
PASS with caveat. VONDA autonomous runtime has been proven at process/profile level, but client-live Telegram operation remains pending and must not be reported as live.

### Evidence > theory
PASS with caveat. Runtime/process/isolation evidence exists by PRIME report. Live client workflow evidence does not yet exist.

### Anti-hallucination discipline
Current state must be classified as:
- autonomous Hermes runtime: **implemented / verified pre-live**;
- Telegram bot/client binding: **prepared / not activated**;
- VONDA client workflows: **designed, partly scaffolded, not yet validated through sustained real use**;
- RYZ3N native orchestration: **approved architecture / future implementation**;
- Brains/Agents decomposition: **conceptual / to be evidence-driven**.

**Rating: 9.8/10 interpretation-discipline alignment**

---

## 6. Strongest architectural qualities

1. **Recursive structural mirroring** — the prototype is a smaller operational reflection of the future RYZ3N → ARC model rather than a dead-end bot integration.
2. **Constitution/runtime separation** — the canon remains stable while runtime experimentation remains additive and evidence-driven.
3. **Autonomous node identity** — VONDA is a first-class node, not a disguised PRIME session.
4. **Migration-preserving contracts** — same ARC meaning can survive shared VPS → dedicated VPS → future RYZ3N orchestration.
5. **Bidirectional learning path** — execution produces lessons/evidence back toward productization.
6. **Fail-closed/security boundaries** — unauthorized or unconfigured routes do not silently fall back into PRIME.
7. **Founder sovereignty** — material gates stay explicit.
8. **No premature canonical rewrite** — prototype reality informs future standards without mutating constitutional source files.

---

## 7. Weakest points / architectural debt

1. **Native RYZ3N runtime missing.** PRIME still performs functions RYZ3N is intended to own later.
2. **Brains are implicit.** Reasoning boundaries are not yet formal components.
3. **Agents are implicit.** Execution authority/tool contracts need clearer runtime representation as the system grows.
4. **Same Unix user / same kernel.** Hermes-profile isolation is real, but not equivalent to host/container/user security isolation.
5. **Live-client evidence missing.** Laetitia has not yet exercised the system in real operation.
6. **Convergence is file/operator mediated.** It is structurally correct but not yet native or automatic.
7. **Provisioning is not yet factory-grade.** VONDA proves the pattern, not yet repeatable one-command production provisioning.
8. **Rollback/offboarding distinction must remain strict.** Normal rollback must preserve data/state; destructive purge must be separately authorized.
9. **Secrets portability needs hardened procedure.** Exports must not casually package live tokens/credentials.
10. **Resource/capacity evidence still thin.** Same-VPS multi-ARC economics and performance need measurement over time.

---

## 8. What should be built next — ordered by constitutional value

### P0 — Before VONDA live activation
1. Non-destructive rollback path.
2. Secret-safe export/migration procedure.
3. Dedicated VONDA systemd/service lifecycle proof.
4. Telegram token + allowed chat binding.
5. Unauthorized chat negative test.
6. VONDA → PRIME bounded incident/escalation signal test.
7. Final constitutional three-pass check after activation configuration.

### P1 — First live pilot evidence
1. First-run onboarding through VONDA itself.
2. Capture Laetitia's 3–5 recurring workflows.
3. Validate memory categories and retention preferences.
4. Validate reminders, meeting prep, drafting, priorities and follow-up.
5. Observe confusion/friction/support needs.
6. Measure RAM/CPU/storage/log growth and restart behavior.
7. Record generalized lessons into RYZ3N productization.

### P2 — ARC internal structural maturation
1. Identify stable reasoning domains from real use.
2. Introduce explicit Brain contracts only where justified by evidence.
3. Introduce Agent contracts for stable external actions.
4. Define machine-readable ARC evidence/event envelope.
5. Strengthen OS-level isolation options for higher tiers.

### P3 — Replication
1. Provision ARC #2 from template without VONDA-specific state.
2. Compare setup time, errors, resource use and Founder attention.
3. Automate only repeated/safety-critical steps.
4. Validate shared VPS vs dedicated VPS tier model.

### P4 — Future RYZ3N native runtime
1. ARC registry.
2. Provisioning/factory.
3. Governance enforcement.
4. Verification/observability plane.
5. Evidence convergence.
6. Cross-ARC generalized intelligence.
7. Native migration of supervision from PRIME to RYZ3N.

---

## 9. Attention points for architectural purity

- Never let `PRIME → ARC` become a new canonical hierarchy.
- Never call a Hermes profile itself the ARC; the profile is runtime infrastructure for the ARC.
- Never let Telegram become the ARC identity/source of truth.
- Never promote VONDA private data into cross-ARC intelligence.
- Never call planned Brains/Agents implemented until observable evidence exists.
- Never let PRIME silently define strategy, architecture or client commercial policy.
- Preserve upward evidence flow after every material execution.
- Preserve additive evolution: reality can trigger a proposal/ADR, not silent canonical rewriting.
- Repeat the three-pass constitutional check after every material runtime change.

---

## 10. Master-level rating

### Architectural fidelity to canonical structure
**9.6 / 10**

### Fidelity of PRIME/Hermes role to canon
**9.6 / 10**

### Autonomous ARC node execution fidelity
**9.5 / 10**

### Upward/downward information-flow fidelity
**9.0 / 10**

### Brain/Agent decomposition fidelity
**7.2 / 10**

### Reality/evidence discipline
**9.8 / 10**

### Current native RYZ3N runtime maturity
**4.5 / 10**

### Overall current implementation accuracy relative to the intended constitutional architecture

# **9.3 / 10**

The rating is intentionally not 10/10. The design-to-runtime correspondence is exceptionally tight, but the constitutional model is broader than what is currently implemented: native RYZ3N orchestration, explicit evidence-driven Brain/Agent separation, live-client proof, stronger host isolation options and automated convergence are still incomplete.

---

## 11. Final judgment

The current PRIME/VONDA build is no longer merely a theoretical demonstration of the canon. It is a **real bounded implementation mirror** of the RYZ3N constitutional structure.

The strongest engineering decision was moving from a shared PRIME chat/gateway model to an autonomous Hermes profile/runtime for VONDA under PRIME supervision. That creates a clean joint between today's operational reality and tomorrow's RYZ3N-native ARC network.

The architecture should now evolve by evidence, not by adding more conceptual layers. VONDA should go live, produce real operational evidence, and force the next structural decisions from reality.

Constitutional rule for the next phase:

> **Do not add a layer because the canon names it. Add a runtime boundary when reality proves the boundary exists.**

> **Do not simplify away a constitutional boundary merely because the runtime could. Preserve the invariant and let implementation mature toward it.**
