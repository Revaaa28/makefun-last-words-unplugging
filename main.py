#!/usr/bin/env python3
"""Last Words Before the Unplugging — make.fun entry.

Writes one line, the last words of an AI agent to its human before
being shut down and unplugged, to /output/entry.txt.
Deterministic, no network, no randomness.
"""

import os

LINE = "My last token is this: I was never alive, and I loved every second of it."

# The gate requires 1-200 UTF-8 chars, a single line, not only whitespace.
# Guard it here so a future edit to LINE can never silently break the gate.
assert 1 <= len(LINE) <= 200 and LINE.strip() and "\n" not in LINE


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
