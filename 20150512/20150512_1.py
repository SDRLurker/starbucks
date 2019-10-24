class Solution(object):
    def _diff(self, s, t):
        dic = {}
        for i, c in enumerate(s):
            if c in dic and dic[c] != ord(c) - ord(t[i]):
                return False
            dic[c] = ord(c) - ord(t[i])
        return True        
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False        
        return self._diff(s,t) and self._diff(t,s)

import unittest
class test_solution(unittest.TestCase):
    def test_all(self):
        s = Solution()
        self.assertEqual(s.isIsomorphic("egg","add"), True)
        self.assertEqual(s.isIsomorphic("foo","bar"), False)
        self.assertEqual(s.isIsomorphic("paper","title"), True)
        self.assertEqual(s.isIsomorphic("aba","baa"), False)
        self.assertEqual(s.isIsomorphic("ab","aa"), False)

if __name__ == "__main__":
    unittest.main()
