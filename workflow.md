# arpatek — workflow

How these files get used. The config in this repo is only half the practice; this is the
other half.

---

## Why the files are split

The split is not cosmetic. Each file changes at a different rate and for a different reason.

| File | Holds | Changes when |
|------|-------|--------------|
| `soul.md` | Doctrine, worldview, opinions, tensions | Rarely — a genuine shift in how I think |
| `style.md` | Voice, modes, anti-patterns | When an interaction pattern proves wrong |
| `skills/*-conventions/` | Bash, Python, config, git conventions | When a convention is earned, usually by a bug |
| `skills/` (method) | Debug, plan, teach, review, ship-pressure | When a way of working proves wrong |
| `context.md` | Identity, stack, projects, tooling | Monthly — facts go stale fastest |

Keeping them separate means a stale fact in `context.md` never forces a rewrite of doctrine,
and a new Bash convention does not touch the voice rules. One file would drift as a unit and
get replaced wholesale instead of maintained.

The split is also load-bearing at runtime. `soul.md`, `style.md` and `context.md` are always in
context; everything else is a skill, pulled in only when its description matches the task.
Writing a Bash script loads the Bash rules and leaves the FastAPI router conventions on disk.

The working-method skills used to be prose in `style.md` — a Modes section that was always
loaded and never invoked. Describing a process in an instruction file is not the same as
having it available as one, and `style.md` now keeps only the index.

---

## The conventions are downstream of failures

Nothing in `conventions.md` is a preference. Each rule is the residue of something that broke.

`set -eo pipefail` and `trap '...' ERR` on every script exist because an earlier codebase had
them on one file out of thirty-two, and a failed fetch wrote an empty file that read as a clean
result. `printf` over `echo` exists because `echo -e` interprets backslashes in *data*.
"Source `lib.sh`, don't copy-paste" exists because fourteen near-identical scripts meant every
fix was fourteen edits and some of them got missed.

A convention that can't name the failure it prevents does not belong in the file.

---

## Rules that enforce themselves

A config *asks* a model to follow conventions. Late in a long session, with a full context
window and a persuasive prompt, asking is not always enough.

Two mechanisms close that gap, and both live in this repo:

- **A `PostToolUse` hook** runs `shellcheck` on every shell script the agent writes and blocks
  on findings. The agent does not get a vote.
- **An eval suite** turns the anti-patterns in `style.md` into assertions that run in CI, so a
  wording change that fixes one case and breaks five others fails the build instead of
  shipping silently.

This is the Puppet-versus-Ansible distinction applied to my own tooling. Instructions
orchestrate; hooks and evals enforce. A rule that matters belongs in the second category.

---

## The verification loop

The config tells a model how to behave. It does not make the output correct. What follows is
what actually gets checked before anything lands.

**Premises first.** A model will accept a wrong framing and produce confident work on top of
it. Most corrections I make are not to the answer — they are to the question. If it is
reviewing code I have already archived, I say so before it writes a patch I will not apply.

**Plan before execution on anything non-trivial.** Stated in `soul.md` as a boundary, enforced
here as a habit. If the first thing produced is a diff rather than an approach, that is the
signal to stop and back up.

**Version pins get verified, always.** A recommended version is a claim about current stable
and about known CVEs. That claim gets checked against the source, never taken on trust.

**Read the diff, not the summary.** A description of a change is not the change. This is the
single most reliable place for an error to hide, because the summary is usually accurate about
intent and wrong about detail.

**Nothing is pushed without asking.** Commits get written and shown in full — the actual
message, not a description of it. Pushing is a separate decision, made by me.

---

## Persistent memory

Claude Code sessions write to a file-based memory directory — one file per fact, with typed
frontmatter and an index that loads at session start.

```markdown
---
name: <short-kebab-case-slug>
description: <one line, used to decide relevance on recall>
metadata:
  type: user | feedback | project | reference
---

<the fact. For feedback and project, follow with **Why:** and **How to apply:** lines.>
```

`user` is who I am and how I work. `feedback` is a correction I made that should stick.
`project` is ongoing work not derivable from the code. `reference` is a pointer outward.

**What earns a memory:** something non-obvious, durable, and not already recorded by the repo.
Corrections are the highest-value type — a mistake that gets written down once stops repeating.

**What does not:** anything git history, `CLAUDE.md`, or the code itself already says. Storing
what the repo already knows produces a second source of truth that drifts.

**What gets deleted:** memories that turn out to be wrong. A stale memory is worse than a
missing one, because it is asserted with the same confidence as a correct one.

---

## Where AI belongs

An accelerator and multiplier of what you already are. If you build bad code, it helps you
build bad code faster. That is the whole thesis and it cuts both ways.

The line is understanding. Generated code I cannot explain is a liability I have not
priced yet — it works until it doesn't, and then I am debugging something I never reasoned
about. Shipping before full understanding is acceptable; skipping the return trip is not.

Where it earns its keep: surveying a codebase faster than I can read it, catching the thing I
stopped seeing, holding context across a long session, and drafting the version I then
rewrite. Where it doesn't: anything I could not review. If I cannot tell whether the output is
right, I am not qualified to accept it.
