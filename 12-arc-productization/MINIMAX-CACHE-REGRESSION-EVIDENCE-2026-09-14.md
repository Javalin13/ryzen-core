# MiniMax Cache/Provider Regression Evidence — 2026-09-14

Status: active E1 Reliable Excellence evidence
Master: M3/16 — Cargo ARC GREEN

## Proven observation

Inspection of the old working MiniMax session shows that although `sessions.model_config` recorded a NVIDIA gateway runtime with fallback active, the actual persisted `session_model_usage` for `minimax-m3` was through `ollama-cloud` (`https://ollama.com/v1`).

The same historical session accumulated very large prompt-cache reuse, including a record with `cache_read_tokens = 261338753`, plus additional cache-read totals in other MiniMax usage rows.

The current Laguna path is different: persisted runtime evidence shows NVIDIA as the active provider and the bad Laguna turn required two model calls with 40,892 total input tokens.

## Interpretation

The old working PRIME was not merely 'MiniMax with the same runtime'. It was effectively benefiting from an Ollama Cloud serving path with extensive prefix/prompt-cache reuse. The recent replacement changed both model and serving/provider behavior.

This is now the leading explanation for why PRIME could carry a ~35k-character supervisory prompt during the MiniMax era without feeling as slow, while the current NVIDIA/Laguna path becomes expensive on each recursive call.

The prompt-composition hypothesis was also narrowed: the old MiniMax prompt already contained the current autonomy doctrine and an even stricter Execution Discipline/tool-persistence block. Therefore recent autonomy wording is not supported as the primary regression trigger.

## Next acceptance check

Before adding a compensating fast-gate plugin, compare current Laguna session cache accounting and provider behavior directly against the historical MiniMax/Ollama Cloud path. Determine whether NVIDIA long-prefix prefill / cache handling is the dominant latency regression and whether a free serving path with equivalent cache reuse exists.

Reliable Excellence rule: compare full serving path, not just model name.