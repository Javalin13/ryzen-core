# Model-Independent Mission Control Lesson — 2026-09-13

**Status:** ACTIVE ARCHITECTURE LESSON  
**Scope:** PRIME, OMEGA, Factory-created ARCs, shared agent-control layer  
**Constitution/Canon impact:** none — additive execution architecture

## Lesson

A recursive agent must not rely on the currently selected LLM to preserve mission truth, workflow state or completion discipline.

The language model supplies intelligence. The mission controller supplies continuity, state, acceptance gates and termination authority.

Canonical shorthand:

> **Model intelligence is replaceable; mission continuity must be deterministic.**

## Evidence from the 2026-09-13 model replacement

After replacing the previous PRIME model route with NVIDIA Nemotron:

- PRIME/Hermes remained capable of recursive tool use and source reads;
- Ultra provider latency/overload repeatedly caused long stalls;
- after a fresh `consume`, one session drifted into generic Hermes/persona prose instead of completing the bounded bridge task;
- another fresh session began task-oriented work but later returned `No function calls have been executed in this session` despite the mission still being incomplete;
- repository-root `FROM_PRIME.md` remained untouched, proving no valid acceptance receipt had been produced;
- therefore recursion alone did not guarantee mission completion.

This is not treated as proof that Hermes recursion is fundamentally broken. It proves that model-specific behavior can expose a missing control-plane invariant: the LLM was still allowed to decide that a turn/session was complete even when the durable mission acceptance gate was not satisfied.

## Architectural conclusion

The RYZ3N agent stack should separate **intelligence execution** from **mission control**.

```text
Founder / Lux / Owner intent
        ↓
Durable mission source
(GitHub bridge / ARC-local source)
        ↓
MODEL-INDEPENDENT MISSION CONTROLLER
        ↓
mission_id / state / acceptance gates / checkpoint / timeout policy
        ↓
Hermes recursive agent loop
        ↓
capability router
   ├─ Super — fast interactive
   ├─ Ultra — deep reasoning when healthy
   ├─ Omni — perception
   └─ Qwen — emergency continuity
        ↓
tools / runtime / repositories
        ↓
MISSION CONTROLLER verifies acceptance
        ├─ NOT SATISFIED → continue / recover / re-route
        └─ SATISFIED     → close mission + emit receipt
```

## Required mission-state properties

A durable mission controller should track at minimum:

- `mission_id`;
- authoritative source pointer / repository / bridge file;
- consumed source revision / commit;
- bounded task scope;
- mission state such as `PENDING`, `ACTIVE`, `BLOCKED`, `RECOVERING`, `VERIFYING`, `GREEN`, `FAILED`;
- required acceptance gates;
- last durable checkpoint;
- last successful tool/action evidence;
- model/provider route currently serving the mission;
- retry/fallback/circuit state;
- elapsed time and current ETA where applicable;
- explicit Founder/Lux decision dependency when required;
- final durable receipt / commit.

## Completion invariant

The LLM must not be the sole authority deciding that a bounded engineering mission is finished.

For a bridge-driven PRIME task, completion should require objective evidence such as:

```text
required source inspected?          YES
required implementation/test done?  YES
required FROM_PRIME report written? YES
required commit pushed?              YES
acceptance criteria satisfied?       YES
```

Only then may the mission controller transition to `GREEN` and permit the final MINI REPORT.

If one or more required gates are false, conversational prose must not substitute for completion.

## `consume` should become a control-plane command

Long-term target behavior:

```text
consume
  ↓
fetch authoritative source
  ↓
load current TO_PRIME / ARC-local directive
  ↓
create or resume durable mission state
  ↓
mark mission ACTIVE
  ↓
run recursive agent under bounded scope
  ↓
verify acceptance gates
  ↓
write/push required receipt
  ↓
close mission only when verified
```

`consume` should not depend only on the LLM semantically understanding the word.

## Session/provider crash recovery

A provider timeout, overloaded model, `/reset`, session crash or model replacement must not reset the mission.

Recovery order:

1. load the latest durable mission state;
2. fetch the authoritative source revision;
3. verify which acceptance gates are already satisfied;
4. preserve proven work and avoid repeating closed diagnostics;
5. select the best currently healthy model route;
6. continue from the last durable checkpoint;
7. close only after acceptance verification.

## Model-replacement invariant

Future model swaps must be treated as **intelligence-layer substitutions**, not workflow migrations.

Changing Super, Ultra, a future NVIDIA model, OpenAI model or another provider must not alter:

- mission identity;
- Founder authority;
- ARC Owner boundaries;
- bridge/source truth;
- acceptance gates;
- recovery semantics;
- audit/receipt requirements;
- privacy/isolation boundaries.

A new model may change quality, speed and reasoning style. It must not redefine the mission lifecycle.

## Capability-router relationship

This lesson complements the free capability router:

- Super = default fast interactive intelligence;
- Ultra = deep-reasoning lane when healthy and warranted;
- Omni = perception specialist;
- Qwen = restricted emergency continuity;
- mission controller = model-independent workflow authority.

The capability router chooses **who thinks**. The mission controller decides **what must remain true until the work is actually complete**.

## PRIME / OMEGA / ARC inheritance

- PRIME should use the mission controller for portfolio/shared-runtime work.
- OMEGA should inherit the same mission-state discipline for Factory/ARC oversight.
- Factory-created ARCs should inherit bounded ARC-local mission control from birth.
- ARC-local mission state must not require unrestricted Owner-private content sharing upward.
- portfolio supervision may receive bounded health/state/receipt evidence only.

## Anti-drift rule

A generic persona response, unrelated narrative, conversational closing statement, tool-free completion, or model/provider fallback notice is never valid evidence that an active bounded mission is complete.

When durable acceptance gates remain open, the system must continue, recover, re-route or report a concrete blocker.

## Founder invariant

Founder remains final authority. This lesson improves execution reliability and model portability; it creates no authority above the Founder and changes no ARC ownership or sovereignty rules.
