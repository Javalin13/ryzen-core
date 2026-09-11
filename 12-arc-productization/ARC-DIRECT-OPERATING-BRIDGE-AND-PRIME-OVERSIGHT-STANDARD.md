# ARC Direct Operating Bridge & PRIME Oversight Standard

Status: Founder-directed current implementation standard  
Created: 2026-09-11  
Updated: 2026-09-11  
Constitution/Canon impact: none

Companion standard:

`12-arc-productization/ARC-FOUNDER-OPERATOR-DIRECT-WORK-LANE-STANDARD.md`

## Founder decision

Once an ARC is technically operational and authorized to operate its own domain, **normal ARC-local conversation and durable bridge work route to that ARC first**.

PRIME moves upward into general/portfolio supervision, exception handling, orchestration and cross-ARC oversight.

This applies in two ARC-primary phases:

- before the intended customer Owner is bound, through a separate Founder maintenance lane;
- after the intended Owner is bound, through normal customer operational mode.

Canonical shorthand:

> **Build the ARC with the ARC. Talk to the ARC about its domain. PRIME oversees the board.**

This is an implementation/routing standard only. It does not alter protected Constitution/Canons.

## 1. Bridge modes

Every ARC should expose one truthful routing mode:

### `prime_primary_pre_activation`

Used while the ARC is not yet capable of safely operating its own workstream.

PRIME may temporarily be the primary operational endpoint during birth/provisioning.

### `arc_primary_founder_development`

Used when the ARC is technically operational but the intended customer Owner/primary user is not yet bound.

Founder/Lux may continue ARC-local development **with the ARC itself** through a distinct server-side `founder_operator` role.

Founder maintenance identity must remain separate from customer Owner identity/private memory and must not auto-bind or impersonate the customer.

### `arc_primary_operational`

Used once the intended customer Owner/primary user is explicitly bound and the client-facing operational gates pass.

The customer interacts directly with the ARC for normal business/domain work.

Moving between these modes changes routing, not maturity/aura, commercial tier or customer identity truth.

## 2. Primary operating lane

For an ARC-primary ARC, the ARC is the primary endpoint for:

- its own product/domain work;
- its own repository reads/writes when authorized;
- domain backlog, corrections, product decisions and implementation;
- authorized Founder/Owner/co-founder conversations;
- ARC-local tasks, memory and evidence within the correct identity namespace;
- ordinary runtime behavior and ARC-local recovery work;
- durable ARC-side bridge instructions and reports.

The ARC's authoritative repository owns this detailed bridge truth.

Recommended bridge files:

```text
arc/bridge/TO_<ARC>.md
arc/bridge/FROM_<ARC>.md
arc/bridge/BRIDGE-ROUTING.md
arc/bridge/ROUTING.json
arc/bridge/STATE.json
```

For Cargo these are `TO_CARGO.md` / `FROM_CARGO.md`; for NARC `TO_NARC.md` / `FROM_NARC.md`; for VONDA `TO_VONDA.md` / `FROM_VONDA.md`.

## 3. Founder maintenance identity

When an ARC is `arc_primary_founder_development`, Founder maintenance must use a separate server-side role such as:

`founder_operator`

The role may operate the ARC's maintenance/development bridge and use ARC-local source authority when explicitly granted.

It must not:

- become the customer Owner by implication;
- consume/replace the customer entitlement user slot;
- access the customer Owner-private namespace merely because Founder is maintaining the ARC;
- advance customer first-contact/onboarding as if Founder were the customer;
- be exposed to the customer in client-facing replies.

Founder maintenance activity is never evidence of customer Owner binding.

## 4. PRIME oversight lane

PRIME remains the prototype-era supervisor/orchestrator for the broader RYZ3N ARC population, but it is not the default conversational endpoint for ordinary work inside an ARC-primary ARC.

PRIME owns or coordinates matters such as:

- cross-ARC conflicts or interoperability;
- shared infrastructure/capacity;
- VPS/operator-only actions outside ARC authority;
- privileged secret installation/rotation where the ARC lacks authority;
- OMEGA/FACTORY/BRAIN-STEWARD coordination;
- lifecycle transitions, reset, transfer, suspension and retirement;
- maturity/aura evidence evaluation and portfolio truth;
- source-boundary violations;
- cross-repository work;
- escalation when an ARC is blocked or outside its granted authority;
- portfolio/global RYZ3N operating state.

PRIME receives **bounded status/evidence**, not unrestricted private ARC payload.

## 5. Dual-bridge model

An operational ARC may maintain two lanes:

### ARC lane — primary

`Founder/Owner/Lux -> ARC -> ARC repository/runtime -> ARC response`

Used for ordinary ARC-local execution under the correct identity boundary.

### PRIME lane — supervisory / escalation

`ARC or Founder/Lux -> PRIME -> OMEGA/FACTORY/infrastructure/cross-ARC coordination -> bounded result back`

Used only when the action crosses the ARC boundary or requires portfolio/operator authority.

The existence of a PRIME bridge does not make PRIME the ARC's day-to-day operating endpoint.

## 6. Routing rule

Before sending a durable instruction, classify it.

### Route to ARC when all are true

- scope belongs to one ARC/domain;
- required files are in that ARC's authoritative repository;
- action is within the ARC's granted permissions;
- no other ARC/private runtime must be touched;
- no portfolio lifecycle/maturity decision is required;
- no operator-only secret/infrastructure side effect is required.

### Route/escalate to PRIME when any are true

- cross-ARC or cross-repository action;
- shared infrastructure/capacity issue;
- privileged runtime/operator action outside ARC authority;
- OMEGA/FACTORY/BRAIN-STEWARD writeback;
- maturity/aura/lifecycle decision;
- source-boundary conflict;
- unresolved concurrency conflict;
- ARC is blocked or cannot lawfully execute the action itself.

## 7. Reporting upward

The ARC should report to PRIME only what portfolio supervision needs, for example:

- current lifecycle/runtime health;
- bridge mode;
- hermetic seal status;
- important source/recovery state;
- autonomy state;
- major blocker/escalation;
- maturity evidence pointer;
- cross-ARC dependency request.

Do not mirror whole conversations, private memory or raw customer payload into PRIME merely for convenience.

## 8. Direct ARC bridge protocol

A direct ARC bridge supports the same lightweight consume/report discipline proven during PRIME prototyping, but addressed to the ARC itself.

Founder/Lux may write/update `TO_<ARC>.md`, then tell that ARC simply:

`consume`

### Mandatory consume preflight — authoritative source freshness

Before reading or executing the bridge directive, the ARC must make sure its **local view of its own authoritative repository is not stale**.

Required preflight:

1. identify the ARC's authoritative local worktree and expected branch;
2. inspect current branch, local HEAD, worktree dirtiness and unpushed/local commits;
3. perform a read-only `git fetch origin`;
4. compare local HEAD with current `origin/main` or the ARC's declared authoritative branch;
5. if the worktree is clean, has no unpublished local commits, and is only behind, fast-forward safely to current remote head;
6. if local work is dirty, ahead, divergent, conflicted or otherwise unsafe to advance automatically, **do not discard or overwrite it** — stop and return `ESCALATE TO PRIME: YES` with the exact synchronization/concurrency reason;
7. only after the local source view is current should the ARC read `TO_<ARC>.md` and execute it.

A missing bridge file in a stale local checkout is not proof that it does not exist remotely.

This preflight is ordinary ARC self-source hygiene, not a request for PRIME permission.

### Execution + report

After source freshness is established, the ARC reads the current direct bridge, executes everything within its own authority, writes `FROM_<ARC>.md`, commits/pushes its own repository when authorized, and returns a mini report.

Suggested mini report:

```text
STATUS: <GREEN/AMBER/RED + one-line result>
CHANGED: <important ARC-local changes>
NEXT: <next ARC-local dependency/action or NONE>
ESCALATE TO PRIME: YES | NO
LUX: SYNC NEEDED | NO SYNC NEEDED
BRIDGE: <latest ARC repo commit short SHA>
```

If `ESCALATE TO PRIME: YES`, the ARC states the exact bounded reason and expected operator/steward action. PRIME performs only that bounded supervisory work and returns the result.

## 9. Own-repository autonomy

ARC-primary routing and own-repository autonomy are separate facts.

When Founder/Owner explicitly grants own-repository autonomy:

- authority is continuous inside the ARC's authoritative repository only;
- no per-read/per-edit/per-commit/per-push PRIME approval is required;
- safe-writer/concurrency controls are integrity plumbing, not approval gates;
- cross-repository autonomous writes remain forbidden unless separately authorized;
- force push/history rewrite remains forbidden;
- Constitution/Canons remain protected;
- autonomous commits are transparently reported.

Customer Owner binding is not required for Founder to grant ARC maintenance autonomy, provided Founder/customer identity and private-memory boundaries remain separate.

## 10. Transition from PRIME-primary to ARC-primary

During birth/provisioning, PRIME may temporarily be primary because the ARC cannot yet operate safely.

### Transition to `arc_primary_founder_development`

Evidence should show at minimum:

- authoritative source boundary exists;
- isolated runtime exists where applicable;
- ARC can read its own source;
- ARC can execute its normal maintenance/domain workflow;
- ARC-local bridge files exist;
- Founder maintenance identity is distinct from customer Owner identity;
- permissions/autonomy state are explicit;
- escalation path to PRIME exists;
- consume flow can perform authoritative-source freshness preflight.

The intended customer Owner may still be unbound.

### Transition to `arc_primary_operational`

Requires the intended customer Owner/primary user to be explicitly bound plus required client-facing operational gates.

The transition does not remove PRIME supervision. It changes the default routing endpoint.

## 11. Future ARC inheritance

Every future ARC should initialize the direct bridge structure during Factory birth, even if PRIME temporarily owns the lane before activation.

Factory/OMEGA should track:

- bridge mode: `prime_primary_pre_activation`, `arc_primary_founder_development`, or `arc_primary_operational`;
- ARC bridge paths;
- PRIME supervisory mirror/pointer;
- escalation boundary;
- source-freshness preflight capability;
- Founder-maintenance/customer-Owner identity separation where applicable;
- repository-autonomy state;
- last bridge sync evidence.

## Founder invariant

> **The ARC runs its own domain. PRIME oversees the system of ARCs. Detailed work stays with the ARC; portfolio supervision stays with PRIME.**

> **Before an ARC consumes its direct bridge, it synchronizes its own source view safely. Stale local source must never masquerade as authoritative truth.**
