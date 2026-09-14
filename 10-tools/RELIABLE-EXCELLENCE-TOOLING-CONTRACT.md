# RYZ3N Tooling Contract — Reliable Excellence

Date: 2026-09-14  
Status: **ACTIVE / TOOLING QUALITY CONTRACT**

Governing invariant:
`00-foundation/RELIABLE-EXCELLENCE-ARCHITECTURAL-INVARIANT.md`

## Rule

Internal RYZ3N tools, scripts and automation inherit Reliable Excellence too.

A tool is not exempt merely because it is internal. Unreliable internal tooling can corrupt source, evidence, deployments, Factory output or operator trust and therefore propagate unreliability into the entire architecture.

## Expectations

Where material to the tool's purpose, tooling should favor:

- deterministic/repeatable behavior;
- explicit inputs and outputs;
- validation before destructive or externally visible action;
- idempotency or safe replay where applicable;
- bounded retries and avoidance of retry storms;
- clear partial-failure reporting;
- non-destructive defaults;
- source/state integrity;
- useful diagnostics/logging;
- testability;
- rollback/recovery when the tool mutates important state;
- current evidence/receipts after material changes;
- no false success when a downstream action failed.

## Quality rule

Automation must not turn a manual defect into a faster automated defect.

A recurring manual process should be automated only in a way that preserves or raises the reliability of the outcome.

## Standing red thread

**Know-how → High-Quality Execution → Verification → Proven Reliability → Reliable Excellence**
