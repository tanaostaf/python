#!/usr/bin/env python3
# -*- coding: utf-8 -*-
zrist = float(input('Введіть зріст, в м : '))
vaga = float (input ('Введіть вагу, в кг: '))
BodyMassIndex = float( vaga / (zrist ** 2))
print('Індекс маси тіла: ',BodyMassIndex)
