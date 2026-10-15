---
name: rhythm
description: >
  Give expository prose its order: one thesis for the whole piece, and a
  topic sentence at the head of each paragraph with two sentences that
  support it. Use when drafting or reading any piece that explains,
  informs or directs: a chapter, an article, a Substack piece, a README,
  a letter, a proposal. Use when a reader says it rambles, has no point,
  lacks rhythm, reads choppy, feels disorganized, or asks for a thesis or
  topic sentence, and when the rhythm-lint program reports. Pairs with
  dopamine-hook, which governs the opening grab and the closing hook.
  Reports on the author's prose. Drafts in this form only when asked to write.
license: Apache-2.0
metadata:
  author: Tom Adelstein
  version: "1.0.0"
---

# Rhythm in expository prose

Rhythm in exposition comes from order. The reader learns the point of the
whole piece in one sentence, then meets each paragraph's point in its first
sentence, then reads two sentences that support it. The pattern repeats,
and the repetition carries the reader forward. A paragraph that opens on a
detail breaks the beat: the reader holds the detail and waits to learn why
it matters.

The author learned this form as a freshman at the University of Texas in
1966 and set it aside for forty years of deadline writing. He named the
gap on 13 October 2026, reading the opening of a Linux book: "The rhythm
needs a topic." Every rule below traces to a printed source, and each
source sits in `references/sources.md` with its page.

## Why a model needs this file

A model writes one word at a time, choosing each by the words before it.
That process keeps neighboring sentences smooth. It holds no plan for the
whole piece, so a model drafts paragraphs that connect to each other and
point nowhere. Much of the prose a model learned from comes from magazines,
where writers skip the topic sentence (Braddock 1974 found 13% of paragraphs
opening with one). A model copies that habit. This file supplies the plan
the process lacks.

## The thesis

James McCrimmon defined it in *Writing with a Purpose* (3rd ed., 1963,
p. 40), a leading freshman text of that decade:

> "A thesis is a single sentence, preferably a simple sentence, which
> expresses the basic idea the paper is to develop. The thesis is to the
> whole paper what the topic sentence or topic idea is to the paragraph."

> "A good thesis is restricted, unified, and precise."

The four tests, in his words and in practice:

| Test | McCrimmon | Ask of the sentence |
|---|---|---|
| Single | "a single sentence, preferably a simple sentence" | One sentence? One main clause? |
| Restricted | it "limits the scope of the paper to what can be properly discussed in the space available" | Can this piece, at this length, deliver it? |
| Unified | it commits the writer "to deal with only one dominant idea" | Does it make one claim, or two joined by *and*? |
| Precise | "words which permit only one interpretation" | Could a reader take any word two ways? |

**The thesis covers the whole piece.** Every section develops some part of
it, and no section strays outside it. After drafting, read the headings
against the thesis. A section the thesis does not cover means one of two
repairs: widen the thesis to hold it, or cut the section. In the first test
of this skill, a draft on Texas law stated "two things: trained employees
and prompt reports," then spent half its length on the State's framework,
which the thesis never mentioned.

**A thesis that fails unity**, from the first draft of the book's Chapter 1:

> The City of Calder called your firm because the state's Cybersecurity
> Planning Committee gives grant priority to projects that retire
> unsupported software, and the clerk still works on a Windows 10 computer.

Two claims, a grant rule and an old computer, joined by *and*. McCrimmon's
own example fails the same way: "The United Nations Organization has major
weaknesses and cannot prevent a major war." His repair shows the relation
in one clause: "The organization of the UN makes it incapable of preventing
a war between major powers."

**A thesis that passes**, the author's words joined, 13 October 2026:

> We bring a public office's existing infrastructure up to the State's
> cybersecurity standard.

One simple sentence. One claim. "Existing" restricts it: the office keeps
its computers. "The State's cybersecurity standard" names one thing, the
Texas Cybersecurity Framework.

## The paragraph

Each paragraph does for its own idea what the thesis does for the piece.

1. **The topic sentence comes first.** Alexander Bain set the rule in 1866:
   "The opening sentence, unless so constructed as to be obviously
   preparatory, is expected to indicate with prominence the subject of the
   paragraph" (*English Composition and Rhetoric*, Rule III, p. 150).
   William Strunk gave the reason in 1918: "Again, the object is to aid
   the reader" (*The Elements of Style*, Rule 9).
2. **Two sentences support it.** Each explains, proves or shows the topic
   sentence. Francis Christensen numbered a paragraph's sentences by level
   of generality (*CCC*, May 1966, p. 61). In his terms, the house
   paragraph runs **1 2 2**: the topic at level 1, two supports at level 2,
   each a comment on the topic and equal to the other.
3. **One idea per paragraph.** Bain, Rule V, p. 151: unity "forbids
   digressions and irrelevant matter." A second level-1 sentence in the
   middle starts a new topic, so it starts a new paragraph.
4. **The last sentence lands.** Strunk: the final sentence "either
   emphasizes the thought of the topic sentence or states some important
   consequence." It never ends on a digression or a stray detail.

Two supports set the floor, not the ceiling. A paragraph may carry three
when the topic needs them. It may not carry a second topic.

**A paragraph that opens on a detail:**

> The Dell Inspiron 5567 still ran Windows 10, and Microsoft's engineers
> stopped sending it security updates in October 2025.

The reader meets a model number and a date and has to guess the point.

**The same material with its topic first:**

> The clerk's computer no longer met the State's standard. Her Dell
> Inspiron 5567 still ran Windows 10, and Microsoft's engineers stopped
> sending it security updates in October 2025. It could not move to
> Windows 11, which demands a newer processor than the Inspiron carries.

Topic, then two supports. The model number and the date now prove a point
the reader already holds.

## The whole shape

Exposition for today's reader opens and closes with the attention devices
of `dopamine-hook` and keeps this form between them.

1. **The grab.** A scene, an image or a charged line. Readers decide in
   about a second whether to stay. Bain allowed an opening "obviously
   preparatory," and a grab fits that allowance.
2. **The thesis.** One sentence, after the grab. In the author's LUC
   articles it closes the opening scene.
3. **The body.** Paragraphs in 1 2 2 form, each topic sentence serving
   the thesis. Headings group them.
4. **The hook.** The last line states a consequence, as Strunk asks, and
   leaves one question open so the reader wants the next piece.

The grab wins the reader. The topic sentences keep the reader. The reading
studies that Frank D'Angelo surveyed in 1986 found that readers recall more
and read faster when each paragraph opens with its topic (*CCC* 37.4,
pp. 435–439).

## What the published record shows, and why the rule stands

Braddock studied twenty-five essays from *The Atlantic*, *The New Yorker*
and two other magazines. Only 13% of the paragraphs opened with a topic
sentence. Writers cite that figure to retire the rule. Three answers keep it:

- **Braddock himself** wrote that those essays "would have been clearer and
  more comfortable to read if the paragraphs had presented more explicit
  topic sentences" (quoted in D'Angelo, p. 435).
- **Smith (2008)** replicated the study on history articles and counted by
  block, a run of short paragraphs under one topic. Two thirds of the
  blocks opened with the topic (*Reading Matrix* 8.1, p. 85).
- **Christensen** on copying published prose: "We cannot base our teaching
  on such models" (p. 66).

The rule rests on the reader, not on the habits of magazine writers.

## How to use it

**When asked to write.** Before the first sentence, write the thesis and
test it against the four tests. Put `<!-- thesis -->` on the line above it. List each paragraph's topic sentence under
it, in order. Read that list alone: it should argue the thesis by itself.
Then draft each paragraph as a topic sentence and two supports. When a
paragraph shows a command, state the topic before the command and let the
output support it after. Last, read the headings against the thesis. Follow
`tom-voice` for the sentences.

**When reading a draft.** Find the thesis. Underline each paragraph's first
sentence and read those alone. Report where the list breaks: a paragraph
that opens on a detail, a paragraph with two topics, a paragraph whose
topic does not serve the thesis.

**On the author's own prose.** Report in the chat. Never rewrite a sentence
he wrote. He decides.

## The program

`rhythm-lint FILE` reports. It never rewrites. A person decides each flag.

| Rule | Flags | Source |
|---|---|---|
| WRONG-PREP | a person and a computer joined by the wrong preposition: "works at a Dell" | Tom, 13 Oct 2026: a person works on a computer |
| NO-TOPIC | a paragraph whose first sentence carries a figure, a model number or a date | Tom, 13 Oct 2026; Bain Rule III |
| THESIS-TWO | two main clauses in the thesis, each with its own subject | McCrimmon: "only one dominant idea" |
| THESIS-COMPLEX | a clause hung on the thesis's main clause | McCrimmon: "preferably a simple sentence" |
| THESIS-VAGUE | *things*, *issues*, *various*, *aspects* and their kin in the thesis | McCrimmon: "words which permit only one interpretation" |

**Mark the thesis.** Put `<!-- thesis -->` on the line above the thesis.
Markdown hides the mark, so readers never see it. The program tests the
first sentence after the mark, prints it, and asks the restriction question
for a person to answer. With no mark, the report says so and tests nothing.
(Tom, 15 Oct 2026.)

NO-TOPIC flags the sign of a detail, not the absence of a topic. A date can
be the topic. The flag asks a person to look.

NO-TOPIC skips the opening above the thesis mark, where Bain allows a
paragraph "obviously preparatory," and skips text that resumes a paragraph
after a code block. A paragraph that a command interrupts still opens with
its topic sentence before the command.

`rhythm-lint --test` runs the cases in `tests/rhythm/`.

## Open

- **A block test.** Per Smith, judge a run of short paragraphs under one
  topic as one unit.

## Adding a rule

A rule enters when the author rules on a real sentence. Record his words,
the sentence that taught it and the date beside the rule, add a test case
to `tests/rhythm/`, and run the test before the commit.
