# RYZ3N CORE — TO PRIME

**Status:** CONSUME REQUIRED  
**Authority:** Founder / Lux master engineering bridge  
**Repository:** `Javalin13/ryzen-core`  
**Counterpart:** `FROM_PRIME.md`

## Bridge invariant

A Founder message `consume` or `consume bridge` is an operational bridge command, not an ordinary conversational request.

Canonical direction remains:

`Lux -> TO_PRIME.md -> PRIME executes -> FROM_PRIME.md -> Lux sync`

PRIME must use the established `prime` Git context, fetch current `origin/main`, read this file, execute only the bounded directive, update `FROM_PRIME.md`, commit/push durable evidence, then send Founder only the MINI REPORT.

Do not use the Founder as copy/paste transport. Do not treat `FROM_PRIME.md` as the input directive. Never destroy local work to make a pull succeed.

## Master position

**MASTER: M3/16 — CARGO ARC GREEN**

The 16-step master is unchanged. Current work remains the reusable PRIME reliability/cognition substrate required before Cargo parity.

## Architecture correction — 2026-09-17

Founder direction now explicitly rejects solving current PRIME cognition defects by accumulating more channel-specific hardcoding.

Read and inherit:

- `12-arc-productization/RYZ3N-COGNITIVE-CONNECTION-LAYER-AND-OWNER-SOVEREIGNTY-RUNTIME-DIRECTION-2026-09-17.md`
- `02-ryzen/future-reliability-capabilities/OWNER-SOVEREIGNTY-COGNITIVE-CONNECTION-SKILL-REGISTRY-ADDENDUM-2026-09-17.md`

Key invariant:

> RYZ3N owns cognition architecture. Models, providers, agent runtimes, tools and channels remain replaceable substrates.

MiniMax is **not** selected as PRIME's permanent model. The architectural lesson being adopted is model-independent proportional/interleaved reasoning: intent -> reasoning budget -> tool/no-tool -> act -> observe -> verify -> stop, with private cognition structurally separated from public Owner output.

Owner sovereignty must remain human and non-simulatable. Owner-aware cognition may model relevant identity, intent, working style, priorities and decision patterns only as bounded evidence-based context; inference is never authority and explicit current Owner direction always wins.

## CURRENT: E1.23A — non-destructive cognition/control mutation audit

### Objective

Before another behavioral patch is introduced, establish exactly what custom PRIME/Hermes modifications exist and whether any cognition/control hardcoding can plausibly contribute to:

- `/think*` or hidden-control leakage;
- unsolicited text-to-speech or other tool calls;
- failure to obey exact/direct requests;
- excessive verbosity/expansion;
- brittle `consume` semantics;
- recursion/fallback amplification.

### Round A — source truth / working-tree audit

Inspect only. Do not mutate runtime behavior in this round.

1. Inspect `/home/prime/hermes-agent` tracked modifications, untracked files and detached-HEAD state.
2. Inspect `/home/prime/ryzen-core` local changes versus `origin/main` without destructive reset/clean/checkout.
3. Classify every relevant deviation into:
   - `TRANSPORT/NETWORKING`
   - `TELEMETRY/MEASUREMENT`
   - `COGNITION/CONTROL`
   - `UNKNOWN`
4. Preserve the known Telegram hostname-first networking repair.
5. Preserve deployed v0.1.6 Cache Controller/instrumentation evidence.
6. Identify any custom code/prompt/runtime change that affects reasoning controls, tool selection, message interpretation, exact-output handling or visible response shaping.
7. Do not patch `consume` into the Telegram adapter during this audit.
8. Do not redesign router, Omega, Factory, NARC, VONDA or Cargo.

### Round B — locate the smallest generic RYZ3N cognition seam

After the audit, identify but do not yet overbuild the smallest provider/channel-independent seam capable of owning:

- authenticated control intent (`consume` class commands);
- direct-vs-reasoning classification;
- reasoning budget selection;
- no-tool/tool discipline;
- private working state vs public output separation;
- bounded action/observation loops;
- final instruction/intent verification.

Prefer an existing generic hook/extension seam over Hermes core mutation. If no adequate seam exists, report that truth before implementing a new one.

## Acceptance for E1.23A

This round is GREEN only when the report contains:

- complete relevant local deviation inventory;
- exact paths/functions for cognition/control modifications;
- evidence-backed classification of likely/non-likely contributors to current PRIME defects;
- confirmation that Telegram networking repair and Cache Controller evidence remain preserved;
- proposed smallest generic RYZ3N Cognitive Connection seam;
- explicit rollback/isolation boundaries;
- no unapproved Cargo/NARC/VONDA mutation.

No production cognition fix is authorized until Lux reviews this audit.

## Subsequent sequence

```text
E1.23A audit accumulated PRIME/Hermes cognition/control modifications
  -> E1.23B define/prove smallest RYZ3N Cognitive Connection seam
  -> E1.23C restore fast + correct PRIME behavior through that seam
  -> E1.24 verified context reduction / pressure reduction
  -> E1.25 bounded health-aware fallback / circuit behavior
  -> PRIME GREEN acceptance
  -> E2 Cargo parity/proof
  -> E3 reusable NARC/VONDA migration template
  -> E4 deterministic mission/control acceptance invariant
  -> E5 broader bounded authority restoration
  -> M3 Cargo GREEN durable receipt
```

## Safety / isolation

- No destructive `git reset --hard`, `git clean`, forced checkout or overwrite of uncommitted work.
- Use the established `prime` user Git path; do not add GitHub credentials to root.
- Do not restart or mutate Cargo for this audit.
- Do not mutate NARC or VONDA.
- Preserve ARC identity, memory, aura, maturity, Owner boundaries, business logic and bridges.
- No paid capacity/provider commitment changes without Founder authorization.

## Reporting

Replace repository-root `FROM_PRIME.md` with detailed evidence and push it to `ryzen-core`.

Founder receives only:

```text
STATUS: <GREEN/AMBER/RED + one-line result>
CHANGED: <one or two key facts>
NEXT: <next bounded action or NONE>
TIME: <elapsed> | ETA: <estimate>
LUX: SYNC NEEDED | NO SYNC NEEDED
BRIDGE: <ryzen-core pushed short SHA>
```

Detailed terminal output belongs in the GitHub report, not Founder chat.
