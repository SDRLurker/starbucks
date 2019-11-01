class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        if len(nums) == 0:
            return []
        m = nums[0]
        mi = 0
        win = []
        for i in range(1,k):
            if nums[i] > m:
                m = nums[i]
                mi = i
        win.append(m)
        for i in range(k,len(nums)):
            if mi == i - k:
                m = nums[i-k+1]
                mi = i-k+1
                for ii in range(i-k+1,i):
                    if nums[ii] > m:
                        m = nums[ii]
                        mi = ii
            if nums[i] > m:
                m = nums[i]
                mi = i
            win.append(m)                
        return win

import unittest
class test_solution(unittest.TestCase):
    def test_all(self):
        s = Solution()
        self.assertEqual(s.maxSlidingWindow([1,3,-1,-3,5,3,6,7], 3), [3,3,5,5,6,7])
        self.assertEqual(s.maxSlidingWindow([7,6,5,4,3,2,1], 3), [7,6,5,4,3])
        self.assertEqual(s.maxSlidingWindow([], 0), [])

if __name__ == "__main__":
    unittest.main()
