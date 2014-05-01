#!/usr/bin/env python

# http://projecteuler.net/problem=3

# The prime factors of 13195 are 5, 7, 13 and 29.

# What is the largest prime factor of the number 600851475143 ?


def prime_factors(num):
    prime = [1, ]               # 1 is universal prime factor
    x = 2
    while num > 1:
        if not num % x:         # if num is divisible by x
            prime.append(x)     # save x as one of num' prime factors
        while not num % x:      # prevent adding x^2 and x^3 to prime
            num = num / x       # divide num by it's prime factors

        x = x + 1

    return prime

print prime_factors(600851475143)
