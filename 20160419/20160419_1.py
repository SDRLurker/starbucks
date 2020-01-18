#!/usr/bin/python
# -*- coding: utf-8 -*-
def is_prime(n):
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

def generator_prime():
    p = 2
    while True:
        if is_prime(p):
            yield p
        p = 3 if p == 2 else p + 2
    
prime_dic = {}
def prime_seq(n):
    if n in prime_dic:
        return prime_dic[n]
    i = 0
    pp = 0
    for p in generator_prime():
        i += 1
        prime_dic[i] = p
        if i == n:
            pp = p
            break
    return p

import unittest
class test_solution(unittest.TestCase):
    def test_all(self):
        self.assertEqual(prime_seq(10000), 104729)
        self.assertEqual(prime_seq(3), 5)
        self.assertEqual(prime_seq(6), 13)


if __name__ == "__main__":
    unittest.main()

