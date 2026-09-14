# E1.8 Cache Hypothesis Correction — 2026-09-14

Status: evidence checkpoint
Master: M3/16 — Cargo ARC GREEN

## Finding
The current Laguna/NVIDIA session recorded 40,892 input tokens across 2 Laguna calls with cache_read_tokens=0.

However, older working MiniMax/Ollama Cloud sessions from Aug 28 through Sep 3 also recorded cache_read_tokens=0 despite very large input volumes. Large prompt-cache reuse appeared later, especially Sep 10-11, and therefore cannot be the sole reason PRIME previously behaved correctly or responsively.

## Surviving hypotheses
- model/provider tool-call compatibility difference;
- serving-path difference (MiniMax mostly Ollama Cloud vs current Laguna on NVIDIA);
- Hermes runtime/version/configuration change around Sep 12-13;
- context-engine or session-handling change;
- provider handling of long prompts/prefixes.

Decision: fast-gate plugin remains on HOLD. Inspect Hermes runtime/git/config history around the regression window before adding compensating architecture.
