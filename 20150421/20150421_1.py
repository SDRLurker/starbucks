class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        d = [[0,0] for _ in range(2)];        
        sz = len(nums);
        for i in range(sz):
            d[1][1] = d[0][0] + nums[i]
            d[1][0] = max(d[0][1], d[0][0])
            d[0][1] = d[1][1]
            d[0][0] = d[1][0]
        return max(d[0][0], d[0][1])

import unittest
class test_solution(unittest.TestCase):
    def test_all(self):
        s = Solution()
        self.assertEqual(s.rob([1,2,3,1]), 4)
        self.assertEqual(s.rob([2,7,9,3,1]), 12)

if __name__ == "__main__":
    unittest.main()
