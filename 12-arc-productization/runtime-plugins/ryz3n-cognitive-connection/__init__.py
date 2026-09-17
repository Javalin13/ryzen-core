"""RYZ3N Cognitive Connection v0.3.1.

Minimum viable, model-independent cognition/control layer.

Scope of v0.3.1:
- preserve a generic pre-gateway control seam without channel-specific behavior;
- recognize explicit exact-response requests as R0_DIRECT_EXACT;
- recognize explicit no-tool requests as R1_DIRECT_NO_TOOL;
- inject narrow direct-response policy before the LLM call;
- enforce generic epistemic integrity for no-tool turns;
- block tool execution for exact/no-tool turns;
- remove provider tool schemas from request-local R0/R1 payloads;
- enforce exact public response for R0 turns;
- collapse runaway repetitive output for bounded R1 direct/no-tool turns.

Non-goals:
- no model routing changes;
- no cache/context redesign;
- no Telegram-specific commands;
- no privileged control execution before authorization;
- no broad heuristic classification of ordinary conversation yet.

The plugin keeps only short-lived process-local turn policy state and persists no
private message content. Request-local tool suppression never mutates agent.tools
or the canonical Hermes tool registry.
"""

from __future__ import annotations

import os
import re
import threading
import time
from difflib import SequenceMatcher
from typing import Any

_VERSION = "0.3.1"
_ENABLED_ENV = "RYZ3N_COGNITIVE_CONNECTION_ENABLED"
_TTL_SECONDS = 900.0
_MAX_SESSIONS = 256
_BRIEF_MAX_CHARS = 1800

_EXACT_REPLY_RE = re.compile(r"^\s*reply\s+exactly\s*:\s*(.+?)\s*$", re.IGNORECASE | re.DOTALL)
_NO_TOOL_RE = re.compile(
    r"\b(?:without\s+using\s+(?:any\s+)?tools?|do\s+not\s+use\s+(?:any\s+)?tools?|don't\s+use\s+(?:any\s+)?tools?|no\s+tools?)\b",
    re.IGNORECASE,
)
_BRIEF_RE = re.compile(r"\b(?:brief|briefly|short|concise|concisely)\b", re.IGNORECASE)
_TOOL_REQUEST_KEYS = (
    "tools",
    "tool_choice",
    "parallel_tool_calls",
    "functions",
    "function_call",
)

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


def _explicit_no_tool(user_message: Any) -> bool:
    return isinstance(user_message, str) and bool(_NO_TOOL_RE.search(user_message))


def _brief_requested(user_message: Any) -> bool:
    return isinstance(user_message, str) and bool(_BRIEF_RE.search(user_message))


def _normalize_unit(text: str) -> str:
    return re.sub(r"\s+", " ", re.sub(r"[^a-z0-9\s]", " ", text.lower())).strip()


def _near_duplicate(candidate: str, prior: str) -> bool:
    if candidate == prior:
        return True
    if len(candidate) < 24 or len(prior) < 24:
        return False
    return SequenceMatcher(None, candidate, prior).ratio() >= 0.82


def _collapse_repetitive_output(text: str) -> str:
    """Keep the first sufficient answer and stop when a repetition loop begins.

    This is deliberately conservative and only used on explicit bounded
    direct/no-tool turns. Two consecutive near-duplicate units are treated as
    evidence that the model has entered a restatement loop.
    """
    stripped = text.strip()
    if not stripped:
        return stripped

    units = [
        unit.strip()
        for unit in re.split(r"(?<=[.!?])(?:\s+|\n+)|\n{2,}", stripped)
        if unit and unit.strip()
    ]
    if len(units) < 3:
        return stripped

    kept: list[str] = []
    seen: list[str] = []
    consecutive_repeats = 0

    for unit in units:
        normalized = _normalize_unit(unit)
        if not normalized:
            continue

        is_repeat = any(
            _near_duplicate(normalized, prior)
            for prior in seen[-8:]
        )

        if is_repeat:
            consecutive_repeats += 1
            if consecutive_repeats >= 2:
                break
            continue

        consecutive_repeats = 0
        kept.append(unit)
        seen.append(normalized)

    return " ".join(kept).strip() if kept else stripped


def _truncate_brief_output(text: str) -> str:
    if len(text) <= _BRIEF_MAX_CHARS:
        return text
    candidate = text[:_BRIEF_MAX_CHARS].rstrip()
    boundary = max(candidate.rfind(". "), candidate.rfind("? "), candidate.rfind("! "))
    if boundary >= _BRIEF_MAX_CHARS // 2:
        return candidate[: boundary + 1].rstrip()
    return candidate.rstrip() + "…"


def _state_for_turn(session_id: str, turn_id: str) -> dict[str, Any] | None:
    state = _get_session_state(session_id)
    if not state:
        return None
    if state.get("turn_id") != turn_id:
        return None
    return state


def on_pre_gateway_dispatch(**kwargs: Any) -> None:
    """Reserved generic ingress/control seam.

    v0.3.1 deliberately performs no privileged action here. This hook fires
    before Hermes authorization, so Owner-only control commands must not be
    executed from this callback until an explicit authenticated contract is
    added.
    """
    return None


def on_pre_llm_call(**kwargs: Any) -> dict[str, str] | None:
    """Classify the current turn and apply the smallest sufficient policy."""
    if not _enabled():
        return None

    session_id = str(kwargs.get("session_id") or "")
    turn_id = str(kwargs.get("turn_id") or "")
    user_message = kwargs.get("user_message")
    exact_output = _classify_exact(user_message)

    if exact_output is not None:
        _store_session_state(
            session_id,
            {
                "turn_id": turn_id,
                "lane": "R0_DIRECT_EXACT",
                "exact_output": exact_output,
                "brief_requested": True,
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

    if _explicit_no_tool(user_message):
        brief = _brief_requested(user_message)
        _store_session_state(
            session_id,
            {
                "turn_id": turn_id,
                "lane": "R1_DIRECT_NO_TOOL",
                "exact_output": None,
                "brief_requested": brief,
            },
        )
        return {
            "context": (
                "RYZ3N COGNITIVE CONNECTION — R1_DIRECT_NO_TOOL. "
                "The user explicitly forbids tool use for this turn. "
                "Answer once, directly and sufficiently from available knowledge. "
                "Maintain epistemic integrity: never present a time-sensitive, live, current, "
                "or externally changing fact as known unless it is explicitly supported by "
                "evidence already available in the current conversation/runtime context. "
                "If the answer depends on fresh external state and tools are forbidden, say "
                "that it cannot be known or verified with certainty from the current evidence "
                "and identify the kind of live source or evidence required. Do not guess, "
                "fabricate, or present an unsupported current value as fact. "
                "Do not restate the same conclusion in alternate wording. "
                "Stop when the answer is complete. "
                + ("The user asked for a brief answer, so keep it compact." if brief else "")
            )
        }

    # Always overwrite session state for an ordinary new turn so a prior lane
    # can never bleed into later conversation.
    _store_session_state(
        session_id,
        {
            "turn_id": turn_id,
            "lane": "DEFAULT",
            "exact_output": None,
            "brief_requested": False,
        },
    )
    return None


def on_llm_request_middleware(**kwargs: Any) -> dict[str, Any] | None:
    """Remove tool schemas from request-local payloads for R0/R1 turns only.

    Hermes passes a copy of the final provider kwargs into request middleware.
    Returning a replacement request changes only this provider call; the agent's
    canonical tool registry remains available for later R2+ turns.
    """
    if not _enabled():
        return None

    session_id = str(kwargs.get("session_id") or "")
    turn_id = str(kwargs.get("turn_id") or "")
    state = _state_for_turn(session_id, turn_id)
    if not state or state.get("lane") not in {"R0_DIRECT_EXACT", "R1_DIRECT_NO_TOOL"}:
        return None

    request = kwargs.get("request")
    if not isinstance(request, dict):
        return None

    if not any(key in request for key in _TOOL_REQUEST_KEYS):
        return None

    narrowed = dict(request)
    removed: list[str] = []
    for key in _TOOL_REQUEST_KEYS:
        if key in narrowed:
            narrowed.pop(key, None)
            removed.append(key)

    return {
        "request": narrowed,
        "action": "strip_tool_schemas",
        "reason": "RYZ3N selected a direct no-tool lane for this turn.",
        "metadata": {
            "lane": state.get("lane"),
            "removed_request_keys": removed,
        },
    }


def on_pre_tool_call(**kwargs: Any) -> dict[str, str] | None:
    """Block tools for the same turn when the selected lane forbids them."""
    if not _enabled():
        return None

    session_id = str(kwargs.get("session_id") or "")
    turn_id = str(kwargs.get("turn_id") or "")
    state = _state_for_turn(session_id, turn_id)
    if not state:
        return None
    if state.get("lane") not in {"R0_DIRECT_EXACT", "R1_DIRECT_NO_TOOL"}:
        return None

    return {
        "action": "block",
        "reason": "RYZ3N selected a no-tool direct lane for this turn.",
    }


def on_transform_llm_output(**kwargs: Any) -> str | None:
    """Apply the public-output contract for the current bounded direct lane."""
    if not _enabled():
        return None

    session_id = str(kwargs.get("session_id") or "")
    turn_id = str(kwargs.get("turn_id") or "")
    state = _get_session_state(session_id)
    if not state:
        return None
    if turn_id and state.get("turn_id") and state.get("turn_id") != turn_id:
        return None

    if state.get("lane") == "R0_DIRECT_EXACT":
        exact_output = state.get("exact_output")
        if isinstance(exact_output, str) and exact_output:
            return exact_output
        return None

    if state.get("lane") != "R1_DIRECT_NO_TOOL":
        return None

    response_text = kwargs.get("response_text")
    if not isinstance(response_text, str) or not response_text.strip():
        return None

    bounded = _collapse_repetitive_output(response_text)
    if state.get("brief_requested"):
        bounded = _truncate_brief_output(bounded)

    return bounded if bounded and bounded != response_text else None


def register(ctx: Any) -> None:
    ctx.register_hook("pre_gateway_dispatch", on_pre_gateway_dispatch)
    ctx.register_hook("pre_llm_call", on_pre_llm_call)
    ctx.register_hook("pre_tool_call", on_pre_tool_call)
    ctx.register_hook("transform_llm_output", on_transform_llm_output)
    ctx.register_middleware("llm_request", on_llm_request_middleware)
