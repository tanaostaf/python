#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import math
import decimal

numbers = {
  1: 'одна', 
  2: 'дві', 
  3: 'три', 
  4: 'чотири', 
  5: 'п\'ять', 
  6: 'шість', 
  7: 'сім', 
  8: 'вісім', 
  9: 'дев\'ять', 
  10: 'десять', 
  11: 'одинадцять',
  12: 'дванадцять', 
  13: 'тринадцять', 
  14: 'чотирнадцять', 
  15: 'п\'ятнадцять',
  16: 'шістнадцять', 
  17: 'сімнадцять', 
  18: 'вісімнадцять', 
  19: 'дев\'ятнадцять',
  20: 'двадцять', 
  30: 'тридцять', 
  40: 'сорок', 
  50: 'п\'ятдесят', 
  60: 'шістдесят', 
  70: 'сімдесять', 
  80: 'вісімдесять', 
  90: 'дев\'яносто', 
  100: 'сто',
  200: 'двісті', 
  300: 'триста', 
  400: 'чотириста', 
  500: 'п\'ятсот', 
  600: 'шістсот',
  700: 'сімсот', 
  800: 'вісімсот', 
  900: 'дев\'ятсот', 
  0: ''
}

def convert(amount : decimal) -> str:
  if amount > 1000000 : raise ValueError('Not supporter over million')
  
  lst = list(str(int(amount)))
  s1 = ''
  
  s2 = ''
  coins = int((amount - int(amount))*100)
  if coins == 0:
      s2 = ''
  elif coins % 10 == 1:
      s2 = str(coins) + ' копійка'
  elif coins % 10 < 5:
      s2 = str(coins) + ' копійки'
  else:
      s2 = str(coins) + ' копійок'

  lst.reverse()
  n = len(lst)
  if len(lst) >= 2:
    if lst[1] == '1':
      s1 = numbers[int(lst[1]) * 10 + int(lst[0])] + ' гривень ' + s1
      n = 2
  if n != 2:
      if int(lst[0]) == 1:
        s1 = "одна гривня " + s1
      elif int(lst[0]) < 5:
        s1 = numbers[int(lst[0])] + " гривні " + s1
      else:
        s1 = numbers[int(lst[0])] + " гривень " + s1
      n = 1

  if len(lst) < 3:
    m = len(lst)
  else:
    m = 3

  for i in range(n,m):
    s1 = numbers[int(lst[i]) * pow(10,i)] + ' ' + s1
  
  if len(lst) <= 3:
    return s1 + s2

  n = 3
  if len(lst) >= 5:
    if lst[4] == '1':
      s1 = numbers[int(lst[4]) * 10 + int(lst[3])] + ' тисяч ' + s1
      n = 5
  if n != 5:
      if int(lst[3]) == 1:
        s1 = "одна тисяча " + s1
      elif int(lst[3]) < 5:
        s1 = numbers[int(lst[3])] + " тисячі " + s1
      else:
        s1 = numbers[int(lst[3])] + " тисяч " + s1
      n = 4
 

  for i in range(n, len(lst)):
    s1 = numbers[int(lst[i]) * pow(10,i - 3)] + ' ' + s1
  
  return s1 + s2


s = decimal.Decimal(input("Enter number: "));
print(convert(s))
input ('Press ENTER to exit') 
