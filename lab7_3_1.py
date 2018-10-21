#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def checkio(expression):
    s = ''.join(c for c in expression if c in '([{<>}])')
    while s:
        s0, s = s, s.replace('()', '').replace('[]', '').replace('{}', '').replace('<>','')
        if s == s0:
            return False
    return True

print (checkio('(((a * x) + [b] * y) + c '))
print (checkio('auf(zlo)men [gy<psy>] four{s}  '))
input ('Press ENTER to exit')


