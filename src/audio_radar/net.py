from __future__ import annotations

import json
import time
import urllib.error
import urllib.request
from typing import Dict, Optional


USER_AGENT = "audio-llm-radar/0.1 (research literature monitoring)"


def get_bytes(
    url: str,
    headers: Optional[Dict[str, str]] = None,
    timeout: int = 45,
    attempts: int = 3,
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
            if attempt + 1 < attempts:
                time.sleep(2 ** attempt)
    raise last_error


def get_json(url: str, headers: Optional[Dict[str, str]] = None) -> dict:
    return json.loads(get_bytes(url, headers=headers).decode("utf-8"))

