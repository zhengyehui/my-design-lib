#!/usr/bin/env python3
import sys, os, time
sys.path.insert(0, '/Users/weta/Library/Python/3.9/lib/python/site-packages')
import paramiko

transport = paramiko.Transport(('192.168.124.17', 11928))
transport.connect(username='root', password='Weta@0928')
sftp = paramiko.SFTPClient.from_transport(transport)

local_dist = os.path.expanduser('~/desktop/project/design-lib/docs/.vitepress/dist')
remote_base = '/var/www/design-lib'

def upload_dir(local_dir, remote_dir):
    try:
        sftp.mkdir(remote_dir)
    except:
        pass
    for item in os.listdir(local_dir):
        local_path = os.path.join(local_dir, item)
        remote_path = remote_dir + '/' + item
        if os.path.isdir(local_path):
            upload_dir(local_path, remote_path)
        else:
            sftp.put(local_path, remote_path)

upload_dir(local_dist, remote_base)
sftp.close()
transport.close()
print(f'Deployed successfully to {remote_base}')
