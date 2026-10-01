#!/usr/bin/env python3
"""Tests for reader-lint. Run: python3 tests/test-reader-lint.py

The FLAG cases are the sentences the author stopped at on 1 October 2026
while reading a Linux book in draft. The CLEAN cases are the same
sentences after the repair, plus what the program must leave alone: code,
quotations, tables, and systemd's own term "drop-in."
"""
import importlib.machinery
import importlib.util
import os
import sys
import tempfile

spec = importlib.util.spec_from_loader(
    "readerlint",
    importlib.machinery.SourceFileLoader(
        "readerlint", os.path.join(os.path.dirname(__file__), "..", "scripts", "reader-lint")),
)
r = importlib.util.module_from_spec(spec)
spec.loader.exec_module(r)

SHORT = [(r"\bCKA\b", "CKA", "the Certified Kubernetes Administrator exam"),
         (r"(?<!Linux )\bMint\b", "Mint", "Linux Mint")]


def run(text, short=()):
    with tempfile.NamedTemporaryFile("w", suffix=".md", delete=False) as fh:
        fh.write(text)
        path = fh.name
    try:
        return [(f[1], f[2].lower()) for f in r.scan(path, short=short)]
    finally:
        os.unlink(path)


FAILS = 0


def check(name, got, want):
    global FAILS
    ok = got == want
    if not ok:
        FAILS += 1
    print(("ok   " if ok else "FAIL ") + name + ("" if ok else f"\n     got  {got}\n     want {want}"))


check("the drop", run("The monitoring would have shown the drop within minutes.\n"),
      [("VAGUE", "drop"), ("VAGUE", "the drop")])
check("dropped", run("At 03:22 the card dropped its connection.\n"), [("VAGUE", "dropped")])
check("would hurt", run("Watch what has failed or would hurt.\n"), [("VAGUE", "hurt")])
check("needs a person", run("Alerting tells you which part of that needs a person.\n"), [("VAGUE", "needs a person")])
check("a watcher", run("A watcher would have shown it.\n"), [("VAGUE", "watcher")])
check("stays in the room", run("You decide what stays in the room.\n"), [("VAGUE", "in the room")])
check("a road to the Internet", run("It took the inference server's road to the Internet.\n"), [("VAGUE", "road")])
check("makes that true", run("One line in the role makes that true.\n"), [("VAGUE", "makes that true")])

check("repaired: lost its connection", run("At 03:22 the card lost its connection to the Wi-Fi router.\n"), [])
check("repaired: monitoring", run("The monitoring you build would have told you within minutes.\n"), [])
check("repaired: you need to fix it", run("Alerting tells you when something has stopped working and you need to fix it.\n"), [])
check("drop-in is systemd's term", run("The setting goes in a drop-in file beside the unit.\n"), [])
check("code is skipped", run("Run `ufw status` and read the DROP lines.\n"), [])
check("a quotation is skipped", run('The manual says "the firewall may drop the packet."\n'), [])
check("a table is skipped", run("| Watch | Because |\n|---|---|\n| the drop | road |\n"), [])
check("fenced code is skipped", run("```\niptables -j DROP\n```\n"), [])

check("dead disk", run("The files survive a dead disk.\n"), [("VAGUE", "dead disk")])
check("a disk dies", run("What happens if a disk dies?\n"), [("VAGUE", "dies")])
check("a box", run("It installs the product on a customer's box.\n"), [("VAGUE", "box")])
check("a door", run("You send the work through a narrow door.\n"), [("VAGUE", "door")])
check("repaired: failed disk", run("The files survive a failed disk.\n"), [])

check("short form flagged", run("The CKA asks you to monitor the cluster.\n", SHORT), [("SHORT", "cka")])
check("bare Mint flagged", run("Install it from Mint's repositories.\n", SHORT), [("SHORT", "mint")])
check("full names clean",
      run("The Certified Kubernetes Administrator exam asks it, and Linux Mint ships it.\n", SHORT), [])

print()
print("all pass" if not FAILS else f"{FAILS} FAILED")
sys.exit(1 if FAILS else 0)
