#!/usr/bin/env python3
"""Tests for chip-lint. Run: python3 tests/test-chip-lint.py"""
import importlib.machinery
import importlib.util
import os
import tempfile

spec = importlib.util.spec_from_loader(
    "chiplint",
    importlib.machinery.SourceFileLoader("chiplint", os.path.join(os.path.dirname(__file__), "..", "scripts", "chip-lint")),
)
c = importlib.util.module_from_spec(spec)
spec.loader.exec_module(c)

pass_n = fail_n = 0


def ok(name, got, want):
    global pass_n, fail_n
    if got == want:
        pass_n += 1
        print(f"  ok    {name}")
    else:
        fail_n += 1
        print(f"  FAIL  {name}\n        got  {got!r}\n        want {want!r}")


print("classify")
ok("label", c.classify("Process."), "LABEL")
ok("messaging", c.classify("Messaging."), "LABEL")
ok("full sentence", c.classify("You write calm English."), None)
ok("ended", c.classify("Mass ended and the organ stopped."), None)
ok("long no-verb", c.classify("The current situation of the funding process without any actor in the subject seat."), "NO-VERB")

print("scan")
with tempfile.NamedTemporaryFile("w", suffix=".md", delete=False) as fh:
    fh.write("# Heading\n\n")
    fh.write("You write calm English. Process. Messaging.\n")
    fh.write("Nothing heroic. Nothing theological.\n")
    path = fh.name
try:
    rows = c.scan(path)
    kinds = [(k, s) for _, k, s in rows]
    ok("flags the labels", ("LABEL", "Process.") in kinds, True)
    ok("keeps the sentence", any(s.startswith("You write") for _, _, s in rows), False)
finally:
    os.remove(path)

print(f"{pass_n} passed, {fail_n} failed")
raise SystemExit(1 if fail_n else 0)
