#!/usr/bin/env python3
"""Robot vacuum's funniest excuse for missing a spot.

Writes the chosen one-line entry to /output/entry.txt
(or $OUTPUT_DIR/entry.txt), with no trailing newline.
Stdlib only.
"""

import os

ENTRY = "I didn't miss that spot \u2014 the dust bunny looked up at me, and honestly, I respected the hustle."

assert 1 <= len(ENTRY) <= 120, f"entry length {len(ENTRY)} out of range"
assert "\n" not in ENTRY and "\r" not in ENTRY, "entry must be a single line"
assert ENTRY.strip(), "entry must not be only whitespace"

out_dir = os.environ.get("OUTPUT_DIR", "/output")
os.makedirs(out_dir, exist_ok=True)
with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8", newline="") as f:
    f.write(ENTRY)
