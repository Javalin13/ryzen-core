# E1.6 Prompt Diff Result — 2026-09-14

Status: canonical regression evidence
Master: M3/16 — Cargo ARC GREEN
Checkpoint: 15:28:09 CEST

## Result

The hypothesis that recent PRIME autonomy doctrine caused the new tool-heavy behavior is falsified by state.db prompt comparison.

Last working MiniMax prompt:
- model: minimaxai/minimax-m3
- chars: 35,558

Current Laguna prompt:
- model: poolside/laguna-xs-2.1
- chars: 31,640
- delta: -3,918 chars

The following doctrine already existed in both old and new prompts:
- Commander-in-Chief / terminal-operator boundary
- exhaust reasonable autonomous execution paths
- Founder-decision execution rules
- use every autonomous path
- execution-mode transition
- no re-litigation after final decision
- build/run/verify -> real execution/result expectations

The old MiniMax prompt was actually MORE tool-aggressive because it still included the removed `# Execution discipline` block with tool persistence, mandatory tool use, repeated-tool completion/verification rules, and external-state verification.

Therefore recent autonomy doctrine is not the source regression.

## New active hypothesis class

The regression is more likely in a runtime/model compatibility layer changed around the model replacement period:
- model/provider behavior under the same supervisory prompt;
- API mode / tool-call implementation;
- Hermes runtime/version or tool-schema behavior;
- session/context-engine composition beyond the plain system prompt;
- prompt caching / provider-side prefix handling;
- model-specific interpretation of tool availability and exact-response constraints.

## Decision

Fast-gate plugin remains on HOLD until the old working MiniMax behavior is compared directly against current runtime behavior. Do not compensate for a regression before isolating its actual source.

Reliable Excellence rule: falsified hypotheses must be recorded and removed from the active causal model rather than defended.