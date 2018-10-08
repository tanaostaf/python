#!/usr/bin/env python3
# -*- coding: utf-8 -*-

s = input('Vedit radok: ')
len(s)
k = int(input('Vedit chyslo:'))
if k > 0:
 print (s[k:]+ s[0:k])
elif k < 0:
   d = len(s) + k 
   print (s[d:]+ s[:d])




