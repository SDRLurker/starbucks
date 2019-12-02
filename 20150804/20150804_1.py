class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        cnt_s = {}
        cnt_t = {}
        for c in s:
            cnt_s[c] = cnt_s.get(c, 0) + 1
        for c in t:
            cnt_t[c] = cnt_t.get(c, 0) + 1
        return cnt_s == cnt_t

import unittest
class test_solution(unittest.TestCase):
    def test_all(self):
        s = Solution()
        self.assertEqual(s.isAnagram("anagram", "nagaram"), True)
        self.assertEqual(s.isAnagram("rat", "car"), False)

if __name__ == "__main__":
    unittest.main()
