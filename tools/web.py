import logging

import httpx

log = logging.getLogger(__name__)


def fetch_url(url: str, headers: dict | None = None) -> str:
    log.debug("fetch: %s", url)
    try:
        with httpx.Client(timeout=15, follow_redirects=True) as client:
            resp = client.get(url, headers=headers or {})
        content_type = resp.headers.get("content-type", "")
        if "json" in content_type:
            return resp.text
        if "text" in content_type or "html" in content_type:
            return resp.text[:8000]
        return f"[binary {len(resp.content)} bytes, status {resp.status_code}]"
    except httpx.TimeoutException:
        return "[error: request timed out]"
    except Exception as e:
        return f"[error: {e}]"
