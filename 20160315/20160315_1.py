#!/usr/bin/python
# -*- coding: utf-8 -*-
# Complete the squares function below.
def squares(a, b):
    s = int(a ** 0.5)
    e = int(b ** 0.5)
    cnt = 0
    for i in range(s, e+1):
        if a <= i**2 <= b:
            cnt +=1
    return cnt

import unittest
class test_solution(unittest.TestCase):
    def test_all(self):
        self.assertEqual(squares(3,9), 2)
        self.assertEqual(squares(17,24), 0)
        self.assertEqual(squares(35,70), 3)
        self.assertEqual(squares(100,1000), 22)

if __name__ == "__main__":
    unittest.main()

