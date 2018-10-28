#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def change():
    dict1 = {"A":".-","B":"-...","C":"-.-.","D":"-..","E":".","F":"..-.","G":"--.","H":"....","I":"..","J":"-.-.","K":"-.-","L":".-..","M":"--",
          "N":"-.","O":"---","P":".--.","Q":"--.-","R":".-.","S":"...","T":"-","U":"..-","V":"...-","W":".--","X":".-..","Y":"-.--","Z":"--.."} 
    crypt = ""
    text = input(" Vvedit tekst\n[text]>>>")
    for i in text:
        b = i.upper()
        for j in dict1:
            if b == " ":
                crypt += " "
            elif b == j:
                crypt += str(dict1.get(b))
    print("Crypt text:\n" + str(crypt))
change()

input ('Press ENTER to exit')