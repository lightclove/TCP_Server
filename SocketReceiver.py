# -*- coding: utf-8 -*-
#!\usr\bin\python
# This is my SNMP trap receiver code
import socket
import sys

from datetime import date

# serverPort = 162
# serverAddress = '192.168.13.117'
# clientPort = 33333
# clientAddress = '192.168.13.210'

import configparser

config = configparser.ConfigParser()
config.read('Agent.conf')

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
serverPort = config.get("server", "serverPort")
s.bind(("0.0.0.0", int(serverPort)))
print('Server accepting data on: ' + str(s.getsockname()))

while 1:
    data, addr = s.recvfrom(33333)
    print('from address: ' + str(addr[0]))
    print('on port: ' + str(addr[1]))
    print(' Received UDP-datagram data:')
    print(data)
