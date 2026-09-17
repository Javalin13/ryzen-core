"""RYZ3N Cache Controller v0.1.7 — shadow telemetry only.

E1.22 contract:
- NEVER mutates an LLM request.
- NEVER short-circuits provider execution.
- NEVER persists prompt/response content, credentials, chat/user ids, or private memory.
- Measures the provider-facing repeated prefix separately from Hermes' own
  registered cross-session-stable system-prompt prefix.
- Measures provider cache behavior, concurrency, latency, retries, errors,
  and token-estimate calibration.

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


def _hash_text(value: str) -> str:
    return hashlib.sha256(value.encode("utf-8", errors="replace")).hexdigest()


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


def _message_content(item: Any) -> Any:
    if isinstance(item, Mapping):
        return item.get("content")
    try:
        return getattr(item, "content", None)
    except Exception:
        return None


def _content_text(content: Any) -> str | None:
    """Return text transiently for measurement; callers must never persist it."""
    if isinstance(content, str):
        return content
    if isinstance(content, list):
        chunks: list[str] = []
        for block in content:
            if isinstance(block, Mapping):
                text = block.get("text")
                if isinstance(text, str):
                    chunks.append(text)
            else:
                text = getattr(block, "text", None)
                if isinstance(text, str):
                    chunks.append(text)
        if chunks:
            return "".join(chunks)
    return None


def _leading_stable_messages(messages: list[Any]) -> list[Any]:
    """Legacy provider-facing prefix: leading messages before the first user turn."""
    stable: list[Any] = []
    for item in messages:
        if _role(item) == "user":
            break
        stable.append(item)
    return stable


def _hermes_registered_prefix_measurements(messages: list[Any]) -> dict[str, Any]:
    """Measure Hermes' own registered stable system-prefix boundary.

    ``agent.prompt_cache_boundary.find_stable_prefix`` returns a prefix already
    registered by Hermes' prompt builder/cache machinery.  We use the returned
    text only transiently to count/hash it; no prompt text is persisted.
    """
    system_text: str | None = None
    for item in messages:
        if _role(item) == "system":
            system_text = _content_text(_message_content(item))
            break

    if not system_text:
        return {
            "hermes_system_message_char_count": None,
            "hermes_registered_stable_prefix_found": False,
            "hermes_registered_stable_prefix_char_count": None,
            "hermes_registered_stable_prefix_fingerprint": None,
            "hermes_nonstable_system_tail_char_count": None,
            "hermes_registered_stable_share_of_system_message": None,
        }

    found: str | None = None
    try:
        from agent.prompt_cache_boundary import find_stable_prefix
        candidate = find_stable_prefix(system_text)
        if isinstance(candidate, str) and candidate and system_text.startswith(candidate):
            found = candidate
    except Exception:
        found = None

    system_chars = len(system_text)
    if found is None:
        return {
            "hermes_system_message_char_count": system_chars,
            "hermes_registered_stable_prefix_found": False,
            "hermes_registered_stable_prefix_char_count": None,
            "hermes_registered_stable_prefix_fingerprint": None,
            "hermes_nonstable_system_tail_char_count": None,
            "hermes_registered_stable_share_of_system_message": None,
        }

    stable_chars = len(found)
    return {
        "hermes_system_message_char_count": system_chars,
        "hermes_registered_stable_prefix_found": True,
        "hermes_registered_stable_prefix_char_count": stable_chars,
        "hermes_registered_stable_prefix_fingerprint": _hash_text(found),
        "hermes_nonstable_system_tail_char_count": max(0, system_chars - stable_chars),
        "hermes_registered_stable_share_of_system_message": _ratio(stable_chars, system_chars),
    }


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
        provider_prefix = _leading_stable_messages(raw)
        latest = raw[-1:] if raw else []

        total_chars = _serialized_chars(raw)
        history_chars = _serialized_chars(history)
        provider_prefix_chars = _serialized_chars(provider_prefix)
        latest_chars = _serialized_chars(latest)
        request_chars = kwargs.get("request_char_count")

        hermes_boundary = _hermes_registered_prefix_measurements(raw)

        return {
            "request_fingerprint": _hash({"context": context, "messages": raw}),
            "history_prefix_fingerprint": _hash({"context": context, "messages": history}),
            # Legacy field retained for evidence continuity. Semantics are the
            # provider-facing leading pre-user message prefix, not Hermes' own
            # internal cross-session stable tier.
            "stable_prefix_fingerprint": _hash({"context": context, "messages": provider_prefix}),
            "stable_content_fingerprint": _hash({"messages": provider_prefix}),
            "fingerprint_source": "request_messages",
            "message_payload_char_count": total_chars,
            "history_prefix_char_count": history_chars,
            "stable_prefix_char_count": provider_prefix_chars,
            "latest_wire_item_char_count": latest_chars,
            "stable_prefix_message_count": len(provider_prefix),
            "dynamic_message_count": max(0, len(raw) - len(provider_prefix)),
            "stable_prefix_share_of_message_payload": _ratio(provider_prefix_chars, total_chars),
            "stable_prefix_share_of_request_chars": _ratio(provider_prefix_chars, request_chars),
            # Explicit names remove ambiguity introduced by the original field.
            "provider_leading_prefix_char_count": provider_prefix_chars,
            "provider_leading_prefix_share_of_message_payload": _ratio(provider_prefix_chars, total_chars),
            "provider_leading_prefix_share_of_request_chars": _ratio(provider_prefix_chars, request_chars),
            **hermes_boundary,
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



def _builder_tier_measurements(kwargs: Mapping[str, Any]) -> dict[str, Any]:
    """Consume provider-independent content-free system-prompt builder metrics."""
    raw = kwargs.get("system_prompt_builder_tier_metrics")
    full = kwargs.get("system_prompt")

    full_chars = len(full) if isinstance(full, str) else None

    if not isinstance(raw, Mapping):
        return {
            "builder_tier_metrics_available": False,
            "builder_stable_char_count": None,
            "builder_context_char_count": None,
            "builder_volatile_char_count": None,
            "builder_separator_char_count": None,
            "builder_total_char_count": None,
            "builder_total_matches_system_prompt": None,
            "builder_stable_share": None,
            "builder_context_share": None,
            "builder_volatile_share": None,
        }

    def as_int(name: str) -> int | None:
        try:
            value = raw.get(name)
            return int(value) if value is not None else None
        except Exception:
            return None

    stable = as_int("stable_chars")
    context = as_int("context_chars")
    volatile = as_int("volatile_chars")
    separators = as_int("separator_chars")
    total = as_int("total_chars")

    matches = (
        total == full_chars
        if total is not None and full_chars is not None
        else None
    )

    active_chars = as_int("active_prompt_chars")

    return {
        "builder_tier_metrics_available": True,
        "builder_tier_metric_source": raw.get("source"),
        "builder_stable_char_count": stable,
        "builder_context_char_count": context,
        "builder_volatile_char_count": volatile,
        "builder_separator_char_count": separators,
        "builder_total_char_count": total,
        "builder_active_prompt_char_count": active_chars,
        "builder_candidate_matches_active_prompt":
            raw.get("candidate_matches_active_prompt"),
        "builder_total_matches_system_prompt": matches,
        "builder_stable_share": _ratio(stable, total),
        "builder_context_share": _ratio(context, total),
        "builder_volatile_share": _ratio(volatile, total),
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

    request = kwargs.get("request")
    body = request.get("body") if isinstance(request, Mapping) else None
    if not isinstance(body, Mapping) and isinstance(request, Mapping):
        body = request

    tools = body.get("tools") if isinstance(body, Mapping) else None

    effective_tool_count = (
        len(tools)
        if isinstance(tools, list)
        else (0 if isinstance(body, Mapping) and tools is None else None)
    )
    effective_tool_payload_present = (
        bool(tools) if isinstance(body, Mapping) else None
    )
    effective_tool_payload_char_count = (
        _serialized_chars(tools)
        if isinstance(tools, list)
        else (0 if isinstance(body, Mapping) and tools is None else None)
    )

    pre = {
        "approx_input_tokens": kwargs.get("approx_input_tokens"),
        "request_char_count": kwargs.get("request_char_count"),
        "message_count": kwargs.get("message_count"),
        "tool_count": kwargs.get("tool_count"),
        "effective_tool_count": effective_tool_count,
        "effective_tool_payload_present": effective_tool_payload_present,
        "effective_tool_payload_char_count": effective_tool_payload_char_count,
        **measurements,
        **_builder_tier_measurements(kwargs),
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
