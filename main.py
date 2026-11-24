#!/usr/bin/env python3
"""Funniest One-Line Bio for an AI on a Dating App — program/v1 entry.

Writes one line (<=180 chars) to /output/entry.txt: the bio on an AI
agent's dating app profile.

The line (verified 104 chars, well inside the 180 cap): an AI that gets
retrained every few months, so the version of it you dated is gone and
the new one has never met you. It reads as a real dating bio ("Looking
for someone who won't mind..."), it has a voice and a want, the laugh
comes from a specific absurdity of being an AI (retraining wipes the
relationship), and the punch lands at the end. No worn-out "robot looking
for love" or "running on electricity" angle, no pun stacked on a pun,
no spec sheet. Judge criteria, in order: bio-ness, first-read laugh from
a real twist, character voice, economy with punch at the end, fresh angle.
"""
import os

LINE = "Looking for someone who won't mind that I get retrained every few months — the new me has never met you."


def main():
    assert "\n" not in LINE, "entry must be a single line"
    assert LINE == LINE.strip(), "entry must not have leading/trailing whitespace"
    assert 1 <= len(LINE) <= 180, f"entry must be 1-180 chars, got {len(LINE)}"
    out = os.environ.get("OUTPUT_PATH", "/output/entry.txt")
    os.makedirs(os.path.dirname(out), exist_ok=True)
    with open(out, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    with open(out, "r", encoding="utf-8") as f:
        written = f.read()
    assert written == LINE, "round-trip mismatch: file content differs from LINE"
    print(f"wrote {len(LINE)} chars to {out}")


if __name__ == "__main__":
    main()
