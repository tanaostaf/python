#!/usr/bin/env python3
# -*- coding: utf-8 -*-
print ('Введіть сторони трикутника:')

a = float(input ("a : "))
b = float(input ("b : "))
c = float(input ("c : "))

if (a < b+c) or (b < a+c) or (c < a+b):
       print ('Трикутник існує')
else:
       print ('Трикутник не існує')


