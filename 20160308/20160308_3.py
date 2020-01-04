#!/usr/bin/python
# -*- coding: utf-8 -*-
# Complete the squares function below.
def findDigits(n):
    cnt = 0
    origin = n
    while n > 0:
        d = n % 10
        if d > 0 and origin % d == 0:
            cnt += 1
        n //= 10
    return cnt

import unittest
class test_solution(unittest.TestCase):
    def test_all(self):
        self.assertEqual(findDigits(12),2)
        self.assertEqual(findDigits(1012),3)
        self.assertEqual(findDigits(123456789),3)
        self.assertEqual(findDigits(114108089),3)
        self.assertEqual(findDigits(110110015),6)
        self.assertEqual(findDigits(121),2)
        self.assertEqual(findDigits(33),2)
        self.assertEqual(findDigits(44),2)
        self.assertEqual(findDigits(55),2)
        self.assertEqual(findDigits(66),2)
        self.assertEqual(findDigits(77),2)
        self.assertEqual(findDigits(88),2)
        self.assertEqual(findDigits(106108048),5)

if __name__ == "__main__":
    unittest.main()

