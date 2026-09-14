# E0 Access Recovery Checkpoint — 2026-09-14

**Master:** M3/16 — Cargo ARC GREEN  
**Substep:** E0 — externally stabilize PRIME  
**Checkpoint:** ACCESS RESTORED / READY FOR RUNTIME SNAPSHOT

## Proven access state

- Founder Windows device is authenticated to the same Tailscale tailnet as PRIME.
- Windows tailnet address observed: `100.124.16.123`.
- PRIME tailnet address corrected and proven: `100.83.143.22`.
- `tailscale status` showed `prime-vps-01` on the same tailnet.
- `tailscale ping 100.83.143.22` returned repeated successful DERP pongs.
- Direct path was not established during the observed ping, but connectivity was functional through DERP.
- `ssh root@100.83.143.22` invoked Tailscale SSH authentication and completed successfully.
- Founder reached `root@prime-vps-01:~#`.

## Correction

A previously recalled address `100.83.148.22` was wrong. The current proven PRIME Tailscale IPv4 is `100.83.143.22`.

## Operational consequence

Remote operator access is no longer a blocker. Do not reopen general Hetzner/IPv6/DNS64/NAT64 diagnosis based on this access event. Continue directly with E0.1: backup PRIME Hermes config and inspect exact live routing state before any mutation.

## Next acceptance gate

1. backup `/home/prime/.hermes/config.yaml`;
2. inspect current model/fallback/vision routing values;
3. confirm `hermes-gateway.service` state;
4. make no model change until snapshot is reviewed.
