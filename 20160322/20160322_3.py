#!/usr/bin/python
# -*- coding: utf-8 -*-

def gcd(a, b):
    while b != 0:
        r = a % b
        a = b 
        b = r
    return a

def lcm(a, b):
    return a * b // gcd(a, b)
    
def small_multiple(n):
    s = 1
    for i in range(2, n+1):
        s = lcm(s, i)
    return s

import unittest
class test_solution(unittest.TestCase):
    def test_all(self):
        self.assertEqual(small_multiple(3), 6)
        self.assertEqual(small_multiple(4), 12)
        self.assertEqual(small_multiple(5), 60)
        self.assertEqual(small_multiple(6), 60)
        self.assertEqual(small_multiple(7), 420)
        self.assertEqual(small_multiple(8), 840)
        self.assertEqual(small_multiple(9), 2520)
        self.assertEqual(small_multiple(10), 2520)
        self.assertEqual(small_multiple(20), 232792560)

if __name__ == "__main__":
    unittest.main()
