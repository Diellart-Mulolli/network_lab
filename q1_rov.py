"""Question 1(b): route origin validation (RFC 6811) applied to the Orange Espana incident of 3 January 2024.

Implements the three states of RFC 6811 (Valid, Invalid, NotFound) and applies them to a few of Orange's
real routes under the sets of ROAs published during the incident (ROAs and times from the APNIC/Kentik
analysis), then shows why routes stayed invalid until the maxLength was raised, and the size of the loss.

    python3 q1_rov.py
"""
from ipaddress import ip_network

from report_output import say

ORANGE, ATTACKER = 12479, 49581

# a ROA is (prefix, maxLength, origin AS); the sets below are the ROAs in force in each phase
PHASES = [
    ("0  before: no ROA for these prefixes (the account had never created one)", []),
    ("1  14:20 UTC: attacker's ROAs with origin AS49581 (the two /12s, plus the earlier /16)",
     [("85.48.0.0/12", 12, ATTACKER), ("90.160.0.0/12", 12, ATTACKER), ("62.36.0.0/16", 16, ATTACKER)]),
    ("2  ~18:00 UTC: Orange regains the account: AS12479 ROAs, maxLength = prefix length",
     [("85.48.0.0/12", 12, ORANGE), ("90.160.0.0/12", 12, ORANGE), ("62.36.0.0/16", 16, ORANGE)]),
    ("3  8 Jan 16:00 UTC: Orange raises the maxLength to 24",
     [("85.48.0.0/12", 24, ORANGE), ("90.160.0.0/12", 24, ORANGE), ("62.36.0.0/16", 24, ORANGE)]),
]

# routes announced by Orange (AS12479); the /24s are real announcements inside the ROA prefixes
ROUTES = [("85.48.0.0/12", ORANGE), ("85.48.12.0/24", ORANGE), ("90.163.112.0/24", ORANGE),
          ("62.36.0.0/16", ORANGE), ("62.36.13.0/24", ORANGE)]
HIJACK = ("85.48.0.0/12", ATTACKER)  # what the attacker could announce, with the matching ROA


def validity(prefix, origin, roas):
    """RFC 6811: Valid if some ROA covers the prefix, its maxLength allows the length and the AS matches;
    Invalid if the prefix is covered but nothing matches; NotFound if nothing covers it."""
    route = ip_network(prefix)
    covered = False
    for p, max_len, asn in roas:
        roa = ip_network(p)
        if roa.version == route.version and roa.prefixlen <= route.prefixlen and route.subnet_of(roa):
            covered = True
            if route.prefixlen <= max_len and asn == origin:
                return "Valid"
    return "Invalid" if covered else "NotFound"


say("RFC 6811 validity of Orange's routes (origin AS12479) in each phase")
say("  Valid = a ROA covers the prefix, allows its length and names the origin AS")
say("  Invalid = covered by a ROA, but none matches (wrong AS or longer than maxLength)")
say("  NotFound = no ROA covers the prefix")
say("")
head = f"  {'route':<18}" + "".join(f"{'phase ' + n[0]:>14}" for n, _ in PHASES)
say(head)
for prefix, origin in ROUTES:
    cells = "".join(f"{validity(prefix, origin, roas):>14}" for _, roas in PHASES)
    say(f"  {prefix:<18}{cells}")
say("")
for name, _ in PHASES:
    say("  phase " + name)
say("")
say("Why only networks that do route origin validation (ROV) lost the routes")
say("  an ROV network drops 'Invalid' routes; a network without ROV accepts every route.")
say("  in phase 1 every Orange route is Invalid, so ROV networks drop it and the others keep it;")
say("  Kentik: when a route is evaluated as Invalid, its propagation is cut in half or more.")
say("")
p, o = HIJACK
say("What the same ROAs allow the attacker (phase 1)")
say(f"  announcing {p} from AS{o}: {validity(p, o, PHASES[1][1])}  (the attacker's own ROA makes his route Valid)")
say(f"  announcing {p} from AS{ORANGE}: {validity(p, ORANGE, PHASES[1][1])}")
say("")
say("Why some routes stayed Invalid until 8 January (phase 2)")
for prefix, origin in ROUTES:
    v2, v3 = validity(prefix, origin, PHASES[2][1]), validity(prefix, origin, PHASES[3][1])
    if v2 != v3:
        length = ip_network(prefix).prefixlen
        say(f"  {prefix:<18} /{length} longer than maxLength 12 or 16: {v2}; with maxLength 24: {v3}")
say("")
routes_before, routes_after = 9200, 7400
addr_before, addr_after = 7_000_000, 5_000_000
say("Size of the loss (Kentik / APNIC, 3-4 January 2024)")
say(f"  globally routed routes of AS12479: {routes_before:,} -> {routes_after:,} = "
    f"-{routes_before - routes_after:,} ({(routes_before - routes_after) / routes_before * 100:.1f} %)")
say(f"  unique IPv4 addresses originated:  {addr_before / 1e6:.0f} M -> {addr_after / 1e6:.0f} M = "
    f"-{(addr_before - addr_after) / 1e6:.0f} M ({(addr_before - addr_after) / addr_before * 100:.1f} %)")
