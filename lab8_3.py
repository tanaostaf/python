#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def median(lst): 
    sortedLst = sorted(lst) 
    lstLen = len(lst)
    SeredZnach = sum(lst)//lstLen	
    print ('Serednye znachennya: ',SeredZnach)
    index = (lstLen - 1) // 2 

    if (lstLen % 2): 
     return sortedLst[index] 
    else: 
     return (sortedLst[index] + sortedLst[index + 1])/2.0 
a = [1,2,3,4,9,5,7,10,15]
print (a)
print ("Mediana: ",median(a))

input ('Press ENTER to exit')
