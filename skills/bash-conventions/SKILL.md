---
name: bash-conventions
description: arpatek's Bash conventions — script skeleton, 80-char section dividers, printf over echo, status decorators, error trapping, lib.sh sourcing. Load when writing, editing, or reviewing any Bash or shell script.
---

# Bash conventions


**Structure — every script in this order:**
1. `#!/usr/bin/env bash` shebang
2. Header block:
   ```bash
   # =============================================================================
   # Script Name: name.sh
   # Description: What it does.
   # Author: Juan Garcia (arpatek)
   # Created: YYYY-MM-DD
   # Version: 1.0
   # =============================================================================
   ```
3. Bash version guard — always:
   ```bash
   if ((BASH_VERSINFO[0] < 4)); then
     printf "name.sh requires bash 4 or higher (detected: %s)\n" "$BASH_VERSION" >&2
     exit 1
   fi
   ```
4. `set -eo pipefail`
5. Section dividers throughout — exactly **80 characters**:
   `# ──[ Section Name ]──────────────────────────────────────────────────────────`
6. `trap '...' ERR` error handler
7. `usage()` function + `while [[ $# -gt 0 ]]; do case "$1" in` arg parsing when args exist
8. Functions before main logic; `local` on every variable inside functions
9. Main logic at the bottom under `# ──[ Main ]──`

**Output — always `printf`, never `echo`:**
```bash
printf "%s Some message\n" "$(BANNER)"
```

**Status decorators (from lib.sh — source it, don't redefine):**
```
BANNER [^]  — yellow/purple  — section headers
PLUS   [+]  — yellow/green   — in-progress steps
COMPLETE[*] — yellow/blue    — success
FAILED [!]  — yellow/red     — errors
LAMBDA [λ]  — yellow/sage    — environment entry (#79be9a — matches arpatek.dev)
```
The `[λ]` in sage green is the personal signature. Use it for the final "entering environment" line.

**Patterns to always follow:**
- `command -v foo` not `which foo` for binary detection
- `case "$(uname -m)"` for architecture detection
- GitHub releases: `curl API | grep '"tag_name"' | grep -o 'v[0-9][^"]*' | tr -d '\r'`
- Temp dirs: `tmp_dir="$(mktemp -d)"` + `trap 'rm -rf "$tmp_dir"' RETURN`
- `|| true` to suppress pipefail on optional commands
- Shared utilities in `lib.sh` — source it, don't copy-paste functions
- `declare -A` for associative arrays

