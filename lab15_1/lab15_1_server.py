#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import socket 

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 

host = '127.0.0.1'                           
port = 9999 
                                          
serversocket.bind((host, port))                                  
serversocket.listen(5)
print('the server is waiting for connection')        
                                    
while True:
    clientsocket, addr = serversocket.accept()      
    print('Got a connection from {}'.format(addr))
    
    clientsocket.send('Hello'.encode('utf-8'))
    client_answer = clientsocket.recv(1024)
    print(client_answer.decode('utf-8'))

    clientsocket.send('What is your name?'.encode('utf-8'))
    client_answer = clientsocket.recv(1024)
    print(client_answer.decode('utf-8'))
    clientsocket.send('Hello, '.encode('utf-8') + client_answer)
   
    clientsocket.send('My name Ruuuu, '.encode('utf-8'))
    client_answer = clientsocket.recv(1024)
    print(client_answer.decode('utf-8'))
    
    clientsocket.close()



