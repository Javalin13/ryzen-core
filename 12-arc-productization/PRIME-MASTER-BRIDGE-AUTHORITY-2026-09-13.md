# PRIME Master Bridge Authority — 2026-09-13

**Status:** ACTIVE / CURRENT AUTHORITY  
**Scope:** Lux ↔ PRIME master engineering bridge  
**Founder correction:** the canonical PRIME bridge is in `Javalin13/ryzen-core`, not VONDA.

## Canonical rule

The canonical Lux ↔ PRIME master bridge is the repository-root pair:

```text
Javalin13/ryzen-core/TO_PRIME.md
Javalin13/ryzen-core/FROM_PRIME.md
```

- `TO_PRIME.md` = Lux / Founder → PRIME master engineering directive.
- `FROM_PRIME.md` = PRIME → Lux master engineering report.

These files are authoritative for portfolio-level, cross-ARC and shared-runtime PRIME work.

`Javalin13/VONDA-Corporation`, Cargo and NARC may contain ARC-specific bridge material, but those are ARC-local bridges only and must not replace the portfolio-level Lux ↔ PRIME control bridge.

## Immediate correction for the active 2026-09-13 router round

1. Do not treat any `FROM_PRIME` file written in the VONDA repository during the misrouted active run as the master bridge receipt.
2. Use the authenticated local worktree whose origin is `Javalin13/ryzen-core`.
3. Fetch/pull current `origin/main` without discarding valid local work.
4. Read repository-root `TO_PRIME.md` together with current canonical RYZ3N source truth.
5. Continue only the already-authorized free-router Phase-A inspection: inspect first; no Hermes-core mutation and no unnecessary runtime restarts.
6. Write the detailed Phase-A result into repository-root `FROM_PRIME.md`, commit/push through the authenticated `ryzen-core` worktree, then send the Founder only the timed MINI REPORT.
7. Preserve ARC-local bridges for Cargo, NARC and VONDA as bounded ARC-specific synchronization surfaces.

## Bridge hierarchy

```text
Javalin13/ryzen-core
  TO_PRIME.md   = Lux / Founder → PRIME master engineering directive
  FROM_PRIME.md = PRIME → Lux master engineering report

ARC repositories
  Cargo bridge = Cargo-local
  NARC bridge  = NARC-local
  VONDA bridge = VONDA-local
```

## Consume / sync shorthand

`consume` = PRIME fetches current `ryzen-core`, reads repository-root `TO_PRIME.md` plus the current canonical source relevant to the mission, executes only the bounded authorized work, and reports via repository-root `FROM_PRIME.md`.

`sync` = Lux reads the latest pushed repository-root `FROM_PRIME.md`, reviews evidence/source changes, and updates repository-root `TO_PRIME.md` or other canonical source as necessary.

The Founder is never used as the detailed technical copy/paste transport.

## Anti-drift rule

When a master PRIME task spans multiple ARCs or RYZ3N infrastructure, use the repository-root `TO_PRIME.md` / `FROM_PRIME.md` pair. ARC repositories may receive downstream/local receipts, but they do not replace the master bridge.

If these files are ever absent from the local `ryzen-core` worktree, first fetch current `origin/main`; do not fall back to VONDA as the master bridge and do not create a competing pair elsewhere.

Founder remains final authority.
