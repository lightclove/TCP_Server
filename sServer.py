#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket

sock = socket.socket()
sock.bind(('127.0.0.1', 9091))
sock.listen(1)
conn, addr = sock.accept()

channel1_state = "On"
channel2_state = "Off"
channel3_state = "Off"
channel4_state = "Off"

def switch_case(case):
    return "Received: " + {
        '1' : conn.send(  " Channel 1 state:" + channel1_state),
        '2' : conn.send(  " Channel 2 state:" + channel2_state),
        '3' : conn.send(  " Channel 3 state:" + channel3_state),
        '4' : conn.send(  " Channel 4 state:" + channel4_state)
    }.get(case, "an out of range number")

print 'Сервер работает:', addr

while True:

    data = conn.recv(1024)
    if not data:
        break

   	switch_case(data)

    #conn.send(  " Channel 1 state:" + channel1_state)
    #conn.send(  " Channel 1 state:" + channel1_state + '\n' + " Channel 2 state:" + channel2_state + '\n' + " Channel 3 state:" + channel3_state + '\n' + " Channel 4 state:" + channel4_state)

    #conn.send(channel1_state, channel2_state, channel3_state, channel4_state)