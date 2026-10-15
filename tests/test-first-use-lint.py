#!/usr/bin/env python3
"""Tests for first-use-lint. Run: python3 tests/test-first-use-lint.py

The FLAG cases come from a Linux book drafted 26-28 September 2026: the
page used "port" in section 2.1 and explained it only in 2.3, and the
author caught it by asking. The CLEAN cases are sentences from the same
book after the author asked for every word to be cleared where the reader
meets it. A filter that flags a cleared word teaches the writer to stop
reading it.
"""
import importlib.machinery
import importlib.util
import os
import sys
import tempfile

spec = importlib.util.spec_from_loader(
    "firstuselint",
    importlib.machinery.SourceFileLoader(
        "firstuselint", os.path.join(os.path.dirname(__file__), "..", "scripts", "first-use-lint")),
)
f = importlib.util.module_from_spec(spec)
spec.loader.exec_module(f)

TERMS = f.trade_terms([])


def run(text, known=()):
    with tempfile.NamedTemporaryFile("w", suffix=".md", delete=False) as fh:
        fh.write(text)
        path = fh.name
    try:
        return {r[2].lower(): r[1] for r in f.scan(path, TERMS, set(known))}
    finally:
        os.unlink(path)


FAILS = 0


def check(name, got, want):
    global FAILS
    if got != want:
        FAILS += 1
        print(f"FAIL  {name}: got {got!r}, want {want!r}")
    else:
        print(f"ok    {name}")


# FLAG: the fault the program exists for.
r = run("SSH listens on port 22 at every address inspiron holds.\n")
check("port used, never explained", r.get("port"), "UNEXPLAINED")

r = run("SSH listens on port 22 at every address.\n\n"
        "A program that waits for connections listens on a port, a number from 0 to 65535.\n")
check("port explained two paragraphs late", r.get("port"), "LATE")

r = run("Run `ss -tln` and read the list.\n")
check("command with nothing beside it", r.get("ss"), "UNEXPLAINED")

# CLEAN: the shapes a writer uses to clear a word.
r = run("A program that waits for connections listens on a port, a number from 0 to 65535.\n")
check("apposition clears port", r.get("port"), "OK")

r = run("You keep your key on the command center, and sshd, the SSH server program, accepts it.\n")
check("apposition clears sshd", r.get("sshd"), "OK")

r = run("The `ss -tln` command lists every program waiting on this computer.\n")
check("command verb clears ss", r.get("ss"), "OK")

r = run("The Internet Assigned Numbers Authority, IANA, keeps the public list.\n")
check("words before an acronym clear it", r.get("iana"), "OK")

r = run("SSH, short for Secure Shell, lets you log in to one computer from another.\n")
check("short for clears SSH", r.get("ssh"), "OK")

r = run("Every command hands back a number when it finishes, its exit code, and 0 means success.\n")
check("name after its description clears exit code", r.get("exit code"), "OK")

r = run("A tunnel, which SSH calls a port forward, carries a second connection inside the first.\n")
check("'calls' clears port forward", r.get("port forward"), "OK")

r = run("An SSH key takes the place of a password you type.\n")
check("'takes the place of' clears SSH key", r.get("ssh key"), "OK")

# IGNORED: what is not the writer's prose, and plain English.
r = run("## 2.1 The port\n\n```\n$ ss -tln\nLISTEN 0 4096 0.0.0.0:22\n```\n")
check("headings and fenced code are not prose", r, {})

r = run("Treat the stick like a house key: whoever holds it can log in.\n")
check("a house key is plain English", r.get("key"), None)

r = run("SSH listens on port 22.\n", known={"port", "ssh"})
check("--known skips a term an earlier chapter cleared", r.get("port"), None)

# LEDGER: a word one chapter explains stays quiet in the next.
with tempfile.TemporaryDirectory() as d:
    ch2 = os.path.join(d, "chapter-02.md"); ch3 = os.path.join(d, "chapter-03.md")
    ledger = os.path.join(d, "cleared-terms.tsv")
    open(ch2, "w").write("A program listens on a port, a number from 0 to 65535.\n")
    open(ch3, "w").write("optiplex-9020 listens on port 22.\n")
    import contextlib, io
    with contextlib.redirect_stdout(io.StringIO()):
        f.main(["--emit", ledger, ch2])
    known = {w.lower() for w in f.load_list(ledger)}
    rows = {r[2].lower(): r[1] for r in f.scan(ch3, TERMS, known)}
    check("--emit then --known carries port to the next chapter", rows.get("port"), None)
    line = open(ledger).read().strip()
    check("ledger names the chapter and line", line, "port\tchapter-02.md\t1")

print()
print("all passed" if not FAILS else f"{FAILS} failed")
sys.exit(1 if FAILS else 0)
