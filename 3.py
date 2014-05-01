#!/usr/bin/env python


def prime(max):
    prime = [1, ]            # 1 is universal prime factor
    x = 2
    while x <= max:
        if not max % x:       # if max is divisible by x
            prime.append(x)   # save x as one of max' prime factors
        while not max % x:    # prevent adding x^2 and x^3 to prime
            max = max / x

        x = x + 1

    return prime
print prime(600851475143)
