class Solution:
    def maxSubArray(self, nums):
        dp = [0 for _ in range(len(nums))]
        dp[0] = nums[0]
        for i in range(1, len(nums)):
            dp[i] = max(nums[i], dp[i-1]+nums[i])
        return max(dp)
        
import unittest
class test_solution(unittest.TestCase):
    def test_all(self):
        s = Solution()
        self.assertEqual(s.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]),6)

if __name__ == "__main__":
    unittest.main()
