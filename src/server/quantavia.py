#!/usr/bin/env python
# Dev port: 5000

import fcntl
import os
from sys import stdin

from gevent import spawn
from gevent.server import StreamServer
from gevent.socket import wait_read

HOST='0.0.0.0'
PORT=5000

# network subsystem tied to command parsing subsystem
def handler(socket, address):
    print 'new connection [%s:%s]!' % (address)
    fileobj = socket.makefile()
    fileobj.write('Welcome to Quantavia.\r\n')
    fileobj.flush()
    while True:
        line = fileobj.readline()
        
        if not line:
            print 'client disconnect'
            break

        if line.strip().lower() == 'look':
            fileobj.write('You are in the strange land of Quantavia.\r\n')
            fileobj.flush()
        elif line.strip().lower() == 'quit':
            fileobj.write('Goodbye.\r\n')
            fileobj.flush()
            break


def stdin_handler():
    fcntl.fcntl(stdin, fcntl.F_SETFL, os.O_NONBLOCK)
    while True:
        wait_read(stdin.fileno())
        cmd = stdin.readline().strip().lower()
        if cmd == 'quit':
            exit(0)

if __name__ == '__main__':
    server = StreamServer((HOST, PORT), handler)
    server.start()
    print 'Quantavia started on host %s port %d' % (HOST, PORT)
    spawn(stdin_handler).join()
