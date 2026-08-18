---
name: tense-normalize
description: >
  Keep narrative and conversation in one clean past unless a time shift must be
  marked. Sweep unanchored had + participle, dialogue tags, and had been +
  passive. Use on every draft this seat writes, every reply to Tom, and when he
  says past perfect, sweep had, or tense normalization.
license: Apache-2.0
metadata:
  author: Tom Adelstein
  version: "1.0.0"
---

# Tense normalization

Apply to **your** sentences — drafts and chat. Never rewrite Tom's prose.
On a file of his, run the lints and report. He judges.

**Do not write past perfect.** Editors flag it. Simple past is the habit.
Reach for *had* + participle only when a later past is sitting in the
sentence and the earlier event must be marked. If you typed *had ended*,
*had said*, or *had been hired*, take the *had* off before you send.

The named rules live in the table in this file.
This skill is the trigger.

## When

- Before you send a reply that contains a past-tense sentence
- Before Tom reads a draft you wrote
- When he says **sweep had**, **past perfect**, or **tense normalization**
- When `writing-pipeline` lands on unmeasured tense

## The test

For every `had` + participle: is there a later past this one sits before,
stated in or next to the sentence? If not → simple past.

Past perfect with no later past leaves the **timeline floating with no anchor**.

## Subtypes (same test)

| name | tell | fix |
|---|---|---|
| unanchored past perfect | *Mass had ended* | *Mass ended* |
| two *had*s, one moment | *had ended. The organ had stopped* | join; simple past |
| aspectual redundancy / drift | *had mostly stopped … by 1972* | the time phrase already sequences |
| dialogue tag (stricter) | *John had said* | *John said* — the talk is the now |
| double distance | passive + past perfect | simple past — the stack is remote and bureaucratic |
| unmotivated aspect shift | *He had been hired so money could move* | *He was hired* or name the hirer |
| temporal over-marking | *had* plus *after/before/by/until* | drop *had* |
| passive-voice inflation | *had been* + participle | drop *had*; name the actor if you can |

Possession (`had a book`) and obligation (`had to leave`) are not past perfect.

## Filter

```
had-lint FILE
```

Flags. Does not rewrite. `scripts/had-lint`. Tests: `python3 tests/test-had-lint.py`.

On chat, sweep without the program: if you typed *had* + a verb, run the test
before you send.

## What this never does

- It does not delete every past perfect. An earlier event with a later past stays.
- It does not rewrite the author's sentences.
- It does not treat *had* + noun as a hit.
