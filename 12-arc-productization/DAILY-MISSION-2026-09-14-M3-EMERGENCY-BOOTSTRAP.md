# Daily Mission — 2026-09-14 — M3 Emergency Bootstrap

**Status:** ACTIVE  
**Master:** M3/16 — Cargo ARC GREEN  
**Mission mode:** external stabilization first, then restore delegated execution  
**Founder:** final authority  
**Lux:** architecture / control / acceptance supervisor

## Mission objective

Complete the current PRIME/Cargo stabilization without repeating the bootstrap paradox exposed on 2026-09-13.

The current problem is not the broad RYZ3N architecture, Hetzner networking, Telegram credentials, NVIDIA credentials, or ARC identity. The active defect is the control/intelligence boundary after the model replacement.

## Emergency engineering principle

> **Do not ask an unstable PRIME to bootstrap the control plane that makes PRIME stable.**

Until the minimum stable control surface is restored, Lux + GitHub source truth temporarily act as the repair controller. PRIME resumes delegated engineering only after real runtime acceptance proves it is stable enough to carry the load again.

## M3 merged emergency sequence

```text
M3 — Cargo ARC GREEN
  E0 — externally stabilize PRIME
  E0.5 — free-model reliability gate
  E1 — prove PRIME fast interactive execution
  E2 — apply/prove Cargo parity
  E3 — prepare reusable NARC/VONDA migration template from the proven stack
  E4 — install minimum deterministic mission guard / acceptance invariant
  E5 — return bounded execution authority to PRIME
  M3 acceptance — Cargo GREEN receipt + durable source alignment
```

## Current capability target after evidence

```text
FAST_INTERACTIVE  -> poolside/laguna-xs-2.1 (direct endpoint proven)
DEEP_REASONING    -> Nemotron Ultra only when explicitly warranted + healthy
MULTIMODAL        -> Nemotron Omni perception -> fast/deep synthesis lane
BACKGROUND_LIGHT  -> local Qwen when safe
BACKGROUND_NORMAL -> fast interactive lane
EMERGENCY_LOCAL   -> local Qwen restricted continuity
```

## Proven live evidence — 2026-09-14

- ~14:19 CEST — Founder resumed operator-access recovery from Windows PowerShell.
- ~14:29 CEST — GitHub-authenticated Tailscale SSH path restored to `prime-vps-01`; live tailnet IP verified as `100.83.143.22`.
- 14:31:01 CEST — E0.1 backup + exact PRIME routing snapshot started; backup `config.yaml.e0-20260914-143101.bak` created.
- E0.1 proved: Ultra primary, Super automatic fallback, local Qwen emergency fallback, Omni vision, gateway active.
- E0.2 changed only PRIME ordinary primary Ultra -> Super; YAML remained valid; gateway restarted active.
- E0.3 removed redundant automatic Super fallback while preserving local Qwen; Omni unchanged; gateway restarted active.
- 14:35:23 CEST — E0 timing checkpoint; E0 configuration execution measured at **4m22s**.
- ~14:37 CEST — first E1 exact-response test on Super path started.
- ~14:40 CEST — PRIME unexpectedly executed a `write_file` action instead of simply replying.
- ~14:42 CEST — Super live provider path failed and PRIME fell back to local Qwen.
- 14:43:14 CEST — E1.1 failed checkpoint; visible wall-clock approximately 5 minutes.

### Free-model reliability gate

Nemotron 3.5 Lightning:
- 1/5 successful direct requests;
- first success 4.93s;
- four consecutive ~20s ReadTimeouts;
- avg 17.06s;
- verdict: **REJECTED** for FAST_INTERACTIVE.

Poolside Laguna XS 2.1:
- 5/5 HTTP 200;
- 5/5 exact instruction following;
- timings: 0.56s, 0.43s, 0.45s, 0.43s, 0.44s;
- avg **0.46s**;
- max **0.56s**;
- zero timeouts / 429 / 5xx;
- verdict: **DIRECT ENDPOINT GREEN**.

### E0.6 integration

PRIME was changed to:

```text
PRIMARY            -> poolside/laguna-xs-2.1
PROVIDER           -> nvidia
AUTOMATIC FALLBACK -> local qwen3:0.6b only
VISION             -> nvidia/nemotron-3-nano-omni-30b-a3b-reasoning
GATEWAY            -> active
```

YAML validated and controlled gateway restart completed.

### E1 Laguna Hermes proof — decisive split

- 14:57:40 CEST — Founder message entered the persisted Telegram session: `PRIME Laguna verification. Reply exactly: PRIME LAGUNA GREEN`.
- 14:58:57 CEST — Laguna returned a `write_file` tool call targeting `~/.prime/laguna/verification.txt`.
- 14:58:58 CEST — `write_file` completed successfully.
- 14:59:11 CEST — final assistant response returned narrative verification text rather than the exact requested reply.
- Session forensic evidence: model `poolside/laguna-xs-2.1`, provider `nvidia`, provider fallback inactive, 2 Laguna API calls, 40,892 total input tokens across the recorded model-usage entry.

### E1.3 root-cause proof

The persisted PRIME system prompt contains strong execution doctrine, including obligations to exhaust autonomous paths, execute Founder decisions, and produce a working artifact backed by real tool output when asked to build, run, or verify something.

The Founder test contained the word `verification`. Laguna therefore followed the higher-priority execution doctrine and selected `write_file` rather than honoring the local exact-reply constraint as a pure conversational turn.

This proves two distinct defects in the full PRIME path:

1. **capability-selection defect** — trivial/simple chat receives an execution-oriented system prompt and broad tool machinery;
2. **context-cost defect** — a sub-second direct model call becomes a long turn because PRIME sends a very large supervisory context and may require multiple model/tool rounds.

### E1.4 fast-gate implementation snapshot

At 15:17:14 CEST the live PRIME config showed:

```text
plugins               -> null
configured toolsets   -> ["hermes-cli"]
custom_toolsets       -> null
hooks                 -> null
agent.tool_use_enforcement -> auto
agent.execution_guidance   -> null
existing PRIME plugin files -> none
```

Interpretation: there is no existing custom plugin layer to unwind. The clean implementation boundary remains a small versioned RYZ3N pre-agent fast gate / supported Hermes hook or equivalent extension, not a Hermes-core fork.

## Current acceptance ledger

- [x] E0 PRIME configuration backed up
- [x] E0 PRIME bootstrap routing applied
- [x] E0.5 fast free-model candidate found: Laguna direct 5/5, avg 0.46s
- [ ] E1 PRIME simple-response proof — FAILED through full Hermes path despite direct Laguna GREEN
- [ ] E1 PRIME structured-response proof
- [x] E1 root cause isolated to PRIME/Hermes capability/context path
- [x] E1 plugin/toolset implementation surface inspected
- [x] Hermes tool execution observed — but unrequested, therefore drift evidence rather than acceptance
- [x] E1 failed-attempt timing captured
- [ ] E1 deterministic fast gate implemented/proven
- [ ] E2 Cargo parity applied
- [ ] E2 Cargo real-message proof
- [ ] E2 Cargo latency recorded
- [ ] E3 reusable ARC migration template updated
- [ ] E4 minimum mission guard implemented/proven
- [ ] E5 PRIME bounded delegated execution restored
- [ ] M3 Cargo GREEN durable receipt accepted

## Immediate next diagnostic / implementation gate

Before writing the RYZ3N fast-gate plugin, inspect the installed Hermes source for the exact supported pre-dispatch hook/plugin contract and one real plugin example. Do not guess hook signatures and do not modify Hermes core.

Target behavior after implementation:

```text
Founder message
  -> deterministic RYZ3N pre-agent classifier
     -> SIMPLE / EXACT CHAT: minimal identity/policy, Laguna, no execution tools/full doctrine
     -> READ / ANALYZE: read-only relevant capabilities
     -> EXECUTE / BUILD / CHANGE: full PRIME recursive agent + relevant tools + acceptance guard
     -> DEEP / MULTIMODAL: explicit capability escalation
```

Do not reopen networking, credentials or model selection without contradictory new evidence.

## Reliable Excellence rule

A candidate model is not production GREEN because a direct API call is fast. Production GREEN requires the full system path to preserve:

**correct intent -> smallest sufficient capability lane -> correct tool/no-tool choice -> bounded recursion -> fast completion -> durable acceptance evidence.**

## Related canonical source

- `MODEL-INDEPENDENT-MISSION-CONTROL-LESSON-2026-09-13.md`
- `HERMES-FAST-PATH-LESSON-2026-09-14.md`
- repository-root `TO_PRIME.md` / `FROM_PRIME.md`
- current M1→M16 master remains authoritative.
