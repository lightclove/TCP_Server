# -*- coding: utf-8 -*-
#!/usr/bin/env python2
'''
    TCPServer использует протокол TCP, который обеспечивает непрерывные потоки данных(data streams) между клиентом и сервером.
    https://documentation.help/Python-2.7/socketserver.html
'''
import SocketServer

'''
    Класс обработчик входящих запросов для сервера, создается один раз для каждого соединения с сервером и должен переопределить метод handle () для реализации связи с клиентом.
'''
class MyTCPHandler(SocketServer.BaseRequestHandler):

    def handle(self):
        # self.request is the TCP socket connected to the client
        self.data = self.request.recv(1024).strip()
        print "%s wrote:" % self.client_address[0]
        print self.data
        # just send back the same data, but upper-cased
        self.request.send(self.data.upper())
'''
    Альтернативный класс обработчика запросов, который использует потоки (файловые объекты, которые упрощают связь, предоставляя стандартный файловый интерфейс):
    Разница в том, что вызов readline () во втором обработчике будет вызывать recv() несколько раз, пока не встретит символ новой строки, в то время как одиночный вызов recv()
    в первом обработчике просто вернет то, что было отправлено с клиента в одном вызовe send() .
'''

class MyStreamRequestHandler(SocketServer.StreamRequestHandler):

    def handle(self):
        # self.rfile - это файловый объект, созданный обработчиком;
        # теперь можно использовать, например, readline () вместо необработанных вызовов recv ()
        self.data = self.rfile.readline().strip()
        print "%s wrote:" % self.client_address[0]
        print self.data
        # Аналогично, self.wfile - это файловый объект, используемый для обратной записи клиенту
        self.wfile.write(self.data.upper())

if __name__ == "__main__":
    HOST, PORT = "127.0.0.1", 9999

    # Создайте сервер, передадим ему нужный обработчик запросов
    server = SocketServer.TCPServer((HOST, PORT), MyStreamRequestHandler)

    # Наконец, вызовите метод handle_request () или serve_forever () объекта сервера для обработки одного или нескольких запросов.
    # Активация сервера,
    print('Server is running on host: ' + str(HOST) + ' and port: ' + str(PORT))
    print('Press Ctrl + C to interrupt server process')
    server.serve_forever()

