#!/usr/bin/env python3
# -*- coding: utf-8 -*-
s = input()
w = 0
min_w = len(s)
for i in s:
	if 'a'<=i<='z' or 'A'<=i<='Z' \
	or 'а'<=i<='я' or 'А'<=i<='Я':
		w += 1
	else:
		if w < min_w and w != 0:
			min_w = w
		w = 0
 
print(min_w)
input ('Press ENTER to exit')
