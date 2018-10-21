#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import re

def convert1(name):
    s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', name)
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1).lower()
def convert2(snake_str):
    components = snake_str.split('_')
    return components[0] + ''.join(x.title() for x in components[1:])
print (convert1('resSquare ** 2 for resSquare in inputArray if resSquare > 18'))
print (convert2('res_square ** 2 for res_square in input_array if res_square > 18 '))
input ('Press ENTER to exit')