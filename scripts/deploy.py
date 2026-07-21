import paramiko
import os

# Connect
client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect('192.168.124.17', port=11928, username='root', password='Weta@0928')

sftp = client.open_sftp()
dist_dir = '/Users/weta/desktop/project/design-lib/docs/.vitepress/dist'
remote_dir = '/var/www/design-lib/'

def upload_dir(local, remote):
    try:
        sftp.mkdir(remote)
    except:
        pass
    for item in os.listdir(local):
        local_path = os.path.join(local, item)
        remote_path = remote + item
        if os.path.isdir(local_path):
            upload_dir(local_path, remote_path + '/')
        else:
            sftp.put(local_path, remote_path)
            print(f'  uploaded: {remote_path}')

print('Deploying...')
upload_dir(dist_dir, remote_dir)
print('Done!')

sftp.close()
client.close()
