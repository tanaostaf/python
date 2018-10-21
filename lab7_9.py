#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def func():
    s = str(input())
    sum1=int(s[0])+int(s[1])+int(s[2])
    sum2=int(s[3])+int(s[4])+int(s[5])
    return True if sum1==sum2 else False 

print(func())
input ('Press ENTER to exit')