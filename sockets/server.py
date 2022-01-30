import socket
import os
import subprocess
from subprocess import Popen
import time
"""
socket.socket-------> To create object for socket
AF_INET ------------> responsible for IPV4 Address
AF_INET6------------> responsible for IPV6 Address 
SOCK.STREAM---------> responsible for To estbalish TCP connection between to nodes
SOCK.DGREAM---------> responsible for To estbalish UDP connection between to nodes

"""

def logmsg(msg):
    msg = "%s %s\n" % (time.strftime("%y%m%d-%H:%M:%S"), msg)
    print (msg)
    f = open(log_filename, 'a')
    f.write(msg)
    f.close()

def runproc(cmnd, wait=1):
    #logmsg("run app: %s" % cmnd)
    if wait:
        lines = []
        proc = subprocess.Popen(cmnd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        while proc.returncode == None:
            lines += proc.stdout.readlines()
            proc.poll()
        lines = [x.decode('UTF8') for x in lines]
        if not lines:
            lines = ['dummy result']
        else:
            print("app output: %s" %"\n".join(lines))
    else:
        lines = ["run in background"]
        proc = subprocess.Popen(cmnd, shell=True, close_fds=True)
        #logmsg("no wait result request, return in 4s")
        time.sleep(4)
    return lines



server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

"""
general format for socket connection estbalishment --------> Object.bind(IP_address, Port_Name) <---->  For server side

"""
test_connection=server.bind((socket.gethostname(), 9998))

server.listen(5)

while 1:
	clientsocket, address= server.accept()
	print("connection is established from {}".format(address))
	clientsocket.send(bytes("Hey there!!!","utf-8"))
	msg = clientsocket.recv(1024)
	print(msg.decode("utf-8"))
	result=runproc(msg)
	clientsocket.send(bytes(str(result),"utf-8"))
