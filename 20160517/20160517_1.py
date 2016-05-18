#!/usr/bin/python
# -*- coding: utf-8 -*-

n = int(raw_input())
sum_nums = 0
for _ in range(n):
    num = int(raw_input())
    sum_nums += num
print str(sum_nums)[:10]
