class Solution(object):
    def plusOne(self, digits):
        plus_lst = [d + 1 if i == len(digits) - 1 else d for i, d in enumerate(digits)]
        for i in range(len(plus_lst)-1,0,-1):
            if plus_lst[i] == 10:
                plus_lst[i-1] += 1
                plus_lst[i] = 0
        if plus_lst[0] == 10:
            plus_lst = [1,0] + plus_lst[1:]
        return plus_lst

import unittest
class test_solution(unittest.TestCase):
    def test_all(self):
        s = Solution()
        self.assertEqual(s.plusOne([1,2,3]), [1,2,4])
        self.assertEqual(s.plusOne([4,3,2,1]), [4,3,2,2])
        self.assertEqual(s.plusOne([9]), [1,0])
        self.assertEqual(s.plusOne([9,9]), [1,0,0])

if __name__ == "__main__":
    unittest.main()
