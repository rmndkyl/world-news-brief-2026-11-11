"""Write the 11 November 2026 world news summary to $MAKEFUN_OUTPUT_DIR/entry.txt.

Python 3.13, standard library only. No network access and no clock reads: the
summary.txt stored beside this file is copied byte for byte, so a second run
always produces the same bytes. MAKEFUN_OUTPUT_DIR defaults to /output and is
created if it does not exist.

Local check:

    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""

import os
from pathlib import Path


def main() -> None:
    """Copy summary.txt beside this script to $MAKEFUN_OUTPUT_DIR/entry.txt."""
    summary_bytes = Path(__file__).resolve().with_name("summary.txt").read_bytes()
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output")
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_bytes(summary_bytes)


if __name__ == "__main__":
    main()
