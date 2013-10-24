__author__ = 'luoguoling'
#udp connect
import sys,socket
host = '127.0.0.1'
port = 3437
try:
    s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
except socket.error,e:
    print "strange connect %s" % e
    sys.exit(1)
try:
    s.connect((host,port))
except socket.gaierror,e:
    print "connect failed %s" % e
data = sys.stdin.readline().strip()
s.sendall(data)
print "looking for replied,please use crtl+c to break"
while 1:
    buf = s.recv(2048)
    if not len(buf):
        break
    sys.stdout.write(buf)
