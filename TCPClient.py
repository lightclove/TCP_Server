# -*- coding: utf-8 -*-
#!/usr/bin/env python2
'''
 В качестве аргумента укажите сообщение, передаваемое на сервер.
 Использование:
    python TCP_Client.py Message to client
'''
#https://documentation.help/Python-2.7/socketserver.html
import ConfigParser
import socket
import sys
import os
# Считывание конфигурационного файла IPC.conf
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
CONFIG_PATH = os.path.join(ROOT_DIR, u'IPC.conf')
config = ConfigParser.ConfigParser()
config.read(CONFIG_PATH)

HOST, PORT = "127.0.0.1", 9999
data = " ".join(sys.argv[1:])
#data = "Message to Client"

# Создадим сокет(SOCK_STREAM - это TCP-сокет)
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Подключимся к серверу и передадим data
sock.connect((HOST, PORT))
sock.send(data + "\n")

# Получим ответ от сервера и закроем сокет клиента
received = sock.recv(1024)
sock.close()

print "Sent message to server: %s" % data
print "Received message from server: %s" % received