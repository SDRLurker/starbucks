class Solution:
    def numDecodings(self, s):
        self.cnt = 0
        a = [0 for _ in range(len(s)+1)]
        self.backtrack(a, s, 0)
        return self.cnt
    
    def backtrack(self, a, s, k):
        if self.is_solution(a, s, k):
            self.cnt += 1
        k = k + 1
        c = self.candidate(a, s, k)
        for i in range(len(c)):
            a[k] = c[i]
            self.backtrack(a, s, k)
    
    def candidate(self, a, s, k):
        c = []
        p = a[k-1]
        if 0 <= p < len(s) and s[p] != '0':
            c.append(p+1)
        if 0 <= p < len(s)-1 and 10 <= int(s[p:p+2]) <= 26:
            c.append(p+2)
        return c
            
    def is_solution(self, a, s, k):
        if a[k] == len(s):
            return True

import unittest
class test_solution(unittest.TestCase):
    def test_all(self):
        s = Solution()
        self.assertEqual(s.numDecodings("12"), 2)
        self.assertEqual(s.numDecodings("226"), 3)
        self.assertEqual(s.numDecodings("0"), 0)
        self.assertEqual(s.numDecodings("10"), 1)
        self.assertEqual(s.numDecodings("4757562545844617494555774581341211511296816786586787755257741178599337186486723247528324612117156948"), 589824)

if __name__ == "__main__":
    unittest.main()
