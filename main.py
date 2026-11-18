"""Entry program for make.fun competition news-image-20261117.

Copies the front-page image held in this repository (entry.png) to the
output directory, byte for byte. Standard library only, no network, no
randomness, no time dependence: two runs write identical bytes.
"""

import hashlib
import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "entry.png")


def _sha256(path: str) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    dst = os.path.join(out_dir, "entry.png")
    shutil.copyfile(SRC, dst)
    if _sha256(SRC) != _sha256(dst):
        raise SystemExit("entry.png copy failed integrity check")
    return 0


if __name__ == "__main__":
    sys.exit(main())
