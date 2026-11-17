# Network Security Incidents Lab – report, Python scripts and sources

**Course:** Information Security, *Network Security Incidents: An Investigation Laboratory*
**Author:** Diellart Mulolli (230756200035)
**Repository:** <https://github.com/Diellart-Mulolli/network_lab>

The laboratory sheet has four segments with six incidents. Where a segment offers two cases, one was chosen:

| Segment | Cases offered | Answered |
|---|---|---|
| 2.1 Routing and Denial of Service | Q1 RPKI account hijack, Q2 HTTP/2 Rapid Reset | **Question 2** |
| 2.2 Web Applications | Q3 Operation RoundPress | **Question 3** |
| 2.3 Firewalls and Intrusion Detection | Q4 firewall as entry point, Q5 forged key and custom alert | **Question 5** |
| 2.4 Authentication Protocols | Q6 backdoor in SSH (xz) | **Question 6** |

This repository holds the report (`report.tex` / `report.pdf`), three Python scripts for the calculations and the date
arithmetic, and `SOURCES.md`, which lists every source with its link and the facts taken from it (the same sources, with
clickable links, are in the reference list of the report). The exact output of the scripts is printed in Appendix A of the
report (the files in `outputs/`).

| Script | Report section | What it shows |
|---|---|---|
| `q2_rapid_reset.py` | Question 2(a)–(c), Appendix A.1 | Record factor, requests/s and bandwidth per bot and in total, a model of HTTP/2 stream accounting |
| `q5_base_rate.py` | Question 5(c), Appendix A.2 | Alerts per day, P(attack \| alert) and analysts needed; why a narrow rule helps |
| `timelines.py` | Questions 5 and 6, Appendix A.3 | The dated timelines with the gaps between events and the exposure windows of the distributions |

## Project structure

```
network_lab/
├── .gitignore               keeps Python caches, virtual environments and LaTeX build files out of git
├── README.md                this file: running guide and explanation of every script
├── SOURCES.md               every source with its link and the facts taken from it
├── report.tex               LaTeX source of the report (IEEE references, pdfLaTeX/Overleaf/Tectonic)
├── report.pdf               compiled report (Appendix A: script values and outputs)
├── report_output.py         small helper shared by the scripts: print() that wraps long lines
├── q2_rapid_reset.py        Q2: record factor, bandwidth calculation, HTTP/2 stream accounting
├── q5_base_rate.py          Q5(c): base-rate calculation of the intrusion detection system
├── timelines.py             Q5 and Q6: dated timelines and gaps
├── outputs/                 verbatim output of each script; report.tex includes these files
│   ├── q2_rapid_reset.txt
│   ├── q5_base_rate.txt
│   └── timelines.txt
└── figures/
    └── README.md            where to put the photo of the hand-drawn diagram of Question 6(b)
```

---

## Running guide

### 1. Prerequisites

| Requirement | Needed for | Check with |
|---|---|---|
| Python 3.8 or newer | all scripts | `python3 --version` |
| LaTeX (or Overleaf) | rebuilding `report.pdf` only | `pdflatex --version` or `tectonic --version` |

All scripts use only the Python standard library: there is nothing to install and no `requirements.txt`.

### 2. Get the project

```bash
git clone https://github.com/Diellart-Mulolli/network_lab.git
```
```bash
cd network_lab
```

### 3. Run the scripts

All commands run from the repository root. The three calculation scripts take well under a second and take
optional arguments (`--help`).

```bash
python3 q2_rapid_reset.py
```
```bash
python3 q5_base_rate.py
```
```bash
python3 timelines.py
```

### 4. Rebuild the report (optional)

The report includes the three files in `outputs/`, so keep that folder next to `report.tex`. To regenerate them:

```bash
python3 q2_rapid_reset.py > outputs/q2_rapid_reset.txt
python3 q5_base_rate.py > outputs/q5_base_rate.txt
python3 timelines.py > outputs/timelines.txt
```

Then compile with any of:

```bash
tectonic report.tex
```
```bash
pdflatex report.tex && pdflatex report.tex
```

On Overleaf, upload the whole folder (including `outputs/` and `figures/`) and set the main file to `report.tex`.

### 5. The hand-drawn diagram of Question 6(b)

The sheet asks for the chain from the xz release tarball to the SSH server to be drawn **by hand**. The report cannot
contain that photograph until it exists: Figure 1 shows a framed placeholder. Draw the seven steps of Table 11, photograph
the drawing, save it as `figures/xz_chain_hand_drawn.jpg` and rebuild; `report.tex` includes it automatically.

### 6. Troubleshooting

| Problem | Cause and fix |
|---|---|
| A link in `SOURCES.md` no longer opens | Search for the title of the source (given in the table). The CSRB report is a PDF on cisa.gov; its facts are in sections 1.2.3, 1.3.1 and the executive summary. |
| `report.pdf` shows the placeholder box in Figure 1 | `figures/xz_chain_hand_drawn.jpg` does not exist yet (see 5). |
| `File outputs/... not found` while compiling | `outputs/` is missing next to `report.tex`; regenerate it as in step 4. |

---

## What each script prints

### `q2_rapid_reset.py`

(a) The record factor 201 / 71 = 2.83. (c) The requests per second per bot (10 050), the attack bandwidth in total and per bot
(96.48 Gbit/s, 4.824 Mbit/s) and the bandwidth the bots would need to receive every response (32.16 Tbit/s, 1.608 Gbit/s), each computed in total and per
bot as a cross-check. (b) A model of one HTTP/2 connection with a stream limit of 100 and a round-trip time of 50 ms: an ordinary client sends
2000 requests in one second and always has up to 100 streams counted, a rapid-reset client sends 10 050 and never has more than one stream
counted; the two closed forms are printed next to the simulation.

### `q5_base_rate.py`

The expected number of malicious events, true alerts and false alerts per day, the alerts per day (50 047.45), P(attack | alert)
(0.0949 %, one alert in 1054) and the analysts needed (835), computed by counting and by Bayes' formula (difference 0). A table shows how
the precision and the staffing change as the false positive rate falls from 10^-2 to 10^-6, and the last block gives an *assumed* narrow rule
(TPR 0.6, FPR 10^-6: 80 alerts per day, precision 37.5 %, 2 analysts).

### `timelines.py`

The Q5 (Storm-0558) and Q6 (xz) timelines with the number of days since the previous event and since the first one, then the selected
intervals used in the report (31, 26 and 188 days for Q5; 882, 243, 343 and 34 days for Q6) and the exposure windows of openSUSE, Debian and Kali.

---

## Sources

All sources are public. They are listed with their links, and with the facts taken from each, in [`SOURCES.md`](SOURCES.md), and
in the reference list of the report (accessed 17 Nov. 2026): the vendor posts and CVE records for Question 2, ESET Research
for Question 3, the Cyber Safety Review Board report and Microsoft's blogs for Question 5, and the oss-security post, Russ Cox's timeline and the distribution announcements for Question 6.
