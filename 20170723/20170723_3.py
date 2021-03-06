class Solution:
    def isPalindrome(self, s):
        if len(s) == 0:
            return False
        for i in range(len(s)//2 + 1):
            if s[i] != s[len(s)-1-i]:
                return False
        return True
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        c = 0
        bsub = ""
        for siz in range(1, len(s)+1):
            bc = 0
            for i in range(len(s)+1-siz): 
                subset = s[i:i+siz]
                if self.isPalindrome(subset):
                    c += 1
                if bsub == subset:
                    bc += 1
                bsub = subset
            if siz == 1 and bc == len(s)-1:
                for p in range(1,bc+1):
                    c += p
                break
        return c

import unittest
class test_solution(unittest.TestCase):
    def test_all(self):
        s = Solution()
        self.assertEqual(s.countSubstrings("abc"), 3)
        self.assertEqual(s.countSubstrings("aaa"), 6)
        self.assertEqual(s.countSubstrings("abba"), 6)
        self.assertEqual(s.countSubstrings("ababab"), 12)
        self.assertEqual(s.countSubstrings("a"*1000), 500500)

if __name__ == "__main__":
    unittest.main()
