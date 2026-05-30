import sys
sys.path.insert(0, '/Users/weta/Library/Python/3.9/lib/python/site-packages')
import paramiko
import os

# Pack the dist directory
dist_dir = os.path.expanduser('~/desktop/project/design-lib/docs/.vitepress/dist')
tarball = '/tmp/design-lib-dist.tar.gz'

# Create tarball
import subprocess
result = subprocess.run(
    ['tar', 'czf', tarball, '-C', dist_dir, '.'],
    capture_output=True, text=True
)
if result.returncode != 0:
    print(f"Tar failed: {result.stderr}")
    sys.exit(1)

tarball_size = os.path.getsize(tarball) / 1024 / 1024
print(f"📦 Tarball created: {tarball_size:.1f} MB")

# Upload via paramiko
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect('192.168.124.17', port=11928, username='root', password='Weta@0928')
print("🔐 Connected to server")

# Upload tarball
sftp = ssh.open_sftp()
sftp.put(tarball, '/tmp/design-lib-dist.tar.gz')
sftp.close()
print("📤 Tarball uploaded")

# Extract on remote
stdin, stdout, stderr = ssh.exec_command(
    'cd /var/www/design-lib && tar xzf /tmp/design-lib-dist.tar.gz && rm /tmp/design-lib-dist.tar.gz'
)
exit_code = stdout.channel.recv_exit_status()
if exit_code != 0:
    print(f"Extract failed: {stderr.read().decode()}")
else:
    print("✅ Extracted to /var/www/design-lib/")

ssh.close()

# Verify
import urllib.request
try:
    resp = urllib.request.urlopen('http://192.168.124.17:11928/')
    print(f"🌐 Verification: HTTP {resp.status}")
except Exception as e:
    print(f"⚠️ Verification failed: {e}")

# Cleanup
os.remove(tarball)
print("🧹 Cleaned up tarball")
