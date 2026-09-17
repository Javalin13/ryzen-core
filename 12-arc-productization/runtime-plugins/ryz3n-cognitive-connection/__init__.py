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
_MAX_STATES = 256

_EXACT_REPLY_RE = re.compile(r"^\s*reply\s+exactly\s*:\s*(.+?)\s*$", re.IGNORECASE | re.DOTALL)

_LOCK = threading.RLock()
_TURN_STATE: dict[tuple[str, str], dict[str, Any]] = {}


def _enabled() -> bool:
    value = os.getenv(_ENABLED_ENV, "true").strip().lower()
    return value not in {"0", "false", "no", "off", "disabled"}


def _now() -> float:
    return time.monotonic()


def _purge_locked(now: float | None = None) -> None:
    current = _now() if now is None else now
    stale = [
        key
        for key, state in _TURN_STATE.items()
        if current - float(state.get("created_at", current)) > _TTL_SECONDS
    ]
    for key in stale:
        _TURN_STATE.pop(key, None)

    while len(_TURN_STATE) > _MAX_STATES:
        oldest = min(
            _TURN_STATE,
            key=lambda key: float(_TURN_STATE[key].get("created_at", current)),
        )
        _TURN_STATE.pop(oldest, None)


def _store_turn_state(session_id: str, turn_id: str, state: dict[str, Any]) -> None:
    if not session_id or not turn_id:
        return
    with _LOCK:
        _purge_locked()
        _TURN_STATE[(session_id, turn_id)] = {
            **state,
            "created_at": _now(),
        }
        _purge_locked()


def _get_turn_state(session_id: str, turn_id: str) -> dict[str, Any] | None:
    if not session_id or not turn_id:
        return None
    with _LOCK:
        _purge_locked()
        state = _TURN_STATE.get((session_id, turn_id))
        return dict(state) if isinstance(state, dict) else None


def _latest_session_state(session_id: str) -> dict[str, Any] | None:
    if not session_id:
        return None
    with _LOCK:
        _purge_locked()
        candidates = [
            state
            for (sid, _turn_id), state in _TURN_STATE.items()
            if sid == session_id
        ]
        if not candidates:
            return None
        latest = max(candidates, key=lambda state: float(state.get("created_at", 0.0)))
        return dict(latest)


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
    """Classify only explicit exact-response requests into R0_DIRECT."""
    if not _enabled():
        return None

    exact_output = _classify_exact(kwargs.get("user_message"))
    if exact_output is None:
        return None

    session_id = str(kwargs.get("session_id") or "")
    turn_id = str(kwargs.get("turn_id") or "")
    _store_turn_state(
        session_id,
        turn_id,
        {
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
    """Block tools for a turn already classified as R0_DIRECT_EXACT."""
    if not _enabled():
        return None

    session_id = str(kwargs.get("session_id") or "")
    turn_id = str(kwargs.get("turn_id") or "")
    state = _get_turn_state(session_id, turn_id)
    if not state or state.get("lane") != "R0_DIRECT_EXACT":
        return None

    return {
        "action": "block",
        "reason": "RYZ3N R0_DIRECT_EXACT forbids tool execution for this turn.",
    }


def on_transform_llm_output(**kwargs: Any) -> str | None:
    """Enforce the exact public response for the current exact/direct turn."""
    if not _enabled():
        return None

    session_id = str(kwargs.get("session_id") or "")
    state = _latest_session_state(session_id)
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
