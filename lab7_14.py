#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re

def email_check():
    email = input('Enter your e-mail: ')
    check = re.search(r'[\w.-]+@[\w.-]+', email)
    result = bool(check)
    if check:
     result = True
     print (result)
    else:
     result = False
     print (result)
    return

email_check()		
input ('Press ENTER to exit')	