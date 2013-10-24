__author__ = 'luoguoling'
import socket,sys
#handle errors
#host = sys.argv[1]
#textport = sys.argv[2]
#filename = sys.argv[3]
host = '8.8.8.8'
textport = '80'
filename = 'a.txt'
try:
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
except socket.error,e:
    print "strange error creating socket %s" % e
    sys.exit(1)
#try parsing it as a numeric port
try:
    port = int(textport)
except ValueError:
    #maybe it is not a protocol name
    try:
        port = socket.getservbyname(textport,'tcp')
    except socket.error,e:
        print "i can not find the port %s" % e
        sys.exit(1)
try:
    s.connect((host,port))
except socket.gaierror,e:
    print "address-related error %s" % e
    sys.exit(1)
try:
    s.sendall("GET %s HTTP/1.0\R\N\R\N" % filename)
except socket.error,e:
    print "error sending data: %s" % e
    sys.exit(1)
try:
    s.shutdown(1)
except socket.error,e:
    print "error sending data %s" % e
    sys.exit(1)
while 1:
    try:
        buf = s.recv(2048)
    except socket.error,e:
        print "error receiving data:%s" % e
        sys.exit(1)
    if not len(buf):
        break
    sys.stdout.write(buf)








