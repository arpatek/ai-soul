---
name: writing-skills
description: How to write a new skill for this config — what earns one, the frontmatter contract, and the rule that a convention must name the failure it prevents. Load when adding, editing, or splitting a skill in ai-soul.
---

# Writing skills

Skills exist so the instruction file stays small. Every skill is content that would otherwise load on every session in every directory whether or not it was relevant.

## What earns a skill

A skill is warranted when the content is:

- **Conditional** — relevant to some tasks and inert for the rest. Bash conventions qualify. Voice does not; it applies to every response and belongs in `style.md`.
- **Non-trivial** — more than a sentence. A one-line rule goes in `style.md`, not a directory.
- **Repeated** — a workflow or convention that comes up again, not a one-off.

If it applies always, it is not a skill. If it applies once, it is not a skill either.

## The failure rule

Every convention in a skill names the failure it prevents, or it does not go in.

`set -eo pipefail` is in `bash-conventions` because a suite once had it on one file out of thirty-two, and a failed fetch wrote an empty file that read as a clean QC result. `printf` over `echo` is there because `echo -e` interprets backslashes in data. Both earn their place.

A rule that cannot name its failure is taste. Taste is fine, but it belongs in `style.md` where it is cheap, not in a skill where it claims to be load-bearing.

## Frontmatter contract

```yaml
---
name: kebab-case-name          # required, matches the directory
description: ...               # required — this is the loading trigger
aliases: [alt-name]            # optional
disable-model-invocation: true # optional — user-invoked only
---
```

**The description is the whole mechanism.** Claude Code reads descriptions up front and loads the body only when one matches the task. A vague description means the skill never loads, or loads constantly. Write it as: what it contains, then *"Load when ..."* with the concrete trigger.

Compare:

- Bad — `description: Bash stuff`
- Good — `description: arpatek's Bash conventions — script skeleton, 80-char section dividers, printf over echo, status decorators. Load when writing, editing, or reviewing any Bash or shell script.`

## After adding one

1. Run `./build.sh` — `conventions.md` is generated from `skills/` and will be stale otherwise.
2. Add an eval case to `evals/promptfooconfig.yaml`. A rule with no assertion is a rule nobody is checking.
3. If it is a convention skill, add it to the loop in `compose_conventions()`.
