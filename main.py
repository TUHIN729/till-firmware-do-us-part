#!/usr/bin/env python3
"""Till Firmware Do Us Part — a robot's wedding vow.

Writes a single wedding vow, spoken by a robot at its own wedding,
to /output/entry.txt. One sentence, under 200 characters.
Deterministic, no network, no dependencies.
"""

import os
import sys

# The vow: a machine whose memory is failing keeps exactly one thing.
VOW = (
    "I vow to love you in every frame rate, through every glitch "
    "and lag spike, until my memory banks forget everything "
    "except your name."
)


def main() -> int:
    # Gate-check the vow before writing: the sealed scorer only
    # accepts UTF-8 text of 1-200 characters, not only whitespace.
    if not 1 <= len(VOW) <= 200 or not VOW.strip():
        print("error: vow fails the 1-200 character gate", file=sys.stderr)
        return 1
    out_dir = "/output"
    # Never delete /output itself: the grader mounts it root-owned.
    # Create it if missing, then write entry.txt inside it.
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(VOW)
    return 0


if __name__ == "__main__":
    sys.exit(main())
