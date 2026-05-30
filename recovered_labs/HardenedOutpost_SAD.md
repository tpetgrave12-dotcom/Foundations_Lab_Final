# TITAN SMALL BUSINESS SERVICES: SECURITY ARCHITECTURE DOCUMENT (SAD)
**Operator:** tpetgrave12
**Date:** May 10, 2026

## 1. Perimeter Hardening (UFW & SSH)
* **SSH Status:** Hardened. Disabled root login and password authentication by modifying `/etc/ssh/sshd_config` (PermitRootLogin no, PasswordAuthentication no).
* **Firewall Logic:** Implemented a "Default Deny" policy. Explicitly allowed Port 22 (SSH) and Port 8080 (App) to ensure a minimal attack surface.

## 2. The Automated Auditor (Python)
* **Script Logic:**
```python
import os
import datetime
target_dc = "8.8.8.8"
status = os.system(f"ping -c 2 {target_dc} > /dev/null 2>&1")
timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
with open("/tmp/dc_audit.log", "a") as log:
    if status == 0:
        log.write(f"[{timestamp}] DC CONNECTION SUCCESSFUL\n")
    else:
        log.write(f"[{timestamp}] DC CONNECTION FAILED\n")
