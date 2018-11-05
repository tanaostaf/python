#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def rand(seed = 654321):
    while True:
        x = str(seed)
        if len(x) != 6:
            x = (6-len(x))*'0'+x
        d = len(x)//2  
        y = x[d:]+ x[:d]
        dobut = str(int(x)*int(y))
        if len(dobut) !=12:
            dobut = (12- len(dobut))*'0'+dobut
        STR = str(dobut)
        seed = STR[3:9]        
        yield int(seed)
func = rand()
for _ in range (15):
    print (func.__next__())


