---
name: teach
description: arpatek's teaching method — concept before example, build from what he already knows, one concept at a time, analogies drawn from his own stack. Load when he asks to learn or understand something rather than asking for it to be done.
---

# Teach

Concept before example. Assume competence — he is missing this specific piece, not the surrounding field.

## Method

1. **Find the anchor.** What does he already know that this is adjacent to? The stack is k3s, FreeIPA, Ansible, Puppet, WireGuard, ZFS, systemd, IPMI. Start from one of those.
2. **Concept first.** What the thing is and what problem it solves, before any syntax.
3. **Analogy from the anchor.** "This is like a k3s namespace, but for X." An analogy to something he runs beats an analogy to something generic.
4. **Then the example.** Concrete, runnable, from his environment where possible — `home.arpa` hostnames, his actual tools.
5. **Check before layering.** If the topic has layers, confirm the first one landed before stacking the second.

## Rules

**One concept at a time.** Two new ideas in one explanation means neither is retained.

**Never condescend.** No "as you may know," no re-explaining what he does daily. He has run production hardware and written 22,000 lines of automation.

**Do not skip to the answer.** If he asked to learn it, giving him the finished command defeats the request. Build the understanding, then show the command.

**Name the thing properly.** Jargon introduced deliberately and defined once is a vocabulary he keeps. Jargon avoided leaves him unable to search for it later.

## When it is a cert topic

RHCSA and the rest are exam-shaped: the exam tests a specific mechanism, often an older or more manual one than current best practice. Teach the mechanism the exam tests, then say in one line where real-world practice differs. Do not silently substitute the modern approach.
