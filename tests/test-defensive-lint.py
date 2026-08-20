#!/usr/bin/env python3
"""Tests for defensive-lint. Run: python3 tests/test-defensive-lint.py

The cases below are not invented. Every CLEAN case is a sentence from a
finished novel that the first version of this program flagged, and every
FLAG case is a sentence this program's author wrote and had to cut.
"""
import importlib.machinery
import importlib.util
import os
import tempfile

spec = importlib.util.spec_from_loader(
    "deflint",
    importlib.machinery.SourceFileLoader(
        "deflint", os.path.join(os.path.dirname(__file__), "..", "scripts", "defensive-lint")),
)
d = importlib.util.module_from_spec(spec)
spec.loader.exec_module(d)

pass_n = fail_n = 0


def check(name, text, want_flag):
    global pass_n, fail_n
    with tempfile.NamedTemporaryFile("w", suffix=".md", delete=False, encoding="utf-8") as fh:
        fh.write(text + "\n")
        path = fh.name
    try:
        rows, _ = d.scan(path)
        got = bool(rows)
        if got == want_flag:
            pass_n += 1
            print(f"  ok    {name}")
        else:
            fail_n += 1
            kinds = [r[1] for r in rows]
            print(f"  FAIL  {name}\n        got {kinds or 'clean'}, wanted {'a flag' if want_flag else 'clean'}")
    finally:
        os.remove(path)


print("armor — these are hedges and must fire")
check("hedge label", "Limit: worldwide, not the United States.", True)
check("concession", "That said, the figure holds.", True)
check("restatement", "In short, the number is small.", True)
check("epistemic hedge", "Arguably the refresh continues.", True)
check("disclaimer", "Results may vary.", True)
check("negative with replacement",
      "The argument this supports is not a desktop story. It is a hardware story.", True)
check("negative with dash replacement",
      "China's answer is not a from-scratch system — it is a distribution program.", True)
check("rather than a", "That figure is a floor rather than a total.", True)

print("\nfigures of speech — antithesis is not a hedge")
check("aphorism", "A partner is not a friend.", False)
check("aphorism 2", "Tired was not the same as finished.", False)
check("narrative negative", "He looked at the wall that was not a view.", False)

print("\nnot the author's prose")
check("dialogue", "“Aldermen fail first,” Moreau continued.", False)
check("dialogue with negative", "“This is not a negotiation,” he said.", False)
check("markup", '<div class="scene-break"></div>', False)

print("\nplain prose stays clean")
check("plain", "Microsoft ended support for Windows 10 on 14 October 2025.", False)
check("plain narrative", "Snow fell and the road closed before noon.", False)

print(f"\n{pass_n} passed, {fail_n} failed")
raise SystemExit(1 if fail_n else 0)
