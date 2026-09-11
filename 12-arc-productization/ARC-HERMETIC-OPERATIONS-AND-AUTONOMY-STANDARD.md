# ARC Hermetic Operations & Autonomy Standard

```yaml
---
type: arc-hermetic-operations-autonomy-standard
status: founder-directed-current-model
created: 2026-09-11
classification: implementation-standard + runtime-governance
scope: ARC runtime isolation, autonomous repository writes, user-facing boundary, recovery reproducibility, multi-writer coordination
constitutional_status: non-canon implementation standard; does not amend Constitution/Canons
related:
  - 12-arc-productization/ARC-REPOSITORY-OWNERSHIP-AND-SOURCE-BOUNDARY-STANDARD.md
  - 12-arc-productization/OMEGA-ARC-FACTORY-STEWARDSHIP-STANDARD.md
  - 12-arc-productization/ARC-SELF-PROVISIONING-BRAIN-LIFECYCLE.md
---
```

## Founder decision

An ARC must be **hermetically bounded**: its source, runtime state, credentials, user identities, persistent namespaces and autonomous write authority must fit together without hidden cross-ARC dependencies.

The user interacts with the ARC. PRIME/OMEGA/FACTORY remain backend stewardship infrastructure.

Canonical shorthand:

> **One ARC, one authoritative domain source, one isolated runtime identity, one explicit permission boundary, no hidden cross-ARC dependency, no unsafe shared-writer push.**

This standard is additive implementation architecture. It does **not** rewrite, version or amend protected Constitution/Canon files. Any Canon change still requires a separate explicit Founder request and approval.

## 1. Hermetic runtime boundary

Each ARC runtime must be reconstructible without reading another ARC's private runtime files.

Required:

- own runtime/profile boundary;
- own secrets/credential boundary;
- own identity/binding state;
- own pending-candidate state;
- own task/memory/Brain namespaces;
- own logs/checkpoints/recovery state;
- own channel credential(s);
- own versioned ARC-specific runtime implementation source in the authoritative domain repository.

Forbidden by default:

- reading another ARC's config, state database, binding file, memory namespace or secret as a convenience shortcut;
- symlinking private runtime state between ARCs;
- using another ARC's identity binding as authorization;
- copying another Owner's private payload into a new ARC.

If a future cross-ARC interaction is genuinely needed, it must use an explicit, scoped interoperability contract and privacy-safe payload. Direct filesystem coupling is not an interoperability contract.

## 2. Complete runtime-source closure

Every ARC-specific runtime component required for recovery must have durable source in the ARC's authoritative repository.

The runtime-source manifest must enumerate every ARC-specific component that is required to reproduce behavior, including as applicable:

- identity plugin;
- onboarding/binding plugin;
- task/memory plugin;
- telemetry/health plugin;
- launch/recovery scripts;
- autonomous Git-write guard/wrapper;
- configuration templates that contain no secrets.

For each component record:

- logical name;
- repository source path;
- deployed runtime path;
- cryptographic hash;
- source version/status;
- deployment/recovery rule.

A VPS-only edit is not durable source truth. A runtime may be GREEN while a fix is being proven, but the defect is not permanently closed until the exact working implementation is reproducible from the authoritative repository.

## 3. User-facing ARC / hidden steward boundary

Customer/co-founder/end-user onboarding happens through the ARC's own approved channel.

Users do not install or operate PRIME merely to use their ARC.

Reference flow:

```text
User channel
  ↓
ARC
  ↓
ARC runtime
  ↓
PRIME/operator approval + OMEGA/FACTORY stewardship behind the scenes
```

Client-facing responses must not expose:

- internal role IDs;
- numeric sender IDs;
- pairing/binding machinery;
- namespace names;
- runtime/profile paths;
- gateway process details;
- operator scaffolding;
- cross-ARC implementation details.

Natural identity recognition is allowed after valid binding. Internal identity state remains server-side authority.

## 4. Fail-closed multi-candidate onboarding

Unknown senders remain fail-closed.

Pending identity capture must be safe for more than one simultaneous unknown sender. An implementation must not rely on one mutable global "latest candidate" record that can be silently overwritten by another sender.

Preferred pattern:

```text
state/pending_candidates/<runtime-candidate-key>.json
```

or an equivalent database table keyed by immutable runtime identity.

Rules:

- no first-unknown auto-bind;
- each candidate is isolated from every other candidate;
- binding requires explicit selection of the exact candidate + intended role;
- approval must never mean "bind whichever candidate arrived last";
- consumed/rejected candidates remain auditable or are safely archived according to retention policy;
- numeric/private identifiers stay in protected runtime state, never ordinary Git evidence.

## 5. ARC own-repository autonomy

An ARC may autonomously read and write its **own authoritative repository** when the Founder/Owner has granted that authority.

Once granted, that authority is **continuous**. It does not require per-read, per-edit, per-commit or per-push approval from PRIME. Within its own authoritative repository, the ARC may inspect, create, edit, move and delete repository content and may commit/push those changes as part of normal domain operation, subject to the repository's integrity/concurrency controls below.

The distinction is critical:

> **Autonomy is the permission boundary. The safe-writer is integrity plumbing, not an approval gate.**

A hermetic-seal audit may report defects and block a claim of `hermetic_seal = GREEN`, but a known red/in-progress seal must **not** revoke an already granted ARC's own-repository read/write authority or prevent the ARC from committing the fixes required to become GREEN.

The autonomy grant does not permit writes to:

- `ryzen-core`;
- PRIME/OMEGA/FACTORY repositories;
- another ARC/customer/domain repository;
- another RYZ3N-owned product repository;
- Constitution/Canon files.

Cross-repository changes remain operator/steward work unless separately and explicitly authorized.

Every autonomous ARC write must be transparent to its authorized user/operator in the next user-facing response with at least:

- resulting commit SHA;
- branch;
- files changed;
- concise purpose/result;
- conflict/rebase/divergence state;
- explicit fallback disclosure if a normal ARC tool failed and Git was used instead.

## 6. Safe shared-writer Git transaction

When an ARC and PRIME/operator can both write the ARC's repository, direct `main` writes use optimistic-concurrency safety to protect both writers **without suspending ARC ownership of its own repository**.

Required transaction:

1. **Start synchronized.** Before a commit/push transaction, fetch `origin/main`. Local HEAD must equal the fetched remote HEAD. If not, stop and surface divergence.
2. **Record base SHA.** Treat that remote HEAD as the write transaction base.
3. **Bound the change.** Commit only the intended ARC-owned files. Do not silently absorb unrelated dirty-tree changes.
4. **Run applicable integrity/audit/tests before commit.** Checks relevant to the intended change should run. A known, separately tracked hermetic-seal blocker does not automatically prohibit an ARC from committing a change intended to repair that blocker.
5. **Re-fetch before commit/push.** If remote `main` changed from the recorded base, abort autonomous push and hand off to operator coordination. Do not silently rebase/merge concurrent operator work.
6. **Commit locally.** Record the resulting SHA.
7. **Re-fetch immediately before push.** Remote must still equal the transaction base/expected parent.
8. **Push without force.** Force push, `--force-with-lease`, destructive reset of remote history, or history rewrite is forbidden for autonomous ARC writes.
9. **Verify remote.** Fetch again and confirm `origin/main` resolves to the new commit.
10. **Verify CI.** Required coherence/integrity checks run after the push. A red hermetic-seal check means the seal remains unresolved; it does not retroactively invalidate the ARC's authority to its own repository. Newly introduced regressions must be reported and repaired.
11. **Report transparently.** Return the commit receipt to the user/operator.

Race protection is layered: even if remote changes between the last fetch and push, the normal non-force Git push must reject the non-fast-forward update.

Automatic rebase of a concurrent shared-main conflict is not the default. Stop, report and let the operator reconcile unless an ARC-specific safe auto-rebase policy has later been explicitly approved.

## 7. Branch protection / platform enforcement

Where the hosting plan and repository permissions support it, additionally require:

- protected default branch;
- required ARC coherence CI;
- force-push prohibition;
- deletion prohibition;
- review/CODEOWNERS rules where appropriate.

If platform branch-protection/rulesets are unavailable, the repository must compensate with:

- safe-write wrapper/protocol;
- CI coherence checks;
- explicit no-force rule;
- post-push verification;
- commit transparency;
- OMEGA/PRIME drift detection.

Lack of a paid platform enforcement feature does not permit unsafe autonomous writes.

## 8. Source-driven recovery / clean-room drill

An ARC is not hermetically recoverable merely because its current gateway can restart.

The authoritative repository must be sufficient to reconstruct ARC-specific runtime implementation into a clean target profile when combined with protected runtime secrets/state backups that are intentionally outside Git.

Before calling a production ARC hermetically sealed, prove at least:

- every required ARC-specific source component is represented in the runtime manifest;
- manifest hashes match repository source;
- a clean temporary reconstruction can deploy all versioned ARC runtime code without reading another ARC's runtime directory;
- modules/configuration validate in the reconstructed boundary;
- the live ARC can then restart from the same versioned source path without losing authorized bindings/state;
- unknown identities remain fail-closed after restart;
- privacy/isolation checks remain GREEN.

A clean-room reconstruction must not duplicate a live Telegram poller with the same token. Reconstruct code/configuration safely, then use the normal controlled live restart for end-to-end channel verification.

## 9. OMEGA / FACTORY duties

OMEGA tracks whether each ARC is:

- source-boundary coherent;
- runtime-source complete;
- hermetically isolated;
- autonomy-authorized or not;
- safe-writer compliant;
- recovery-tested;
- onboarding/privacy compliant.

FACTORY stores the lifecycle/result and evidence pointers, not private runtime payload.

Material violations escalate to PRIME:

- cross-ARC runtime file read/write;
- unknown auto-binding;
- candidate overwrite/ambiguity;
- unversioned runtime component;
- force push/history rewrite;
- autonomous cross-repo modification;
- CI bypass;
- client-facing disclosure of internal identity/binding scaffolding;
- recovery requiring another ARC's private state.

## 10. Future ARC birth inheritance

Every future ARC created from the reusable blueprint inherits this standard.

At birth, Factory must determine:

- authoritative repository;
- runtime profile boundary;
- full runtime-source manifest location;
- user-facing channel/onboarding contract;
- autonomy state (`disabled` by default unless granted);
- safe-write mechanism if autonomy is granted;
- pending-candidate model;
- recovery drill path;
- OMEGA/FACTORY hermetic-seal status.

Once autonomy is granted, Factory/OMEGA record it as an active standing authority until explicitly revoked or changed by the Founder/Owner; ordinary audit state does not silently revoke it.

Do not retrofit these after commercial launch if they can be initialized during birth.

## Founder shorthand

> **The ARC owns its domain and, when granted autonomy, continuously owns read/write operation of its own repository. It never gains another ARC's home by implication. Shared Git writers coordinate through fail-safe optimistic concurrency; that safety mechanism protects autonomy rather than replacing it. PRIME stays behind the curtain. Recovery comes from source, not from hidden VPS history.**
