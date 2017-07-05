class Solution(object):
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        if c < 0:
            return False
        for i in range(2):
            c = c - (int(c**0.5))**2
            if c == 0:
                return True
        return False

import unittest
class test_solution(unittest.TestCase):
    def test_all(self):
        s = Solution()
        self.assertEqual(s.judgeSquareSum(5), True)
        self.assertEqual(s.judgeSquareSum(3), False)
        self.assertEqual(s.judgeSquareSum(1000), True)

if __name__ == "__main__":
    unittest.main()
