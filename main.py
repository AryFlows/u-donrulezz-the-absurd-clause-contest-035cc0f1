#!/usr/bin/env python3
"""Frost Absurd Clause: one absurd ToS clause, deadpan legal boilerplate.

Writes a single sentence (1-200 characters) to /output/entry.txt,
or to $MAKEFUN_OUTPUT_DIR/entry.txt when set.
"""

import os
import sys

CLAUSE = (
    "Section 14.2: by using this service, you agree to lend your dreams "
    "to the company on alternate Tuesdays, returnable only upon written "
    "request in triplicate."
)


def main() -> int:
    text = CLAUSE.strip()
    if not (1 <= len(text) <= 200):
        print(f"gate: clause is {len(text)} chars, must be 1-200", file=sys.stderr)
        return 1
    if text.count("\n"):
        print("gate: clause must be a single line", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
    # Round-trip check: what the grader reads must be exactly the clause.
    with open(path, "r", encoding="utf-8") as f:
        if f.read() != text:
            print("gate: round-trip mismatch", file=sys.stderr)
            return 1
    print(f"wrote {len(text)} chars to {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
