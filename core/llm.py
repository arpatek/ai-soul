import os
import time
import logging
import anthropic
from anthropic import APIStatusError, APIConnectionError

log = logging.getLogger(__name__)


class LLMClient:
    def __init__(self, config: dict):
        api_key = os.environ.get("ANTHROPIC_API_KEY")
        if not api_key:
            raise EnvironmentError("ANTHROPIC_API_KEY not set")
        self.client = anthropic.Anthropic(api_key=api_key)
        self.model = config.get("model", "claude-sonnet-4-6")
        self.max_tokens = config.get("agent", {}).get("max_tokens", 4096)

    def complete(
        self,
        system: str,
        messages: list,
        tools: list,
    ) -> anthropic.types.Message:
        kwargs: dict = {
            "model": self.model,
            "max_tokens": self.max_tokens,
            "system": [
                {
                    "type": "text",
                    "text": system,
                    "cache_control": {"type": "ephemeral"},
                }
            ],
            "messages": messages,
        }
        if tools:
            kwargs["tools"] = tools

        for attempt in range(3):
            try:
                resp = self.client.messages.create(**kwargs)
                log.info(
                    "usage input=%d output=%d cache_read=%d cache_create=%d",
                    resp.usage.input_tokens,
                    resp.usage.output_tokens,
                    getattr(resp.usage, "cache_read_input_tokens", 0),
                    getattr(resp.usage, "cache_creation_input_tokens", 0),
                )
                return resp
            except APIStatusError as e:
                if e.status_code == 429 and attempt < 2:
                    wait = 2**attempt
                    log.warning("rate limited, retrying in %ds", wait)
                    time.sleep(wait)
                    continue
                raise
            except APIConnectionError:
                if attempt < 2:
                    time.sleep(1)
                    continue
                raise
        raise RuntimeError("LLM request failed after retries")
