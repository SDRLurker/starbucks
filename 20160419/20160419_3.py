#!/usr/bin/python
# -*- coding: utf-8 -*-
def max_triangle(n):
	max_product = -1
	for a in range(3, n//3):
		b = ( n * (n - 2*a) ) / ( 2 * (n - a) )
		if ( n * (n - 2*a) ) % ( 2 * (n - a) ) == 0:
			c = n - a - b
			if a * b * c > max_product:
				max_product = a * b * c
	return max_product

import unittest
class test_solution(unittest.TestCase):
    def test_all(self):
        self.assertEqual(max_triangle(12), 60)
        self.assertEqual(max_triangle(4), -1)

if __name__ == "__main__":
    unittest.main()

