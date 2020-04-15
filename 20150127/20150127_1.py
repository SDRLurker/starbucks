class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cur_max = nums[0]
        until_max = nums[0]
        for i in range(1, len(nums)):
            cur_max = max(cur_max + nums[i], nums[i])
            until_max = max(until_max, cur_max)
            print(i, cur_max, until_max)
        return until_max

import unittest
class test_solution(unittest.TestCase):
    def test_all(self):
        s = Solution()
        self.assertEqual(s.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]), 6)

if __name__ == "__main__":
    unittest.main()
