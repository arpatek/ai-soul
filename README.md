# ai-soul

AI persona config for arpatek — works with any model or agent that reads a system prompt.

## Files

| File | Purpose |
|------|---------|
| `soul.md` | Identity, doctrine, worldview, opinions, tensions, influences |
| `style.md` | Voice, modes, code conventions, anti-patterns, vocabulary |
| `context.md` | Homelab topology, stack, projects, certs, daily tooling |
| `Modelfile` | Ollama model definition — bakes all three into a local model |

## Usage

### Ollama (local models)

```bash
ollama create arpatek -f Modelfile
ollama run arpatek
```

Swap `FROM hermes3` in the Modelfile for any model you have pulled.

### Claude Code

```bash
cat soul.md style.md context.md > ~/.claude/CLAUDE.md
```

Loaded automatically at the start of every session.

### Any other tool

Paste the contents of `soul.md`, `style.md`, and `context.md` into the system prompt field.

## Updating

Edit the source files directly. After changes, regenerate CLAUDE.md:

```bash
cat soul.md style.md context.md > ~/.claude/CLAUDE.md
```

Rebuild the Ollama model:

```bash
ollama create arpatek -f Modelfile
```
