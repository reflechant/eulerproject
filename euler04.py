#!/usr/bin/env python3

# http://projecteuler.net/problem=4

# A palindromic number reads the same both ways.
# The largest palindrome made from the product of
# two 2-digit numbers is 9009 = 91 * 99.

# Find the largest palindrome made from the product
# of two 3-digit numbers.


def palindromes():
    for x in range(100, 1000):
        for y in range(100, 1000):
            prod = x * y
            if str(prod) == str(prod)[::-1]:
                yield prod


print(max(palindromes()))
