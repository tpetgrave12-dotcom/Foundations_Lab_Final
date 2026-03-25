# The Scoreboard
attack_count = 0

# The Double Doors (Open the messy log and the clean report)
# Note: The lab script just created auth_audit.log for you!
with open("auth_audit.log", "r") as log_file:
    with open("brute_report.txt", "w") as report_file:
        
        # The Conveyor Belt
        for line in log_file:
            # The X-Ray Vision
            if "Failed password" in line:
                report_file.write(line)
                attack_count = attack_count + 1

# The Final Announcement
print(f"[*] Audit Complete. Extracted {attack_count} threat signatures to brute_report.txt")

