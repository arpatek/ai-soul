# ai-soul

[![built by arpatek](.assets/badge.svg)](https://arpatek.dev)

AI persona config for arpatek — works with any model or agent that reads a system prompt.

An AI is an accelerator and a multiplier of what you already are. If you build bad code, it
helps you build bad code faster. That makes the configuration the interesting part: what you
require of the tool, what you refuse from it, and what you check before accepting its output.

This repo is that configuration, published in full — with a build step, a skill split, and a
regression suite, because a persona config that nobody tests is a preference, not an artifact.

## Files

### Source

| File | Purpose |
|------|---------|
| `soul.md` | Identity, doctrine, worldview, opinions, tensions, influences |
| `style.md` | Voice, modes, anti-patterns, vocabulary, quick reactions |
| `context.md` | Identity, stack, projects, certs, daily tooling (topology lives in `home.arpa`) |
| `workflow.md` | How the files are used — the split, the verification loop, persistent memory |
| `skills/*/SKILL.md` | Code conventions, one skill per language. Loaded on relevance, not on boot |
| `calibration.msg` | Few-shot examples baked into the Ollama model |
| `statusline-command.sh` | Claude Code status line — model, effort, rate limits, context bar, tokens, cost, git |

### Generated — do not edit

| File | Built from |
|------|------------|
| `build/AGENTS.md` | `soul.md` + `style.md` + `context.md` |
| `build/CLAUDE.md` | Symlink to `AGENTS.md` (Claude Code does not read `AGENTS.md` natively) |
| `conventions.md` | Readable rollup of `skills/` |
| `Modelfile` | Everything, baked — Ollama has no skill mechanism |

## Why conventions are skills

The four source files used to concatenate into a single ~3,900-token instruction file loaded
at the start of every session in every directory. Most of it was inert most of the time —
you paid for the Bash section-divider widths while asking which Pi was serving NTP.

The code conventions are now skills, which Claude Code loads only when their description
matches what you are doing. Writing Bash pulls in `bash-conventions` and nothing else.

### Conventions

| Skill | Loads when |
|-------|------------|
| `bash-conventions` | Writing, editing, or reviewing shell scripts |
| `python-conventions` | Writing, editing, or reviewing Python |
| `config-conventions` | Editing dotfiles and configs, or writing project docs |
| `git-conventions` | Writing a commit message or tagging a release |

### Working method

The Modes section in `style.md` used to describe these as prose — always loaded, never
invoked. They are processes, so they are skills now, and `style.md` keeps only the index.

| Skill | Loads when |
|-------|------------|
| `debug` | Investigating a failure. Known / unknown / next step, one hypothesis at a time |
| `plan` | A non-trivial change. Research, propose, wait for agreement before executing |
| `teach` | He asked to learn rather than to have it done. Concept before example |
| `review` | Critiquing a diff or an approach. Ranked by consequence, each finding names a failure |
| `ship-pressure` | He is polishing something that already works |
| `writing-skills` | Adding or editing a skill in this repo |
| `rhcsa-drill` | Invoked by name only — generates and grades RHCSA tasks against the UTM lab |
| `obsidian-capture` | Saving a conversation into the Obsidian vault as a linked, synthesized note |

## Build

```bash
./build.sh              # generate everything
./build.sh --check      # verify artifacts are current, exit 1 if stale
./build.sh --help
```

`skills/` and the three persona files are the source of truth. Everything else in the repo is
generated from them, which is why the `Modelfile` no longer drifts — it used to carry a
hand-maintained copy of every source file and fell two VMs and a laptop behind.

## Install

### Claude Code — as a plugin

```bash
claude plugin marketplace add https://codeberg.org/arpatek/ai-soul
claude plugin install arpatek-soul
```

Ships the twelve skills, the shellcheck hook, and the conventions-reviewer subagent.

### Claude Code — manual

```bash
./build.sh
ln -sf "$PWD/build/AGENTS.md" ~/.claude/CLAUDE.md
mkdir -p ~/.claude/skills && cp -r skills/* ~/.claude/skills/
```

### Any other agent

`build/AGENTS.md` targets the [AGENTS.md](https://agents.md) convention — the cross-tool
standard maintained under the Linux Foundation. Cursor, Codex and others read it directly.
Claude Code reads `CLAUDE.md` only, which is what the symlink is for.

### Ollama

```bash
./build.sh
ollama create arpatek -f Modelfile
ollama run arpatek
```

Provided for portability rather than as a daily driver — the config is runtime-agnostic and
this proves it. Set a different base with `./build.sh --model <name>`.

## Evals

The anti-patterns in `style.md` are a spec. [Promptfoo](https://promptfoo.dev) runs them as a
suite so a config change is testable rather than a matter of judgment.

```bash
export ANTHROPIC_API_KEY=...
cd evals && npx promptfoo@latest eval
```

Eleven cases, four assertions applied to every response. See [`evals/README.md`](evals/README.md).

**Not wired to CI, and not yet run.** The config validates (`npx promptfoo@latest validate`
passes), but executing it needs an `ANTHROPIC_API_KEY` — API access bills separately from a
Claude Pro subscription. The `evals` job in `.gitea/workflows/ci.yml` is commented out with
instructions for enabling it. Treat the suite as a machine-readable spec for `style.md` rather
than as a passing test run.

## Subagent

`agents/conventions-reviewer.md` reviews a diff against the four convention skills and runs
`shellcheck`, in its own context window. Use it when changes are ready and you don't want the
review competing for main-thread context.

## Hooks

`hooks/hooks.json` registers a `PostToolUse` hook that runs `shellcheck` on any shell script
the agent writes or edits, and blocks on findings. The config *asks* for conventions; the hook
*enforces* them, and cannot be talked out of it late in a long session.

## Status line

```bash
ln -sf "$PWD/statusline-command.sh" ~/.claude/statusline-command.sh
```

Then in `~/.claude/settings.json`:

```json
{ "statusLine": { "type": "command", "command": "~/.claude/statusline-command.sh" } }
```

## Updating

Edit the source files, run `./build.sh`, run the evals. Never edit a generated file — the next
build overwrites it, and `./build.sh --check` fails in CI if you do.

## License

MIT. See [LICENSE](LICENSE).
