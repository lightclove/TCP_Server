# -*- coding: utf-8 -*-
#!/usr/bin/env python3
#! Tcp echo server
# That’s the nature of TCP: the protocol fills up packets (lower layer being IP packets) and sends them.
# You can have some degree of control over the MTU (Maximum Transfer Unit).
# In other words: you must devise a protocol that rides on top of TCP where your “payload delineation” is defined.
# By “payload delineation” I mean the way you extract the unit of message your protocol supports.
# This can be as simple as “every NULL terminated strings”.
# Tcp_server.py
import socket
from threading import Thread

ADDRESS = ''
PORT = 54321


class TCP_Server(object):
    def __init__(self, destination_host, destination_port):
        self._socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
        self._dest = (destination_host, destination_port)
        self.connections = []
        self.host = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.host.setblocking(0)
        self.host.bind((ADDRESS, PORT))
        self.host.listen(10)  # 10 is how many clients it accepts

    def close_socket(self, connection):
        try:
            self.connection.shutdown(socket.SHUT_RDWR)
        except:
            pass
        try:
            self.connection.close()
        except:
            pass

    def read(self):

        for i in reversed(range(len(self.connections))):
            try:
                data, sender = self.connections[i][0].recvfrom(1500)
                return data
            except (BlockingIOError, socket.timeout, OSError):
                pass
            except (ConnectionResetError, ConnectionAbortedError):
                self.close_socket(self.connections[i][0])
                self.connections.pop(i)
        return b''  # return empty if no data found

    def write(self, data):
        for i in reversed(range(len(self.connections))):
            try:
                self.connections[i][0].sendto(data, self.connections[i][1])
            except (BlockingIOError, socket.timeout, OSError):
                pass
            except (ConnectionResetError, ConnectionAbortedError):
                self.close_socket(self.connections[i][0])
                self.connections.pop(i)

    def run(self):
        # Run the main loop
        print("Program started...")
        print("Server listening on..." + str(self._dest))

        while True:
            try:
                con, addr = self.host.accept()
                self.connections.append((con, addr))
            except BlockingIOError:
                pass

            data = self.read()
            if data != b'':
                print(data)
                self.write(b'ECHO: ' + data)
                if data == b"exit":
                    break

        # Close the sockets
        for i in reversed(range(len(self.connections))):
            self.close_socket(self.connections[i][0])
            self.connections.pop(i)
            self.close_socket(self.host)


########################################################################################################################



def main():
    """
    The main entry point of the application
    """


if __name__ == '__main__':
    TCP_Server = TCP_Server("127.0.0.1", 33333)
    TCP_Server.run()
    # TCP_Server.jokin_Client()
    # Thread(target=jokin_Client).start()
