#!/usr/bin/python
# -*- coding: utf-8 -*-

import math
def is_prime(n):
        i = 2
        while i <= int(math.sqrt(n)):
                if n % i == 0:
                        return False
                i += 1
        return True

def p_cnt(n, p):
        cnt = 0
        while n % p == 0:
                cnt += 1
                n = n // p
        return n, cnt

def get_divisor(n):
        d = {}
        n, cnt = p_cnt(n, 2)
        if cnt > 0:
                d[2] = cnt

        p = 3
        while n > 1:
                cnt = 0
                if is_prime(p):
                        n, cnt = p_cnt(n, p)
                        if cnt > 0:
                                d[p] = cnt
                p += 2
        return d

def get_divisor_size(n):
	d = get_divisor(n)
	size = 1
	for p in d:
		size *= (d[p]+1)
	return size

def get_min_divisor_triangle(n):
	t = 1
	plus = 2
	while True:
		ds = get_divisor_size(t)
		if ds > n:
			break
		t += plus
		plus += 1
	return t

t = int(raw_input())
for _ in range(t):
	n = int(raw_input())
	print get_min_divisor_triangle(n)