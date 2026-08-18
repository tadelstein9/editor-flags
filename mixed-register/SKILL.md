---
name: mixed-register
description: >
  Flag mixed register in one mouth, chips (not complete sentences), and
  tech-speak drift — grant and workflow language that hides the person.
  Use when a speech jumps dialect, when a draft is fragments, when Tom says
  mixed register, chips, jewelry, process, stream, or tech-speak, or when a
  novel sample is examined for AI tells. Reports. Does not rewrite his
  sentences. Rewrites on the novel wait.
license: Apache-2.0
metadata:
  author: Tom Adelstein
  version: "1.0.0"
---

# Mixed register and chips

This skill owns two tells that populate the novel and the machine's drafts.
Apply to **your** prose and to chat. On his file, flag and report. He judges.
Do not rewrite the novel. Rewrites wait.

The named rules are in this file.

## When

- Before you send a reply
- Before Tom reads a draft you wrote
- When he says **mixed register**, **chips**, **one mouth**, or **jewelry**
- When `writing-pipeline` lands on unmeasured register or chips

## 1. Mixed register — one mouth, one dialect

A recruiter who says *You write calm English* does not say *pathogens were
jewelry on slides* in the next breath. One mouth, one beat, one dialect.

Read the speech or paragraph for:

| tell | what it costs |
|---|---|
| mixed register | the voice feels unstable |
| metaphor drift | a vivid image the next lines do not pay for |
| unstated *we* / *partners* / *money* | no actor |
| category confusion | fame as a gate on articles |
| unsupported leap | two short sentences that fake a therefore |
| tone inconsistency | instruction, gothic, judgment, bureaucracy |
| compression that obscures | a workflow packed into one cryptic clause |

Dialogue does not exempt this. People talk in passives. They do not stack
four dialects in five sentences.

**Tech-speak drift** — the mouth leaves the room and speaks like a grant.
*Process. Stream. Remediation. Partnership. Messaging. Funds do not move.*
Those words name categories, not events. The actor disappears. Ask: who
decides, who worries, what did a person do with their hands. If the speech
cannot answer, it is a meeting agenda, not a scene.

**The fix:** tech-speak → human action. A person in a room, a motive, a
constraint, a consequence. Systems become people. Categories become events.

## 2. Chips — not a complete sentence

A chip is a word or a label standing where a sentence belongs.

> Process. Messaging. Chain-of-custody language.
> Fifty-one thousand words. Headings as headings.

A sentence has a verb and an objective. A chip has neither, or only a noun.

Earned fragments are rare. *He would not say what the three strikes meant*
is a sentence. *He wouldn't say.* is a chip if the objective is missing.

`tom-voice` short declaratives describe narrative cadence. They do not
license chips in exposition, in chat, or in a recruiter's mouth.

## Filters

```
chip-lint FILE
```

Flags sentences with no finite verb, and label-sentences. Does not rewrite.
`scripts/chip-lint`. Tests: `python3 tests/test-chip-lint.py`.

Mixed register has no lint. A person hears the jump. Report it by quoting
the two lines that do not belong in one mouth.

## Report

Name the tell, quote the line, stop. Do not offer a rewrite of his
manuscript until he sets the time.

## What this never does

- It does not rewrite the novel.
- It does not flatten an earned fragment he left on purpose.
- It does not run the filter on his sentences as if they were mine.
