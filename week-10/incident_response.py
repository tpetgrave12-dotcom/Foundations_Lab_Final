#!/usr/bin/env python3
import subprocess
import json

print("[*] Starting Automated Threat Hunt...")

# Phase 1: Use Subprocess to grep for Failed Passwords
result = subprocess.run(
    ["grep", "Failed password", "/var/log/titan_sim/auth_sim.log"],
    capture_output=True,
    text=True
)

raw_output = result.stdout

# Phase 2: Data Parsing Logic
lines = raw_output.strip().split('\n')
attacker_ips = []

for line in lines:
    if line:
        # Splitting the line by spaces and grabbing the IP (index 10)
        parts = line.split(" ")
        if len(parts) > 10:
            ip = parts[10]
            attacker_ips.append(ip)

# Phase 3: The JSON Export
alert_data = {
    "alert_type": "Brute Force",
    "attacker_ips": list(set(attacker_ips)) # using set() to remove duplicates
}

with open("threat_report.json", "w") as file:
    json.dump(alert_data, file, indent=4)

print(f"[*] Incident Response Complete. {len(attacker_ips)} signatures exported to threat_report.json")


