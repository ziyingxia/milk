# -*- coding: utf-8 -*-
"""
Created on Mon Jul 15 07:52:37 2019

@author: stunkard
"""

import socket
s=socket.socket()
print("socket successfully created")
port=12345
s.bind(('',port))
print("socket binded to %s" %(port))
s.listen(5)
print("socket is listening")
while True:
    c,addr=s.accept()
    print("Got connection from",addr)
    c.send("Thank you for connecting")
    c.close()