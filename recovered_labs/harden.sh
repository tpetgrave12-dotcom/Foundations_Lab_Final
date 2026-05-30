#!/bin/bash
# Session 02: System Hardening Script
echo "[*] Starting Security Remediation..."
sudo chmod 640 /etc/shadow
sudo chown root:shadow /etc/shadow
mkdir -p ~/Vault
chmod 700 ~/Vault
echo "[+] Posture Restored: Identity Crisis Averted."

