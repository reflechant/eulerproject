#!/usr/bin/env python

from math import sqrt

def prime(max):
    prime=[1,]              # 1 is a universal prime factor
    limit=int(sqrt(max))    # there are no prime factors beyond sqrt(max)
    x = 1           
    while x <= limit:
        for y in prime:
            if x%y:
                prime.append(x)
                break
        x = x + 1
	return prime

print prime(100)
