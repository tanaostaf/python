#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from decimal import Decimal 
zz = input("Введіть свій місячний дохід: ") 
Zarplata = Decimal(zz) 
Podatok = Zarplata * Decimal('0.18')
ViyskovyyZbir = Zarplata * Decimal('0.015')
SumaPoditku = Podatok + ViyskovyyZbir
print("Податок на доходи : ", Podatok)
print("Військовий збір : ", ViyskovyyZbir)
print("Сума податку : ", SumaPoditku)
input ('Press ENTER to exit')






