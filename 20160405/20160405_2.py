#!/usr/bin/python
# -*- coding: utf-8 -*-
# Complete the caesarCipher function below.
def twoStrings(s1, s2):
    c1_dic = {}
    c2_dic = {}
    for c in s1:
        c1_dic[c] = c1_dic.get(c,0) + 1
    for c in s2:
        c2_dic[c] = c2_dic.get(c,0) + 1
    for c in c1_dic:
        if c in c2_dic:
            return "YES"
    return "NO"


import unittest
class test_solution(unittest.TestCase):
    def test_all(self):
        self.assertEqual(twoStrings("hello", "world"), "YES")
        self.assertEqual(twoStrings("hi", "world"), "NO")
        s1 = "wouldyoulikefries"
        s2 = "abcabcabcabcabcabc"
        self.assertEqual(twoStrings(s1, s2), "NO") 
        s1 = "hackerrankcommunity"
        s2 = "cdecdecdecde"
        self.assertEqual(twoStrings(s1, s2), "YES") 
        s1 = "jackandjill"
        s2 = "wentupthehill"
        self.assertEqual(twoStrings(s1, s2), "YES") 
        s1 = "writetoyourparents"
        s2 = "fghmqzldbc"
        self.assertEqual(twoStrings(s1, s2), "NO") 
        self.assertEqual(twoStrings("aardvark", "apple"), "YES")
        self.assertEqual(twoStrings("beetroot", "sandals"), "NO")

if __name__ == "__main__":
    unittest.main()

