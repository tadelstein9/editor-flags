#!/usr/bin/env python3
"""Tests for agency-lint. Run: python3 tests/test-agency-lint.py

The FLAG cases are sentences a machine drafted for a Linux book on
26 September 2026 and the author sent back. The CLEAN cases come from the
author's own published prose, or are ordinary English the program must
leave alone. A filter that flags the writer's own clean sentences teaches
the writer to stop reading it.

Needs spaCy (en_core_web_sm). Without it the grammar tests cannot run, and
this file says so and stops.
"""
import importlib.machinery
import importlib.util
import os
import sys
import tempfile

spec = importlib.util.spec_from_loader(
    "agencylint",
    importlib.machinery.SourceFileLoader(
        "agencylint", os.path.join(os.path.dirname(__file__), "..", "scripts", "agency-lint")),
)
a = importlib.util.module_from_spec(spec)
spec.loader.exec_module(a)

if a._parser() is None:
    print("spaCy not found. Install it, then run these tests:")
    print("  python -m pip install spacy click && python -m spacy download en_core_web_sm")
    sys.exit(1)

pass_n = fail_n = 0


def check(name, text, want):
    """want: a family name that must flag, or None for clean."""
    global pass_n, fail_n
    with tempfile.NamedTemporaryFile("w", suffix=".md", delete=False, encoding="utf-8") as fh:
        fh.write(text + "\n")
        path = fh.name
    try:
        rows, _ = a.scan(path)
        kinds = {r[1] for r in rows}
        ok = (want in kinds) if want else not rows
        if ok:
            pass_n += 1
            print(f"  ok    {name}")
        else:
            fail_n += 1
            got = [f"{r[1]}: {r[2]}" for r in rows] or "clean"
            print(f"  FAIL  {name}\n        got {got}, wanted {want or 'clean'}")
    finally:
        os.remove(path)


print("sentences the author sent back")
check("serves as", "The hardened endpoint serves as the machine a person sits at.", "DISGUISED-BE")
check("SSH decides", "SSH decides who gets in once a computer arrives there.", "THING-MINDS")
check("a computer arrives", "SSH decides who gets in once a computer arrives there.", "TRAVEL")
check("arrives there", "SSH decides who gets in once a computer arrives there.", "LOOSE-THERE")
check("knocks", "In the first line, paris-07 knocks on port 22 from the lab network.", "TRAVEL")
check("lets you in", "Wait 35 seconds and log in again, and paris-04 lets you in.", "TRAVEL")
check("the manual promises", "The ufw manual promises that an active firewall keeps your session.", "THING-MINDS")
check("this book walks", "The signed spine: this book walks the work those seats require.", "TRAVEL")
check("a login gets in", "A new key login from paris-06 gets in with the undo showing.", "TRAVEL")

check("Bynari started as", "Bynari started as a consulting business.", "HIDDEN-FOUNDER")
check("Bynari became a partner", "Bynari became IBM's first Linux Influencer Partner in April 2001.", "HIDDEN-FOUNDER")
check("Bynari Insight grew from it", "Bynari Insight grew from it: tools that run on Linux.", "HIDDEN-FOUNDER")
check("was founded, no one named", "The company was founded in 1998.", "HIDDEN-FOUNDER")

check("the key you met", "The key met the server in Chapter 2.", "THING-LIVES")
check("the account lives", "The git account lives at /srv/git.", "THING-LIVES")
check("the laptops ran into it", "Hold on to that sentence; the laptops ran into it.", "THING-LIVES")
check("a textbook tells", "A textbook can tell you what Git does.", "THING-SPEAKS")
check("the guide says", "Ubuntu's guide says a domain controller needs a fixed address.", "THING-SPEAKS")
check("the exam asks", "The Red Hat Certified Engineer exam asks you to manage packages.", "THING-SPEAKS")
check("section showed", "As section 4.5 showed, the password stays in a file.", "THING-SPEAKS")

print("\nthe author's own prose and ordinary English stay clean")
check("a person held an office", "William B. Miller served as the first Secretary.", None)
check("a person's role", "Basically, I function as the CTO and Mr. Hani Jabsheh is the CEO.", None)
check("a program does its job", "UFW admits the connection, and sshd refuses the password.", None)
check("the developers say", "The Samba developers warn in their notes that the clock must agree.", None)
check("a parcel arrived", "Once the laptop arrived, I began searching around on Google.", None)
check("a market arrival", "Linux indeed has arrived on the desktop and is ready for use.", None)
check("plays a role in", "Unfortunately, Linux plays a minor role in this project.", None)
check("there with an antecedent", "They post some helpful information there.", None)
check("a person decides", "Tom decides which account may log in.", None)
check("the administrator knows", "The administrator knows the key sits on paris-06.", None)
check("log in", "Log in from the command center and read the status.", None)
check("the rewrite", "In this section you choose which accounts may log in over that connection, "
      "and the SSH server on paris-04, the program sshd, enforces your choice.", None)
check("admits and accepts", "Wait 35 seconds and connect again: UFW admits the connection, "
      "and sshd accepts your key.", None)
check("a program refuses", "sshd refused the password. UFW dropped paris-07.", None)
check("there is", "There is one rule in the list, and there are two addresses.", None)
check("a quotation stays", 'The page quoted the draft: "SSH decides who gets in."', None)
check("inline code stays", "Run `the server decides` as a test string.", None)

check("begin to act", "Physicians and master-surgeons had begun to flee.", None)
check("founded by a person", "The company was founded by Tom in 1998.", None)
check("a company acts on something", "In 2001 Bynari sponsored a contest for papers.", None)
check("the founder in the subject seat", "I started Bynari as a consulting business.", None)

print(f"\n{pass_n} passed, {fail_n} failed")
sys.exit(1 if fail_n else 0)
