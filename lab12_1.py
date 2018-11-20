#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import math #Підключаємо математичну бібліотеку
class Point:
    
    def __init__(self, initX, initY):

        self.x = initX
        self.y = initY

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def distance(self,point2): #Функція  яка повертає відстань між 2 точками 
        xdiff = point2.getX()- self.getX() #х2-х1
        ydiff = point2.getY()- self.getY() #y2-y1
        dist = math.sqrt(xdiff**2 + ydiff**2) # відстань між двома точками 
        return dist #Повертаємо знайдене значення
		
print ('vvedit koordynaty tochky A: ' ) #ввести координати 1-ої точки
x1 = int(input ())  #Вводимо координату по х
y1 = int(input ())  # Вводимо координату по y

print ('vvedit koordynaty tochky B: ')
x2 = int(input ())
y2 = int(input ())

print ('vvedit koordynaty tochky C: ')
x3 = int(input ())
y3 = int(input ())

A = Point(x1,y1)
B = Point(x2,y2)
C = Point(x3,y3)

class trykutnyk:
    def __init__(self,A,B,C):
        self.A = A
        self.B = B
        self.C = C
    AB = A.distance(B)
    BC = B.distance(C)
    CA = C.distance(A)
    print('AB = ',AB)
    print ('BC = ',BC)
    print ('CA = ',CA)
    def triangle_check(self): #функція на перевірку чи існує трикутник
        result = None
        if (self.AB + self.BC > self.CA) and (self.AB + self.CA > self.BC) and (self.CA + self.BC > self.AB):
           result = True
        else:
           result = False 
        return result
    def ploshcha(self): # функція обчислення площі трикутника 
        perym = self.AB + self.BC + self.CA # знаходимо периметр трикутника 
        print ('Perymetr: ',perym)
        piv_perym=(perym)/2 #Знаходимо півпериметр 
        s = math.sqrt(piv_perym * (piv_perym - self.AB) * (piv_perym - self.BC) * (piv_perym - self.CA)) # обчислення площі 
        return s #Повертаємо площу трикутника 
tryk = trykutnyk(A, B, C)
print("Chy isnuie trykutnyk: ",tryk.triangle_check())
print("Ploshcha : {}".format(tryk.ploshcha())) 

input ('Press ENTER to exit')
