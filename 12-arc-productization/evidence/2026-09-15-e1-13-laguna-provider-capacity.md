# E1.13 — Laguna hosted-provider capacity result — 2026-09-15

## Context
PRIME primary remains `poolside/laguna-xs-2.1` via NVIDIA. The live PRIME config remains intact; local Qwen fallback and Omni vision are configured in their own sections.

## E1.12 full-context result
With the real current PRIME system prompt (~31,640 characters), zero tools, and exact-reply instruction:
- round 1: HTTP 200, 9.45s, exact reply;
- round 2: HTTP 200, 27.95s, exact reply;
- round 3: HTTP 503, 0.69s, `ResourceExhausted: Worker local total request limit reached (32/32)`.

## E1.13 prefix-cache probe
A smaller 16,000-character stable prefix was sent twice, zero tools:
- round 1: HTTP 503, 0.56s;
- round 2: HTTP 503, 0.56s;
- both returned `ResourceExhausted: Worker local total request limit reached (32/32)`.

## Interpretation
The cache probe is inconclusive because both requests were rejected at provider admission before inference. The result is nevertheless decisive for reliability: the free NVIDIA Laguna endpoint is currently subject to worker-level capacity saturation and cannot be accepted as PRIME's sole production-critical path.

Laguna remains a strong candidate for a bounded fast lane because short direct requests previously passed 5/5 at ~0.46s average. But production use requires circuit breaking/fallback and a more reliable primary or alternate serving path.

## Next acceptance direction
Benchmark a known-good VPS-era serving path on the same realistic PRIME workload before designing compensating architecture. Priority candidate: MiniMax M3 through Ollama Cloud, which previously carried the real PRIME/ARC workload on this VPS. Compare exact reply, realistic prompt latency, reliability, cache usage, and then controlled tool execution.

Reliable Excellence rule: endpoint capability is not production reliability; provider admission capacity is part of the system acceptance surface.
