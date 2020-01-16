#!/usr/bin/python
# -*- coding: utf-8 -*-
def max_product(num, k):
    m = -1
    for i in range(len(num)-k):
        p = 1
        for kk in range(k):
            p *= int(num[i+kk])
        m = max(m, p)
    return m

import unittest
class test_solution(unittest.TestCase):
    def test_all(self):
        self.assertEqual(max_product("3675356291", 5), 3150)
        self.assertEqual(max_product("2709360626", 5), 0)

if __name__ == "__main__":
    unittest.main()

