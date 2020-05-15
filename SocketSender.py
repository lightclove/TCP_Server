# -*- coding: utf-8 -*-
#!\usr\bin\python
#! tcp/udp client as sender
import socket


class SocketSender(object):
    @property
    def get_SOCKET(self):
        return self.__SOCKET

    def set_SOCKET(self, SOCKET):
        self.__SOCKET = SOCKET

    @property
    def get_PORT(self):
        return self.__PORT

    def set_PORT(self, PORT):
        self.__PORT = PORT

    @property
    def get_ADDRESS(self):
        return self.ADDRESS

    def set_ADDRESS(self, ADDRESS):
        self.__ADDRESS = ADDRESS

    def __init__(self, ADDRESS, PORT):
        #        ADDRESS = "127.0.0.1"
        #        PORT = 33333
        self.__ADDRESS = ADDRESS
        self.__PORT = PORT

        SOCKET = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        SOCKET.connect((ADDRESS, PORT))
        SOCKET.setblocking(0)
        self.SOCKET = SOCKET

    def close_socket(self, connection):
        socket = self.SOCKET
        try:
            socket.shutdown(socket.SHUT_RDWR)
        except:
            pass
        try:
            connection.close()
        except:
            pass

    def read(self):
        """Read data and return the read bytes."""
        socket = self.SOCKET
        try:
            data, sender = socket.recvfrom(1500)
            return data
        except (BlockingIOError, socket.timeout, AttributeError, OSError):
            return b''
        except (ConnectionResetError, ConnectionAbortedError, AttributeError):
            self.close_socket(socket)
            return b''

    def write(self, data):
        socket = self.SOCKET
        try:
            socket.sendto(data, (self.set_ADDRESS, self.set_PORT))
        except (ConnectionResetError, ConnectionAbortedError):
            self.close_socket(socket)


########################################################################################################################
def main():
    """
    The main entry point of the application
    """
    print("Program started...")


if __name__ == '__main__':
    s = SocketSender("127.0.0.1", 33333)
    while True:
        msg = input("Enter a message: ")
        s.write(msg.encode('utf-8'))
        data = s.read()
        if data != b"":
            print("Message Received:", data)

        if msg == "exit":
            break

    s.close_socket()
