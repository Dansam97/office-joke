#!/usr/bin/env python3
"""One-Line Office Joke: 24-Hour Sprint — make.fun entry.

Writes the entry joke to entry.txt in the output directory
(MAKEFUN_OUTPUT_DIR, default /output). The joke is embedded in this
file so the program is fully self-contained: no network, no inputs,
the same bytes on every run.
"""

import os

JOKE = (
    "My out-of-office reply now attends my meetings in my place, "
    "and so far it's the only one who has noticed I'm not there."
)


MAX_CHARS = 200  # the gate's cap for this bounty


def validate(text: str) -> str:
    """Return the exact file content for `text`, or raise if it would
    fail the gate: UTF-8 text of 1..200 characters, a single line, and
    not only whitespace."""
    if not text.strip():
        raise ValueError("entry text is empty or only whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("entry text must be a single line")
    content = text + "\n"
    if not 1 <= len(content) <= MAX_CHARS:
        raise ValueError(f"entry is {len(content)} characters, over the {MAX_CHARS} cap")
    content.encode("utf-8")  # raises if not encodable
    return content


def main() -> None:
    content = validate(JOKE)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(content)
    # Read back what landed on disk: the judged bytes must be exact.
    with open(path, "r", encoding="utf-8", newline="") as fh:
        if fh.read() != content:
            raise IOError("entry.txt on disk does not match the intended bytes")


if __name__ == "__main__":
    main()
