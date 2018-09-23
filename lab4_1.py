#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import math
a = float ( input ('Введіть невідємне число а: '))
b = float ( input ('Введіть невідємне число b, b не дорівнює 0: '))
if a >= 0 and b != 0:
  	
	x1 = math.sqrt(a * b)/ (math.exp(a) * b)
	x2 = a * math.exp( 2 * a / b)
	x3 = x1 + x2
	print(" x = %.6f " % x3)
else: 
        print("Ви ввели невірні значення")
input ('Press ENTER to exit')
