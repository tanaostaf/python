#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import socket 

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  

host = '127.0.0.1'                           
port = 9999

s.connect((host, port)) 
                              
server_responce = s.recv(1024)
print(server_responce.decode('utf-8'))

a = input()
s.send(a.encode('utf-8'))    
server_responce = s.recv(1024)                                
print(server_responce.decode('utf-8'))

b = input()
s.send(b.encode('utf-8'))
server_responce = s.recv(1024)                                
print(server_responce.decode('utf-8'))

c = input()
s.send(c.encode('utf-8'))
server_responce = s.recv(1024)                                
print(server_responce.decode('utf-8'))

s.close()

input ('Press ENTER to exit') 
