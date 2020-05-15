# -*- coding: utf-8 -*-
#!/usr/bin/env python2
import os, time, sys
# имена должны быть одинаковыми
fifoname = '/tmp/pipefifo'
def child():
    # открыть fifo как дескриптор
    pipeout = os.open(fifoname, os.O_WRONLY)
    zzz = 0
    while True:
        time.sleep(zzz)
        # был открыт в двоичном режиме
        msg = ('Spam %03d\n' % zzz).encode()
        os.write(pipeout, msg)
        zzz = (zzz+1) % 5
def parent():
    # открыть fifo как текстовый файл
    pipein = open(fifoname, 'r')
    while True:
        # блокируется до отправки данных
        line = pipein.readline()[:-1]
        print('Parent %d got “%s” at %s' % (os.getpid(), line, time.time()))
if __name__ == '__main__':
    if not os.path.exists(fifoname):
        # создаем именованный канал систеной утилитой mkfifo
        os.mkfifo(fifoname)
    if len(sys.argv) == 1:
        # если нет аргументов - запустить как родительский процесс
        parent()
    else:
        # иначе - запустить как дочерний процесс
        child()