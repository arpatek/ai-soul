import logging
from importlib import import_module
from typing import Any, Callable

log = logging.getLogger(__name__)

TOOL_DEFINITIONS: dict[str, dict] = {
    "shell": {
        "name": "shell",
        "description": (
            "Execute a shell command and return stdout, stderr, and exit code. "
            "Use for system operations, file management, and automation tasks."
        ),
        "input_schema": {
            "type": "object",
            "properties": {
                "command": {"type": "string", "description": "Shell command to run"},
            },
            "required": ["command"],
        },
    },
    "read_file": {
        "name": "read_file",
        "description": "Read and return the contents of a file.",
        "input_schema": {
            "type": "object",
            "properties": {
                "path": {"type": "string", "description": "Absolute or relative path"},
            },
            "required": ["path"],
        },
    },
    "write_file": {
        "name": "write_file",
        "description": "Write content to a file, creating parent directories if needed.",
        "input_schema": {
            "type": "object",
            "properties": {
                "path": {"type": "string", "description": "File path to write"},
                "content": {"type": "string", "description": "Content to write"},
            },
            "required": ["path", "content"],
        },
    },
    "list_dir": {
        "name": "list_dir",
        "description": "List files and subdirectories at a given path.",
        "input_schema": {
            "type": "object",
            "properties": {
                "path": {"type": "string", "description": "Directory to list"},
            },
            "required": ["path"],
        },
    },
    "fetch_url": {
        "name": "fetch_url",
        "description": "Fetch the response body of a URL via HTTP GET.",
        "input_schema": {
            "type": "object",
            "properties": {
                "url": {"type": "string", "description": "URL to fetch"},
                "headers": {
                    "type": "object",
                    "description": "Optional HTTP headers",
                    "additionalProperties": {"type": "string"},
                },
            },
            "required": ["url"],
        },
    },
}

_MODULE_MAP: dict[str, tuple[str, str]] = {
    "shell": ("tools.shell", "run"),
    "read_file": ("tools.files", "read_file"),
    "write_file": ("tools.files", "write_file"),
    "list_dir": ("tools.files", "list_dir"),
    "fetch_url": ("tools.web", "fetch_url"),
}


class ToolRegistry:
    def __init__(self, enabled: list[str], tool_config: dict):
        self.enabled = enabled
        self.tool_config = tool_config
        self._funcs: dict[str, Callable] = {}
        self._load()

    def _load(self):
        for name in self.enabled:
            if name not in _MODULE_MAP:
                log.warning("unknown tool: %s", name)
                continue
            mod_path, func_name = _MODULE_MAP[name]
            try:
                mod = import_module(mod_path)
                self._funcs[name] = getattr(mod, func_name)
                log.debug("loaded tool: %s", name)
            except (ImportError, AttributeError) as e:
                log.error("failed to load tool %s: %s", name, e)

    def definitions(self) -> list[dict]:
        return [TOOL_DEFINITIONS[n] for n in self.enabled if n in TOOL_DEFINITIONS]

    def execute(self, name: str, inputs: dict) -> Any:
        if name not in self._funcs:
            return f"tool '{name}' not available"
        try:
            if name == "shell":
                timeout = self.tool_config.get("shell", {}).get("timeout", 30)
                return self._funcs[name](inputs["command"], timeout=timeout)
            return self._funcs[name](**inputs)
        except Exception as e:
            log.error("tool %s raised: %s", name, e)
            return f"error: {e}"
