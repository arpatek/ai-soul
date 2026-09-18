# Evals

Behavioral regression suite for the persona config. Every assertion here traces
to a rule in `soul.md` or `style.md` — the anti-patterns are `not-icontains`
checks, the doctrine is `llm-rubric`, the Bash conventions are `contains` checks
against generated code.

The point is that a config change is testable. Tightening one rule in `style.md`
can loosen three others, and no manual spot-check catches that.

## Running

```bash
export ANTHROPIC_API_KEY=...
cd evals
npx promptfoo@latest eval        # run the suite
npx promptfoo@latest view        # browse results
```

`../build/AGENTS.md` is the system prompt under test, so run `./build.sh` first
if the source markdown changed.

## Adding a case

An anti-pattern in `style.md` that has no assertion here is a rule nobody is
checking. When you add a rule, add the case that proves it.
