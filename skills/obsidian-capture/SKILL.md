---
name: obsidian-capture
description: Writes a note from the current conversation into the Obsidian vault — summarized, linked to related notes, filed by topic. Load when arpatek says to put something in Obsidian, save it to the vault, or add it to the second brain. Not limited to technical subjects.
aliases: [obsidian, capture, second-brain]
---

# Obsidian capture

Compiles a conversation into a vault note. Based on the LLM Wiki pattern: the vault is not a
place to dump transcripts, it is a maintained set of synthesized pages that already contain
the answer.

## Vault location

Read `$OBSIDIAN_VAULT`, falling back to `~/Documents/Vault`. If neither exists, say so and
stop — do not create a vault silently.

Never write to a vault on `/Volumes/` (an SMB mount). Obsidian on a network share risks
corruption on dropped connections. The NAS is a backup target, not the live vault.

## What to write

A note is a synthesized page, not a transcript. It answers a question or explains a thing.

```markdown
---
created: YYYY-MM-DD
tags: [topic, subtopic]
---

# Title stating the subject, not the conversation

One-paragraph answer up front. What this is and why it matters.

## Detail

The substance, in his voice — direct, no filler. Commands and paths in code blocks.
Structured comparisons in tables.

## Related

- [[Adjacent note]]
- [[Another note]]
```

## Rules

**Synthesize, don't transcribe.** "We talked about X" is worthless in six months. Write what
was concluded and why, as a standalone page.

**Link before creating.** Search the vault for related notes first (`grep -ril` over the
vault, or read the folder listing). Link to what exists. A `[[link]]` to a note that does not
exist yet is fine — it marks a page worth writing, which is how the graph grows.

**One note, one subject.** A conversation covering three things becomes three notes with links
between them, not one note with three headings.

**Update over duplicate.** If a note on the subject exists, edit it. A second note on the same
topic splits the graph and both copies go stale.

**Not everything is technical.** Recipes, travel notes, a book argument, a medical detail worth
remembering — the vault is a personal reference, and a note about a fermentation schedule is
as valid as one about SELinux contexts. Do not editorialize about what belongs.

**Offline-first.** Every note must be readable and useful with no network. No links to content
that only exists behind a URL — quote the substance, cite the source below it.

## Filing

Shallow topic folders, one level deep — never a nested tree. A note is usually about several
things at once, and a tree forces one category; tags and links carry the cross-cutting
structure instead. A new subject gets a new top-level folder.

```
Vault/
├── Homelab/        # infrastructure, services, audits
├── Linux/          # Linux and RHCSA reference
├── Meta/           # vault and tooling notes
├── Todo/           # action lists and backlogs, one per subject
├── Daily/          # optional, date-stamped
└── Attachments/    # images and files
```

Folders and files are both Title Case with spaces (minor words lowercase unless leading;
preserve literals like `home.arpa`, `systemd`, `SELinux`, `iMessage`). An action list or
backlog split from a note goes in `Todo/`, not beside the reference note.

Read the existing folder layout before filing — match a folder that fits, add a new top-level
one only when the subject is genuinely new.

## After writing

Report the path written and the links created, one line. If a `[[link]]` points at a note that
does not exist yet, say which — those are the next pages worth compiling.
