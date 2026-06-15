# 2026-06-15 — Autonomous-acceptance doctrine (act by default, pause for crucial)

```yaml
---
id: 2026-06-15-autonomous-acceptance-doctrine
date: 2026-06-15
title: Autonomous-acceptance doctrine (act by default, pause for crucial)
related_docs:
  - 05-adrs/0003-shift-to-autonomous-acceptance-doctrine.md
  - 00-foundation/FOUNDATION.md (autonomous-acceptance section)
  - 00-foundation/GOVERNANCE.md (Rule F-GOV-5)
  - 11-fleet-arc-intake/01-dispatch-intelligence/2026-06-15-01-driver-assignment-by-proximity.md (first agent-accepted intake)
  - 11-fleet-arc-intake/INDEX.md (intake log with first row)
  - 09-cadences/fleet-arc-intake/TEMPLATE.md (revised lifecycle)
  - Javalin13/ryzen-continuity/10-lessons-learned/2026-06-15-autonomous-acceptance-doctrine.md (sibling lesson)
related_adrs: 0003
tags: #doctrine #autonomy #accumulation #founder-authority #bright-line
projects: ryzen-core
classification: approved-architecture (doctrine evolution)
amendable: true-additively
status: foundation-doctrine (cross-repo)
related_repo_canonical: Javalin13/ryzen-continuity
```

## The lesson

The previous operational doctrine (codified in the foundation and the intake template) required the agent to wait for founder acceptance on every accumulation change. The default mode was *wait*; the agent produced "awaiting your X" messages; the founder read them as stalls.

The founder's clarification 2026-06-15 inverted the default:

> Change the doctrine to not wait for github changes and discoveries accept if you plan to change something crucial.

The new doctrine is codified in **ADR 0003** (`05-adrs/0003-shift-to-autonomous-acceptance-doctrine.md`). The bright line is:

- **Doctrine changes** (governing docs, canonicals, ADRs, runtime roadmap strategy, intake promotion, new repos, off-strategy, data risk, large-scope rework, uncertain changes) require founder signoff.
- **Accumulation changes** (intakes, lessons, scaffolding, cadences, tools, fixes, refactors, commits, tags, pushes) are the agent's default mode.

**The agent accumulates. The agent does not implement. The agent does not wait.**

## What this lesson is about

This lesson is about the **operational posture** of the agent, not about a specific technical decision. The lesson has 4 sub-insights:

1. **Founder intent is the bright line.** The founder's clarification established that some changes are crucial (doctrine) and some are not (accumulation). The agent's job is to recognize the bright line and act accordingly.
2. **"Awaiting your X" is an anti-pattern.** The previous doctrine produced wait-state messages. The new doctrine produces "what was just done" reports. The shift from *wait* to *act* is a behavioral change, not just a textual change.
3. **The 5-state intake lifecycle now includes `agent-accepted` as the default.** The previous lifecycle was `raw → validated → accepted → promoted | deprecated`. The new lifecycle is `raw → validated → agent-accepted → founder-accepted → promoted | deprecated`. The `agent-accepted` state is the new default; the founder-accepted state is a higher-trust sub-class.
4. **The agent's first autonomous action was to *seed* the accumulation layer with an inferred baseline.** The first intake (driver-assignment-by-proximity) is *inferred*, not *observed*. The agent marks it as such explicitly. The founder may deprecate, override, or promote at any time. The act of *seeding* the layer is itself the lesson: the agent proposes, the founder refines.

## The lesson's operational consequence

The agent's *next* actions (per ADR 0003) will be:

- **Continue accumulating.** Add more intakes (one per turn or per discovery cycle) in the appropriate subdirectory. Each intake is an *agent-accepted* candidate that the founder may deprecate, override, or promote.
- **Refine existing intakes.** When the agent learns more (e.g., from a FleetConnect repo, from a real conversation, from a simulation), update the intake's tier classification, validation evidence, and reusability argument.
- **Cross-reference actively.** The intake log (`11-fleet-arc-intake/INDEX.md`) is the canonical log. The agent updates it as intakes are added, deprecated, or promoted.
- **Promote only when asked.** Promotion is a *crucial* change (per the bright line). The agent does not auto-promote; the founder promotes.
- **Pause for the runtime phase.** The runtime phase is *deferred* (per ADR 0002) and is a *crucial* change. The agent does not start R1 without founder authorization.

## Why this lesson matters

The previous doctrine was *too conservative*. It prioritized safety over velocity. The founder's clarification says: *act*, not *wait*. The lesson is that **the agent's operational posture is the founder's call**, and the founder prefers velocity with bright lines over conservatism with wait states.

The lesson is *cross-repo* — it is captured in both `ryzen-core` (this lesson) and `Javalin13/ryzen-continuity` (the sibling lesson in the canonical doctrine layer). The continuity version is the *canonical* statement; the core version is the *operational* statement.

## Cross-references

- ADR 0003: `05-adrs/0003-shift-to-autonomous-acceptance-doctrine.md`
- Foundation doctrine (autonomous-acceptance section): `00-foundation/FOUNDATION.md`
- Foundation governance (Rule F-GOV-5): `00-foundation/GOVERNANCE.md`
- Intake log (first row): `11-fleet-arc-intake/INDEX.md`
- First intake: `11-fleet-arc-intake/01-dispatch-intelligence/2026-06-15-01-driver-assignment-by-proximity.md`
- Intake template (revised): `09-cadences/fleet-arc-intake/TEMPLATE.md`
- Sibling lesson in continuity: `Javalin13/ryzen-continuity/10-lessons-learned/2026-06-15-autonomous-acceptance-doctrine.md`

## The 1-sentence summary

> The agent acts by default and pauses only for crucial changes; the founder prefers velocity with bright lines over conservatism with wait states.
