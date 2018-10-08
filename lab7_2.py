#!/usr/bin/env python3
# -*- coding: utf-8 -*-
s = input('Vedit radok: ')
import re

def palindrom(s):
    pattern = r'\,|\s|\:|\.|\-|\_'
    s = re.sub(pattern, '', s.lower())
    return list(s) == list(reversed(s))

print(palindrom(s))


