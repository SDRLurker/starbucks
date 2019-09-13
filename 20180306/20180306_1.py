class Solution:
    def rotatedDigits(self, N):
        cnt = 0
        for i in range(1, N+1):
            n = str(i)
            is_ok_rotate = any([True for c in n if c in ('2','5','6','9')])
            is_not_rotate = any([True for c in n if c in ('3','4','7')])
            if is_ok_rotate and not is_not_rotate:
                cnt += 1
        return cnt

import unittest
class test_solution(unittest.TestCase):
    def test_all(self):
        s = Solution()
        self.assertEqual(s.rotatedDigits(10), 4)
        self.assertEqual(s.rotatedDigits(22), 11)
        self.assertEqual(s.rotatedDigits(33), 15)

if __name__ == "__main__":
    unittest.main()
