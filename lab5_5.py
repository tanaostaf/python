#!/usr/bin/env python3
# -*- coding: utf-8 -*-
n = int(input(" Введіть ціле число: "))
prime = True
i = 2
while i <= n-1:
 if (n % i) == 0:
     prime = False
 i = i + 1
 if prime :
  print ('Число', n,'є просте.')
 else:
  print ('Число', n,'не є просте.')
input ('Press ENTER to exit')






