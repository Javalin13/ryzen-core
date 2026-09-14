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

Current Hermes documentation independently confirms that its default `tool_use_enforcement: auto` model-family list does not include Poolside/Laguna, so this incident should not be attributed to automatic Hermes tool-use enforcement for the selected model family.

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

## Supported Hermes implementation boundary

Current Hermes documentation provides native extension surfaces that match this architecture without requiring a core fork:

1. Toolsets are the native mechanism for controlling tool availability per platform, session or task. The `file` toolset contains `write_file`, `patch`, `read_file` and `search_files`.
2. `pre_gateway_dispatch` is a directive/control plugin hook that runs on incoming gateway messages before normal agent dispatch. It can `allow`, `rewrite`, or `skip` an inbound turn.
3. A RYZ3N plugin can therefore recognize a deterministic SIMPLE/EXACT fast-path, call the proven fast model with a compact PRIME/ARC identity prompt, deliver the result directly, and return `skip` so the full agent/tool/skill context is never assembled.
4. Non-fast-path requests fall through to ordinary Hermes dispatch, where execution doctrine and relevant capabilities remain available.
5. A later capability router can combine this with narrowed toolsets for READ/ANALYZE and EXECUTE lanes.

Preferred hierarchy:
- native Hermes toolsets and profile capability controls;
- thin versioned RYZ3N plugin using `pre_gateway_dispatch` for deterministic fast-path routing;
- plugin hooks/guardrails for tool policy and metrics;
- Hermes-core modification only if a required capability cannot be achieved through supported extension surfaces.

This avoids rebuilding Hermes, preserves upstream updateability, and makes the routing logic a reusable ARC Factory inheritance layer.

Reliable Excellence: know-how -> high-quality execution -> verification -> proven reliability -> Reliable Excellence.
