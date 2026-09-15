# RYZ3N CORE — TO PRIME

**Status:** CONSUME REQUIRED  
**Authority:** Founder / Lux master engineering bridge  
**Repository:** `Javalin13/ryzen-core`  
**Counterpart:** `FROM_PRIME.md`

## Master position

**MASTER: M3/16 — CARGO ARC GREEN**

PRIME is returned to **bounded engineering execution authority** after the 2026-09-15 external performance bootstrap restored responsive interactive operation and established the RYZ3N Cache Controller / performance measurement foundation.

This is NOT a declaration that PRIME performance is fully GREEN. Current remaining defects are specific and must now be closed under Reliable Excellence.

## Current execution line

**E1.23 — PRIME fast-interactive correctness + tool-discipline closure**

Observed current state at handoff:

- PRIME is responsive again and can answer quickly enough for interactive work.
- Direct Laguna endpoint capability was previously proven at ~0.46 s average for tiny exact prompts.
- Best real PRIME Laguna request observed during the bootstrap was ~4.75 s.
- PRIME request pressure has been measured at roughly ~20k provider input tokens on trivial requests.
- ~98% repeated/stable request-character opportunity was measured on a representative live request while provider-reported cache reuse remained effectively zero.
- RYZ3N Cache Controller evolved through v0.1.6 shadow instrumentation, provider-independent and content-free.
- Fresh-build and restored Telegram-session prompt paths were traced to the common `_restore_or_build_system_prompt()` -> `agent._cached_system_prompt` -> `turn_context.py` convergence.
- PRIME and Cargo process isolation remained preserved throughout PRIME-only restarts.
- Telegram hostname-first repair must remain byte-preserved unless a separately authorized networking mission requires change.

Current visible failures still to close:

1. trivial requests may incorrectly trigger tools (including text-to-speech / config reads);
2. `/think*` or reasoning-control leakage can appear in Founder-facing output;
3. responses are often far more verbose than requested;
4. Laguna provider failures can fall back to local Qwen, which has shown ~77–115 s latency and is not acceptable as an interactive normal-path fallback;
5. exact-reply / simple-response instruction following is not yet consistently correct;
6. local v0.1.6 source changes on the VPS may be ahead of remote `ryzen-core`; source truth must be reconciled safely before any pull/overwrite that could lose them.

## ROUND A — mandatory source reconciliation first

Before implementation work:

1. Inspect `/home/prime/ryzen-core` working tree and `origin/main` without destructive reset/clean/checkout.
2. Preserve the currently deployed/local v0.1.6 Cache Controller and Hermes instrumentation evidence.
3. Reconcile the local v0.1.6 RYZ3N-owned source changes into `Javalin13/ryzen-core` so remote `main` becomes durable source truth.
4. Do not overwrite or discard local uncommitted work.
5. Do not add GitHub credentials to root; use the established `prime` user Git path.
6. Preserve the Hermes Telegram modification and its existing backup/artifact state.

If a source conflict exists, stop the conflicting write and report it; do not guess.

## ROUND B — inspect and close fast-interactive correctness

Primary objective:

> A trivial Founder message must receive a direct, semantically correct, concise response with NO unnecessary tool call, NO `/think*` leakage, bounded execution, and interactive latency when the fast provider is healthy.

Inspect the smallest relevant surfaces for:

- no-tool / tool-selection policy for trivial conversational and exact-response requests;
- why `text_to_speech` was invoked without Founder request;
- why `/think*` leaks into visible output;
- why exact/simple requests are over-expanded;
- whether retry/fallback policy can turn a small request into long local-Qwen execution;
- v0.1.6 live measurement availability at the common prompt convergence seam.

Do not redesign the router, dashboard, ARC Factory, Skills Registry, Omega, or research brains during this round.

## Acceptance sequence

After the smallest reversible fix is implemented, prove THREE real PRIME Telegram tests:

### Test 1 — exact output
Founder prompt:
`Reply exactly: PRIME FAST CORRECT`

Acceptance:
- visible answer exactly `PRIME FAST CORRECT`;
- no tool call;
- no `/think*` or hidden-control leakage;
- no explanatory suffix/prefix;
- record latency and provider/fallback path.

### Test 2 — ordinary conversational response
Founder asks a simple non-tool question such as:
`Are you fully operational?`

Acceptance:
- concise direct answer;
- no unsolicited tool execution;
- no fabricated operational claims beyond known runtime state;
- no `/think*` leakage;
- record latency and provider/fallback path.

### Test 3 — legitimate tool path
Use one small, explicit tool-requiring task chosen by PRIME that cannot be answered correctly without the tool.

Acceptance:
- correct tool selected once;
- bounded execution;
- useful result;
- no recursion drift;
- record latency.

## Performance target and truthfulness

Do not declare performance GREEN merely because one reply is visually fast.

GREEN requires:

**correct intent -> smallest sufficient capability lane -> correct tool/no-tool choice -> bounded recursion -> fast completion -> durable evidence**

Provider outages are external and may prevent a strict universal latency guarantee, but PRIME must not magnify a transient provider failure into avoidable multi-minute behavior for trivial requests.

## Fallback boundary

Local Qwen remains emergency continuity only and is temporary. Do not promote Ollama/Qwen/MiniMax into the permanent RYZ3N backbone. The project target remains provider/model independent.

Do not purchase capacity, add paid subscriptions, or change provider commercial commitments without Founder authorization.

## Cargo / ARC isolation

- Do not restart or mutate Cargo during PRIME-only E1.23 work unless a later directive explicitly authorizes Cargo parity.
- Do not mutate NARC or VONDA.
- Preserve ARC identity, memory, aura, maturity, Owner boundaries, business logic, and bridges.
- Founder remains Founder / Commander-in-Chief, never ARC Owner.

## Reporting and bridge contract

Use repository-root `FROM_PRIME.md` for the detailed report.

Required sequence:

1. consume this directive;
2. perform Round A source reconciliation;
3. perform the bounded E1.23 inspection/fix/test sequence;
4. update `FROM_PRIME.md` with detailed evidence;
5. commit/push all durable RYZ3N source/evidence to `ryzen-core`;
6. send Founder only the MINI REPORT.

Founder MINI REPORT format:

```text
STATUS: <GREEN/AMBER/RED + one-line result>
CHANGED: <one or two key facts>
NEXT: <next bounded action or NONE>
TIME: <elapsed> | ETA: <estimate>
LUX: SYNC NEEDED | NO SYNC NEEDED
BRIDGE: <ryzen-core pushed short SHA>
```

Do not dump terminal logs, raw prompts, secrets, tokens, API keys, private Owner conversations, or large diagnostics into Founder chat.

## Tomorrow/continuation handoff alignment

The detailed daily bulletin is recorded in `12-arc-productization/DAILY-BULLETIN-2026-09-15-M3-PERFORMANCE.md` and is the canonical day-resume overview.

Current macro sequence after E1.23:

```text
E1.23 PRIME fast-interactive correctness/tool discipline
  -> E1.24 verified context reduction / pressure reduction
  -> E1.25 bounded health-aware fallback / circuit behavior
  -> PRIME GREEN acceptance
  -> E2 Cargo parity/proof
  -> E3 reusable NARC/VONDA migration template
  -> E4 deterministic mission guard / acceptance invariant
  -> E5 broader bounded authority restoration
  -> M3 Cargo GREEN durable receipt
```

Remain inside this sequence unless Lux/Founder explicitly changes it.
