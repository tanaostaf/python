#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import re

str = input('Vedit radok: ')

print (re.sub(r'\s+', ' ', str)) 

input ('Press ENTER to exit')