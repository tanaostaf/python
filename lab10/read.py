#!/usr/bin/env python3
# -*- coding: utf-8 -*-

with open("test.jpg", "rb") as r: 
		byte = r.read(1)
		k=0
		while byte: 
			k+=1
			print(byte)
			byte = r.read(1)