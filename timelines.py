"""Dated timelines for Question 5 (Storm-0558) and Question 6 (xz backdoor) with the gaps between events.

Every date comes from the sources cited in the report (CSRB report, Microsoft blogs, CISA advisory for Q5;
oss-security post, R. Cox's xz timeline, distribution announcements for Q6). The script only does the date
arithmetic (days between events, years as days / 365.25).

    python3 timelines.py
"""
from datetime import date

from report_output import say

Q5 = [
    (date(2023, 5, 15), "Storm-0558 gains access to email accounts (CSRB)"),
    (date(2023, 6, 15), "State's SOC detects anomalous mailbox access (CSRB)"),
    (date(2023, 6, 16), "'Big Yellow Taxi' alerts; State notifies Microsoft (CSRB)"),
    (date(2023, 6, 26), "Microsoft finds a consumer key forged the tokens (CSRB)"),
    (date(2023, 6, 29), "Microsoft replaces the MSA signing keys (Microsoft blog)"),
    (date(2023, 7, 11), "Microsoft's first public disclosure (MSRC blog)"),
    (date(2023, 7, 12), "CISA/FBI advisory AA23-193A on detecting the activity"),
    (date(2023, 9, 6), "Microsoft blames a 2021 crash dump for the key theft (blog)"),
    (date(2024, 3, 12), "Microsoft corrects it: no crash dump with the key found"),
    (date(2024, 3, 20), "CSRB report on the Exchange Online intrusion is dated"),
]

Q6 = [
    (date(2021, 10, 29), "first contribution by 'Jia Tan' (an .editorconfig patch)"),
    (date(2022, 4, 22), "first pressure e-mail to the maintainer (Jigar Kumar)"),
    (date(2022, 6, 10), "first commit with 'Jia Tan' as author"),
    (date(2022, 6, 29), "Collin: Jia is 'practically a co-maintainer already'"),
    (date(2022, 10, 28), "Jia Tan joins the Tukaani GitHub organisation"),
    (date(2022, 12, 30), "Jia Tan merges commits directly into the xz repo"),
    (date(2023, 3, 18), "Jia Tan tags the first own release, v5.4.2"),
    (date(2024, 2, 23), "backdoor code merged into binary test files"),
    (date(2024, 2, 24), "v5.6.0 released; tarball has the malicious build-to-host.m4"),
    (date(2024, 3, 9), "v5.6.1 released"),
    (date(2024, 3, 28), "Freund finds the backdoor, tells Debian and distros@openwall"),
    (date(2024, 3, 29), "disclosure on oss-security; CVE-2024-3094"),
]


def table(title, events):
    say(title)
    say(f"  {'date':<11}{'+days':>6}{'total':>7}  event")
    first, prev = events[0][0], events[0][0]
    for d, text in events:
        say(f"  {d.isoformat():<11}{(d - prev).days:>6}{(d - first).days:>7}  {text}")
        prev = d
    say("")


def gap(a, b, what):
    days = (b - a).days
    say(f"  {what}: {a.isoformat()} -> {b.isoformat()} = {days} days ({days / 365.25:.2f} years)")


table("Question 5: Storm-0558 and the Exchange Online intrusion", Q5)
say("selected intervals (Question 5)")
gap(Q5[0][0], Q5[1][0], "intrusion start to detection")
gap(Q5[1][0], Q5[5][0], "detection to public disclosure")
gap(Q5[7][0], Q5[8][0], "inaccurate blog to its correction")
say("")
table("Question 6: the xz backdoor", Q6)
say("selected intervals (Question 6)")
gap(Q6[0][0], Q6[11][0], "first contribution to disclosure")
gap(Q6[0][0], Q6[3][0], "first contribution to co-maintainer status")
gap(Q6[6][0], Q6[8][0], "first own release to backdoored release")
gap(Q6[8][0], Q6[11][0], "backdoored v5.6.0 release to disclosure")
say("")
say("exposure of the distributions that shipped the backdoored xz (dates from their announcements)")
gap(date(2024, 3, 7), date(2024, 3, 28), "openSUSE Tumbleweed and MicroOS")
gap(date(2024, 2, 26), date(2024, 3, 28), "Debian unstable")
gap(date(2024, 3, 26), date(2024, 3, 29), "Kali")
