#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def kill1(k):
    p = [1,2,3,4,5,6,7,8,9,10]
    i = 0
    seq = []
	
    while p:
        i = (i + k - 1) % len(p)
        seq.append(p.pop(i))
    return 'Killing order: %s.\nSurvivor: %i\n' % (', '.join(str(i) for i in seq[:-1]), seq[-1])
print(kill1(3))
input ('Press ENTER to exit')	

