# Hermes Fast-Path Lesson — 2026-09-14

Status: canonical Reliable Excellence evidence
Master: M3/16 — Cargo ARC GREEN

## Proven finding

The PRIME/Laguna forensic trace separated raw model performance from full agent performance.

Direct Laguna test outside Hermes:
- 5/5 exact responses
- average 0.46 s
- max 0.56 s

Inside PRIME/Hermes, the Founder message `PRIME Laguna verification. Reply exactly: PRIME LAGUNA GREEN` entered at 14:57:40 CEST. The model returned a `write_file` tool call at 14:58:57, the tool completed at 14:58:58, and the final assistant response arrived at 14:59:11.

The session used `poolside/laguna-xs-2.1` with no provider fallback. Two Laguna API calls consumed 40,892 input tokens total.

The PRIME system prompt includes strong execution doctrine: PRIME should exhaust autonomous paths, execute Founder decisions, and when asked to build, run, or verify something, produce a working result backed by real tool output. The word `verification` therefore conflicted with the local exact-reply instruction and the model selected `write_file`.

## Architectural conclusion

A fast endpoint can become slow and over-active when every trivial turn receives the full supervisory prompt, tool registry, skills and execution doctrine.

RYZ3N therefore needs a deterministic pre-agent capability gate that selects the smallest sufficient lane before assembling the expensive agent context.

Target lanes:
- SIMPLE / EXACT CHAT: minimal identity/policy, no execution doctrine, no tools unless required, fast interactive model.
- READ / ANALYZE: relevant read-only capabilities only.
- EXECUTE / BUILD / CHANGE: full PRIME/ARC execution doctrine, relevant tools, verification and mission acceptance gates.
- DEEP REASONING: explicit escalation only when warranted.
- MULTIMODAL: perception specialist followed by synthesis lane.

Mandatory invariants:
1. trivial chat must not load the full tool/skill stack;
2. `Reply exactly:` must be treated as a deterministic response constraint;
3. tool availability must be capability-scoped;
4. mission completion remains model-independent and acceptance-gated;
5. benchmarking must distinguish raw endpoint latency from context-prefill, tool-selection, recursive agent and transport latency;
6. the proven control pattern must be inherited by PRIME, Cargo, NARC, VONDA and future ARC Factory templates.

Implementation preference: use native Hermes per-turn/profile/tool selection if available, then plugin/hook/extension, then a thin RYZ3N pre-agent routing layer, and modify Hermes core only if no safe boundary exists.

Reliable Excellence: know-how -> high-quality execution -> verification -> proven reliability -> Reliable Excellence.
