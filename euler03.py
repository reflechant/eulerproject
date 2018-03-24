#!/usr/bin/env python3

# http://projecteuler.net/problem=3

# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?

def primes():
    primes = set((2,))
    
        

def prime_factors(N):
    factors = set()
    x = 2
    while N > 1:
        if N % x == 0:  # if N is divisible by x
            factors.add(x)  # save x as one of N's prime factors
        while N % x == 0:  # prevent adding x^2 and x^3 to factors
            N = N // x

        x = x + 1

    return factors


print(prime_factors(600851475143))
