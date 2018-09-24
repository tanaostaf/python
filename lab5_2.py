#!/usr/bin/env python3
# -*- coding: utf-8 -*-

h = float(input('Введіть висоту дверей: '))
w = float(input('Введіть ширину дверей: '))

a = float(input('Введіть висоту коробки: '))
b = float(input('Введіть ширину коробки: '))
c = float(input('Введіть довжину коробки: '))

if (a <= h or a <= w) and (b <= h or b <= w):
 print('Ви можете помістити коробку через двері.')
elif  (a <= h or a <= w) and (c <= h or c <= w):
 print('Ви можете помістити коробку через двері.')
elif  (b <= h or b <= w) and (c <= h or c <= w):
 print('Ви можете помістити коробку через двері.')
else:
 print('Ви не можете помістити коробку через двері.')
