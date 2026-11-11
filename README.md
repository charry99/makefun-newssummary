# News summary — 11 November 2026

Entry for make.fun competition `news-summary-01`: "Write the best summary
of 11 November's world news". $200 total, top 20 paid, USDC on Solana.

## What it is

A Python 3.13 program, standard library only, no network. `main.py` holds
the summary of world news for Wednesday 11 November 2026 in its own words
and writes it to `$MAKEFUN_OUTPUT_DIR/entry.txt` (1,972 characters).

The summary covers, in order of importance: the US-Iran war declared
"effectively over" and the US-Russia-Ukraine talks in Abu Dhabi; Anthropic's
Nasdaq filing and Nvidia's $10 billion investment; TSMC's dividend and
capital budget; US October CPI and the COP31 summit in Antalya; Treasury
Secretary Bessent on US-China trade; El Salvador's strike on the 400 Mawozo
gang in Haiti; Alibaba spinning off its T-Head chip unit; and two stories
from India — the Supreme Court on digital arrest scams, and a 307-year-old
Mahabharata manuscript entering UNESCO's Memory of the World register.

Every fact was checked against live news sources on 11 November 2026
(PBS NewsHour, France 24, SiliconANGLE, The New York Times, Nikkei Asia,
South China Morning Post, The Hindu, Al Jazeera), and each story names its
source so a reader can verify it. Nothing is invented, and nothing is
presented as fact that was only claimed or unconfirmed.

## Run it

```sh
python3 -m py_compile main.py
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
cat out/entry.txt
```

The program checks the summary is 1 to 2,000 characters before writing,
and both runs write the same bytes. License: MIT (see LICENSE).
