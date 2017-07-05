class Solution(object):
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        if c == 0:
            return True
        tc = c
        for sqtc in range(int(tc**0.5), 0, -1):
            tc = c
            tc = tc - (sqtc**2)
            if tc == 0:
                return True
            tc -= int(tc**0.5) ** 2
            if tc == 0:
                return True
            sqtc -= 1
        return False

import unittest
class test_solution(unittest.TestCase):
    def test_all(self):
        s = Solution()
        self.assertEqual(s.judgeSquareSum(5), True)
        self.assertEqual(s.judgeSquareSum(3), False)
        self.assertEqual(s.judgeSquareSum(1000), True)
        self.assertEqual(s.judgeSquareSum(0), True)

if __name__ == "__main__":
    unittest.main()
