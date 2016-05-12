#!/usr/bin/python
# -*- coding: utf-8 -*-

def sum_primes(n):
    primes = range(n+1)	# [0,1,2,...,n]인 리스트 생성
    primes[1] = 0	# 1은 소수가 아니라 0 대임
    import math		# 에라스토스의 채를 이용하여 소수가 아닌 값에 0 대입
    for base in range(2,int(math.sqrt(n))+1):
        s = 2
        while base * s <= n:
            primes[base * s] = 0
            s += 1
    return sum(primes)

t = int(raw_input())
for _ in range(t):
    n = int(raw_input())
    print sum_primes(n)