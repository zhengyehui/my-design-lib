#!/usr/bin/env python3
"""Incremental deploy: only upload new/changed files via paramiko."""
import sys, os, time
sys.path.insert(0, '/Users/weta/Library/Python/3.9/lib/python/site-packages')
import paramiko

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect("192.168.124.17", port=11928, username="root", password="Weta@0928")

sftp = ssh.open_sftp()
local_dist = os.path.expanduser('~/desktop/project/design-lib/docs/.vitepress/dist')
remote_base = '/var/www/design-lib/'

ssh.exec_command(f'mkdir -p {remote_base}')

# cache of remote sizes
remote_sizes = {}
def remote_size(path):
    if path in remote_sizes:
        return remote_sizes[path]
    try:
        st = sftp.stat(path)
        remote_sizes[path] = st.st_size
    except IOError:
        remote_sizes[path] = None
    return remote_sizes[path]

uploaded = 0
skipped = 0
made_dirs = set()
for root, dirs, files in os.walk(local_dist):
    for f in files:
        local_path = os.path.join(root, f)
        rel_path = os.path.relpath(local_path, local_dist)
        remote_path = os.path.join(remote_base, rel_path)
        local_sz = os.path.getsize(local_path)
        if remote_size(remote_path) == local_sz:
            skipped += 1
            continue
        remote_dir = os.path.dirname(remote_path)
        if remote_dir not in made_dirs:
            ssh.exec_command(f'mkdir -p {remote_dir}')
            made_dirs.add(remote_dir)
            time.sleep(0.02)
        sftp.put(local_path, remote_path)
        uploaded += 1
        if uploaded % 25 == 0:
            print(f'  ... uploaded {uploaded} files', flush=True)

sftp.close()
ssh.close()
print(f'DONE: uploaded {uploaded} new/changed files, skipped {skipped} unchanged -> {remote_base}')
