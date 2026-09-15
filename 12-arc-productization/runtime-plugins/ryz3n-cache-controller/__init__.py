"""RYZ3N Cache Controller v0.1 — shadow telemetry only.

E1.19 contract:
- NEVER mutates an LLM request.
- NEVER short-circuits provider execution.
- NEVER persists prompt/response content, credentials, chat/user ids, or private memory.
- Emits content-free operational telemetry and deterministic hashes needed to measure
  prefix stability, provider cache behavior, concurrency, retries, errors, and later
  cache/dedup efficiency.
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


def _now() -> str:
    return datetime.now(timezone.utc).isoformat()


def _arc_id() -> str:
    explicit = (os.environ.get("RYZ3N_ARC_ID") or "").strip()
    if explicit:
        return explicit
    home = os.environ.get("HERMES_HOME", "")
    low = home.lower().replace("\\", "/")
    if "/profiles/cargo" in low:
        return "cargo"
    if "/profiles/narc" in low:
        return "narc"
    if "/profiles/vonda" in low:
        return "vonda"
    return "prime"


def _telemetry_path() -> Path:
    hermes_home = Path(os.environ.get("HERMES_HOME") or (Path.home() / ".hermes"))
    path = hermes_home / "ryz3n-telemetry" / "cache-controller-shadow.jsonl"
    path.parent.mkdir(parents=True, exist_ok=True)
    return path


def _stable_json(value: Any) -> str:
    """Serialize only in memory for hashing. The serialized content is never persisted."""
    try:
        return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False, default=str)
    except Exception:
        return repr(value)


def _hash(value: Any) -> str:
    return hashlib.sha256(_stable_json(value).encode("utf-8", errors="replace")).hexdigest()


def _session_hash(value: Any) -> str | None:
    if value in (None, ""):
        return None
    return _hash(str(value))[:20]


def _request_fingerprints(request: Any) -> tuple[str | None, str | None]:
    if not isinstance(request, Mapping):
        return None, None

    # Deliberately exclude credentials/network headers. Content is used transiently only
    # as hash input and is never written to telemetry.
    structural: dict[str, Any] = {}
    for key in (
        "model", "messages", "input", "tools", "tool_choice", "max_tokens",
        "max_completion_tokens", "temperature", "top_p", "response_format",
    ):
        if key in request:
            structural[key] = request[key]

    full = _hash(structural)

    prefix_material: dict[str, Any] = {k: v for k, v in structural.items() if k not in ("messages", "input")}
    seq = structural.get("messages")
    seq_key = "messages"
    if not isinstance(seq, list):
        seq = structural.get("input")
        seq_key = "input"
    if isinstance(seq, list):
        # Generic stable-prefix measurement: exclude the most recent wire item. This is
        # intentionally observational; it does not assert provider-specific KV boundaries.
        prefix_material[seq_key] = seq[:-1] if seq else []
    elif seq is not None:
        prefix_material[seq_key] = seq

    return full, _hash(prefix_material)


def _get(obj: Any, *names: str, default: int = 0) -> int:
    for name in names:
        try:
            if isinstance(obj, Mapping) and name in obj:
                value = obj[name]
            else:
                value = getattr(obj, name)
            if value is not None:
                return int(value)
        except Exception:
            continue
    return default


def _usage(kwargs: Mapping[str, Any]) -> dict[str, int]:
    usage = (
        kwargs.get("canonical_usage")
        or kwargs.get("usage")
        or kwargs.get("response_usage")
    )
    if usage is None:
        return {}

    input_tokens = _get(usage, "input_tokens", "prompt_tokens")
    output_tokens = _get(usage, "output_tokens", "completion_tokens")
    cache_read = _get(usage, "cache_read_tokens", "cache_read_input_tokens", "cached_tokens")
    cache_write = _get(usage, "cache_write_tokens", "cache_creation_input_tokens")

    # OpenAI-compatible nested prompt token details.
    details = None
    try:
        details = usage.get("prompt_tokens_details") if isinstance(usage, Mapping) else getattr(usage, "prompt_tokens_details", None)
    except Exception:
        details = None
    if details is not None:
        if not cache_read:
            cache_read = _get(details, "cached_tokens")
        if not cache_write:
            cache_write = _get(details, "cache_write_tokens", "cache_creation_input_tokens")

    total_tokens = _get(usage, "total_tokens")
    if not total_tokens:
        total_tokens = input_tokens + output_tokens + cache_read + cache_write

    return {
        "input_tokens": input_tokens,
        "cached_input_tokens": cache_read,
        "cache_write_tokens": cache_write,
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
    # Final allowlisted event is metadata-only. Never add raw hook kwargs here.
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
    request = kwargs.get("request")
    request_fp, prefix_fp = _request_fingerprints(request)

    with _LOCK:
        _ACTIVE += 1
        active = _ACTIVE
        if rid:
            _STARTS[rid] = time.monotonic()

    event = _base(kwargs, "pre_api_request")
    event.update({
        "approx_input_tokens": kwargs.get("approx_input_tokens"),
        "request_char_count": kwargs.get("request_char_count"),
        "message_count": kwargs.get("message_count"),
        "tool_count": kwargs.get("tool_count"),
        "active_concurrency_at_start": active,
        "request_fingerprint": request_fp,
        "prefix_fingerprint": prefix_fp,
        "middleware_trace_count": len(kwargs.get("middleware_trace") or []),
    })
    _write(event)


def _finish(kwargs: Mapping[str, Any], event_type: str) -> tuple[dict[str, Any], float | None]:
    global _ACTIVE
    rid = str(kwargs.get("api_request_id") or "")
    with _LOCK:
        started = _STARTS.pop(rid, None) if rid else None
        _ACTIVE = max(0, _ACTIVE - 1)
        active_after = _ACTIVE

    elapsed_ms = None
    if started is not None:
        elapsed_ms = round((time.monotonic() - started) * 1000.0, 3)

    event = _base(kwargs, event_type)
    event["latency_ms_local"] = elapsed_ms
    event["active_concurrency_after"] = active_after
    event.update(_usage(kwargs))
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
