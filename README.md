# news-image-20261117

Entry for the make.fun competition **news-image-20261117**: sum up 17 November
2026's world news in one image.

## The entry

`entry.png` is a single-page newspaper front page that sums up the world's
news of 17 November 2026. It contains 30 stories in the classic front-page
format used by the competition's winning entries: a large lead story, a grid
of sectioned stories with icons, and a map with location pins. The image is
1024 x 1024 pixels.

## How to run

```bash
python3 main.py
```

The program copies `entry.png` from this repository into the output
directory and verifies the copy. The output directory is read from the
`MAKEFUN_OUTPUT_DIR` environment variable and defaults to `/output`:

```bash
MAKEFUN_OUTPUT_DIR=./out python3 main.py
```

On success it prints the destination path and the SHA-256 digest of the
copied file, then exits with status 0. If the source image is missing, the
output directory cannot be created, the copy fails, or the digest of the
copy does not match the source, it prints an error to stderr and exits
with status 1.

## Determinism

The build is deterministic: the output is a byte-for-byte copy of
`entry.png`, with no randomness, no network access, and no timestamps
involved. Two runs produce byte-identical output, with the same SHA-256
digest as the source image.

## Requirements

Python 3, standard library only (no third-party packages needed).
