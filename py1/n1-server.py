__author__ = 'luoguoling'
#network for server
import socket,sys,traceback
host = "127.0.0.1"
port = 3434
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
s.bind((host,port))
s.listen(1)
while 1:
    try:
        clientsock,clientaddr = s.accept()
    except KeyboardInterrupt:
        raise "accept the connection"
    except:
        traceback.print_exc()
        continue
    #process the connection
    try:
        print "got the connection from %s" % clientsock.getpeername()
    except (KeyboardInterrupt,SystemExit):
        raise
    except:
        traceback.print_exc()
    try:
        clientsock.close()
    except KeyboardInterrupt:
        raise
    except:
        traceback.print_exc()



