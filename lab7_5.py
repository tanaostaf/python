#!/usr/bin/env python3
# -*- coding: utf-8 -*-
slovo = input('Vedit slovo: ')
hlasni = 0
pryholosni = 0
for i in slovo:
    letter = i.lower()
    if letter == "a" or letter == "e" or\
       letter == "i" or letter == "o" or\
       letter == "u" or letter == "y":
        hlasni += 1
    else:
        pryholosni += 1
print("hlasni %i\npryholosni %i" % (hlasni, pryholosni))

input ('Press ENTER to exit')