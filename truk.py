#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math 

	
def suma_stor(a, b, c):
    """Rozrakhunok ploshchi trykutnyka"""  
    p = (a + b + c)/2 
    s = math.sqrt(p * (p - a) * (p - b) * (p - c))
    return s	

