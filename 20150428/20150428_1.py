class Solution(object):
    def isHappy(self, n):
        ss = set()
        s = sum([int(d)**2 for d in str(n)])
        while s > 1:
            if s in ss:
                return False
            ss.add(s)
            s = sum([int(d)**2 for d in str(s)])
        return True

import unittest
class test_solution(unittest.TestCase):
    def test_all(self):
        s = Solution()
        self.assertEqual(s.isHappy(19), True)
        self.assertEqual(s.isHappy(116), False)

if __name__ == "__main__":
    unittest.main()
