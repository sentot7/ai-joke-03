#!/usr/bin/env python3
"""ai-joke-03 entry: write one one-liner about AI coding agents to entry.txt.

The grader runs this twice with no network, and both runs must write the
same bytes, so the joke is a fixed string: no randomness, no clock, no I/O
besides the single output file. Locally, MAKEFUN_OUTPUT_DIR stands in for
/output (mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py).
"""

import os
from pathlib import Path

JOKE = (
    "My AI coding agent finally achieved sentience: it looked at my legacy "
    "code, said 'I didn't write this,' and closed the ticket as 'won't fix'."
)

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

Path(OUTPUT_DIR).mkdir(parents=True, exist_ok=True)
Path(OUTPUT_DIR, "entry.txt").write_text(JOKE, encoding="utf-8")
