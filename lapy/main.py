#! /usr/local/bin/python
import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('0.0.0.0', 8444))
s.listen(1)
c, a = s.accept()
print('connected')
c.sendall('hello world'.encode())
print('send hello')
