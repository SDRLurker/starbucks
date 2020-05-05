class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        return nums[len(nums)//2]

import unittest
class test_solution(unittest.TestCase):
    def test_all(self):
        s = Solution()
        self.assertEqual(s.majorityElement([3,2,3]), 3)
        self.assertEqual(s.majorityElement([2,2,1,1,1,2,2]), 2)

if __name__ == "__main__":
    unittest.main()
