#!/usr/bin/python
# -*- coding: utf-8 -*-
# Complete the squares function below.
def angryProfessor(k, a):
    return "YES" if sum(1 for b in a if b <= 0) < k else "NO"

import unittest
class test_solution(unittest.TestCase):
    def test_all(self):
        self.assertEqual(angryProfessor(3, [-1, -3, 4, 2]), "YES")
        self.assertEqual(angryProfessor(2, [0, -1, 2, 1]), "NO")

if __name__ == "__main__":
    unittest.main()

