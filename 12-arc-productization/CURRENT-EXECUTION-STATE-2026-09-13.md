# RYZ3N Current Execution State — live pointer

Status: **ACTIVE LIVE POINTER**  
Last aligned: **2026-09-14**

This file is the compact current-state pointer for the detailed M1→M16 execution crosswalk and the broader post-mission roadmap.

## Master position

- M1 Core/source truth — DONE
- M2 PRIME GREEN — **DONE / CLOSED historically**
- M3 Cargo ARC GREEN — **CURRENT**
- M4 NARC GREEN — pending M3
- M5 VONDA GREEN — pending M4
- M6 onward — unchanged from the detailed master crosswalk

## Current M3 reality

PRIME and Cargo have both proven real end-to-end operation in the NVIDIA-era runtime, but the model replacement exposed a control-plane weakness that prevents us from calling the new architecture production-stable yet.

Key evidence:

- NVIDIA Ultra, Super and Omni direct hosted checks have all been GREEN at least once.
- Real Founder -> PRIME -> Founder Telegram path has worked.
- Real Founder -> Cargo -> Founder Telegram path has worked.
- Cargo direct benchmark: Ultra returned HTTP 503 after ~56.96 s while Super returned HTTP 200 in ~0.68 s.
- Cargo runtime logs showed real Ultra provider overload and retry delay before the final response.
- PRIME sessions later exhibited provider stalls, persona drift and tool-free false completion after the model replacement.
- `FROM_PRIME.md` remained awaiting a valid Phase-A report, proving that conversational completion did not equal mission completion.

The active defect is therefore **model/control-plane integration**, not broad VPS/Telegram/NVIDIA credential failure.

## 2026-09-14 emergency path merged inside M3

The emergency bootstrap is not a new roadmap. It is the implementation sequence inside the current M3 mission:

```text
M3 — Cargo ARC GREEN
  E0 — externally stabilize PRIME
  E1 — prove PRIME fast interactive execution
  E2 — apply/prove Cargo parity
  E3 — prepare reusable NARC/VONDA migration template
  E4 — minimum deterministic mission guard / acceptance invariant
  E5 — return bounded execution authority to PRIME
  M3 acceptance — Cargo GREEN receipt + durable source alignment
```

### E0 — CURRENT

Lux + GitHub source truth temporarily act as the repair controller so we do not ask unstable PRIME to bootstrap the control plane that makes PRIME stable.

Bootstrap routing target:

```text
FAST_INTERACTIVE  -> Nemotron Super
DEEP_REASONING    -> Nemotron Ultra only when warranted + healthy
MULTIMODAL        -> Nemotron Omni perception -> Super/Ultra synthesis
BACKGROUND_LIGHT  -> local Qwen when safe
BACKGROUND_NORMAL -> Super
EMERGENCY_LOCAL   -> local Qwen restricted continuity
```

During E0/E1, ordinary PRIME execution should use Super rather than waiting on Ultra by default. Ultra remains available for later selective deep-reasoning routing.

## E0→E5 acceptance summary

- E0: back up and externally stabilize PRIME routing.
- E1: prove simple reply, structured reply and one real tool/action path; record latency.
- E2: apply only the proven template to Cargo and prove real direct operation/latency.
- E3: encode the proven template for NARC/VONDA/Factory inheritance.
- E4: implement the minimum model-independent mission guard so `consume` cannot close without objective gates + durable receipt.
- E5: return bounded execution authority to PRIME and resume bridge-driven delegated engineering.

Full daily implementation plan: `12-arc-productization/DAILY-MISSION-2026-09-14-M3-EMERGENCY-BOOTSTRAP.md`.

## Protected invariants

- Founder is Founder, never Owner.
- PRIME remains supervisory.
- ARC Owners communicate directly with their ARCs.
- Narek remains NARC Owner; Founder/test identities never consume the Owner slot.
- ARC identity, aura, maturity, memory, source boundary, business logic and sovereignty are not changed by the model replacement.
- settled Hetzner IPv6/DNS64/NAT64 conclusions remain closed unless contradictory new evidence appears.
- existing proven Telegram fallback-IP invariant stays preserved.
- no raw secrets/tokens committed or exposed.

## Timing discipline

Target technical completion for the emergency bootstrap + M3 closure path: **~60–90 minutes if no genuinely new external blocker appears.**

Track actual elapsed time, provider latency, false-completion events, restarts/resets, Founder intervention count, and wasted/repeated diagnostic time. Keep `ryzen-core`, relevant ARC bridges and private `JohnDough` performance evidence aligned at meaningful state transitions.
