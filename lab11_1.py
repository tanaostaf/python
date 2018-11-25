#!/usr/bin/env python3
# -*- coding: utf-8 -*-
www = open("nginx.txt")
i=0
sum = 0
for line in www:
    bytecolumn = line.rsplit(" ")
    i+=int(bytecolumn[9]) 
    sum+=int(bytecolumn[9])
    print (bytecolumn[9])
print ("Suma bytes: ",sum)    

bytes = (int(i)) 
#print ("Vsogo", bytes)
input ('Press ENTER to exit')

