
#!/usr/bin/python
import os, sys
from pathlib import Path
print("Home folder location:", Path.home())
import socket
print("Host name:", socket.gethostname())

for line in open('env.txt'):
    print("current shell:", line)
    break
cwd = os.getcwd()
print("current working directiory", cwd)
#process
import subprocess
pl = subprocess.Popen(['ps', '-U', '0'], stdout=subprocess.PIPE).communicate()[0]
print(pl)