#!/usr/bin/env python

# http://projecteuler.net/problem=4

# A palindromic number reads the same both ways.
# The largest palindrome made from the product of
# two 2-digit numbers is 9009 = 91 * 99.

# Find the largest palindrome made from the product
# of two 3-digit numbers.

def palindrome():
    palindrome = 0
    for x in xrange(100,1000):
        for y in xrange(100,1000):
            prod = x * y
            if str(prod) == str(prod)[::-1] and prod > palindrome:
                palindrome = prod
    return palindrome

print palindrome()
