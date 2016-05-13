#!/usr/bin/python
# -*- coding: utf-8 -*-
# 참고주소 : http://stackoverflow.com/questions/18281956/java-code-for-project-euler-12

import math
def get_divisor_size(n):
	size = 0
	i = 1
	while i * i <= n:
		if n % i == 0:
			size += 2
		i += 1
	sqrt = int(math.sqrt(n))
	if sqrt * sqrt == n:
		size -= 1
	return size

# seq와 seq+1이 서로소인 성질을 이용함.
def get_min_divisor_triangle(n):
	seq = 1
	while True:
		if seq % 2 == 0:
			ds1 = get_divisor_size(seq // 2)
			ds2 = get_divisor_size(seq+1)
		else:
			ds1 = get_divisor_size(seq)
			ds2 = get_divisor_size((seq+1) // 2)		
		if ds1 * ds2 > n:
			t = (seq * (seq+1)) // 2		
			break
		seq += 1
	return t

t = int(raw_input())
for _ in range(t):
	n = int(raw_input())
	print get_min_divisor_triangle(n)