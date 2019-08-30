class Solution(object):
    def arrayPairSum(self, nums):
        nums.sort()
        return sum(nums[::2])

import unittest
class test_solution(unittest.TestCase):
    def test_all(self):
        s = Solution()
        self.assertEqual(s.arrayPairSum([1,4,3,2]), 4)

if __name__ == "__main__":
    unittest.main()
