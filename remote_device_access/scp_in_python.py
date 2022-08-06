from paramiko import *
from scp import SCPClient

ssh = SSHClient()
#print "****"
#ssh.load_system_host_keys()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
#print "****"
ssh.connect('hostname="192.168.106.243", username="testuser", password="vvdn123"')
#print "****"
# SCPCLient takes a paramiko transport as an argument
scp = SCPClient(ssh.get_transport())
#print "****"
##scp.put('test.txt', 'test2.txt')
scp.get('test2.txt')
#print "****"

# Uploading the 'test' directory with its content in the
# '/home/user/dump' remote directory
#scp.put('test', recursive=True, remote_path='/home/user/dump')

scp.close()
