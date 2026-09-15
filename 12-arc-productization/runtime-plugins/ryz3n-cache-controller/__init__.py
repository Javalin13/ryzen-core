"""RYZ3N Cache Controller v0.1.2 — shadow telemetry only.

E1.21 contract:
- NEVER mutates an LLM request.
- NEVER short-circuits provider execution.
- NEVER persists prompt/response content, credentials, chat/user ids, or private memory.
- Measures stable-prefix continuity, repeated-context share, provider cache behavior,
  concurrency, latency, retries, errors, and token-estimate calibration.

Privacy invariant:
Hermes exposes ``request_messages`` as a high-sensitivity/raw observer field. This
plugin may use it transiently in-process for hashes and aggregate counts only. Raw
messages MUST NEVER be persisted, logged, printed, or returned.
"""

from __future__ import annotations

import hashlib
import json
import os
import threading
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Mapping

_LOCK = threading.Lock()
_ACTIVE = 0
_STARTS: dict[str, float] = {}
_PRE: dict[str, dict[str, Any]] = {}
_MAX_PENDING = 1024


def _now() -> str:
    return datetime.now(timezone.utc).isoformat()


def _arc_id() -> str:
    explicit = (os.environ.get("RYZ3N_ARC_ID") or "").strip()
    if explicit:
        return explicit
    low = os.environ.get("HERMES_HOME", "").lower().replace("\\", "/")
    if "/profiles/cargo" in low:
        return "cargo"
    if "/profiles/narc" in low:
        return "narc"
    if "/profiles/vonda" in low:
        return "vonda"
    return "prime"


def _telemetry_path() -> Path:
    home = Path(os.environ.get("HERMES_HOME") or (Path.home() / ".hermes"))
    path = home / "ryz3n-telemetry" / "cache-controller-shadow.jsonl"
    path.parent.mkdir(parents=True, exist_ok=True)
    return path


def _stable_json(value: Any) -> str:
    try:
        return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False, default=str)
    except Exception:
        return repr(value)


def _hash(value: Any) -> str:
    return hashlib.sha256(_stable_json(value).encode("utf-8", errors="replace")).hexdigest()


def _serialized_chars(value: Any) -> int:
    return len(_stable_json(value))


def _ratio(numerator: int | float | None, denominator: int | float | None) -> float | None:
    try:
        n = float(numerator or 0)
        d = float(denominator or 0)
        if d <= 0:
            return None
        return round(n / d, 6)
    except Exception:
        return None


def _session_hash(value: Any) -> str | None:
    if value in (None, ""):
        return None
    return _hash(str(value))[:20]


def _role(item: Any) -> str:
    if isinstance(item, Mapping):
        value = item.get("role")
    else:
        try:
            value = getattr(item, "role", None)
        except Exception:
            value = None
    return str(value or "").lower()


def _leading_stable_messages(messages: list[Any]) -> list[Any]:
    """Leading non-user provider messages, normally system/developer material."""
    stable: list[Any] = []
    for item in messages:
        if _role(item) == "user":
            break
        stable.append(item)
    return stable


def _request_measurements(kwargs: Mapping[str, Any]) -> dict[str, Any]:
    """Content-free fingerprints and aggregate repeated-context measurements."""
    context = {
        "provider": kwargs.get("provider"),
        "model": kwargs.get("model"),
        "api_mode": kwargs.get("api_mode"),
        "tool_count": kwargs.get("tool_count"),
        "max_tokens": kwargs.get("max_tokens"),
    }

    raw = kwargs.get("request_messages")
    if isinstance(raw, list):
        history = raw[:-1] if raw else []
        stable = _leading_stable_messages(raw)
        latest = raw[-1:] if raw else []

        total_chars = _serialized_chars(raw)
        history_chars = _serialized_chars(history)
        stable_chars = _serialized_chars(stable)
        latest_chars = _serialized_chars(latest)
        request_chars = kwargs.get("request_char_count")

        return {
            "request_fingerprint": _hash({"context": context, "messages": raw}),
            "history_prefix_fingerprint": _hash({"context": context, "messages": history}),
            # Lane-specific identity: useful for provider/model cache compatibility.
            "stable_prefix_fingerprint": _hash({"context": context, "messages": stable}),
            # Provider-independent identity: useful for cross-lane context reuse decisions.
            "stable_content_fingerprint": _hash({"messages": stable}),
            "fingerprint_source": "request_messages",
            "message_payload_char_count": total_chars,
            "history_prefix_char_count": history_chars,
            "stable_prefix_char_count": stable_chars,
            "latest_wire_item_char_count": latest_chars,
            "stable_prefix_message_count": len(stable),
            "dynamic_message_count": max(0, len(raw) - len(stable)),
            "stable_prefix_share_of_message_payload": _ratio(stable_chars, total_chars),
            "stable_prefix_share_of_request_chars": _ratio(stable_chars, request_chars),
        }

    request = kwargs.get("request")
    if isinstance(request, Mapping):
        structural: dict[str, Any] = {}
        for key in (
            "model", "messages", "input", "tools", "tool_choice", "max_tokens",
            "max_completion_tokens", "temperature", "top_p", "response_format",
        ):
            if key in request:
                structural[key] = request[key]
        if structural:
            return {
                "request_fingerprint": _hash({"context": context, "request": structural}),
                "history_prefix_fingerprint": None,
                "stable_prefix_fingerprint": None,
                "stable_content_fingerprint": None,
                "fingerprint_source": "sanitized_request",
            }

    return {
        "request_fingerprint": None,
        "history_prefix_fingerprint": None,
        "stable_prefix_fingerprint": None,
        "stable_content_fingerprint": None,
        "fingerprint_source": "unavailable",
    }


def _get(obj: Any, *names: str, default: int = 0) -> int:
    for name in names:
        try:
            value = obj[name] if isinstance(obj, Mapping) and name in obj else getattr(obj, name)
            if value is not None:
                return int(value)
        except Exception:
            continue
    return default


def _usage(kwargs: Mapping[str, Any]) -> dict[str, Any]:
    usage = kwargs.get("canonical_usage") or kwargs.get("usage") or kwargs.get("response_usage")
    if usage is None:
        return {}

    input_tokens = _get(usage, "input_tokens", "prompt_tokens")
    output_tokens = _get(usage, "output_tokens", "completion_tokens")
    cache_read = _get(usage, "cache_read_tokens", "cache_read_input_tokens", "cached_tokens")
    cache_write = _get(usage, "cache_write_tokens", "cache_creation_input_tokens")

    try:
        details = usage.get("prompt_tokens_details") if isinstance(usage, Mapping) else getattr(usage, "prompt_tokens_details", None)
    except Exception:
        details = None
    if details is not None:
        if not cache_read:
            cache_read = _get(details, "cached_tokens")
        if not cache_write:
            cache_write = _get(details, "cache_write_tokens", "cache_creation_input_tokens")

    total_tokens = _get(usage, "total_tokens") or (input_tokens + output_tokens)
    uncached = max(0, input_tokens - cache_read)

    return {
        "input_tokens": input_tokens,
        "cached_input_tokens": cache_read,
        "cache_write_tokens": cache_write,
        "uncached_input_tokens": uncached,
        "provider_cache_read_ratio": _ratio(cache_read, input_tokens),
        "provider_cache_write_ratio": _ratio(cache_write, input_tokens),
        "output_tokens": output_tokens,
        "total_tokens": total_tokens,
    }


def _error_class(kwargs: Mapping[str, Any]) -> str:
    status = kwargs.get("status_code")
    try:
        status_i = int(status)
    except Exception:
        status_i = None
    if status_i == 429:
        return "rate_limited"
    if status_i is not None and 500 <= status_i <= 599:
        return "provider_5xx"
    err = kwargs.get("error")
    name = type(err).__name__.lower() if err is not None else ""
    reason = str(kwargs.get("reason") or "").lower()
    joined = f"{name} {reason}"
    if "timeout" in joined:
        return "timeout"
    if "auth" in joined or status_i in (401, 403):
        return "authentication"
    if "connection" in joined or "network" in joined:
        return "network"
    return "provider_error"


def _write(event: dict[str, Any]) -> None:
    line = json.dumps(event, sort_keys=True, separators=(",", ":"), ensure_ascii=False)
    with _LOCK:
        with _telemetry_path().open("a", encoding="utf-8") as fh:
            fh.write(line + "\n")


def _base(kwargs: Mapping[str, Any], event_type: str) -> dict[str, Any]:
    return {
        "schema": "ryz3n.capacity.v0.shadow",
        "event": event_type,
        "observed_at": _now(),
        "arc_id": _arc_id(),
        "runtime": "hermes",
        "provider": kwargs.get("provider"),
        "model": kwargs.get("model"),
        "api_mode": kwargs.get("api_mode"),
        "request_id": kwargs.get("api_request_id"),
        "turn_id": kwargs.get("turn_id"),
        "task_id": kwargs.get("task_id"),
        "session_ref": _session_hash(kwargs.get("session_id")),
        "api_call_count": kwargs.get("api_call_count"),
        "retry_count": kwargs.get("retry_count"),
        "shadow_mode": True,
    }


def on_pre_api_request(**kwargs: Any) -> None:
    global _ACTIVE
    rid = str(kwargs.get("api_request_id") or "")
    measurements = _request_measurements(kwargs)
    pre = {
        "approx_input_tokens": kwargs.get("approx_input_tokens"),
        "request_char_count": kwargs.get("request_char_count"),
        "message_count": kwargs.get("message_count"),
        "tool_count": kwargs.get("tool_count"),
        **measurements,
    }

    with _LOCK:
        _ACTIVE += 1
        active = _ACTIVE
        if rid:
            _STARTS[rid] = time.monotonic()
            _PRE[rid] = pre
            if len(_PRE) > _MAX_PENDING:
                oldest = next(iter(_PRE))
                _PRE.pop(oldest, None)
                _STARTS.pop(oldest, None)

    event = _base(kwargs, "pre_api_request")
    event.update(pre)
    event.update({
        "active_concurrency_at_start": active,
        "middleware_trace_count": len(kwargs.get("middleware_trace") or []),
    })
    _write(event)


def _finish(kwargs: Mapping[str, Any], event_type: str) -> tuple[dict[str, Any], float | None]:
    global _ACTIVE
    rid = str(kwargs.get("api_request_id") or "")
    with _LOCK:
        started = _STARTS.pop(rid, None) if rid else None
        pre = _PRE.pop(rid, {}) if rid else {}
        _ACTIVE = max(0, _ACTIVE - 1)
        active_after = _ACTIVE

    elapsed_ms = round((time.monotonic() - started) * 1000.0, 3) if started is not None else None
    event = _base(kwargs, event_type)
    event["latency_ms_local"] = elapsed_ms
    event["active_concurrency_after"] = active_after
    event.update(pre)
    event.update(_usage(kwargs))

    approx = event.get("approx_input_tokens")
    actual = event.get("input_tokens")
    if actual is not None and approx:
        event["provider_vs_approx_input_ratio"] = _ratio(actual, approx)
        try:
            event["provider_minus_approx_input_tokens"] = int(actual) - int(approx)
        except Exception:
            pass
    return event, elapsed_ms


def on_post_api_request(**kwargs: Any) -> None:
    event, _ = _finish(kwargs, "post_api_request")
    event["status"] = "success"
    _write(event)


def on_api_request_error(**kwargs: Any) -> None:
    event, _ = _finish(kwargs, "api_request_error")
    event.update({
        "status": "error",
        "http_or_provider_status_class": kwargs.get("status_code"),
        "provider_error_class": _error_class(kwargs),
        "retryable": kwargs.get("retryable"),
        "max_retries": kwargs.get("max_retries"),
        "rate_limit_event": kwargs.get("status_code") == 429,
    })
    _write(event)


def register(ctx: Any) -> None:
    ctx.register_hook("pre_api_request", on_pre_api_request)
    ctx.register_hook("post_api_request", on_post_api_request)
    ctx.register_hook("api_request_error", on_api_request_error)
