# ARC Owner Direct Interaction Standard

**Status:** Founder-authorized canonical standard  
**Date:** 2026-09-12  
**Scope:** Cargo ARC, NARC, VONDA ARC, OMEGA/Factory output, and every future Owner-operated ARC.

## Founder decision

An ARC Owner must be able to interact **directly with their own ARC** through the ARC's normal user-facing channel.

The normal Owner path is:

```text
Owner -> their ARC -> ARC runtime/model/tools -> response to Owner
```

It must NOT require:

```text
Owner -> Founder -> PRIME -> ARC
Owner -> pairing code / PID / candidate ID -> ARC
Owner -> screenshot/manual identity handoff -> ARC
Owner -> another ARC -> their ARC
```

PRIME may supervise, observe non-content telemetry, recover infrastructure, and coordinate bounded maintenance, but PRIME is not a conversational relay between an Owner and the Owner's ARC.

## Current Owner mapping

```text
Narek    -> NARC  -> canonical role: owner
Laetitia -> VONDA -> canonical role: owner
Maria    -> Cargo -> canonical role: owner
John/Jan -> founder everywhere; never consumes an Owner slot
```

Business titles such as Cargo co-founder remain metadata and do not replace canonical authorization role `owner`.

## First-contact contract

For a pre-authorized armed Owner slot, the first eligible real inbound must:

1. arrive directly at the intended ARC;
2. be evaluated by the ARC direct-first-contact identity path before any default Hermes pairing UX can intercept it;
3. atomically bind the intended human to the ARC Owner slot;
4. persist the binding;
5. continue into normal onboarding/conversation in the **same interaction**;
6. require no Founder relay, pairing code, PID, candidate ID, screenshot, or manual identity exchange;
7. keep Founder exclusion intact;
8. fail closed if the slot is unarmed, already bound to another Owner, ambiguous, or otherwise unauthorized.

## Post-binding interaction contract

After binding, every ordinary Owner message must reach that Owner's ARC directly.

The ARC must be able to:

- receive the Owner's message without Founder intervention;
- answer the Owner directly;
- use the ARC's authorized tools/functions directly on behalf of that ARC and Owner context;
- access only its own ARC-scoped Owner namespace/state;
- preserve the Owner identity across gateway/runtime restarts;
- preserve ARC isolation from other Owners and other ARCs;
- continue functioning when PRIME is merely supervising rather than relaying messages.

A healthy Owner conversation is not considered healthy if it only works while the Founder manually intervenes or forwards instructions.

## PRIME / OMEGA boundary

PRIME may:

- supervise gateway health;
- observe non-content operational telemetry;
- detect routing/capacity failures;
- restart/recover approved infrastructure;
- report to Founder;
- coordinate Factory/OMEGA governance.

PRIME must not become a mandatory conversational hop for normal Owner use.

OMEGA/Factory must treat direct Owner-to-ARC interaction as a birth requirement for future ARCs.

## Model/provider independence

Direct Owner interaction is an ARC identity/runtime requirement and must remain true regardless of model routing.

Current model target:

```text
Cargo / NARC / VONDA
  primary  = local-ollama/qwen3:0.6b
  fallback = NONE

PRIME
  primary  = ollama-cloud/minimax-m3:cloud
  fallback = local-ollama/qwen3:0.6b
```

An ARC model failure may produce a sanitized temporary-unavailable message, but it must never reroute the Owner conversationally through PRIME or the Founder as a substitute interaction architecture.

## Owner UX privacy

The Owner should experience their ARC as their direct operational assistant.

Do not expose to Owners:

- provider/model names;
- API/provider billing internals;
- Ollama/Hetzner telemetry;
- daily/weekly/monthly AI quota internals;
- raw provider errors;
- pairing/debug identifiers;
- another ARC's state or Owner information.

## Acceptance gates

An ARC is not Owner-ready until all of the following are proven:

1. Owner sends a normal message directly to the ARC bot/channel.
2. No Hermes pairing screen/code/ID flow appears.
3. If unbound and armed, the intended Owner atomically binds.
4. The same inbound continues to an ARC response without a second manual step.
5. A second normal Owner message receives a direct ARC response.
6. The Owner remains bound after a controlled ARC restart.
7. Founder cannot consume or overwrite the Owner slot.
8. Another unauthorized human cannot take the bound slot.
9. Other ARCs remain isolated/unaffected.
10. PRIME is not required as a conversational relay.
11. No provider/model/capacity internals leak to Owner.
12. The ARC's authorized tool/function path works for the Owner under the same direct interaction path.

## Current master-mission real-human gate

The current migration remains OPEN until all three real humans prove direct interaction end-to-end:

```text
Narek    -> NARC  -> direct inbound -> bind -> same-turn response -> subsequent direct response
Laetitia -> VONDA -> direct inbound -> bind -> same-turn response -> subsequent direct response
Maria    -> Cargo -> direct inbound -> bind -> same-turn response -> subsequent direct response
```

A synthetic/unit test is necessary but not sufficient for this final gate.

## Factory inheritance

Every future Factory-born ARC with an Owner must inherit:

- an armed direct-first-contact Owner slot where applicable;
- Founder exclusion;
- atomic bind semantics;
- no human-visible pairing handoff;
- direct Owner-to-ARC messaging after bind;
- persistent Owner identity across restart;
- ARC-scoped private namespace;
- direct tool/function execution within that ARC's authority;
- Owner-safe temporary-unavailable behavior;
- telemetry proving direct path health without storing private conversation content.

**Founder rule:** the Owner owns the relationship with their ARC. PRIME governs and supervises the ecosystem; it does not sit between the Owner and their ARC during normal use.
