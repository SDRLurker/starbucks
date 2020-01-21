#!/usr/bin/python
# -*- coding: utf-8 -*-
# Complete the squares function below.
def chocolateFeast(n, c, m):
    cnt = n // c
    w = cnt
    while w >= m:
        nc = w // m
        w -= nc * m
        w += nc
        cnt += nc
    return cnt

import unittest
class test_solution(unittest.TestCase):
    def test_all(self):
        self.assertEqual(chocolateFeast(10, 2, 5), 6)
        self.assertEqual(chocolateFeast(12, 4, 4), 3)
        self.assertEqual(chocolateFeast( 6, 2, 2), 5)
        self.assertEqual(chocolateFeast( 7, 3, 2), 3)
        self.assertEqual(chocolateFeast(16809, 123, 11668), 136)
        self.assertEqual(chocolateFeast(2339, 4, 1337), 584)

if __name__ == "__main__":
    unittest.main()
