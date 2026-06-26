#!/usr/bin/env python3
import os, sys, time

sys.path.insert(0, '/Users/weta/Library/Python/3.9/lib/python/site-packages')
import paramiko

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect("192.168.124.17", port=11928, username="root", password="Weta@0928")

sftp = ssh.open_sftp()
local_dist = os.path.expanduser('~/desktop/project/design-lib/docs/.vitepress/dist')
remote_base = '/var/www/design-lib/'

ssh.exec_command(f'mkdir -p {remote_base}')

uploaded = 0
for root, dirs, files in os.walk(local_dist):
    for f in files:
        local_path = os.path.join(root, f)
        rel_path = os.path.relpath(local_path, local_dist)
        remote_path = os.path.join(remote_base, rel_path)
        remote_dir = os.path.dirname(remote_path)
        ssh.exec_command(f'mkdir -p {remote_dir}')
        time.sleep(0.03)
        sftp.put(local_path, remote_path)
        uploaded += 1

sftp.close()
ssh.close()
print(f'Deployed {uploaded} files to {remote_base}')
