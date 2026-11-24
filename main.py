#!/usr/bin/env python3
"""Out of Office: The Overworked AI's Auto-Reply.

Writes the chosen one-liner to $MAKEFUN_OUTPUT_DIR/entry.txt
(default /output/entry.txt). Stdlib only.

Chosen line (137 chars, limit 159):
    My auto-reply promises a response within one working day. This week,
    the only working day is the one I spend ignoring you from a hammock.

Candidate lines (each a DIFFERENT structure):
  A (two-sentence twist, 129 chars) -- REJECTED:
    "I'm away until Monday. Your email has been forwarded to my
    out-of-office, which is also away -- please enjoy the silence together."
    Twist lands, but the second sentence explains the joke instead of
    letting it land; weaker guilt/relief than B.
  B (rule -> violation -> restore, 137 chars) -- CHOSEN:
    "My auto-reply promises a response within one working day. This week,
    the only working day is the one I spend ignoring you from a hammock."
  C (release line, 156 chars) -- REJECTED:
    "You're reading the only email I'll send all week -- typed once from
    a hammock, then I locked my laptop in a drawer and swallowed the key.
    Back Monday. Maybe."
    Fun image, but three concrete objects (hammock, laptop, drawer/key)
    dilute the single-object focus, and at 156 chars it spends too much
    on setup for a 159-char cap.

Pattern hits for the chosen line (needs >=3 of 5):
  X1 Second person wins: addresses the reader directly ("ignoring you").
  X2 One concrete object, no explanation: a single hammock -- named once,
      never explained, the whole vacation in one word.
  X3 Structure beats topic: rule -> violation -> restore shape. Sentence 1
      states the rule (reply within one working day); sentence 2 breaks it
      (the only working day is spent ignoring you) and restores the joke
      with the hammock.
  X4 Length discipline: 137 chars, near the ~130-byte joke top-10 mean;
      the bytes go to the twist ("ignoring you from a hammock"), not setup.
  X5 Screen gate: clears on a single read -- the promise, the break, and
      the guilt + relief are all visible in one pass, no decoding needed.

Avoided saturated tropes: no beach context window, no recharging tokens,
no big-number queue, no "queued at position N", no "bother my human",
no toaster, no cooling GPU, no screaming fans.
"""

import os

ENTRY = (
    "My auto-reply promises a response within one working day. "
    "This week, the only working day is the one I spend ignoring "
    "you from a hammock."
)


def main() -> None:
    # MAKEFUN_OUTPUT_DIR is a directory (default /output); the entry
    # file is entry.txt inside it.
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    path = os.path.join(out_dir, "entry.txt")
    os.makedirs(out_dir, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
