#!/usr/bin/env python3
"""Tests for repeat-lint. Run: python3 tests/test-repeat-lint.py

The FLAG cases come from a Linux book drafted in September 2026. On
1 October the author read "Back up each computer to a different computer"
and said repetition hypnotizes the reader. The CLEAN cases are the same
sentences after the sweep that followed, plus the things the program must
leave alone: code, quotations, tables, lists, names and host names. A
filter that flags those teaches the writer to stop reading the report.
"""
import importlib.machinery
import importlib.util
import os
import sys
import tempfile

spec = importlib.util.spec_from_loader(
    "repeatlint",
    importlib.machinery.SourceFileLoader(
        "repeatlint", os.path.join(os.path.dirname(__file__), "..", "scripts", "repeat-lint")),
)
r = importlib.util.module_from_spec(spec)
spec.loader.exec_module(r)


def run(text, **kw):
    with tempfile.NamedTemporaryFile("w", suffix=".md", delete=False) as fh:
        fh.write(text)
        path = fh.name
    try:
        return [(f[1], f[2]) for f in r.scan(path, **kw)]
    finally:
        os.unlink(path)


FAILS = 0


def check(name, got, want):
    global FAILS
    ok = got == want
    if not ok:
        FAILS += 1
    print(("ok   " if ok else "FAIL ") + name + ("" if ok else f"\n     got  {got}\n     want {want}"))


# --- REPEAT: flagged ----------------------------------------------------
check("computer twice",
      run("Back up each computer to a different computer, because a backup on the same disk dies with it.\n"),
      [("REPEAT", "computer")])
check("plural counts as the same word",
      run("A Git server, a computer that keeps every version, sits beside your computers.\n"),
      [("REPEAT", "computer")])
check("command in an apposition",
      run("Schedule an undo command, a command that puts the old settings back.\n"),
      [("REPEAT", "command")])
check("copies and copy",
      run("Delete the copies first, and keep one copy aside.\n"),
      [("REPEAT", "copies")])

# --- REPEAT: clean ------------------------------------------------------
check("the fixed sentence",
      run("Back up each server to a different system, because a backup on the same disk dies with it.\n"),
      [])
check("pronoun repair",
      run("Schedule an undo command, one that puts the old settings back.\n"),
      [])
check("two sentences are two sentences",
      run("The disk holds every backup. When the disk fills, the backups stop.\n"),
      [])
check("inline code is not prose",
      run("Run `sudo systemctl stop lab-backup` and the backup timer waits.\n"),
      [])
check("a quotation stays as its author wrote it",
      run('The manual says "a timer set in the past fires at once when the timer starts" and means it.\n'),
      [])
check("fenced code is skipped",
      run("Run this:\n\n```\ngit git git commit commit\n```\n"),
      [])
check("a table is skipped",
      run("| Rule | Waits |\n|---|---|\n| BackupLate | backup backup |\n"),
      [])
check("a block quote is skipped",
      run("> The server token, stored on the server, joins a server.\n"),
      [])
check("host names are not words",
      run("paris-04, paris-06 and paris-07 back up to paris-05.\n"),
      [])
check("a path is not a word",
      run("GitHub's record for minio/minio shows the archive.\n"),
      [])
check("names left alone by default",
      run("The Cloud Native Computing Foundation, the Linux Foundation's home for Kubernetes, counts it.\n"),
      [])
check("names flagged with --names",
      run("That job belongs to Kubernetes, and Kubernetes runs on Linux.\n", names=True),
      [("REPEAT", "kubernetes")])
check("--keep spares a fixed phrase",
      run("From the command center, open a session on the command center.\n", keep={"command center"}),
      [])
check("short words below the minimum",
      run("The card lost its card slot.\n"),
      [])

check("a quotation that ends a sentence ends it",
      run('The manual warns that a timer "will immediately elapse." paris-04 booted before you wrote the timer.\n'),
      [])
check("underscores inside a name stay",
      run("sshd reads sshd_config and then the files in sshd_config.d in order.\n"),
      [])

# --- OPENER and RUN -----------------------------------------------------
check("same opening twice",
      run("The node exporter counts the numbers. The node exporter publishes them on port 9100.\n"),
      [("OPENER", "the node exporter")])
check("different openings",
      run("The node exporter counts the numbers. Prometheus reads them every 30 seconds.\n"),
      [])
check("a new paragraph resets the opening",
      run("The node exporter counts.\n\nThe node exporter publishes.\n"),
      [])
check("three sentences on one word",
      run("You install it. You start it. You read its page.\n"),
      [("RUN", "you")])
check("two are not a run",
      run("You install it. You read its page.\n"),
      [])
check("a run of The is not flagged",
      run("The rule waits. The page lists it. The log names the man.\n"),
      [])
check("list items are parallel on purpose",
      run("- port 6443 on paris-07\n- port 8472 on every computer\n- port 10250 on every computer\n"),
      [])

print()
print("all pass" if not FAILS else f"{FAILS} FAILED")
sys.exit(1 if FAILS else 0)
