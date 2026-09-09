# RYZ3N Constitution Compliance Gate

Status: Founder-directed architectural control
Date: 2026-09-09
Scope: PRIME-mediated ARC prototypes, autonomous ARC nodes, VONDA ARC, future ARC productization

## Constitutional authority

The canonical files in `Javalin13/ryzen-continuity` are treated as the constitution of the RYZ3N ecosystem. They are not implementation suggestions.

Primary constitutional references:

- `00-governance/INTERPRETATION-PROTOCOL.md`
- `02-ryzen/RYZEN-CANONICAL.md`
- `02-ryzen/architecture/HIERARCHY.md`
- `02-ryzen/architecture/CONVERGENCE-LAYER.md`
- `03-hermes/RELATIONSHIP-TO-RYZEN.md`

This file does not amend those canonicals. It operationalizes a compliance gate for prototype engineering and ARC runtime implementation.

## Constitutional invariants

Every ARC implementation, PRIME orchestration pattern, Hermes runtime pattern, Telegram adapter, memory model, provisioning flow, migration mechanism and future RYZ3N runtime design must preserve all of the following:

1. Founder remains source of strategic intent and final authority.
2. RYZ3N remains the ecosystem architecture itself, not a product, service, repository, model or Hermes runtime.
3. Canonical hierarchy remains `Creator → RYZ3N → ARCs → Brains → Agents → Execution`.
4. ARCs hold domain framing; they do not become execution agents merely because a runtime is attached to them.
5. Brains reason; Agents execute; Execution touches reality.
6. Hermes serves RYZ3N. Hermes is operational infrastructure, not the ecosystem architecture.
7. PRIME is not an ARC. PRIME is a current operational/supervisory execution arm used to bootstrap, supervise and verify prototype runtime patterns.
8. Information must flow upward as well as downward: execution evidence, decisions, lessons and drift must be able to converge back toward RYZ3N and the Founder.
9. Convergence is additive/read-mostly. Prototype evidence may propose updates; it must not silently rewrite canonical truth.
10. Drift must be surfaced, not normalized.
11. Hermes/PRIME may operationalize governance but may not invent strategic intent or silently redefine architecture.
12. Canonical change requires the canonical amendment/versioning process.

## The constitutional three-pass check

The canonical Interpretation Protocol establishes three operational rules:

1. Reality takes precedence over doctrine.
2. Implementation takes precedence over aspiration.
3. Evidence takes precedence over theory.

For ARC engineering these become a mandatory three-pass verification gate. This is an operationalization of those three canonical rules, not an amendment to the canonical text.

### PASS 1 — REALITY CHECK

Question: **What is actually true on the running system right now?**

Verify observable state directly where possible:

- process/service identity;
- active profile/runtime;
- filesystem and memory boundaries;
- gateway/channel binding;
- permissions and secrets boundaries;
- isolation behavior;
- logs/checkpoints/state;
- current activation/dormancy state;
- actual user-visible behavior when live.

No design document may substitute for this pass.

Output must distinguish:

- observed fact;
- unknown/unobserved state;
- failed state;
- stale documentation.

### PASS 2 — IMPLEMENTATION CHECK

Question: **Does the implementation match the Founder-approved architecture and scope?**

Compare observed reality against:

- Founder intent;
- the constitutional hierarchy;
- the approved ARC productization/runtime design;
- client-specific scope and boundaries;
- current mission and activation gate.

A capability that exists but violates the architecture is not a success. It is drift.

A capability that is designed but not implemented must remain marked as designed/planned, never reported as real.

### PASS 3 — EVIDENCE CHECK

Question: **Can every material claim be proven?**

Require evidence appropriate to the claim, such as:

- verifier/test output;
- service/process state;
- exact file path and current content;
- configuration proof without exposing secrets;
- restart/isolation test;
- negative test / fail-closed test;
- checkpoint/recovery test;
- explicit client/Founder decision where required.

A claim without evidence is not promoted to reality.

## Final-state recheck

The three passes are not only pre-change review. After any material implementation, migration, activation, configuration change or rollback, run the three passes again on the final state.

Required pattern:

`intent → implement → PASS 1 reality → PASS 2 implementation alignment → PASS 3 evidence → final-state confirmation`

If any pass fails:

- do not declare READY;
- preserve evidence;
- classify the drift/failure;
- surface it to PRIME/Founder;
- correct or explicitly defer it;
- rerun all three passes from the beginning.

## VONDA / PRIME application

VONDA ARC must operate according to the RYZ3N constitution as implemented through PRIME supervision.

Current prototype runtime view:

`Founder intent → PRIME supervision/control plane → autonomous VONDA Hermes runtime node → VONDA reasoning/workflow components → agents/adapters → execution`

This runtime view must not replace the canonical ontology. It is the practical implementation mirror used to prove the future RYZ3N ↔ ARC operating model.

PRIME must therefore:

- supervise VONDA without becoming VONDA;
- preserve VONDA autonomous runtime identity;
- verify isolation and boundaries;
- maintain upward reporting of evidence, lessons and drift;
- keep client-private content inside VONDA boundaries;
- generalize only reusable patterns;
- classify reality/design/vision correctly;
- run the three-pass check before and after material VONDA changes.

## Readiness rule

No ARC may be reported as `READY`, `LIVE`, `MIGRATED`, `RECOVERED`, or `COMPLIANT` unless all three passes are green on the final state.

A final readiness report must contain:

- PASS 1 — REALITY: PASS/FAIL + evidence summary
- PASS 2 — IMPLEMENTATION: PASS/FAIL + architecture comparison
- PASS 3 — EVIDENCE: PASS/FAIL + proof references
- DRIFT: none / listed
- FINAL STATE: exact classification (dormant / prepared / live / degraded / rolled-back)
- FOUNDER GATES: pending/completed

## Engineering principle

> The constitution is the invariant. PRIME is the current practical interpreter/operator. VONDA is the proving node. Reality, implementation and evidence must agree before a claim becomes true.
