#!/usr/bin/env python

def prime(max):
    prime=[2,]
    for x in xrange(3,max+1):
        for y in prime:
            if x%y:
                prime.append(x)
                #break
	return prime

print prime(100)
