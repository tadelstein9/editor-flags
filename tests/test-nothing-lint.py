#!/usr/bin/env python3
"""Tests for nothing-lint. Run: python3 tests/test-nothing-lint.py

The FLAG cases are sentences this program's author wrote and had to cut.
The CLEAN cases are ordinary negation, which is a fact about somebody and
stays.
"""
import importlib.machinery
import importlib.util
import os
import tempfile

spec = importlib.util.spec_from_loader(
    "nothinglint",
    importlib.machinery.SourceFileLoader(
        "nothinglint", os.path.join(os.path.dirname(__file__), "..", "scripts", "nothing-lint")),
)
n = importlib.util.module_from_spec(spec)
spec.loader.exec_module(n)

pass_n = fail_n = 0


def check(name, text, want_flag):
    global pass_n, fail_n
    with tempfile.NamedTemporaryFile("w", suffix=".md", delete=False, encoding="utf-8") as fh:
        fh.write(text + "\n")
        path = fh.name
    try:
        rows, _ = n.scan(path)
        got = bool(rows)
        if got == want_flag:
            pass_n += 1
            print(f"  ok    {name}")
        else:
            fail_n += 1
            print(f"  FAIL  {name}\n        got {[r[2] for r in rows] or 'clean'},"
                  f" wanted {'a flag' if want_flag else 'clean'}")
    finally:
        os.remove(path)


print("the absolute standing where a particular belongs")
check("nothing leaves it", "One computer. Bare metal. Nothing leaves it.", True)
check("nothing leaves the building", "It runs here. Nothing leaves the building.", True)
check("not one of them", "Twenty programs read it. Not one of them rewrites a word.", True)
check("none of it", "Two years of research. None of it where you can reach it.", True)
check("nothing goes on the page", "Nothing goes on the page because a machine suggested it.", True)
check("never once", "The kernel has never once lived there.", True)
check("no x no y no z", "No gradients, no shadows, no gloss.", True)
check("not a single", "He read the file and found not a single error.", True)

print("\nordinary negation is a fact about somebody and stays")
check("did not answer", "He did not answer the phone that evening.", False)
check("no error", "The command returned no error.", False)
check("nothing mid-sentence as object",
      "She said nothing to him about the letter.", False)
check("never as habit", "He never learned to drive.", False)
check("none as quantity", "Of the twelve chapters, none ran short.", False)

print("\nplain prose stays clean")
check("positive claim", "Your manuscript stays on the disk in your room.", False)
check("a fact with a number", "The card reports 4,649 MiB in use.", False)

print(f"\n{pass_n} passed, {fail_n} failed")
raise SystemExit(1 if fail_n else 0)
