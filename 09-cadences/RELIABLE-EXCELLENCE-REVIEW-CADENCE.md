# Reliable Excellence — Review Cadence

Date: 2026-09-14  
Status: **ACTIVE / OPERATING CADENCE**

Governing invariant:
`00-foundation/RELIABLE-EXCELLENCE-ARCHITECTURAL-INVARIANT.md`

## Purpose

Reliable Excellence must remain alive during normal operation and evolution, not only during architecture design or incident response.

This cadence is a standing review lens for RYZ3N work. It does not require bureaucracy for trivial changes; it ensures material work repeatedly asks whether quality and reliability are rising or drifting.

## Daily / active-work lens

For material implementation work, ask:

- Did the change do what it was intended to do?
- Did it introduce obvious reliability, latency, security, recovery or consistency regressions?
- Is the claimed state backed by current evidence?
- Did a discovered defect reveal a reusable prevention opportunity?

## Weekly lens

Where active engineering exists, review:

- recurring failures/incidents;
- unresolved reliability gaps;
- performance/responsiveness degradation;
- stale or contradictory evidence;
- recovery/reconstruction readiness;
- tests or quality gates missing for repeatedly touched paths;
- OMEGA findings that should become Factory/architecture improvements;
- manual defect-discovery patterns that should become automated detection/prevention.

## Monthly / maturity lens

Review whether RYZ3N is measurably moving along:

**Engineering Maturity → Proven Reliability → Reliable Excellence**

Look for progress in:

- automated testing and validation;
- observability;
- recovery/rollback;
- source/deploy integrity;
- security/privacy/integrity;
- performance evidence;
- repeatable Factory production quality;
- reduced dependence on Founder manual quality control;
- reusable prevention of previously observed defect classes.

## Lesson-to-prevention rule

A lesson learned should be classified as one of:

1. local one-off correction;
2. ARC/domain pattern;
3. reusable RYZ3N reliability pattern.

Where #2 or #3 applies, route the learning toward the relevant standard, Factory contract, schema, test, observability rule or architecture mechanism.

## Anti-theater rule

Do not create meetings, dashboards or checklists merely to demonstrate compliance.

The cadence exists to answer:

> **Is the technology becoming more dependable in reality?**

If not, surface the truth and improve the system.
