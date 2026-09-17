"""RYZ3N Cognitive Connection v0.1.0.

Minimum viable, model-independent cognition/control layer.

Scope of v0.1.0:
- preserve a generic pre-gateway control seam without channel-specific behavior;
- recognize explicit exact-response requests as R0_DIRECT;
- inject a narrow no-tool/direct-response policy before the LLM call;
- block tool execution for the same exact/direct turn;
- enforce the exact public response for that turn after the tool loop completes.

Non-goals:
- no model routing changes;
- no cache/context redesign;
- no Telegram-specific commands;
- no privileged control execution before authorization;
- no broad heuristic classification of ordinary conversation yet.

The plugin keeps only short-lived process-local turn policy state and persists no
private message content.
"""

from __future__ import annotations

import os
import re
import threading
import time
from typing import Any

_VERSION = "0.1.0"
_ENABLED_ENV = "RYZ3N_COGNITIVE_CONNECTION_ENABLED"
_TTL_SECONDS = 900.0
_MAX_SESSIONS = 256

_EXACT_REPLY_RE = re.compile(r"^\s*reply\s+exactly\s*:\s*(.+?)\s*$", re.IGNORECASE | re.DOTALL)

_LOCK = threading.RLock()
_SESSION_STATE: dict[str, dict[str, Any]] = {}


def _enabled() -> bool:
    value = os.getenv(_ENABLED_ENV, "true").strip().lower()
    return value not in {"0", "false", "no", "off", "disabled"}


def _now() -> float:
    return time.monotonic()


def _purge_locked(now: float | None = None) -> None:
    current = _now() if now is None else now
    stale = [
        session_id
        for session_id, state in _SESSION_STATE.items()
        if current - float(state.get("created_at", current)) > _TTL_SECONDS
    ]
    for session_id in stale:
        _SESSION_STATE.pop(session_id, None)

    while len(_SESSION_STATE) > _MAX_SESSIONS:
        oldest = min(
            _SESSION_STATE,
            key=lambda session_id: float(
                _SESSION_STATE[session_id].get("created_at", current)
            ),
        )
        _SESSION_STATE.pop(oldest, None)


def _store_session_state(session_id: str, state: dict[str, Any]) -> None:
    if not session_id:
        return
    with _LOCK:
        _purge_locked()
        _SESSION_STATE[session_id] = {
            **state,
            "created_at": _now(),
        }
        _purge_locked()


def _get_session_state(session_id: str) -> dict[str, Any] | None:
    if not session_id:
        return None
    with _LOCK:
        _purge_locked()
        state = _SESSION_STATE.get(session_id)
        return dict(state) if isinstance(state, dict) else None


def _classify_exact(user_message: Any) -> str | None:
    if not isinstance(user_message, str):
        return None
    match = _EXACT_REPLY_RE.match(user_message)
    if not match:
        return None
    exact = match.group(1)
    return exact if exact else None


def on_pre_gateway_dispatch(**kwargs: Any) -> None:
    """Reserved generic ingress/control seam.

    v0.1.0 deliberately performs no privileged action here. This hook fires
    before Hermes authorization, so Owner-only control commands must not be
    executed from this callback until an explicit authenticated contract is
    added.
    """
    return None


def on_pre_llm_call(**kwargs: Any) -> dict[str, str] | None:
    """Classify the current turn and constrain explicit exact responses."""
    if not _enabled():
        return None

    session_id = str(kwargs.get("session_id") or "")
    turn_id = str(kwargs.get("turn_id") or "")
    exact_output = _classify_exact(kwargs.get("user_message"))

    # Always overwrite session state for the new turn so an old exact-response
    # policy can never bleed into a later ordinary turn.
    if exact_output is None:
        _store_session_state(
            session_id,
            {
                "turn_id": turn_id,
                "lane": "DEFAULT",
                "exact_output": None,
            },
        )
        return None

    _store_session_state(
        session_id,
        {
            "turn_id": turn_id,
            "lane": "R0_DIRECT_EXACT",
            "exact_output": exact_output,
        },
    )

    return {
        "context": (
            "RYZ3N COGNITIVE CONNECTION — R0_DIRECT_EXACT. "
            "This turn is an explicit exact-response request. "
            "Do not call any tool. Do not explain, expand, annotate, or emit "
            "reasoning/control markers. Return only the exact requested text."
        )
    }


def on_pre_tool_call(**kwargs: Any) -> dict[str, str] | None:
    """Block tools for the same turn when classified as R0_DIRECT_EXACT."""
    if not _enabled():
        return None

    session_id = str(kwargs.get("session_id") or "")
    turn_id = str(kwargs.get("turn_id") or "")
    state = _get_session_state(session_id)
    if not state:
        return None
    if state.get("turn_id") != turn_id:
        return None
    if state.get("lane") != "R0_DIRECT_EXACT":
        return None

    return {
        "action": "block",
        "reason": "RYZ3N R0_DIRECT_EXACT forbids tool execution for this turn.",
    }


def on_transform_llm_output(**kwargs: Any) -> str | None:
    """Enforce exact public output only for the current session's exact lane."""
    if not _enabled():
        return None

    session_id = str(kwargs.get("session_id") or "")
    state = _get_session_state(session_id)
    if not state or state.get("lane") != "R0_DIRECT_EXACT":
        return None

    exact_output = state.get("exact_output")
    if isinstance(exact_output, str) and exact_output:
        return exact_output
    return None


def register(ctx: Any) -> None:
    ctx.register_hook("pre_gateway_dispatch", on_pre_gateway_dispatch)
    ctx.register_hook("pre_llm_call", on_pre_llm_call)
    ctx.register_hook("pre_tool_call", on_pre_tool_call)
    ctx.register_hook("transform_llm_output", on_transform_llm_output)
