#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math 

def storona():
    """Vvedennya danykh"""
    a = float(input('Vvedit storony a: '))
    b = float(input('Vvedit storony b: '))
    c = float(input('Vvedit storony c: '))
    return a, b, c
	
def suma_stor(parametru):
    """Rozrakhunok ploshchi trykutnyka"""
    a = parametru[0]
    b = parametru[1]
    c = parametru[2]
    p = (a + b + c)/2 
    s = math.sqrt(p * (p - a) * (p - b) * (p - c))
    print ('Plosha trukutnuka: ', s)
    return s	
parametru = storona()
suma_stor(parametru)
input ('Press ENTER to exit')


