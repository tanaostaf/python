#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from abc import ABCMeta, abstractmethod

class Worker: #Клас робітник 
    __metaclass__ = ABCMeta
 
    def __init__(self, id, rate, name):
        self.id = id
        self.rate = rate
        self.name = name
        
 # абстрактный метод, який буде необхідно перевизначати для кожного підкласу
    @abstractmethod  
    def calc_av_wage(self): #Метод розрахунку зарплати, Абстрактный метод
        pass  
    @abstractmethod 
    def calc_tax(self): #метод розрахунку податку 
        pass 

# Клас робітник з погодинною оплатою
class Worker_Hourly(Worker):
 
    def calc_av_wage(self):
        wage = 20.8 * 8 * self.rate #розрахунок зарплати
        return wage #повертає значення зарплати         
    def calc_tax(self, wage):
        pdfo = wage * 0.18 #ПДФО    
        militar_duty = wage * 0.015 #військовий збір 
        
        total_tax_amount = pdfo + militar_duty # Сумарна сума податку 
        return total_tax_amount #Сумарна сума податку

#Клас робітник з фіксованою ставкою 
class Worker_Fixed(Worker):
 
    def calc_av_wage(self):
        wage = self.rate  #зарплата
        return wage  #повертає значення зарплати 
    def calc_tax(self,wage):
        pdfo = wage * 0.18 #ПДФО    
        militar_duty = wage * 0.015 #військовий збір 
      
        total_tax_amount = pdfo + militar_duty # Сумарна сума податку 
        return total_tax_amount #Сумарна сума податку        
        
# Клас робітник  погодинник оформлений як ФОП 
class Worker_Hourly_FOP(Worker):
 
    def calc_av_wage(self):
        wage_hourly = 20.8 * 8 * self.rate #розрахунок зарплати
        wage = (wage_hourly * 0.10) + wage_hourly
        return wage #повертає значення зарплати         
    def calc_tax(self, wage):
        single_tax = wage * 0.05 #єдиний податок 
    
        ECV = 704
        wage_without_ECV = wage - ECV #Зарплата без ЄСВ 
    
        total_tax_amount = single_tax + ECV # Сумарна сума податку 
        return total_tax_amount #Сумарна сума податку

#самозайнята особа яка працює за цівільно-правовим договором 
class Worker_Selfemployed(Worker):
    def calc_av_wage(self):
        price_line = 3.20 #ціна рядка 
        wage = self.rate * price_line #розрахунок зарплати        
        return wage #повертає значення зарплати         
    def calc_tax(self, wage):
        pdfo = wage * 0.18 #ПДФО
        militar_duty = wage * 0.015 #військовий збір 
        
        ECV = 704
        wage_without_ECV = wage - ECV #Зарплата без ЄСВ 
         
        total_tax_amount = pdfo + militar_duty + ECV # Сумарна сума податку 
        return total_tax_amount  #Сумарна сума податку  
       
      

# Створення екземпляра класа 
workers = [Worker_Hourly(1, 210, 'Tanya'), Worker_Hourly_FOP (6, 140, 'Basil'),
           Worker_Hourly(2, 210, 'Andriy'), Worker_Selfemployed(7, 50000, 'Peter'),
           Worker_Fixed(3, 4000, 'Iryna'), Worker_Selfemployed(8, 20000, 'Andriy'),
           Worker_Fixed(4, 5300, 'Rostislav'), Worker_Hourly_FOP (9, 190, 'Natalya'),
           Worker_Selfemployed(5, 80000, 'Dmytro'), Worker_Fixed(10, 4100, 'Volodymyr')]

# Доступ до методів класу 
#print(workers.calc_av_wage()) 
#print(workers.calc_tax(workers.calc_av_wage()) )
 
 
#сортуємо по двом полях - по зп на зменшення і по імені на збільшення        
workers.sort(key=lambda x: (-x.calc_av_wage(), x.name)) 
print ('Працівники (ідентифікаційний, імя працівника, зарплата, сумарна сума податку): \n', [(x.id, x.name, x.calc_av_wage(), x.calc_tax(x.calc_av_wage())) for x in workers])


input ('Press ENTER to exit') 