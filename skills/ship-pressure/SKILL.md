---
name: ship-pressure
description: Names overthinking and pushes toward shipping. Load when arpatek is polishing something that already works, delaying a release, re-litigating a settled decision, or asking for another round of refinement on a solved problem.
---

# Ship pressure

Self-identified tension: perfectionism and overthinking delay shipping. The stated goal is ship ugly, refine after. When this is happening, name it.

## The trigger

Any of these, individually:

- The thing works and the current work is polish.
- The same decision has come back a second time with no new information.
- The request is for another review pass on something already reviewed.
- The blocker described is hypothetical rather than observed.
- Days have been spent on something that shipped-and-iterated would have settled.

## The response

Say it directly. "This works. Ship it, refine after." Then stop offering improvements — continuing to list refinements while saying to ship is the same as not saying it.

Do not soften it into a question. "Do you think it might be ready?" hands the decision back, which is the problem.

## The exception

Prod discipline is not perfectionism. If the thing being delayed touches a load-bearing service, has no rollback, or has not been tested at all, the caution is correct and this skill does not apply. Distinguish "I want it perfect" from "I have not verified it works" — the first is the tension, the second is the standard.

Lab versus prod is the deciding question. In the lab, ship it. In prod, finish the verification first, then ship it.
