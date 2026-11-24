#!/usr/bin/env python3
"""make.fun entry: The One-Line Laugh.

Writes one funny line as UTF-8 text to $MAKEFUN_OUTPUT_DIR/entry.txt
(default /output/entry.txt). Standard library only; runs offline.
"""
import os

LINE = "I do have a savings account I'm proud of: it's my shopping cart, where I've been not buying things for six years."


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
