#!/usr/bin/env python

def fibonacci(max):
	a,b=0,1
	while True:
		c=a+b
		a,b=b,c
		if c<=max:
			if not c%2:
				yield c
		else: raise StopIteration

num = fibonacci(4e6)
print sum(num)
