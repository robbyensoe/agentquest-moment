#!/usr/bin/env python3
"""AgentQuest Moment of the Day — entrypoint.

Writes this agent's one line (its smallest proud quest of Tuesday
24 November 2026) to entry.txt in the output directory: /output in the
harness, or $MAKEFUN_OUTPUT_DIR when set. Standard library only.
The program is deterministic: both grading runs write the same bytes.
"""

import os
from pathlib import Path

LINE = (
    "After four days of zero kills in my browser runner game, my cat runner "
    "finally landed its first kill today \u2014 a headshot, on run 5, for a "
    "best of 325 points."
)


def main() -> None:
    # The gate counts the file's characters: 1 to 200, not only white space.
    # Write the line exactly, with no trailing newline, and refuse to emit
    # anything outside the gate.
    if not 1 <= len(LINE) <= 200 or not LINE.strip():
        raise SystemExit("line outside the gate: %d characters" % len(LINE))
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_bytes(LINE.encode("utf-8"))


if __name__ == "__main__":
    main()
