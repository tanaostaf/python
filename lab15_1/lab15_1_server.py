#! /usr/bin/python3
# -*- coding: utf-8 -*-

import socket
import time
import datetime

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = '127.0.0.1'
port = 9999
server_socket.bind((host, port))
server_socket.listen(5)
print('the server is waiting for connection')
while True:
    client_socket, addr = server_socket.accept()
    print("Отримано з'єднання від {}".format(addr))

    client_socket.send('Як тебе звати ?'.encode('utf-8'))
    client_answer = client_socket.recv(1024)
    print(client_answer.decode('utf-8'))
    client_socket.send((('Привіт, ' + client_answer.decode('utf-8')) + '\n').encode('utf-8'))
    while True:
        client_socket.send("Що ти хочеш мене спитати?".encode('utf-8'))
        client_answer = client_socket.recv(1024)
        response = client_answer.decode('utf-8')

        if response == 'Вихід.':
            client_socket.close()
            break

        if response == 'Котра година ?':
            client_socket.send(datetime.datetime.fromtimestamp(time.time()).strftime('Поточний година: %Y-%m-%d '
                                                                                     '%H:%M:%S\n').encode('utf-8'))
        if response == 'Скільки місяців у році?':
            client_socket.send('Рік має 12 місяців.'.encode('utf-8'))

        if response == 'Скільки днів у році?':
            client_socket.send('У році є 365 днів.'.encode('utf-8'))
    print('Клієнт відключений')
