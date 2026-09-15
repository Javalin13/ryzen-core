# E1.15 — MiniMax/Ollama Cloud full PRIME exactness GREEN

Date: 2026-09-15
Checkpoint: 13:30 CEST
Master: M3/16 — Cargo ARC GREEN

## Test

Direct API call from `prime-vps-01` to Ollama Cloud using model `minimax-m3:cloud`.

- Real current PRIME system prompt: 31,640 characters / 7,524 prompt tokens
- Tools sent: 0
- Output budget: 256 tokens
- Expected exact reply: `PRIME MINIMAX GREEN`

## Results

Round 1:
- HTTP 200
- latency 5.97s
- finish_reason `stop`
- exact reply PASS
- visible text `PRIME MINIMAX GREEN`
- reasoning field present, 585 chars
- no tool calls
- prompt tokens 7,524
- cached tokens 7,296
- completion tokens 137

Round 2:
- HTTP 200
- latency 1.90s
- finish_reason `stop`
- exact reply PASS
- visible text `PRIME MINIMAX GREEN`
- reasoning field present, 99 chars
- no tool calls
- prompt tokens 7,524
- cached tokens 7,523
- completion tokens 32

## Verdict

`minimax-m3:cloud` over Ollama Cloud is the current leading PRIME primary candidate.

It passed the realistic PRIME-sized context gate for:
- availability;
- exact instruction following;
- bounded reasoning;
- no unwanted tool calls when tools are absent;
- provider-side prefix cache reuse;
- practical latency after warm cache.

The next mandatory gate is full Hermes/PRIME execution with normal tools available. Production primary should not be changed permanently until that test passes.

## Comparison

Laguna XS 2.1 on NVIDIA remains an excellent short-prompt candidate but the free NVIDIA serving path showed repeated `503 ResourceExhausted` admission failures under realistic context load. MiniMax/Ollama therefore currently leads for PRIME-sized production work.
