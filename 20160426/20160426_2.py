#!/usr/bin/python
# -*- coding: utf-8 -*-

def equal_sub(n, a):
    if n == 1:
        return 0
    right_sum = sum(a[1:])
    left_sum = 0
    for i in range(n-1):
        left_sum += a[i]
        right_sum -= a[i+1]
        if left_sum == right_sum:
            return i+1
    return -1

t = int(raw_input())
for _ in range(t):
    n = int(raw_input())
    s = raw_input()
    a = [int(x) for x in s.split()]
    if equal_sub(n,a) >= 0:
        print "YES"
    else:
        print "NO"