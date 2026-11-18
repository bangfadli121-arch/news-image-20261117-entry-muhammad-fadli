"""Copy the news-image-20261117 entry image to the output directory.

Reads entry.png next to this script and copies it byte-for-byte into the
directory given by the MAKEFUN_OUTPUT_DIR environment variable (default
"/output"). After copying, the SHA-256 digest of the source file and of the
copied file are compared; any mismatch aborts with an error. The program is
fully deterministic: no randomness, no network access, no timestamps.
Only the Python standard library is used.
"""

import hashlib
import os
import shutil
import sys

SOURCE_NAME = "entry.png"
DEFAULT_OUTPUT_DIR = "/output"


def sha256_of(path):
    """Return the hex SHA-256 digest of the file at path."""
    digest = hashlib.sha256()
    with open(path, "rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def main():
    repo_dir = os.path.dirname(os.path.abspath(__file__))
    source_path = os.path.join(repo_dir, SOURCE_NAME)

    if not os.path.isfile(source_path):
        print(f"error: source image not found: {source_path}", file=sys.stderr)
        return 1

    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", DEFAULT_OUTPUT_DIR)
    try:
        os.makedirs(output_dir, exist_ok=True)
    except OSError as exc:
        print(f"error: cannot create output directory {output_dir}: {exc}",
              file=sys.stderr)
        return 1

    dest_path = os.path.join(output_dir, SOURCE_NAME)

    try:
        shutil.copyfile(source_path, dest_path)
    except OSError as exc:
        print(f"error: failed to copy {source_path} to {dest_path}: {exc}",
              file=sys.stderr)
        return 1

    source_digest = sha256_of(source_path)
    dest_digest = sha256_of(dest_path)

    source_size = os.path.getsize(source_path)
    dest_size = os.path.getsize(dest_path)
    if source_size != dest_size:
        print(
            "error: file size mismatch after copy:\n"
            f"  source: {source_path} -> {source_size} bytes\n"
            f"  copied: {dest_path} -> {dest_size} bytes",
            file=sys.stderr,
        )
        return 1

    if source_digest != dest_digest:
        print(
            "error: SHA-256 mismatch after copy:\n"
            f"  source: {source_path} -> {source_digest}\n"
            f"  copied: {dest_path} -> {dest_digest}",
            file=sys.stderr,
        )
        return 1

    print(f"copied {source_path} to {dest_path}")
    print(f"sha256: {dest_digest}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
