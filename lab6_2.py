#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math

def grosh():
    """Vvedennya danykh"""
    suma = float(input('Nayavnu sumu hroshey: '))
    rok = float(input('Vedit kilkist rokiv: '))
    proz = float(input('Richnyy bankivskyy protsent po depozytu: '))
    Cal_Sum(suma, rok, proz) 
	
def Cal_Sum(suma, rok, proz):
    """Rozrakhunok sumy po depozytu za pevnu kilkist rokiv"""
    potribsum = suma * (math.pow( (1 + (proz / 100)), rok))
    print ("Potribna Suma:  %.3f" % potribsum)
    return potribsum
 
grosh()
input ('Press ENTER to exit')
