#!/usr/bin/env python3
"""Real-Life Patch Notes: The Comedy Changelog (program/v1).

Writes one original one-line patch note for a bug in human biology
(111 characters, inside the 1-160 gate) to /output/entry.txt.
The bug is original: the bladder's low-battery warning arriving only
once you are already out of the house, door locked behind you.

Deterministic and offline: the line is a fixed string. No randomness,
no network, no timestamps, no environment input. Two runs produce
byte-identical output.
"""

import os

ENTRY = "v3.1.4: Fixed a bug where the bladder reported 100% full only after you had left the house and locked the door."

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    # Gate mirror: the sealed scorer requires UTF-8 text of 1-160
    # characters, not only whitespace. Refuse to write an invalid entry.
    if not 1 <= len(ENTRY) <= 160 or not ENTRY.strip():
        raise ValueError("entry fails the gate (must be 1-160 characters)")
    if ENTRY.count("\n") or ENTRY.count("\r"):
        raise ValueError("entry must be a single line")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
