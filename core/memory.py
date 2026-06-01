import json
import logging
from pathlib import Path
from typing import Any

log = logging.getLogger(__name__)


class Memory:
    def __init__(self, path: str, max_messages: int = 40):
        self.path = Path(path)
        self.max_messages = max_messages
        self.messages: list[dict] = []
        self._load()

    def _load(self):
        if self.path.exists():
            try:
                data = json.loads(self.path.read_text())
                self.messages = data.get("messages", [])
                log.debug("loaded %d messages from %s", len(self.messages), self.path)
            except (json.JSONDecodeError, KeyError) as e:
                log.warning("could not load memory (%s), starting fresh", e)
                self.messages = []

    def _save(self):
        self.path.write_text(json.dumps({"messages": self.messages}, indent=2))

    def add_user(self, content: str):
        self.messages.append({"role": "user", "content": content})
        self._trim()
        self._save()

    def add_assistant(self, content: Any):
        self.messages.append({"role": "assistant", "content": content})
        self._trim()
        self._save()

    def add_tool_results(self, results: list[dict]):
        self.messages.append({"role": "user", "content": results})
        self._save()

    def get_messages(self) -> list[dict]:
        return self.messages.copy()

    def _trim(self):
        if len(self.messages) > self.max_messages:
            # Drop from the front, but keep pairs so we never orphan a tool_result
            self.messages = self.messages[-self.max_messages :]
