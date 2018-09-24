#!/usr/bin/env python3
# -*- coding: utf-8 -*-

print ('Коефіцієнти рівняння')

a = float ( input ("a : "))
b = float ( input ("b : "))
c = float ( input ("c : "))
import math

D = (b**2)-4*a*c
print ('Дискримінант: ',D)
if D < 0:
     print ('Коренів немає!')
elif D == 0:
     x = -b/(2*a)
     print ('Корені рівняння: ',x1)
else:
     x1 = (-b+math.sqrt(D))/(2*a)
     x2 = (-b-math.sqrt(D))/(2*a) 
     print(x1)
     print(x2)

