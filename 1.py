#!/usr/bin/env python

a = [x for x in xrange(1000) if not x%3]
b = [x for x in xrange(1000) if not x%5]
c = a
for x in b:
	if x not in c:
		c.append(x)

print sum(c)

