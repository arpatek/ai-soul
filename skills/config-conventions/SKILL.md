---
name: config-conventions
description: arpatek's conventions for non-code files — 80-char section dividers in SSH configs and dotfiles, and the four-file docs/ pattern (architecture, decisions, gotchas, upgrading) every component gets. Load when editing config files, dotfiles, or writing project documentation.
---

# Config and docs conventions

## Config files (SSH, dotfiles, etc.)

Section dividers — exactly **80 characters**:
`# ──[ Section Name ]────────────────────────────────────────────────────────`

Same width as Bash — 80 is the universal column anchor. Same `──[` / `]` style for consistency.

---

## Docs (home.arpa pattern)

Every component gets a `docs/` directory with these four files:
- `architecture.md` — what it is and how the pieces fit
- `decisions.md` — why it was built this way
- `gotchas.md` — things that will trip you up
- `upgrading.md` — how to safely update

---

