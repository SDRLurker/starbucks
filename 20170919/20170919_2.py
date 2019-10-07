class Solution:
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        cnt = 1
        for x in range(m+n-2, m-1,-1):
            cnt *= x
        for d in range(n-1,0,-1):
            cnt //= d
        return cnt

import unittest
class test_solution(unittest.TestCase):
    def test_all(self):
        s = Solution()
        self.assertEqual(s.uniquePaths(3, 2), 3)
        self.assertEqual(s.uniquePaths(7, 3), 28)

if __name__ == "__main__":
    unittest.main()
