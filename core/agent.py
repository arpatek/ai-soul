import logging
from pathlib import Path

import yaml
from rich.console import Console
from rich.markdown import Markdown
from rich.panel import Panel
from rich.prompt import Confirm, Prompt

from core.llm import LLMClient
from core.memory import Memory
from core.tools import ToolRegistry

log = logging.getLogger(__name__)
console = Console()

_CONFIG_PATH = Path(__file__).parent.parent / "config" / "config.yaml"


class Agent:
    def __init__(self, config_path: str | None = None, no_confirm: bool = False):
        path = config_path or _CONFIG_PATH
        with open(path) as f:
            self.config = yaml.safe_load(f)

        self.llm = LLMClient(self.config)
        self.memory = Memory(
            path=self.config["memory"]["file"],
            max_messages=self.config["memory"].get("max_messages", 40),
        )
        tools_cfg = self.config.get("tools", {})
        self.tools = ToolRegistry(
            enabled=tools_cfg.get("enabled", []),
            tool_config=tools_cfg,
        )
        self.system_prompt: str = self.config["agent"].get("system_prompt", "You are a helpful assistant.")
        self._confirm_shell = (
            tools_cfg.get("shell", {}).get("confirmation_required", True) and not no_confirm
        )

    def _run_turn(self, user_input: str) -> str:
        self.memory.add_user(user_input)

        while True:
            response = self.llm.complete(
                system=self.system_prompt,
                messages=self.memory.get_messages(),
                tools=self.tools.definitions(),
            )
            log.debug("stop_reason=%s", response.stop_reason)

            if response.stop_reason == "end_turn":
                text = next(
                    (b.text for b in response.content if hasattr(b, "text")),
                    "",
                )
                self.memory.add_assistant(response.content)
                return text

            if response.stop_reason == "tool_use":
                self.memory.add_assistant(response.content)
                tool_results = []

                for block in response.content:
                    if block.type != "tool_use":
                        continue

                    if block.name == "shell":
                        cmd = block.input.get("command", "")
                        console.print(f"\n[dim]$ {cmd}[/dim]")
                        if self._confirm_shell and not Confirm.ask("run?", default=True):
                            result = "cancelled by user"
                        else:
                            result = self.tools.execute(block.name, block.input)
                    else:
                        console.print(f"\n[dim]tool: {block.name}[/dim]")
                        result = self.tools.execute(block.name, block.input)

                    tool_results.append(
                        {
                            "type": "tool_result",
                            "tool_use_id": block.id,
                            "content": str(result),
                        }
                    )

                self.memory.add_tool_results(tool_results)
                continue

            log.warning("unexpected stop_reason: %s", response.stop_reason)
            break

        return ""

    def run_once(self, prompt: str):
        response = self._run_turn(prompt)
        console.print(Markdown(response))

    def run(self):
        console.print(
            Panel(
                "[bold]ai-agent[/bold]  type [cyan]exit[/cyan] or [cyan]Ctrl-C[/cyan] to quit",
                style="dim",
            )
        )
        try:
            while True:
                user_input = Prompt.ask("\n[bold green]>[/bold green]")
                if user_input.strip().lower() in ("exit", "quit", ":q"):
                    break
                if not user_input.strip():
                    continue

                with console.status("[dim]thinking…[/dim]"):
                    response = self._run_turn(user_input)

                console.print()
                console.print(Markdown(response))
        except KeyboardInterrupt:
            console.print("\n[dim]bye[/dim]")
