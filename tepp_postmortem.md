# Phase 1 Final Reckoning — TEPP Post-Mortem
**Operator:** Trey Petgrave
**Date:** May 30, 2026
**Repository:** https://github.com/tpetgrave12/Foundations_Lab_Final
**TKH Innovation Fellowship 2026 | Phase 1 | Cybersecurity**

---

## Phase 0: Reconnaissance
*   **Triage Network (172.100.0.0/24):** Reconnaissance identified three primary hosts: broken_server_1, broken_server_2, and broken_server_3. Nmap scans revealed exposed Redis (port 6379), FTP (port 21), and insecure directory permissions, establishing these as the primary attack surface.
*   **Breach Network (172.80.0.0/24):** This network contained the midterm_target host, which exhibited evidence of a credential-stuffing attack. Authentication logs confirmed successful unauthorized access, providing the telemetry necessary to identify the attacker's source IP.
*   **Exploitation Network (172.60.0.0/24):** The capstone_target featured a web-based application vulnerable to Remote Command Injection. Initial probes confirmed the application failed to sanitize inputs passed to system-level calls.

## Phase 1: Rapid Triage
*   **Server 1 — 172.100.0.11:** The Redis instance was exposed without authentication, violating the Principle of Least Privilege (NIST, 2018). Remediation was executed via: `docker exec -it broken_server_1 redis-cli CONFIG SET requirepass "StrongPassword123!"`. This moved the service from an open state to an authenticated state.
*   **Server 2 — 172.100.0.12:** An unauthorized vsftpd service was active. Remediation was executed via: `docker exec -it broken_server_2 pkill vsftpd`. This eliminated an unauthorized entry point.
*   **Server 3 — 172.100.0.13:** The directory maintained world-writable permissions. Remediation was executed via: `docker exec -it broken_server_3 chmod 755 /var/www/html`. This restricted write access to the owner only.

## Phase 2: The Breach
*   **Cracked Credentials:** User: root | Password: [wordlist]
*   **Forensic Evidence:** Attacker IP: 172.80.0.5.
*   **Engineered iptables Rule:** `sudo iptables -A INPUT -s 172.80.0.5 -j DROP`.
*   **SOC Analysis:** Static firewall rules are reactive and insufficient as a primary defense. An enterprise-grade SOC must integrate Identity and Access Management (IAM) with Multi-Factor Authentication (MFA) to prevent unauthorized credential usage, complemented by continuous monitoring (NIST, 2018).

## Phase 3: Full Spectrum
*   **Command Injection Explanation:** Command injection occurs when applications improperly incorporate user-supplied data into shell commands. This vulnerability allows an attacker to escape intended logic to execute arbitrary OS commands.
*   **Lockdown Command:** `sudo iptables -A INPUT -p tcp --dport 80 -j DROP`.
*   **Final Analytical Paragraph:** This attack demonstrates that perimeter defense is insufficient if internal application logic is flawed. The most effective defensive control would have been a Web Application Firewall (WAF) configured to drop requests containing shell metacharacters such as ';', '|', or '&'. By adopting the Principle of Least Privilege for web service accounts, organizations can minimize the attack surface, preventing remote code execution even if an injection attempt occurs (NIST, 2018).

## References
National Institute of Standards and Technology. (2018). *Framework for improving critical infrastructure cybersecurity* (Version 1.1). U.S. Department of Commerce. https://doi.org/10.6028/NIST.CSWP.04162018
