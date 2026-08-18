#!/usr/bin/env python3
"""Tests for that-lint. Run: python3 tests/test-that-lint.py"""
import importlib.machinery
import importlib.util
import os
import tempfile

spec = importlib.util.spec_from_loader(
    "thatlint",
    importlib.machinery.SourceFileLoader("thatlint", os.path.join(os.path.dirname(__file__), "..", "scripts", "that-lint")),
)
thatlint = importlib.util.module_from_spec(spec)
spec.loader.exec_module(thatlint)

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
    "hadn't touched",
    thatlint.hits_in("sixty-three towns that hadn't touched the sickness"),
    ["that hadn't touched"],
)
ok("no clause", thatlint.hits_in("towns untouched by the sickness"), [])
ok("who had seen", thatlint.hits_in("a man who had seen the pits"), ["who had seen"])
ok("had a book is silent", thatlint.hits_in("a man that had a book"), [])

print("scan skips")
with tempfile.NamedTemporaryFile("w", suffix=".md", delete=False) as fh:
    fh.write("# towns that hadn't touched\n\n")
    fh.write("towns that hadn't touched the sickness.\n")
    path = fh.name
try:
    rows = thatlint.scan(path)
    ok("skips heading", [r[1] for r in rows], ["that hadn't touched"])
finally:
    os.remove(path)

print(f"{pass_n} passed, {fail_n} failed")
raise SystemExit(1 if fail_n else 0)
