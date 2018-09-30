#!/usr/bin/env python3
# -*- coding: utf-8 -*-
print ('Введіть сторони трикутника:')

a = float(input ("a : "))
b = float(input ("b : "))
c = float(input ("c : "))

if (a + b > c) and (a + c > b) and (b + c > a):
       print ('Трикутник існує')
else:
       print ('Трикутник не існує')
input ('Press ENTER to exit')
