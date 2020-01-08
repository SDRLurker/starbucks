#!/usr/bin/python
# -*- coding: utf-8 -*-
# Complete the caesarCipher function below.
def caesarCipher(s, k):
    es = ""
    for c in s:
        n = ord(c)
        if c.isupper():
            n = (ord(c)-ord('A')+k)%26+ord('A')
        elif c.islower():
            n = (ord(c)-ord('a')+k)%26+ord('a')
        es += chr(n)
    return es



import unittest
class test_solution(unittest.TestCase):
    def test_all(self):
        self.assertEqual(caesarCipher("middle-Outz",2), "okffng-Qwvb")
        i = "Always-Look-on-the-Bright-Side-of-Life"
        o = "Fqbfdx-Qttp-ts-ymj-Gwnlmy-Xnij-tk-Qnkj"
        self.assertEqual(caesarCipher(i,5), o)

if __name__ == "__main__":
    unittest.main()

