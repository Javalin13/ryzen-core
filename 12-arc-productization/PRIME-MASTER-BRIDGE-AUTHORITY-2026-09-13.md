# PRIME Master Bridge Authority — 2026-09-13

**Status:** ACTIVE CORRECTION / CURRENT AUTHORITY
**Scope:** Lux ↔ PRIME master engineering bridge
**Founder correction:** the canonical PRIME bridge is in `Javalin13/ryzen-core`, not in VONDA.

## Canonical rule

The existing **TO PRIME** and **FROM PRIME** markdown files in PRIME's authenticated local `ryzen-core` worktree are the canonical Lux ↔ PRIME master bridge.

`Javalin13/VONDA-Corporation` may contain VONDA-specific bridge material, but VONDA is an ARC-local bridge only and must not be used as the portfolio-level Lux ↔ PRIME control bridge.

## Immediate correction for the active 2026-09-13 router round

1. Do not treat any `FROM_PRIME` file written in the VONDA repository during the misrouted active run as the master bridge receipt.
2. Switch to the authenticated local worktree whose origin is `Javalin13/ryzen-core`.
3. Locate the already-existing TO PRIME and FROM PRIME markdown pair there; do not create a duplicate bridge pair merely because the exact local path was not supplied in chat.
4. Read the current TO PRIME master directive together with the current RYZ3N source truth, including the free capability router standard and this correction.
5. Continue only the already-authorized router Phase-A inspection: inspect first; no Hermes-core mutation and no unnecessary runtime restarts.
6. Write the detailed Phase-A result into the existing `ryzen-core` FROM PRIME markdown, commit/push it through the authenticated `ryzen-core` worktree, and then send the Founder only the timed MINI REPORT.
7. Preserve ARC-local bridges for Cargo, NARC and VONDA as bounded ARC-specific synchronization surfaces.

## Bridge hierarchy

```text
Javalin13/ryzen-core
  existing TO PRIME markdown   = Lux / Founder → PRIME master engineering directive
  existing FROM PRIME markdown = PRIME → Lux master engineering report

ARC repositories
  Cargo bridge = Cargo-local
  NARC bridge  = NARC-local
  VONDA bridge = VONDA-local
```

## Anti-drift rule

When a master PRIME task spans multiple ARCs or RYZ3N infrastructure, use the `ryzen-core` TO/FROM PRIME bridge. ARC repositories may receive downstream/local receipts, but they do not replace the master bridge.

If PRIME cannot locate the existing TO/FROM pair in its local `ryzen-core` worktree, it must report the local worktree/path ambiguity without creating a competing pair and without falling back to VONDA.

Founder remains final authority.
