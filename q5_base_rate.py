"""Question 5(c): base rate of an intrusion detection system with 5e7 events per day.

Counts expected true and false alerts, P(attack | alert) and the analysts needed (each computed with
exact fractions and with Bayes' formula), then shows why a narrow rule helps (assumed illustrative values).

    python3 q5_base_rate.py [--events 5e7] [--prevalence 1e-6] [--tpr 0.95] [--fpr 1e-3] [--capacity 60]
"""
import argparse
import math
from fractions import Fraction

from report_output import say

ap = argparse.ArgumentParser()
ap.add_argument("--events", type=float, default=5e7, help="events per day")
ap.add_argument("--prevalence", type=float, default=1e-6, help="fraction of events that are malicious")
ap.add_argument("--tpr", type=float, default=0.95, help="detection rate (true positive rate)")
ap.add_argument("--fpr", type=float, default=1e-3, help="false positive rate")
ap.add_argument("--capacity", type=int, default=60, help="alerts one analyst investigates per day")
a = ap.parse_args()

N = Fraction(int(a.events))
p = Fraction(a.prevalence).limit_denominator(10**12)
tpr = Fraction(a.tpr).limit_denominator(10**6)
fpr = Fraction(a.fpr).limit_denominator(10**9)

say(f"events per day N = {int(N):,}; p = {float(p):g}; TPR = {float(tpr)}; FPR = {float(fpr):g}; "
    f"capacity = {a.capacity} alerts per analyst per day")
say("")
bad = N * p
good = N - bad
tp = bad * tpr
fp = good * fpr
alerts = tp + fp
say("method 1: expected counts per day")
say(f"  malicious events         N*p          = {float(bad):,.1f}")
say(f"  benign events            N*(1-p)      = {float(good):,.2f}")
say(f"  true alerts              N*p*TPR      = {float(tp):,.2f}")
say(f"  false alerts             N*(1-p)*FPR  = {float(fp):,.2f}")
say(f"  alerts per day                        = {float(alerts):,.2f}")
prec = tp / alerts
say(f"  P(attack | alert) = {float(tp):.2f} / {float(alerts):,.2f} = {float(prec):.6f} = {float(prec) * 100:.4f} %"
    f"  (one alert in {float(1 / prec):,.0f} is real)")
analysts = alerts / a.capacity
say(f"  analysts = {float(alerts):,.2f} / {a.capacity} = {float(analysts):.2f} -> {math.ceil(analysts)} analysts")
say("")
bayes = (tpr * p) / (tpr * p + fpr * (1 - p))
say("method 2: Bayes' formula  P = TPR*p / (TPR*p + FPR*(1-p))")
say(f"  P(attack | alert) = {float(bayes):.6f}   (difference to method 1: {float(abs(bayes - prec)):.1e})")
say(f"  share of alerts that are false = {float(1 - bayes) * 100:.4f} %")
say("")
say("sensitivity: precision and analysts as the false positive rate falls (TPR kept at 0.95)")
say(f"  {'FPR':>8} {'alerts/day':>12} {'P(attack|alert)':>16} {'analysts':>9}")
for f in (Fraction(1, 100), Fraction(1, 1000), Fraction(1, 10**4), Fraction(1, 10**5), Fraction(1, 10**6)):
    al = bad * tpr + good * f
    say(f"  {float(f):>8.0e} {float(al):>12,.0f} {float(bad * tpr / al):>16.6f} {math.ceil(al / a.capacity):>9}")
say("")
say("narrow rule (assumed values for illustration, not taken from the incident):")
say("  a rule for one pattern only, e.g. mailbox access by an application ID not seen before")
t2, f2 = Fraction(6, 10), Fraction(1, 10**6)
al2 = bad * t2 + good * f2
say(f"  TPR = {float(t2)} (misses many attacks), FPR = {float(f2):g}")
say(f"  alerts per day = {float(bad * t2):.1f} true + {float(good * f2):.1f} false = {float(al2):.1f};  "
    f"P(attack | alert) = {float(bad * t2 / al2):.3f};  analysts = {math.ceil(al2 / a.capacity)}")
say(f"  compared with the general rule: {float(alerts):,.0f} alerts/day, precision {float(prec):.4f}, "
    f"{math.ceil(analysts)} analysts")
