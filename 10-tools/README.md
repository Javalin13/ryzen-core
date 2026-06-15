# 10-tools/ — Repository Tools

```yaml
---
type: tools
status: foundation-only
created: 2026-06-15
classification: approved-architecture
amendable: true-additively
```

## Purpose

This directory contains the **repository tools** — scripts and utilities that make this repository work. Tools are *operational* (they run, they don't document).

## The Tools

At the foundation stage, no tools are required. The first tool will be `push-to-remote.sh` (modeled on the continuity repo's `push-to-remote.sh`), which will be added when the founder creates the GitHub remote and provisions a credential.

## Future Tools (planned)

| Tool | Purpose | Phase |
|---|---|---|
| `push-to-remote.sh` | Push local commits and tags to the remote | R1 (when remote is created) |
| `verify-doctrine-compliance.sh` | Run the 17 doctrine compliance checks on the repo | R1 |
| `update-classification-index.sh` | Regenerate the runtime classification index from file frontmatter | R1 |
| `verify-no-runtime-code.sh` | Verify that no runtime code exists in the foundation (closes the "do not implement" boundary) | Foundation (will be added after the first commit) |
| `run-reality-check.sh` | Run the Founder Reality Check Protocol's 7-dimension scorecard against a new idea | R1 |
| `test-scaffolding-readiness.sh` | Verify that all scaffolding placeholders have explicit "NOT IMPLEMENTED" READMEs | Foundation (will be added after the first commit) |

## The "DO NOT IMPLEMENT" Boundary

The tools directory is *not* part of the runtime. It is *part of* the foundation. Tools are scripts that the founder (or the team) runs locally; they are not the runtime itself. The runtime is in `07-runtime-scaffolding/`.

## Cross-References

- `Javalin13/ryzen-continuity/blob/main/push-to-remote.sh` — the continuity repo's push tool (the model for `push-to-remote.sh` here)
- `Javalin13/ryzen-continuity/blob/main/10-lessons-learned/2026-06-15-fix-wrong-credential-username.md` — the lesson about credential username
- `Javalin13/ryzen-continuity/blob/main/10-lessons-learned/2026-06-15-relax-push-preflight-for-private-repos.md` — the lesson about private-repo pre-flight
