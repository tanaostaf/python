#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import math 

def grosh():
    """Vvedennya danykh"""
    nsuma = float(input('Nayavnu sumu hroshey: '))
    potribsuma = float(input('Vedit potribnu sumu: '))
    proz = float(input('Richnyy bankivskyy protsent po depozytu: '))
    Cal_Rokiv(nsuma, potribsuma, proz)
	
def Cal_Rokiv(nsuma, potribsuma, proz):
    """Funktsiya povertaye kilkist rokiv"""
    roku = math.log10(potribsuma / nsuma) / math.log10(1 + (proz / 100))
    print ("Kilkist rokiv: %.3f " % roku)
    return roku
 
grosh()
input ('Press ENTER to exit')




   

