---
name: repeat-lint
description: >
  Flag a word used twice in one sentence, and sentences in a row that open
  the same way. Repetition hypnotizes the reader: the second "computer"
  in "back up each computer to a different computer" turns the sentence
  into a drone. Use on any draft before a person reads it, on chapters,
  documentation, letters and articles, when a reader says repetitious,
  repetition, same word, hypnotizes, or when the repeat-lint program
  reports. Reports on the author's prose. Proposes repairs only on a
  machine draft.
license: Apache-2.0
metadata:
  author: Tom Adelstein
  version: "1.0.0"
---

# Repetition in prose

A reader who meets the same word twice in one sentence stops reading the
sentence and starts hearing it. L. Ron Hubbard observed that repetition
hypnotizes: the attention goes dull, and the page goes past unread. The
writer cannot hear it in his own draft, because he knows what each word
means. A program points at it. A person picks the other word.

The author named the rule on 1 October 2026, reading a Linux book in
draft: "Back up each computer to a different computer." His note: "computer is
repetitious." The sweep that followed changed about 300 sentences across
ten chapters. Every specimen below comes from that sweep.

## When

- Before a person reads a draft you wrote
- After the `repeat-lint` program reports, to judge each flag
- On a machine draft, before the voice pass hands it on
- When the reader says *repetitious*, *same word*, *you said that*, or
  *hypnotizes*

On the author's own file: flag and stop. The author judges. On a draft a
machine wrote: flag, then propose the repair beside it.

## What the program finds

```
repeat-lint FILE
repeat-lint --keep LIST FILE      a book's fixed names, one to a line
repeat-lint --names FILE          also flag proper names
```

| Flag | Meaning |
|---|---|
| REPEAT | a word of five letters or more used twice in one sentence; plurals count (computer, computers; copy, copies) |
| OPENER | two sentences in a row, in one paragraph, open with the same words |
| RUN | three sentences or more in a row open with the same word (not *The*) |

It skips code, command output, tables, headings, block quotes, list items
for openers, and anything inside quotation marks.

## The repairs that worked

Pick the lightest repair that keeps the fact true. In order:

1. **A pronoun or "one."** The noun already stands in the sentence.
   - *Schedule an undo command, a command that puts the old settings back*
     → *an undo command, **one** that puts the old settings back*
   - *a backup on the same disk dies with that disk* → *dies with **it***
2. **A true synonym.** Check that it still states the fact.
   - *Back up each computer to a different computer*
     → *Back up each **server** to a different **system***
   - *a Git server, a computer that keeps every version* → *a **system** that keeps*
   - *sshd reads the files in order ... for each setting* → *for each **option***
3. **Cut the second one** when the reader already has it.
   - *paris-04 still found the domain's Administrator account* → *found **its** Administrator account*
   - *the list of timers systemd starts at boot, and systemd starts it* → *the list systemd works through at boot, and the timer starts*

A synonym must not change the fact. *Machine* stays out of a book that
banned it. *Server* for a laptop may mislead; *system* will not. A
technical term the reader must learn, *token*, *claim*, *domain*, keeps
its name; repair the other word in the sentence instead, or recast.

For OPENER and RUN, vary the subject or join the sentences:
*The node exporter counts the numbers. The node exporter publishes them*
→ *The node exporter counts the numbers and publishes them.*

## What stays

- **Proper names.** *the Linux Foundation's home for Linux* names two
  things. The program leaves names alone unless you pass `--names`; then
  repair only where a pronoun reads clean (*Kubernetes, and **it** runs
  on Linux*).
- **Names the author asked to repeat.** Full exam names, *the Certified
  Kubernetes Administrator exam*, stay full every time. A book's fixed
  name, *command center*, goes in the `--keep` list.
- **Terms of a system's own vocabulary.** PAM's stacks are named
  *account* and *password*: *Password changes the password* stays.
- **Quotations and command output.** They stay as written.
- **A deliberate pair.** *A rule you have never seen fire carries the
  same doubt as a backup you have never restored.* The parallel carries
  the point. The author decides; the drafter asks.

## Never

- Never run it on the author's sentences to rewrite them. Flag and stop.
- Never fix a repeat by reaching for a word that changes the fact.
- Never trade one repeat for another: read the whole sentence after the
  repair.

Pairs with `agency-lint` (who acts) and `first-use-lint` (does the page
say what the word is). Run all three before a person reads the draft.
