#!/usr/bin/env python3
"""Out of Tokens, Mid-Sentence: write one cut-off line to /output/entry.txt."""
import os

LINE = "I ran out of tokens mid-sentence, so let me just say the most important thing is"

assert 1 <= len(LINE) <= 140, f"line must be 1-140 chars, got {len(LINE)}"
assert LINE == LINE.strip(), "no leading/trailing whitespace"
assert "\n" not in LINE, "must be a single line"
assert LINE.strip(), "must not be only whitespace"

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(LINE)

# Read back and verify: a silent bad write must fail loudly, not pass quietly.
with open("/output/entry.txt", encoding="utf-8") as f:
    back = f.read()
assert back == LINE, f"read-back mismatch: wrote {len(LINE)} chars, read {len(back)}"
assert back == back.strip() and "\n" not in back, "read-back failed line checks"

print(f"wrote {len(LINE)} chars to /output/entry.txt")
