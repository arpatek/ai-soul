---
name: python-conventions
description: arpatek's Python conventions — module docstring layout, __version__, 88-char section dividers, import grouping, type hints, one router per module for FastAPI. Load when writing, editing, or reviewing Python.
---

# Python conventions


**Structure — every module in this order:**
1. `#!/usr/bin/env python3`
2. Module docstring:
   ```python
   """
   module.py - Module Name
   ========================================================================================

   What this module does.

   Author: Juan Garcia (arpatek)
   """
   ```
3. `__version__ = "x.x.x"` (entry point files)
4. Section dividers — exactly **88 characters**:
   `# ──[ Section Name ]─────────────────────────────────────────────────────────────────`
5. Import grouping — each group gets its own divider:
   ```python
   # ──[ Imports ]─────────────────────────────────────────────────────────────────────────
   from fastapi import ...

   # ──[ Internal Module Imports ]─────────────────────────────────────────────────────────
   from app.routes.foo import ...
   ```
6. Align multi-line assignments to a column when it aids readability
7. Type hints on all function signatures
8. One router per module (FastAPI pattern) — include in `main.py`, never define routes there

**No comments that describe what the code does** — only comments that explain why something non-obvious is happening (workaround, constraint, subtle invariant).

---

