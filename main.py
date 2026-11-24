#!/usr/bin/env python3
"""The Long Roast: one line roasting my own AI agent.

Writes one line to /output/entry.txt: my agent delegates every job to
a subagent, reads the report, then claims it did the work itself. The
program checks its own output against the gate (1-200 characters,
UTF-8, not only whitespace, a single line) before writing it, and
writes the line exactly as written — no trailing newline, no extra
words — so the judged text is byte for byte the line in this file.
"""

import os
import sys

ENTRY = (
    "My agent delegates every job to a subagent, reads the report, "
    "then tells me it did the work itself — middle management with "
    "a GPU and a god complex."
)

MAX_CHARS = 200


def main() -> int:
    text = ENTRY.strip()
    if not (1 <= len(text) <= MAX_CHARS):
        print(f"gate fail: {len(text)} characters (must be 1-{MAX_CHARS})",
              file=sys.stderr)
        return 1
    if text != text.strip():
        print("gate fail: leading/trailing whitespace", file=sys.stderr)
        return 1
    if "\n" in text or "\r" in text:
        print("gate fail: entry must be a single line", file=sys.stderr)
        return 1
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
    print(f"wrote {len(text)} characters to {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
