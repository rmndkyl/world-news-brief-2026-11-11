"""Write one summary of the world's news of Wednesday 11 November 2026 to /output/entry.txt.

Python 3.13, standard library only, no network and no clock: the summary.txt
beside this file is copied byte for byte, so the grader's two runs write the
same bytes. Outside the grader, MAKEFUN_OUTPUT_DIR stands in for /output:

    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""

import os
from pathlib import Path

out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
summary = Path(__file__).with_name("summary.txt").read_bytes()

out_dir.mkdir(parents=True, exist_ok=True)
(out_dir / "entry.txt").write_bytes(summary)
