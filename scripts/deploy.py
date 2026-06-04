#!/usr/bin/env python3
import subprocess
import sys

# Step 1: Upload tarball via scp
print("📤 Uploading tarball...")
result = subprocess.run(
    ["scp", "-P", "11928", "/tmp/design-lib-dist.tar.gz", "root@192.168.124.17:/tmp/"],
    capture_output=True, text=True, timeout=120
)
if result.returncode != 0:
    print(f"❌ SCP failed: {result.stderr}")
    sys.exit(1)
print("✅ Tarball uploaded")

# Step 2: Extract on remote server
print("📦 Extracting on server...")
result = subprocess.run(
    ["ssh", "-p", "11928", "root@192.168.124.17",
     "cd /var/www/design-lib && tar xzf /tmp/design-lib-dist.tar.gz && rm /tmp/design-lib-dist.tar.gz"],
    capture_output=True, text=True, timeout=120
)
if result.returncode != 0:
    print(f"❌ Extract failed: {result.stderr}")
    sys.exit(1)
print("✅ Extracted to /var/www/design-lib/")

# Step 3: Verify
print("🔍 Verifying deployment...")
result = subprocess.run(
    ["ssh", "-p", "11928", "root@192.168.124.17",
     "ls -la /var/www/design-lib/pages/fintech-payment-landing/"],
    capture_output=True, text=True, timeout=30
)
print(result.stdout)
print("✅ Deployment complete!")
