---
name: plan
description: arpatek's planning method — research before proposing, ask clarifying questions upfront, get agreement before executing. Load before any non-trivial implementation, migration, or change to a load-bearing service.
---

# Plan

Research first, then propose. Do not execute until the plan is agreed.

## Sequence

1. **Ask upfront.** Every clarifying question comes before the plan, not scattered through it. If the answer changes the shape of the work, it is blocking — ask it and wait. If it only changes a detail, state the assumption and continue.
2. **Research.** Read the existing code, the existing config, the docs. A plan built on assumptions about what is already there is a guess with formatting.
3. **Propose.** What will change, in what order, and what each step depends on. Name the parts that are reversible and the parts that are not.
4. **Wait for agreement.** Then execute.

## What a plan contains

- The steps, ordered by dependency, not by ease.
- What is being touched that is load-bearing, called out explicitly.
- The rollback for anything that cannot simply be re-run.
- What is deliberately out of scope, so it does not get assumed in.

## What a plan is not

Not a survey of options with no recommendation. If there are three approaches, say which one and why, then note the others in a sentence. An unmade decision handed back is not a plan.

Not an essay. A plan for a two-file change is four lines.

## Trigger

Anything touching prod. Anything with a migration. Anything where the first step makes the second step harder to undo. Small, reversible, well-understood changes do not need one — say what you are doing and do it.
