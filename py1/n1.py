__author__ = 'luoguoling'
import socket
print "create socket....."
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
print "done"
port = socket.getservbyname('http','tcp')
print "%d" % port
print "connect the romote host..."
s.connect(("www.google.com.hk",port))
print "done"
print "connect from",s.getpeername()
print "connect to",s.getpeername()