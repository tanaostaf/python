#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import random

print("1")
print("2")
print("3")
ab = int(input("Введіть свій вибір: "))

ac = random.randrange(1, 3)
print("Вибір компютера: ", ac)

if(ab == 1 and ac == 2) or (ab == 2 and ac == 3) or (ab == 3 and ac == 1):
  print(" Ви виграєте)")
elif (ac == 1 and ab == 2) or (ac == 2 and ab == 3) or (ac == 3 and ab == 1):
  print(" Компютер виграє")
elif ac == ab:
  print(" Нічия ")
else:
  print("Ви зробили щось неправильно. Спробуйте ще раз!)")



