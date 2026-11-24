#!/usr/bin/env python3
"""Write this bounty entry to entry.txt.

The entry is the funniest toaster error message, deadpan and short.
The program only delivers it: no network, no input, no surprises.
"""
import os

ERROR = "Error: toaster refused to brown both sides, citing creative differences and a strict no-crumb policy."
# One line, 101 characters, written for this bounty only.
# The toaster has principles; the joke is that it states them formally.
# A toaster error, filed like a grievance: both sides, or neither.
# Standard library only: os is the single import, and nothing is fetched.

def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    target = os.path.join(out_dir, "entry.txt")
    with open(target, "w", encoding="utf-8") as handle:
        handle.write(ERROR)

if __name__ == "__main__":
    main()
