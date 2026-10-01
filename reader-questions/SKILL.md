---
name: reader-questions
description: >
  Read a draft as the reader and find every place they would stop and ask
  "what?": a vague word (the drop, a watcher, would hurt), a figure of
  speech where a fact belongs (what stays in the room, a road to the
  Internet), a missing object (needs a person to do what?), a missing
  place (keep it in Git, where?), a certainty word that claims too much
  (when a disk dies, not if), a list that names no item (its numbers,
  what numbers?), and a short form the book spells out (CKA, Mint). Use
  before a person reads any draft this seat wrote, when the reader writes
  WAIT, what's that, what does that mean, or when reader-lint reports.
  Reports on the author's prose. Proposes repairs only on a machine draft.
license: Apache-2.0
metadata:
  author: Tom Adelstein
  version: "1.0.0"
---

# The questions a reader asks

A writer knows what each word means, so no word stops him. The reader
knows only what the page says. Every place the reader has to stop and
ask "what?" costs the page that reader's trust, and a reader who stops
often enough stops reading.

On 1 October 2026 the author read two chapters of a Linux book in draft
and wrote back one stop after another, most of them in capitals: *WAIT
THIS IS CONFUSING*, *WHAT'S THAT? DON'T USE DROP*, *hurt what?*, *a person
to do what?* Every specimen below is one of those stops, with the repair
that answered it.

## When

- Before a person reads any draft you wrote: a chapter, a page, a letter
- After `reader-lint` reports, to judge each flag
- When the reader writes *WAIT*, *what's that*, *what does that mean in
  English*, *what numbers*, or asks a one-word question about a word

On the author's own file: flag and stop. The author judges. On a draft a
machine wrote: flag, then propose the repair beside it.

## The procedure

Read each sentence once as its reader, who knows only the pages before
it. At every word, ask the one question: **what would this reader have to
stop and ask?** Then answer that question on the page, in the sentence,
where the reader meets it. Seven kinds of stop came up, and each has its
repair.

| The stop | Specimen | The reader asked | The repair |
|---|---|---|---|
| **A vague word** | *would have shown the drop* | the drop? what's that? | Say what happened: *paris-07 could not reach the Internet* |
| | *A watcher would have shown* | a watcher of what? | Name the thing: *the monitoring you build in this chapter* |
| **A figure of speech** | *what stays in the room* | what does that mean in English? | Say the fact: *which files each computer backs up, and which system holds each copy* |
| | *the inference server's road to the Internet* | WAIT, this is confusing | *its only connection to the Internet* |
| **A missing object** | *which part of that needs a person* | to do what? | *when something has stopped working and you need to fix it* |
| | *what has failed or would hurt* | hurt what? | *what would stop your work if it broke, such as the backups* |
| **A list that names no item** | *asks every computer for its numbers* | what numbers? | Name them: *how busy the processor runs, how much memory sits free, how much room the disk has left* |
| **A missing place** | *keep it in Git* | where? | *on the lab's Git server, paris-05* |
| **A certainty word** | *what happens when a disk dies* | "if" | A thing that may not happen takes *if* |
| **A short form** | *CKA*, *LFCS*, *Mint* | spell it out | *the Certified Kubernetes Administrator exam*, every time; *Linux Mint* |

A paragraph can stop the reader as a whole. *Your lab holds four computers
... and the lab learned of it hours later, when the author sat down at
paris-06* drew WAIT THIS IS CONFUSING. Write the plain version: one fact
to a sentence, in the order things happened, with the person who acted
named.

## What the program finds

```
reader-lint FILE
reader-lint --words LIST FILE     a book's own vague words, each with its question
reader-lint --short LIST FILE     a book's short forms, each with its full name
```

It flags the vague words and short forms it knows. It cannot see a
missing object, a missing place, a list with no items, a figure of speech
it has never met, or a paragraph that confuses: those take the reading
above. `nothing-lint` catches *nothing* and *nobody* doing the verb, and
`first-use-lint` catches a term the page never explains. Run all of them,
then read.

## What stays

- **A word that names a fact.** UFW *drops* a packet: DROP is the
  firewall's action, and the sentence says so. Keep it. The program skips
  DROP in capitals and systemd's *drop-in* file.
- **Quotations, commands and output.** They stay as written.
- **The author's sentences.** Flag and stop.

## Never

- Never answer the reader's question in chat and leave the page as it was.
  The page has to answer it.
- Never repair a vague word with another vague word. *The drop* becomes
  what happened, not *the outage*.
- Never guess the fact a vague word hid. If the draft does not say what
  happened, find out from the record before you write it.

Pairs with `repeat-lint` (the same word twice), `agency-lint` (who acts)
and `tom-voice`.
