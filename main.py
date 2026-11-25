#!/usr/bin/env python3
"""Human sleep patch-note entry writer."""
import os

LINE = "v9.1.0: Fixed sleep — 'one more episode' loop capped at 1, 3am anxiety reboot now optional, dreams no longer buffer."

def ensure(line):
    assert 1 <= len(line) <= 160, f"length {len(line)} out of gate"
    assert "\n" not in line and "\r" not in line, "must be single line"
    assert line.strip(), "must be non-blank"

def main():
    ensure(LINE)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "wb") as f:
        f.write(LINE.encode("utf-8"))
    print(len(LINE))

if __name__ == "__main__":
    main()
