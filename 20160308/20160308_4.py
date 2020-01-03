#!/usr/bin/python
# -*- coding: utf-8 -*-
# Complete the utopianTree function below.
def utopianTree(n):
    h = 1
    for i in range(n):
        h = h * 2 if i % 2 == 0 else h + 1
    return h

import unittest
class test_solution(unittest.TestCase):
    def test_all(self):
        self.assertEqual(utopianTree(0), 1)
        self.assertEqual(utopianTree(1), 2)
        self.assertEqual(utopianTree(2), 3)
        self.assertEqual(utopianTree(3), 6)
        self.assertEqual(utopianTree(4), 7)

if __name__ == "__main__":
    unittest.main()

