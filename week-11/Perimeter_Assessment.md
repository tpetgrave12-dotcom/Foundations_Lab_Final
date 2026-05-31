# TITANCORP: PERIMETER ASSESSMENT REPORT
**Operator:** tpetgrave12 **Target Subnet:** 172.88.0.0/24

## PHASE 1: ACTIVE ENUMERATION (NMAP)
* **Host 1 (172.88.0.20):** HTTP / Apache httpd 2.4.67 (Unix)
* **Host 2 (172.88.0.15):** Redis / Redis key-value store 8.6.3
* **Host 3 (172.88.0.1):** HTTP / Apache httpd (Staging Web Gateway)

## PHASE 2: VULNERABILITY AUDIT (NIKTO)
* **Web Server 1 Finding:** Nikto discovered that the HTTP TRACE method is actively enabled (OSVDB-877), rendering the server vulnerable to Cross-Site Tracing (XST) attacks.
* **Web Server 2 Finding:** Nikto discovered that the anti-clickjacking X-Frame-Options header is completely missing from the HTTP responses, leaving the application vulnerable to UI redressing attacks.

## PHASE 3: RISK TRIAGE
* **Top Priority Finding:** Active HTTP TRACE Method (OSVDB-877) on 172.88.0.20
* **Justification:** The likelihood of exploitation is exceptionally high because this staging asset resides on an exposed, active DMZ perimeter frequently swept by malicious scanners, and the operational impact is severe because it enables attackers to bypass cookie flags and intercept valid corporate streaming credentials.
