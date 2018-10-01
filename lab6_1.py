#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math

a = float(input('Vedit storony a: '))
b = float(input('Vedit storony b: '))
c = float(input('Vedit storony c: '))

def ploshcha():
    """Ploshcha trykutnyka"""
    global a
    global b
    global c
    p = ((a + b + c) / 2)
    s = math.sqrt(p * (p - a) * (p - b) * (p - c))
    print ('Ploshcha trykutnyka: ', s)
    return s

ploshcha ()
