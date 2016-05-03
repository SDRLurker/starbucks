#!/usr/bin/python
# -*- coding: utf-8 -*-

def equal_sub(n, a):
    for i in range(n):
        if sum(a[:i]) == sum(a[i+1:]):
            return i
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