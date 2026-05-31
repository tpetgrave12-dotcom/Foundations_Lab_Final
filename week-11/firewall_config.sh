#!/bin/bash
# S31: The Barricade - Firewall Config Script
# Operator: tpetgrave12

# 1. Allow standard HTTP and HTTPS traffic into the web server
iptables -A INPUT -p tcp -m multiport --dports 80,443 -j ACCEPT

# 2. Allow the web server to communicate with the internal database on the SQL port only
iptables -A OUTPUT -p tcp -d 10.0.5.50 --dport 3306 -j ACCEPT

# 3. Drop all other outbound traffic attempting to reach the internal subnet
iptables -A OUTPUT -d 10.0.5.0/24 -j DROP
