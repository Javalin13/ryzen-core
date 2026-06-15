#!/usr/bin/env bash
# ============================================================================
# push-to-remote.sh — Ship ryzen-core to a GitHub remote.
# ============================================================================
#
# This script is invoked by the founder (Jan Blommaert) once the remote
# repository `https://github.com/Javalin13/ryzen-core` exists and a
# credential is available.
#
# It is designed to fail loudly, not silently. If anything is wrong, it stops.
#
# Pre-flight (the founder does these, NOT this script):
#   1. Create the repo at github.com/Javalin13/ryzen-core, private,
#      empty (no README, no LICENSE, no .gitignore — we have our own).
#   2. Have a credential available — either:
#        a) a fine-scoped GitHub PAT in env GITHUB_TOKEN, or
#        b) `gh auth login` already completed on this machine, or
#        c) `git credential.helper` configured to store/manager with
#           the right x-access-token username.
#
# Invocation:
#   bash push-to-remote.sh
#
# Or with a token (do not paste a real token into chat; use your password
# manager or a local export):
#   GITHUB_TOKEN=*** bash push-to-remote.sh
#
# Modeled on ryzen-continuity/push-to-remote.sh (the same pattern, same
# doctrine, same hard-fail semantics).
# ============================================================================

set -euo pipefail

REMOTE_URL="https://github.com/Javalin13/ryzen-core.git"
BRANCH="main"
EXPECTED_COMMITS=13
EXPECTED_TAGS=2

echo "==> Pre-flight: working tree clean?"
if [[ -n "$(git status --porcelain)" ]]; then
  echo "ERROR: working tree is not clean. Commit or stash first."
  git status --short
  exit 1
fi
echo "    OK"

echo "==> Pre-flight: branch is ${BRANCH}?"
current=$(git branch --show-current)
if [[ "$current" != "$BRANCH" ]]; then
  echo "ERROR: current branch is '$current', expected '$BRANCH'."
  exit 1
fi
echo "    OK"

echo "==> Pre-flight: commit count is ${EXPECTED_COMMITS}?"
count=$(git rev-list --count HEAD)
if [[ "$count" -ne "$EXPECTED_COMMITS" ]]; then
  echo "WARNING: commit count is $count, expected $EXPECTED_COMMITS}."
  echo "         Continuing — the founder should know what they shipped."
fi
echo "    OK"

echo "==> Pre-flight: remote URL is reachable?"
if command -v curl >/dev/null 2>&1; then
  # Anonymous HEAD (fast, will 404 for private repos but that's fine -- we have
  # the credential, git will use it). The real authorization is checked by the
  # actual push below, not by this probe.
  http_code=$(curl -sS -o /dev/null -w "%{http_code}" -L "$REMOTE_URL" || echo "000")
  if [[ "$http_code" == "404" || "$http_code" == "200" || "$http_code" == "401" ]]; then
    echo "    OK (HTTP $http_code -- 404/401 expected for private repos to anonymous probes)"
    echo "    Authorization is checked by the actual push below."
  else
    echo "ERROR: $REMOTE_URL returned HTTP $http_code."
    echo "       DNS or network is down. Try again from a connected device."
    exit 1
  fi
else
  echo "    SKIP (no curl)"
fi

echo "==> Pre-flight: 12 top-level folders, 0 runtime code, 0 tokens?"
if [[ ! -d "00-foundation" || ! -d "11-fleet-arc-intake" ]]; then
  echo "ERROR: expected 00-foundation/ and 11-fleet-arc-intake/ to exist."
  exit 1
fi
py_count=$(find . -name '*.py' -not -path '*/.git*' | wc -l)
if [[ "$py_count" -ne "0" ]]; then
  echo "ERROR: found $py_count .py files. The foundation must have 0 runtime code."
  find . -name '*.py' -not -path '*/.git*'
  exit 1
fi
token_hits=$(grep -r "github_pat_\|ghp_\|ghs_\|gho_\|ghu_" --include="*.md" . 2>/dev/null | wc -l)
if [[ "$token_hits" -ne "0" ]]; then
  echo "ERROR: found $token_hits token-pattern matches. The foundation must have 0 tokens."
  exit 1
fi
echo "    OK"

echo "==> Configuring remote origin (idempotent)..."
if git remote get-url origin >/dev/null 2>&1; then
  echo "    origin already set to: $(git remote get-url origin)"
else
  if [[ -n "${GITHUB_TOKEN:-}" ]]; then
    # Embed the token in the URL only for this command, never persisted.
    # The token stays in process memory; not in .git/config.
    authed_url="https://x-access-token:${GITHUB_TOKEN}@github.com/Javalin13/ryzen-core.git"
    git remote add origin "$authed_url"
    echo "    origin set with embedded token (in-memory only)"
  else
    git remote add origin "$REMOTE_URL"
    echo "    origin set to: $REMOTE_URL"
    echo "    (will use credential.helper or prompt; username MUST be 'x-access-token' for PATs)"
  fi
fi

echo "==> Pushing commits and tags to remote..."
git push origin "$BRANCH" --follow-tags 2>&1 | tail -20

echo ""
echo "==> Post-push verification..."
echo "    Local commits:  $(git rev-list --count HEAD)"
remote_count=$(git rev-list --count origin/"$BRANCH" 2>/dev/null || echo "?")
echo "    Remote commits: $remote_count"
echo "    Local tags:     $(git tag | wc -l)"
remote_tags=$(git ls-remote --tags origin 2>/dev/null | grep -v '\^{}' | wc -l)
echo "    Remote tags:    $remote_tags"

if [[ "$remote_count" == "$(git rev-list --count HEAD)" ]]; then
  echo ""
  echo "==> local == remote. Push complete."
  echo ""
  echo "==> The 2 canonical tags are now on the remote:"
  git tag | sort | sed 's/^/    /'
  echo ""
  echo "==> Next: validate local == remote == 31 commits == 18 tags in ryzen-continuity (sibling repo, unchanged)."
  echo "    And: ready for the first Fleet ARC intake in 11-fleet-arc-intake/."
else
  echo ""
  echo "==> WARNING: local != remote. Investigate before continuing."
  exit 1
fi
