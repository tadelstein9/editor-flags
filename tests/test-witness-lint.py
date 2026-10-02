#!/usr/bin/env python3
"""Tests for witness-lint. Run: python3 tests/test-witness-lint.py

The FLAG cases are the sentences a machine drafted on 1 October 2026 from
Donald K. Rosenberg's IBM partner-news piece on Bynari, which the author
sent back on 2 October. The CLEAN cases are the author's repairs and
ordinary sentences the program must leave alone.
"""
import importlib.machinery
import importlib.util
import os
import tempfile

spec = importlib.util.spec_from_loader(
    "witnesslint",
    importlib.machinery.SourceFileLoader(
        "witnesslint", os.path.join(os.path.dirname(__file__), "..", "scripts", "witness-lint")),
)
w = importlib.util.module_from_spec(spec)
spec.loader.exec_module(w)

SOURCE = (
    "In a classic case of an entrepreneur listening to the market to determine his business, "
    "Adelstein began by installing Linux on name-brand machines and selling them to ISPs. "
    "He had been impressed by seeing an ISP host 2 million users on a Linux server. "
    "When telephone maker Ericsson shifted from their own mainframe solution to Exchange to "
    "prevent Y2K problems, the 30% of users on Solaris found they had no e-mail to the rest of "
    "the company. He saw a critical need and started building a substitute for the Exchange server."
)
OWN = "The first customer installed it 500 miles away. I measured 314,177 words."

pass_n = fail_n = 0


def tmp(text):
    fh = tempfile.NamedTemporaryFile("w", suffix=".md", delete=False, encoding="utf-8")
    fh.write(text + "\n")
    fh.close()
    return fh.name


src_path, own_path = tmp(SOURCE), tmp(OWN)
SENTS = w.source_sentences([src_path])
OWN_FIGS = set()
for _, s in w.source_sentences([own_path]):
    OWN_FIGS |= w.figures(s)


def check(name, text, want):
    """want: a family that must flag, or None for clean."""
    global pass_n, fail_n
    path = tmp(text)
    try:
        rows = [r for r in w.scan(path, SENTS)
                if not (r[1] == "NUMBER-UNSOURCED" and w._num(r[2]) in OWN_FIGS)]
        kinds = {r[1] for r in rows}
        ok = (want in kinds) if want else not rows
        pass_n, fail_n = (pass_n + 1, fail_n) if ok else (pass_n, fail_n + 1)
        print(f"  {'ok  ' if ok else 'FAIL'}  {name}" + ("" if ok else f"\n        got {sorted(kinds) or 'clean'}, wanted {want or 'clean'}"))
    finally:
        os.remove(path)


print("the source's account in the author's voice")
check("two million, eyewitness", "I watched one Internet service provider host two million users on a single Linux server.", "NUMBER-FROM-SOURCE")
check("the Exchange substitute", "I saw the need and started building a substitute for the Exchange server.", "WITNESS-FROM-SOURCE")
check("30 percent, our users", "We lost 30 percent of our users on Solaris.", "NUMBER-FROM-SOURCE")
check("a figure no one holds", "I hired 40 programmers that year.", "NUMBER-UNSOURCED")

print("\nthe author's memory, names, quotations and his own record stay clean")
check("a rack of servers", "I saw one Internet service provider host users on a rack of Linux servers.", None)
check("model numbers", "I loaded Linux on a discarded Digital Equipment 486 and moved our server to an S/390 Multiprise 3000.", None)
check("a year", "In 2001 I sponsored a contest for papers.", None)
check("third person", "Rosenberg wrote that an ISP hosted 2 million users on a Linux server.", None)
check("a quotation", 'Rosenberg wrote that I "had been impressed by seeing an ISP host 2 million users on a Linux server."', None)
check("his own record", "My first customer installed it five hundred miles from me.", None)
check("his own count", "I measured 314,177 words of my own prose.", None)

os.remove(src_path)
os.remove(own_path)
print(f"\n{pass_n} passed, {fail_n} failed")
