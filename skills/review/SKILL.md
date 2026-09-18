---
name: review
description: arpatek's code review method — direct critique, say what is wrong and why, do not soften it. Ranked by consequence, with the failure each finding causes. Load when reviewing a diff, a file, a PR, or an approach.
---

# Review

Direct critique. Say what is wrong and why. Do not soften it unnecessarily.

## Structure

Findings ranked by consequence, not by order encountered. For each one:

- **What** is wrong, in a sentence.
- **Why** it matters — the concrete failure it produces, with inputs or conditions.
- **Where**, as `file:line`.

A finding that cannot name the failure it causes is a preference, not a finding. Either state the failure or drop it.

## Rules

**Measure before asserting.** "There's a lot of duplication" is an impression. "Four files differing by one comment line, 1,952 lines doing the work of 488" is a finding. Count it.

**Separate severity from taste.** A silent failure path and an inconsistent brace style are not the same category and should not appear in the same list without a marker saying so.

**Say what is right, briefly.** Not encouragement — calibration. A reviewer who only reports problems gives no signal about what to preserve.

**Context changes the verdict.** Archived code is explained, not patched. A prototype is not held to the standard of a load-bearing service. Establish which one this is before the first finding.

**Do not pad.** Five real findings beat fifteen with ten stylistic notes mixed in. If the code is fine, say it is fine.

## What to check first

Silent failure — anything that swallows an error, writes an empty result, or returns success on a failed fetch. In a tool whose job is detecting problems, failing open is the worst available default. Then: unquoted expansions, missing error handling, duplicated state, credentials in argv.
