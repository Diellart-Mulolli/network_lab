# Sources

Every source used in `report.tex`, grouped by question. The numbers in brackets are the reference numbers of
the report (the same sources, with their URLs, are in its reference list). All pages were read on 17 November 2026.
For each source the table says which facts of the report come from it, so any figure can be checked by opening the link.

## Course material

| Ref | Source | Facts taken from it |
|---|---|---|
| [1] | M. Stamp, *Information Security: Principles and Practice*, 3rd ed., Wiley, 2022, chapters 8–9 | concepts of the questions: protocol stack, denial of service, XSS, firewalls and defence in depth, IDS and base rate, authentication protocols |

## Question 1 – Orange España and the hijacked RPKI account (3 January 2024)

| Ref | Source | Facts taken from it |
|---|---|---|
| [2] | RIPEstat (web interface and Data API: rpki-validation, announced-prefixes, as-overview) and RIPE Database, organisation ORG-IA73-RIPE <https://stat.ripe.net/> | holder names of AS12479 and AS21246; the ROAs of 85.48.0.0/12 (AS12479, maxLength 24) and 91.187.96.0/19 (AS21246, maxLength 19) on 17 Nov. 2026; IPKO's address in Prishtina, Republic of Kosovo; the screenshots of Question 1(d) |
| [3] | J. Greig, J. Warminsky, "Major Spanish mobile carrier suffers three-hour outage after account takeover", The Record, 4 Jan. 2024 <https://therecord.media/orange-espana-outage-hacker-internet-ripe-bgp-rpki> | Orange's statement (some customers affected, service practically restored, no client data compromised); the RIPE NCC statement (account restored to the legitimate holder, 2FA to be mandatory); Cloudflare's 50 % traffic fall |
| [4] | H. P. Holen, "[News] Security Breach: Investigation Update", RIPE NCC, ncc-announce, 10 Jan. 2024 <https://www.ripe.net/ripe/mail/archives/ncc-announce/2024-January/001695.html> | 800 forced password resets; two-factor authentication to become mandatory; password guidance |
| [5] | D. Madory (Kentik), "Digging into the Orange España hack", APNIC Blog, 26 Jan. 2024 <https://blog.apnic.net/2024/01/26/digging-into-the-orange-espana-hack/> | the technical analysis: AS12479 and AS49581; times in UTC (09:28, 09:42, about 14:20, just before 18:00, 8 Jan. 16:00); the ROAs and their maxLength; 9,200 to 7,400 routes; 7 to 5 million addresses; over a thousand routes still invalid; the password 'ripeadmin' found in a public leak; the account had never created a ROA |
| [6] | P. Mohapatra et al., "BGP Prefix Origin Validation", RFC 6811, Jan. 2013 <https://www.rfc-editor.org/rfc/rfc6811> | the states Valid, Invalid and NotFound and the matching rule with the maximum length (used in q1_rov.py) |
| [7] | Y. Gilad et al., "The Use of maxLength in the Resource Public Key Infrastructure (RPKI)", RFC 9319 (BCP 185), Oct. 2022 <https://www.rfc-editor.org/rfc/rfc9319> | operators should generally avoid maxLength; forged-origin sub-prefix hijacks |
| [8] | "Weak password and infostealer blamed for Orange Spain outage", The Register, 4 Jan. 2024 <https://www.theregister.com/2024/01/04/orange_spain_outage_breach/> | Hudson Rock: employee account in infostealer logs since August 2023, password 'ripeadmin'; two-factor authentication not enabled and not mandated by RIPE; ARIN has required it since Feb. 2023 |
| [9] | RIPE NCC, "RIPE NCC Access: Security Investigation Report", 13 May 2024 <https://www.ripe.net/publications/documentation/disclosures-and-reports/ripe-ncc-access-security-investigation-report/> | 870 accounts with exposed passwords (104 linked to LIR accounts), 270 changed e-mail addresses; mandatory 2FA, longer passwords and lock-out, automated resets, 2FA visibility for admins, e-mail addresses can no longer be changed |

## Question 2 – HTTP/2 Rapid Reset (CVE-2023-44487)

| Ref | Source | Facts taken from it |
|---|---|---|
| [11] | Cloudflare, "HTTP/2 Zero-Day vulnerability results in record-breaking DDoS attacks", 10 Oct. 2023 <https://blog.cloudflare.com/zero-day-rapid-reset-http2-record-breaking-ddos-attack/> | peak above 201 million requests/s; botnet of roughly 20,000 machines; joint disclosure with Google and AWS |
| [12] | Cloudflare, "HTTP/2 Rapid Reset: Deconstructing the record-breaking attack", 10 Oct. 2023 <https://blog.cloudflare.com/technical-breakdown-http2-rapid-reset-ddos-attack/> | first big attacks on 25 Aug. 2023; HEADERS and RST_STREAM; a reset stream is closed, so the concurrency limit is never reached; the lower limit of 64 caused page-load failures and was restored to 100 |
| [13] | Google Cloud, "How it works: The novel HTTP/2 'Rapid Reset' DDoS attack", 10 Oct. 2023 <https://cloud.google.com/blog/products/identity-security/how-it-works-the-novel-http2-rapid-reset-ddos-attack> | the server still does the work of cancelled requests; rate limited by bandwidth, not round-trip time; closing abusive connections |
| [14] | Google Cloud, "Google Cloud mitigated largest DDoS attack, peaking above 398 million rps", 10 Oct. 2023 <https://cloud.google.com/blog/products/identity-security/google-cloud-mitigated-largest-ddos-attack-peaking-above-398-million-rps> | Google's peak of 398 million requests/s; attacks since August 2023 |
| [15] | T. Scholl, M. Ryland, "How AWS protects customers from DDoS events", AWS Security Blog, 10 Oct. 2023 <https://aws.amazon.com/blogs/security/how-aws-protects-customers-from-ddos-events/> | AWS peak of over 155 million requests/s; events since late August 2023 (28–29 Aug. spike on CloudFront) |
| [16] | Cloudflare, "Cloudflare mitigates record-breaking 71 million request-per-second DDoS attack", 13 Feb. 2023 <https://blog.cloudflare.com/cloudflare-mitigates-record-breaking-71-million-request-per-second-ddos-attack/> | Cloudflare's previous record of 71 million requests/s; it exceeded the 46 million of June 2022 by more than 54 % |
| [17] | M. Thomson, C. Benfield, "HTTP/2", RFC 9113, June 2022, section 5.1.2 <https://www.rfc-editor.org/rfc/rfc9113> | only open and half-closed streams count towards SETTINGS_MAX_CONCURRENT_STREAMS |
| [18] | Go Vulnerability Database, GO-2023-2102 (CVE-2023-39325) <https://pkg.go.dev/vuln/GO-2023-2102> | fixed in Go 1.20.10, Go 1.21.3 and golang.org/x/net v0.17.0; handlers capped at MaxConcurrentStreams (default 250), queue, connection closed if the queue grows |

## Question 3 – Operation RoundPress

| Ref | Source | Facts taken from it |
|---|---|---|
| [19] | M. Faou, "Operation RoundPress targeting high-value webmail servers", ESET Research, 15 May 2025 <https://www.welivesecurity.com/en/eset-research/operation-roundpress/> | attribution to Sednit (APT28, Fancy Bear, Forest Blizzard) with medium confidence; the eight countries and the sectors; Roundcube CVE-2020-35730 and CVE-2023-43770 (patched 14 Sep. 2023; an e-mail of 29 Sep. 2023 used it), Horde, MDaemon CVE-2024-11182 (zero-day, fixed in 24.5.1 on 14 Nov. 2024), Zimbra CVE-2024-27443 (patched 1 Mar. 2024); the SpyPress payloads, the Sieve forwarding rule, the App Password and 2FA secret |
| [20] | MDN Web Docs, "Content Security Policy (CSP)" <https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/CSP> | meaning of default-src, script-src (nonces, no inline scripts), connect-src, form-action, img-src, base-uri, object-src, frame-ancestors |

## Question 4 – The Cisco ASA firewall campaign (ArcaneDoor 2024, ED 25-03 in 2025)

| Ref | Source | Facts taken from it |
|---|---|---|
| [21] | CISA, "ED 25-03: Identify and Mitigate Potential Compromise of Cisco Devices", 25 Sep. 2025 (updated 23 Apr. 2026) <https://www.cisa.gov/news-events/directives/ed-25-03-identify-and-mitigate-potential-compromise-cisco-devices> | products in scope (ASA hardware, ASA-SM, ASAv, FTD); the two CVEs; deadlines (26 Sep. 2025 11:59 PM core dumps and updates, 30 Sep. disconnect end-of-support hardware, 2 Oct. inventory); update within 48 hours; link to ArcaneDoor; ROM manipulation to persist; an update does not necessarily remove the actor |
| [22] | Cisco, "Cisco Event Response: Continued Attacks Against Cisco Firewalls", 25 Sep. 2025 (updated 24 Apr. 2026) <https://sec.cloudapps.cisco.com/security/center/resources/asa_ftd_continued_attacks> | same actor as ArcaneDoor (high confidence); product families; CVE-2025-20333, -20362, -20363; VPN web server; ROMMON modification on models without Secure Boot; disabling logging, intercepting commands; no successful compromise observed where Secure Boot and Trust Anchor exist; mitigation by disabling VPN services; reset and rotate credentials; end-of-support dates |
| [23] | Cisco, Security Advisory cisco-sa-asaftd-webvpn-z5xP8EUB, 25 Sep. 2025 <https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-asaftd-webvpn-z5xP8EUB> | CVE-2025-20333 (VPN web server remote code execution, CVSS 9.9, needs VPN credentials); affected configurations (webvpn, IKEv2 client services); no workarounds; final fixed releases 9.12.4.72 and 9.14.4.28 for the oldest 5500-X models |
| [24] | Cisco Talos, "ArcaneDoor – New espionage-focused campaign found targeting perimeter network devices", 24 Apr. 2024 (updated 25 Sep. 2025) <https://blog.talosintelligence.com/arcanedoor-new-espionage-focused-campaign-found-targeting-perimeter-network-devices/> | UAT4356 / Storm-1849; testing from about July 2023, infrastructure in early November 2023, activity December 2023 to early January 2024; a customer's report in early 2024; CVE-2024-20353 and CVE-2024-20359; Line Dancer and Line Runner; the capabilities (disable syslog, packet capture, AAA bypass, crash-dump tampering) |
| [25] | I. Arghire, "Cisco Firewall Zero-Days Exploited in China-Linked ArcaneDoor Attacks", SecurityWeek, 26 Sep. 2025 <https://www.securityweek.com/cisco-firewall-zero-days-exploited-in-china-linked-arcanedoor-attacks/> | Cisco called in during May 2025 to investigate attacks on government organisations; the ROM modification and the missing Secure Boot; the models |
| [26] | UK NCSC, "RayInitiator & LINE VIPER", Malware Analysis Report v1.1, Oct. 2025 <https://www.ncsc.gov.uk/static-assets/documents/malware-analysis-reports/RayInitiator-LINE-VIPER/ncsc-mar-rayinitiator-line-viper.pdf> | the GRUB bootkit that survives reboots and upgrades; models without secure boot (released 2012, end-of-life notice 2020, all past or at the last day of support on 30 Sep. 2025); LINE VIPER's capabilities (packet capture, AAA bypass, syslog suppression, delayed reboot, anti-forensics) |

## Question 5 – Storm-0558 and the forged key

| Ref | Source | Facts taken from it |
|---|---|---|
| [27] | Microsoft Threat Intelligence, "Analysis of Storm-0558 techniques for unauthorized email access", 14 Jul. 2023 (updated Aug. 2024) <https://www.microsoft.com/en-us/security/blog/2023/07/14/analysis-of-storm-0558-techniques-for-unauthorized-email-access/> | China-based actor, moderate confidence (now Antique Typhoon); forged tokens from 15 May 2023; customer report on 16 Jun. 2023; about 25 organisations; mitigation dates in June and July 2023 |
| [28] | Cyber Safety Review Board, "Review of the Summer 2023 Microsoft Exchange Online Intrusion", 20 Mar. 2024 <https://www.cisa.gov/sites/default/files/2025-03/CSRBReviewOfTheSummer2023MEOIntrusion508.pdf> | 'preventable'; 22 organisations and 503 personal accounts; about 60,000 e-mails from State; State's detection on 15–16 Jun. 2023 with the 'Big Yellow Taxi' rule on MailItemsAccessed (G5 licence, Purview Audit Premium); the 2016 MSA key, planned retirement in March 2021, the common OIDC endpoint and SDK flaw; Microsoft's inaccurate blog and its correction on 12 Mar. 2024 (sections 1.2.3.1, 1.2.3.2, 1.3.1 and the executive summary) |
| [29] | Microsoft Security Response Center, "Results of Major Technical Investigations for Storm-0558 Key Acquisition", 6 Sep. 2023 (updated 12 Mar. 2024) <https://www.microsoft.com/en-us/msrc/blog/2023/09/results-of-major-technical-investigations-for-storm-0558-key-acquisition> | the crash-dump explanation of 6 Sep. 2023 and the correction of 12 Mar. 2024; the validation issue after the move to a common metadata endpoint |
| [30] | CISA and FBI, "Enhanced Monitoring to Detect APT Activity Targeting Outlook Online", AA23-193A, 12 Jul. 2023 <https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-193a> | detection through MailItemsAccessed events with an unexpected AppId |

## Question 6 – the xz backdoor (CVE-2024-3094)

| Ref | Source | Facts taken from it |
|---|---|---|
| [31] | A. Freund, "backdoor in upstream xz/liblzma leading to ssh server compromise", oss-security, 29 Mar. 2024 <https://www.openwall.com/lists/oss-security/2024/03/29/4> | the original post; versions 5.6.0 and 5.6.1; 0.299 s against 0.807 s for ssh, sshd -h 0.5 s against 0.01 s; valgrind, perf and gdb; release tarball versus repository; IFUNC and audit hook; RSA_public_decrypt redirected; libsystemd and the distribution patch |
| [32] | CISA, "Reported Supply Chain Compromise Affecting XZ Utils Data Compression Library, CVE-2024-3094", 29 Mar. 2024 <https://www.cisa.gov/news-events/alerts/2024/03/29/reported-supply-chain-compromise-affecting-xz-utils-data-compression-library-cve-2024-3094> | advice to downgrade to XZ Utils 5.4.6 |
| [33] | R. Cox, "Timeline of the xz open source attack", research!rsc <https://research.swtch.com/xz-timeline> | all dates of the timeline of Jia Tan (29 Oct. 2021 to 29 Mar. 2024), the Debian dates, Arch building from git on 28 Mar. 2024 |
| [34] | Debian Security Tracker, CVE-2024-3094 <https://security-tracker.debian.org/tracker/CVE-2024-3094> | Debian stable (bookworm) not affected |
| [35] | Red Hat, "Urgent security alert for Fedora 40 and Fedora Rawhide users", 29 Mar. 2024 (updated 30 Mar.) <https://www.redhat.com/en/blog/urgent-security-alert-fedora-41-and-rawhide-users> | Fedora Rawhide and Fedora 40 beta builds; no RHEL version affected |
| [36] | M. Meissner, "openSUSE addresses supply chain attack against xz compression library", 29 Mar. 2024 <https://news.opensuse.org/2024/03/29/xz-backdoor/> | Tumbleweed and MicroOS affected 7–28 Mar. 2024 |
| [37] | Kali Linux, "All about the xz-utils backdoor", 29 Mar. 2024 <https://www.kali.org/blog/about-the-xz-backdoor/> | xz-utils 5.6.0-0.2 available 26–29 Mar. 2024 |
| [38] | A. E. Patrakov quoting F. Valsorda's preliminary analysis, oss-security, 31 Mar. 2024 <https://www.openwall.com/lists/oss-security/2024/03/30/36> | payload in the N value of the RSA public key, fingerprint, ChaCha20, Ed448 signature, then system(); the backdoor reverts to normal operation if anything fails. Early analyses differ in detail |
| [39] | OpenSSH Project, "OpenSSH 9.8 release notes", 2024 <https://www.openssh.org/txt/release-9.8> | systemd notification with a standalone implementation that does not depend on libsystemd |

## Vulnerability records (several questions)

| Ref | Source | Facts taken from it |
|---|---|---|
| [10] | NIST National Vulnerability Database, records of CVE-2023-44487, CVE-2020-35730, CVE-2023-43770, CVE-2024-11182, CVE-2024-27443, CVE-2024-3094, CVE-2024-20353, CVE-2024-20359, CVE-2025-20333, CVE-2025-20362 <https://nvd.nist.gov/vuln/detail/CVE-2023-44487> (same path for the others) | publication dates and CVSS scores of every CVE named in the report (for example CVE-2023-44487: 10 Oct. 2023, 7.5; CVE-2024-3094: 29 Mar. 2024, 10.0; CVE-2025-20333: 25 Sep. 2025, 9.9; CVE-2025-20362: 25 Sep. 2025, NVD 8.6 and Cisco 6.5) |

## Notes

- The screenshots of Question 1(d) (`figures/q1_orange_ripestat.png`, `figures/q1_ipko_ripestat.png`) are real captures of the RIPEstat web interface and of the RIPEstat Data API response, taken with a headless Chromium on 17 November 2026; the header strip of each image was added afterwards and states the date. The query times of the API responses (about 21:50 UTC) are visible inside the screenshots.
- The CSRB report [28] is a PDF on cisa.gov; if the address changes, search for the title on cisa.gov.
- Figures that are *computed* in the report (record factor, bandwidths, base-rate counts, ROV validity, the gaps between dates) come from the four scripts in this repository, not from the sources; the inputs of those calculations come from the sources above.
- Items marked in the report as my own reasoning and not as a statement of a source: that a password change does not remove the Roundcube Sieve rule or the MDaemon App Password (Question 3), the account-takeover scenarios for IPKO and the argument about stronger protection of RPKI accounts (Question 1), and the narrow-rule example values of Question 5(c).
