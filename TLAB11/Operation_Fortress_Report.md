# OPERATION FORTRESS: DEFENSE IN DEPTH REPORT
**Operator:** ## LAYER 1: PERIMETER FIREWALL (iptables)
**Objective:** Block egress to C2 Subnet 198.51.100.0/24
**Rule Used:** [Insert completed iptables command]

## LAYER 2: NETWORK IDS (Suricata)
**Objective:** Detect web shell execution "cmd=whoami"
**Signature Used:** [Insert completed Suricata rule]

## LAYER 3: ENDPOINT SECURITY (Sysmon)
**Objective:** Alert on payload download via curl
**XML Condition Used:** [Insert completed Sysmon CommandLine tag]
