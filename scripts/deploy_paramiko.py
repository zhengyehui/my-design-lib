#!/usr/bin/env python3
import paramiko
import os
import sys

# Configuration
host = "192.168.124.17"
port = 11928
username = "root"
password = "Weta@0928"
local_path = os.path.expanduser("~/desktop/project/design-lib/docs/.vitepress/dist/")
remote_path = "/var/www/design-lib/"

print(f"Starting deployment to {host}:{port}")
print(f"Local path: {local_path}")
print(f"Remote path: {remote_path}")

try:
    # Create SSH client
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    
    print("Connecting...")
    ssh.connect(host, port, username, password)
    print("Connected!")
    
    # Create SFTP client
    sftp = ssh.open_sftp()
    
    # Ensure remote directory exists
    try:
        sftp.stat(remote_path)
        print(f"Remote directory exists: {remote_path}")
    except FileNotFoundError:
        print(f"Creating remote directory: {remote_path}")
        sftp.mkdir(remote_path)
    
    # Count files to upload
    file_count = 0
    for root, dirs, files in os.walk(local_path):
        file_count += len(files)
    print(f"Found {file_count} files to upload")
    
    # Upload files
    uploaded = 0
    for root, dirs, files in os.walk(local_path):
        for file in files:
            local_file = os.path.join(root, file)
            relative_path = os.path.relpath(local_file, local_path)
            remote_file = os.path.join(remote_path, relative_path)
            
            # Create subdirectories if needed
            remote_dir = os.path.dirname(remote_file)
            try:
                sftp.stat(remote_dir)
            except FileNotFoundError:
                # Create directories recursively
                parts = remote_dir.split("/")
                current = ""
                for part in parts:
                    if part:
                        current += "/" + part
                        try:
                            sftp.stat(current)
                        except FileNotFoundError:
                            sftp.mkdir(current)
            
            # Upload file
            sftp.put(local_file, remote_file)
            uploaded += 1
            if uploaded % 10 == 0:
                print(f"Uploaded {uploaded}/{file_count} files...")
    
    print(f"Upload completed! Total: {uploaded} files")
    
    # Verify by listing remote directory
    print("\nVerifying deployment...")
    files = sftp.listdir(remote_path)
    print(f"Remote directory now contains {len(files)} items")
    
    sftp.close()
    ssh.close()
    print("Deployment successful!")
    
except Exception as e:
    print(f"Error: {e}")
    import traceback
    traceback.print_exc()
    sys.exit(1)
