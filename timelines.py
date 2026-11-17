"""Dated timelines for Questions 1, 4, 5 and 6 with the gaps between events.

Every date comes from the sources cited in the report (APNIC/Kentik analysis and RIPE NCC for Q1; Talos,
Cisco, CISA and the SecurityWeek report for Q4; CSRB report, Microsoft blogs and CISA advisory for Q5;
oss-security post, R. Cox's xz timeline and distribution announcements for Q6). The script only does the date
arithmetic (days or hours between events, years as days / 365.25). Events given only to the month are
marked with a tilde and counted from the first of the month.

    python3 timelines.py
"""
from datetime import date, datetime

from report_output import say

Q1 = [  # all times UTC (APNIC/Kentik analysis, RIPE NCC announcements)
    (datetime(2024, 1, 3, 9, 28), "attacker starts publishing and revoking ROAs"),
    (datetime(2024, 1, 3, 9, 42), "AS12479 ROAs published (incl. a /16 with maxLength 16)"),
    (datetime(2024, 1, 3, 14, 20), "AS49581 ROAs for two /12s: over 1000 routes Invalid"),
    (datetime(2024, 1, 3, 18, 0), "Orange regains the account, publishes ROAs (before 18:00)"),
    (datetime(2024, 1, 4, 0, 0), "over a thousand AS12479 routes still RPKI-invalid (APNIC)"),
    (datetime(2024, 1, 8, 16, 0), "Orange raises maxLength of the /12s and the /16 to 24"),
    (datetime(2024, 1, 10, 12, 22), "RIPE NCC: 2FA to become mandatory (13:22 CET)"),
    (datetime(2024, 1, 26, 0, 0), "APNIC blog: Madory's (Kentik) analysis"),
    (datetime(2024, 5, 13, 0, 0), "RIPE NCC Access security investigation report"),
]

Q4 = [  # (date, month_only, text)
    (date(2023, 7, 1), True, "ArcaneDoor capability tested, as early as (Talos)"),
    (date(2023, 11, 1), True, "actor infrastructure, early November (Talos)"),
    (date(2023, 12, 1), True, "most ArcaneDoor activity, Dec. to early Jan. (Talos)"),
    (date(2024, 4, 24), False, "Talos and Cisco publish ArcaneDoor; CVE-2024-20353, -20359"),
    (date(2025, 5, 1), True, "Cisco called in to investigate government attacks (SecurityWeek)"),
    (date(2025, 9, 25), False, "ED 25-03; Cisco advisories, CVE-2025-20333 and -20362"),
    (date(2025, 9, 26), False, "ED 25-03: core dumps and updates due, 11:59 PM"),
    (date(2025, 9, 30), False, "ED 25-03: end-of-support ASA hardware disconnected"),
    (date(2025, 10, 2), False, "ED 25-03: complete inventory due, 11:59 PM"),
]

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


def table_dt(title, events):
    say(title)
    say(f"  {'date and time (UTC)':<18}{'+hours':>8}{'total':>8}  event")
    first = prev = events[0][0]
    for d, text in events:
        gap = (d - prev).total_seconds() / 3600
        tot = (d - first).total_seconds() / 3600
        say(f"  {d.strftime('%Y-%m-%d %H:%M'):<18}{gap:>8.1f}{tot:>8.1f}  {text}")
        prev = d
    say("")


def table_month(title, events):
    say(title)
    say(f"  {'date':<11}{'+days':>6}{'total':>7}  event")
    first = prev = events[0][0]
    for d, month_only, text in events:
        label = ("~" + d.strftime("%Y-%m")) if month_only else d.isoformat()
        say(f"  {label:<11}{(d - prev).days:>6}{(d - first).days:>7}  {text}")
        prev = d
    say("")


def gap(a, b, what):
    days = (b - a).days
    unit = "day" if days == 1 else "days"
    say(f"  {what}: {a.isoformat()} -> {b.isoformat()} = {days} {unit} ({days / 365.25:.2f} years)")


table_dt("Question 1: the Orange Espana RIPE NCC account hijack (3 January 2024)", Q1)
say("selected intervals (Question 1)")
h = (Q1[3][0] - Q1[0][0]).total_seconds() / 3600
say(f"  first ROA activity to Orange regaining control: 09:28 -> 18:00 = {h:.1f} h")
h = (Q1[3][0] - Q1[2][0]).total_seconds() / 3600
say(f"  attack ROAs of 14:20 to recovery (traffic drop 14:20 to about 18:00): {h:.1f} h")
d = (Q1[5][0] - Q1[2][0]).total_seconds() / 86400
say(f"  14:20 on 3 Jan. to the maxLength fix on 8 Jan.: {d:.2f} days")
say("")
table_month("Question 4: the Cisco ASA/FTD campaigns (ArcaneDoor 2023-2024, ED 25-03 in 2025)", Q4)
say("selected intervals (Question 4)")
gap(Q4[3][0], Q4[5][0], "ArcaneDoor publication to ED 25-03")
gap(Q4[0][0], Q4[6][0], "first activity (~Jul 2023) to ED deadline")
gap(Q4[5][0], Q4[6][0], "directive issued to the core-dump deadline")
gap(Q4[5][0], Q4[8][0], "directive issued to the inventory deadline")
say("")
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
