#!/usr/bin/env python

# http://projecteuler.net/problem=2

# Each new term in the Fibonacci sequence is generated
# by adding the previous two terms. By starting with 1 and 2,
# the first 10 terms will be:
# 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

# By considering the terms in the Fibonacci sequence
# whose values do not exceed four million,
# find the sum of the even-valued terms.


def fibonacci(max):
    a, b = 0, 1
    while True:
        c = a + b
        a, b = b, c
        if c <= max:
            if not c % 2:
                yield c
        else:
            raise StopIteration

num = fibonacci(4e6)
print sum(num)
