# Model-Independent Mission Controller Architecture — 2026-09-13

**Status:** ACTIVE TARGET ARCHITECTURE  
**Scope:** PRIME, OMEGA, Factory-created ARCs, shared mission/control plane  
**Constitution/Canon impact:** none — additive execution architecture  
**Companion lesson:** `MODEL-INDEPENDENT-MISSION-CONTROL-LESSON-2026-09-13.md`

## Core principle

> **The LLM provides intelligence. The mission controller provides truth, continuity, acceptance and termination authority.**

Recursive-agent behavior remains useful, but recursion alone is not sufficient to guarantee completion of a bounded mission across model swaps, provider overload, session resets or persona drift.

The RYZ3N architecture therefore separates:

- **mission/control plane** — deterministic, durable and model-independent;
- **intelligence plane** — replaceable model/provider capability routing;
- **execution plane** — Hermes tools, repositories, runtime and platform actions;
- **evidence plane** — bridge receipts, commits, tests, runtime proofs and Founder-visible mini reports.

---

# Full architecture scheme

```text
┌──────────────────────────────────────────────────────────────────────┐
│                           FOUNDER / LUX                             │
│  Founder = final authority                                          │
│  Lux = architecture / control / review / acceptance supervision     │
└───────────────────────────────┬──────────────────────────────────────┘
                                │
                                │ intent / directive / acceptance policy
                                ▼
┌──────────────────────────────────────────────────────────────────────┐
│                     DURABLE MISSION SOURCE                          │
│                                                                      │
│  PRIME master work:                                                  │
│    Javalin13/ryzen-core/TO_PRIME.md                                 │
│    Javalin13/ryzen-core/FROM_PRIME.md                               │
│                                                                      │
│  ARC-local work:                                                     │
│    authoritative ARC repository + ARC-local bridge                   │
│                                                                      │
│  GitHub / source truth outranks chat-session memory.                 │
└───────────────────────────────┬──────────────────────────────────────┘
                                │
                                │ consume / resume / sync
                                ▼
┌──────────────────────────────────────────────────────────────────────┐
│              MODEL-INDEPENDENT MISSION CONTROLLER                  │
│                                                                      │
│  Owns:                                                               │
│    • mission_id                                                      │
│    • authoritative source pointer                                    │
│    • consumed source revision / commit                               │
│    • bounded scope                                                   │
│    • mission state                                                   │
│    • acceptance gates                                                │
│    • checkpoint                                                      │
│    • timeout / recovery policy                                       │
│    • capability lane requested                                       │
│    • provider/model health state                                     │
│    • circuit-breaker state                                           │
│    • elapsed time / ETA                                              │
│    • Founder/Lux decision dependency                                 │
│    • final durable receipt                                           │
│                                                                      │
│  Mission states:                                                     │
│    PENDING → ACTIVE → VERIFYING → GREEN                              │
│                  ↘ BLOCKED                                          │
│                  ↘ RECOVERING → ACTIVE                              │
│                  ↘ FAILED                                            │
│                                                                      │
│  The LLM cannot unilaterally mark GREEN.                             │
└───────────────────────────────┬──────────────────────────────────────┘
                                │
                                │ bounded execution context
                                ▼
┌──────────────────────────────────────────────────────────────────────┐
│                    HERMES RECURSIVE AGENT LOOP                     │
│                                                                      │
│  observe → reason → select action → tool call → observe → repeat    │
│                                                                      │
│  Hermes supplies recursive execution behavior, but remains          │
│  subordinate to the durable mission controller.                     │
└───────────────────────────────┬──────────────────────────────────────┘
                                │
                                │ capability request
                                ▼
┌──────────────────────────────────────────────────────────────────────┐
│                    RYZ3N CAPABILITY ROUTER                         │
│                                                                      │
│  FAST_INTERACTIVE  → Nemotron Super                                 │
│  DEEP_REASONING    → Nemotron Ultra when warranted + healthy        │
│  MULTIMODAL        → Nemotron Omni perception → Super/Ultra         │
│  BACKGROUND_LIGHT  → local Qwen when safe                           │
│  BACKGROUND_NORMAL → Super                                          │
│  EMERGENCY_LOCAL   → local Qwen restricted continuity               │
│                                                                      │
│  Shared Ultra circuit:                                               │
│    overload / 503 / excessive latency                               │
│        → open 60–120 s cooldown                                     │
│        → route interactive work to Super                            │
│        → one half-open Ultra probe                                  │
│        → restore deep-lane eligibility only after success           │
│                                                                      │
│  Planned account governor: ~35 RPM operating target under           │
│  observed ~40 RPM NVIDIA shared limit.                              │
└───────────────────────────────┬──────────────────────────────────────┘
                                │
                                │ model intelligence
                                ▼
┌──────────────────────────────────────────────────────────────────────┐
│                      EXECUTION / TOOL PLANE                        │
│                                                                      │
│  • shell / runtime                                                   │
│  • GitHub repositories                                               │
│  • ARC bridges                                                       │
│  • media / vision / transcription paths                             │
│  • application/runtime tools                                        │
│  • tests / probes / diagnostics                                      │
│                                                                      │
│  Tool results return to Hermes and mission controller.              │
└───────────────────────────────┬──────────────────────────────────────┘
                                │
                                │ evidence / receipts
                                ▼
┌──────────────────────────────────────────────────────────────────────┐
│                    ACCEPTANCE-GATE VALIDATOR                       │
│                                                                      │
│  Example PRIME engineering mission:                                 │
│                                                                      │
│    required source inspected?           □                           │
│    required change/inspection done?     □                           │
│    required tests/proofs completed?     □                           │
│    FROM_PRIME written?                  □                           │
│    commit pushed?                       □                           │
│    privacy/isolation preserved?         □                           │
│    acceptance criteria satisfied?       □                           │
│                                                                      │
│  ANY NO  → mission remains ACTIVE/BLOCKED/RECOVERING                │
│  ALL YES → mission may transition to GREEN                          │
└───────────────────────────────┬──────────────────────────────────────┘
                                │
                                │ GREEN receipt
                                ▼
┌──────────────────────────────────────────────────────────────────────┐
│                        REPORT / SYNC LAYER                          │
│                                                                      │
│  PRIME writes detailed engineering result to FROM_PRIME.md          │
│  ARC writes detailed ARC-local result to its own bridge/source      │
│                                                                      │
│  Founder receives only MINI REPORT:                                 │
│    STATUS / CHANGED / NEXT / TIME+ETA / LUX / BRIDGE                │
│                                                                      │
│  If LUX: SYNC NEEDED                                                 │
│      Founder says `sync`                                             │
│      Lux reviews detailed source directly                            │
│      Lux updates TO_PRIME / canonical source                         │
│      Founder says `consume`                                          │
│      mission continues                                               │
└──────────────────────────────────────────────────────────────────────┘
```

---

# `consume` target behavior

`consume` should become a real control-plane operation, not merely a natural-language instruction that the current model may interpret differently.

```text
consume
  ↓
resolve authoritative mission source
  ↓
fetch / reconcile current source revision
  ↓
read TO_PRIME or ARC-local directive
  ↓
load existing durable mission state if present
  ↓
create mission state if new
  ↓
validate bounded scope + authority
  ↓
mark ACTIVE
  ↓
select capability lane
  ↓
run Hermes recursive agent
  ↓
checkpoint durable progress
  ↓
validate acceptance gates
  ├─ incomplete → continue / recover / re-route
  ├─ blocked    → durable blocker receipt + MINI REPORT
  └─ complete   → write/push receipt → GREEN → MINI REPORT
```

The Founder must not need to reconstruct technical context after a model/provider/session failure.

---

# `sync` target behavior

```text
sync
  ↓
Lux reads latest pushed FROM_PRIME / ARC-local report
  ↓
Lux cross-checks source + evidence + runtime acceptance
  ↓
Lux accepts / rejects / narrows next gate
  ↓
Lux updates TO_PRIME or authoritative ARC source
  ↓
commit / push
  ↓
Founder receives command view only
  ↓
next consume
```

The Founder is the decision authority, not the human copy/paste transport.

---

# Model/provider replacement behavior

A model replacement must be an **intelligence-layer substitution** only.

Changing the model/provider may alter:

- latency;
- reasoning depth;
- style;
- tool-call quality;
- context handling;
- cost/capacity characteristics.

It must **not** alter:

- mission identity;
- mission source;
- acceptance gates;
- Founder authority;
- Owner bindings;
- ARC sovereignty;
- privacy boundaries;
- durable checkpoints;
- recovery semantics;
- receipt requirements;
- closure criteria.

If a replacement model produces persona drift, unrelated prose or premature completion, the mission controller must treat that as non-evidence and keep the mission open.

---

# Provider overload / crash recovery scheme

```text
ACTIVE MISSION
    ↓
provider stalls / model overloaded / chat crashes / /reset
    ↓
mission state remains durable
    ↓
RECOVERING
    ↓
fetch latest source + checkpoint
    ↓
validate already-satisfied gates
    ↓
do not repeat closed diagnostics
    ↓
route to best healthy capability lane
    ↓
resume ACTIVE
```

A session reset does not equal a mission reset.

---

# Capability lane decision inputs

The router should eventually consider bounded signals such as:

- explicit deep-reasoning request;
- code/architecture complexity;
- multimodal input presence;
- tool/action criticality;
- expected latency budget;
- provider health/circuit state;
- shared RPM pressure;
- whether work is foreground interactive or background;
- whether local continuity is sufficient;
- privacy/isolation restrictions.

The router should not need raw Owner-private history merely to choose a capability lane.

---

# PRIME / OMEGA / ARC roles

## PRIME

PRIME uses the mission controller for:

- shared runtime/infrastructure;
- portfolio coordination;
- cross-ARC work;
- privileged operator actions;
- OMEGA/Factory coordination;
- escalations outside one ARC's authority.

PRIME does not become the day-to-day conversational relay for an operational ARC.

## OMEGA

OMEGA should inherit the same control-plane pattern for:

- ARC registry oversight;
- Factory-created ARC lifecycle tracking;
- capability/maturity/version state;
- reset/transfer lifecycle coordination;
- cross-ARC health and bounded reporting to PRIME.

## ARCs

Operational ARCs inherit a bounded local mission controller for their own domain:

- ARC-local source truth;
- ARC-local task state;
- ARC-local acceptance gates;
- direct Owner interaction;
- ARC-local receipts;
- escalation to PRIME only when crossing authority boundaries.

ARC mission control must not require unrestricted Owner-private content mirroring to PRIME or OMEGA.

---

# Evidence hierarchy

From strongest to weakest:

1. real runtime acceptance proof;
2. pushed source / durable receipt;
3. reproducible test result;
4. local unpushed state;
5. model statement about what it believes it did;
6. conversational prose.

A model saying `done`, `green` or producing a narrative response is never sufficient by itself.

---

# Completion invariant

For every bounded mission, define objective gates before execution.

Example:

```text
MISSION: implement free capability router

GATES:
  [ ] native/config/plugin integration point inspected
  [ ] implementation boundary approved
  [ ] runtime change applied
  [ ] Cargo fast-interactive proof passes
  [ ] Ultra deep-lane proof passes when healthy
  [ ] overload/circuit behavior proven
  [ ] Omni path preserved
  [ ] local Qwen emergency continuity preserved
  [ ] PRIME parity proven
  [ ] ARC isolation preserved
  [ ] FROM_PRIME receipt pushed
  [ ] Lux review accepted
```

Until all required gates are satisfied or a concrete external blocker is durably reported, the mission must not transition to GREEN.

---

# Founder-facing command view

The Founder should continue receiving the compact operational view:

```text
MASTER: Mx/16 — <stage>
CURRENT: <bounded substep>
STATUS: <GREEN / AMBER / RED>
PROGRESS: <evidence-based estimate>
ELAPSED: <actual known time>
ETA: <current estimate>
NEXT: <one dependency/action>
```

Detailed engineering exchange remains in GitHub bridges/source.

---

# Factory inheritance

Future Factory-created ARCs should receive this architecture by default:

- durable source pointer;
- mission-state store;
- acceptance-gate contract;
- capability-router access;
- crash/provider recovery semantics;
- ARC-local bridge pair;
- PRIME/OMEGA escalation boundary;
- privacy-preserving bounded status reporting;
- explicit closure receipts.

The control plane should be part of ARC birth, not bolted on after failures occur.

---

# Anti-drift invariants

The following never count as mission completion while gates remain open:

- generic persona prose;
- role-play;
- narrative closing language;
- `No function calls have been executed` when required work is still pending;
- provider fallback notices;
- model self-assertion that work is complete;
- process/PID existence without functional proof;
- local unpushed report when durable push is required.

When any such event occurs, mission state remains open and the controller must continue, recover, re-route or produce a concrete blocker.

---

# Current 2026-09-13 lesson linkage

This architecture was reinforced by real PRIME migration evidence:

- Ultra showed repeated provider overload/stalls;
- one session drifted into Hermes persona prose after reading the mission source;
- another session returned a tool-free completion statement while `FROM_PRIME.md` remained untouched;
- these behaviors exposed that mission closure was still too dependent on model behavior;
- therefore capability routing and model-independent mission control must be developed together.

## Canonical final principle

> **The capability router chooses who thinks.**  
> **Hermes decides how to recursively work.**  
> **The mission controller decides what remains true until the work is objectively complete.**  
> **Founder remains final authority.**
