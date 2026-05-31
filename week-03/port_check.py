import socket

# List of targets to audit
targets = ["127.0.0.1", "8.8.8.8", "1.1.1.1", "10.0.0.1"]

print("--- STARTING PORT AUDIT ---")

for ip in targets:
    print(f"\nChecking Server: {ip}")
    
    # Create a TCP socket (The 'Door Knocker')
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Set a 1-second timeout so the script doesn't hang
    s.settimeout(1)
    
    # Knock on Port 22 (SSH)
    # connect_ex returns 0 if the 'knock' was answered (Port is OPEN)
    result = s.connect_ex((ip, 22))
    
    if result == 0:
        print(f" [+] SUCCESS: Port 22 is OPEN on {ip}")
    else:
        print(f" [-] FAILED: Port 22 is CLOSED on {ip}")
        
    # Always close the socket to free up system resources
    s.close()

print("\n--- AUDIT COMPLETE ---")

