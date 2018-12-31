import subprocess
import os
import sys
import getopt

sshIP = input("Enter hostname: ")
# sshIP = '172.27.1.12'
sshPort = '22'

# os.system ("dir")

# if this is windows, use putty
if (sys.platform == 'win32'):
    puttyPath = 'C:\\Program Files\\PuTTY\\putty.exe'

# otherwise it will use the ssh command
else:
    puttyPath = ''

print (puttyPath)

print('Opening SSH connection with putty...')
subprocess.call([puttyPath, '-ssh', sshIP, sshPort])

print('script ending...')