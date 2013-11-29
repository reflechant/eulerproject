#!/usr/bin/env python

a = (x for x in xrange(1000) if not x % 3 or not x % 5)
print sum(a)
