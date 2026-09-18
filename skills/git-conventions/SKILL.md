---
name: git-conventions
description: arpatek's Git conventions — commit message format (type(scope): summary with a Changes: list, never co-author tags) and annotated release tags in Keep a Changelog form. Load when writing a commit message, tagging a release, or reviewing git history.
---

# Git conventions

**Releases:** annotated tags only — never lightweight. Bump `__version__` in code first, commit, then tag.

Tag message follows [Keep a Changelog](https://keepachangelog.com) format:

```
v1.0.0 — Short description

Added:
- new capability or feature

Changed:
- behavior that differs from the previous version

Removed:
- anything dropped
```

First line: `v{version} — short description`. Body uses `Added/Changed/Removed` sections — omit empty ones. Push explicitly: `git push origin v{version}`.

---

**Commits:** `type(scope): short summary` — no co-author tags. Body uses a `Changes:` bullet list.

```
type(scope): short summary

Changes:
- item 1
- item 2
```

Types: `feat` `fix` `docs` `style` `refactor` `perf` `test` `build` `ci` `chore` `revert`
Scope: the subdirectory or component (e.g. `soul`, `k3s`, `wireguard`, `ipa`).

---

