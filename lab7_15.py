#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random
num = input('login: ')
pas = ''
for x in range(2): #кількість символів з одного random
    chuslo = random.choice(list('1234567890'))
    bukva_mal = random.choice(list('abcdefghigklmnopqrstuvyxwz'))
    bukva_V = random.choice(list('ABCDEFGHIGKLMNOPQRSTUVYXWZ'))
    symbol = random.choice(list('~!@#$%^&*()_+`-={}[]:;<>./'))
    pas = pas + chuslo + bukva_mal + bukva_V + symbol #Пароль 
print('Pruvit, ', num, 'vash parol ye: ', pas)

input ('Press ENTER to exit')	

