#!/usr/bin/python
# -*- coding: utf-8 -*-
# Complete the caesarCipher function below.
def gameOfThrones(s):
    cnt_dic = {}
    for c in s:
        cnt_dic[c] = cnt_dic.get(c,0) + 1
    odd_cnt = 0
    for c in cnt_dic:
        if cnt_dic[c] % 2 == 1:
            odd_cnt +=1
    return "NO" if odd_cnt > 2 else "YES"


import unittest
class test_solution(unittest.TestCase):
    def test_all(self):
        self.assertEqual(gameOfThrones("aaabbbb"), "YES")
        self.assertEqual(gameOfThrones("cdefghmnopqrstuvw"), "NO")
        self.assertEqual(gameOfThrones("cdcdcdcdeeeef"), "YES")

if __name__ == "__main__":
    unittest.main()

