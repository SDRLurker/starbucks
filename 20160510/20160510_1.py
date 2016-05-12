#!/usr/bin/python
# -*- coding: utf-8 -*-

def get_sums(n):
    primes = range(n+1)
    primes[1] = 0
    import math
    s = 2
    while 2 * s <= n:
        primes[2 * s] = 0
        s += 1
    base = 3
    while base <= int(math.sqrt(n)):
        s = base
        while base * s <= n:
            primes[base * s] = 0
            s += 2
        base += 2
    i = 1
    while i <= n:
        primes[i] = primes[i-1] + primes[i]
        i += 1
    return primes    

sums = get_sums(1000000)

def sum_primes(n):
    return sums[n]

t = int(raw_input())
for _ in range(t):
    n = int(raw_input())
    print sum_primes(n)