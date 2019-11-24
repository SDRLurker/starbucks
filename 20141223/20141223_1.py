class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return nums.index(max(nums))

import unittest
class test_solution(unittest.TestCase):
    def test_all(self):
        s = Solution()
        self.assertEqual(s.findPeakElement([1,2,3,1]), 2)
        self.assertEqual(s.findPeakElement([1,2,1,3,5,6,4]), 5)

if __name__ == "__main__":
    unittest.main()
