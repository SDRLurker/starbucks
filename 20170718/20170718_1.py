class Solution:
    def findMaxAverage(self, nums, k):
        max_avg = -10001
        s = 0
        for i in range(len(nums)-k+1):
            if i == 0:
                s = sum(nums[i:i+k])
            else:
                s -= nums[i-1]
                s += nums[i+k-1]
            avg = s / k
            max_avg = max(avg, max_avg)
        return max_avg

import unittest
class test_solution(unittest.TestCase):
    def test_all(self):
        s = Solution()
        self.assertEqual(s.findMaxAverage([1,12,-5,-6,50,3], 4), 12.75)
        self.assertEqual(s.findMaxAverage([1,3,12,-5,-6,50], 4), 12.75)

if __name__ == "__main__":
    unittest.main()
