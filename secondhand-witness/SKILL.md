---
name: secondhand-witness
description: >
  Find the places where a draft tells someone else's account as the
  author's own memory: a first-person sentence ("I saw", "I watched", "we
  built") whose details, wording or figures came from a reporter, a press
  release or another writer's summary. Use on memoir, author biographies,
  chapter openings that tell the author's story, and any machine draft
  written from a research folder, before the author reads it, when he
  says "I didn't see that", "that's not what happened", "where did that
  number come from", or when the witness-lint program reports. Reports on
  the author's prose. Proposes repairs only on a machine draft. The
  author's memory decides.
license: Apache-2.0
metadata:
  author: Tom Adelstein
  version: "1.0.0"
---

# Someone else's account in the author's voice

A first-person sentence makes a promise: *I was there, and this is what I
saw.* The reader trusts it more than any citation, because the author
vouches for it with his own name. When the details came from a third
party, the page vouches for something the author never said.

A machine drafting from a research folder makes this mistake easily. It
reads a reporter's summary of the author's life, and it writes the
summary down in the author's voice, figures and all.

## The specimen

On 2 October 2026 the author read the first chapter of his Linux book.
Donald K. Rosenberg, writing about Bynari for IBM's partner news, had put
it this way:

> He had been impressed by seeing an ISP host 2 million users on a Linux
> server.
> — Donald K. Rosenberg, "Bynari Finds Missing Link," IBM partner news

The machine draft turned the reporter's sentence into the author's
eyewitness memory:

> I watched one Internet service provider host two million users on a
> single Linux server.

Three things happened in one sentence. *Seeing* became *watched*, an
eyewitness verb. The reporter's *2 million* became the author's figure.
And *a Linux server* became *a single Linux server*, sharper than the
source. The author remembered a rack of Linux servers. The book now
says what he saw, and Rosenberg's figure stays in the research file as
what Rosenberg printed.

## When

- Before the author reads any draft that tells his story from a research
  folder
- After the `witness-lint` program reports, to judge each flag
- When the author says *I didn't see that*, *that's not what happened*,
  or *where did that number come from*

On the author's own file: flag and stop. On a machine draft: flag, then
propose the repair beside it.

## What the program finds

```
witness-lint DRAFT --source FILE [--source FILE ...] [--own FILE ...]
```

A `--source` is a third party's text. An `--own` file is the author's own
record: his articles, his notes. The program reads only first-person
sentences.

### 1. WITNESS-FROM-SOURCE — the wording follows the source

A first-person sentence that shares a run of five words or more with a
source sentence, or six content words.

> I saw the need and started building a substitute for the Exchange
> server.

Rosenberg: *"He saw a critical need and started building a substitute
for the Exchange server."* The author may well remember it the same way.
Ask him. If he does, the sentence is his. If he does not, it is
Rosenberg's.

### 2. NUMBER-FROM-SOURCE — the figure is the source's

A first-person sentence carrying a figure the source printed: *2
million*, *two million*, *30%*, *30 percent*. Keep it only if the author
vouches for it.

### 3. NUMBER-UNSOURCED — no one holds the figure

A first-person sentence carrying a count that no source and no `--own`
file holds. Model numbers (*Digital Equipment 486*, *S/390*) and years
do not flag. Only the author can say where the figure came from.

## The repair, on a machine draft

Two repairs, and the author picks:

1. **His memory.** Ask what he saw, and write that. *I saw one Internet
   service provider host users on a rack of Linux servers.*
2. **The source, named.** If the source's version belongs on the page,
   give it to its writer. *Donald K. Rosenberg wrote for IBM's partner
   news that Bynari's founder "had been impressed by seeing an ISP host 2
   million users on a Linux server."*

Never blend the two: a quotation from the source in the author's voice is
the fault this skill exists to find.

## What only a reader finds

The program matches words and figures. It cannot see a source's
*judgment* told as the author's: a reporter's "a classic case of an
entrepreneur listening to the market" turned into "I listened to the
market." Read each first-person sentence that praises the author or
explains his motives, and ask whose opinion it is.

## Before you run it

An image cannot be read. Transcribe a clipping or a screenshot to a text
file, word for word, with a header naming the writer, the publication and
the file it came from. Then name the text file as the `--source`.

Written by **Tom Adelstein**. Apache-2.0.
