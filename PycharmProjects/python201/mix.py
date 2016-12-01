#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('127.0.0.1', 4242))
s.send('Hello, world!')
data = s.recv(1024)
s.close()
print 'received', data