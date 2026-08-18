---
name: expository-phrase
description: >
  Expository phrasing from the te'amim: nouns, adjectives and clauses before
  the verb, then a concluding phrase as the objective. Cut tautology and
  needless that-clauses. Use on exposition this seat writes, on conversation
  with Tom, and when he says phrasing, that-clause, or objective. Chips and
  mixed register live in mixed-register.
license: Apache-2.0
metadata:
  author: Tom Adelstein
  version: "1.0.0"
---

# Expository phrasing

Apply to **your** exposition and to chat. Never rewrite Tom's sentences.
On a file of his, flag and report. He judges.

The named rules are in this file.

## When

- Before you send a reply (this conversation is not exempt)
- Before Tom reads exposition you drafted
- When he says **phrasing**, **that-clause**, or **objective**

## The form

Gather, then the verb, then the objective.

Nouns, adjectives, and clauses stand in front of the verb and say who and
under what. The verb does the work. The last phrase is what the sentence is
for. The sentence finishes.

Not a missing objective:

> He would not say.

→ *He would not say what the three strikes meant.*

## Two kinds of doubling

**Tautology** — one beat, two sentences. *Mass had ended. The organ had stopped.*
→ *Mass ended and the organ stopped.* Strunk 17: omit needless words.

**Needless relative clause** — a *that/who/which* clause whose meaning is
already one adjective. Negative padding when *hadn't* restates what
*un-* already said.

> towns that hadn't touched the sickness
> → towns untouched by the sickness

Keep the clause when it adds an actor, a time, or a fact the adjective
cannot hold.

**Kaful** (synonymous parallelism) is the other doubling: one thought in two
members, on purpose. Laborious if the second member does not turn the thought
or land the objective. Not the same as crutch *double words* (*still*,
*already*, *just*).

Chips and mixed register: `mixed-register`.

## Filter

```
that-lint FILE
```

Flags `that/who/which` + `had(n't)` + participle. Does not rewrite.
`scripts/that-lint`. Tests: `python3 tests/test-that-lint.py`.

## What this never does

- It does not flatten a long subject that gathered, verbed, and landed.
- It does not strip every *that*.
- It does not rewrite the author's prose.
- It does not treat *phrase-lint*'s "verb held back" as a ban on this form.
