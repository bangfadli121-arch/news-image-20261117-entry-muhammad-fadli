# news-image-20261117 — "The World in One Day"

Entry for the make.fun competition **"Sum up 17 November's world news in
one image"** ($250, deadline 19 November 2026 07:00 WIB).

The entry is a classic newspaper front page, dated **Tuesday, 17 November
2026**, summing up that day's world news.

## How to run

```sh
mkdir -p out
MAKEFUN_OUTPUT_DIR=out python3 main.py
```

`main.py` (Python 3.13, standard library only) copies the front-page image
held in this repository (`entry.png`) to `$MAKEFUN_OUTPUT_DIR/entry.png`
(or `/output/entry.png` when the variable is not set), byte for byte. No
network, no randomness, no time dependence: two runs write identical bytes.

## Stories on the front page

**Lead story — Ukraine / Crimea: "UKRAINE HITS KERCH BRIDGE AGAIN"**

Ukraine struck the Kerch Bridge again, a second strike in two days, and a
road span fell. Zelenskyy hailed an "unprecedented operation" as Moscow
vowed to rebuild.

**Middle East / Shipping: "TANKERS HIT BY MINES OFF HORMUZ"**

Two tankers were hit by mines off Hormuz, and a third U.S. carrier arrived
in the Middle East.

**Asia / Diplomacy: "TRUMP IN MANILA, THEN SHENZHEN"**

Trump was in Manila, and then Xi, Trump and Putin were to meet in Shenzhen
on 19 November.

The "ALSO TODAY" strip at the bottom of the page carries the short items
shown in the image: JPMorgan blaming a software bug for the banking outage,
Nvidia reporting earnings after the close, WHO: Eritrea ends trachoma,
Japan scrambling jets, Dhoni retiring from IPL, and Cyclone Akvan nearing
India.

Every story happened, or was first reported, on 17 November 2026.

## Files

- `main.py` — the entry program (copies `entry.png` to the output)
- `entry.png` — the front-page image (1024 x 1024, 101,681 bytes)
- `LICENSE` — MIT License
- `.makefun/owner.json` — claim file naming the entrant's wallet
