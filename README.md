# Editor flags

Three skills and three programs that flag what an editor flags: unanchored past perfect, chips that are not sentences, and a mouth that leaves the room.

They report. They do not rewrite the file.

## The week

A writer sat with a finished chapter and a list of *had* + participle. Editors mark that tense when no later past sits in the sentence. The same pages held labels (*Process. Messaging.*) and grant talk (*program stream*, *heritage remediation*) where a person in a room should have spoken.

The wall is the habit. A model reaches for *had ended* and *had been hired* because the extra tense sounds careful. A recruiter in a scene starts talking like a grant. Detectors and word lists do not catch this. An editor does.

## What to run

```
scripts/had-lint FILE
scripts/that-lint FILE
scripts/chip-lint FILE
scripts/rhythm-lint FILE
```

| program | what it prints |
|---|---|
| `had-lint` | *had* + participle. Ask: where is the later past? |
| `that-lint` | *that/who/which* + *had(n't)* + participle |
| `chip-lint` | labels and stretches with no finite verb |
| `defensive-lint` | prose that protects the writer instead of informing the reader |
| `nothing-lint` | the absolute negative used as emphasis |
| `agency-lint` | a protocol, program or document doing what only a person does; a network told as a trip |
| `first-use-lint` | a trade word, a command or an acronym the reader meets before the page says what it is |
| `repeat-lint` | a word used twice in one sentence; sentences in a row that open the same way |
| `reader-lint` | a vague word or a short form that leaves the reader asking "what?" |

`chip-lint` reads the verb with spaCy where spaCy is installed, and falls back to a word list where it is not. Every report names which test produced it, and `chip-lint --how FILE` says so before it reads anything.

```
~/pipeline-venv/bin/python -m pip install spacy click
~/pipeline-venv/bin/python -m spacy download en_core_web_sm
```

The fallback list holds about sixty verbs. It misses *spoke*, *rebuilt*, *rode*, *walks*, *opens* and most irregular simple past, so it reports fragments that are whole sentences, and it is blindest on third person and simple past. Counts from a fallback run read high. Install the parser before you trust a number.

`defensive-lint` hunts the armor a writer puts around a claim: hedge labels (*Limit:*, *Caveat:*), concessions (*that said*, *it is worth noting*), restatement (*in short*, *to be clear*), epistemic hedges (*arguably*), disclaimers, and negative definition — but only where a replacement follows. *"This is not X, it is Y"* hides a claim. *"A partner is not a friend"* is a figure. Length does not separate them; the replacement does.

`--rate` prints flags per 1,000 words. One author's 379,005 published words run 0.31, his novel 0.22, and a machine-written analysis of the same material ran 2.98 before it was cut. Measure your own corpus before trusting anyone else's band.

Both programs skip markup, quoted speech and wholly italic lines. People speak in fragments, a `<div>` is a typesetting instruction, and an italic line is usually something the writer is reporting rather than writing.

`agency-lint` flags a technical sentence that gives a thing the job of a person or the body of a traveler: *SSH decides*, *the manual promises*, *the endpoint serves as*, *a computer arrives there*, *precision knocks on port 22*. It reads the grammar with spaCy and flags a subject only when it names a computer, a program, a protocol, a host, a setting or a document; when it cannot tell, it stays quiet. Before release it ran against published human prose as a control, and the false alarms it raised there came out. Its skill carries four faults no parser sees: one verb standing in for a process, two registers in one sentence, a fact that turns into an instruction without a transition, and a state that seems to contradict itself.

`first-use-lint` follows L. Ron Hubbard's study rule from the writer's side: a reader who passes a word he does not understand blanks the rest of the page, so the page clears each word where the reader meets it. It lists every trade word, inline command and acronym at its first use, and reports UNEXPLAINED when the page never says what the word is, and LATE when it says so only after the reader met it. It counts an explanation when the sentence carries one of a few fixed shapes: an apposition (*a port, a number from 0 to 65535*), a name after its category (*a program named sshd*), *short for*, *means*, *calls*, or the words an acronym stands for right before it. `--known LIST` skips terms an earlier chapter cleared; `--terms LIST` adds a book's own. A shape proves nothing about whether the explanation works; a person judges that.

`repeat-lint` follows Hubbard's observation that repetition hypnotizes the reader. It flags a word of five letters or more used twice in one sentence, plurals counted as the same word, and two sentences in a row that open with the same words, or three that open with the same word. It skips code, quotations, tables, block quotes and names; `--names` checks names too, and `--keep LIST` spares a book's fixed names. The skill file lists the repairs that worked, in order: a pronoun, a true synonym, a cut. A synonym that changes the fact is no repair; a person judges.

`reader-lint` flags the words a reader stopped at: a vague word (*the drop*, *a watcher*, *would hurt*, *the room*, *a road*) with the question the reader asked, and a short form the book spells out every time (`--short LIST`, one entry to a line, regular expressions allowed). Its skill, `reader-questions`, carries the reading no program can do: a missing object, a missing place, a list that names no item, a figure of speech, a paragraph that confuses.

Mixed register and tech-speak have no program. One mouth, one dialect. If the speech cannot name who acts, it is a meeting agenda. Put a person in a room, with a motive, a constraint, and a consequence.

```
python3 tests/test-defensive-lint.py
python3 tests/test-had-lint.py
python3 tests/test-that-lint.py
python3 tests/test-chip-lint.py
python3 tests/test-nothing-lint.py
python3 tests/test-agency-lint.py
python3 tests/test-first-use-lint.py
python3 tests/test-repeat-lint.py
python3 tests/test-reader-lint.py
```

Ninety-five checks across six programs. All ninety-five passed on 26 September 2026.

## Skills

In Claude Code, add the repository as a plugin marketplace, then install:

```
/plugin marketplace add tadelstein9/editor-flags
/plugin install editor-flags@editor-flags
```

Or copy each folder into the skills directory your agent reads, or:

```
npx skills add tadelstein9/editor-flags
```

The skills call the programs in `scripts/`, so put that folder on your `PATH`.

- `rhythm` — one thesis for the piece, a topic sentence plus two supports for each paragraph; `rhythm-lint` tests the marked thesis and flags sound echoes such as *an owner … an older Dell*
- `repeat-lint` — the same word twice in one sentence, and sentences in a row that open the same way
- `reader-questions` — the words a reader stops at
- `secondhand-witness` — a reporter's account in the author's voice
- `tense-normalize` — simple past unless a time shift must be marked
- `expository-phrase` — gather, verb, objective; cut tautology and needless *that*-clauses
- `mixed-register` — one mouth, no chips, tech-speak becomes human action
- `agency-lint` — who acts in a technical sentence: the person decides, the program enforces, the connection reaches a port

On a file the author wrote, flag and stop. The author judges. Do not write past perfect in a new draft. Editors flag it.

## License

Apache-2.0. Written by Tom Adelstein.

## A warning about `--fix`

`had-lint --fix` and `that-lint --fix` write into the file. They are for a
machine draft. Between 2026-08-18 and 2026-08-20 `had-lint --fix` carried
a defect that reversed meaning: an intervening word between *had* and the
participle was captured and then discarded, so

    The job had not left his mouth.      became  The job left his mouth.
    She had not seen him since Tuesday.  became  She saw him since Tuesday.
    They had never spoken of it.         became  They spoke of it.

It now handles negation, and any intervening word it does not recognise
makes it leave the sentence alone rather than delete a word. Six tests
cover it. If you ran `--fix` in that window, check your file for a
sentence that says the opposite of what you wrote.

And a second caution the same run turned up. Run over a chapter of a
finished novel, `--fix` broke parallel constructions — where the author
wrote *"He had not understood. He had only wanted walls…"* it changed the
first clause and left the second, and the two no longer answer each
other. These programs are built to read a machine draft. Point them at
finished human prose and they will flatten what the writer did on
purpose.

## `nothing-lint`

A positive claim costs you a fact. *Your manuscript stays on the disk in your room* can be checked — somebody walks over and looks. *Nothing leaves it* asserts a proposition about the entire universe of things that did not happen. It sounds heavier and commits to less. The absolute negative buys the tone of a guarantee at the price of a guarantee.

Occurrences per 1,000 words:

| | |
|---|---|
| a finished novel | 0.16 |
| Douglass, *Narrative* | 0.17 |
| Dickens, *Great Expectations* | 0.20 |
| Twain, *Huckleberry Finn* | 0.23 |
| the same author's 379,005 published words | 0.25 |
| Austen, *Pride and Prejudice* | 0.32 |
| a page of machine-written product copy | 2.65 |
| six machine-written video captions | **64.52** |

Six writers, two centuries, four genres, inside a sixth of a point of each other. Sixty-two words of machine caption held four.

**Ordinary negation stays.** *He did not answer* is a fact about a man. *Nothing answered* is a claim about the world. The program hunts the second.

**The fix is a replacement, not a deletion.** Say what does happen.

| was | became |
|---|---|
| Nothing leaves the building. | Your pages stay on that disk. |
| Not one of them rewrites a word. | Each one hands you a line number and stops there. |
| Nothing leaves it. | Your manuscript stays on it. |

```
python3 tests/test-nothing-lint.py
```
