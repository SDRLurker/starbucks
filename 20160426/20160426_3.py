#!/usr/bin/python
# -*- coding: utf-8 -*-
def get_dict(l):
    dict = {}
    for i in l:	
        if i in dict:
            dict[i] = dict[i] + 1
        else:
            dict[i] = 1 
    return dict

def missing(m, n):
    m_dict = get_dict(m)
    n_dict = get_dict(n)
    m_items = m_dict.items()
    n_items = n_dict.items()
    diffs = (set(m_items) | set(n_items)) - (set(m_items) & set(n_items))
    diff_set = set()
    for item in diffs:
        diff_set.add(item[0])
    return sorted(list(diff_set))

m = int(raw_input())
m_str = raw_input() 
m_arr = [int(x) for x in m_str.split()]
n = int(raw_input())
n_str = raw_input() 
n_arr = [int(x) for x in n_str.split()]
result = missing(m_arr,n_arr) 
s_arr = [str(i) for i in result]
print " ".join(s_arr)
