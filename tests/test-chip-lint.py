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

# The parser is optional. Without spaCy chip-lint falls back to the old
# sixty-word list, which cannot see these verbs — that is the whole reason
# for the change. Skip rather than fail, and say so.
PARSED = c._parser() is not None
if not PARSED:
    print("\nspaCy not installed — skipping the parser tests.")
    print("chip-lint is running its fallback list, which reports high.")
    print("  ~/pipeline-venv/bin/python -m pip install spacy click")
    print("  ~/pipeline-venv/bin/python -m spacy download en_core_web_sm\n")

print("verbs the sixty-word list could not see (2026-08-20)")
PARSED and ok("spoke", c.classify("One man in that room spoke French better than English."), None)
PARSED and ok("rebuilt", c.classify("Below him the cranes rebuilt the waterfront."), None)
PARSED and ok("rode", c.classify("The old job rode in the seat with him."), None)
PARSED and ok("present tense", c.classify("He walks to the window and opens it."), None)
PARSED and ok("held chose drew", c.classify("He held the door, chose the seat, drew the curtain."), None)
PARSED and ok("intransitive two words", c.classify("Snow fell."), None)
PARSED and ok("imperative", c.classify("Run the query."), None)

print("not the author's prose")
ok("markup", c.classify('<div class="scene-break"></div>'), None)
ok("speech", c.classify("\u201cHow long?\u201d"), None)
ok("speech fragment", c.classify("\u201cNothing heroic.\u201d"), None)
ok("quoted italic", c.classify("*Next tranche.*"), None)

print("and the chips still fire")
PARSED and ok("noun phrase two words", c.classify("Delivery dates."), "LABEL")
ok("glass", c.classify("Glass."), "LABEL")
ok("jewelry", c.classify("Jewelry on the slides."), "LABEL")

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
