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
		
print ('vvedit koordunatu tochku A: ' ) #ввести координати 1-ої точки
x1 = int(input ())  #Вводимо координату по х
y1 = int(input ())  # Вводимо координату по y

print ('vvedit koordunatu tochku B: ')
x2 = int(input ())
y2 = int(input ())

print ('vvedit koordunatu tochku C: ')
x3 = int(input ())
y3 = int(input ())

A = Point(x1,y1)
B = Point(x2,y2)
C = Point(x3,y3)
AB = A.distance(B)
AC = A.distance(C)
BC = B.distance(C)
print('AB = ',AB)
print ('AC = ',AC)
print ('BC = ',BC)

class trykutnyk:
    def __init__(self,AB,AC,BC):
        self.AB = float(AB)
        self.AC = float(AC)
        self.BC = float(BC)
    def perevirka_chy_isnuye(self): #функція на перевірку чи існує трикутник 
        if (self.AB + self.AC > self.BC) and (self.AB + self.BC > self.AC) and (self.AC + self.BC > self.AB):
           return True
        else:
           return False 
    def ploshcha(self): # функція обчислення площі трикутника 
        perym = self.AB + self.AC + self.BC # знаходимо периметр трикутника 
        print ('perymetr: ',perym)
        piv_perym=(perym)/2 #Знаходимо півпериметр 
        s = math.sqrt(piv_perym * (piv_perym - self.AB) * (piv_perym - self.AC) * (piv_perym - self.BC)) # обчислення площі 
        return s #Повертаємо площу трикутника 

tryk = trykutnyk(AB, AC, BC)
print("Chy isnuye trykutnyk: ",tryk.perevirka_chy_isnuye())
print("ploshcha : {}".format(tryk.ploshcha())) 

input ('Press ENTER to exit')