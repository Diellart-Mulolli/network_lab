# Network Security Incidents Lab – report, Python scripts and sources

**Course:** Information Security, *Network Security Incidents: An Investigation Laboratory*
**Author:** Diellart Mulolli (230756200035)
**Repository:** <https://github.com/Diellart-Mulolli/network_lab>

The laboratory sheet has four segments with six incidents. **All six are answered** in the report:

| Segment | Question | Incident |
|---|---|---|
| 2.1 Routing and Denial of Service | Q1 | Orange España and the hijacked RPKI account (Jan. 2024) |
| 2.1 Routing and Denial of Service | Q2 | HTTP/2 Rapid Reset (2023) |
| 2.2 Web Applications | Q3 | Operation RoundPress, webmail XSS (2023–2024) |
| 2.3 Firewalls and Intrusion Detection | Q4 | The Cisco ASA firewall campaign (ArcaneDoor 2024, ED 25-03 in 2025) |
| 2.3 Firewalls and Intrusion Detection | Q5 | Storm-0558 and the forged key (2023) |
| 2.4 Authentication Protocols | Q6 | The backdoor in xz and SSH (2024) |

This repository holds the report (`report.tex` / `report.pdf`), four Python scripts for the calculations, the route-validation example and the
date arithmetic, the screenshots of Question 1(d), and `SOURCES.md`, which lists every source with its link and the facts taken from it (the same
sources, with clickable links, are in the reference list of the report). The exact output of the scripts is printed in Appendix A of the report
(the files in `outputs/`).

| Script | Report section | What it shows |
|---|---|---|
| `q1_rov.py` | Question 1(b), Appendix A.1 | Route origin validation (RFC 6811) of Orange's routes under the ROAs of each phase of the incident; the loss of routes and addresses |
| `q2_rapid_reset.py` | Question 2(a)–(c), Appendix A.2 | Record factor, requests/s and bandwidth per bot and in total, a model of HTTP/2 stream accounting |
| `q5_base_rate.py` | Question 5(c), Appendix A.3 | Alerts per day, P(attack \| alert) and analysts needed; why a narrow rule helps |
| `timelines.py` | Questions 1, 4, 5 and 6, Appendix A.4 | The dated timelines with the gaps between events and the exposure windows of the distributions |

## Project structure

```
network_lab/
├── .gitignore               keeps Python caches, virtual environments and LaTeX build files out of git
├── README.md                this file: running guide and explanation of every script
├── SOURCES.md               every source with its link and the facts taken from it
├── report.tex               LaTeX source of the report (IEEE references, pdfLaTeX/Overleaf/Tectonic)
├── report.pdf               compiled report (Appendix A: script values and outputs)
├── report_output.py         small helper shared by the scripts: print() that wraps long lines
├── q1_rov.py                Q1(b): route origin validation of Orange's routes in each phase
├── q2_rapid_reset.py        Q2: record factor, bandwidth calculation, HTTP/2 stream accounting
├── q5_base_rate.py          Q5(c): base-rate calculation of the intrusion detection system
├── timelines.py             Q1, Q4, Q5 and Q6: dated timelines and gaps
├── outputs/                 verbatim output of each script; report.tex includes these files
│   ├── q1_rov.txt
│   ├── q2_rapid_reset.txt
│   ├── q5_base_rate.txt
│   └── timelines.txt
└── figures/
    ├── q1_orange_ripestat.png   dated RIPEstat screenshots for Question 1(d)
    ├── q1_ipko_ripestat.png
    └── README.md                where to put the photos of the two hand drawings (Q4(b) and Q6(b))
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

All commands run from the repository root. The four scripts take well under a second and take
optional arguments (`--help`).

```bash
python3 q1_rov.py
```
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

The report includes the four files in `outputs/`, so keep that folder next to `report.tex`. To regenerate them:

```bash
python3 q1_rov.py > outputs/q1_rov.txt
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

### 5. The hand drawings of Questions 4(b) and 6(b)

The sheet asks for two diagrams to be drawn **by hand** (Q4(b): the Internet, the firewall/VPN appliance as outer firewall, the DMZ, an inner firewall and the internal network; Q6(b): the chain from the
xz release tarball to the SSH server). A photograph of a real drawing cannot be produced by the scripts, so each figure in the report is a typeset reference
diagram that shows what the drawing must contain. Draw them, photograph them, save the photos as `figures/q4_network_hand_drawn.jpg` and
`figures/xz_chain_hand_drawn.jpg`, and rebuild: `report.tex` includes a photo automatically when the file exists and shows the typeset diagram otherwise.

### 5b. The screenshots of Question 1(d)

`figures/q1_orange_ripestat.png` and `figures/q1_ipko_ripestat.png` are captures of the RIPEstat web interface (Prefix Overview) and of the RIPEstat Data API response
(`https://stat.ripe.net/data/rpki-validation/data.json?resource=AS12479&prefix=85.48.0.0/12`, and the same for AS21246 and 91.187.96.0/19), taken on 17 November 2026. To redo
them, open the two addresses in a browser and take new screenshots.

### 6. Troubleshooting

| Problem | Cause and fix |
|---|---|
| A link in `SOURCES.md` no longer opens | Search for the title of the source (given in the table). The CSRB report is a PDF on cisa.gov; its facts are in sections 1.2.3, 1.3.1 and the executive summary. |
| Figures 3 and 4 show typeset diagrams, not photos | The photos `figures/q4_network_hand_drawn.jpg` and `figures/xz_chain_hand_drawn.jpg` do not exist yet (see 5). |
| `File outputs/... not found` while compiling | `outputs/` is missing next to `report.tex`; regenerate it as in step 4. |

---

## What each script prints

### `q1_rov.py`

The RFC 6811 validity (Valid, Invalid, NotFound) of five of Orange's routes in four phases: before the incident (no ROA), with the attacker's ROAs for AS49581
(everything Invalid), after the recovery with ROAs for AS12479 whose maxLength equals the prefix length (the /12 and /16 Valid, the /24s Invalid) and after
8 January with maxLength 24 (all Valid). It also shows that the attacker's own ROA makes a hijack from AS49581 Valid, and the size of the loss (9 200 to 7 400 routes,
7 to 5 million addresses).

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

The timelines of Q1 (in hours, UTC), Q4 (ArcaneDoor to ED 25-03), Q5 (Storm-0558) and Q6 (xz) with the time since the previous event and since the first one, then the selected
intervals used in the report (3.7 h, 8.5 h and 5 days for Q1; 519 and 818 days for Q4; 31, 26 and 188 days for Q5; 882, 243, 343 and 34 days for Q6) and the exposure windows of openSUSE, Debian and Kali.

---

## Sources

All sources are public. They are listed with their links, and with the facts taken from each, in [`SOURCES.md`](SOURCES.md), and
in the reference list of the report (accessed 17 Nov. 2026): the vendor posts and CVE records for Question 2, ESET Research
for Question 3, the Cyber Safety Review Board report and Microsoft's blogs for Question 5, and the oss-security post, Russ Cox's timeline and the distribution announcements for Question 6.
