#!/usr/bin/env bash
# =============================================================================
# Script Name: shellcheck-hook.sh
# Description: PostToolUse hook — shellcheck any shell script Claude just wrote.
# Author: Juan Garcia (arpatek)
# Created: 2026-09-18
# Version: 1.0
# =============================================================================

if ((BASH_VERSINFO[0] < 4)); then
  printf "shellcheck-hook.sh requires bash 4 or higher (detected: %s)\n" "$BASH_VERSION" >&2
  exit 1
fi

set -eo pipefail

# ──[ Main ]───────────────────────────────────────────────────────────────────

command -v shellcheck >/dev/null 2>&1 || exit 0

payload="$(cat)"
file="$(printf '%s' "$payload" | sed -n 's/.*"file_path"[[:space:]]*:[[:space:]]*"\([^"]*\)".*/\1/p')"

[[ -z "$file" || ! -f "$file" ]] && exit 0
[[ "$file" == *.sh || "$(head -c 2 "$file" 2>/dev/null)" == "#!" ]] || exit 0
head -1 "$file" | grep -qE '^#!.*(ba)?sh' || exit 0

if ! out="$(shellcheck -f gcc "$file" 2>&1)"; then
  printf '[!] shellcheck findings in %s:\n%s\n' "$file" "$out" >&2
  exit 2
fi
exit 0
