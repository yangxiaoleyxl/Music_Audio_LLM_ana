from __future__ import annotations

import json
import time
import urllib.error
import urllib.request
from typing import Dict, Optional


USER_AGENT = "audio-llm-radar/0.1 (research literature monitoring)"


def retry_delay_seconds(exc: BaseException, attempt: int) -> Optional[float]:
    """Seconds to wait before another try. None means the request should stop."""
    if attempt >= 4:
        return None
    if isinstance(exc, urllib.error.HTTPError):
        if exc.code == 429:
            retry_after = exc.headers.get("Retry-After") if exc.headers else None
            if retry_after and str(retry_after).isdigit():
                return min(int(retry_after), 30)
            return min(8 * (attempt + 1), 30)
        if exc.code >= 500:
            return min(5 * (attempt + 1), 20)
        return None
    if isinstance(exc, (urllib.error.URLError, TimeoutError)):
        return min(2 ** attempt, 8)
    return None


def get_bytes(
    url: str,
    headers: Optional[Dict[str, str]] = None,
    timeout: int = 45,
    attempts: int = 4,
) -> bytes:
    request_headers = {"User-Agent": USER_AGENT, "Accept": "*/*"}
    if headers:
        request_headers.update(headers)

    last_error: Exception = RuntimeError("request not attempted")
    for attempt in range(attempts):
        try:
            request = urllib.request.Request(url, headers=request_headers)
            with urllib.request.urlopen(request, timeout=timeout) as response:
                return response.read()
        except (urllib.error.URLError, urllib.error.HTTPError, TimeoutError) as exc:
            last_error = exc
            delay = retry_delay_seconds(exc, attempt)
            if delay is None or attempt + 1 >= attempts:
                break
            time.sleep(delay)
    raise last_error


def get_json(url: str, headers: Optional[Dict[str, str]] = None) -> dict:
    return json.loads(get_bytes(url, headers=headers).decode("utf-8"))

