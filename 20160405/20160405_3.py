#!/usr/bin/python
# -*- coding: utf-8 -*-

def get_cnt(s):
    cnt = [0 for _ in range(26)]
    for c in s:
        cnt[ord(c)-ord('a')] += 1
    return tuple(cnt)

# Complete the sherlockAndAnagrams function below.
def sherlockAndAnagrams(s):
    pairs = 0
    sigs = {}
    for li in range(1, len(s)):
        for i in range(len(s)-li+1):
            cnt = get_cnt(s[i:i+li])
            sigs[cnt] = sigs.get(cnt, 0) + 1
    for cnt in sigs.values():
        pairs += cnt * (cnt-1) // 2
    return pairs

import unittest
class test_solution(unittest.TestCase):
    def test_all(self):
        self.assertEqual(sherlockAndAnagrams("abba"), 4)
        self.assertEqual(sherlockAndAnagrams("abcd"), 0)
        self.assertEqual(sherlockAndAnagrams("ifailuhkqq"), 3)
        self.assertEqual(sherlockAndAnagrams("kkkk"), 10)
        self.assertEqual(sherlockAndAnagrams("cdcd"), 5)

if __name__ == "__main__":
    unittest.main()

