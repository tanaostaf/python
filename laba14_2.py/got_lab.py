#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pickle
import json
import csv

#book = {}#'Ваня': 4098, 'Коля': 4139, 'Петя': 1489

#with open('file.py','w') as file:
   # file.write("dictionary_name = { \n")
   # for k in sorted (data.keys()):
    #    file.write("'%s':'%s', \n" % (k, data[k]))
    #file.write("}")    
    
#with open('test.txt', 'a') as fo:
	#for key, value in book.items():
		#fo.writelines(str(key) + " : " + str(value) + "\n")

            
#with open ('test.txt','a', encoding = 'utf-8') as book:
   # book.write(book)
    #book.fush()

with open('test.txt', 'a') as f:
    book = {}
    f.writelines('{}:{}'.format(keys,values) for keys, values in book.items())
    f.write('\n')  
    f.flush()    

#with open('test.txt','w') as out:
    #json.dump(book,out)
 
#with open('test.txt','r') as inp:
   # d_in = json.load(inp)

#print(d_in)
    
    
e = "test"
x = 0
control = 0
while control == 0:
    a = int(input("""0 - новий контакт
1 - перегляд книги
2 - пошук по імені
3 - пошук по номеру 
4 - видалення запису
Введіть число для виконання дії:  """))
    if a == 1:
        b = book.keys()
        b = list(b)
        b.sort()
        for key in b:
            print(key +'-' +str(book[key]))
 
    elif a == 0:
        e = input("""Введіть імя: """)
        x = int(input("""Введіть номер:  """))
        book[e]= x
    elif a == 2:
        e = input("""Введіть імя:  """)
        if e in book:
            print(book[e])
        else:
            print("Контакт не існує.")
    elif a == 3:
        x = int(input("""Введіть номер: """))
        mirror = dict(zip(book.values(), book.keys()))
        if x in mirror:
            print(mirror[x])
        else:
            print("Контакт не існує.")
    elif a == 4:
        e = input("""Введіть імя: """)
        if e in book:
            del book[e]
            print("Контакт видалений!")
        else:
            print("Такого запису не існує.")
    else:
        print("ERROR")
        
        break

input ('Press ENTER to exit') 
#CSV	Файл, который хранит данные в виде таблицы; для структурирования хранимых данных используются запятые (или другие разделители).