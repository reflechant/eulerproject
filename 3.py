#!/usr/bin/env python

from math import sqrt

def prime(max):
    prime=[2,]
    for x in xrange( 3, int(sqrt(max)) ):
        for y in prime:
            if x%y:
                prime.append(x)
                break
	return prime

print prime(100)
