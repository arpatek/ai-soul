import logging
from pathlib import Path

log = logging.getLogger(__name__)


def read_file(path: str) -> str:
    p = Path(path).expanduser()
    if not p.exists():
        return f"[error: {path} not found]"
    if not p.is_file():
        return f"[error: {path} is not a file]"
    try:
        return p.read_text(errors="replace")
    except Exception as e:
        return f"[error: {e}]"


def write_file(path: str, content: str) -> str:
    p = Path(path).expanduser()
    try:
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(content)
        return f"wrote {len(content)} bytes to {path}"
    except Exception as e:
        return f"[error: {e}]"


def list_dir(path: str) -> str:
    p = Path(path).expanduser()
    if not p.exists():
        return f"[error: {path} not found]"
    if not p.is_dir():
        return f"[error: {path} is not a directory]"
    try:
        entries = sorted(p.iterdir(), key=lambda x: (not x.is_dir(), x.name.lower()))
        lines = []
        for entry in entries:
            if entry.is_dir():
                lines.append(f"d  {entry.name}/")
            else:
                size = entry.stat().st_size
                lines.append(f"f  {entry.name} ({size:,} B)")
        return "\n".join(lines) if lines else "(empty)"
    except Exception as e:
        return f"[error: {e}]"
