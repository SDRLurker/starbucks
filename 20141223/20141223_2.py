class Solution(object):
    def maximumGap(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 2:
            return 0
        nums.sort()
        diff = [nums[i+1] - nums[i] for i in range(len(nums)-1)]
        return max(diff)
        
import unittest
class test_solution(unittest.TestCase):
    def test_all(self):
        s = Solution()
        self.assertEqual(s.maximumGap([3,6,9,1]), 3)
        self.assertEqual(s.maximumGap([10]), 0)

if __name__ == "__main__":
    unittest.main()
