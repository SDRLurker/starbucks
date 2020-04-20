# https://leetcode.com/articles/remove-9/
class Solution:
    def newInteger(self, n):
        ans = ""
        while n:
            ans = str(n%9) + ans
            n //= 9
        return int(ans)

import unittest
class test_solution(unittest.TestCase):
    def test_all(self):
        s = Solution()
        self.assertEqual(s.newInteger(9), 10)
        self.assertEqual(s.newInteger(10), 11)

if __name__ == "__main__":
    unittest.main()
