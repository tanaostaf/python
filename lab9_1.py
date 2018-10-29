#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import random

kol = {'2': 2,'3': 3,'4': 4,'5': 5,'6': 6, '7': 7, '8': 8,'9': 9,'T': 10,'J': 10,'Q':10,'K':10, 'A':11 }
koloda = kol.values()
koloda = list(koloda)*4
random.shuffle(koloda)

count = 0

while True:
    choice = input('Будете брати карту? y/n\n')
    if choice == 'y':
        current = koloda.pop()
        print('Вам попалась карта з цифрою %d' %current)
        count += current
        if count > 21:
            print('Bust')
            break
        elif count == 21:
            print('Набрали 21!')
            break
        else:
            print('У вас %d балів.' %count)
    elif choice == 'n':
        print('У вас %d балів і ви закінчили гру.' %count)
        break
input ('Press ENTER to exit')
