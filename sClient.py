# -*- coding: utf-8 -*-
#!\usr\bin\python
import socket
sock = socket.socket()
sock.connect(('192.168.13.66', 9091))
numChan = raw_input('Insert number of channel:')
sock.send(numChan)
data = sock.recv(1024)
sock.close()
#print data

