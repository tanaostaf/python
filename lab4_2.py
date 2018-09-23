#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import math
print ("Введіть три дійсних числа: ")
a = float ( input('a = '))
b = float ( input('b = '))
c = float ( input('c = '))
x1 = 1 / (c * math.sqrt(2 * math.pi))
x2 = math.exp(- (math.pow((a-b),2)/2* math.pow(c,2))) 
x3 = x1 * x2
print("x = %.6f " % x3)
input ('Press ENTER to exit')