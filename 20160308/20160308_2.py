﻿#!/usr/bin/python
# -*- coding: utf-8 -*-
# Complete the decentNumber function below.
def decentNumber(n):
    three = 0
    five = 0
    while n > 0:
        for i in range(n//3+1,0,-1):
            if n >= 3 and (n-(3*i))%5 == 0:
                three += i
                n -= 3*i
                break
        for i in range(1,n//5+1):
            if n >= 5 and (n-(5*i))%3 == 0:
                five += i
                n -= 5*i
                break
        if n%5 != 0 and n%3 != 0:
            three = five = 0
            break
    r = "-1" if three == 0 and five == 0 else ('5'* (3*three)) + ('3'*(5*five))
    print(r)
    return r
    

import unittest
class test_solution(unittest.TestCase):
    def test_all(self):
        for i in range(10,2194+1):
            self.assertEqual(len(decentNumber(i)), i)
        self.assertEqual(decentNumber(1),  "-1")
        self.assertEqual(decentNumber(2),  "-1")
        self.assertEqual(decentNumber(3),  "555")
        self.assertEqual(decentNumber(4),  "-1")
        self.assertEqual(decentNumber(5),  "33333")
        self.assertEqual(decentNumber(6),  "555555")
        self.assertEqual(decentNumber(7),  "-1")
        self.assertEqual(decentNumber(8),  "55533333")
        self.assertEqual(decentNumber(9),  "555555555")
        self.assertEqual(decentNumber(10), "3333333333")
        self.assertEqual(decentNumber(11), "55555533333")
        self.assertEqual(decentNumber(12), "555555555555")
        self.assertEqual(decentNumber(13), "5553333333333")
        self.assertEqual(decentNumber(14), "55555555533333")
        self.assertEqual(decentNumber(15), "555555555555555")
        self.assertEqual(decentNumber(16), "5555553333333333")
        self.assertEqual(decentNumber(17), "55555555555533333")
        self.assertEqual(decentNumber(18), "555555555555555555")
        self.assertEqual(decentNumber(19), "5555555553333333333")
        self.assertEqual(decentNumber(20), "55555555555555533333")
        #self.assertEqual(decentNumber(20), "33333333333333333333")
        self.assertEqual(decentNumber(21), "555555555555555555555")
        self.assertEqual(decentNumber(22), "5555555555553333333333")
        o = """5555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555553333333333"""
        self.assertEqual(decentNumber(2194), o)

if __name__ == "__main__":
    unittest.main()

