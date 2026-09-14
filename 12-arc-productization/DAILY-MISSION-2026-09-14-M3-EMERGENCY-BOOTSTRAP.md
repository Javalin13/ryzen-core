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

### E1.4 implementation surface

The live PRIME config showed no custom plugin/hook layer, `toolsets=["hermes-cli"]`, `tool_use_enforcement=auto`, and no custom execution guidance. Installed Hermes source confirms a supported `pre_gateway_dispatch` extension surface exists, but implementation is intentionally on HOLD pending regression archaeology.

### E1.5 PRIME regression timeline — new breakpoint

At ~15:22 CEST the persisted session timeline showed that PRIME's system prompt did **not** become larger after the old MiniMax era:

- 2026-08-28 through 2026-09-10 MiniMax sessions: roughly **35.3k–35.6k prompt characters**;
- 2026-09-12/early 2026-09-13 Qwen sessions: roughly **35.65k characters**;
- **2026-09-13 09:49** Ultra session: prompt abruptly dropped to **31,819 characters**;
- later 2026-09-13/14 sessions: roughly **31.6k characters**;
- current Laguna session: **31,640 characters**.

This rules out simple prompt-size growth as the regression. A structural prompt-composition change occurred around **2026-09-13 09:49 CEST**. The prompt became smaller, yet behavior became more execution-heavy. Current hypothesis: an older block was removed/replaced while autonomy/execution doctrine gained stronger relative influence or scope. The doctrine may have originated from Lux/Founder/PRIME efforts to stop the Founder acting as terminal relay; attribution is not yet proven.

**Decision:** do not build the fast-gate workaround yet. First compare the last working MiniMax prompt to the current Laguna prompt and identify the exact content change at source.

## Current acceptance ledger

- [x] E0 PRIME configuration backed up
- [x] E0 PRIME bootstrap routing applied
- [x] E0.5 fast free-model candidate found: Laguna direct 5/5, avg 0.46s
- [ ] E1 PRIME simple-response proof — FAILED through full Hermes path despite direct Laguna GREEN
- [ ] E1 PRIME structured-response proof
- [x] E1 root cause isolated to PRIME/Hermes capability/context path
- [x] E1 plugin/toolset implementation surface inspected
- [x] E1 prompt-regression breakpoint identified around 2026-09-13 09:49
- [ ] E1 old-vs-current prompt composition diff completed
- [ ] E1 deterministic fast gate implemented/proven — HOLD until prompt regression is understood
- [ ] E2 Cargo parity applied
- [ ] E2 Cargo real-message proof
- [ ] E2 Cargo latency recorded
- [ ] E3 reusable ARC migration template updated
- [ ] E4 minimum mission guard implemented/proven
- [ ] E5 PRIME bounded delegated execution restored
- [ ] M3 Cargo GREEN durable receipt accepted

## Immediate next diagnostic

Compare the last working MiniMax system prompt against the current Laguna system prompt from `state.db`. Determine which custom PRIME doctrine, skills, memories, or runtime prompt blocks were added, removed, or replaced around the 2026-09-13 breakpoint.

Do not reopen networking, credentials or model selection without contradictory new evidence. Do not implement the fast-gate plugin until the regression source is understood.

## Reliable Excellence rule

A candidate model is not production GREEN because a direct API call is fast. Production GREEN requires the full system path to preserve:

**correct intent -> smallest sufficient capability lane -> correct tool/no-tool choice -> bounded recursion -> fast completion -> durable acceptance evidence.**

And regression fixes must repair the source defect before layering compensating architecture on top.

## Related canonical source

- `MODEL-INDEPENDENT-MISSION-CONTROL-LESSON-2026-09-13.md`
- `HERMES-FAST-PATH-LESSON-2026-09-14.md`
- repository-root `TO_PRIME.md` / `FROM_PRIME.md`
- current M1→M16 master remains authoritative.
