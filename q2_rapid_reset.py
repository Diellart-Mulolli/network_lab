"""Question 2: HTTP/2 Rapid Reset (CVE-2023-44487): record factor, bandwidth calculation, stream accounting.

(a) factor by which Cloudflare's own record was exceeded,
(c) requests per second per bot, attack bandwidth in total and per bot, and the bandwidth that would be
    needed if the bots had to receive every response (each quantity computed two ways),
(b) a small model of HTTP/2 stream accounting that shows why cancelling defeats SETTINGS_MAX_CONCURRENT_STREAMS.

    python3 q2_rapid_reset.py [--peak 201e6] [--bots 20000] [--request 60] [--response 20000]
"""
import argparse
from fractions import Fraction

from report_output import say

ap = argparse.ArgumentParser()
ap.add_argument("--peak", type=float, default=201e6, help="peak requests per second (Cloudflare)")
ap.add_argument("--prior", type=float, default=71e6, help="Cloudflare's previous record, requests per second")
ap.add_argument("--bots", type=int, default=20000, help="size of the botnet")
ap.add_argument("--request", type=int, default=60, help="bytes per cancelled request (HEADERS + RST_STREAM)")
ap.add_argument("--response", type=int, default=20000, help="bytes of a normal response (20 kB)")
ap.add_argument("--rtt", type=float, default=0.05, help="round-trip time in seconds for the stream model")
ap.add_argument("--limit", type=int, default=100, help="SETTINGS_MAX_CONCURRENT_STREAMS")
a = ap.parse_args()

peak, prior = Fraction(int(a.peak)), Fraction(int(a.prior))
bots, req, resp = a.bots, a.request, a.response

say(f"inputs: peak = {int(peak):,} requests/s, previous record = {int(prior):,} requests/s, bots = {bots:,},")
say(f"        cancelled request = {req} B, normal response = {resp:,} B (1 kB = 1000 B), 1 bit = 1/8 B")
say("")

say("(a) record factor")
say(f"  peak / previous record = {int(peak):,} / {int(prior):,} = {float(peak / prior):.3f}x")
say(f"  (Cloudflare writes 'nearly 3x'; the exact ratio is {float(peak / prior):.2f}, i.e. +{float(peak / prior - 1) * 100:.0f}%)")
say("")

say("(c) calculation")
per_bot = peak / bots
say(f"  (i)   requests per second per bot = {int(peak):,} / {bots:,} = {float(per_bot):,.0f} requests/s")
total_bits = peak * req * 8
per_bot_bits = per_bot * req * 8
say(f"  (ii)  total attack bandwidth = {int(peak):,} x {req} B x 8 = {float(total_bits) / 1e9:.2f} Gbit/s")
say(f"        per bot = {float(per_bot_bits) / 1e6:.3f} Mbit/s")
say(f"        cross-check, per bot x bots: {float(per_bot_bits) / 1e6:.3f} Mbit/s x {bots:,} = "
    f"{float(per_bot_bits * bots) / 1e9:.2f} Gbit/s")
resp_bits = peak * resp * 8
resp_bot_bits = per_bot * resp * 8
say(f"  (iii) bandwidth to receive every response = {int(peak):,} x {resp:,} B x 8 = "
    f"{float(resp_bits) / 1e12:.2f} Tbit/s")
say(f"        per bot = {float(resp_bot_bits) / 1e9:.3f} Gbit/s")
say(f"        cross-check, per bot x bots: {float(resp_bot_bits) / 1e9:.3f} Gbit/s x {bots:,} = "
    f"{float(resp_bot_bits * bots) / 1e12:.2f} Tbit/s")
say(f"  ratio (iii)/(ii) = {resp}/{req} = {float(Fraction(resp, req)):.1f}  (the same for the total and for each bot)")
say("")

say("(b) why cancelling defeats the stream limit: HTTP/2 stream accounting on one connection")
say(f"  SETTINGS_MAX_CONCURRENT_STREAMS = {a.limit}; round-trip time = {a.rtt * 1000:.0f} ms")
say("  Only streams in the states open or half-closed count towards the limit (RFC 9113, 5.1.2).")


def simulate(cancel, seconds=1.0, uplink_bps=float(per_bot_bits)):
    """Client opens streams as fast as it may. Returns (requests sent, highest count against the limit)."""
    counted, peak_counted, sent, done_at = 0, 0, 0, []  # done_at: times at which responses arrive
    t, dt = 0.0, 8 * req / uplink_bps  # time to send one HEADERS (+RST_STREAM) pair on the uplink
    while t < seconds:
        done_at = [x for x in done_at if x > t]
        counted = len(done_at)
        if t + dt > seconds:
            break
        if cancel:
            sent += 1  # HEADERS, then RST_STREAM at once: the stream is closed again immediately
            peak_counted = max(peak_counted, 1)
            t += dt
        elif counted < a.limit:
            sent += 1
            done_at.append(t + a.rtt)  # the stream stays open until the response has come back
            peak_counted = max(peak_counted, counted + 1)
            t += dt
        else:
            t = min(done_at)  # blocked: wait for a stream to finish
    return sent, peak_counted


for cancel in (False, True):
    sent, hi = simulate(cancel)
    name = "rapid reset (HEADERS + RST_STREAM)" if cancel else "ordinary client (waits for the response)"
    say(f"  {name:<42} requests in 1 s: {sent:>6,}   max counted: {hi}")
say(f"  closed form for the ordinary client: limit / RTT = {a.limit} / {a.rtt} = {a.limit / a.rtt:,.0f} requests/s")
say(f"  closed form for rapid reset: uplink / bits per request = {float(per_bot_bits):,.0f} / {req * 8} "
    f"= {float(per_bot_bits) / (req * 8):,.0f} requests/s")
