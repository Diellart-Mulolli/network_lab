# Sources

Every source used in `report.tex`, grouped by question. The numbers in brackets are the reference numbers of
the report (the same sources, with their URLs, are in its reference list). All pages were read on 17 November 2026.
For each source the table says which facts of the report come from it, so any figure can be checked by opening the link.

## Course material

| Ref | Source | Used for |
|---|---|---|
| [1] | M. Stamp, *Information Security: Principles and Practice*, 3rd ed., Wiley, 2022, chapters 8–9 | concepts of the questions: protocol stack, denial of service, XSS, firewalls and IDS, base rate, authentication protocols |

## Question 2 – HTTP/2 Rapid Reset (CVE-2023-44487)

| Ref | Source | Facts taken from it |
|---|---|---|
| [2] | NVD record of CVE-2023-44487 <https://nvd.nist.gov/vuln/detail/CVE-2023-44487> | published 10 Oct. 2023, CVSS v3 base score 7.5 (High) |
| [3] | Cloudflare, "HTTP/2 Zero-Day vulnerability results in record-breaking DDoS attacks", 10 Oct. 2023 <https://blog.cloudflare.com/zero-day-rapid-reset-http2-record-breaking-ddos-attack/> | peak above 201 million requests/s; botnet of roughly 20,000 machines; joint disclosure with Google and AWS |
| [4] | Cloudflare, "HTTP/2 Rapid Reset: deconstructing the record-breaking attack", 10 Oct. 2023 <https://blog.cloudflare.com/technical-breakdown-http2-rapid-reset-ddos-attack/> | first big attacks on 25 Aug. 2023; HEADERS and RST_STREAM; a reset stream is closed, so the concurrency limit is never reached; the lower limit of 64 caused page-load failures and was restored to 100 |
| [5] | Google Cloud, "How it works: The novel HTTP/2 'Rapid Reset' DDoS attack", 10 Oct. 2023 <https://cloud.google.com/blog/products/identity-security/how-it-works-the-novel-http2-rapid-reset-ddos-attack> | the server still does the work of cancelled requests; rate limited by bandwidth, not round-trip time; closing abusive connections |
| [6] | Google Cloud, "Google Cloud mitigated largest DDoS attack, peaking above 398 million rps", 10 Oct. 2023 <https://cloud.google.com/blog/products/identity-security/google-cloud-mitigated-largest-ddos-attack-peaking-above-398-million-rps> | Google's peak of 398 million requests/s; attacks since August 2023 |
| [7] | T. Scholl and M. Ryland, "How AWS protects customers from DDoS events", AWS Security Blog, 10 Oct. 2023 <https://aws.amazon.com/blogs/security/how-aws-protects-customers-from-ddos-events/> | AWS peak of over 155 million requests/s; events since late August 2023 (28–29 Aug. spike on CloudFront) |
| [8] | Cloudflare, "Cloudflare mitigates record-breaking 71 million request-per-second DDoS attack", 13 Feb. 2023 <https://blog.cloudflare.com/cloudflare-mitigates-record-breaking-71-million-request-per-second-ddos-attack/> | Cloudflare's previous record of 71 million requests/s; it exceeded the 46 million of June 2022 by more than 54 % |
| [9] | M. Thomson, C. Benfield, "HTTP/2", RFC 9113, June 2022, section 5.1.2 <https://www.rfc-editor.org/rfc/rfc9113> | only open and half-closed streams count towards SETTINGS_MAX_CONCURRENT_STREAMS |
| [10] | Go Vulnerability Database, GO-2023-2102 (CVE-2023-39325) <https://pkg.go.dev/vuln/GO-2023-2102> | fixed in Go 1.20.10, Go 1.21.3 and golang.org/x/net v0.17.0; handlers capped at MaxConcurrentStreams (default 250), queue, connection closed if the queue grows |

## Question 3 – Operation RoundPress

| Ref | Source | Facts taken from it |
|---|---|---|
| [11] | M. Faou, "Operation RoundPress targeting high-value webmail servers", ESET Research, 15 May 2025 <https://www.welivesecurity.com/en/eset-research/operation-roundpress/> | attribution to Sednit (APT28, Fancy Bear, Forest Blizzard) with medium confidence; the eight countries and the sectors; Roundcube CVE-2020-35730 and CVE-2023-43770 (patched 14 Sep. 2023), Horde, MDaemon CVE-2024-11182 (zero-day, fixed in 24.5.1 on 14 Nov. 2024), Zimbra CVE-2024-27443 (patched 1 Mar. 2024); the SpyPress payloads, the Sieve forwarding rule, the App Password and 2FA secret |
| [2] | NVD records of CVE-2020-35730, CVE-2023-43770, CVE-2024-11182, CVE-2024-27443 <https://nvd.nist.gov/vuln/detail/CVE-2023-43770> (same path for the others) | publication dates 28 Dec. 2020, 22 Sep. 2023, 15 Nov. 2024, 12 Aug. 2024; CVSS v3 base score 6.1 for all four; the XSS descriptions |
| [12] | MDN Web Docs, "Content Security Policy (CSP)" <https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/CSP> | meaning of default-src, script-src (nonces, no inline scripts), connect-src, form-action, img-src, base-uri, object-src, frame-ancestors |

## Question 5 – Storm-0558 and the forged key

| Ref | Source | Facts taken from it |
|---|---|---|
| [13] | Microsoft Threat Intelligence, "Analysis of Storm-0558 techniques for unauthorized email access", Microsoft Security Blog, 14 Jul. 2023 (updated Aug. 2024) <https://www.microsoft.com/en-us/security/blog/2023/07/14/analysis-of-storm-0558-techniques-for-unauthorized-email-access/> | China-based actor with moderate confidence (now Antique Typhoon); forged tokens from 15 May 2023; customer report on 16 Jun. 2023; about 25 organisations; mitigation dates in June and July 2023 |
| [14] | Cyber Safety Review Board, "Review of the Summer 2023 Microsoft Exchange Online Intrusion", 20 Mar. 2024 <https://www.cisa.gov/sites/default/files/2025-03/CSRBReviewOfTheSummer2023MEOIntrusion508.pdf> | "preventable"; 22 organisations and 503 personal accounts; about 60,000 e-mails from State; State's detection on 15–16 Jun. 2023 with the "Big Yellow Taxi" rule on MailItemsAccessed (G5 licence, Purview Audit Premium); the 2016 MSA key, planned retirement in March 2021, the common OIDC endpoint and SDK flaw; Microsoft's inaccurate blog and its correction on 12 Mar. 2024 (report sections 1.2.3.1, 1.2.3.2, 1.3.1 and the executive summary) |
| [15] | Microsoft Security Response Center, "Results of major technical investigations for Storm-0558 key acquisition", 6 Sep. 2023 (updated 12 Mar. 2024) <https://www.microsoft.com/en-us/msrc/blog/2023/09/results-of-major-technical-investigations-for-storm-0558-key-acquisition> | the crash-dump explanation of 6 Sep. 2023 and the correction of 12 Mar. 2024; the validation issue after the move to a common metadata endpoint |
| [16] | CISA and FBI, "Enhanced monitoring to detect APT activity targeting Outlook Online", AA23-193A, 12 Jul. 2023 <https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-193a> | detection through MailItemsAccessed events with an unexpected AppId |

## Question 6 – the xz backdoor (CVE-2024-3094)

| Ref | Source | Facts taken from it |
|---|---|---|
| [17] | A. Freund, "backdoor in upstream xz/liblzma leading to ssh server compromise", oss-security, 29 Mar. 2024 <https://www.openwall.com/lists/oss-security/2024/03/29/4> | the original post; versions 5.6.0 and 5.6.1; 0.299 s against 0.807 s for `ssh`, `sshd -h` 0.5 s against 0.01 s; valgrind, perf and gdb; release tarball versus repository; IFUNC and audit hook; RSA_public_decrypt redirected; libsystemd and the distribution patch |
| [2] | NVD record of CVE-2024-3094 <https://nvd.nist.gov/vuln/detail/CVE-2024-3094> | published 29 Mar. 2024, CVSS v3 base score 10.0 (critical) |
| [18] | CISA, "Reported supply chain compromise affecting XZ Utils data compression library, CVE-2024-3094", 29 Mar. 2024 <https://www.cisa.gov/news-events/alerts/2024/03/29/reported-supply-chain-compromise-affecting-xz-utils-data-compression-library-cve-2024-3094> | advice to downgrade to XZ Utils 5.4.6 |
| [19] | R. Cox, "Timeline of the xz open source attack", research!rsc <https://research.swtch.com/xz-timeline> | all dates of the timeline of Jia Tan (29 Oct. 2021 to 29 Mar. 2024), the Debian dates, Arch building from git on 28 Mar. 2024 |
| [20] | Debian Security Tracker, CVE-2024-3094 <https://security-tracker.debian.org/tracker/CVE-2024-3094> | Debian stable (bookworm) not affected |
| [21] | Red Hat, "Urgent security alert for Fedora 40 and Fedora Rawhide users", 29 Mar. 2024 (updated 30 Mar.) <https://www.redhat.com/en/blog/urgent-security-alert-fedora-41-and-rawhide-users> | Fedora Rawhide and Fedora 40 beta builds; no RHEL version affected |
| [22] | M. Meissner, "openSUSE addresses supply chain attack against xz compression library", 29 Mar. 2024 <https://news.opensuse.org/2024/03/29/xz-backdoor/> | Tumbleweed and MicroOS affected 7–28 Mar. 2024 |
| [23] | Kali Linux, "All about the xz-utils backdoor", 29 Mar. 2024 <https://www.kali.org/blog/about-the-xz-backdoor/> | xz-utils 5.6.0-0.2 available 26–29 Mar. 2024 |
| [24] | A. E. Patrakov quoting F. Valsorda's preliminary analysis, oss-security, 31 Mar. 2024 <https://www.openwall.com/lists/oss-security/2024/03/30/36> | payload in the N value of the RSA public key, fingerprint, ChaCha20, Ed448 signature, then `system()`; the backdoor reverts to normal operation if anything fails. Early analyses differ in detail |
| [25] | OpenSSH Project, "OpenSSH 9.8 release notes", 2024 <https://www.openssh.org/txt/release-9.8> | systemd notification with a standalone implementation that does not depend on libsystemd |

## Notes

- The CSRB report [14] is a PDF on cisa.gov; if the address changes, search for the title on cisa.gov.
- Figures that are *computed* in the report (record factor, bandwidths, base-rate counts, the gaps between dates) come from the three scripts in this repository, not from the sources; the inputs of those calculations come from the sources above.
- Two items are explicitly marked in the report as my own reasoning and not as a statement of a source: that a password change does not remove the Roundcube Sieve rule or the MDaemon App Password (Question 3), and the narrow-rule example values of Question 5(c).
