#!/usr/bin/python
# -*- coding: utf-8 -*-

def ice(m, n, c):
        i = 0
        while i < n-1:
                for j in range(i+1,n):
                    if c[i] + c[j] == m:
                        return i+1, j+1
                i += 1


t = int(raw_input())
for _ in range(t):
        m = int(raw_input())
        n = int(raw_input())
        s = raw_input()
        c = [int(x) for x in s.split()]
        a,b = ice(m,n,c)
        if a > b:
                a,b = b,a
        print a,b
