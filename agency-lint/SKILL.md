---
name: agency-lint
description: >
  Flag technical prose that gives a thing the job of a person or the body
  of a traveler: a protocol that decides, a manual that promises, an
  endpoint that serves as, a computer that arrives, a host that knocks, a
  there with no place behind it. Also carries four faults no program can
  see: one verb standing in for a process, a register jump inside a
  sentence, a fact that turns into an instruction without a transition,
  and a state that seems to contradict itself. Use on documentation,
  runbooks, technical chapters and any machine draft about systems, when a
  reader says who is the actor, agency, SSH decides, serves as, arrives,
  gets in, or when the agency-lint program reports. Reports on the
  author's prose. Proposes repairs only on a machine draft.
license: Apache-2.0
metadata:
  author: Tom Adelstein
  version: "1.0.0"
---

# Agency in technical prose

A reader of a technical page has one job: do the work the page describes.
Every sentence that puts the wrong thing in the subject seat makes that
reader translate the sentence back into what happened before they can act
on it. *SSH decides who gets in* has to become *the administrator writes
settings, and sshd, the server program, enforces them when a connection
reaches port 22.* The page should have said that.

The eight families below come from one afternoon, 26 September 2026: a
machine drafted a chapter about hardening a Linux laptop, and the author
sent back each sentence here. Every specimen is real.

## When

- Before a person reads a technical draft you wrote
- After the `agency-lint` program reports, to judge each flag
- On a machine draft, before the voice pass hands it on
- When the reader says *who is the actor*, *agency*, *serves as*,
  *decides*, *arrives*, *gets in*, or *there*

On the author's own file: flag and stop. The author judges. On a draft a
machine wrote: flag, then propose the repair beside it.

## What the program finds

```
agency-lint FILE
agency-lint --rate FILE
```

It reads the grammar with spaCy and flags a subject only when it names a
computer, a program, a protocol, a host, a setting or a document. A person
may decide, and a named person, a company or a government may want. When
the program cannot tell, it stays quiet: a false alarm on the author's own
prose teaches the author to stop reading the report.

### 1. DISGUISED-BE — a thing that "serves as"

> The hardened endpoint serves as the machine a person sits at.

*Serves as*, *acts as*, *functions as*, *plays the role of*: a to-be verb
in a costume. The sentence defines the thing where it should show someone
using it. Name the person and what they do.

> A user works directly on the hardened endpoint.

A person who *served as the first Secretary* held an office. That stays.

### 2. THING-MINDS — a protocol, program or document with a mind

> SSH decides who gets in.
> The ufw manual promises that an active UFW will not flush its chains.

SSH names a protocol. A protocol decides nothing. A manual promises
nothing. Put the person who decides in the subject seat, and let the
program do what programs do: listen, read, enforce, accept, refuse, log.

> You choose which accounts may log in, and sshd, the SSH server program
> on paris-04, enforces your choice.
> The ufw authors write in the manual that an active UFW "will not flush
> the chains when adding or removing rules."

The verbs that need a mind: decide, know, want, think, believe,
understand, remember, choose, promise, teach, hope, expect, trust,
refuse, assume, notice.

### 3. TRAVEL — a network told as a trip

> ...once a computer arrives there.
> paris-07 knocks on port 22.
> Wait 35 seconds and log in again, and paris-04 lets you in.

Computers do not arrive. A client opens a connection, and packets reach a
listening port. A host does not knock or let anyone in: UFW admits or
drops a connection, and sshd accepts or refuses a key. Name the program and
the act.

> Wait 35 seconds and connect again: UFW admits the connection, and sshd
> accepts your key.

*The laptop arrived* reports a parcel, and *Linux has arrived on the
desktop* reports a market. Both stay. The program flags *arrive*, *land*
and *visit* only in a sentence about a network.

### 4. LOOSE-THERE — a place the sentence never named

> ...once a computer arrives there.

A technical sentence anchors every location to a host, a port, a file or
a service. *There* closing a sentence about a network, with no place named,
leaves the reader to guess which one.

> ...once a client opens a connection to port 22 on paris-04.

## What only a reader finds

No parser sees these. Read for them after the program runs.

### 5. One verb for a whole process

> SSH decides who gets in once a computer arrives there.

*Arrives* hides a TCP handshake, the server's host key, a key agreement,
encryption, and only then an authentication dialog. When one verb stands
in for a process the reader has to perform or troubleshoot, name the steps,
and take them from the source, not from memory. The sshd manual gives
them:

> When a client connects, sshd sends its host key, the two sides agree on
> a session key and encrypt the rest of the session, and only then, in the
> words of the sshd manual, "the server and the client enter an
> authentication dialog."

### 6. Two registers in one sentence

> UFW, the firewall that ships with Mint, turns your rule into kernel
> packet filters.

*Ships with* talks like a box on a shelf. *Kernel packet filters* talks
like the source code. The reader hears two voices. Hold one register for
the sentence.

> UFW came installed on paris-04. You write rules in UFW's short syntax,
> and UFW translates each rule into netfilter rules, the packet filters the
> Linux kernel enforces.

### 7. A fact that turns into an instruction without a transition

> paris-04 offers the network one service, SSH, and only one computer needs
> it. You write that sentence as a firewall rule.

The first sentence describes. The second instructs. Between them the reader
loses the frame. Say the turn in words.

> ...and one computer needs it: the command center, paris-06. In this
> section you turn that fact into a firewall rule.

### 8. A state that seems to contradict itself

> A switched-off firewall can carry saved rules, and the moment you enable
> it, UFW loads every one of them.

*Switched off* tells the reader the firewall does nothing. *Loads every one
of them* tells them it stands ready. Both hold, and the reader needs to be
told how.

> An inactive firewall enforces no rule, but it can hold rules someone
> saved earlier, and when you enable UFW, it loads those saved rules along
> with yours.

### Compression

> Start by reading what UFW holds.

One verb, *reading*, for two commands and a distinction between rules in
force and rules on disk. Name the commands and what each shows.

> Run `ufw status verbose` to see whether the firewall runs and what it
> enforces now. Run `ufw show added` to list the rules saved on disk.

## After a correction

When the author sends one sentence back, sweep the whole draft for the same
fault. On 26 September the first correction, *serves as*, led to five more
of the same kind in one section, and *SSH decides* led to four more across
three sections. The author should not have to find each one.

## How it was checked

Before it shipped, the program ran against a large body of published human
prose as a control, not a score. The first version flagged ordinary English
as a fault: people who "served as" officers, a laptop that "arrived" in the
mail. Those false alarms came out before release. Run it against your own
finished writing first; if it flags sentences you would defend, tell it so
in the lists at the top of the program.

Written by **Tom Adelstein**. Apache-2.0.
