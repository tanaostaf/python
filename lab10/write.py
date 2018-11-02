#!/usr/bin/env python3
try: 
	with open('test.jpg', 'rb') as file1: 
		read1=file1.read()
except FileNotFoundError: 
	print("[x] File: '"+str(test.jpg)+"' is not defined!")
	raise SystemExit
	
	
try: 
	with open('text.txt', 'rb') as file2: 
		read2=file2.read()
except FileNotFoundError: 
	print("[x] File: '"+str(text.txt)+"' is not defined!")
	raise SystemExit 
	
	
	
with open('test.jpg', 'wb') as file3: 
	file3.write(read1)
	file3.write(read2)	