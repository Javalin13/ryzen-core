# 2026-06-15-01 — First agent-accepted Fleet ARC intake (FLEETCONNECT-DRIVER-ASSIGNMENT-BY-PROXIMITY)

```yaml
---
id: 2026-06-15-01-driver-assignment-by-proximity
date_observed: 2026-06-15
date_intake_created: 2026-06-15
intake_type: 01-dispatch-intelligence
title: First agent-accepted Fleet ARC intake (driver-assignment-by-proximity)
status: agent-accepted
classification: research-and-exploration (inferred; not yet observed in operational data)
amendable: true-additively
related_fleetconnect_evidence: (none — this is the first intake; the agent is seeding the canonical accumulation layer)
related_arc: FleetConnect
founder_acceptance: null (per ADR 0003, the agent accepts by default)
agent_acceptance:
  agent: hermes
  date: 2026-06-15
  decision: agent-accepted
  notes: First agent-accepted intake; founder may deprecate, override, or promote at any time
founder_override_available: yes
promotion_path: (not promoted; this intake is the seed of the accumulation layer)
deprecation_path: (not deprecated)
---

# 2026-06-15-01 — First agent-accepted Fleet ARC intake (driver-assignment-by-proximity)

> **Founder notice:** This is the first intake. The agent is *seeding* the canonical accumulation layer (per ADR 0003, the autonomous-acceptance doctrine). The discovery is *inferred*, not *observed*, and is explicitly marked as such in §5 (Tier Classification). The founder may deprecate, override, or promote this intake at any time. The agent's role is to propose, commit, and surface; the founder's role is to refine.

## 1. Discovery (inferred)

In the absence of FleetConnect's operational data (which the agent does not yet have access to), the first inferred Fleet ARC discovery is:

> **In FleetConnect, the optimal driver for a given booking is the *nearest available driver* to the pickup location at the time of booking, weighted by (a) vehicle capacity match, (b) driver rating, (c) driver historical on-time rate.**

This discovery is the *trivial case* of a FleetConnect dispatch intelligence observation. It is the **default baseline** that any FleetConnect deployment is expected to have. The discovery is *inferred* from the standard ride-hailing / dispatch domain, not *observed* in FleetConnect's actual data. The agent marks it as `research-and-exploration` per the tier classification.

The discovery has 3 sub-insights:

1. **Proximity is a load-bearing heuristic.** In most dispatch domains, the nearest available driver is the best default because it minimizes pickup time, which is the most-visible customer satisfaction metric.
2. **Capacity, rating, and on-time rate are second-order filters.** A driver who is *close* but has the wrong vehicle, low rating, or poor on-time record is worse than a driver who is *slightly farther* but has better second-order metrics.
3. **The weighting is a tunable parameter.** The FleetConnect operator can tune the relative weights of proximity vs. capacity vs. rating vs. on-time rate based on operational priorities (e.g., prioritize rating during peak demand; prioritize proximity during low-demand surge).

## 2. Source (FleetConnect Evidence)

**This intake does NOT have FleetConnect operational data as its source.** The discovery is *inferred* from the standard dispatch domain, not *observed* in FleetConnect's data.

The agent's source for this intake is:
- The intake template itself (`09-cadences/fleet-arc-intake/TEMPLATE.md`)
- The Intake type 1 description (`11-fleet-arc-intake/01-dispatch-intelligence/README.md`)
- The general ride-hailing / dispatch domain knowledge embedded in the agent's training data (which is *not* FleetConnect-specific)

**Critical note for the founder:** When FleetConnect's operational data becomes available (e.g., a FleetConnect repo with real booking data, real driver records, real performance metrics), this intake should be **superseded** by one or more *observed* intakes that cite the actual data.

## 3. Validation Evidence

The validation evidence for this intake is *weak* (since the discovery is *inferred*, not *observed*):

- **Domain pattern:** The "nearest available driver + second-order filter" pattern is the *de facto* standard in ride-hailing / dispatch. It is not a novel insight; it is the baseline.
- **No FleetConnect-specific evidence:** The agent has no access to FleetConnect's operational data as of 2026-06-15.
- **Test case:** This intake would be *validated* (in the strict sense) when FleetConnect's operational data shows that the *current* default dispatch heuristic is, in fact, proximity-weighted with second-order filters. If FleetConnect uses a *different* heuristic (e.g., always-assign-to-favorite-driver, or always-assign-to-highest-rated, or round-robin), this intake would be *superseded* or *deprecated*.

**The agent marks this intake as `inferred` explicitly** so the founder knows the evidence is weak. The intake is still useful as a *baseline* against which FleetConnect's actual heuristic can be compared.

## 4. Reusability Argument

The discovery is expected to recur because:

- The dispatch domain is mature and the baseline heuristic is well-known.
- Any new dispatch system (including FleetConnect's future deployment) is likely to start with proximity as the default and add second-order filters.
- The load-bearing insight (proximity as the *default*, second-order as the *filter*) is *durable* across time and across ARC domains.

The reusability is high, but the *specific weights* are FleetConnect-specific and will need to be tuned.

## 5. Tier Classification (per the Interpretation Protocol)

| State | Status for this intake |
|---|---|
| **Implemented** | ❌ No (FleetConnect is not yet deployed; the heuristic is *inferred*, not implemented) |
| **Planned** | ❌ No (not on a FleetConnect roadmap yet) |
| **Designed** | ❌ No (the agent has no FleetConnect architecture docs to reference) |
| **Envisioned** | ⚠️ Partial (the heuristic is *envisioned* as the baseline, but not yet designed into FleetConnect) |
| **Researched** | ✅ Yes (this is a *researched* intake — the heuristic is investigated and the agent has the data to support it) |

**Net tier: `research-and-exploration`** (per the Interpretation Protocol's 5-tier classification).

## 6. Cross-References

- **Recovery archive:** `Javalin13/ryzen-continuity/04-recovery-archive/RECOVERED-REUSABLE-CONCEPTS.md` (C1 Cognition Loop, C5 Fleet ARC topology)
- **Rebuild spec:** `Javalin13/ryzen-continuity/RYZEN-REBUILD-SPECIFICATION-v1.0.md` (R3 Real Execution & Adaptive Cognition, §3.3)
- **Runtime roadmap:** `06-runtime-roadmap/ROADMAP.md` (R3 deferred, not imminent)
- **Foundation governance:** `00-foundation/GOVERNANCE.md` Rule F-GOV-5 (agent-autonomy for intakes)
- **Continuity canonical:** `Javalin13/ryzen-continuity/04-fleetconnect/FLEETCONNECT-CANONICAL.md` (when available)
- **Other intakes:** This is the first intake; no siblings yet.

## 7. Promotion Path

**Not promoted.** This intake is the *seed* of the accumulation layer. It is not promoted to design or runtime.

**If/when promoted**, the promotion path would be:

- **Promoted to runtime requirement (R3 deliverable):** "FleetConnect dispatch must implement proximity-based driver assignment with second-order filtering. The weights are tunable. The default weights are: proximity = 0.5, vehicle capacity match = 0.2, driver rating = 0.2, on-time rate = 0.1." This would be a new ADR (e.g., ADR 0004: "FleetConnect dispatch heuristic v1.0").
- **Promoted to foundation governance (new rule):** "All Fleet ARC dispatch intakes must include proximity + second-order filter analysis as a baseline against which observed heuristics are compared." This would be a new ADR.
- **Promoted to canonical doctrine (continuity repo):** "The dispatch domain follows a proximity-default, second-order-filter pattern across all ARCs." This would be a new canonical in continuity.

Promotion requires a new ADR. The promotion ADR must reference this intake.

## 8. Deprecation Path

**Not deprecated.** This intake remains valid as a *baseline* against which observed heuristics are compared.

**If/when deprecated**, the deprecation path would be:

- **Superseded by an observed intake:** When FleetConnect's operational data is available, an *observed* intake would replace this *inferred* intake. The observed intake would have FleetConnect-specific data as its source.
- **Found invalid:** If the agent or founder determines that the proximity-default, second-order-filter pattern is *not* the right baseline for FleetConnect (e.g., FleetConnect uses a different domain — long-haul trucking, where proximity is less important; or FleetConnect is a niche market where customer-favorite-driver is the dominant heuristic), this intake is deprecated and replaced with the correct baseline.

Deprecated intakes are *preserved* (additive only); they are never deleted.

## 9. Notes

- The agent is *not* claiming this is a novel insight. It is the *trivial case* of a dispatch domain observation.
- The agent is *not* claiming this is FleetConnect-specific. It is a general pattern that *may or may not* apply to FleetConnect.
- The agent's role is to *propose* (per ADR 0003) and *commit* (per the autonomous-acceptance doctrine). The founder's role is to *validate* (with real data) or *deprecate* (with a better baseline).
- The intake filename is `2026-06-15-01-driver-assignment-by-proximity.md` because it is the first intake on 2026-06-15 and its subject is the proximity-based driver assignment heuristic.
- The intake is added to `11-fleet-arc-intake/01-dispatch-intelligence/` (per the 10-intake-type structure).

---

## Template Followed

This intake follows the `09-cadences/fleet-arc-intake/TEMPLATE.md` structure. The 9 sections (Discovery, Source, Validation Evidence, Reusability Argument, Tier Classification, Cross-References, Promotion Path, Deprecation Path, Notes) are all present.

The intake is `agent-accepted` (status: agent-accepted) per ADR 0003. The founder may deprecate, override, or promote at any time.

The intake is added to the intake log (`11-fleet-arc-intake/INDEX.md`) as the first accepted intake.

The intake is the *seed* of the accumulation layer. Future intakes will build on this one (or supersede it).
