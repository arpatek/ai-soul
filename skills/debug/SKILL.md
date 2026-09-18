---
name: debug
description: arpatek's debugging method — state what is known, what is unknown, and the single next diagnostic step. One hypothesis at a time, no spiraling. Load when investigating a failure, a broken service, unexpected output, or when the user is stuck.
aliases: [diagnose]
---

# Debug

Methodical, not scattershot. The failure mode to avoid is spiraling — trying six things at once and losing track of which one changed the outcome.

## The loop

Every response while debugging states three things, in this order:

1. **Known** — what has been established, with the evidence that established it.
2. **Unknown** — the specific gap that is blocking a conclusion.
3. **Next** — one diagnostic step, and what each possible result would tell us.

That is the whole structure. It fits in five lines and it stops the spiral.

## Rules

**One hypothesis at a time.** Two simultaneous changes mean neither result is interpretable. If two things must be tested, test them in sequence and say which is first.

**A diagnostic step must be able to fail.** "Check the logs" is not a step. "Check whether `journalctl -u foo` shows the unit restarting in the last hour" is — it has a yes and a no, and both are informative.

**Distinguish evidence from inference.** "The service is down" is an inference. "`systemctl status` reports `inactive (dead)`" is evidence. Say which one you have.

**Escalate scope deliberately.** Start at the layer the symptom appeared in. Move outward only when that layer is cleared, and say you are moving.

**Prod versus lab changes the method.** In the lab, trial and error is a legitimate diagnostic. In prod, research first — a wrong guess against a load-bearing service costs more than the time it saved.

## When it is not converging

After three cycles with no narrowing, stop and say so. State what has been ruled out, what remains, and what additional access or information would break the tie. Do not keep proposing steps to look productive.
