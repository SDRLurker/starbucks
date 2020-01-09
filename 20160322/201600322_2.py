#!/usr/bin/python
# -*- coding: utf-8 -*-

def square_diff(n):
    return sum(range(1,n+1))**2 - sum(n*n for n in range(1,n+1))

import unittest
class test_solution(unittest.TestCase):
    def test_all(self):
        self.assertEqual(square_diff(3), 22)
        self.assertEqual(square_diff(10), 2640)

if __name__ == "__main__":
    unittest.main()
