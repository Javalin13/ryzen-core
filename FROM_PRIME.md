# RYZ3N CORE — FROM PRIME

**Status:** AWAITING PRIME REPORT  
**Authority:** PRIME -> Lux master engineering report  
**Repository:** `Javalin13/ryzen-core`  
**Counterpart:** `TO_PRIME.md`

This file is the canonical detailed PRIME -> Lux report surface for portfolio-level / cross-ARC / shared-runtime engineering work.

## Reporting rule

Before representing a material engineering round as durably reported, PRIME must:

1. fetch/pull current `ryzen-core` source;
2. read repository-root `TO_PRIME.md` and current canonical RYZ3N source relevant to the mission;
3. execute only the bounded authorized task;
4. replace this file with the current detailed report;
5. commit and push it to `ryzen-core`;
6. then send the Founder only the MINI REPORT.

The Founder must not be used as a copy/paste transport between PRIME and Lux.

## Required detailed-report fields

For each material round, replace the placeholder below with:

```text
ROUND / MASTER POSITION:
STATUS / ACCEPTANCE RESULT:
CONSUMED RYZEN-CORE HEAD:
CONSUMED TO_PRIME DIRECTIVE:

INSPECTION / IMPLEMENTATION SUMMARY:
- exact files/classes/functions/hooks inspected or changed
- exact runtime/source boundary used

EVIDENCE:
- observed runtime/source evidence
- real vs simulated classification
- relevant latency/capacity/fallback evidence

ISOLATION / PRIVACY:
- PRIME impact
- Cargo impact
- NARC impact
- VONDA impact
- Owner-private content boundary

CHANGED PATHS:

ROLLBACK:

RISKS / BLOCKERS:

ELAPSED:
IMPLEMENTATION ETA / NEXT STEP:

LUX: SYNC NEEDED | NO SYNC NEEDED
```

Do not place raw secrets, tokens, API keys, passwords, private keys, pairing secrets/codes, full environment dumps, private Owner conversations or unnecessary customer payload in this file.

## Current expected report

Current master position is **M3/16 — Cargo ARC GREEN**.

The next report expected here is the Phase-A inspection result for the Founder-approved free capability router described in `TO_PRIME.md`.

Phase A is inspection-only: no Hermes-core mutation and no unnecessary PRIME/Cargo/NARC/VONDA restart.

## Founder MINI REPORT contract

After this detailed report is pushed, Founder chat should contain only:

```text
STATUS: <GREEN/AMBER/RED + one-line result>
CHANGED: <one or two key facts>
NEXT: <next bounded action or NONE>
TIME: <elapsed> | ETA: <estimate>
LUX: SYNC NEEDED | NO SYNC NEEDED
BRIDGE: <ryzen-core pushed short SHA>
```

## Bridge hierarchy

Repository-root `TO_PRIME.md` / `FROM_PRIME.md` in `Javalin13/ryzen-core` are the canonical Lux <-> PRIME master bridge.

ARC repository bridges remain ARC-local and do not replace this master surface.
