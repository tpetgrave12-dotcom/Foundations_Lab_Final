#!/bin/bash
# =================================================
# SESSION 11: THE DISPOSABLE WEB SERVER
# Operator Deployment Script
# =================================================

echo "[*] Initiating Container Deployment..."

# Stop/Remove existing container to prevent conflicts
docker rm -f training-web 2>/dev/null

# Run the nginx image in detached mode, name it "training-web",
# and map port 8080 on the host to port 80 on the container.
docker run -d --name training-web -p 8080:80 nginx

echo "[+] Deployment command executed."
