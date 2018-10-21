#!/usr/bin/env python3
# -*- coding: utf-8 -*-
 
llst = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
blst = ['A','B','C','D','E','F','G','H','I','G','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
 
 
def encryptCaesar(msg, shift=1):
    ret = ""
    for x in msg:
        if x in llst:
            ind = llst.index(x)
            ret += llst[ind+shift]
        elif x in blst:
            ind = blst.index(x)
            ret += blst[ind+shift]
        else:
            ret += x
    return ret
 
 
print(encryptCaesar("vasia"))
input ('Press ENTER to exit')