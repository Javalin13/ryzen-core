# E0.1 PRIME Bootstrap Snapshot — 2026-09-14

**Master:** M3/16 — Cargo ARC GREEN
**Stage:** E0.1 — external PRIME stabilization snapshot
**Status:** GREEN / snapshot complete
**Observed:** ~14:31 CEST

## Runtime evidence

- PRIME config backup created on VPS: `/home/prime/.hermes/config.yaml.e0-20260914-143101.bak`
- Current primary model: `nvidia/nemotron-3-ultra-550b-a55b`
- Current provider: `nvidia`
- Current NVIDIA base URL: `https://integrate.api.nvidia.com/v1`
- Fallback 1: `nvidia/nemotron-3-super-120b-a12b`
- Fallback 2: local Ollama `qwen3:0.6b` at `http://127.0.0.1:11434/v1`
- Vision specialist: `nvidia/nemotron-3-nano-omni-30b-a3b-reasoning`
- Gateway: `active`

## Interpretation

The live runtime still has Ultra as ordinary primary, exactly matching the known source of long interactive stalls and provider-overload retries. Super, Omni and local Qwen are already present, so the lowest-risk bootstrap change is a reversible primary-lane swap from Ultra to Super without touching Omni, local continuity, identities, Owner bindings, ARC sovereignty, Telegram networking, bridges, memory, aura or Hermes core.

## Next gate

E0.2 — change only the PRIME ordinary primary model from Ultra to Super, validate YAML, restart the gateway once, then immediately run E1 functional proof.

Rollback is the timestamped backup above.
