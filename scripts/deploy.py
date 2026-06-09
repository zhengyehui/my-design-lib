#!/usr/bin/env python3
import sys
sys.path.insert(0, '/Users/weta/Library/Python/3.9/lib/python/site-packages')
import paramiko
import os

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect('192.168.124.17', port=11928, username='root', password='Weta@0928')

# Clear target directory contents
stdin, stdout, stderr = ssh.exec_command('find /var/www/design-lib -mindepth 1 -delete')
stdout.channel.recv_exit_status()

# Upload using sftp
sftp = ssh.open_sftp()
local_dist = os.path.expanduser('~/desktop/project/design-lib/docs/.vitepress/dist')
remote_base = '/var/www/design-lib'

for root, dirs, files in os.walk(local_dist):
    rel = os.path.relpath(root, local_dist)
    remote_dir = os.path.join(remote_base, rel)
    try:
        sftp.mkdir(remote_dir)
    except:
        pass
    for f in files:
        local_path = os.path.join(root, f)
        remote_path = os.path.join(remote_dir, f)
        sftp.put(local_path, remote_path)

sftp.close()
ssh.close()
print('✅ Deploy complete!')
