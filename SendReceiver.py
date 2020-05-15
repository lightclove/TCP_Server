# -*- coding: utf-8 -*-
#!\usr\bin\python
import socket
import sys

###########
from threading import Thread

HOST = '127.0.0.1'
PORT = 9999
###########

name = input("Enter your name: ")
s = socket.socket()
s.connect((HOST,PORT))

def recv():
    while True:
         data = s.recv(1024)
         if not data: sys.exit(0)
         print (data)

#KillableThread(target=recv).start()

while 1:
    message = input("Message: ")
    s.send("{}: {}".format(name, message).encode('utf-8'))
    #data = s.recv(1024)
    #a = data.decode("utf-8")

    #print(a)
