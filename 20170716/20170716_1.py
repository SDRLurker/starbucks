class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        ma = -10001
        s = 0
        for n in nums[0:k-1]:
            s += n
        for i in range(len(nums)-k+1):
            s += nums[i+k-1]
            a = s / k
            ma = max(ma, a)
            s -= nums[i]
        return ma

import unittest
class test_solution(unittest.TestCase):
    def test_all(self):
        s = Solution()
        self.assertEqual(s.findMaxAverage([1,12,-5,-6,50,3], 4), 12.75)
        self.assertEqual(s.findMaxAverage([1,3,12,-5,-6,50], 4), 12.75)

if __name__ == "__main__":
    unittest.main()
