# Evals

Behavioral regression suite for the persona config. Every assertion here traces
to a rule in `soul.md` or `style.md` — the anti-patterns are `not-icontains`
checks, the doctrine is `llm-rubric`, the Bash conventions are `contains` checks
against generated code.

The point is that a config change is testable. Tightening one rule in `style.md`
can loosen three others, and no manual spot-check catches that.

## Status

Validated, not run. `npx promptfoo@latest validate` passes, so the assertions, provider string
and file references are all well-formed — but the suite has never been executed against the
model, and it is not wired to CI. Running it needs an `ANTHROPIC_API_KEY`, which bills
separately from a Claude Pro subscription (roughly $0.40 per run on `claude-opus-5`: eleven
generation calls plus ten `llm-rubric` grading calls).

Until it has been run once, this is a spec rather than evidence. Read it that way.

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
