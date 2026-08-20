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
```

| program | what it prints |
|---|---|
| `had-lint` | *had* + participle. Ask: where is the later past? |
| `that-lint` | *that/who/which* + *had(n't)* + participle |
| `chip-lint` | labels and stretches with no finite verb |

`chip-lint` reads the verb with spaCy where spaCy is installed, and falls back to a word list where it is not. Every report names which test produced it, and `chip-lint --how FILE` says so before it reads anything.

```
~/pipeline-venv/bin/python -m pip install spacy click
~/pipeline-venv/bin/python -m spacy download en_core_web_sm
```

The fallback list holds about sixty verbs. It misses *spoke*, *rebuilt*, *rode*, *walks*, *opens* and most irregular simple past, so it reports fragments that are whole sentences, and it is blindest on third person and simple past. Counts from a fallback run read high. Install the parser before you trust a number.

`chip-lint` skips markup, quoted speech and wholly italic lines. People speak in fragments, a `<div>` is a typesetting instruction, and an italic line is usually something the writer is reporting rather than writing.

Mixed register and tech-speak have no program. One mouth, one dialect. If the speech cannot name who acts, it is a meeting agenda. Put a person in a room, with a motive, a constraint, and a consequence.

```
python3 tests/test-had-lint.py
python3 tests/test-that-lint.py
python3 tests/test-chip-lint.py
```

Twenty-one checks. All twenty-one passed on the tree that shipped.

## Skills

Copy each folder into the skills directory your agent reads, or:

```
npx skills add tadelstein9/editor-flags
```

- `tense-normalize` — simple past unless a time shift must be marked
- `expository-phrase` — gather, verb, objective; cut tautology and needless *that*-clauses
- `mixed-register` — one mouth, no chips, tech-speak becomes human action

On a file the author wrote, flag and stop. The author judges. Do not write past perfect in a new draft. Editors flag it.

## License

Apache-2.0. Written by Tom Adelstein.
