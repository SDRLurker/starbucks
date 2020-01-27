#!/usr/bin/python
# -*- coding: utf-8 -*-
def is_palind(n):
    s = str(n)
    for i in range(len(s) // 2):
        if s[i] != s[-1-i]:
            return False
    return True

def get_palind_set():
    p_set = set()
    for i in range(100,1000+1):
        for j in range(100000//i+1, 1000-1):
            if is_palind(i*j):
                p_set.add(i*j)
    return p_set

def get_largest_palind(n, p_set):
    for p in range(n-1, 101101-1,-1):
        if p in p_set:
            print(p)
            return p
    print(0)
    return 0

import unittest
class test_solution(unittest.TestCase):
    def test_all(self):
        p_set = get_palind_set()
        self.assertEqual(get_largest_palind(101110,p_set), 101101)
        self.assertEqual(get_largest_palind(800000,p_set), 793397)

if __name__ == "__main__":
    unittest.main()
