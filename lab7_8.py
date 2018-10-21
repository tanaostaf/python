#!/usr/bin/env python3
# -*- coding: utf-8 -*-

x = range(1, 101)

for y in x:
    if y % 3 == 0 and y % 5 == 0:
        print ("Fizz Buzz")
    elif y % 5 == 0:
        print ("Buzz")
    elif y % 3 == 0:
        print ("Fizz")
    else:
        print (y)

input ('Press ENTER to exit')