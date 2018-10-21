#!/usr/bin/env python3
# -*- coding: utf-8 -*-

s = input()
l = s.split()
ln = len(l)
for i in range(ln-1):
    for j in range(ln-1-i):
        if len(l[j]) > len(l[j+1]):
            l[j],l[j+1] = l[j+1],l[j]
 
s = ''
for i in range(ln):
    s += l[i] + ' '
print(s)

input ('Press ENTER to exit')