# E1.11 — VPS Model-Replacement Breakpoint — 2026-09-14

## Proven timeline

The Sep 10–11 VPS PRIME session (`20260910_091337_8075b366`) ran MiniMax M3 primarily through Ollama Cloud and performed the heavy ARC engineering workload successfully.

On Sep 12, PRIME entered a mixed replacement phase. Exact-reply tests on NVIDIA-hosted alternatives were semantically correct but slow: `PRIME_OK` took about 47 seconds and `PRIME_READY` about 157 seconds. The provider usage in that same session shows DeepSeek V4 Pro and Kimi K3 via NVIDIA before MiniMax M3 Cloud resumed later that day.

On Sep 13, NVIDIA Nemotron Super and Ultra exact-response tests were again semantically correct but slow: `PRIME GREEN` took about 66 seconds and `ULTRA GREEN` about 69 seconds. Subsequent execution-heavy `consume` work produced long multi-call tool loops and provider/fallback churn.

On Sep 14, Laguna XS 2.1 proved excellent on tiny direct VPS prompts (5/5, avg 0.46s), but the full PRIME path produced an unwanted `write_file` action and ~91s turn latency. A direct no-tools request with the full current PRIME prompt was rejected by NVIDIA with HTTP 503 ResourceExhausted before model behavior could be evaluated.

## Current diagnosis

The original PRIME/Hermes architecture is not the primary regression source. The same VPS, recursive execution model, large prompt, and autonomy doctrine were already functioning during the MiniMax/Ollama Cloud period.

The strongest surviving fault domain is the replacement intelligence-serving boundary:

1. NVIDIA free hosted endpoints show long-context latency/capacity instability across multiple candidate models.
2. Different replacement models also interpret PRIME's execution-oriented system context differently; Laguna converted a verification-style exact-reply request into a file-write action.
3. These are separate issues: provider capacity/latency and model/tool-choice compatibility.

## Reliable Excellence consequence

Future model qualification for PRIME/ARCs must test the full realistic workload, not just tiny prompts. A production candidate must pass:

- short prompt latency and reliability;
- full PRIME/ARC prompt latency and provider capacity;
- exact instruction adherence;
- correct no-tool vs tool decision;
- recursive multi-step tool execution;
- long-session stability and fallback behavior.

A model is not FAST_INTERACTIVE merely because a tiny direct request is sub-second.
