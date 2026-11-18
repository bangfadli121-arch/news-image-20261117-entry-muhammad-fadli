"""News-image entry runner for make.fun (news-image-20261117).

The entry itself is a single finished picture, entry.png, sitting next to
this file. All this program does is place an exact copy of that picture
where the competition harness expects it and prove the copy is exact.

It reads the output folder from MAKEFUN_OUTPUT_DIR and falls back to
/output when the variable is unset. After copying it checks two things:
the copy has the same byte count as the original, and both files share
one SHA-256 digest. Any mismatch is reported on stderr and the program
exits non-zero, so a bad copy can never pass silently.

There is no randomness, no clock, no network and no third-party code
here: the same input always produces the same output bytes.
"""

import hashlib
import os
import shutil
import sys
from pathlib import Path

ENTRY = "entry.png"
FALLBACK_DIR = "/output"


def file_sha256(path):
    """Hex SHA-256 digest of the file at path, streamed in 1 MiB blocks."""
    digest = hashlib.sha256()
    with open(path, "rb") as handle:
        while True:
            block = handle.read(1024 * 1024)
            if not block:
                break
            digest.update(block)
    return digest.hexdigest()


def fail(message):
    """Print an error to stderr and return the failure exit code."""
    print(f"error: {message}", file=sys.stderr)
    return 1


def run():
    """Copy entry.png to the output folder and verify the copy."""
    here = Path(__file__).resolve().parent
    source = here / ENTRY
    if not source.is_file():
        return fail(f"entry image missing: {source}")
    if source.stat().st_size == 0:
        return fail(f"entry image is empty: {source}")

    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", FALLBACK_DIR))
    try:
        out_dir.mkdir(parents=True, exist_ok=True)
    except OSError as exc:
        return fail(f"cannot create output folder {out_dir}: {exc}")

    target = out_dir / ENTRY
    try:
        shutil.copyfile(source, target)
    except OSError as exc:
        return fail(f"copy failed: {source} -> {target}: {exc}")

    # The copy must be byte-identical: same size and same digest.
    if source.stat().st_size != target.stat().st_size:
        return fail(
            "size mismatch after copy: "
            f"source {source.stat().st_size} bytes, "
            f"copy {target.stat().st_size} bytes"
        )
    want = file_sha256(source)
    got = file_sha256(target)
    if want != got:
        return fail(f"SHA-256 mismatch after copy: {want} != {got}")

    print(f"copied {source} to {target}")
    print(f"size: {target.stat().st_size} bytes")
    print(f"sha256: {got}")
    return 0


if __name__ == "__main__":
    sys.exit(run())
