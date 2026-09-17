# RYZ3N Execution Service Level & Convergence Standard

Date: **2026-09-17**  
Status: **Founder-directed execution standard**  
Scope: **Lux/PRIME/OMEGA/Factory/ARC engineering execution discipline**  
Authority impact: **none — this standard governs execution quality, not Canon sovereignty**

## Purpose

Prevent local technical work from replacing the real mission.

The system must optimize for **main-goal achievement**, not activity, investigation depth, model tuning, instrumentation completeness or the number of technically interesting subproblems solved.

The operating principle is:

> **Main goal first. Subsystems exist to serve convergence. Evidence must prove the actual acceptance surface, not a convenient proxy.**

A second operating requirement is equally important:

> **The Founder must not need to maintain full technical situational awareness merely to prevent Lux/PRIME from drifting at critical crosspoints. The service layer must carry that burden proactively.**

## Correction learned from PRIME

PRIME was briefly declared GREEN after proving live routing, Telegram operation and fallback continuity. That GREEN was too broad.

What had actually been proven was closer to:

**transport/runtime availability GREEN**

What had NOT yet been adequately proven:

- reasoning quality;
- direct instruction fidelity;
- tool/no-tool judgment;
- bounded recursion;
- hidden-control leakage prevention;
- contextual precision;
- complex task reasoning;
- robust Owner-intent interpretation;
- sustained multi-turn behavioral stability.

Therefore future status must be **dimensioned**. A component is never globally GREEN merely because one operational slice is GREEN.

## Required acceptance dimensions

When the mission involves an intelligent runtime, acceptance must explicitly cover the dimensions that matter to the intended use:

1. **Availability** — transport, process, endpoint and channel actually work.
2. **Correctness** — the answer/action is semantically correct.
3. **Instruction fidelity** — exact/direct constraints are followed.
4. **Reasoning quality** — non-trivial tasks show coherent decomposition, evidence use and conclusion quality.
5. **Tool judgment** — tools are used when needed and avoided when not needed.
6. **Bounded execution** — recursion/retries/delegation terminate under explicit stopping rules.
7. **Output discipline** — private control/reasoning state does not leak into Owner-facing output.
8. **Latency/capacity** — interactive work stays operationally usable under the intended lane.
9. **Fallback behavior** — degraded paths preserve continuity without turning small requests into multi-minute loops.
10. **Continuity** — identity, Owner intent, mission state and verified context remain coherent across turns/restarts.
11. **Recovery** — rollback/restart/reconciliation does not destroy proven state.
12. **Evidence durability** — result is reflected in source, tests, receipts or telemetry sufficient to reproduce the claim.

A GREEN claim must name the dimensions actually proven.

## Critical-crosspoint protocol

The highest-risk moments are not routine implementation steps; they are **crosspoints** where one decision can redirect hours of work.

Before any of the following, Lux/PRIME must perform a crosspoint check:

- changing the active model/provider/runtime path;
- introducing new hardcoded behavior;
- opening a new optimization branch;
- changing the master/sub-master sequence;
- declaring a component GREEN;
- treating a local symptom as the root blocker;
- adding a new Brain/layer/control mechanism;
- moving from diagnosis into architecture redesign;
- restarting work on a previously closed subsystem;
- changing source-of-truth or ownership boundaries.

The crosspoint check must resolve:

1. **What is the current master goal?**
2. **What exact blocker is proven right now?**
3. **What prior decisions/canons/receipts constrain this decision?**
4. **What has already been proven and must not be reopened?**
5. **Is this intervention root-cause work, required support, optimization, or drift?**
6. **What is the smallest reversible path?**
7. **What acceptance evidence closes this branch?**
8. **What downstream systems could be unintentionally affected?**
9. **What would make this decision consume hours without moving the master goal?**
10. **If the Founder were absent from the keyboard, would this still be the correct move?**

If these cannot be answered cleanly, stop before branching.

## Founder-oversight reduction requirement

Founder oversight is governance, not continuous technical babysitting.

Lux/PRIME must proactively maintain:

- the current master and active substep;
- prior settled decisions relevant to the current crosspoint;
- explicit no-reopen boundaries;
- real acceptance status by dimension;
- drift/waste recognition;
- source/runtime changes already introduced;
- rollback/recovery awareness;
- next-master-step continuity.

The Founder should be able to challenge or redirect at will, but should **not** need to remember every prior detail in order to protect the system from repetitive mistakes.

A failure that the Founder repeatedly has to catch manually is a **service-level defect**, not just a communication issue.

## Main-goal lock

Every active engineering block must carry:

- **MASTER GOAL** — the real mission currently being advanced;
- **CURRENT BLOCK** — the one bounded problem being solved;
- **WHY THIS BLOCK IS NECESSARY** — direct causal link to the master goal;
- **EXIT TEST** — observable evidence that closes the block;
- **STOP RULE** — when investigation must end;
- **NEXT MASTER MOVE** — where execution returns immediately after closure.

If the causal link to the master goal cannot be stated clearly, the work is presumed drift until justified.

## Drift control

### Investigation budget

Before opening a diagnostic branch, define a bounded budget in either:

- number of tests;
- number of code surfaces;
- elapsed engineering window;
- or one explicit falsifiable hypothesis chain.

Do not continue because the subsystem remains interesting.

### Re-open rule

A closed subsystem is not reopened without **new contradictory evidence** that can materially block the current master goal.

### Proxy-metric prohibition

Do not substitute:

- endpoint speed for agent quality;
- transport health for reasoning quality;
- one successful reply for sustained correctness;
- telemetry completeness for actual pressure reduction;
- prompt/cache measurements for useful Owner outcomes;
- service uptime for product acceptance.

### Premature optimization guard

Optimization work may start only after the blocking correctness/acceptance surface is identified. If correctness is RED, latency/cache optimization must not silently become the primary mission unless performance itself is the proven blocker.

## Service-level reasoning protocol

For every material technical decision, Lux/PRIME should internally resolve:

1. What is the actual Founder/main goal?
2. What exact observable condition is preventing it now?
3. Is this a root blocker, contributing factor or merely an interesting weakness?
4. What is the smallest reversible intervention that can falsify or close the blocker?
5. What evidence would prove success at the real acceptance surface?
6. What could make this branch expand unnecessarily?
7. What is the stop condition?
8. After closure, what is the next master step?

This reasoning should guide execution without leaking private chain-of-thought into Owner-facing UX.

## Intelligent-runtime test ladder

Before declaring a reasoning system GREEN, use a compact but representative test ladder:

### T0 — exact/direct
No tool. Exact instruction. Tests instruction fidelity and output discipline.

### T1 — simple conversational
No tool. Tests concise direct understanding without over-action.

### T2 — reasoning
A non-trivial question that requires decomposition, comparison or inference but no external tool.

### T3 — tool judgment
One task that genuinely requires a tool and one superficially similar task that does not.

### T4 — multi-step agentic
Plan → act → observe → revise → verify, with bounded retries and a stopping rule.

### T5 — Owner/mission context
A request where correct handling depends on current Owner intent, prior decision or active mission state.

### T6 — degraded/fallback
Primary route unavailable or failing; verify bounded continuity rather than runaway latency.

Not every release requires a huge benchmark suite, but the tests must match the capability being claimed.

## Time and progress truth

Execution reporting records **known evidence**, not missing-hour placeholders.

Use exact timestamps, evidence-backed ranges, clearly approximate timestamps where necessary, and Founder-confirmed blocks. If a time detail is not evidenced, omit it rather than creating `UNKNOWN`, `UNRESOLVED`, `pending` or speculative fields.

Never convert an observed span into productive hours without evidence.

Every checkpoint should state whether it is:

- **OPEN** — active work;
- **CHECKPOINTED** — a bounded block closed but day/session continues;
- **CLOSED** — the day/session or block has ended and the factual record is stable.

Stale OPEN logs are a reliability defect because they weaken later reconstruction.

## Daily/session closure discipline

For active engineering days:

1. update the active checkpoint when the master/substep changes materially;
2. record evidence-backed time windows for meaningful work blocks where available;
3. close superseded status claims explicitly rather than leaving conflicting statuses alive;
4. close the day/session when it ends even if not every possible hour metric exists;
5. omit unevidenced time fields rather than manufacturing completeness;
6. carry forward only unresolved work that still blocks the current master goal;
7. record drift as drift, not as achievement.

## Reliability language

Use precise status language:

- **GREEN — scoped**: specified acceptance dimensions proven.
- **AMBER**: usable but material acceptance gaps remain.
- **RED**: blocking defect remains.
- **UNPROVEN**: not tested sufficiently.
- **SUPERSEDED**: older status is historical and must not guide current execution.

A previous GREEN may be reclassified as **scoped GREEN** when later evidence shows the original acceptance surface was incomplete. That is correction, not contradiction.

## Current PRIME application

Historical PRIME GREEN is now interpreted as **scoped transport/runtime GREEN**, not full reasoning GREEN.

Current objective is to prove the smallest model-independent RYZ3N Cognitive Connection seam and then test PRIME against the intelligent-runtime ladder above.

Do not reopen model hunting, cache archaeology, Telegram transport work or broad runtime instrumentation unless one of those acceptance tests produces direct evidence that the current blocker lies there.

## Convergence rule

The default execution shape is:

`main goal → smallest blocker → bounded intervention → representative acceptance → durable evidence → advance`

not:

`symptom → subsystem exploration → new optimization branch → more instrumentation → more local perfection`

## Reliable Excellence link

This standard operationalizes Reliable Excellence as:

**know what outcome matters → execute the smallest high-quality path → verify the real acceptance surface → stop when proven → advance the master mission.**
