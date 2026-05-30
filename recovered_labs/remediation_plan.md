# Remediation Plan - CloudNano Corp

## 1. Unauthenticated AWS S3 Bucket (Contains Customer PII) [CVSS 9.8]
- **Justification:** The likelihood of compromise is extreme because the bucket requires absolutely no authentication over the open internet, while the impact is catastrophic due to the direct public exposure of regulated customer PII.

## 2. Remote Code Execution in Apache Struts (Internet Facing Web Server) [CVSS 9.8]
- **Justification:** Because this asset is directly internet-facing, the likelihood of automated malicious scanning is exceptionally high, carrying a severe operational impact that allows an attacker to take full code execution control over the host.

## 3. SQL Injection in Login Page (Customer Database Portal) [CVSS 8.1]
- **Justification:** Authentication entry points face a high likelihood of targeted web attacks, resulting in a massive data impact where unauthorized actors can manipulate back-end queries to dump the entire customer database.

## 4. SMBv1 Enabled (Internal HR File Server) [CVSS 9.0]
- **Justification:** Legacy protocols are heavily targeted inside corporate perimeters, creating a dangerous likelihood of fast internal worm or ransomware propagation with a devastating impact on sensitive HR files.

## 5. Cross-Site Scripting (XSS) on Support Forum [CVSS 8.8]
- **Justification:** The likelihood of exploitation is elevated because the support forum actively renders user-supplied input, leading to a high-impact threat scenario where attackers can silently steal session tokens from authenticated enterprise employees.
