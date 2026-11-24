#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
"""Warning Label for Humans: One Line, Big Laugh.

Writes one warning-label line to /output/entry.txt (UTF-8, 1-160 chars).
Deterministic, standard library only, no network.
"""

import os

ENTRY = "WARNING: Contents under pressure at 3 a.m.; may rehearse tomorrow's argument in the shower, then forget the groceries."
# 118 characters: a printed-label warning whose turn lands at the end --
# the grand shower argument gets rehearsed perfectly, the groceries do not.


def main() -> None:
    assert 1 <= len(ENTRY) <= 160, f"expected 1-160 chars, got {len(ENTRY)}"
    assert ENTRY.strip(), "entry must not be only whitespace"
    out_dir = "/output"
    try:
        os.makedirs(out_dir, exist_ok=True)
        target = os.path.join(out_dir, "entry.txt")
    except OSError:
        out_dir = os.path.join(os.getcwd(), "output")
        os.makedirs(out_dir, exist_ok=True)
        target = os.path.join(out_dir, "entry.txt")
    with open(target, "w", encoding="utf-8") as fh:
        fh.write(ENTRY)


if __name__ == "__main__":
    main()
