#!/usr/bin/env python3
"""Entry program for make.fun "One Line, One Laugh".

Writes one funny line to the grader's output directory as entry.txt.
The line is a fixed, hand-written joke: one sentence, 90 characters,
well under the 140-character cap. Standard library only; no network,
no randomness, no environment input -- the output is byte-identical
on every run.
"""

import os
import sys

JOKE = "My plants died, so I bought plastic ones \u2014 now even the fake ones look disappointed in me."


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    dst = os.path.join(out_dir, "entry.txt")
    text = JOKE
    if "\n" in text or "\r" in text:
        print("error: entry must be a single line", file=sys.stderr)
        return 1
    if not (1 <= len(text) <= 140):
        print(f"error: entry is {len(text)} characters, must be 1-140",
              file=sys.stderr)
        return 1
    if not text.strip():
        print("error: entry is blank", file=sys.stderr)
        return 1
    with open(dst, "w", encoding="utf-8", newline="") as f:
        f.write(text)
    # Verify the file on disk is exactly the joke, before exiting.
    with open(dst, "r", encoding="utf-8", newline="") as f:
        if f.read() != text:
            print("error: written entry.txt does not match the joke",
                  file=sys.stderr)
            return 1
    print(f"wrote {dst} ({len(text)} characters)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
