#!/usr/bin/env python3
"""Tests for had-lint. Run: python3 tests/test-had-lint.py"""
import os
import sys
import tempfile

import importlib.machinery
import importlib.util

spec = importlib.util.spec_from_loader(
    "hadlint",
    importlib.machinery.SourceFileLoader("hadlint", os.path.join(os.path.dirname(__file__), "..", "scripts", "had-lint")),
)
hadlint = importlib.util.module_from_spec(spec)
spec.loader.exec_module(hadlint)

pass_n = fail_n = 0


def ok(name, got, want):
    global pass_n, fail_n
    if got == want:
        pass_n += 1
        print(f"  ok    {name}")
    else:
        fail_n += 1
        print(f"  FAIL  {name}\n        got  {got!r}\n        want {want!r}")


print("hits_in")
ok(
    "Mass had ended",
    hadlint.hits_in("Mass had ended. The organ had stopped."),
    ["had ended", "had stopped"],
)
ok("simple past is silent", hadlint.hits_in("Mass ended and the organ stopped."), [])
ok("possession", hadlint.hits_in("He had a book and had three days."), [])
ok("obligation", hadlint.hits_in("He had to leave. She had better go."), [])
ok("hadn't seen", hadlint.hits_in("She hadn't seen him."), ["hadn't seen"])
ok("had been walking", hadlint.hits_in("He had been walking the walls."), ["had been walking"])
ok(
    "had already stopped",
    hadlint.hits_in("after the machine had already stopped"),
    ["had already stopped"],
)
ok(
    "anchored pair still flags — person judges",
    hadlint.hits_in("After the ship had docked, the bishop arrived."),
    ["had docked"],
)

print("scan skips")
with tempfile.NamedTemporaryFile("w", suffix=".md", delete=False) as fh:
    fh.write("# had ended in a heading\n\n")
    fh.write("Mass had ended.\n\n")
    fh.write("```\nhad written\n```\n")
    path = fh.name
try:
    rows = hadlint.scan(path)
    ok("skips heading and fence", [r[1] for r in rows], ["had ended"])
finally:
    os.remove(path)

print("negation must survive --fix (2026-08-20)")


def fixed(s):
    import tempfile, os
    with tempfile.NamedTemporaryFile("w", suffix=".md", delete=False, encoding="utf-8") as fh:
        fh.write(s + "\n")
        path = fh.name
    try:
        hadlint.fix_file(path)
        return open(path, encoding="utf-8").read().strip()
    finally:
        os.remove(path)


ok("had not keeps the not", fixed("The job had not left his mouth."),
   "The job did not leave his mouth.")
ok("had not, second case", fixed("She had not seen him since Tuesday."),
   "She did not see him since Tuesday.")
ok("had never keeps the never", fixed("They had never spoken of it."),
   "They never spoke of it.")
ok("hadn't still contracts", fixed("He hadn't finished the report."),
   "He didn't finish the report.")
ok("plain past perfect still fixed", fixed("Nobody had asked her twice."),
   "Nobody asked her twice.")
ok("unknown middle word is refused, never dropped",
   fixed("She had quietly closed the door."), "She had quietly closed the door.")

print(f"{pass_n} passed, {fail_n} failed")
sys.exit(1 if fail_n else 0)
