#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import math
print ('Коефіцієнти рівняння')

a = float(input ("a : "))
b = float(input ("b : "))
c = float(input ("c : "))

D = (b**2)-4*a*c
print ('Дискримінант: ',D)
if D < 0:
     d  = abs(D)	 
     x1 = complex((-b/(2*a)),(math.sqrt(d)/(2*a)))
     x2 = complex((-b/(2*a)),(-(math.sqrt(d)/(2*a))))
     print(x1)
     print(x2)	 
elif D == 0:
     x1 = -b/(2*a)
     print ('Корені рівняння: ',x1)
elif a == 0:
     x1 = (-b)/c
     print(x1)
elif b == 0:
     x1 = math.sqrt(-c/a)
     x2 = -(math.sqrt(-c/a))
     print(x1)
     print(x2)
elif c == 0:
     x1 = 0
     x2 = -b/a
     print(x1)
     print(x2)
elif b == 0 or c == 0:
     x1 = 0
     x2 = 0
     print(x1)
     print(x2)
else:
     x1 = (-b+math.sqrt(D))/(2*a)
     x2 = (-b-math.sqrt(D))/(2*a) 
     print(x1)
     print(x2)

input ('Press ENTER to exit')

